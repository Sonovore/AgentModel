# Error Handling Conventions

**Purpose:** Define consistent error detection, reporting, and recovery patterns based on Jidoka principles.

## Philosophy: Jidoka (Autonomation)

**Core principle:** Build quality in at each step. Detect abnormalities immediately and stop before defects propagate.

**Key insight:** Agents detecting their own errors is more valuable than supervisors catching them later.

## Error Detection

### When to Detect

Agents MUST check for errors:
1. **After every significant operation** (file read, API call, computation)
2. **Before state transitions** (starting new phase, completing task)
3. **On receiving input** (validate all messages, arguments, data)
4. **Periodically during long-running operations** (heartbeat checks)

### What Constitutes an Error

**Errors (STOP immediately):**
- Violated invariants (data in impossible state)
- Missing required resources (file not found, API unreachable)
- Schema validation failures (malformed input)
- Timeout exceeded (operation took too long)
- Conflicting instructions (multiple tasks assigned simultaneously)

**Abnormalities (ESCALATE for guidance):**
- Unexpected but valid states (edge cases)
- Degraded performance (operation slower than normal)
- Partial failures (some items succeeded, some failed)
- Ambiguous instructions (unclear what to do)

**Warnings (LOG but continue):**
- Non-critical resource constraints (low disk space)
- Performance anomalies (unusually high load)
- Deprecated patterns (old style still works)

## Error Reporting Format

All errors MUST use this structured format:

```yaml
message_type: escalation.error
timestamp: "2026-01-20T10:30:00Z"
sender: specialist-code
recipient: orchestrator-main
error_details:
  severity: CRITICAL | HIGH | MEDIUM | LOW
  category: validation | resource | timeout | conflict | invariant
  description: "Clear, actionable description of what went wrong"
  context:
    task_id: CODE-100
    operation: "Reading file src/main.py"
    expected: "File exists and is readable"
    actual: "FileNotFoundError: src/main.py"
  suggested_action: "Verify file path or create missing file"
  can_retry: true | false
  requires_human: true | false
```

## Escalation Tiers

**Tier 1: Self-Recovery**
- Agent detects error
- Agent attempts automatic recovery (retry, fallback)
- If successful, log and continue
- If fails, escalate to Tier 2

**Tier 2: Orchestrator Resolution**
- Agent stops and reports to orchestrator
- Orchestrator attempts resolution (reassign task, provide missing resource)
- If successful, agent resumes
- If fails, escalate to Tier 3

**Tier 3: Tournant (Generalist) Intervention**
- Orchestrator routes to tournant agent
- Tournant attempts workaround or alternative approach
- If successful, task completes via alternate path
- If fails, escalate to Tier 4

**Tier 4: Human Escalation**
- System cannot resolve automatically
- Human receives structured error report
- Human provides resolution or adjustment
- Task resumes or is cancelled

## Stop Conditions

Agents MUST stop immediately (before doing anything else) when:

1. **Schema Validation Fails**
   ```python
   if not validate_schema(message, expected_schema):
       raise ValidationError("Message does not match schema")
   ```

2. **Invariant Violated**
   ```python
   if task.dependencies_complete != len(task.dependencies):
       raise InvariantError("Cannot start task with incomplete dependencies")
   ```

3. **Resource Unavailable**
   ```python
   if not Path(required_file).exists():
       raise ResourceError(f"Required file missing: {required_file}")
   ```

4. **Timeout Exceeded**
   ```python
   if elapsed_time > max_duration:
       raise TimeoutError(f"Operation exceeded {max_duration}s limit")
   ```

5. **Explicit STOP Signal**
   ```python
   if message.message_type == "coord.stop":
       raise StopSignal("Received explicit stop command")
   ```

## Recovery Strategies

### Strategy 1: Retry with Exponential Backoff

Use for: Transient failures (network errors, temporary resource unavailability)

```python
max_retries = 3
backoff_base = 2  # seconds
for attempt in range(max_retries):
    try:
        result = perform_operation()
        return result
    except TransientError as e:
        if attempt < max_retries - 1:
            sleep_time = backoff_base ** attempt
            time.sleep(sleep_time)
        else:
            escalate_error(e, "Max retries exceeded")
```

### Strategy 2: Fallback to Alternative

Use for: Resource conflicts, capability limitations

```python
try:
    result = preferred_method()
except MethodUnavailable:
    result = fallback_method()
```

### Strategy 3: Graceful Degradation

Use for: Non-critical components, optional features

```python
try:
    enhanced_result = perform_with_enhancement()
except EnhancementError:
    basic_result = perform_basic_version()
    log_warning("Enhancement unavailable, using basic version")
    return basic_result
```

### Strategy 4: Escalate for Resolution

Use for: Errors requiring orchestrator intervention

```python
try:
    result = perform_operation()
except UnrecoverableError as e:
    escalation_message = create_escalation(
        severity="HIGH",
        error=e,
        suggested_action="Reassign task to agent with required capability"
    )
    send_to_orchestrator(escalation_message)
    await_resolution()
```

## Error Logging

All errors must be logged with sufficient context for diagnosis:

```python
logger.error(
    "Task execution failed",
    extra={
        "task_id": task.id,
        "agent_id": agent.id,
        "error_type": type(error).__name__,
        "error_message": str(error),
        "operation": "File processing",
        "timestamp": datetime.utcnow().isoformat(),
        "stack_trace": traceback.format_exc(),
        "can_retry": determine_retry_eligibility(error),
        "escalation_tier": determine_tier(error)
    }
)
```

## Preventive Measures

### Input Validation (Always)

```python
def process_message(message: dict) -> None:
    # Validate BEFORE processing
    if not validate_schema(message, MESSAGE_SCHEMA):
        raise ValidationError("Invalid message format")

    if message.get("task_id") not in valid_task_ids:
        raise ValueError(f"Unknown task_id: {message.get('task_id')}")

    # Now safe to process
    perform_task(message)
```

### Pre-Flight Checks (Before Major Operations)

```python
def execute_workflow(workflow: Workflow) -> None:
    # Check all prerequisites BEFORE starting
    check_resources_available(workflow.required_resources)
    check_dependencies_met(workflow.dependencies)
    check_agent_capacity(workflow.estimated_load)

    # All checks passed, proceed
    run_workflow(workflow)
```

### Boundary Conditions (Explicit Limits)

```python
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
MAX_PROCESSING_TIME = 300  # 5 minutes
MAX_RETRY_ATTEMPTS = 3

if file_size > MAX_FILE_SIZE:
    raise ResourceError(f"File too large: {file_size} > {MAX_FILE_SIZE}")
```

## Rationale

- **Prevention > Detection > Resolution** - Catch errors as early as possible
- **Explicit over implicit** - Make error conditions clear
- **Fail fast** - Don't propagate bad state
- **Structured escalation** - Clear path from detection to resolution
- **Graceful degradation** - Partial success better than total failure

## Validation

- Every operation has defined error conditions
- Every error has a recovery strategy
- Every escalation has a designated handler
- All errors are logged with sufficient context
