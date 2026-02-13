# Flow Management: Architectural Analysis for AI Agent Systems

## Executive Summary

Flow management in air traffic control orchestrates system throughput by controlling the rate at which aircraft enter constrained resources. The surface-level understanding---"slow things down when they get busy"---misses the deeper principle: **flow management is about making irrevocable decisions under uncertainty, accepting that predictions will be wrong, and designing systems that degrade gracefully when they are.**

For AI agent systems, this reframing is powerful. Agents face analogous challenges: API rate limits, context window constraints, budget limits, human attention bottlenecks. The question is not "how fast can agents work?" but "what sustained throughput can be maintained without collapse given uncertainty about capacity?"

| ATC Concept | Agent Equivalent | Key Insight |
|-------------|-----------------|-------------|
| Airport/runway | API endpoint, database, compute resource | Bottleneck determines system throughput |
| Ground delay | Task queuing, admission control | Cheaper to wait before starting than fail mid-execution |
| Airborne delay | Retry loops, timeout waiting, polling | Expensive and often unrecoverable |
| Flow rate | Task submission rate | Must be controlled to avoid collapse |
| Capacity | Rate limits, context window, budget | Stochastic, not fixed |
| Congestion collapse | Retry storms, timeout cascades, memory exhaustion | System throughput drops to near-zero under overload |
| CDM (Collaborative Decision Making) | Coordinated multi-agent scheduling | Information sharing enables better allocation |

**The central claim:** Agent systems should manage throughput based on sustainable capacity under uncertainty, not peak theoretical capacity. Systems that optimize for maximum throughput will periodically collapse; systems that optimize for resilient throughput will be slower on average but never catastrophically slower.

---

## Part I: The Flow Management Framework

### What Practitioners Think They Understand

The surface-level understanding: "When the system is overloaded, slow down inputs until it recovers."

This framing treats flow management as reactive throttling. Wait until problems appear, then back off. It implies that the natural state is maximum throughput, with occasional interventions.

This understanding is dangerously incomplete.

### What Flow Management Actually Is

Flow management is a framework for making irrevocable decisions (task submissions, resource commitments) based on uncertain predictions (future capacity, task requirements) where the feedback loop has significant latency (you learn whether your decision was right only after the cost has been incurred).

The fundamental challenges:

1. **Capacity is stochastic.** You cannot know exact throughput until you try.
2. **Predictions are imperfect.** Weather forecasts are wrong; task estimates are wrong.
3. **Decisions are irrevocable.** Once a plane takes off, it must land somewhere. Once a task begins, some resources are consumed.
4. **Feedback has latency.** By the time you know capacity was insufficient, tasks have already failed.
5. **Objectives conflict.** Throughput vs. latency vs. fairness vs. cost.

The fundamental equation:

```
E[Submit_Rate] ≤ E[Capacity] - f(Var[Capacity], Prediction_Error, Risk_Tolerance)
```

The safety margin isn't constant---it grows with uncertainty and shrinks with risk tolerance. Systems that operate without margin will periodically collapse.

### Why This Matters for Agents

Agent systems that ignore flow management principles exhibit predictable failure modes:

**Failure Mode 1: Congestion collapse**
System overloaded → requests queue → timeouts trigger → retries amplify load → throughput drops to near-zero.

**Failure Mode 2: Cascade delays**
One slow task → dependent tasks wait → their dependents wait → system-wide slowdown.

**Failure Mode 3: Oscillation**
Load detected → aggressive throttling → load clears → throttling lifted → load spikes → repeat.

**Failure Mode 4: Prediction failure**
Estimated capacity ≠ actual capacity → either underutilization (wasted capacity) or overload (failed tasks).

**Failure Mode 5: Local-global misalignment**
Each agent optimizes locally → global system performs poorly → no individual agent is "wrong."

These aren't edge cases. They're the natural consequences of operating without flow management.

---

## Part II: Where Agents Struggle vs. Excel

### Where Agents Struggle

**Struggle 1: Predicting their own resource requirements**

Agents don't know how much context they'll need until they need it. A task that looks simple may require extensive observation; a task that looks complex may be straightforward.

In aviation: flight times are fairly predictable (known routes, known speeds). In agent systems: task completion times are highly variable.

**Struggle 2: Observing system capacity in real-time**

Agents can't directly observe rate limits until they hit them. They can't know if an API will respond slowly until they call it. Capacity is revealed through failure, not measurement.

