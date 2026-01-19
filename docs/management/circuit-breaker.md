# Circuit Breaker Pattern for Agent Supervision

Exploring how the Circuit Breaker Pattern from distributed systems applies to AI agent failure handling and cascade prevention.

## Background

| Aspect | Description |
|--------|-------------|
| **Origin** | Michael Nygard, "Release It!" (2007, 2nd ed. 2018) |
| **Domain** | Distributed systems, fault tolerance, stability patterns |
| **Core Problem** | Failures in one component cascade to dependent components, causing system-wide collapse |
| **Key Insight** | Fail fast and protect the system rather than waiting for inevitable timeout |
| **Pattern Type** | Stability pattern - prevents cascading failure |

The Circuit Breaker pattern takes its name from electrical circuit breakers that trip to prevent house fires. When current exceeds safe levels, the breaker opens, cutting power to prevent damage. Once conditions normalize, the breaker can be reset.

In software systems, the circuit breaker prevents a failing service from taking down its callers. Instead of waiting for slow timeouts or retrying endlessly, the circuit breaker "trips" and immediately returns failure - failing fast rather than failing slow.

## The Three States

```
                     ┌────────────────────────────────────────────────┐
                     │                                                │
                     │  Success threshold met                         │
                     │                                                │
                     ▼                                                │
              ┌─────────────┐                                   ┌─────────────┐
              │             │                                   │             │
              │   CLOSED    │─────── Failure threshold ────────>│    OPEN     │
              │             │         exceeded                  │             │
              │ (Normal     │                                   │ (Failing    │
              │  operation) │                                   │  fast)      │
              └─────────────┘                                   └─────────────┘
                     ^                                                │
                     │                                                │
                     │                                                │ Timeout
                     │                                                │ expires
                     │                                                │
                     │         ┌─────────────┐                        │
                     │         │             │                        │
                     └─────────│  HALF-OPEN  │<───────────────────────┘
                   Success     │             │
                               │ (Testing    │
                               │  recovery)  │────── Failure ──────┐
                               └─────────────┘                     │
                                                                   │
                                                                   │
                               ┌────────────────────────────────────┘
                               │
                               ▼
                         Back to OPEN
```

| State | Behavior | Transitions |
|-------|----------|-------------|
| **Closed** | Normal operation. Requests pass through. Failures are counted. | Transitions to Open when failure threshold exceeded |
| **Open** | Circuit tripped. All requests fail immediately without attempting operation. | Transitions to Half-Open after timeout period |
| **Half-Open** | Testing recovery. Allows limited requests through to test if underlying problem resolved. | Transitions to Closed on success, back to Open on failure |

## Key Concepts from Release It!

### 1. Fail Fast

The core principle: if something is going to fail, fail immediately rather than wasting resources on slow failure.

| Slow Failure | Fast Failure |
|--------------|--------------|
| Wait 30s for timeout | Return error in 10ms |
| Hold connection open | Release resources immediately |
| Block calling threads | Free caller to handle error |
| Queue requests behind failing call | Caller can try alternatives |
| Resource exhaustion spreads | Failure stays contained |

**Why fast failure matters:** Slow failures cause resource exhaustion. Threads waiting on timeouts can't handle other work. Connection pools fill up. Memory accumulates. Eventually the caller fails too, propagating the failure.

### 2. Cascade Failure

Nygard's central concern: **one failure becoming many failures**.

```
Service A (fails)
    │
    ▼
Service B (calls A, waits, times out, exhausts threads)
    │
    ▼
Service C (calls B, waits, times out, exhausts threads)
    │
    ▼
Service D (calls C, waits...)
    │
    ▼
System-wide outage
```

Without circuit breakers, a single failing component can take down an entire distributed system. Each layer waits on the layer below, consuming resources while waiting, until the whole system is paralyzed.

### 3. Bulkheads

