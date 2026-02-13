# Coordination Protocols

**Purpose:** Define how agents coordinate actions without constant communication.

## Core Principle: Explicit Coordination

Agents coordinate through **documented protocols**, not ad-hoc messaging. When all agents follow the same protocol, coordination is implicit and overhead is minimal.

## Protocol 1: Cue-Based Coordination (WARNING/STANDBY/GO)

**Source:** Theater stage management
**Use case:** Synchronizing multiple agents for coordinated action

### Three-Phase Protocol

**Phase 1: WARNING**
- **Purpose:** Alert agents that coordinated action is coming
- **Timing:** Sent well in advance (30-60 seconds for quick tasks, hours for complex)
- **Agent action:** Begin preparation, gather resources, review instructions
- **Response required:** `ack.warning` within 5 seconds

**Phase 2: STANDBY**
- **Purpose:** Confirm agents are ready and await execution trigger
- **Timing:** Sent when all WARNING acknowledgments received
- **Agent action:** Complete final preparations, enter ready state
- **Response required:** `ack.standby` when ready (agents self-declare readiness)

**Phase 3: GO**
- **Purpose:** Trigger simultaneous execution
- **Timing:** Sent when all STANDBY acknowledgments received
- **Agent action:** Execute immediately
- **Response required:** None (execution is the response)

### Message Format

```yaml
# WARNING message
message_type: coord.warning
cue_id: CUE-100
cue_group: deployment-tasks
target_agents:
  - specialist-build
  - specialist-test
  - specialist-deploy
estimated_go_time: "2026-01-20T14:00:00Z"
preparation_required:
  - "Verify build artifacts ready"
  - "Check test environment availability"
  - "Confirm deployment slots available"

# STANDBY message
message_type: coord.standby
cue_id: CUE-100
target_agents:
  - specialist-build
  - specialist-test
  - specialist-deploy
ready_check:
  - "All preparations complete?"
  - "Resources available?"
  - "Ready to execute on GO?"

# GO message
message_type: coord.go
cue_id: CUE-100
target_agents:
  - specialist-build
  - specialist-test
  - specialist-deploy
```

### Auto-Follow Chains

Some cues automatically trigger subsequent cues:

```yaml
# In cuelist definition
cues:
  - id: CUE-100
    description: "Build application"
    auto_follow: CUE-200  # Automatically trigger next cue when complete

  - id: CUE-200
    description: "Run tests"
    auto_follow: CUE-300

  - id: CUE-300
    description: "Deploy to staging"
    auto_follow: null  # Manual GO required
```

## Protocol 2: Hub-and-Spoke Communication

**Source:** Theater stage management
**Use case:** Centralized information flow, preventing message overload

### Communication Channels

**Channel 1: Status Updates**
- **Direction:** Specialists → Hub
- **Frequency:** On state change
- **Format:** `status.*` messages
- **Purpose:** Keep hub aware of agent state

**Channel 2: Task Assignments**
- **Direction:** Hub → Specialists
- **Frequency:** As needed
- **Format:** `task.*` messages
- **Purpose:** Distribute work to specialists

**Channel 3: Escalations**
- **Direction:** Any → Hub → Appropriate handler
- **Frequency:** On error/abnormality
- **Format:** `escalation.*` messages
- **Purpose:** Route problems to resolution

**Channel 4: Broadcasts**
- **Direction:** Hub → All agents
- **Frequency:** Rare (system-wide events only)
- **Format:** `broadcast.*` messages
- **Purpose:** System-wide notifications

### Routing Rules

```python
def route_message(message: dict) -> str:
    """Determine which channel/handler receives message."""

    # Escalations go to appropriate tier
    if message["message_type"].startswith("escalation."):
        return route_by_severity(message)

    # Status updates go to monitoring
    elif message["message_type"].startswith("status."):
        return "monitoring"

    # Task messages route to assignment logic
    elif message["message_type"].startswith("task."):
        return "task_distributor"

    # Coordination messages route to cue manager
    elif message["message_type"].startswith("coord."):
        return "cue_manager"

    else:
        raise ValueError(f"Unknown message type: {message['message_type']}")
```

### Exception-Based Reporting

Agents only send status when something **changes** or is **abnormal**:

**DO send:**
- State transitions (started, completed, blocked)
- Errors and abnormalities
- Requested status updates (hub asking for current state)

**DON'T send:**
- "Still working" messages
- Periodic heartbeats during normal operation
- Redundant state confirmations

## Protocol 3: Dependency-Based Sequencing

