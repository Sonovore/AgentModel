# Just-in-Time Coordination: Architectural Analysis for AI Agent Systems

## Executive Summary

Just-in-Time (JIT) coordination represents a principled architecture for managing dependencies across complex systems without centralized scheduling. The core insight: **pull-based coordination with minimal buffers creates efficiency through flow optimization while surfacing problems that would otherwise remain hidden.**

For AI agent systems, JIT principles translate to specific architectural decisions about task queuing, context management, and inter-agent coordination:

| Dimension | Push Approach | Pull/JIT Approach |
|-----------|---------------|-------------------|
| **Task assignment** | Orchestrator pushes tasks based on plans | Agents pull tasks when capacity available |
| **Context loading** | Pre-load everything that might be needed | Load context when task requires it |
| **Inter-agent coordination** | Central scheduler synchronizes all agents | Demand signals between agents |
| **Failure response** | Buffer absorbs impact, failure hidden | Failure immediately visible, forces response |

**The central architectural claim:** Agent systems should implement pull-based coordination with deliberate buffer minimization because this creates both operational efficiency and continuous improvement through problem visibility. Systems with large buffers operate more "smoothly" but accumulate hidden dysfunction.

This analysis serves three purposes:
1. **Design framework** for architecting agent systems with appropriate coordination mechanisms
2. **Diagnostic framework** for understanding flow problems and identifying bottlenecks
3. **Efficiency framework** for minimizing waste in agent operations

---

## Part I: The Core Problem JIT Addresses

### The Coordination Challenge

Complex systems face a fundamental coordination problem: **how do independent processes synchronize work without centralized control creating a bottleneck?**

Consider a multi-agent system:
- Agent A produces analysis
- Agent B uses A's analysis to generate code
- Agent C reviews B's code
- Agent D integrates reviewed code

Several coordination approaches exist:

**Centralized Push:**
A central orchestrator creates a plan, assigns all tasks, and manages timing. Every agent reports to the orchestrator, who coordinates all dependencies.

Problems:
- Orchestrator becomes bottleneck
- Plan assumes future conditions known
- Replanning is expensive when conditions change
- Single point of failure

**Fully Decentralized:**
Each agent acts independently, publishing outputs and consuming inputs without coordination.

Problems:
- No guarantee of synchronization
- Race conditions and conflicts
- Duplicated work
- No global optimization

**JIT/Pull-Based:**
Downstream agents signal when they need input. Upstream agents produce in response to signals. Coordination emerges from local interactions.

Benefits:
- No central bottleneck
- Adapts to changing conditions
- Produces only what's needed
- Problems surface immediately

### Why Traditional Approaches Create Waste

**Push Systems Create Speculative Work**

When a central orchestrator pushes tasks based on plans:
- Tasks may become obsolete before completion
- Work may not be needed if earlier stages fail
- Resources allocated to speculation rather than known needs
- Replanning overhead when conditions change

**Example in agents:**
```
Orchestrator pushes:
1. "Agent A: Analyze requirements"
2. "Agent B: Design architecture" (assigned before A completes)
3. "Agent C: Implement module X" (assigned before B completes)

Result: B and C may do speculative work that gets invalidated
when A's analysis reveals different requirements.
```

**Push Systems Hide Problems Through Buffers**

When work queues buffer between stages:
- Upstream problems aren't visible until buffers deplete
- By then, context is lost
- Root cause analysis is difficult
- Multiple downstream processes may be affected

**Example in agents:**
```
Agent A produces 50 outputs queued for Agent B
Agent A starts producing wrong outputs (undetected)
Agent B processes the 50 correct outputs from queue
Agent B starts receiving wrong outputs
Root cause analysis: What changed 50 outputs ago?
```

### The JIT Alternative

JIT addresses these problems through pull-based coordination:

**Produce only when downstream needs:**
- No speculative work
- No wasted effort if earlier stages fail
- Resources allocated to known needs

**Minimal buffers surface problems immediately:**
- Upstream problems visible instantly
- Context preserved for analysis
- Single downstream process affected

The tradeoff: **efficiency and learning vs. short-term resilience.**

---

## Part II: JIT Translation for Agent Systems

### Agent Inventory Categories

"Inventory" in agent systems takes several forms:

**Task Queues**

Tasks waiting to be processed. In push systems, orchestrators may queue many tasks per agent. In pull systems, agents request tasks only when ready.

Measurement: Queue depth, wait time, queue age

**Context Accumulation**

