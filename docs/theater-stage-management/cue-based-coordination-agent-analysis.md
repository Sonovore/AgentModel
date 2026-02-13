# Cue-Based Coordination: Agent Analysis

## Executive Summary

Cue-based coordination from theater stage management provides a framework for designing multi-phase commitment protocols that enable precise triggering of autonomous agents. The model reveals how to separate resource preparation from execution, when to use central orchestration versus autonomous execution, and how to implement acknowledgment protocols that verify readiness before commitment.

This analysis examines how the cue-based model translates to AI agent orchestration, where agents excel versus struggle with multi-phase protocols, critical bottleneck patterns, and practical implementation guidance including CLAUDE.md templates.

---

## Part I: Translation to AI Agent Systems

### The Core Mapping

Theater cue-based coordination concepts map to agent architectures:

| Theater Concept | Agent System Analog |
|-----------------|---------------------|
| Stage manager | Orchestrator agent |
| Technical operator | Specialized execution agent |
| Warning | Resource pre-allocation signal |
| Standby | Execution ready state / commit preparation |
| Go | Execution trigger |
| Acknowledgment ("Copy") | ACK message |
| Cue number (LQ 47) | Task ID |
| Calling script | Workflow definition / orchestration plan |
| Operator cue sheet | Agent task list |
| Self-cue | Event-driven autonomous execution |
| Visual cue | Condition-based trigger |
| Auto-follow | Choreographed task chaining |
| Cluster cue | Synchronized multi-agent execution |
| Headset network | Message bus / communication channel |
| Tech rehearsal | Integration testing |
| Missed cue | Task timeout / execution failure |

### The Three-Phase Protocol for Agents

The warning/standby/go protocol translates directly to agent systems:

**Warning Phase (t-60s): Resource Allocation**
```python
orchestrator.send_warning(
    agent_id="data_processor",
    task_id="task_123",
    estimated_start=60,
    context={
        "task_type": "large_batch",
        "estimated_memory_gb": 8,
        "input_schema": "batch_v2"
    }
)
```

**Agent Response:**
- Begin memory allocation
- Load required models/context
- Pre-fetch input data
- Transition state: `IDLE → PREPARING`
- Return: `{"status": "preparing", "ready_in_seconds": 30}`

**Standby Phase (t-10s): Commitment**
```python
orchestrator.send_standby(
    agent_id="data_processor",
    task_id="task_123",
    payload={
        "input_data": data_reference,
        "parameters": processing_params
    }
)
```

**Agent Response:**
- Validate payload completeness
- Verify resources allocated
- Final readiness check
- Transition state: `PREPARING → READY`
- Return: `{"status": "ready", "can_execute": True}`

**Go Phase (t=0): Execution**
```python
orchestrator.send_go(task_id="task_123")
```

**Agent Response:**
- Immediate execution
- Transition state: `READY → EXECUTING`
- No response expected (already executing)
- Report completion when done

### When to Use Multi-Phase vs. Direct Execution

**Multi-phase (warning/standby/go) when:**
- Task requires expensive resource initialization
- Multiple agents must synchronize
- Human approval gate is needed
- Task is high-stakes/irreversible
- Preparation time significantly improves execution

**Direct execution when:**
- Task is lightweight (< 5 seconds)
- No resource preparation needed
- Task is idempotent/reversible
- Latency is critical
- Task is part of auto-follow chain

---

## Part II: Where Agents Excel

### Perfect Protocol Adherence

Agent orchestrators can implement the three-phase protocol perfectly:

**Capabilities:**
- Never skip warning/standby phases for critical tasks
- Precise timing control (microsecond accuracy vs. human variability)
- Consistent acknowledgment tracking
- Automatic timeout handling
- Perfect syntax adherence (reserved words, message structure)

### High-Volume Cue Management

Stage managers manage ~400 cues per show. Agent orchestrators can manage orders of magnitude more:

**Capabilities:**
- Track thousands of concurrent task states
- Parallel warning/standby across many agents
- Automatic dependency resolution
- Real-time progress tracking across all tasks
- No cognitive load degradation

### Choreographed Auto-Follow Sequences

Agents excel at executing auto-follow chains with precise timing:

```python
chain = AutoFollowChain([
    Task("start", duration=0),
    Wait(2.0),
    Task("step_1", duration=5.0),
    Wait(0.5),
    Task("step_2", duration=3.0),
    Wait(1.0),
    Task("finalize", duration=0)
])

# Single trigger executes entire chain
chain.go()
```

**Advantages over manual calling:**
- Precise timing (no human reaction time variability)
- Complex sequences from single trigger
- Reduced orchestrator cognitive load
- Deterministic execution

### Cluster Synchronization

Agents can implement synchronized multi-agent execution reliably:

```python
cluster = SynchronizedCluster([
    ("agent_a", "task_1"),
    ("agent_b", "task_2"),
    ("agent_c", "task_3")
])

# Warning phase
cluster.warn()

# Standby phase - wait for all ACKs
if cluster.all_ready(timeout=30):
    # Go phase - simultaneous execution
    cluster.go()
else:
    # Handle agents that didn't reach ready state
    cluster.abort()
    cluster.diagnose_failures()
```

**Capabilities:**
- Detect readiness failures before execution
- Prevent partial state changes
- Atomic coordinated actions
- Automatic rollback on failure

---

## Part III: Where Agents Struggle

### Contextual Timing Adjustment

Stage managers adjust cue timing based on performer energy:
- "Actor seems rushed tonight—give them more warning"
- "The scene is dragging—tighten the transitions"

Agents struggle with:
- Inferring appropriate timing from indirect signals
- Adjusting warning/standby intervals dynamically
- Understanding when to deviate from defined timing

**Mitigation:**
- Explicit timing rules based on metrics
- Configurable timing parameters
- Human override for timing adjustments

### Judgment in Failure Recovery

Stage managers make nuanced recovery decisions:
- "Missed cue was minor—continue without"
- "Missed cue was critical—we need to compensate"
- "This is recoverable if we skip the next two cues"

Agents lack the judgment to:
- Assess impact severity
- Choose between recovery strategies
- Make creative compensations

**Mitigation:**
- Pre-defined recovery rules for known failure modes
- Impact severity classification
- Human escalation for novel failures
- Graceful degradation defaults

### Adaptive Acknowledgment Interpretation

Operators acknowledge in various ways:
- "Copy"
- "Standing by"
- "Lights ready"
- Silence followed by execution

Agents may struggle to interpret varied acknowledgment patterns or recognize implicit acknowledgment through action.

**Mitigation:**
- Require structured ACK messages
- Standardized ACK schema
- Timeout-based escalation for missing ACKs

### Visual/Conditional Cue Judgment

Stage managers and operators make visual cue decisions:
- "Actor is almost in position—fire when they hit the mark"
- "The beat isn't quite right—wait for the better moment"

Agents struggle with:
- Subjective timing judgments
- "Feel" of the moment
- Aesthetic decisions

**Mitigation:**
- Convert visual cues to explicit conditions
- Metric-based triggering (position detection, audio analysis)
- Accept that some timing finesse may be lost

---

## Part IV: Bottleneck Identification

### The Orchestrator Calling Bottleneck

Stage managers can call ~1 cue per second sustained, with brief bursts faster. Agent orchestrators have different limits:

**Detection metrics:**
- Dispatches per second (capacity)
- Queue depth of pending dispatches
- Time from task ready to dispatch sent

**Thresholds:**
| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| Dispatch rate | < 100/s | 100-500/s | > 500/s |
| Queue depth | < 10 | 10-50 | > 50 |
| Dispatch latency | < 10ms | 10-100ms | > 100ms |

**Mitigation:**
- Auto-follow chains (reduce individual dispatches)
- Batch dispatches for related tasks
- Hierarchical orchestration (domain orchestrators)
- Async dispatch with acknowledgment