In aviation: weather radar shows conditions in advance. In agent systems: many constraints are opaque until violated.

**Struggle 3: Coordinating without communication**

Multiple agents submitting to the same API don't know about each other. Each independently decides to retry. Retry storms emerge without any agent intending overload.

In aviation: controllers see all aircraft and can coordinate. In agent systems: decentralized coordination is hard.

**Struggle 4: Making irrevocable decisions under uncertainty**

Agents must commit to actions (start a task, call an API, allocate context) before knowing if resources will be available. Once committed, some cost is sunk.

In aviation: ground delay programs make these tradeoffs explicitly. In agent systems: the tradeoff is often implicit and unmanaged.

### Where Agents Excel

**Excel 1: Fast response to detected conditions**

Once an agent detects overload (rate limit hit, timeout, error), it can respond in milliseconds. Exponential backoff is trivial to implement.

In aviation: communication latency is seconds to minutes. In agent systems: sub-second response is normal.

**Excel 2: Consistent application of policies**

An agent told to always use exponential backoff will always use it. No fatigue, no forgetting, no shortcuts under pressure.

In aviation: human controllers vary. In agent systems: policy compliance is deterministic.

**Excel 3: Parallel execution at scale**

Agents can scale to thousands of concurrent instances. The coordination challenge is managing scale, not achieving it.

In aviation: controller capacity limits parallel operations. In agent systems: parallelism is cheap.

**Excel 4: Perfect memory of recent history**

Within a session, agents remember every request and response. They can track exact patterns of success and failure.

In aviation: humans have limited working memory. In agent systems: perfect short-term recall.

### The Asymmetry

| Capability | Humans | Agents |
|------------|--------|--------|
| Predict task requirements | Moderate (experience-based) | Poor (high variance) |
| Observe capacity | Good (instruments, communication) | Poor (opaque until failure) |
| Coordinate | Good (explicit communication) | Poor (decentralized) |
| Respond to signals | Slow (seconds) | Fast (milliseconds) |
| Apply policy consistently | Variable | Perfect |
| Scale | Limited | Unlimited |

**The implication:** Agent flow management should rely less on prediction and coordination, more on fast response and consistent policy.

---

## Part III: Bottleneck Identification

### The Theory of Constraints Applied

Any system has at least one bottleneck. Improving non-bottleneck components doesn't improve system throughput.

For agent systems, common bottlenecks:

**Bottleneck 1: API rate limits**

External APIs impose rate limits. Exceeding them causes failures and potentially bans.

| API | Typical Limit | Characteristic |
|-----|---------------|----------------|
| LLM APIs | Tokens/minute, requests/minute | Often tiered, soft limits |
| Database | Connections, queries/second | Hard limits, cascade on exceed |
| External services | Requests/second, daily quota | Variable enforcement |

**Bottleneck 2: Context window**

Agents have finite context. Large tasks exceed capacity, causing information loss.

The autocompact problem: when context is exceeded, the agent loses state mid-task, forcing restart or degraded completion.

**Bottleneck 3: Human attention**

Human-in-the-loop workflows are constrained by human review capacity.

```
Agent_Throughput_With_Human = min(Agent_Capacity, Human_Review_Capacity)
```

If agents can produce 100 tasks/hour but humans can review 10/hour, human capacity is the bottleneck.

**Bottleneck 4: Budget**

API costs constrain total throughput. Even if rate limits allow more, budget may not.

```
Budget_Constrained_Throughput = Budget / Cost_Per_Task
```

**Bottleneck 5: Coordination overhead**

Multi-agent systems spend resources coordinating. As agent count grows, coordination overhead can dominate productive work.

```
Effective_Work = Total_Work - Coordination_Overhead
```

For N agents, coordination overhead often grows as O(N^2) in naive implementations.

### Identifying the System Bottleneck

**Method 1: Measure queue depths**

The bottleneck will have the longest queue. If API requests queue while human review is instant, API is the bottleneck.

**Method 2: Vary capacity**

Increase capacity at one point. If system throughput increases, that was the bottleneck. If not, it wasn't.

**Method 3: Observe failure modes**

What fails first under load? That's likely the bottleneck.

**Method 4: Track utilization**

The bottleneck will be at 100% utilization while other components are below.

### The Moving Bottleneck Problem

Fixing one bottleneck reveals the next. The bottleneck moves.