Information loaded into agent context "just in case." Context windows have fixed capacity; pre-loaded context consumes space that may be needed for actual reasoning.

Measurement: Context utilization, unused context ratio

**Cached Results**

Pre-computed results stored for potential reuse. Caching trades storage for computation but cached results can become stale.

Measurement: Cache hit rate, staleness rate, storage cost

**Speculative Outputs**

Agent outputs produced before downstream consumption is confirmed. May be discarded if circumstances change.

Measurement: Output utilization rate, discard rate

### Agent Waste Categories

Applying the seven wastes to agents:

**1. Overproduction** (most costly)

Generating outputs that aren't used:
- Comprehensive analysis when quick answer needed
- Multiple alternatives when one would suffice
- Pre-generating responses for anticipated questions

Detection: Output utilization tracking
Fix: Pull-based task assignment, explicit scope definition

**2. Waiting**

Agent capacity unused while waiting for:
- Input from upstream agents
- Human decisions
- External API responses
- Resource availability

Detection: Agent idle time, blocking frequency
Fix: Parallel task availability, dependency pre-staging

**3. Inventory**

Excess accumulation of:
- Queued tasks
- Pre-loaded context
- Cached results
- Unprocessed inputs

Detection: Queue depths, context utilization, cache age
Fix: Pull-based coordination, JIT context loading, cache expiration

**4. Transportation**

Moving data unnecessarily:
- Routing through intermediary agents
- Format conversions between agents
- Redundant data transfer

Detection: Hop count, transformation count
Fix: Direct agent-to-agent communication, standard formats

**5. Motion**

Agent doing avoidable work:
- Re-reading unchanged files
- Re-computing available results
- Re-establishing context

Detection: Redundant operation tracking
Fix: Change detection, result memoization, context preservation

**6. Overprocessing**

More processing than required:
- Using expensive models for simple tasks
- Deep analysis for trivial decisions
- Verification beyond requirements

Detection: Resource consumption per task type
Fix: Task-appropriate model selection, verification calibration

**7. Defects**

Outputs requiring rework:
- Hallucinations
- Misunderstandings
- Incorrect reasoning
- Format errors

Detection: Rework rate, error rate
Fix: Quality gates, validation, jidoka integration

### Push vs. Pull in Agent Systems

**Push-Based Agent Coordination**

```
Orchestrator
    │
    ├── Pushes task to Agent A
    ├── Pushes task to Agent B
    ├── Pushes task to Agent C
    │
    └── Manages all timing and dependencies
```

Characteristics:
- Central planning determines task assignment
- Tasks assigned based on capacity forecasts
- Dependencies managed through scheduling
- Agents receive work; don't request it

When appropriate:
- Task decomposition known in advance
- Dependencies are predictable
- Environment is stable
- Tasks are independent

**Pull-Based Agent Coordination**

```
Task Source
    │
    ├── Agent A requests → receives task
    │       │
    │       └── Completes → signals downstream
    │
    ├── Agent B receives signal → requests A's output
    │       │
    │       └── Completes → signals downstream
    │
    └── Agent C receives signal → requests B's output
```

Characteristics:
- Agents request work when ready
- Production triggered by downstream demand
- Dependencies managed through signals
- No central scheduling

When appropriate:
- Task requirements emerge during execution
- Dependencies discovered dynamically
- Environment is changing
- Tasks have strong dependencies

**Hybrid: Push-Pull Boundary**

Most practical systems are hybrid:

```
Push Zone                   Pull Zone
    │                           │
Orchestrator pushes        Agents pull
high-level tasks           specific subtasks
    │                           │
    │     Push-Pull Boundary    │
    │                           │
Planning, decomposition    Execution, coordination
```

The boundary location is a strategic choice:
- Push too far: Speculative work, inflexible plans
- Pull too far: No global optimization, local suboptimality

---

## Part III: Where Agents Struggle vs. Excel

### Agent Advantages in JIT Context

**Fast Signal Propagation**

Agents can send and receive signals in milliseconds. Human-based systems require minutes to hours for coordination messages. This enables tighter JIT coupling.

**Consistent Execution**

Agents execute consistently given the same inputs. Process variability---a major JIT challenge---is lower for agents than humans (though not zero due to model nondeterminism).

**Parallel Processing**

Multiple agents can process simultaneously. When one agent signals readiness, multiple downstream agents can respond in parallel.

**Unlimited Patience**

Agents don't experience frustration from waiting. They can handle pull-based coordination that would frustrate human workers with variable wait times.

### Agent Weaknesses in JIT Context