### The Acknowledgment Bottleneck

Waiting for acknowledgments serializes the protocol:

```
WARNING → wait for ACK → STANDBY → wait for ACK → GO
```

If ACK latency is high, throughput suffers.

**Detection metrics:**
- Average ACK latency
- ACK timeout rate
- Time in standby waiting for ACKs

**Mitigation:**
- Parallel acknowledgments for independent tasks
- Timeout with retry
- Skip ACK for trusted fast tasks
- Async ACK tracking

### The Cluster Synchronization Bottleneck

Cluster execution waits for the slowest agent:

```
Agent A ready: 2s
Agent B ready: 5s
Agent C ready: 3s
Cluster ready: 5s (slowest)
```

**Detection metrics:**
- Cluster wait time vs. expected
- Variance in agent readiness times
- Percentage of time waiting on specific agents

**Mitigation:**
- Stagger warnings based on expected readiness time
- Timeout with fallback (proceed without slow agent)
- Agent health monitoring
- Pre-warming slow agents

### The Auto-Follow Chain Bottleneck

Auto-follow chains execute deterministically, but if one step fails, the chain halts:

```
Task 1 → Task 2 → Task 3 (fails) → Task 4 (never executes)
```

**Detection:**
- Chain completion rate
- Point of failure in chains
- Chain abandonment rate

**Mitigation:**
- Optional steps in chains (fail and continue)
- Fallback tasks on failure
- Checkpoints that allow restart
- Maximum failure tolerance

---

## Part V: Optimization Patterns with CLAUDE.md Templates

### Pattern 1: Three-Phase Commitment Protocol

**CLAUDE.md Template:**
```markdown
## Task Commitment Protocol

### Three-Phase Protocol

**Phase 1: WARNING (t - 60s)**
```json
{
  "type": "warning",
  "task_id": "task_123",
  "agent_id": "processor_agent",
  "estimated_start_seconds": 60,
  "context": {
    "task_type": "heavy_computation",
    "required_resources": {...}
  }
}
```

**Agent actions on WARNING:**
- Allocate required resources
- Load context/models
- Pre-fetch data
- Transition: IDLE → PREPARING

**Agent response:**
```json
{
  "type": "warning_ack",
  "task_id": "task_123",
  "status": "preparing",
  "ready_in_seconds": 30
}
```

**Phase 2: STANDBY (t - 10s)**
```json
{
  "type": "standby",
  "task_id": "task_123",
  "payload": {...}
}
```

**Agent actions on STANDBY:**
- Validate payload
- Final readiness check
- Commit to execution
- Transition: PREPARING → READY

**Agent response:**
```json
{
  "type": "standby_ack",
  "task_id": "task_123",
  "status": "ready",
  "can_execute": true
}
```

**Phase 3: GO (t = 0)**
```json
{
  "type": "go",
  "task_id": "task_123"
}
```

**Agent actions on GO:**
- Immediate execution
- Transition: READY → EXECUTING
- No response (already executing)
- Report completion when done

### When to Use Three-Phase

Required:
- Resource-heavy tasks (memory, GPU, external APIs)
- Multi-agent synchronized execution
- Human approval gates
- High-stakes/irreversible operations

Skip warning/standby:
- Lightweight tasks (< 5 seconds)
- Already-prepared agents
- Auto-follow chain steps
- Latency-critical operations
```

### Pattern 2: Acknowledgment Protocol