Related pattern: **isolate failures to prevent spread**. Like watertight compartments in a ship, bulkheads ensure that a breach in one area doesn't sink the entire vessel.

| Without Bulkheads | With Bulkheads |
|-------------------|----------------|
| All requests share one thread pool | Different request types get separate pools |
| One slow operation starves all operations | Slow operations only starve their own pool |
| Failure anywhere affects everything | Failure contained to one compartment |

### 4. Timeouts as Circuit Breaker Triggers

Every call that can block should have a timeout. But timeouts alone aren't enough - they determine when a single call fails, not when to stop trying.

| Timeout Alone | Timeout + Circuit Breaker |
|---------------|--------------------------|
| Each call waits for timeout | After N timeouts, stop trying |
| Constant timeout cost | Fail immediately until recovery |
| Never gives up | Gives underlying system time to recover |

### 5. Recovery Behavior

The Half-Open state is where recovery is tested. Nygard emphasizes:

- **Don't flood a recovering system:** Only allow limited test requests through
- **Monitor recovery attempts:** Track success rate, not just single success
- **Consider gradual recovery:** Some implementations ramp up traffic rather than going from Half-Open to fully Closed immediately

## Mapping to AI Agent Supervision

The Circuit Breaker pattern maps to agent supervision when viewing an agent (or agent capability) as a "service" that can fail.

### What "Failure" Means for Agents

| Distributed Systems | Agent Supervision |
|---------------------|-------------------|
| HTTP 500 errors | Agent produces incorrect output |
| Timeouts | Agent exceeds time/token budget |
| Connection refused | Agent refuses or fails to start task |
| Malformed response | Agent output doesn't meet format requirements |
| Resource exhaustion | Agent consumes excessive context/compute |

**Key distinction:** Agent failures are often soft failures - the agent produces output, but the output is wrong. This requires verification to detect, unlike network errors which are immediately apparent.

### Agent-Specific Failure Types

| Failure Type | Detection | Circuit Breaker Response |
|--------------|-----------|-------------------------|
| **Hallucination** | Verification agent, human review | Trip after N unverified claims |
| **Task misunderstanding** | Output doesn't match intent | Trip after repeated misalignment |
| **Loop/spin** | Token budget exhausted, no progress | Trip on budget exceed |
| **Regression** | Previously working capability fails | Trip immediately, investigate |
| **Capability boundary** | Agent cannot do what's asked | Trip, route to different agent/human |

### The Three States for Agent Supervision

```
┌──────────────────────────────────────────────────────────────────────┐
│                           CLOSED                                      │
│                                                                       │
│  Agent operating normally                                             │
│  - Tasks assigned freely                                              │
│  - Autonomy at normal level                                           │
│  - Standard verification                                              │
│                                                                       │
│  Monitoring:                                                          │
│  - Track failure rate                                                 │
│  - Count consecutive failures                                         │
│  - Watch for failure patterns                                         │
└────────────────────────────────────────────────────────────────────────┘
         │
         │ Failure threshold exceeded:
         │ - N consecutive failures
         │ - Error rate > X%
         │ - Specific failure pattern detected
         ▼
┌──────────────────────────────────────────────────────────────────────┐
│                            OPEN                                       │
│                                                                       │
│  Agent capability suspended                                           │
│  - Tasks of this type not assigned                                    │
│  - Route to alternative (other agent, human, queue)                   │
│  - Fast failure: don't wait for inevitable failure                    │
│                                                                       │
│  During Open state:                                                   │
│  - Give agent/system time to recover                                  │
│  - Don't flood with retries                                           │
│  - Investigate root cause                                             │
└────────────────────────────────────────────────────────────────────────┘
         │
         │ Timeout expires (or manual reset)
         ▼
┌──────────────────────────────────────────────────────────────────────┐
│                          HALF-OPEN                                    │
│                                                                       │
│  Testing recovery                                                     │
│  - Allow limited/supervised tasks                                     │
│  - Higher verification than normal                                    │
│  - Ready to trip back to Open                                         │
│                                                                       │
│  Success criteria:                                                    │
│  - N successful tasks → Close                                         │
│  - Any failure → Open (with longer timeout)                           │
└────────────────────────────────────────────────────────────────────────┘
```

