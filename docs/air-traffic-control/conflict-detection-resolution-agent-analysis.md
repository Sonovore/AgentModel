# Conflict Detection and Resolution: Architectural Analysis for AI Agent Systems

## Executive Summary

Conflict detection and resolution (CD&R) in air traffic control identifies potential collisions before they occur and determines how to prevent them. The surface-level understanding---"predict when planes will be too close and fix it"---misses the deeper principle: **CD&R is about characterizing the space of possible futures and ensuring safe paths exist within that space.**

For AI agent systems, this reframing is powerful. Agents face analogous challenges: resource conflicts, deadlocks, state corruption. The question is not "will these agents conflict?" but "does a safe execution exist across all possible behaviors within the uncertainty envelope?"

| ATC Concept | Agent Equivalent | Key Insight |
|-------------|-----------------|-------------|
| Trajectory prediction | Plan execution prediction | Future behavior is uncertain |
| Closest Point of Approach | Resource access overlap point | Where plans might conflict |
| Detection horizon | How far ahead to check for conflicts | Tradeoff: early detection vs. accuracy |
| Resolution maneuver | Conflict avoidance action | Multiple strategies with different costs |
| TCAS RA | Last-resort conflict resolution | Automatic recovery when prediction fails |
| False alarm | Unnecessary conflict block | Expected cost of uncertainty |
| Cascade resolution | Fixing one conflict creates another | Multi-agent interdependence |

**The central claim:** Agent conflict detection should focus not on predicting specific conflicts but on ensuring that safe execution paths exist regardless of how uncertainty resolves.

---

## Part I: The CD&R Framework

### What Practitioners Think They Understand

The surface-level understanding: "Predict when agents will need the same resource at the same time, and prevent it."

This framing treats conflict detection as a prediction problem and resolution as optimization. Predict the conflict, find the minimum-cost fix, apply it.

This understanding is dangerously incomplete.

### What CD&R Actually Is

CD&R is a framework for maintaining the existence of safe execution paths under compound uncertainty. It recognizes that:

1. **Prediction is fundamentally uncertain.** You cannot know exactly what agents will do.
2. **Detection and resolution are coupled.** Detection thresholds depend on resolution capability.
3. **False alarms are not failures.** They're the expected cost of operating under uncertainty.
4. **Cascades are inherent.** Resolving one conflict can create others.

The fundamental question is not "will these agents conflict?" but:

```
∀ possible_execution ∈ Uncertainty_Envelope:
    ∃ resolution: all agents complete without conflict
```

### Why This Matters for Agents

Agent systems that ignore CD&R principles exhibit predictable failure modes:

- **Late conflict detection** that leaves only expensive resolution options
- **Resolution cascades** where each fix creates new problems
- **Alert fatigue** from poorly calibrated detection thresholds
- **Missed conflicts** from over-reliance on prediction accuracy
- **Deadlock** when resolution mechanisms themselves create circular dependencies

Aviation's CD&R framework provides proven patterns for managing these challenges.

---

## Part II: Translation Mapping

### The Domain Analogy

| Aviation Domain | Agent Domain |
|-----------------|--------------|
| Aircraft | Agents / tasks / processes |
| Position | State (resources held, progress made) |
| Trajectory | Plan / action sequence / intent |
| Velocity | Rate of progress / resource consumption |
| CPA calculation | Resource access overlap prediction |
| Conflict detection | Identifying potential resource contention |
| Resolution maneuver | Conflict avoidance action |
| TCAS RA | Deadlock detection, automatic abort/retry |
| MTCD (20 min lookahead) | Pre-execution plan analysis |
| STCA (2 min lookahead) | Active execution monitoring |
| False alarm | Unnecessary block/delay |

### Agent "Trajectory Prediction"

What is the agent equivalent of trajectory prediction?

**Plan execution prediction:**
- Agent states what it intends to do
- But execution may differ from plan (conditional branches, exceptions)
- Execution time is variable (API latency, compute availability)
- Plan may change based on intermediate results