**Demand Estimation**

JIT works best when demand is predictable. Agents cannot reliably estimate future demand patterns. Human judgment is often needed for demand forecasting.

**Quality Variability**

Agent outputs have quality variability (hallucinations, errors) that doesn't exist in physical manufacturing. JIT without quality gates propagates defects quickly.

**Context Constraints**

Physical inventory can be stored indefinitely. Agent context has fixed capacity and time constraints. JIT context loading must account for these limits.

**Recovery Complexity**

In manufacturing, JIT failure means production stops. In agent systems, failure mid-task may leave state that's difficult to recover. Checkpointing adds complexity.

### The Bottleneck Analysis

| JIT Phase | Agent Performance | Bottleneck? |
|-----------|-------------------|-------------|
| Signal generation | Excellent | No |
| Signal reception | Excellent | No |
| Demand response | Good | No |
| Quality assurance | Variable | **Yes** |
| Context management | Constrained | **Yes** |
| Error recovery | Poor | **Yes** |
| Demand forecasting | Poor | **Yes** |

Four bottlenecks emerge:
1. Quality assurance (agent outputs need validation)
2. Context management (fixed capacity requires JIT loading)
3. Error recovery (failures require checkpointing)
4. Demand forecasting (human judgment needed)

---

## Part IV: Design Patterns

### Pattern 1: Pull-Based Task Assignment

**Problem:** Push-based task assignment creates speculative work and hides problems in queues.

**Solution:** Agents request tasks when capacity available.

```markdown
# System Pattern: Pull-Based Task Assignment

## Task Pool
Maintains available tasks with:
- Task ID
- Dependencies (what must complete first)
- Priority
- Requirements (which agents can perform)

## Agent Protocol
When agent completes current work:
1. Signal completion to task pool
2. Request next task
3. Receive task (or wait signal if none available)
4. Begin processing

## Task Pool Protocol
When agent requests task:
1. Check dependencies (are prerequisites complete?)
2. Check priority (which available task is highest priority?)
3. Check requirements (can this agent perform the task?)
4. Assign task or signal "no tasks available"

## Benefits
- No speculative work
- Natural load balancing
- Dependencies respected automatically
- Queue depth = available work, not committed work
```

**CLAUDE.md Integration:**

```markdown
# Task Assignment Protocol

## When You Complete Work
Signal completion with:
- Task ID
- Output location
- Any downstream implications
- Your availability status

## When Requesting Work
Request with:
- Your agent ID
- Your capabilities
- Your current context state
- Any preferences or constraints

## When No Work Available
- Maintain readiness
- Do not speculate on future tasks
- Wait for assignment signal
```

### Pattern 2: JIT Context Loading

**Problem:** Pre-loading context "just in case" wastes context window capacity.

**Solution:** Load context when task requires it, not before.

```markdown
# System Pattern: JIT Context Loading

## Context Categories

### Always Loaded (Minimal)
- CLAUDE.md (agent operating instructions)
- Current task specification
- Immediate dependencies

### Loaded on Demand
- File contents (load when needed for task)
- Prior outputs (load when referenced)
- Documentation (load when ambiguity arises)

### Never Pre-loaded
- "Might be relevant" information
- Context from prior unrelated tasks
- Background information not required

## Loading Protocol

1. **Receive task**
2. **Assess minimum context needed**
   - What files must be read?
   - What prior outputs are referenced?
   - What documentation is required?
3. **Load minimum context**
4. **Begin processing**
5. **Load additional context only if needed**
   - Ambiguity encountered
   - Dependency discovered
   - Scope expanded

## Benefits
- Maximum context available for reasoning
- No wasted capacity on unused context
- Faster task startup (less loading)
- Natural documentation of what was actually needed
```

**CLAUDE.md Integration:**

```markdown
# Context Management

## What to Load Immediately
- Task specification
- Files explicitly mentioned in task
- Dependencies from upstream agents

## What to Load On Demand
- Additional files only when needed for current step
- Documentation only when uncertain
- Prior context only when referenced

## What Not to Load
- "Everything related to X"
- "All files in directory Y"
- Context from prior tasks unless explicitly relevant

## Context Discipline
Before loading additional context, ask:
1. Do I need this for the current step?
2. Have I tried proceeding without it?
3. Is this the minimum I need?
```

### Pattern 3: Kanban Signals Between Agents

**Problem:** Agents need to coordinate without central scheduling overhead.

**Solution:** Implement kanban-style signals between agents.