### Cascade Failure in Agent Systems

Without circuit breakers, agent failures cascade:

```
Agent A: Code generation (failing - producing bugs)
         │
         ▼
Agent B: Code review (reviewing buggy code, approving it)
         │
         ▼
Agent C: Testing (writing tests for buggy implementation)
         │
         ▼
Agent D: Documentation (documenting incorrect behavior)
         │
         ▼
Human: Debugging a mess that looks professionally done
```

The cascade happens because downstream agents trust upstream output. If Agent A is producing garbage, everything built on that garbage is also garbage - but now with more effort invested.

**With circuit breakers:**

```
Agent A: Code generation (failing - producing bugs)
         │
         ├── Circuit breaker trips after 3 failed reviews
         │
         ▼
OPEN STATE:
  - Code generation tasks route to human
  - Downstream agents not fed bad input
  - Investigation begins on why Agent A is failing
```

### Agent Bulkheads

Isolate agent failures by capability:

| Capability | Bulkhead | Effect of Failure |
|------------|----------|-------------------|
| Code generation | Own circuit breaker | Code tasks fail, other tasks continue |
| Code review | Own circuit breaker | Review fails, generation/testing continue |
| Testing | Own circuit breaker | Tests fail, other tasks continue |
| Documentation | Own circuit breaker | Docs fail, code tasks continue |

**Multi-agent pool bulkhead:** If using multiple agents in parallel, failures in one agent shouldn't exhaust the pool for others.

| Without Bulkhead | With Bulkhead |
|------------------|---------------|
| Agent A's failures block task queue | Agent A quarantined, others continue |
| Retry storms consume all capacity | Retries limited to Agent A's allocation |
| System-wide slowdown | Degraded capacity in one area only |

## Supervision Patterns

### 1. Failure-Rate Circuit Breaker

Trip based on error rate over a window.

| Parameter | Example Value | Meaning |
|-----------|---------------|---------|
| Window | Last 10 tasks | Failure rate calculated over recent tasks |
| Threshold | 40% | Trip if 4+ of last 10 tasks failed |
| Timeout | 30 minutes | Stay Open for 30 minutes before Half-Open |
| Half-Open limit | 2 tasks | Allow 2 test tasks in Half-Open |

**When to use:** General capability monitoring. Good for detecting gradual degradation.

### 2. Consecutive-Failure Circuit Breaker

Trip after N failures in a row.

| Parameter | Example Value | Meaning |
|-----------|---------------|---------|
| Threshold | 3 consecutive | Trip after 3 failures without success |
| Timeout | 15 minutes | Stay Open for 15 minutes |
| Recovery threshold | 2 consecutive | Need 2 successes in Half-Open to Close |

**When to use:** Detecting sudden capability loss. More sensitive to acute failures than rate-based.

### 3. Specific-Failure Circuit Breaker

Trip on specific failure types regardless of rate.

| Failure Type | Response |
|--------------|----------|
| Security violation | Immediate trip, manual reset required |
| Data corruption | Immediate trip, investigation required |
| Infinite loop (budget exceeded) | Trip, extend timeout on repeat |
| Capability not applicable | Trip, route to appropriate handler |

**When to use:** Critical failures that should never cascade, regardless of frequency.

### 4. Composite Circuit Breaker

Combine multiple breaker types:

```
Agent Code Generation Circuit Breaker:
├── Rate-based: >30% failure over last 20 tasks → OPEN
├── Consecutive: 5 failures in a row → OPEN
├── Specific: Any security-flagged output → OPEN (manual reset)
└── Timeout: Any of above → 15 min, then HALF-OPEN
```