**CLAUDE.md Template:**
```markdown
## Acknowledgment Protocol

### Required Acknowledgments

**After WARNING:**
```json
{
  "type": "warning_ack",
  "task_id": "task_123",
  "status": "preparing|failed",
  "ready_in_seconds": 30,
  "failure_reason": null  // or reason if failed
}
```

Timeout: 10 seconds
On timeout: Retry once, then escalate

**After STANDBY:**
```json
{
  "type": "standby_ack",
  "task_id": "task_123",
  "status": "ready|not_ready",
  "can_execute": true|false,
  "reason": null  // if not_ready
}
```

Timeout: 5 seconds
On timeout: Do NOT send GO, escalate

**After GO (for non-obvious completions):**
```json
{
  "type": "execution_status",
  "task_id": "task_123",
  "status": "running|complete|failed",
  "result": {...}  // if complete
}
```

Optional for: Tasks with observable output
Required for: Long-running tasks, tasks with invisible output

### ACK Processing

```python
def handle_standby_ack(ack):
    if ack.status == "ready" and ack.can_execute:
        mark_ready(ack.task_id)
        if all_ready(ack.cluster_id):
            send_go(ack.cluster_id)
    elif ack.status == "not_ready":
        handle_not_ready(ack.task_id, ack.reason)
    else:
        handle_unexpected_ack(ack)
```
```

### Pattern 3: Autonomous vs. Orchestrated Execution

**CLAUDE.md Template:**
```markdown
## Execution Mode Selection

### Orchestrated Execution (Stage Manager-Called)

**Use when:**
- Timing is predetermined
- Multiple agents must synchronize
- Orchestrator has visibility into trigger conditions
- Failure would be high-impact
- Preparation time is needed

**Pattern:**
```
ORCHESTRATOR → WARNING → (wait) → STANDBY → (wait) → GO → AGENT EXECUTES
```

### Autonomous Execution (Self-Cue)

**Use when:**
- Agent observes trigger better than orchestrator
- Reactive to environmental changes
- Communication latency would cause unacceptable delay
- Timing varies based on conditions

**Pattern:**
```
AGENT observes condition → AGENT EXECUTES → AGENT reports completion
```

**Configuration:**
```yaml
autonomous_agent:
  trigger_conditions:
    - type: metric_threshold
      metric: queue_depth
      threshold: 100
      action: scale_up
    - type: event
      event: error_detected
      action: alert_and_remediate
  reporting: on_execution  # Report each execution to orchestrator
```

### Hybrid Execution (Followspot Pattern)

**Use when:**
- Autonomous execution needed for responsiveness
- But coordination with orchestrated timeline required

**Pattern:**
```
ORCHESTRATOR sets context → AGENT monitors autonomously →
AGENT executes when condition met (within context) → AGENT reports
```

**Configuration:**
```yaml
hybrid_agent:
  context_from_orchestrator:
    - active_phase: "phase_2"
    - priority_level: "high"
    - constraints: {...}
  autonomous_triggers:
    - condition: metric > threshold
      action: execute_within_context
  reporting: on_execution
```
```

### Pattern 4: Auto-Follow Chains

**CLAUDE.md Template:**
```markdown
## Auto-Follow Configuration

### Chain Definition

```yaml
auto_follow_chain:
  id: "processing_chain"
  trigger: manual  # or condition-based
  steps:
    - task_id: "initialize"
      duration_seconds: 0
      auto_follow: true

    - type: wait
      duration_seconds: 2.0
      auto_follow: true

    - task_id: "process_batch"
      duration_seconds: 30
      auto_follow: true

    - type: wait
      duration_seconds: 1.0
      auto_follow: true

    - task_id: "finalize"
      duration_seconds: 5
      auto_follow: false  # End of chain
```

### Execution

```python
# Single trigger starts entire chain
chain.go()

# Chain executes:
# t=0: initialize starts
# t=0: wait 2s starts
# t=2: process_batch starts
# t=32: wait 1s starts
# t=33: finalize starts
# t=38: chain complete
```

### Error Handling

```yaml
auto_follow_chain:
  on_step_failure:
    - action: retry
      max_retries: 2
    - action: fallback
      fallback_task: "step_fallback"
    - action: skip  # Skip failed step, continue chain
    - action: abort  # Stop entire chain
```

### When to Use

Use auto-follow:
- Deterministic sequences
- Precise timing requirements
- Reduce orchestrator load
- Minimize timing jitter

Don't use auto-follow:
- Adaptive sequences (need decision points)
- Variable timing based on output
- Human approval needed between steps
```