```markdown
# System Pattern: Agent Kanban

## Signal Types

### Completion Signal
Sent when agent finishes task:
```
{
  type: "completion",
  agent: "agent-id",
  task: "task-id",
  output: "output-location",
  confidence: 0.85,
  downstream_implications: ["list of affected tasks"]
}
```

### Ready Signal
Sent when agent has capacity:
```
{
  type: "ready",
  agent: "agent-id",
  capabilities: ["list of task types"],
  context_available: 0.7,
  constraints: ["any limitations"]
}
```

### Request Signal
Sent when agent needs upstream output:
```
{
  type: "request",
  agent: "agent-id",
  needs: "what is needed",
  for_task: "task-id",
  urgency: "normal|high|critical"
}
```

### Problem Signal
Sent when agent encounters issue:
```
{
  type: "problem",
  agent: "agent-id",
  task: "task-id",
  issue: "description",
  impact: "blocked|degraded|informational",
  context: "relevant state"
}
```

## Signal Processing

### Downstream Receives Completion
- Check if dependencies are now satisfied
- If all dependencies ready, begin or request task
- If not, wait for remaining dependencies

### Upstream Receives Request
- Prioritize requested work
- Signal if cannot fulfill (problem signal)
- Produce and send completion when done

### Orchestrator Receives Problem
- Assess impact
- Route to appropriate response
- Update downstream expectations
```

### Pattern 4: Flow Efficiency Monitoring

**Problem:** Systems optimize for resource efficiency (keeping agents busy) rather than flow efficiency (work completing quickly).

**Solution:** Measure and optimize for flow efficiency.

```markdown
# System Pattern: Flow Efficiency Metrics

## Key Metrics

### Lead Time
Time from task request to task completion
Target: Minimize
Formula: completion_timestamp - request_timestamp

### Cycle Time
Time actively processing (excluding waiting)
Target: Lead time should approach cycle time
Formula: sum(processing_time) for task

### Flow Efficiency
Percentage of lead time spent in active processing
Target: >50% for complex tasks, >80% for simple tasks
Formula: cycle_time / lead_time

### Queue Time
Time tasks spend waiting
Target: Minimize
Formula: lead_time - cycle_time

### Work In Progress (WIP)
Number of tasks in system (not completed)
Target: Minimize (per Little's Law)
Formula: count(tasks where status != completed)

## Monitoring Protocol

1. **Track per-task metrics**
   - Record timestamps at each state transition
   - Calculate lead/cycle/queue time at completion

2. **Track system-level metrics**
   - WIP at regular intervals
   - Throughput (completions per time period)
   - Queue depths at each stage

3. **Alert conditions**
   - Flow efficiency drops below threshold
   - Queue time exceeds threshold
   - WIP exceeds target

## Improvement Process

When flow efficiency is low:
1. Identify where time is spent waiting
2. Trace waiting to root cause
3. Address bottleneck or dependency
4. Measure improvement
```

### Pattern 5: Takt Time Synchronization

**Problem:** Agents producing at different rates create queues or starvation.

**Solution:** Synchronize agent production rates to demand rate.

```markdown
# System Pattern: Agent Takt Time

## Concept
Takt time = Available time / Demand
If users need 100 responses per hour and agents work 60 minutes:
Takt time = 60 min / 100 responses = 0.6 min per response = 36 seconds

## Application

### External Takt (User Demand)
- Measure actual demand rate
- Set system takt to match demand
- Monitor queue depth to detect mismatch

### Internal Takt (Inter-Agent)
- Downstream consumption rate sets upstream takt
- If Agent B consumes 10 outputs/hour, Agent A's takt = 6 min
- Monitor handoff queues to detect mismatch

## Balancing

### When Upstream Too Fast
- Inventory accumulates between agents
- Upstream capacity is wasted
- Options: Reduce upstream capacity, find additional downstream consumers

### When Upstream Too Slow
- Downstream starves
- Lead time increases
- Options: Increase upstream capacity, reduce downstream demand

### When Rates Are Balanced
- Minimal queue between agents
- Steady flow through system
- Optimal resource utilization

## Takt Time Dashboard

| Stage | Takt Target | Actual Rate | Queue Depth | Status |
|-------|-------------|-------------|-------------|--------|
| Input | 36s | 32s | 3 | Fast |
| Process A | 36s | 38s | 0 | Slow |
| Process B | 36s | 35s | 2 | OK |
| Output | 36s | 36s | 0 | OK |

Action: Process A is bottleneck, causing Process B to have queue
```

### Pattern 6: Demand Smoothing (Heijunka)

