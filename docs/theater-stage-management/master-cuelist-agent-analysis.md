# Master Cuelist: Agent Analysis

## Executive Summary

The Master Cuelist from theater stage management provides a framework for designing workflow specifications that enable precise coordination under uncertainty. The model reveals how to maintain reference stability during continuous revision, implement progressive commitment protocols, and enable intelligent adaptation when execution conditions deviate from plan.

This analysis examines how the Master Cuelist model translates to AI agent orchestration, where agents excel versus struggle with cuelist-based patterns, critical bottleneck identification, and practical implementation guidance including CLAUDE.md templates.

---

## Part I: Translation to AI Agent Systems

### The Core Mapping

Theater Master Cuelist concepts map to agent architectures:

| Theater Concept | Agent System Analog |
|-----------------|---------------------|
| Master Cuelist | Workflow specification / orchestration plan |
| Cue number (LQ 47.5) | Task ID with hierarchical numbering |
| Cue type (LQ, SQ, FQ) | Agent type / capability domain |
| Visual/aural trigger | Condition for task execution |
| Stage manager | Orchestrator agent |
| Technical operator | Specialized execution agent |
| Warning | Pre-allocation signal |
| Standby | Execution-ready state |
| Go | Trigger / dispatch |
| Autofollow cue | Automatic task chaining |
| Paper tech | Workflow design phase |
| Cue-to-cue rehearsal | Integration testing |
| Tech dress | System testing |
| Performance | Production execution |
| Performance report | Execution log / deviation record |
| Prompt book | Complete workflow documentation |

### The Orchestration Challenge

The Master Cuelist solves a specific coordination challenge that maps directly to agent orchestration:

**Theater challenge:**
- 400+ technical events (cues) across multiple departments
- Precise timing requirements (cues must synchronize)
- Variable conditions (actor timing changes nightly)
- Distributed execution (operators can't see each other)
- High reliability (no retakes in front of audience)
- Constant revision during development

**Agent orchestration challenge:**
- Hundreds of tasks across multiple agent types
- Dependency management (tasks must sequence correctly)
- Variable conditions (API latency, data availability)
- Distributed execution (agents operate independently)
- High reliability (production systems can't fail)
- Constant revision during development

The cuelist model addresses both through: **centralized specification with distributed execution, condition-based triggering, and progressive commitment protocols**.

---

## Part II: Where Agents Excel

### Hierarchical Numbering for Reference Stability

Agents excel at maintaining consistent hierarchical numbering schemes:

**Implementation:**
```
Task-100: Original planned task
Task-100.5: Inserted during revision
Task-100.5.3: Further refinement
Task-101: Next original task
```

**Agent advantages:**
- Perfect consistency in numbering scheme application
- No human errors in number assignment
- Automatic detection of collision (duplicate numbers)
- Instant lookup by hierarchical ID
- Automatic preservation of sequence semantics

**Practical benefit:** When Task-100 is referenced in logs, dependencies, and human communication, it remains stable even as Task-100.5 through Task-100.9 are inserted around it.

### Progressive Commitment Protocol

Agents can perfectly implement Warning-Standby-Go:

**Agent protocol:**
```
PLANNED → WARNED → STANDBY → RUNNING → COMPLETE/FAILED

Transitions:
- PLANNED → WARNED: "Task approaching, prepare resources"
- WARNED → STANDBY: "Task imminent, confirm readiness"
- STANDBY → RUNNING: "Execute now"
- RUNNING → COMPLETE/FAILED: "Task finished"
```

**Agent implementation:**

```python
# Orchestrator sends warning
orchestrator.warn(task_id="Task-47",
                  estimated_start_seconds=60,
                  context={"requires_api": "external_service"})

# Agent acknowledges, begins preparation
agent.on_warn(task_id):
    self.load_context(task_id)
    self.preallocate_resources()
    return {"status": "warned", "ready_in_seconds": 30}

# Orchestrator sends standby when conditions approaching
orchestrator.standby(task_id="Task-47")

# Agent confirms execution-ready
agent.on_standby(task_id):
    assert self.resources_ready()
    return {"status": "standby", "ready": True}

# Orchestrator sends go when conditions met
orchestrator.go(task_id="Task-47")

# Agent executes immediately
agent.on_go(task_id):
    return self.execute(task_id)
```

**Benefits:**
- Resource preparation without premature execution
- Readiness verification before commitment
- Clear audit trail of state transitions
- Graceful handling of delays (extend standby without wasted work)

### Condition-Based Triggering

Agents can evaluate complex trigger conditions consistently:

**Instead of time-based:**
```yaml
task_47:
  execute_at: T+300s
```

**Use condition-based:**
```yaml
task_47:
  execute_when:
    all:
      - task_46: completed
      - output_size: ">1MB"
      - error_rate: "<0.01"
      - external_service: available
```

**Agent advantages:**
- Continuous condition monitoring without fatigue
- Complex boolean logic evaluation
- Real-time adaptation to variable conditions
- Explicit documentation of trigger conditions

### Autofollow for Tight Sequences

Agents can implement autofollow (automatic task chaining) precisely:

**Configuration:**
```yaml
task_47:
  action: "Transform data format"
  autofollow:
    - task: task_47.5
      delay_seconds: 3
    - task: task_47.7
      delay_seconds: 5
```

**Execution:**
When Task-47 completes, Task-47.5 automatically triggers after 3 seconds, then Task-47.7 after 5 seconds—no orchestrator intervention required.

**Benefits:**
- Reduces orchestrator load for tight sequences
- Microsecond timing precision (vs. human calling variability)
- Enables complex choreographed sequences from single trigger

### Rich Metadata for Adaptation

Agents can store and utilize comprehensive task metadata:

**Task specification with full metadata:**
```yaml
task_47:
  # Identification
  id: "Task-47"
  type: "data_transformation"
  agent: "transformer_agent"

  # Trigger
  execute_when:
    task_46: completed

  # Execution
  action: "Transform CSV to JSON"
  expected_duration_seconds: 30
  timeout_seconds: 120

  # Coordination
  simultaneous_with: ["Task-48"]
  depends_on: ["Task-46"]
  blocks: ["Task-50", "Task-51"]

  # Intent
  purpose: "Enable downstream JSON processing"
  importance: REQUIRED

  # Contingency
  on_failure:
    - retry: 2
    - fallback: "Task-47-alt"
    - skip_if: importance != REQUIRED
```

This metadata enables intelligent adaptation when conditions deviate.

---

## Part III: Where Agents Struggle

### Trigger Ambiguity Resolution

Human stage managers resolve ambiguous triggers through judgment:
- "On the kiss" becomes precise through observation: when lips touch, when actors separate, when the embrace ends
- "When the door closes" becomes: the moment the door touches frame, when the latch clicks

Agents struggle when trigger conditions are ambiguous:

**Problematic:**
```yaml
execute_when: "task_46 substantially complete"
```

**What is "substantially"?** 80%? 95%? Output looks correct?

**Mitigation:**
- Require precise trigger specifications
- Use measurable conditions only
- Default to explicit thresholds: `task_46.progress >= 95`
- Escalate genuinely ambiguous conditions to human

### Contextual Adaptation

Stage managers adapt cues to actual conditions using contextual judgment:
- Actor rushes: call cue early or skip standby
- Actor late: extend standby, wait for trigger
- Section skipped: assess which cues still needed

Agents lack the contextual understanding for equivalent adaptation:

**Challenge:** Task-46 completed faster than expected. Should Task-47 execute immediately, or wait for the originally planned moment?

**Agent limitation:** Without understanding *why* the timing was planned that way, agents can't make intelligent adaptation decisions.

**Mitigation:**
- Include intent metadata explaining timing rationale
- Define adaptation rules explicitly: "If Task-46 completes early, Task-47 may execute immediately"
- Escalate ambiguous adaptation decisions to human

### Intent Preservation Under Deviation

When the plan encounters reality, stage managers preserve intent:
- The purpose of LQ 47 is to create isolation. If the actor is in a different position than expected, the stage manager may call an alternate cue that achieves isolation differently.

Agents struggle to infer intent and find alternatives:

**Challenge:** Task-47 fails. The purpose was "enable downstream JSON processing." Agent doesn't understand "JSON processing" well enough to find alternatives.

**Mitigation:**
- Explicit intent metadata with alternatives listed
- Contingency branches pre-planned
- Human escalation for failures requiring creative alternatives

### Lifecycle Phase Judgment

Theater explicitly transitions between phases (rehearsal → performance), with different norms for each. Human judgment determines phase appropriateness.

Agents may not recognize phase-inappropriate behaviors:
- Making changes during "production" that introduce instability
- Over-constraining during "development" that prevents learning

**Mitigation:**
- Explicit phase markers in workflow state
- Phase-specific policies enforced programmatically
- Human gates for phase transitions

---

## Part IV: Bottleneck Identification

### The Orchestrator Calling Bottleneck

The stage manager calls all cues. If they can't call fast enough, the show stops.

**Agent equivalent:** The orchestrator dispatches all tasks. If it can't dispatch fast enough, agents idle.

**Detection metrics:**
- Task dispatch queue depth
- Time from task WARNED to task RUNNING
- Agent idle time waiting for dispatch

**Mitigation:**
- Autofollow for tight sequences (reduces orchestrator calling load)
- Parallel dispatch for independent tasks
- Hierarchical orchestration for large workflows

### The Condition Evaluation Bottleneck

Every condition-based trigger requires evaluation. Complex conditions evaluated frequently become bottlenecks.

**Detection metrics:**
- Condition evaluation time
- Condition evaluation frequency
- CPU utilization in orchestrator

**Mitigation:**
- Cache condition results with TTL
- Event-driven condition updates (push, not poll)
- Simplify conditions where possible

### The Metadata Lookup Bottleneck

Rich metadata enables adaptation but requires storage and retrieval.

**Detection metrics:**
- Metadata lookup time
- Metadata size per task
- Memory usage for metadata cache

**Mitigation:**
- Index frequently-accessed metadata
- Lazy loading for rarely-needed metadata
- Partition metadata by lifecycle phase

### The Coordination Overhead Bottleneck

Progressive commitment (Warning-Standby-Go) adds communication overhead. For many rapid tasks, this overhead dominates.

**Detection metrics:**
- Time in WARNING + STANDBY vs. time in RUNNING
- Communication round-trips per task
- Overhead as percentage of task duration

**Mitigation:**
- Skip progressive commitment for fast, low-risk tasks
- Batch warnings/standbys for task groups
- Use autofollow for sequences where individual commitment is unnecessary

### Bottleneck Summary Table

| Bottleneck | Detection Metric | Alert Threshold | Mitigation |
|------------|------------------|-----------------|------------|
| Dispatch | Queue depth | > 10 tasks | Autofollow, parallelism |
| Condition | Evaluation time | > 100ms | Caching, event-driven |
| Metadata | Lookup time | > 50ms | Indexing, lazy loading |
| Coordination | Overhead ratio | > 30% | Skip commitment for fast tasks |

---

## Part V: Optimization Patterns with CLAUDE.md Templates

### Pattern 1: Hierarchical Task Numbering

**CLAUDE.md Template:**
```markdown
## Task Identification

### Numbering Scheme

**Format:** `Task-<major>.<minor>.<patch>`

- **Major:** Integer, assigned during initial planning. Use gaps (100, 200, 300) or increments (10, 20, 30).
- **Minor:** Decimal, assigned when tasks inserted. Use .5 first, then .3, .7 for further insertions.
- **Patch:** Optional, for fine-grained insertions within minor versions.

**Examples:**
- Task-100: Original planned task
- Task-100.5: Inserted during development
- Task-100.5.3: Further refinement
- Task-101: Next original task

### Numbering Rules

1. **Never renumber existing tasks** (preserves reference stability)
2. **Use decimals for insertions** (Task-100.5 between Task-100 and Task-101)
3. **Reserve ranges for phases:**
   - 100-199: Data ingestion
   - 200-299: Transformation
   - 300-399: Validation
   - 400-499: Output

### Reference Stability

Task IDs are referenced by:
- Logs: "Task-100 completed at..."
- Dependencies: "Task-200 depends on Task-100"
- Human communication: "Check output from Task-100"
- Dashboards: "Task-100 success rate"

Renumbering invalidates all references. Decimal insertion preserves them.
```

### Pattern 2: Progressive Commitment Protocol

**CLAUDE.md Template:**
```markdown
## Task State Machine

### States

```
PLANNED → WARNED → STANDBY → RUNNING → COMPLETE
                                    ↘ FAILED
                                    ↘ SKIPPED
```

### State Definitions

**PLANNED:** Task exists in workflow but not yet approaching execution.

**WARNED:** Task execution approaching. Agent should prepare resources.
- Trigger: ~60 seconds before expected execution (configurable)
- Agent action: Load context, preallocate resources
- Agent response: ACK with readiness estimate

**STANDBY:** Task execution imminent. Agent must be ready.
- Trigger: ~10 seconds before expected execution (configurable)
- Agent action: Final preparation, hands on controls
- Agent response: ACK with ready=true/false

**RUNNING:** Task executing.
- Trigger: Conditions met, orchestrator sends GO
- Agent action: Execute task
- Agent response: Progress updates, completion

**COMPLETE/FAILED/SKIPPED:** Terminal states.

### Protocol Messages

**Warning:**
```json
{
  "type": "warn",
  "task_id": "Task-100",
  "estimated_start_seconds": 60,
  "context": {...}
}
```

**Standby:**
```json
{
  "type": "standby",
  "task_id": "Task-100"
}
```

**Go:**
```json
{
  "type": "go",
  "task_id": "Task-100"
}
```

### When to Skip Progressive Commitment

Skip WARNING/STANDBY for:
- Tasks with duration < 5 seconds
- Tasks with no resource preparation needed
- Autofollow sequences (commitment at chain start)
- Emergency/priority tasks (immediate execution)
```

### Pattern 3: Condition-Based Triggers

**CLAUDE.md Template:**
```markdown
## Task Triggers

### Trigger Types

**Dependency-based:** Execute when specified tasks complete.
```yaml
execute_when:
  all:
    - task: Task-100
      state: COMPLETE
    - task: Task-101
      state: COMPLETE
```

**Metric-based:** Execute when metrics meet thresholds.
```yaml
execute_when:
  all:
    - metric: output_size
      comparison: greater_than
      value: 1048576  # 1MB
    - metric: error_rate
      comparison: less_than
      value: 0.01
```

**External-based:** Execute when external conditions met.
```yaml
execute_when:
  all:
    - service: external_api
      state: available
    - resource: gpu_memory
      comparison: greater_than
      value: 8GB
```

**Combined:** Multiple condition types.
```yaml
execute_when:
  all:
    - task: Task-100
      state: COMPLETE
    - metric: queue_depth
      comparison: less_than
      value: 10
    - service: database
      state: available
```

### Condition Evaluation

- Orchestrator evaluates conditions continuously
- State transitions: PLANNED → WARNED when 1+ conditions remaining
- State transitions: WARNED → STANDBY when conditions nearly met
- State transitions: STANDBY → RUNNING when all conditions met

### Never Use

**Time-based triggers without conditions:**
```yaml
# BAD: Fragile to timing variations
execute_at: T+300s
```

Use condition-based triggers that adapt to actual state.
```

### Pattern 4: Autofollow Chains

**CLAUDE.md Template:**
```markdown
## Autofollow Configuration

### Definition

Autofollow chains execute automatically after an initial trigger, without requiring orchestrator intervention for each step.

### Configuration

```yaml
task_100:
  action: "Initial task"
  autofollow:
    - task: task_100.5
      delay_seconds: 3
    - task: task_100.7
      delay_seconds: 2
      condition: "task_100.5.success"
```

### Execution

1. Orchestrator sends GO for Task-100
2. Agent executes Task-100
3. On Task-100 completion, timer starts
4. After 3 seconds, Task-100.5 auto-executes
5. If Task-100.5 succeeds, after 2 more seconds, Task-100.7 auto-executes

### When to Use Autofollow

**Use when:**
- Timing precision matters (computer timing > human calling)
- Sequence is invariant (doesn't need per-step adaptation)
- Orchestrator load is high (reduce calling overhead)
- Steps are tightly coupled (always execute together)

**Don't use when:**
- Adaptation may be needed between steps
- Conditions may change requiring skip/adjustment
- Human oversight needed at each step
- Steps may need independent retry

### Cancellation

If autofollow chain must be interrupted:
```json
{
  "type": "cancel_autofollow",
  "chain_root": "Task-100",
  "reason": "Condition change detected"
}
```

All pending autofollows in chain are cancelled.
```

### Pattern 5: Intent Metadata for Adaptation

**CLAUDE.md Template:**
```markdown
## Task Intent Metadata

### Purpose

Intent metadata enables intelligent adaptation when conditions deviate from plan.

### Schema

```yaml
task_100:
  # Action metadata (what)
  action: "Transform CSV to JSON"

  # Intent metadata (why)
  intent:
    purpose: "Enable downstream JSON processing in Task-200"
    importance: REQUIRED  # REQUIRED, IMPORTANT, OPTIONAL
    alternatives:
      - "Task-100-alt: Modify Task-200 to accept CSV"
      - "Task-100-manual: Human transforms data"

  # Contingency metadata (if failure)
  contingency:
    on_failure:
      - retry: 2
      - fallback: "Task-100-alt"
    on_timeout:
      - escalate: human
    skip_conditions:
      - "importance != REQUIRED AND deadline_critical"
```

### Adaptation Logic

When Task-100 fails:
1. Check `intent.importance`
2. If REQUIRED: Try `contingency.on_failure` (retry, fallback)
3. If still failing: Check `intent.alternatives`
4. If alternatives exist: Evaluate feasibility, execute if viable
5. If no alternatives or all fail: Escalate based on `intent.purpose`

### Required Fields

**Minimum intent metadata:**
```yaml
intent:
  purpose: "Brief description of why this task exists"
  importance: REQUIRED|IMPORTANT|OPTIONAL
```

**Recommended additions:**
- `alternatives`: Other ways to achieve the purpose
- `contingency`: What to do on failure
- `skip_conditions`: When it's OK to skip
```

### Pattern 6: Workflow Lifecycle Phases

**CLAUDE.md Template:**
```markdown
## Workflow Lifecycle

### Phases

**DEVELOPMENT:**
- Rapid revision expected
- Tasks frequently added, removed, reordered
- Execution logs capture improvement opportunities
- Failures are learning opportunities
- Consistency not prioritized

**STAGING:**
- Moderate revision with review
- Changes require approval
- Execution logs capture stability metrics
- Failures trigger investigation
- Consistency becoming important

**PRODUCTION:**
- Minimal revision, requires formal approval
- Changes are rare and conservative
- Execution logs capture incidents
- Failures trigger incident response
- Consistency is critical

### Phase Transitions

**DEVELOPMENT → STAGING:**
- Trigger: Feature complete, ready for integration testing
- Gate: All tasks have intent metadata
- Gate: All critical paths have contingencies
- Gate: Integration tests pass

**STAGING → PRODUCTION:**
- Trigger: Stability metrics met, ready for production
- Gate: X consecutive successful executions
- Gate: Error rate below threshold
- Gate: Human approval

**PRODUCTION → DEVELOPMENT (rollback):**
- Trigger: Critical production failure
- Process: Revert to known-good version
- Post-mortem: Document failure, update workflow

### Phase-Specific Policies

| Policy | DEVELOPMENT | STAGING | PRODUCTION |
|--------|-------------|---------|------------|
| Task addition | Allowed | Review required | Approval required |
| Task modification | Allowed | Review required | Approval required |
| Task removal | Allowed | Review required | Approval required |
| Failure response | Log and continue | Investigate | Incident response |
| Consistency requirement | None | Moderate | Strict |
```

### Pattern 7: Execution Logging (Performance Reports)

**CLAUDE.md Template:**
```markdown
## Execution Logging

### Log Events

**Workflow events:**
```json
{
  "type": "workflow_start",
  "workflow_id": "wf-12345",
  "version": "1.0.0",
  "phase": "PRODUCTION",
  "timestamp": "2024-01-15T14:00:00Z"
}
```

**Task lifecycle events:**
```json
{
  "type": "task_warned",
  "task_id": "Task-100",
  "agent_id": "transformer_1",
  "timestamp": "2024-01-15T14:01:00Z"
}

{
  "type": "task_running",
  "task_id": "Task-100",
  "trigger_conditions": ["Task-99.complete", "queue_depth<10"],
  "timestamp": "2024-01-15T14:02:00Z"
}

{
  "type": "task_complete",
  "task_id": "Task-100",
  "duration_seconds": 45,
  "output_summary": {...},
  "timestamp": "2024-01-15T14:02:45Z"
}
```

**Deviation events:**
```json
{
  "type": "deviation",
  "task_id": "Task-100",
  "expected": "Complete in 30 seconds",
  "actual": "Complete in 45 seconds",
  "reason": "API latency higher than usual",
  "timestamp": "2024-01-15T14:02:45Z"
}
```

**Adaptation events:**
```json
{
  "type": "adaptation",
  "decision": "Delayed Task-200 by 15 seconds",
  "reason": "Task-100 overran expected duration",
  "outcome": "Success—Task-200 had required inputs",
  "timestamp": "2024-01-15T14:02:50Z"
}
```

### Execution Summary

After workflow completes:
```json
{
  "type": "workflow_complete",
  "workflow_id": "wf-12345",
  "duration_seconds": 1847,
  "tasks_total": 47,
  "tasks_complete": 45,
  "tasks_failed": 1,
  "tasks_skipped": 1,
  "deviations": 3,
  "adaptations": 2,
  "timestamp": "2024-01-15T14:30:47Z"
}
```

### Log Analysis

Logs enable:
- **Debugging:** Why did Task-100 fail?
- **Optimization:** Which tasks consistently overrun?
- **Compliance:** Audit trail of all actions
- **Learning:** Patterns across executions
```

---

## Part VI: Measurement Framework

### Cuelist Quality Metrics

**Reference Stability:**
| Metric | Description | Target |
|--------|-------------|--------|
| Renumbering events | Times tasks were renumbered | 0 in production |
| Reference validity | Percentage of references still valid | 100% |
| Decimal depth | Maximum decimal depth (e.g., Task-100.5.3.2) | < 4 |

**Trigger Precision:**
| Metric | Description | Target |
|--------|-------------|--------|
| Trigger ambiguity rate | Triggers requiring human interpretation | < 5% |
| Condition evaluation time | Time to evaluate trigger conditions | < 100ms |
| False trigger rate | Triggers that fire incorrectly | < 1% |

**Adaptation Effectiveness:**
| Metric | Description | Target |
|--------|-------------|--------|
| Deviation rate | Executions diverging from plan | < 20% |
| Successful adaptation rate | Deviations handled without failure | > 95% |
| Escalation rate | Deviations requiring human intervention | < 5% |

### Progressive Commitment Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Warning acknowledgment rate | Warnings acknowledged by agents | > 99% |
| Standby readiness rate | Agents ready when standby sent | > 99% |
| Go-to-execution latency | Time from GO to execution start | < 100ms |
| Commitment overhead | Time in WARN+STANDBY vs. total | < 20% |

### Lifecycle Phase Metrics

| Metric | DEVELOPMENT | STAGING | PRODUCTION |
|--------|-------------|---------|------------|
| Revision frequency | High (daily) | Medium (weekly) | Low (monthly) |
| Failure rate | Acceptable (20%) | Low (5%) | Minimal (<1%) |
| Execution consistency | Not measured | > 80% | > 99% |
| Human interventions | Common | Occasional | Rare |

---

## Part VII: Failure Taxonomy

### Specification Failures

**Type 1: Ambiguous Trigger**
- **Symptom:** Task execution varies across runs; inconsistent timing
- **Cause:** Trigger condition not precisely specified
- **Detection:** Timing variance analysis
- **Mitigation:** Require explicit, measurable trigger conditions

**Type 2: Missing Dependency**
- **Symptom:** Task executes before required input available
- **Cause:** Dependency not declared in specification
- **Detection:** Task failure due to missing input
- **Mitigation:** Dependency analysis, pre-execution validation

**Type 3: Circular Dependency**
- **Symptom:** Tasks deadlocked waiting for each other
- **Cause:** A depends on B, B depends on A (directly or transitively)
- **Detection:** Deadlock detection, dependency graph analysis
- **Mitigation:** Dependency graph validation at specification time

### Commitment Protocol Failures

**Type 4: Warning Timeout**
- **Symptom:** Agent doesn't acknowledge warning
- **Cause:** Agent unavailable, message lost, agent overloaded
- **Detection:** Warning ACK timeout
- **Mitigation:** Retry, agent health check, failover to alternate agent

**Type 5: Standby Not Ready**
- **Symptom:** Agent reports not ready at standby
- **Cause:** Resource preparation incomplete, external dependency unavailable
- **Detection:** Standby ACK with ready=false
- **Mitigation:** Extend preparation time, check resources, defer task

**Type 6: Go Without Acknowledgment**
- **Symptom:** Task dispatched but execution unknown
- **Cause:** Go sent but no execution confirmation
- **Detection:** Execution start timeout
- **Mitigation:** Retry go, verify agent status, failover if needed

### Adaptation Failures

**Type 7: Deviation Without Recovery**
- **Symptom:** Conditions deviate from plan, workflow fails
- **Cause:** No contingency defined, adaptation logic insufficient
- **Detection:** Task failure after deviation
- **Mitigation:** Define contingencies, improve adaptation logic

**Type 8: Inappropriate Adaptation**
- **Symptom:** Adaptation makes situation worse
- **Cause:** Adaptation logic doesn't understand intent
- **Detection:** Downstream failures after adaptation
- **Mitigation:** Richer intent metadata, conservative adaptation defaults

**Type 9: Escalation Timeout**
- **Symptom:** Human escalation sent but no response
- **Cause:** Human unavailable, notification not seen
- **Detection:** Escalation response timeout
- **Mitigation:** Escalation to alternate humans, default actions for timeout

### Lifecycle Failures

**Type 10: Phase Mismatch**
- **Symptom:** Inappropriate behavior for current phase
- **Cause:** Workflow in PRODUCTION but being modified like DEVELOPMENT
- **Detection:** Policy violation
- **Mitigation:** Enforce phase-specific policies, require phase transition approval

---

## Part VIII: Multi-Agent Implications

### Workflow Specification as Shared Contract

The Master Cuelist serves as the contract between orchestrator and agents:

**Orchestrator commits to:**
- Sending warnings with adequate preparation time
- Sending standbys only when conditions are approaching
- Sending go only when conditions are met
- Respecting agent readiness responses
- Following defined contingency paths on failure

**Agents commit to:**
- Acknowledging warnings and preparing resources
- Reporting honest readiness at standby
- Executing immediately on go
- Reporting completion/failure accurately
- Following defined interfaces

### Scaling Patterns

**Single orchestrator:**
- One orchestrator managing all tasks
- Direct progressive commitment with each agent
- Suitable for < 50 concurrent tasks

**Hierarchical orchestration:**
- Meta-orchestrator coordinates phase-level flow
- Phase orchestrators coordinate task-level flow within phases
- Each orchestrator manages bounded complexity

```
Meta-Orchestrator
├── Ingestion Phase Orchestrator
│   ├── Agent 1
│   ├── Agent 2
│   └── Agent 3
├── Transform Phase Orchestrator
│   ├── Agent 4
│   └── Agent 5
└── Output Phase Orchestrator
    ├── Agent 6
    └── Agent 7
```

**Event-driven orchestration:**
- Tasks publish completion events
- Dependent tasks subscribe to conditions
- Orchestrator manages event routing
- Scales better for high-volume, loose coupling

### Anti-Patterns

**Anti-Pattern 1: Time-Based Everything**
Using fixed timestamps instead of condition-based triggers.
- Fragile to timing variations
- Doesn't adapt to actual state
- Fails when upstream tasks are slow

**Anti-Pattern 2: Skip Progressive Commitment Everywhere**
Going directly from PLANNED to RUNNING for all tasks.
- No preparation time
- No readiness verification
- Higher failure rate

**Anti-Pattern 3: Missing Intent**
Task specifications without purpose/intent metadata.
- Can't adapt intelligently
- Can't find alternatives on failure
- Debugging is guesswork

**Anti-Pattern 4: Eternal Development Phase**
Never transitioning to production policies.
- Constant instability
- No consistency guarantees
- Reliability never improves

**Anti-Pattern 5: Renumbering on Insert**
Renumbering all tasks when inserting new ones.
- Breaks all references
- Invalidates logs
- Confuses everyone

---

## Part IX: Implementation Recommendations

### Starting Point

1. **Adopt hierarchical task numbering** from the beginning
2. **Implement progressive commitment** for tasks with preparation needs
3. **Use condition-based triggers** instead of time-based
4. **Require intent metadata** for all tasks
5. **Define lifecycle phases** with explicit transition criteria
6. **Log comprehensively** from the start

### Workflow Specification Checklist

- [ ] All tasks have hierarchical IDs with room for insertion
- [ ] All tasks have explicit trigger conditions (not time-based)
- [ ] All tasks have intent metadata (purpose, importance)
- [ ] Critical tasks have contingency definitions
- [ ] Dependencies are explicit and validated
- [ ] Autofollow chains documented where used
- [ ] Lifecycle phase defined with appropriate policies

### Progressive Commitment Checklist

- [ ] Warning timing appropriate for resource preparation
- [ ] Standby timing appropriate for condition convergence
- [ ] Go triggers immediate execution
- [ ] All states have timeout handling
- [ ] ACK requirements defined for each transition

### Production Readiness Checklist

- [ ] Stability metrics defined and measured
- [ ] Phase transition criteria documented
- [ ] Incident response plan for production failures
- [ ] Rollback procedure defined
- [ ] Execution logging comprehensive

---

## Part X: Key Takeaways

### The Core Insight

The Master Cuelist achieves coordination through **shared specification with distributed execution**. The orchestrator doesn't execute tasks—it provides the temporal trigger that synchronizes distributed agents who execute autonomously within their domains.

This enables:
- Precise coordination without central execution bottleneck
- Adaptation to variable conditions while maintaining structure
- Reference stability under constant revision
- Progressive commitment without premature resource allocation

### Critical Success Factors

1. **Hierarchical numbering preserves references:** Task-100 remains Task-100 forever
2. **Progressive commitment enables preparation:** Warning → Standby → Go
3. **Condition-based triggers adapt to reality:** Execute when conditions met, not at fixed times
4. **Intent metadata enables adaptation:** Understanding *why* enables intelligent deviation handling
5. **Lifecycle phases set expectations:** Development ≠ Production in norms and behaviors
6. **Execution logs capture reality:** Performance reports enable learning and debugging

### The Promise

Well-implemented cuelist patterns enable:
- Coordination of 100+ tasks with precise sequencing
- Adaptation to variable conditions without losing structure
- Stable references across continuous revision
- Progressive commitment without wasted preparation
- Intelligent adaptation when conditions deviate
- Comprehensive audit trail for debugging and learning

The Master Cuelist proves these patterns work under extreme pressure, coordinating 400+ cues across distributed operators, adapted to variable conditions, night after night for the run of a show. The principles transfer directly to AI agent orchestration.

---

## Cross-References

### Related Models in This Repository

- **Cue-Based Coordination** (docs/theater-stage-management/cue-based-coordination.md): The three-phase protocol (Warning-Standby-Go) in detail
- **Central Communication Hub** (docs/theater-stage-management/central-communication-hub.md): How the stage manager coordinates distributed operators
- **Chain of Command Routing** (docs/kitchen-brigade/chain-of-command-routing.md): Hierarchical communication patterns

### Complementary Patterns

- **Warning-Standby-Go:** Progressive commitment protocol
- **Decimal insertion:** Reference-stable numbering
- **Autofollow:** Choreographed task chaining
- **Performance reports:** Execution logging pattern

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent analysis document for multi-agent architecture research

---

## Sources

### Primary Research

- Master Cuelist deep research document (docs/theater-stage-management/master-cuelist.md)

### Stage Management Practice

- Theatre Template: Master Cue Sheet - Theaterish
- Stage Cue in Theater: Examples, Definition, and Advice - Backstage
- Master Cue Sheet - SMNetwork.org

### Calling Protocols

- Cue (theatrical) - Wikipedia
- Running shows and calling cues - Fiveable
- calling cues? (warning vs standby) - SMNetwork.org

### Multi-Agent Systems Research

- Workflow Orchestration Patterns - Temporal.io
- Distributed Task Coordination - Anthropic documentation
- State Machine Design - XState documentation