```
Initial: API rate limit (100 req/min)
Fix: Upgrade API tier (1000 req/min)
New bottleneck: Human review (50 reviews/hour)
Fix: Batch reviews, hire more reviewers
New bottleneck: Budget ($1000/day)
...
```

Flow management must be bottleneck-aware, continuously adapting as constraints shift.

---

## Part IV: Optimization Patterns

### Pattern 1: The Ground Delay Principle

**ATC Version:** It's cheaper to delay aircraft on the ground than in the air. Ground delays transfer costs from expensive (airborne holding) to cheap (gate waiting).

**Agent Version:** It's cheaper to queue tasks before starting than to fail mid-execution. The cost of a failed task includes all resources consumed before failure, plus recovery costs, plus delay from restart.

**Implementation:**

```markdown
# Flow Management Protocol (CLAUDE.md)

## Before Starting a Task

1. Check current system state:
   - API rate limit headroom
   - Context window availability
   - Budget remaining
   - Human review queue depth

2. If any resource is constrained:
   - Queue the task rather than starting
   - Log the constraint
   - Retry after backoff period

3. Never start a task you can't finish:
   - Estimate required context
   - Verify budget is sufficient
   - Confirm dependencies are ready
```

**The tradeoff:** Aggressive queuing increases latency for individual tasks but prevents system-wide failure.

### Pattern 2: Admission Control

**ATC Version:** Ground Delay Programs decide which aircraft depart and when, based on predicted destination capacity.

**Agent Version:** Admission control decides which tasks start and when, based on predicted resource availability.

**Implementation:**

```python
class AdmissionController:
    def __init__(self, capacity_estimator):
        self.capacity = capacity_estimator
        self.work_in_progress = 0

    def admit(self, task):
        estimated_load = task.estimate_load()
        available_capacity = self.capacity.current() - self.work_in_progress

        if estimated_load > available_capacity:
            return False  # Reject/queue

        self.work_in_progress += estimated_load
        return True  # Admit

    def complete(self, task, actual_load):
        self.work_in_progress -= task.estimate_load()
        self.capacity.update(actual_load)  # Learn from actual
```

**Key design decisions:**
- How to estimate task load?
- How to estimate current capacity?
- What to do with rejected tasks?
- How to update estimates from actuals?

### Pattern 3: Backpressure

**ATC Version:** When an airport is overloaded, upstream airports delay departures. Congestion signals propagate backward through the network.

**Agent Version:** When a component is overloaded, upstream producers slow down. Overload at any point throttles the entire pipeline.

**Implementation:**

```markdown
# Backpressure Protocol (CLAUDE.md)

## When Downstream Is Slow

If a dependency (API, database, human review) is responding slowly:

1. Do NOT keep submitting at full rate
2. Reduce submission rate proportionally to slowdown
3. If slowdown persists, halt new submissions
4. Resume gradually when downstream recovers

## Signals of Downstream Overload

- Response latency increasing
- Error rate increasing
- Queue depth at downstream increasing
- Rate limit warnings received
```

**The TCP/AIMD analogy:**

- **Additive Increase:** When succeeding, increase rate slowly (linear)
- **Multiplicative Decrease:** When failing, decrease rate quickly (multiplicative)

This converges to fair allocation among competing flows without explicit coordination.

### Pattern 4: Circuit Breaker

**ATC Version:** When conditions are unsafe (weather, equipment failure), airspace is closed entirely. No traffic allowed until conditions improve.

**Agent Version:** When a component is failing, stop calling it entirely. Allow time for recovery before retrying.

**Implementation:**

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_time=60):
        self.failure_count = 0
        self.threshold = failure_threshold
        self.recovery_time = recovery_time
        self.state = "CLOSED"  # CLOSED = allow, OPEN = block
        self.opened_at = None

    def call(self, func, *args):
        if self.state == "OPEN":
            if time.time() - self.opened_at > self.recovery_time:
                self.state = "HALF-OPEN"  # Allow one test call
            else:
                raise CircuitOpenError()

        try:
            result = func(*args)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            if self.failure_count >= self.threshold:
                self.state = "OPEN"
                self.opened_at = time.time()
            raise