**Problem:** Variable demand creates peaks and valleys that stress JIT systems.

**Solution:** Smooth demand before it enters the system.

```markdown
# System Pattern: Demand Smoothing

## Why Smooth Demand?

Variable demand causes:
- Peak periods: Queues build, latency increases, errors increase
- Valley periods: Capacity idle, waste

JIT systems are especially sensitive because no buffer absorbs variability.

## Smoothing Techniques

### Time-Based Batching
Collect requests over time window, process as batch
- Trade latency for smoothness
- Appropriate for non-urgent requests

### Priority-Based Routing
- Critical requests: Process immediately
- High priority: Small queue tolerance
- Normal: Batch and smooth
- Low priority: Process when capacity available

### Load Shedding
When demand exceeds capacity:
- Reject lowest priority requests
- Better to fail explicitly than fail slowly
- Preserve capacity for critical work

### Capacity Reservation
Reserve portion of capacity for:
- Critical requests (always available)
- Burst handling (absorb short spikes)
- Recovery work (address backlogs)

## Implementation

```
Incoming Requests
       │
       v
   ┌───────────┐
   │  Classify │
   │  Priority │
   └───────────┘
       │
       ├─ Critical ──> Immediate Processing
       │
       ├─ High ──────> Short Queue (max 3)
       │
       ├─ Normal ────> Batch Queue (process every N minutes)
       │
       └─ Low ───────> Background Queue (process when idle)
```

## Metrics

| Metric | Target | Warning |
|--------|--------|---------|
| Demand coefficient of variation | <0.3 | >0.5 |
| Peak/average ratio | <2x | >3x |
| Shed rate | <5% | >10% |
| Reserved capacity utilization | <80% | >95% |
```

---

## Part V: Failure Mode Taxonomy

### Flow Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| Queue buildup | WIP increasing, lead time increasing | Upstream faster than downstream | Balance rates, add downstream capacity |
| Starvation | Downstream idle, waiting for upstream | Upstream slower than downstream | Add upstream capacity, reduce demand |
| Bullwhip | Upstream demand variability > downstream | Signal amplification through chain | Direct demand visibility, reduce stages |
| Blocking | Agent can't release output, full queue | Downstream not consuming | Implement WIP limits, investigate downstream |

### Coordination Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| Missed signal | Work not started despite dependency ready | Signal not received or processed | Implement signal acknowledgment |
| Stale signal | Work based on outdated information | Signal delayed or not updated | Add timestamps, expiration |
| Signal storm | Too many signals, system overwhelmed | Granularity too fine | Batch signals, increase threshold |
| Deadlock | Multiple agents waiting for each other | Circular dependencies | Dependency analysis, timeout |

### Quality Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| Defect propagation | Downstream errors from upstream defect | No quality gate between stages | Add jidoka-style inspection |
| Fast failure | Errors discovered immediately after output | JIT working correctly (this is good) | Address root cause |
| Slow failure | Errors discovered much later | Quality gate missing or ineffective | Improve detection, add gates |

### Capacity Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| Context exhaustion | Agent can't complete task | Too much context loaded | JIT context loading, task sizing |
| Timeout | Task not completed in time | Takt time violated | Task sizing, capacity planning |
| Thrashing | Agent starting but not completing | Tasks too large, constant context switching | Task sizing, WIP limits |

---

## Part VI: Measurement Framework

### What to Measure

**Flow Metrics**

| Metric | Definition | Target | Warning |
|--------|------------|--------|---------|
| Lead time | Request to completion | Domain-specific | >2x target |
| Cycle time | Active processing time | Minimize | >90% of lead time |
| Flow efficiency | Cycle time / Lead time | >50% | <30% |
| Throughput | Completions per period | Match demand | <80% or >120% of demand |
| WIP | Tasks in progress | Minimize | >2x target |

**Queue Metrics**

| Metric | Definition | Target | Warning |
|--------|------------|--------|---------|
| Queue depth | Tasks waiting at stage | 0-3 | >10 |
| Queue age | Time oldest item waiting | <1 minute | >5 minutes |
| Queue variability | CV of queue depth | <0.5 | >1.0 |

**Synchronization Metrics**

| Metric | Definition | Target | Warning |
|--------|------------|--------|---------|
| Takt deviation | Actual rate vs. takt rate | <10% | >25% |
| Handoff latency | Time from completion to consumption | <1 second | >10 seconds |
| Signal success rate | Signals received / Signals sent | >99% | <95% |

**Efficiency Metrics**