## Open vs. Closed State Actions

### When Open (Agent Capability Suspended)

| Action | Purpose |
|--------|---------|
| Route tasks to human | Ensure work continues |
| Route to backup agent | Maintain automation where possible |
| Queue tasks for later | Non-urgent work can wait |
| Reject task immediately | Don't let backlog build for time-sensitive work |
| Log and alert | Visibility into failure state |
| Begin investigation | Understand why agent is failing |

### When Closed (Normal Operation)

| Action | Purpose |
|--------|---------|
| Assign tasks normally | Standard operation |
| Monitor failure rate | Detect degradation early |
| Log successes and failures | Track patterns |
| Update confidence metrics | Calibrate trust |

### Half-Open Testing Protocol

| Step | Action |
|------|--------|
| 1 | Select a low-stakes task for testing |
| 2 | Assign with higher verification than normal |
| 3 | Evaluate result carefully |
| 4 | On success, try another (up to limit) |
| 5 | On any failure, return to Open |
| 6 | After sufficient successes, return to Closed |

**Critical:** Don't test recovery with high-stakes tasks. The agent might still be failing.

## Cascade Prevention Strategies

### 1. Output Verification Before Propagation

Don't feed unverified agent output to downstream processes.

```
Bad: Agent A output → Agent B (trusts output)
Good: Agent A output → Verification → Agent B (verified input)

If verification fails:
  - Trip Agent A's circuit breaker
  - Don't propagate bad output
  - Route to human or alternative
```

### 2. Dependency-Aware Circuit Breakers

When an upstream agent trips, consider downstream effects:

| Upstream State | Downstream Effect |
|----------------|-------------------|
| Agent A: OPEN | Agents B, C, D: Consider pausing (no valid input) |
| Agent A: HALF-OPEN | Agents B, C, D: Limited operation (testing inputs) |
| Agent A: CLOSED | Agents B, C, D: Normal operation |

### 3. Blast Radius Limits

Constrain how far failure can spread:

| Level | Scope | Circuit Breaker |
|-------|-------|-----------------|
| Task | Single task | Retry limit per task |
| Agent | One agent | Per-agent circuit breaker |
| Capability | One function across agents | Per-capability breaker |
| Pipeline | Multi-agent workflow | Pipeline-level breaker |
| System | All agents | Emergency stop |

### 4. Graceful Degradation

Plan what happens when capabilities are unavailable:

| Capability | Degraded Mode |
|------------|---------------|
| Code generation | Human writes code |
| Code review | Human reviews code |
| Automated testing | Manual testing |
| Documentation | Documentation deferred |
| All agent capabilities | Human does everything (pre-agent state) |

**The system should always be able to operate in degraded mode.** Circuit breakers enforce graceful degradation rather than catastrophic failure.

## Recovery Strategies

### 1. Automatic Recovery (After Timeout)

For transient failures, automatic Half-Open testing after timeout.

**Appropriate when:**
- Failures are likely transient (network, resource contention)
- No configuration change needed
- Agent capability fundamentally works

### 2. Manual Reset Required

Some failures require human intervention before reset.

**Require manual reset for:**
- Security violations
- Data corruption
- Repeated trip (tripped multiple times in short period)
- Unknown root cause

### 3. Progressive Timeout (Exponential Backoff)

Each trip increases the Open timeout:

| Trip Count | Timeout | Rationale |
|------------|---------|-----------|
| 1 | 5 minutes | Quick test if transient |
| 2 | 15 minutes | Something more persistent |
| 3 | 1 hour | Give significant recovery time |
| 4 | 4 hours | Consider manual intervention |
| 5+ | Manual reset | Clearly a deeper problem |

### 4. Canary Recovery

In Half-Open, test with a canary task specifically designed to detect the failure mode:

```
Agent failed on: Complex multi-file refactoring
Canary test: Small, targeted refactoring that exercises same patterns
If canary passes: Allow limited real tasks
If canary fails: Back to Open, targeted investigation
```

## What Circuit Breakers Reveal About Agent Supervision

### 1. Trust Is Dynamic, Not Binary

The circuit breaker embodies dynamic trust:
- Closed: High trust, full autonomy
- Open: Low trust, capability suspended
- Half-Open: Calibrating trust, testing

This matches how humans manage trust - it can be lost quickly but must be rebuilt gradually.

### 2. Fail Fast Is Kindness

Letting agents continue to fail wastes:
- Compute resources on doomed tasks
- Human attention on reviewing bad output
- Downstream effort built on bad foundations

Failing fast is more efficient and prevents cascade damage.

### 3. Isolation Enables Resilience

Bulkheads between agent capabilities allow:
- Partial system operation during failures
- Independent recovery paths
- Clearer diagnosis (which capability failed?)

### 4. Recovery Requires Testing

You can't know if an agent is recovered until you test it. The Half-Open state formalizes this - don't fully trust until verified.

### 5. Manual Intervention Is Part of the System

Circuit breakers include manual reset by design. Some failures require human judgment. This isn't a failure of automation - it's proper separation of automated handling from human judgment.

## Anti-Patterns

### 1. No Circuit Breaker (Blind Retry)

```
Task fails → Retry immediately → Fails → Retry → Fails → Retry...
```

**Problem:** Wastes resources, never gives system time to recover, can accelerate failure.

### 2. Circuit Breaker Too Sensitive

```
Single failure → OPEN → Long timeout
```

**Problem:** Trips on normal variance. Too much downtime for non-problems.

### 3. Circuit Breaker Too Insensitive

```
10 failures → Still CLOSED
```

**Problem:** Doesn't trip until significant damage done. Defeats the purpose.

### 4. No Half-Open State (Binary)

```
CLOSED ←→ OPEN (jump directly based on time)
```

**Problem:** No testing of recovery. May be assigning to still-broken agent.

### 5. One Breaker for Everything

```
Single circuit breaker for all agent capabilities
```

**Problem:** One failing capability takes down all capabilities. No isolation.

### 6. Ignoring the Open State

```
Circuit trips → Continue assigning tasks anyway
```

**Problem:** Defeats the entire purpose. Just a logging mechanism at this point.

## Practical Implementation Considerations

### What to Track

| Metric | Purpose |
|--------|---------|
| Failure rate per capability | Detect degradation |
| Time in each state | Understand failure patterns |
| Trips per time period | Identify chronically failing capabilities |
| Recovery success rate | Half-Open → Closed vs Half-Open → Open |
| Time to detection | How long until circuit trips after failure begins |

### Tuning Parameters

Start conservative (trip easily), tune based on data:

| Parameter | Too Low | Too High |
|-----------|---------|----------|
| Failure threshold | Trips on normal variance | Trips too late, damage done |
| Open timeout | Constant testing, no recovery time | Long outages for transient issues |
| Half-Open limit | Not enough testing to confirm recovery | Too many tasks to failed agent |

### Human Interface

Supervisors need visibility into circuit breaker state:

```
Agent Status Dashboard:
┌────────────────────────────────────────────────────┐
│ Agent: code-gen-1                                  │
│ State: HALF-OPEN (testing recovery)                │
│ Last trip: 2024-01-15 14:32 UTC                    │
│ Trip reason: 4 consecutive verification failures   │
│ Test tasks: 1/2 successful                         │
│ Action: [Force Close] [Force Open] [View History]  │
└────────────────────────────────────────────────────┘
```

## Connection to Other Frameworks

### Circuit Breaker + Cynefin

| Cynefin Domain | Circuit Breaker Approach |
|----------------|--------------------------|
| Clear | Tight thresholds, fast trips (known failure modes) |
| Complicated | Medium thresholds, expert analysis when tripped |
| Complex | Looser thresholds, more Half-Open testing (learning) |
| Chaotic | Immediate trip, manual reset (stabilize first) |