```

**When to use:**
- Dependency is frequently failing
- Failures are not immediately recoverable
- Continued calling makes things worse (retry storms)

### Pattern 5: Load Shedding

**ATC Version:** When severely overloaded, flights are cancelled entirely. Some traffic is sacrificed to maintain system viability.

**Agent Version:** When severely overloaded, low-priority tasks are rejected or cancelled. System remains functional for high-priority work.

**Implementation:**

```markdown
# Load Shedding Protocol (CLAUDE.md)

## Priority Classes

1. **Critical:** Must complete (user-blocking, time-sensitive)
2. **High:** Should complete (important but not blocking)
3. **Normal:** Will complete if resources allow
4. **Low:** Best-effort, may be dropped

## Shedding Rules

When system load > 80% of capacity:
- Stop accepting Low priority tasks
- Log shedding events

When system load > 95% of capacity:
- Stop accepting Normal priority tasks
- Alert human operator

When any component failing:
- Only accept Critical tasks
- Queue High for later
- Drop Normal and Low
```

**The tradeoff:** Some tasks are sacrificed to maintain system viability. Better to complete 80% of tasks than to collapse trying to complete 100%.

### Pattern 6: Multi-Scale Planning

**ATC Version:** Strategic (hours), tactical (minutes), reactive (seconds) planning layers, each constraining the next.

**Agent Version:** Strategic (session), tactical (task), reactive (action) planning layers.

**Implementation:**

```markdown
# Multi-Scale Flow Management (CLAUDE.md)

## Strategic (Session Level)

At session start:
- Assess total work to be done
- Estimate required resources
- Identify likely bottlenecks
- Set session-level budget/limits

## Tactical (Task Level)

Before each task:
- Check strategic budget remaining
- Verify task fits in remaining capacity
- Adjust task scope if needed
- Report progress to strategic layer

## Reactive (Action Level)

For each API call/operation:
- Apply exponential backoff on failure
- Track per-operation success rates
- Escalate patterns to tactical layer
- Hard stop if limits exceeded
```

**The coupling problem:** Strategic decisions constrain tactical options. But tactical outcomes should inform strategic replanning. Build feedback loops.

---

## Part V: Measurement Framework

### What to Measure

**Throughput Metrics:**

| Metric | Definition | Target |
|--------|------------|--------|
| Task completion rate | Tasks completed / time | Stable, not maximized |
| Effective throughput | Completed / (Completed + Failed) | >95% |
| Queue depth | Tasks waiting to start | Stable, not growing |
| Wait time | Time from submission to start | Predictable |

**Capacity Metrics:**

| Metric | Definition | Warning Sign |
|--------|------------|--------------|
| API utilization | Requests / Rate limit | >80% = danger zone |
| Context utilization | Used / Available | >90% = autocompact risk |
| Budget burn rate | Cost / Time | Exceeding plan |
| Human queue depth | Awaiting review | Growing unboundedly |

**Failure Metrics:**

| Metric | Definition | Action |
|--------|------------|--------|
| Error rate | Errors / Requests | >5% = investigate |
| Retry rate | Retries / Attempts | >20% = likely overload |
| Timeout rate | Timeouts / Requests | Any = likely problem |
| Circuit breaker trips | Trips / Period | Any = investigate |

### Early Warning Signs

**Sign 1: Queue depth growing**
Tasks waiting faster than completing. Collapse imminent if trend continues.

**Sign 2: Latency variance increasing**
Some requests fast, some slow. System becoming unstable.

**Sign 3: Error rate increasing**
Not yet collapsed, but approaching limits.

**Sign 4: Retry rate increasing**
System compensating for failures. Additional load making things worse.

**Sign 5: Utilization at limits**
No headroom for variance. Any spike will cause failure.

### Dashboards and Alerts

```markdown
# Flow Management Dashboard (Template)

## Current State
- Throughput: [current] tasks/hour ([trend] vs. last hour)
- Error rate: [current]% ([trend])
- Utilization: API [x]%, Context [y]%, Budget [z]%
- Queue depth: [n] tasks waiting

## Health Indicators
- [ ] All error rates < 5%
- [ ] All utilizations < 80%
- [ ] Queue depth stable
- [ ] No circuit breakers open