| Metric | Definition | Target | Warning |
|--------|------------|--------|---------|
| Context utilization | Used context / Loaded context | >80% | <50% |
| Output utilization | Used outputs / Produced outputs | >95% | <80% |
| Rework rate | Reworked tasks / Total tasks | <5% | >15% |

### Measurement Implementation

```markdown
# Measurement Protocol

## Per-Task Tracking

At task request:
- Record request_timestamp
- Record requester
- Record task_specification

At task start:
- Record start_timestamp
- Record assigned_agent
- Record initial_context_size

During task:
- Record processing_milestones
- Record context_loads
- Record any waiting periods

At task completion:
- Record completion_timestamp
- Record final_context_size
- Record output_location
- Calculate derived metrics

## Aggregation

Hourly:
- Calculate average lead/cycle/queue times
- Calculate throughput
- Calculate flow efficiency

Daily:
- Analyze trends
- Identify bottlenecks
- Calculate utilization metrics

Weekly:
- Review against targets
- Identify systematic issues
- Plan improvements
```

---

## Part VII: Multi-Agent Implications

### The Cascade Problem

In multi-agent systems, JIT failures compound:

```
Agent A
  │
  └── Produces output slowly (takt violation)
        │
        └── Agent B starves, waits
              │
              └── Agent C starves, waits
                    │
                    └── Final output delayed

Delay amplifies through chain.
```

Without buffers, a single slow agent affects all downstream agents immediately.

### Multi-Agent JIT Architecture

**Principle 1: Minimize chain length**

Each handoff adds:
- Signal latency
- Potential queue delay
- Opportunity for misalignment

Design for minimum necessary stages.

**Principle 2: WIP limits at boundaries**

```markdown
# Multi-Agent Pattern: Boundary WIP Limits

Between each pair of agents:
- Maximum queue depth (e.g., 3 tasks)
- When limit reached, upstream pauses
- Prevents runaway inventory accumulation
- Creates backpressure for natural pacing

Implementation:
Before producing output:
1. Check downstream queue depth
2. If at limit, wait for signal
3. If below limit, produce and signal
```

**Principle 3: Direct demand visibility**

```markdown
# Multi-Agent Pattern: Demand Transparency

All agents see actual end-user demand, not filtered demand.

Benefits:
- Prevents bullwhip amplification
- All agents can anticipate
- Coordination without communication

Implementation:
- Publish demand forecast to all agents
- Update forecast frequently
- Agents adjust rate to match
```

**Principle 4: Parallel paths reduce coupling**

```markdown
# Multi-Agent Pattern: Parallel Paths

Instead of:
A → B → C → D (serial)

Design:
     B
    / \
A →     → D
    \ /
     C

Benefits:
- B and C work in parallel
- Single slow agent has less impact
- Natural load balancing

When applicable:
- Task can be decomposed
- Subtasks are independent
- Results can be merged
```

### Scaling Considerations

**Small Scale (2-5 agents)**
- Direct signals between agents
- Simple kanban cards
- Manual takt balancing
- Low coordination overhead

**Medium Scale (5-20 agents)**
- Central signal bus
- Automated takt calculation
- WIP limits become critical
- Need systematic monitoring

**Large Scale (20+ agents)**
- Hierarchical coordination
- Agent pools rather than individuals
- Statistical demand management
- Capacity planning becomes complex

---

## Part VIII: Integration with Jidoka

JIT and jidoka are the two pillars of the Toyota Production System. They serve complementary purposes:

**JIT**: Ensure the right things arrive at the right time (flow optimization)
**Jidoka**: Ensure problems are surfaced immediately (quality assurance)

### How They Interact

**Without jidoka, JIT efficiently propagates defects:**
- Defective output flows immediately to downstream
- No buffer to catch for inspection
- Errors compound through chain

**Without JIT, jidoka catches problems in batches:**
- Large queue between stages
- Multiple defects before detection
- Problems discovered in clumps

**Together:**
- JIT ensures immediate flow (no hiding in queues)
- Jidoka ensures quality at each step (no defects flowing)
- Problems surface quickly (JIT) and are caught (jidoka)

### Implementation Integration

```markdown
# Integrated JIT + Jidoka Pattern

## At Each Handoff

1. **Producer completes work** (JIT)
2. **Producer validates output** (jidoka self-check)
3. **Producer signals completion** (JIT)
4. **Consumer receives signal** (JIT)
5. **Consumer validates input** (jidoka input check)
6. **If valid, consumer processes** (JIT continues)
7. **If invalid, consumer signals problem** (jidoka escalation)

## Quality Gate Integration

```
Producer → Output → Quality Gate → Consumer
                        │
                        ├── Pass → Flow continues
                        │
                        └── Fail → Stop, escalate, fix