### Circuit Breaker + Principal-Agent

Circuit breakers address the "hidden action" problem:
- Agent's internal failures become externally visible via output verification
- Circuit breaker makes failure response systematic rather than ad-hoc
- Trust calibration becomes measurable (state transitions)

### Circuit Breaker + OODA Loop

Circuit breaker as Observe + Decide:
- Observe: Track failure metrics
- Orient: Interpret against thresholds
- Decide: Trip/Close/Test
- Act: Change task routing

Fast OODA loop on agent capability enables fast response to degradation.

## Open Questions

1. **Failure detection latency:** How quickly can we detect agent failure? For some failure modes (subtle bugs), detection might be slow. Does circuit breaker pattern work with delayed feedback?

2. **Soft failure calibration:** What failure rate is acceptable? 10%? 5%? 1%? Depends on stakes, verification cost, alternative cost.

3. **Multi-agent dependency:** If Agent A trips, should downstream agents enter a "waiting" state rather than fully Open? What's the dependency-aware circuit breaker?

4. **Capability vs agent breaker:** Should breakers be per-agent or per-capability? If Agent A is bad at refactoring but good at tests, should refactoring capability trip while tests continue?

5. **Retraining signal:** When a circuit breaker trips repeatedly, what's the signal to underlying model training? Does this pattern reveal systematic capability gaps?

6. **Human-in-loop as Half-Open:** Could "route to human" be a permanent Half-Open state rather than Open? Human verifies while agent attempts?

7. **Proactive tripping:** Should circuit breakers trip proactively when conditions suggest failure is likely, before failures occur? (E.g., unusual input patterns)

## Systems to Build

- [ ] **Failure tracking per capability:** Log and aggregate failure rates by agent capability
- [ ] **Circuit breaker state machine:** Implement Closed/Open/Half-Open transitions
- [ ] **Routing based on state:** Task router respects circuit breaker state
- [ ] **Supervisor dashboard:** Visibility into all circuit breaker states
- [ ] **Canary task library:** Pre-defined test tasks for Half-Open validation
- [ ] **Cascade detector:** Identify when failures are propagating through pipeline
- [ ] **Alert on trip:** Notify supervisors when capabilities degrade
- [ ] **Historical analysis:** Track circuit breaker patterns over time to identify systematic issues

## Summary

The Circuit Breaker pattern prevents cascade failures in distributed systems by failing fast when components are unhealthy. For agent supervision, this translates to:

**Key insight:** An agent capability that is failing should be suspended quickly, not retried endlessly. The goal is to prevent bad output from cascading through dependent systems and to give the underlying capability time to recover.

**The three states:**
- **Closed:** Normal operation, monitoring for failures
- **Open:** Capability suspended, routing to alternatives, failing fast
- **Half-Open:** Testing recovery with limited, verified attempts

**Core principles:**
1. **Fail fast:** Better to immediately route to alternative than wait for slow failure
2. **Prevent cascade:** Don't let one failing agent poison downstream work
3. **Bulkheads:** Isolate failures by capability so partial operation continues
4. **Test recovery:** Don't blindly trust that agents have recovered - verify
5. **Dynamic trust:** Trust can be lost quickly but must be rebuilt through demonstrated success

**The pattern reveals:** Trust in agents should be operationalized as a state machine with defined transitions, not a vague feeling. When an agent starts failing, there should be a systematic response, not ad-hoc human judgment for each failure.

## Status

**Phase:** Initial exploration complete. Core pattern mapped to agent supervision. Key insight is that agent capabilities should be treated like services - monitored for failure, suspended when unhealthy, and tested before restoration. This prevents the cascade failure mode where one failing agent produces garbage that infects all downstream work.

**Next:** Implement failure tracking per agent capability and build basic circuit breaker state machine.