## Alerts (last 24h)
- [timestamp]: [event]
- ...
```

---

## Part VI: Failure Taxonomy

### Failure Mode 1: Congestion Collapse

**What it is:** System throughput drops to near-zero despite high demand.

**Mechanism:**
1. Load increases
2. Some requests start failing/timing out
3. Clients retry failed requests
4. Retries add to load
5. More failures trigger more retries
6. Positive feedback loop until collapse

**In aviation:** Controller overload → increased spacing → reduced throughput → more aircraft waiting → more workload.

**In agents:** API overload → errors/timeouts → retries → more overload → near-total failure.

**Detection:**
- Error rate spiking
- Throughput dropping while demand constant
- Retry rate > 50%

**Prevention:**
- Exponential backoff with jitter
- Circuit breakers
- Admission control
- Load shedding

**Recovery:**
- Stop all new submissions
- Wait for in-flight requests to clear
- Gradually resume at reduced rate
- AIMD back to normal

### Failure Mode 2: Cascade Delays

**What it is:** One slow component delays everything downstream.

**Mechanism:**
1. Component A slows down
2. Tasks waiting for A accumulate
3. Dependent tasks (B, C, D) can't start
4. Their dependents also wait
5. System-wide slowdown

**In aviation:** Weather at hub airport → connecting flights delayed → delays propagate through network.

**In agents:** Slow API → tasks waiting → dependent tasks waiting → everything waiting.

**Detection:**
- Localized latency increase spreading
- Dependency graph showing single slow node
- Queue depths growing at dependent components

**Prevention:**
- Timeout bounds on all dependencies
- Fallback paths for critical dependencies
- Bulkheads (isolation) between subsystems
- Graceful degradation (proceed without slow dependency)

**Recovery:**
- Identify bottleneck component
- Either fix or bypass
- Clear accumulated queues
- Resume normal flow

### Failure Mode 3: Oscillation (Hunting)

**What it is:** System alternates between over-controlled and under-controlled states.

**Mechanism:**
1. Overload detected
2. Aggressive throttling applied
3. Load drops rapidly
4. Throttling removed
5. Pent-up demand creates spike
6. Overload detected again
7. Repeat

**In aviation:** Traffic surge → ground stop → all clear → traffic surge.

**In agents:** Rate limit hit → back off to zero → resume full rate → rate limit hit again.

**Detection:**
- Throughput oscillating
- Periodic error spikes
- Control actions alternating between extremes

**Prevention:**
- Gradual, not sudden, control actions
- AIMD (slow increase, fast decrease)
- Hysteresis (different thresholds for on/off)
- Smoothing of demand signals

**Recovery:**
- Reduce gain in control loop
- Add delay between control actions
- Smooth demand through buffering

### Failure Mode 4: Prediction Failure

**What it is:** Decisions based on wrong predictions cause worse outcomes than no intervention.

**Mechanism:**
- Predicted capacity higher than actual → overload
- Predicted capacity lower than actual → wasted capacity
- Predicted task requirements wrong → either waste or failure

**In aviation:** Weather better than forecast → unnecessary ground delays. Weather worse → airborne holding.

**In agents:** Estimated context need < actual → autocompact. Estimated API capacity > actual → failures.

**Detection:**
- Actual outcomes differing from predictions
- Calibration metrics showing bias
- Unnecessary throttling or unexpected failures

**Prevention:**
- Conservative predictions (err toward safety)
- Continuous calibration of estimates
- Adaptive models that learn from outcomes
- Margin that absorbs prediction error

**Recovery:**
- Detect prediction failure
- Recalibrate models
- Adjust margins
- Resume with corrected predictions

### Failure Mode 5: Local-Global Misalignment

**What it is:** Each component optimizes locally, but system performs poorly.

**Mechanism:**
- Agent A optimizes for A's throughput
- Agent B optimizes for B's throughput
- Their combined behavior overloads shared resource
- Neither agent is "wrong" locally
- System fails globally

**In aviation:** Each airline optimizes flight schedules → hub congestion → system-wide delays.

**In agents:** Each agent retries aggressively → collective retry storm → system collapse.

**Detection:**
- Individual components showing healthy metrics
- System-level metrics degraded
- Shared resources overloaded

**Prevention:**
- Shared understanding of system state (CDM equivalent)
- Global coordination mechanisms
- Individual incentives aligned with system goals
- Resource allocation visible to all participants

**Recovery:**
- Identify shared resource under contention
- Implement coordination mechanism
- Align individual behavior with global goals

---

## Part VII: Multi-Agent Implications

### The Coordination Problem

Multiple agents sharing resources face coordination challenges:

**Without coordination:**
- Each agent independently estimates capacity
- Each agent independently retries on failure
- Aggregate behavior exceeds what any agent intended
- Tragedy of the commons

**With coordination:**
- Agents share information about system state
- Allocation decisions consider global picture
- Individual behavior constrained by collective need
- Sustainable throughput for all

### Coordination Mechanisms

**Mechanism 1: Centralized coordinator**

Single point that knows all agent activity and allocates resources.

```
Coordinator sees: Agent A wants 50 req/min, Agent B wants 60 req/min
Coordinator knows: Total capacity is 80 req/min
Coordinator allocates: Agent A gets 40, Agent B gets 40
```

**Pros:** Optimal allocation possible, global view
**Cons:** Single point of failure, bottleneck, latency

**Mechanism 2: Distributed token bucket**

Agents share a token pool. Must acquire tokens before using resources.

```
Pool has 1000 tokens/minute
Agent A takes 100 tokens, uses them
Agent B takes 100 tokens, uses them
If pool empty, agents wait
```

**Pros:** Decentralized, self-regulating
**Cons:** Fairness requires additional mechanism, doesn't handle priority

**Mechanism 3: AIMD-based convergence**

Each agent independently uses AIMD. System converges to fair allocation.

```
Agent A: Additive increase until failure, multiplicative decrease on failure
Agent B: Same
Equilibrium: Each agent gets ~50% of capacity
```

**Pros:** No coordination needed, robust
**Cons:** Slow convergence, not optimal, fairness only approximate

**Mechanism 4: CDM-style information sharing**

Agents share information but make independent decisions.

```
Agent A broadcasts: "I plan to submit 50 tasks"
Agent B broadcasts: "I plan to submit 60 tasks"
Both see: Total demand 110 > capacity 80
Both adjust plans independently
```

**Pros:** Decentralized, informed decisions
**Cons:** Requires trust, gaming possible

### Fairness in Multi-Agent Flow

When demand exceeds capacity, how to allocate?

**Option 1: Equal shares**
Each agent gets capacity / num_agents.
- Fair in one sense
- Inefficient if agents have different needs
- Small agents get same as large

**Option 2: Proportional to demand**
Each agent gets capacity * (demand / total_demand).
- Larger users get more
- Small users not crowded out
- May not match priority

**Option 3: Priority-weighted**
Higher priority agents get more.
- Matches business importance
- Requires priority definition
- Risk of starvation

**Option 4: Market-based**
Agents "bid" for capacity. Highest bidders win.
- Efficient allocation
- Requires pricing mechanism
- Disadvantages resource-constrained agents

### Scaling Behavior

| Agent Count | Coordination Challenge | Flow Management Complexity |
|-------------|------------------------|---------------------------|
| 1 | None | Simple rate limiting |
| 2-5 | Low | Informal coordination possible |
| 5-20 | Medium | Need explicit coordination mechanism |
| 20-100 | High | Need automated coordination |
| 100+ | Very High | Need hierarchical/distributed coordination |

As scale increases:
- Coordination overhead grows
- Local decisions have more global impact
- Central coordination becomes bottleneck
- Distributed mechanisms become necessary

---

## Part VIII: CLAUDE.md Templates

### Template 1: Basic Flow Management

```markdown
# Flow Management