```

## CLAUDE.md Integration

```markdown
# Quality-Aware JIT Protocol

## Before Signaling Completion
Run quality checks:
- Output format correct?
- Output content valid?
- No obvious errors?

If checks pass: Signal completion
If checks fail: Signal problem, do not release output

## Upon Receiving Input
Run input checks:
- Format as expected?
- Content plausible?
- Provenance clear?

If checks pass: Process input
If checks fail: Signal upstream problem, do not process
```
```

---

## Part IX: CLAUDE.md Templates

### Basic JIT Integration

```markdown
# Task Coordination Protocol

## Receiving Work

Wait for task assignment signal.
Do not anticipate or speculate on future work.
When signal received:
1. Acknowledge receipt
2. Load minimum required context
3. Begin processing

## During Work

Process task to completion.
If blocked on dependency:
1. Signal request with specific need
2. Wait for response
3. Do not work around or guess

## Completing Work

When task complete:
1. Validate output (quality check)
2. Signal completion with output location
3. Signal readiness for next task
4. Do not begin next task until assigned

## Context Management

Load context just-in-time:
- Start with task specification only
- Load files when needed for current step
- Unload context no longer needed
- Track what was actually used
```

### Advanced Pull-Based Coordination

```markdown
# Pull-Based Coordination Protocol

## Your Role as Producer

When downstream signals request:
1. Acknowledge request received
2. Assess what is needed
3. Produce requested output
4. Validate output quality
5. Signal completion with output
6. Record production for metrics

## Your Role as Consumer

When you need upstream output:
1. Signal request with specifics:
   - What you need
   - Why you need it
   - Urgency level
2. Wait for completion signal
3. Receive and validate output
4. Signal receipt acknowledgment

## Queue Discipline

Never queue more than 3 pending requests.
If queue full:
- Wait for space before requesting more
- Signal if you're blocking on full queue

## Backpressure Response

If upstream signals they're overwhelmed:
- Reduce request rate
- Prioritize critical requests
- Signal downstream about delay

## Flow Metrics to Report

With each completion, report:
- Task ID
- Start timestamp
- Completion timestamp
- Wait time (if any)
- Processing time
- Context used vs. loaded
```

### Multi-Agent JIT Protocol

```markdown
# Multi-Agent Coordination Protocol

## Signal Types

### READY Signal
Send when available for work:
```
READY | agent_id | capabilities | context_capacity
```

### REQUEST Signal
Send when needing input:
```
REQUEST | agent_id | need | task_id | urgency
```

### COMPLETE Signal
Send when finishing work:
```
COMPLETE | agent_id | task_id | output_location | confidence
```

### PROBLEM Signal
Send when encountering issue:
```
PROBLEM | agent_id | task_id | issue_type | details
```

## Coordination Rules

1. **Never assume** - Always wait for signals
2. **Always acknowledge** - Confirm receipt of signals
3. **Minimize handoffs** - Prefer direct over intermediary
4. **Respect WIP limits** - Don't exceed queue limits
5. **Surface problems immediately** - JIT means no hiding

## When Signals Conflict

If you receive conflicting signals:
1. Signal PROBLEM to orchestrator
2. Wait for resolution
3. Do not attempt to resolve yourself

## Timeout Handling

If signal not received within threshold:
1. Send QUERY for status
2. If no response, signal PROBLEM
3. Do not proceed without acknowledgment
```

---

## Part X: Implementation Roadmap

### Phase 1: Measurement Foundation (Week 1-2)

**Instrumentation**
- [ ] Implement timestamp tracking for all tasks
- [ ] Calculate lead time, cycle time, queue time
- [ ] Create flow efficiency dashboard
- [ ] Baseline current performance

**Visibility**
- [ ] Queue depth visualization
- [ ] WIP tracking
- [ ] Bottleneck identification

### Phase 2: Pull-Based Basics (Week 3-4)

**Task Assignment**
- [ ] Implement pull-based task requests
- [ ] Agent signals readiness
- [ ] Task pool manages assignments
- [ ] Remove push-based assignment

**Context Management**
- [ ] Implement JIT context loading
- [ ] Track context utilization
- [ ] Remove pre-loading patterns

### Phase 3: Signal Infrastructure (Week 5-6)