**Source:** Master Cuelist
**Use case:** Ensuring tasks execute in correct order

### Dependency Declaration

```yaml
task:
  id: CODE-300
  description: "Deploy to production"
  dependencies:
    - CODE-100  # Must complete before this starts
    - CODE-200
  conditions:
    - all_dependencies_complete
    - tests_passed
    - approval_received
```

### Execution Rules

1. **Task cannot start** until all dependencies complete
2. **Dependencies are transitive** - if A depends on B, and B depends on C, A implicitly depends on C
3. **Circular dependencies are invalid** - must be detected and rejected
4. **Failed dependency blocks dependent** - if CODE-100 fails, CODE-300 cannot start

### Validation

```python
def validate_task_sequence(tasks: list[Task]) -> bool:
    """Ensure task dependencies are valid."""

    # Check for circular dependencies
    if has_circular_dependency(tasks):
        raise ValueError("Circular dependency detected")

    # Check all dependencies exist
    task_ids = {t.id for t in tasks}
    for task in tasks:
        for dep in task.dependencies:
            if dep not in task_ids:
                raise ValueError(f"Unknown dependency: {dep}")

    return True
```

## Protocol 4: Handoff Between Specialists

**Source:** Station-based specialization
**Use case:** Transferring work between specialized agents

### Handoff Message Format

```yaml
message_type: task.handoff
from_agent: specialist-code
to_agent: specialist-test
task_id: CODE-100
handoff_context:
  work_completed:
    - "Code review completed"
    - "All tests passing"
    - "Documentation updated"
  artifacts_produced:
    - path: "src/feature.py"
      hash: "abc123..."
    - path: "tests/test_feature.py"
      hash: "def456..."
  next_steps:
    - "Run integration tests"
    - "Verify performance benchmarks"
  constraints:
    - "Must complete within 24 hours"
    - "Cannot deploy before QA approval"
```

### Interface Contracts

Each specialist defines what they **require** and what they **provide**:

```yaml
# In agent-code-specialist.yaml
agent:
  id: specialist-code
  requires:
    - task_description
    - acceptance_criteria
    - existing_codebase_context
  provides:
    - implemented_code
    - unit_tests
    - documentation
  handoff_to:
    - specialist-test  # For testing
    - specialist-deploy  # For deployment
```

### Validation at Handoff

```python
def validate_handoff(handoff: dict) -> bool:
    """Ensure handoff meets receiving agent's requirements."""

    receiving_agent = get_agent_config(handoff["to_agent"])

    # Check all required inputs provided
    for required in receiving_agent["requires"]:
        if required not in handoff["handoff_context"]:
            raise ValueError(f"Missing required context: {required}")

    return True
```

## Protocol 5: Conflict Resolution

**Source:** Conflict detection and resolution (ATC)
**Use case:** Multiple agents want same resource or have incompatible plans

### Detection

```python
def detect_conflict(agent1_plan: dict, agent2_plan: dict) -> bool:
    """Check if two agent plans conflict."""

    # Resource conflicts
    if shared_resources(agent1_plan, agent2_plan):
        return True

    # Timing conflicts
    if overlapping_time_windows(agent1_plan, agent2_plan):
        return True

    # Output conflicts
    if same_output_target(agent1_plan, agent2_plan):
        return True

    return False
```

### Resolution Strategies

**Strategy 1: Priority-Based**
- Higher priority agent proceeds
- Lower priority agent waits or is reassigned

**Strategy 2: First-Come-First-Served**
- Agent who claimed resource first proceeds
- Second agent notified and must re-plan

**Strategy 3: Orchestrator Arbitration**
- Both agents escalate to hub
- Orchestrator decides based on global context
- Decision binding on both agents

### Conflict Message Format

```yaml
message_type: escalation.conflict
agents_involved:
  - specialist-A
  - specialist-B
conflict_type: resource | timing | output
resource_in_question: "database-connection-pool"
proposed_resolution: "priority-based"
suggested_winner: specialist-A  # Higher priority task
```

## Rationale

- **Protocols prevent ad-hoc coordination** - Reduces message complexity
- **Explicit phases** - Agents know where they are in coordination
- **Acknowledgment required** - No fire-and-forget messaging
- **Exception-based** - Only communicate changes, not steady state
- **Dependency-aware** - Tasks execute in valid order automatically

## Validation

- All coordination uses documented protocols
- No protocol violations (checked by hub)
- Acknowledgments received for all critical messages
- Dependency graphs are acyclic