## Rate Limits

- LLM API: [X] tokens/minute, [Y] requests/minute
- Database: [Z] connections max
- External APIs: [List with limits]

## Backoff Policy

On any failure:
1. First retry: Wait 1 second
2. Second retry: Wait 2 seconds
3. Third retry: Wait 4 seconds
4. Fourth retry: Wait 8 seconds
5. Fifth retry: Stop, report failure

Add random jitter (0-50%) to prevent thundering herd.

## Load Thresholds

| Metric | Normal | Caution | Critical |
|--------|--------|---------|----------|
| API utilization | <60% | 60-80% | >80% |
| Error rate | <1% | 1-5% | >5% |
| Queue depth | <10 | 10-50 | >50 |

## Caution Behavior

- Reduce submission rate by 50%
- Increase monitoring frequency
- Log detailed metrics

## Critical Behavior

- Stop new submissions
- Complete in-flight work only
- Alert human operator
- Wait for manual clearance to resume
```

### Template 2: Multi-Agent Coordination

```markdown
# Multi-Agent Flow Coordination

## Shared Resources

| Resource | Total Capacity | Allocation Method |
|----------|---------------|-------------------|
| LLM API | [X] tokens/min | Proportional to task count |
| Database | [Y] connections | First-come-first-served |
| Budget | $[Z]/day | Priority-weighted |