**Intent uncertainty:**
- Agent's high-level goal may be known but detailed steps uncertain
- Agent may have private information not shared with coordinator
- Learning agents may take surprising actions

**Resource demand uncertainty:**
- Actual resource needs may differ from estimates
- Demand may spike unpredictably
- Cascading requests may amplify demand

Unlike aviation where uncertainty is primarily analog (continuous position error), agent uncertainty has both continuous (timing) and discrete (which branch executes) components.

### Time Horizons for Agent CD&R

| Aviation | Agent Equivalent | Purpose |
|----------|-----------------|---------|
| MTCD (20 min) | Pre-execution plan analysis | Check plans for conflicts before starting |
| TCT (8 min) | Near-term execution monitoring | Watch active agents for developing conflicts |
| STCA (2 min) | Imminent conflict detection | Alert when conflict is very close |
| TCAS (30 sec) | Last-resort intervention | Automatic abort/retry when all else fails |

**Tradeoff:** Longer horizons enable gentler resolution (reschedule, re-plan) but have higher false alarm rates. Shorter horizons are more accurate but leave only aggressive options (abort, rollback).

---

## Part III: Where Agents Struggle vs. Excel

### Agent Advantages

**Parallel detection:** Agents can check many potential conflicts simultaneously. No attention bottleneck.

**Consistent application:** Detection rules apply uniformly. No fatigue-induced variation.

**Instant communication:** Conflict detection and resolution commands propagate in milliseconds.

**Perfect memory:** No forgetting about developing conflicts while handling others.

### Where Agents Struggle

**Hidden dependencies:** Aviation conflicts are geometric---aircraft interact when physically proximate. Agent conflicts can be hidden: changing file A affects function B, which service C uses, which breaks agent D. The dependency graph is often not fully known.

**Semantic conflicts:** Aircraft either collide or they don't. Agents can have semantic conflicts where both operations succeed individually but produce collectively inconsistent state. Detecting these requires understanding meaning, not just resource access.

**Intent unpredictability:** Aircraft file flight plans; trajectories are largely known. Agent intent is often hidden---the agent may not know its own future actions until it observes intermediate results.

**Resolution complexity:** Aircraft resolve conflicts by moving in space---the resolution space is well-understood. Agent conflicts may require complex reasoning about state rollback, compensating transactions, or semantic repair.

**Cascade reasoning:** Aircraft conflict resolution has well-characterized cascade patterns (domino effect to adjacent levels). Agent cascades depend on complex dependency graphs that are hard to analyze.

### The Fundamental Challenge

**Aviation:** Given known trajectories with bounded uncertainty, determine if separation can be maintained.

**Agents:** Given partially known plans with unbounded conditional branches, determine if execution can complete without conflict.

The agent problem is strictly harder because:
- Plans have discrete uncertainty (branches), not just continuous uncertainty (timing)
- Dependencies are often hidden until conflict occurs
- "Conflict" includes semantic inconsistency, not just resource contention

---

## Part IV: Detection Architecture

### Layered Detection (Matching Time Horizons)

**Layer 1: Pre-Execution Plan Analysis (Strategic)**

Before agents start, analyze their plans for potential conflicts.

```python
def analyze_plans_for_conflicts(plans):
    """
    Extract resource requirements from each plan.
    Identify overlapping requirements.
    Flag potential conflicts for review or resolution.
    """
    for i, plan_a in enumerate(plans):
        resources_a = extract_resource_requirements(plan_a)
        for plan_b in plans[i+1:]:
            resources_b = extract_resource_requirements(plan_b)
            if resources_overlap(resources_a, resources_b):
                yield PotentialConflict(plan_a, plan_b,
                    overlap=resources_a & resources_b)
```