### Pattern 5: Cluster Synchronization

**CLAUDE.md Template:**
```markdown
## Synchronized Cluster Execution

### Cluster Definition

```yaml
synchronized_cluster:
  id: "database_migration"
  agents:
    - agent_id: "db_agent_1"
      task_id: "migrate_shard_1"
    - agent_id: "db_agent_2"
      task_id: "migrate_shard_2"
    - agent_id: "db_agent_3"
      task_id: "migrate_shard_3"
  coordination: simultaneous  # all execute on same GO
  readiness_timeout_seconds: 30
  abort_on_partial_ready: true
```

### Execution Protocol

```python
def execute_cluster(cluster):
    # 1. WARNING to all agents
    for agent, task in cluster.agents:
        send_warning(agent, task)

    # 2. Wait for all warning ACKs
    warning_acks = wait_for_acks(cluster, "warning", timeout=60)
    if not all_success(warning_acks):
        return handle_warning_failure(warning_acks)

    # 3. STANDBY to all agents
    for agent, task in cluster.agents:
        send_standby(agent, task)

    # 4. Wait for all standby ACKs
    standby_acks = wait_for_acks(cluster, "standby", timeout=30)
    if not all_ready(standby_acks):
        return handle_standby_failure(standby_acks)

    # 5. GO to all agents (simultaneously)
    send_go_broadcast(cluster.agents)

    # 6. Wait for completions
    return wait_for_completions(cluster)
```

### Failure Handling

```yaml
cluster_failure_handling:
  on_warning_failure:
    action: abort
    message: "Cannot prepare all agents"

  on_standby_failure:
    action: abort
    message: "Not all agents ready"
    cleanup: release_prepared_agents

  on_partial_execution:
    action: compensate
    strategy: rollback_completed
```

### When to Use

Use cluster sync:
- Atomic multi-agent operations
- All-or-nothing semantics needed
- Cross-agent consistency required

Avoid when:
- Agents can execute independently
- Partial success is acceptable
- One agent's failure shouldn't block others
```

### Pattern 6: Reserved Trigger Words

**CLAUDE.md Template:**
```markdown
## Communication Protocol - Reserved Words

### Reserved Words

**"GO"** - Execution trigger
- ONLY the orchestrator may send "go" messages
- Agents must NEVER include "go" in other messages
- Use alternatives: "proceed", "continue", "start", "begin"

### Message Validation

```python
def validate_agent_message(message, sender_role):
    # "go" is reserved for orchestrator
    if "go" in message.type and sender_role != "orchestrator":
        raise ProtocolViolation("Only orchestrator can send 'go'")

    # Validate message structure
    if not conforms_to_schema(message):
        raise InvalidMessage("Message does not match schema")

    return True
```

### Protocol Enforcement

```yaml
protocol_rules:
  reserved_words:
    - word: "go"
      permitted_senders: ["orchestrator"]
      context: execution_trigger_only

  message_types:
    warning:
      sender: orchestrator
      requires_ack: true
    standby:
      sender: orchestrator
      requires_ack: true
    go:
      sender: orchestrator
      requires_ack: false  # Agent is executing
    ack:
      sender: agent
      types: [warning_ack, standby_ack, execution_status]
```
```

### Pattern 7: Failure Recovery

**CLAUDE.md Template:**
```markdown
## Failure Recovery Protocol

### Failure Classification

**Missed Execution:**
- Task didn't execute when go sent
- Causes: Agent crash, message lost, timeout
- Detection: Execution timeout

**Early Execution:**
- Task executed before go
- Causes: Race condition, protocol violation
- Detection: Execution timestamp < go timestamp

**Wrong Task Executed:**
- Different task than requested
- Causes: Task ID confusion, state corruption
- Detection: Execution result doesn't match request

**Cascade Failure:**
- One failure triggers downstream failures
- Causes: Dependency chain, shared state
- Detection: Multiple correlated failures

### Recovery Actions

```yaml
recovery_rules:
  missed_execution:
    - action: retry
      max_attempts: 2
    - action: failover
      to: alternate_agent
    - action: skip
      if: non_critical
    - action: escalate
      if: critical

  early_execution:
    - action: log_warning
    - action: accept
      if: result_correct
    - action: compensate
      if: result_incorrect

  cascade_failure:
    - action: isolate_failed_branch
    - action: continue_unaffected
    - action: report_partial_completion

  unknown_failure:
    - action: escalate_immediately
    - action: enter_safe_state