## Coordination Protocol

1. Before starting intensive work, check shared state
2. Estimate resource requirements
3. If resources available: claim and proceed
4. If resources constrained: queue or yield
5. After completion: release claims

## Conflict Resolution

When multiple agents need the same scarce resource:
1. Higher priority agent wins
2. If same priority: first claimer wins
3. If still tied: agent with smaller request wins
4. Losing agent waits and retries

## State Sharing

Agents maintain shared state (file or database):
- Current resource claims
- Recent failure rates
- Queue depths
- Active tasks per agent

Update frequency: Every [N] seconds
```

### Template 3: Circuit Breaker Configuration

```markdown
# Circuit Breaker Configuration

## Breakers

| Dependency | Failure Threshold | Recovery Time | Fallback |
|------------|-------------------|---------------|----------|
| LLM API | 5 failures | 60 seconds | Queue for later |
| Database | 3 failures | 30 seconds | Use cache |
| External API | 10 failures | 120 seconds | Skip feature |

## Behavior

### Closed State (Normal)
- Route all requests to dependency
- Track failures

### Open State (Tripped)
- Block all requests to dependency
- Return fallback immediately
- Log trip event

### Half-Open State (Testing)
- Allow one test request
- If succeeds: close circuit
- If fails: re-open circuit

## Monitoring