**Kanban Signals**
- [ ] Define signal types
- [ ] Implement signal bus
- [ ] Add acknowledgment protocol
- [ ] Test failure modes

**WIP Limits**
- [ ] Determine appropriate limits
- [ ] Implement enforcement
- [ ] Add backpressure handling

### Phase 4: Integration and Optimization (Week 7-8)

**Jidoka Integration**
- [ ] Add quality gates at handoffs
- [ ] Integrate problem signals
- [ ] Test JIT + jidoka flow

**Demand Smoothing**
- [ ] Implement priority-based routing
- [ ] Add load shedding
- [ ] Reserve capacity for critical work

### Phase 5: Continuous Improvement (Ongoing)

**Monitoring**
- [ ] Weekly flow efficiency review
- [ ] Monthly takt time calibration
- [ ] Quarterly architecture review

**Optimization**
- [ ] Identify and address bottlenecks
- [ ] Reduce chain length where possible
- [ ] Improve signal efficiency

---

## Part XI: Open Questions

### Coordination Challenges

1. **Where should the push-pull boundary be?** What criteria determine how much planning vs. pulling is appropriate?

2. **How do you handle variable task complexity?** JIT assumes consistent processing time. What happens when complexity varies by 10x?

3. **How do you balance flow efficiency vs. resource efficiency?** Some domains require high resource utilization. How do you reconcile?

### Scaling Challenges

4. **What are the scaling limits of pull-based coordination?** At what agent count does coordination overhead dominate?

5. **How do you maintain demand visibility at scale?** Propagating demand to all agents becomes expensive.

6. **How do you handle agent heterogeneity?** Different agents have different capabilities. How does this affect JIT?

### Quality Challenges

7. **How do you integrate quality checks without blocking flow?** Quality gates add latency. How do you minimize?

8. **How do you handle quality variability in JIT?** Manufacturing quality is consistent. Agent quality varies. What changes?

### Learning Challenges

9. **How do you implement kaizen in agent JIT?** Problems surface but how do you ensure improvement?

10. **How do you measure JIT maturity?** What indicates readiness for tighter coordination?

---

## Part XII: Cross-Model Integration

### Relationship to OODA Loop

JIT and OODA address different aspects of agent operation:

- **OODA**: How agents cycle through observation, orientation, decision, action
- **JIT**: How work flows between agents and system components

Integration point: OODA cycle time affects JIT takt time. If agents cycle slowly, takt must accommodate. OODA optimization enables tighter JIT.

### Relationship to Jidoka

JIT and jidoka are complementary TPS pillars:

- **JIT**: Flow optimization (the right thing at the right time)
- **Jidoka**: Quality assurance (stop when problems occur)

Integration point: JIT without jidoka propagates defects. Jidoka without JIT catches problems in batches. Together they create efficient, high-quality flow.

### Relationship to Shared Mental Models

Effective JIT requires shared understanding:

- Common signal vocabulary
- Shared takt time awareness
- Consistent quality expectations

Integration point: Einheit (shared mental models) enables implicit coordination that reduces JIT overhead. Documentation alignment enables JIT to function.

---

## Sources

### Toyota Production System

- Ohno, Taiichi. "Toyota Production System: Beyond Large-Scale Production." Productivity Press, 1988.
- Toyota Motor Corporation. Official TPS documentation on Just-in-Time principles.
- Toyoda, Kiichiro. Original JIT articulation (1930s).

### Operations Research

- Little, J.D.C. "A Proof for the Queuing Formula: L = λW." Operations Research, 1961.
- Kingman, J.F.C. Queueing theory foundations for variability analysis.
- Hopp and Spearman. "Factory Physics." McGraw-Hill, 2000.

### Lean Thinking

- Womack and Jones. "Lean Thinking." Free Press, 1996.
- Modig and Ahlstrom. "This is Lean." Rheologica Publishing, 2012.

### Supply Chain

- Lee, Padmanabhan, and Whang. "The Bullwhip Effect in Supply Chains." Sloan Management Review, 1997.

### Cross-Reference

- OODA Loop Agent Analysis (this repository)
- Jidoka Agent Analysis (this repository)
- Shared Mental Models (this repository)

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent architecture analysis for Just-in-Time coordination principles
**Status:** Complete architectural analysis

**Related Documents:**
- just-in-time-coordination.md (source research)
- just-in-time-coordination-three-level.md (three-level explanation)
- ooda-loop-agent-analysis.md (template and cross-reference)
- jidoka-automation-with-human-touch-agent-analysis.md (complementary TPS pillar)