```

### Recovery Implementation

```python
def handle_execution_failure(task_id, failure_type, context):
    rule = recovery_rules.get(failure_type)

    for action in rule.actions:
        if action.condition and not evaluate(action.condition, context):
            continue

        if action.type == "retry":
            result = retry_task(task_id, action.max_attempts)
            if result.success:
                return result

        elif action.type == "failover":
            result = execute_on_alternate(task_id, action.to)
            if result.success:
                return result

        elif action.type == "skip":
            log_skipped(task_id)
            return SkipResult()

        elif action.type == "escalate":
            return escalate_to_human(task_id, context)

    return FailureResult(task_id, "All recovery actions exhausted")
```

### Post-Failure Protocol

1. Log failure with full context
2. Continue execution if possible
3. Report degraded state to human
4. Post-mortem: Update recovery rules
```

---

## Part VI: Measurement Framework

### Protocol Effectiveness Metrics

**Warning Phase:**
| Metric | Description | Target |
|--------|-------------|--------|
| Warning-to-ready time | Time from warning to agent ready | < 60s |
| Warning ACK rate | Warnings acknowledged | > 99% |
| Preparation success rate | Agents ready after preparation | > 99% |

**Standby Phase:**
| Metric | Description | Target |
|--------|-------------|--------|
| Standby-to-ready time | Time from standby to ready ACK | < 10s |
| Standby ACK rate | Standbys acknowledged | > 99.9% |
| Ready rate | Agents reporting ready | > 99% |

**Go Phase:**
| Metric | Description | Target |
|--------|-------------|--------|
| Go-to-execution latency | Time from go to execution start | < 100ms |
| Execution success rate | Tasks completing successfully | > 99% |
| Execution timing variance | Variance in execution timing | < 50ms |

### Coordination Metrics

**Cluster synchronization:**
| Metric | Description | Target |
|--------|-------------|--------|
| Cluster formation time | Time to all-ready state | < 30s |
| Cluster success rate | Clusters executing all members | > 99% |
| Cluster timing variance | Variance across members | < 100ms |

**Auto-follow chains:**
| Metric | Description | Target |
|--------|-------------|--------|
| Chain completion rate | Chains completing all steps | > 99% |
| Chain timing accuracy | Actual vs. expected timing | < 1% deviation |
| Step failure rate | Individual steps failing | < 0.1% |

---

## Part VII: Failure Taxonomy

### Protocol Failures

**Type 1: Warning Timeout**
- **Symptom:** Agent doesn't acknowledge warning
- **Cause:** Agent unavailable, message lost
- **Detection:** No ACK within timeout
- **Mitigation:** Retry, health check, failover

**Type 2: Standby Not Ready**
- **Symptom:** Agent reports not ready at standby
- **Cause:** Resources unavailable, preparation failed
- **Detection:** Standby ACK with ready=false
- **Mitigation:** Extend preparation, diagnose cause, abort if cluster

**Type 3: Go Without Execution**
- **Symptom:** Go sent but execution doesn't happen
- **Cause:** Agent crashed, message lost, agent not in ready state
- **Detection:** Execution timeout
- **Mitigation:** Retry go, verify agent state, failover

**Type 4: Premature Execution**
- **Symptom:** Execution before go
- **Cause:** Race condition, protocol violation, auto-follow error
- **Detection:** Execution timestamp < go timestamp
- **Mitigation:** Accept if result correct, compensate otherwise