Log all circuit breaker events:
- Failure counted
- Circuit opened
- Test attempted
- Circuit closed
```

---

## Part IX: Implementation Roadmap

### Phase 1: Visibility (Week 1)

**Goal:** Understand current flow characteristics

- [ ] Instrument all API calls with timing
- [ ] Track error rates by endpoint
- [ ] Measure queue depths
- [ ] Create basic dashboard
- [ ] Establish baseline metrics

**Success criteria:** Can answer "what is current throughput?" and "what is current error rate?" at any time.

### Phase 2: Basic Control (Week 2)

**Goal:** Implement fundamental flow control

- [ ] Add exponential backoff to all API calls
- [ ] Add circuit breakers to critical dependencies
- [ ] Implement basic admission control
- [ ] Add rate limiting where needed
- [ ] Test under load

**Success criteria:** System degrades gracefully under 2x normal load instead of collapsing.

### Phase 3: Adaptive Control (Week 3-4)

**Goal:** Implement adaptive flow management

- [ ] Track and predict capacity
- [ ] Implement AIMD-based rate control
- [ ] Add predictive admission control
- [ ] Implement load shedding by priority
- [ ] Test under variable load

**Success criteria:** System automatically adjusts to changing conditions without manual intervention.

### Phase 4: Multi-Agent Coordination (Week 5-6)

**Goal:** Coordinate multiple agents sharing resources

- [ ] Implement shared state mechanism
- [ ] Add coordination protocol to CLAUDE.md
- [ ] Test with multiple concurrent agents
- [ ] Measure coordination overhead
- [ ] Optimize allocation fairness

**Success criteria:** Multiple agents share resources without collapse, with fair allocation.

### Phase 5: Optimization (Ongoing)

**Goal:** Continuous improvement

- [ ] Monitor for failure patterns
- [ ] Tune thresholds based on data
- [ ] Identify and address new bottlenecks
- [ ] Reduce coordination overhead
- [ ] Improve prediction accuracy

**Success criteria:** Sustained throughput increasing over time while maintaining reliability.

---

## Part X: Key Insights

### Insight 1: Sustainable Throughput > Maximum Throughput

The goal is not maximum possible throughput but maximum sustainable throughput. Systems optimized for peak performance will periodically collapse; systems optimized for stability will be slower on average but never catastrophically slower.

```
Sustainable_Throughput = Peak_Throughput × (1 - Margin)
Margin = f(Uncertainty, Risk_Tolerance)
```

### Insight 2: The Ground Delay Principle Applies Everywhere

It's cheaper to delay before starting than to fail mid-execution. This applies to tasks, API calls, and any resource-consuming operation.

```
Cost(Queue_Before_Start) << Cost(Fail_Mid_Execution)
```

Implication: Build queuing into every pipeline stage.

### Insight 3: Capacity Is Stochastic, Not Fixed

Treat capacity as a distribution, not a number. Plan for the lower tail, not the mean.

```
Safe_Rate = E[Capacity] - k × σ[Capacity]
```

Where k depends on risk tolerance.

### Insight 4: Local Optimization ≠ Global Optimization

Each agent optimizing locally does not produce global optimum. Explicit coordination mechanisms are required.

This is a fundamental insight from flow management: the "invisible hand" doesn't work without shared information and aligned incentives.

### Insight 5: Prediction Errors Are Inevitable

Flow management decisions are made under uncertainty. Predictions will be wrong. Design for graceful handling of prediction failure, not perfect prediction.

```
Design for: What happens when forecast is wrong?
Not for: How do we make perfect forecasts?
```

### Insight 6: Feedback Loops Have Latency

By the time you know a decision was wrong, the cost has been incurred. Build in margins that absorb the latency.

```
Margin > Decision_Latency × Change_Rate
```

### Insight 7: Oscillation Is a Control System Problem

Flow management is a control system. Oscillation occurs when gain is too high or response is too slow. Use AIMD, hysteresis, and smoothing.

---

## Part XI: Cross-Model Integration

### Connection to Separation Assurance

Flow management and separation assurance are deeply coupled:

- Flow management controls demand so separation can be maintained
- When flow management fails, separation is at risk
- Both require margins to handle uncertainty
- Both must balance efficiency against safety

**Agent implication:** Task scheduling (flow) and resource isolation (separation) must be designed together.

### Connection to Conflict Detection and Resolution

Flow management prevents conditions where conflicts become unresolvable:

- High load creates more conflicts
- Conflicts take resources to resolve
- Uncontrolled load → conflict explosion → system failure

**Agent implication:** Flow control is the first line of defense against coordination failures.

### Connection to OODA Loop

Flow management operates within an OODA loop:

- **Observe:** Current throughput, queue depth, error rates
- **Orient:** Is the system healthy? Trending toward overload?
- **Decide:** Increase/decrease rate? Shed load? Open circuit?
- **Act:** Apply control action, observe result

**Agent implication:** Flow management is a continuous control loop, not a one-time configuration.

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent architecture analysis for flow management mental model
**Related Models:** Separation Assurance, Conflict Detection & Resolution, OODA Loop, Theory of Constraints

---

## Sources

### Air Traffic Flow Management
- [A review on air traffic flow management optimization | Springer](https://link.springer.com/article/10.1007/s43621-024-00781-7)
- [Optimal Large-Scale Air Traffic Flow Management | MIT](https://www.mit.edu/~hamsa/pubs/BalakrishnanChandran_ATFM.pdf)
- [Ground Delay Program | FAA](https://www.faa.gov/air_traffic/publications/atpubs/foa_html/chap18_section_10.html)

### Queueing Theory
- [A Queueing Model for Airport Capacity and Delay Analysis](https://www.m-hikari.com/ams/ams-2014/ams-69-72-2014/thiagarajAMS69-72-2014.pdf)
- [Airport Runway Capacity and Delay | BITRE](https://www.bitre.gov.au/sites/default/files/op_050.pdf)

### Cascade Failures
- [Systemic delay propagation in the US airport network | PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3557445/)
- [A Cascading Failure Model of the Air Traffic Control Network | MDPI](https://www.mdpi.com/2076-3417/13/10/6256)

### Network Congestion Control
- [TCP congestion control | Wikipedia](https://en.wikipedia.org/wiki/TCP_congestion_control)
- [Network congestion / Congestive collapse | Wikipedia](https://en.wikipedia.org/wiki/Congestive_collapse)
- [TCP Congestion Control | Systems Approach](https://book.systemsapproach.org/congestion/tcpcc.html)

### Collaborative Decision Making
- [CDM - Collaborative Decision Making | FAA](https://cdm.fly.faa.gov/)
- [Collaborative air traffic flow management | ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0969699717302879)

### Fairness and Allocation
- [Fairness and Collaboration in Network Air Traffic Flow Management | INFORMS](https://ideas.repec.org/a/inm/ortrsc/v50y2016i1p57-76.html)

### Local vs. Global Optimization
- [Local Optimizations Don't Lead to Global Optimums | ferd.ca](https://ferd.ca/local-optimizations-don-t-lead-to-global-optimums.html)
- [Theory of Constraints 102: The Illusion of Local Optima | Medium](https://medium.com/praxis-blog/theory-of-constraints-102-local-optima-3ca8d348f146)