**Limitations:**
- Plans may not be available (agent decides dynamically)
- Resource requirements may not be known until execution
- High false alarm rate (overlap doesn't mean conflict)

**Value:** Catches obvious conflicts cheaply. Enables re-planning before execution starts.

**Layer 2: Execution Monitoring (Tactical)**

During execution, monitor agent state for developing conflicts.

```python
def monitor_execution(agents):
    """
    Track which resources each agent is approaching.
    Detect when agents are converging on same resource.
    Alert when conflict is likely within horizon.
    """
    for agent in agents:
        projected = project_resource_access(agent, horizon=60)  # 60 seconds
        for other in agents:
            if agent == other: continue
            other_projected = project_resource_access(other, horizon=60)
            if will_conflict(projected, other_projected):
                yield DevelopingConflict(agent, other,
                    time_to_conflict=estimate_ttc(projected, other_projected))
```

**Limitations:**
- Projection is uncertain (agent may branch differently)
- Monitoring has overhead
- Must balance horizon (longer = more false alarms, shorter = less resolution time)

**Value:** Provides time for graceful resolution before conflict materializes.

**Layer 3: Imminent Conflict Detection (Reactive)**

Detect conflicts about to occur.

```python
def detect_imminent_conflict(agents):
    """
    Check current resource requests for conflicts.
    Detect actual contention happening now.
    """
    pending_requests = collect_pending_requests(agents)
    for resource, requests in group_by_resource(pending_requests):
        if len(requests) > 1 and not resource.allows_concurrent:
            yield ImminentConflict(resource, requests)
```

**Limitations:**
- Little time for resolution (must abort or block)
- May already be too late (conflict in progress)

**Value:** Catches conflicts that slipped through earlier detection.

**Layer 4: Last-Resort Intervention (Emergency)**

Automatic recovery when conflict is occurring.

```python
def emergency_resolution(conflict):
    """
    Automatic intervention when conflict detected at runtime.
    """
    if conflict.type == ConflictType.DEADLOCK:
        # Select victim and abort
        victim = select_deadlock_victim(conflict.participants)
        abort_and_retry(victim)
    elif conflict.type == ConflictType.RESOURCE_CONTENTION:
        # Force one to wait
        loser = select_by_priority(conflict.participants)
        block_until_available(loser)
    elif conflict.type == ConflictType.STATE_CORRUPTION:
        # Rollback to last consistent state
        rollback_to_checkpoint(conflict.affected_state)
```

**Limitations:**
- Expensive (work discarded, time lost)
- May not always be possible (some state changes are irreversible)
- Should rarely trigger (indicates earlier detection failed)

**Value:** Prevents catastrophic outcomes when all else fails.

### CLAUDE.md Template: Detection Architecture

```markdown
# Conflict Detection Configuration

## Layer 1: Pre-Execution (Plans)
Before starting a task that modifies shared state:
1. Declare intended resource access
2. System checks for overlap with other planned work
3. If overlap detected: coordinate before starting

## Layer 2: Execution Monitoring (Active)
During task execution:
1. System tracks resource access patterns
2. Alerts generated when convergence detected
3. Agent receives warning: "Another agent approaching same resource"

## Layer 3: Imminent Detection (Requests)
At time of resource access:
1. Locking mechanism detects contention
2. If lock unavailable: wait or abort based on priority
3. Timeout: 30 seconds, then escalate

## Layer 4: Emergency (Automatic)
If conflict occurs:
1. Deadlock: lower-priority agent aborted
2. Contention timeout: lower-priority agent delayed
3. State corruption: rollback to checkpoint

## Instrumentation
Log all detection events for tuning:
- Conflict type, detection layer, resolution method
- Time from detection to resolution
- Was this a false alarm?
```

---

## Part V: Resolution Strategies

### Strategy 1: Temporal Separation (Sequencing)

**Aviation equivalent:** Longitudinal separation (arrive at different times)

**Agent implementation:** Execute agents at different times

```python
def resolve_by_sequencing(conflict):
    """
    Resolve conflict by sequencing agents.
    One completes before other starts.
    """
    agents = conflict.participants
    # Order by priority or arrival time
    ordered = sort_by_priority(agents)

    for i, agent in enumerate(ordered[1:], 1):
        # Each agent waits for all higher-priority agents
        predecessors = ordered[:i]
        agent.wait_for(predecessors)
```

**Pros:** Simple, guaranteed to work, no partial execution
**Cons:** Reduced parallelism, increased latency
**When to use:** When conflicts are common, resources can't be shared

### Strategy 2: Resource Partitioning (Sharding)

**Aviation equivalent:** Lateral separation (different routes)

**Agent implementation:** Divide resources so agents access different partitions

```python
def resolve_by_partitioning(agents, resource):
    """
    Partition resource so each agent works on different part.
    """
    partitions = create_partitions(resource, len(agents))
    for agent, partition in zip(agents, partitions):
        agent.scope = partition  # Agent only accesses its partition
```

**Pros:** Full parallelism, no runtime coordination
**Cons:** Not always possible, cross-partition operations still conflict
**When to use:** When resources are naturally partitionable

### Strategy 3: Optimistic Execution with Rollback

**Aviation equivalent:** Allowing conflict then resolving via TCAS

**Agent implementation:** Execute optimistically, detect conflicts, rollback if needed

```python
def optimistic_execution(agent, operation):
    """
    Execute operation optimistically.
    If conflict detected, rollback and retry.
    """
    checkpoint = create_checkpoint()
    try:
        result = operation.execute()
        if conflict_detected():
            rollback(checkpoint)
            wait_random_backoff()
            return optimistic_execution(agent, operation)  # Retry
        else:
            commit()
            return result
    except ConflictException:
        rollback(checkpoint)
        raise
```

**Pros:** Maximum parallelism when conflicts are rare, no coordination overhead for conflict-free cases
**Cons:** Wasted work on rollback, complexity of rollback implementation
**When to use:** When conflicts are rare, rollback is cheap

### Strategy 4: Priority-Based Preemption

**Aviation equivalent:** Priority rules (emergency aircraft have priority)

**Agent implementation:** Higher-priority agents preempt lower-priority

```python
def priority_resolution(conflict):
    """
    Higher priority agent continues, lower priority waits or aborts.
    """
    winner = max(conflict.participants, key=lambda a: a.priority)
    losers = [a for a in conflict.participants if a != winner]

    for loser in losers:
        if loser.can_rollback():
            loser.rollback_and_wait()
        else:
            loser.block_until_resource_available()
```

**Pros:** Ensures critical work completes, deterministic resolution
**Cons:** Lower-priority agents may starve
**When to use:** When clear priority ordering exists

### Strategy 5: Negotiated Resolution

**Aviation equivalent:** Controller-mediated resolution

**Agent implementation:** Agents negotiate through protocol

```python
def negotiate_resolution(conflict, coordinator):
    """
    Agents negotiate resolution through coordinator.
    """
    proposals = []
    for agent in conflict.participants:
        proposal = agent.propose_resolution()
        proposals.append(proposal)

    # Coordinator selects best proposal
    resolution = coordinator.select_best(proposals)

    # All agents execute resolution
    for agent in conflict.participants:
        agent.execute_resolution(resolution)
```

**Pros:** Flexible, can handle complex situations
**Cons:** Coordination overhead, potential for negotiation deadlock
**When to use:** When conflicts are complex, no clear priority

### Resolution Selection Guide

| Conflict Type | Recommended Strategy | Rationale |
|---------------|---------------------|-----------|
| Common, predictable | Partitioning | Avoid conflict by design |
| Rare, unpredictable | Optimistic with rollback | Don't pay coordination cost |
| Critical path involved | Priority preemption | Ensure critical work completes |
| Complex dependencies | Negotiation | Need flexibility to find solution |
| High contention rate | Sequencing | Reduce wasted work |

---

## Part VI: The False Alarm Problem

### Why False Alarms Are Inevitable

Signal detection theory applies directly to agent conflict detection:

| | Actual Conflict | No Conflict |
|---|---|---|
| **Alert** | True Positive | False Positive (False Alarm) |
| **No Alert** | False Negative (Miss) | True Negative |

**The fundamental tradeoff:** Lower detection threshold catches more conflicts (fewer misses) but generates more false alarms.

For agents:
- **False alarm cost:** Unnecessary blocking, wasted coordination overhead, reduced throughput
- **Miss cost:** Conflict occurs, state corruption, deadlock, cascade failure

**If miss cost >> false alarm cost, operate with low threshold (high false alarm rate).**

### Measuring and Managing False Alarms

**Track false alarm rate:**
```python
def track_false_alarms():
    """
    For each conflict alert:
    - Did actual conflict occur?
    - If alert led to action, would conflict have occurred without action?
    """
    alerts = get_detection_events()
    for alert in alerts:
        if alert.resolution_action_taken:
            # Counterfactual: would conflict have occurred?
            would_conflict = simulate_without_resolution(alert)
            alert.was_false_alarm = not would_conflict
        else:
            # Alert but no action: was there conflict?
            alert.was_false_alarm = not alert.conflict_occurred

    return count(alerts, lambda a: a.was_false_alarm) / len(alerts)
```

**Target false alarm rate:**
- Too high: alert fatigue, coordination overhead dominates
- Too low: misses increase, conflict rate increases
- Optimal: depends on cost ratio

**Rule of thumb:** If false alarm rate > 50%, improve detection (better prediction, more context). If miss rate > acceptable, lower threshold (accept more false alarms).

### The "Cry Wolf" Effect in Agent Systems

High false alarm rates degrade human operator performance:
- Operators learn to ignore alerts
- True alerts get slower response
- Trust in system degrades

For agent systems:
- Automated systems don't have "trust" issues
- But high false alarm rates still waste resources
- And downstream human reviewers exhibit cry wolf effect

**Mitigation:**
- Track and report false alarm rate
- Continuously tune detection thresholds based on data
- Differentiate alert severity (high-confidence vs. low-confidence alerts)
- Provide context with alerts (why was this flagged?)

---

## Part VII: Cascade Management

### The Domino Effect

Resolving one conflict can create another:

```
Agent A and B conflict over Resource 1
  → Resolution: A waits, B proceeds
  → B now takes longer
  → B conflicts with C over Resource 2
  → Resolution: C waits, B proceeds
  → C now conflicts with D
  → ...
```

### Cascade Detection

```python
def detect_cascade_risk(resolution):
    """
    Before applying resolution, check if it creates new conflicts.
    """
    # Simulate resolution
    simulated_state = apply_resolution_simulation(resolution)

    # Check for new conflicts
    new_conflicts = detect_conflicts(simulated_state)

    if new_conflicts:
        # Resolution would create cascade
        return CascadeRisk(
            original=resolution.conflict,
            downstream=new_conflicts,
            cascade_depth=estimate_cascade_depth(new_conflicts)
        )
    return None
```

### Cascade Prevention Strategies

**Strategy 1: Look-ahead before resolution**
Check if proposed resolution creates new conflicts. If so, consider alternative.

**Strategy 2: Global optimization**
Consider all active agents when resolving. Find resolution that doesn't create new conflicts.

**Strategy 3: Cascade breakers**
Insert "firebreaks" that stop cascade propagation:
- Timeout limits on waiting
- Maximum cascade depth
- Abort rather than propagate past limit

**Strategy 4: Isolation**
Structure system so cascades can't propagate across boundaries:
- Independent resource pools
- Separate execution domains
- Circuit breakers between domains

### CLAUDE.md Template: Cascade Management

```markdown
# Cascade Prevention

## Before Resolving Any Conflict
1. Check if proposed resolution creates new conflicts
2. If yes, consider alternatives
3. If no alternative, evaluate cascade depth
4. If depth > 3, escalate to human

## Cascade Limits
- Maximum wait time: 60 seconds
- Maximum cascade depth: 5 resolutions
- If limits exceeded: abort lowest-priority agent

## Isolation Boundaries
- Database operations: isolated from file operations
- API calls: isolated from local operations
- If conflict crosses boundary: resolve within boundary first

## Circuit Breakers
If same conflict pattern occurs 3x in 5 minutes:
- Stop accepting new work in that area
- Complete existing work
- Reset before resuming
```

---

## Part VIII: Measurement Framework

### Detection Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| True positive rate | Conflicts correctly detected | >99% |
| False positive rate | Non-conflicts flagged | <50% |
| Detection lead time | Time from detection to conflict | >10x resolution time |
| Miss rate | Conflicts not detected | <0.1% |

### Resolution Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Resolution success rate | Conflicts resolved without damage | >99.9% |
| Resolution time P50 | Median time to resolve | <1 second |
| Resolution time P99 | 99th percentile resolution time | <30 seconds |
| Cascade rate | Resolutions that create new conflicts | <10% |
| Cascade depth | Average length of cascade chain | <2 |

### System Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Throughput under conflict | Operations/sec during contention | >50% of conflict-free |
| Conflict-free efficiency | Overhead when no conflicts | <5% |
| Recovery completeness | Percent of conflicts fully resolved | 100% |

### Diagnostic Dashboard

```
Conflict Detection Dashboard

Detection Performance (last hour):
- Alerts generated: 142
- True positives: 67 (47%)
- False positives: 75 (53%)  <- Above 50% target, investigate
- Misses detected: 0 (0%)

Resolution Performance (last hour):
- Conflicts resolved: 67
- Resolution time P50: 450ms
- Resolution time P99: 12s
- Cascades: 8 (12%)  <- Above 10% target
- Max cascade depth: 4

Action Items:
1. False positive rate high - review detection thresholds
2. Cascade rate elevated - review resource dependencies
```

---

## Part IX: Optimization Patterns

### Pattern 1: Tiered Detection Horizons

**Problem:** Single detection horizon either misses conflicts (too short) or has too many false alarms (too long).

**Solution:** Multiple detection tiers with different horizons and responses.

**CLAUDE.md template:**
```markdown
# Conflict Detection Horizons

## Tier 1: Plan Analysis (Before Execution)
Horizon: Entire task duration
Response: Re-plan, coordinate, defer

## Tier 2: Execution Monitoring (Active Work)
Horizon: 60 seconds ahead
Response: Slow down, prepare to yield

## Tier 3: Imminent Detection (About to Conflict)
Horizon: 5 seconds
Response: Block, queue, wait

## Tier 4: Emergency (Conflict Occurring)
Horizon: Now
Response: Abort, rollback, escalate

Alert escalation:
- Tier 1 alert: Consider adjusting plan
- Tier 2 alert: Prepare contingency
- Tier 3 alert: Take action
- Tier 4 alert: Emergency recovery
```

### Pattern 2: Conflict Probability Thresholds

**Problem:** Binary conflict detection (yes/no) doesn't capture uncertainty.

**Solution:** Report conflict probability, use tiered thresholds.

**CLAUDE.md template:**
```markdown
# Conflict Probability Handling

## Probability Estimation
For each potential conflict, estimate probability based on:
- How certain are we of resource requirements?
- How variable is execution timing?
- How reliable is intent information?

## Response Thresholds
- P < 10%: Log but no action
- P 10-50%: Monitor closely, prepare contingency
- P 50-90%: Alert, recommend coordination
- P > 90%: Treat as certain conflict, resolve now

## Uncertainty Acknowledgment
When reporting conflicts, include confidence:
- "High confidence conflict: Agent A and B will both need Resource X"
- "Medium confidence: Agent A may need Resource X depending on branch"
- "Low confidence: If Agent A takes unusual path, possible conflict"
```

### Pattern 3: Resolution Cost Comparison

**Problem:** First available resolution may not be best.

**Solution:** Compare resolution options before selecting.

**CLAUDE.md template:**
```markdown
# Resolution Selection

When conflict detected, evaluate options:

## Option 1: Temporal (Sequence)
Cost: Wait time for delayed agent
Risk: Cascade if delayed agent conflicts with others

## Option 2: Resource (Partition)
Cost: Setup overhead, possible inefficiency
Risk: Cross-partition operations later

## Option 3: Rollback (Optimistic)
Cost: Wasted work if conflict occurs
Risk: Repeated rollbacks if high contention

## Selection Criteria
1. Choose lowest expected cost
2. Expected cost = P(conflict) * cost_if_conflict + (1-P) * cost_if_no_conflict
3. Include cascade risk in cost calculation

## Default Selection
- High P(conflict): Sequence (avoid wasted work)
- Low P(conflict): Optimistic (avoid coordination overhead)
- Clear priority: Preemption (fast, deterministic)
```

### Pattern 4: Detection Calibration Loop

**Problem:** Detection thresholds drift from optimal over time.

**Solution:** Continuous calibration based on observed outcomes.

**CLAUDE.md template:**
```markdown
# Detection Calibration

## Tracking
For each alert:
- Record: alert type, confidence, resolution taken
- Record: was this a true conflict?
- Record: if no action taken, did conflict occur?

## Weekly Review
- Calculate false positive rate
- Calculate miss rate
- Compare to targets

## Calibration Actions
If false positive rate > target:
- Raise detection thresholds
- Add more context to detection

If miss rate > target:
- Lower detection thresholds
- Add detection for missed patterns

## Constraints
- Never raise miss rate above acceptable level for throughput
- Document all calibration changes
```

---

## Part X: Multi-Agent Implications

### N-Body Conflict Problem

With N agents, there are N(N-1)/2 potential pairwise conflicts. But the problem is worse:
- Resolving A-B conflict affects A-C, A-D, B-C, B-D...
- True optimization is NP-hard

### Scaling Approaches

**Spatial decomposition:**
- Group agents by resource domain
- Detect conflicts within groups
- Handle cross-group conflicts separately

**Hierarchical detection:**
- Coarse-grained detection for all pairs
- Fine-grained detection only for likely conflicts

**Decoupled resolution:**
- Resolve conflicts independently by priority
- Accept suboptimality for scalability

### Decentralized vs. Centralized Detection

**Centralized:**
- Single detector sees all agents
- Can optimize globally
- Bottleneck as agents scale

**Decentralized:**
- Each agent detects its own conflicts
- No bottleneck
- May miss system-wide patterns
- Risk of inconsistent detection

**Hybrid:**
- Local detection for immediate conflicts
- Central coordination for cross-domain
- Best of both but complex

### CLAUDE.md Template: Multi-Agent Conflict

```markdown
# Multi-Agent Conflict Detection

## Decomposition
Agents grouped by resource domain:
- Group A: auth, users, sessions
- Group B: api, requests, responses
- Group C: data, models, persistence

## Within-Group Detection
Each group has dedicated conflict detector.
Detects all conflicts within group.
Resolves using group-local rules.

## Cross-Group Detection
Central coordinator monitors cross-group access.
Cross-group conflicts: escalate to coordinator.
Coordinator resolves or delegates to human.

## Scaling Rules
- Group size: max 10 agents
- If group grows: split by sub-domain
- Cross-group traffic: minimize
```

---

## Part XI: Cross-Model Integration

### Relationship to Separation Assurance

Separation assurance is **prevention**; CD&R is **backup**.

If separation is maintained, conflicts don't occur (by design). CD&R handles conflicts that separation doesn't prevent.

**Integration:**
- Size separation to minimize conflicts
- Design CD&R for the conflicts that still occur
- Measure both: if CD&R triggers often, separation may be too tight

### Relationship to Flow Management

Flow management is **upstream** of CD&R.

When system load approaches capacity, flow management reduces load before conflicts become frequent.

**Integration:**
- Monitor conflict rate
- If conflict rate rises, activate flow control
- Flow control: delay new work, don't start new agents

### Relationship to OODA Loop

OODA's **Orient** phase is critical for CD&R. Agents must:
- Understand their own future resource needs (self-prediction)
- Understand other agents' likely behavior (other-prediction)
- Recognize developing conflicts (situation awareness)

**Integration:**
- Documentation of agent behavior patterns aids prediction
- Shared conventions enable prediction without communication
- Orient failure leads to missed conflicts or false alarms

---

## Part XII: Failure Mode Taxonomy

### Detection Failures

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| Conflict not detected | Detection threshold too high | Lower threshold |
| Conflict detected too late | Horizon too short | Extend horizon |
| Too many false alarms | Threshold too low | Raise threshold, improve prediction |
| Inconsistent detection | Multiple detectors disagree | Centralize or reconcile |
| Missed semantic conflicts | Only checking resource access | Add semantic analysis |

### Resolution Failures

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| Resolution creates new conflict | No cascade check | Add look-ahead |
| Resolution takes too long | Negotiation overhead | Simplify protocol |
| Resolution fails (conflict persists) | Inadequate resolution strategy | Add emergency fallback |
| Repeated resolution of same conflict | Root cause not addressed | Fix underlying issue |
| Starvation (one agent never proceeds) | Unfair priority scheme | Add aging/fairness |

### System Failures

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| Throughput collapses under load | Too many conflicts | Reduce load or improve separation |
| Detection becomes bottleneck | O(n^2) scaling | Decompose, hierarchical detection |
| Alert fatigue | High false alarm rate | Improve prediction, raise thresholds |
| Cascades propagate widely | No isolation | Add circuit breakers |

---

## Part XIII: Implementation Checklist

### Detection Implementation

- [ ] Define resource access model (what can conflict with what?)
- [ ] Implement plan analysis (pre-execution detection)
- [ ] Implement execution monitoring (active detection)
- [ ] Implement lock-level detection (imminent detection)
- [ ] Implement emergency detection (deadlock, corruption)
- [ ] Instrument all detection events

### Resolution Implementation

- [ ] Implement sequencing resolution
- [ ] Implement priority-based resolution
- [ ] Implement rollback resolution (where feasible)
- [ ] Define resolution selection rules
- [ ] Implement cascade detection
- [ ] Implement cascade limits

### Calibration Implementation

- [ ] Track true positive rate
- [ ] Track false positive rate
- [ ] Track miss rate (if measurable)
- [ ] Set up calibration review process
- [ ] Define threshold adjustment rules

### Monitoring Implementation

- [ ] Dashboard for detection metrics
- [ ] Dashboard for resolution metrics
- [ ] Alerts for threshold violations
- [ ] Trend tracking over time
- [ ] Capacity tracking vs. conflict rate

---

## Sources

### Aviation CD&R
- Development of Conflict Detection System for ATC, Datascience.aero
- Probabilistic Trajectory Prediction and Conflict Detection, AIAA
- Review of CD&R Modeling Methods, MIT Lincoln Laboratory

### Signal Detection Theory
- False Alerts in ATC: Cry Wolf Effect?, Human Factors Journal
- Nuisance Alerts in Operational ATC Environments, FAA

### Distributed Systems
- Wait For Graph Deadlock Detection, GeeksforGeeks
- Distributed Deadlock Detection and Resolution, ResearchGate
- Deadlock Detection in Distributed Systems, UIC

### Multi-Agent Systems
- Decentralized Multi-Agent Path Finding, Springer AAMAS
- Theory and Implementation of Path Planning by Negotiation, ScienceDirect

### Cross-References
- `/docs/air-traffic-control/conflict-detection-resolution.md` - Source research
- `/docs/air-traffic-control/separation-assurance-agent-analysis.md` - Related model
- `/docs/management/ooda-loop-agent-analysis.md` - OODA integration

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent architecture analysis for cross-model synthesis
**Status:** Complete