### Coordination Failures

**Type 5: Cluster Partial Execution**
- **Symptom:** Some agents in cluster execute, others don't
- **Cause:** Go message didn't reach all, agent crashed mid-execution
- **Detection:** Cluster completion missing members
- **Mitigation:** Compensate, rollback completed, retry

**Type 6: Chain Break**
- **Symptom:** Auto-follow chain stops mid-execution
- **Cause:** Step failed, wait timeout, condition not met
- **Detection:** Chain incomplete
- **Mitigation:** Skip failed step, fallback task, abort chain

**Type 7: Synchronization Drift**
- **Symptom:** Cluster members execute at different times
- **Cause:** Network latency variance, clock drift
- **Detection:** Execution timestamp variance
- **Mitigation:** Explicit synchronization barriers, tighter timing

### Recovery Failures

**Type 8: Recovery Loop**
- **Symptom:** Failure → recovery → failure → recovery...
- **Cause:** Underlying issue not resolved by recovery
- **Detection:** Repeated recovery attempts
- **Mitigation:** Limit retries, escalate after N attempts

**Type 9: Cascade Failure**
- **Symptom:** One failure triggers many downstream failures
- **Cause:** Dependency chain, shared state corruption
- **Detection:** Correlated failures, spreading pattern
- **Mitigation:** Circuit breaker, failure isolation, rollback

---

## Part VIII: Multi-Agent Implications

### Design Principles from Cue-Based Coordination

**Principle 1: Separate Preparation from Execution**

Don't send execute commands directly. Separate:
- Resource allocation (Warning)
- Readiness confirmation (Standby)
- Execution trigger (Go)

This enables early failure detection and graceful degradation.

**Principle 2: Central Orchestration for Predetermined, Autonomous for Reactive**

**Orchestrate when:**
- Timing is predetermined
- Multiple agents must synchronize
- Orchestrator has equal or better observability

**Autonomous when:**
- Agent observes trigger better
- Latency is critical
- Timing varies with conditions

**Principle 3: Acknowledgment Verifies Readiness**

Never assume silence means ready:
- Warning → ACK required
- Standby → ACK required with ready status
- Go → ACK optional (execution is the acknowledgment)

**Principle 4: Auto-Follow for Deterministic Sequences**

When timing is deterministic:
- Chain tasks with auto-follow
- Single trigger for entire sequence
- Precise timing without orchestrator overhead

**Principle 5: Cluster for All-or-Nothing**

When partial execution is unacceptable:
- Synchronize cluster with all-ready gate
- Go only when all ACK ready
- Abort if any agent not ready

### Scaling Patterns

**Single orchestrator:**
- Direct three-phase protocol with each agent
- Suitable for < 50 concurrent agents

**Hierarchical orchestration:**
- Domain orchestrators coordinate sub-clusters
- Meta-orchestrator coordinates domains
- Each level has bounded complexity

**Auto-follow for throughput:**
- Chain related tasks
- Reduce individual dispatches
- Improve timing precision

### Anti-Patterns

**Anti-Pattern 1: Direct Execution Without Preparation**
Sending go without warning/standby for resource-heavy tasks.
- Cold start latency
- Unprepared agents fail
- No readiness verification

**Anti-Pattern 2: Assumed Acknowledgment**
Proceeding without explicit ACK.
- Silent failures
- False positive readiness
- Cascading failures

**Anti-Pattern 3: Over-Orchestration**
Using three-phase for every task.
- Overhead for simple tasks
- Unnecessary latency
- Orchestrator bottleneck

**Anti-Pattern 4: Unbounded Retry**
Retrying failures indefinitely.
- Resource exhaustion
- Masking underlying issues
- Never escalating

---

## Part IX: Implementation Recommendations

### Starting Point

1. **Define task criticality levels** - Critical tasks get three-phase; simple tasks get direct execution
2. **Implement acknowledgment from day one** - Build protocol with ACK, not without
3. **Design for failure** - Recovery rules before deployment
4. **Monitor protocol metrics** - Visibility into ACK rates, latencies, failures
5. **Test progressively** - Unit → Integration → System → Stress

### Protocol Implementation Checklist

- [ ] Three-phase protocol defined (warning/standby/go)
- [ ] Acknowledgment messages defined and required
- [ ] Timeout handling for each phase
- [ ] Reserved words enforced in validation
- [ ] Auto-follow chains supported
- [ ] Cluster synchronization implemented
- [ ] Failure recovery rules defined
- [ ] Metrics instrumented
- [ ] Progressive testing completed

### Production Readiness Checklist

- [ ] All task types classified (critical/standard/lightweight)
- [ ] ACK timeout thresholds tuned
- [ ] Recovery rules tested
- [ ] Cascade failure protection implemented
- [ ] Human escalation path defined
- [ ] Monitoring dashboards operational
- [ ] Alerting on protocol failures configured
- [ ] Runbook for common failures documented

---

## Part X: Key Takeaways

### The Core Insight

Cue-based coordination succeeds because it defines a **multi-phase commitment protocol** that separates resource preparation from execution triggering. This separation:

- Enables early failure detection (at warning/standby, not at go)
- Allows graceful degradation (abort before go if not ready)
- Provides synchronization points (all ready before any execute)
- Reduces execution latency (resources pre-allocated)

### Critical Success Factors

1. **Three-phase for critical tasks:** Warning → Standby → Go
2. **ACK required for commitment:** Never assume readiness
3. **Reserved trigger words:** "Go" only from orchestrator
4. **Auto-follow for sequences:** Precise timing, reduced overhead
5. **Cluster for atomic:** All-or-nothing semantics
6. **Autonomous for reactive:** Local observation, immediate response
7. **Recovery rules pre-defined:** Don't improvise under failure

### The Promise

Well-implemented cue-based coordination enables:
- Precise timing across distributed agents
- Early failure detection through multi-phase commitment
- Graceful degradation when agents aren't ready
- Atomic multi-agent operations through cluster synchronization
- High throughput through auto-follow chains
- Resilient operation through defined recovery

Theater has refined cue-based coordination for over a century, coordinating 400+ technical events per show with split-second precision. The principles transfer directly to AI agent orchestration.

---

## Cross-References

### Related Models in This Repository

- **Master Cuelist** (docs/theater-stage-management/master-cuelist.md): The specification that cue-based coordination executes
- **Central Communication Hub** (docs/theater-stage-management/central-communication-hub.md): The hub pattern that enables cue distribution
- **Chain of Command Routing** (docs/kitchen-brigade/chain-of-command-routing.md): Hierarchical communication patterns

### Complementary Patterns

- **Warning/Standby/Go:** The three-phase commitment protocol
- **Auto-Follow:** Choreographed task chaining
- **Cluster Synchronization:** Atomic multi-agent execution
- **Self-Cue:** Autonomous event-driven execution
- **Visual Cue:** Condition-based triggering

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent analysis document for multi-agent architecture research

---

## Sources

### Primary Research

- Cue-Based Coordination deep research document (docs/theater-stage-management/cue-based-coordination.md)

### Stage Management Cue Systems

- Cue (theatrical) - Wikipedia
- Stage Management - Calls and Cans and Comms - TheatreCrafts
- Calling cues? (warning vs standby) - SMNetwork.org
- Running shows and calling cues - Fiveable

### Cue Sheets and Documentation

- Theatre Template: Master Cue Sheet - Theaterish
- The Complete Stage Manager - The Calling Script

### Show Control and Automation

- Cue Sequences - QLab 5 Documentation
- Wait Cues - QLab 5 Documentation
- Show control - Wikipedia

### Multi-Agent Systems Research

- Distributed Systems Coordination - Martin Kleppmann
- Two-Phase Commit Protocol - Distributed Systems literature
- Choreography vs. Orchestration - Microservices patterns
