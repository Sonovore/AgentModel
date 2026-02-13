# Information Flow and Overload Management: Cross-Disciplinary Synthesis

## Problem Statement

### Why This Matters

Information flow is the circulatory system of multi-agent coordination. Without effective information flow, agents operate in silos with stale context, make conflicting decisions, duplicate work, and miss dependencies. With excessive information flow, agents drown in noise, context windows saturate, coordinators become bottlenecks, and signal gets lost in the flood.

The challenge is not simply "share more" or "share less"---it is ensuring **the right information reaches the right agents at the right time without overwhelming them**.

### When This Occurs in Multi-Agent Systems

Information flow challenges emerge whenever:
- Agents work on interdependent tasks requiring awareness of each other's state
- Coordinators/orchestrators must aggregate information from multiple agents
- Decisions require combining knowledge distributed across agents
- System state changes that affect multiple agents simultaneously
- Agents need context from prior work to continue tasks

### What Breaks If You Get It Wrong

**Too little information flow:**
- Conflicting actions: Agent A and B modify the same file without awareness
- Duplicated work: Agents solve the same problem independently
- Missed dependencies: Agent proceeds with stale assumptions
- Incoherent output: Individual outputs don't fit together

**Too much information flow:**
- Coordinator bottleneck: Everything waits for hub to process
- Context saturation: Agents can't fit essential information in context window
- Signal dilution: Important updates lost in noise
- Processing overhead: More time coordinating than executing

### Scope and Boundaries

This synthesis addresses:
- What information to share (filtering and prioritization)
- How to share it (push vs. pull, channels, hierarchies)
- Where information flows (hub architectures, peer patterns)
- When to share (event-driven vs. polling vs. batch)

It does not deeply address:
- Task decomposition (separate synthesis)
- Conflict resolution once detected (separate synthesis)
- Temporal synchronization mechanisms (separate synthesis)

---

## Perspectives

### Perspective 1: Silo Awareness (Incident Response)

**Core Insight:**
Silos in agent systems are a **coordination problem operating under fundamental constraints**, not simply an information-sharing problem. The solution is not "share more" but "share what changes what others should do."

**Mechanisms and How It Works:**

1. **Coordination Relevance Filtering:** Share information when it is coordination-relevant:
   - File modification (shared state change)
   - Objective completion (unblocks other work)
   - Constraint discovery (affects assumptions)
   - Anomaly detection (may indicate broader issues)
   - Conflict identification (requires resolution)

2. **Event-Driven Updates:** Replace continuous broadcasting and polling with event-triggered sharing:
   ```
   EVENT: file_modified
     IF file in shared_files:
       NOTIFY agents subscribed to file
       INCLUDE: file_path, change_summary, intent
   ```

3. **Publish-Subscribe Model:** Let receivers declare interest rather than senders guessing:
   - Agents subscribe to relevant topics
   - Publishers post to topics, not specific agents
   - Decouples sender from receiver knowledge

4. **Transactive Memory:** Maintain explicit registry of who knows what:
   - Capability registry: What each agent can do
   - Knowledge accumulation log: What agents have learned
   - Query routing: How to find the right agent for a question

**When It Works, When It Fails:**
- Works when coordination events are identifiable in advance
- Works when agents can subscribe to relevant topics
- Fails when coordination relevance requires judgment
- Fails when novel situations don't fit defined event types

**Scaling Characteristics:**
- 2-3 agents: Direct communication viable
- 4-10 agents: Need coordination infrastructure, selective awareness
- 10+ agents: Hierarchical coordination, stigmergy essential

**Key Takeaways for Agents:**
- Don't share everything; share what changes what others should do
- Event-driven beats polling beats broadcasting
- Know who knows what (transactive memory)
- Coordinate through artifacts when direct communication is expensive (stigmergy)

---

### Perspective 2: Commander's Critical Information Requirements (Military Command)

**Core Insight:**
Information requirements exist to support **decisions**. Every piece of information reaching the commander should trace back to a specific decision point. Define in advance what information the commander needs---not "what might be useful" but "what will change a decision."

**Mechanisms and How It Works:**

1. **CCIR Framework:** Two types of critical information:
   - **Priority Intelligence Requirements (PIR):** External environment, threats, conditions
   - **Friendly Force Information Requirements (FFIR):** Internal status, capabilities, readiness

   For agents:
   - PIR equivalent: Environment state, external system status, user requirements
   - FFIR equivalent: Agent health, progress, confidence, capability limits

2. **Decision-Point Linkage:** Every requirement traces to a decision:
   - "If enemy reserve uncommitted by H+4, execute Branch A" (PIR)
   - "If lead battalion below 70% combat power, commit reserve" (FFIR)

   For agents:
   - "If agent confidence drops below 0.7, require human approval"
   - "If task duration exceeds 10 minutes, escalate"

3. **Multi-Stage Alerting:** Graduated escalation levels:
   - **Blocking:** Stop and wait for decision (destructive operations)
   - **Immediate notification:** Continue but alert now (unexpected state)
   - **Batched notification:** Include in next summary (progress updates)
   - **Logged only:** Record but don't notify (routine operations)

4. **Battle Rhythm:** Structured process for filtering and presenting information:
   - Battle Captain accepts "the burden of filtering and redistributing information"
   - Scheduled touchpoints for information flow
   - Running estimates maintain continuous context

**When It Works, When It Fails:**
- Works for predictable decision types with known triggers
- Works when thresholds can be defined explicitly
- Fails for genuinely novel situations outside defined patterns
- Fails when defining thresholds requires contextual judgment

**Scaling Characteristics:**
- Scales through explicit filtering and hierarchical staff processes
- Information compresses at each level (detail to status to aggregate)
- Running estimates maintain context without overwhelming

**Key Takeaways for Agents:**
- Start with decisions, not information: What decisions need to be made? What information triggers them?
- Define thresholds explicitly: "Notify if X > Y" not "notify if important"
- Graduated escalation: Not everything is equally urgent
- The supervisor sees insights, not data: Transform information at each level

---

### Perspective 3: Multi-Channel Communication (Orchestral Conducting)

**Core Insight:**
A conductor doesn't use a single command channel---they operate **multiple parallel channels with different bandwidths, latencies, and reliability characteristics**. Channel specialization enables parallel transmission while redundancy provides robustness.

**Mechanisms and How It Works:**

1. **Channel Specialization:** Different channels for different information types:
   | Channel | Information Type | Characteristics |
   |---------|-----------------|-----------------|
   | Right hand (baton) / Event bus | Temporal synchronization | High frequency, low latency, highest reliability |
   | Left hand / Configuration | Behavioral modulation | Medium frequency, medium latency |
   | Eyes / Direct calls | Targeted attention | Low frequency, high reliability when used |
   | Face / Metadata | Qualitative context | Low frequency, high latency tolerance, OK to miss |
   | Body / System mode | Operational baseline | Very low frequency, context for other signals |
   | Breathing / Heartbeat | Preparation, liveness | Episodic, triggers immediate response |

2. **Priority Hierarchy for Conflict Resolution:**
   ```
   1. Event bus (temporal coordination) - highest
   2. Heartbeat (liveness)
   3. Direct calls (targeted)
   4. Configuration (behavioral)
   5. Metadata (qualitative)
   6. System mode (baseline) - lowest
   ```
   When channels conflict, higher priority wins.

3. **Redundant Transmission for Critical Information:**
   - Critical: Transmit through 3+ channels (event + config + direct call)
   - Important: Transmit through 2 channels (event + config)
   - Standard: Single channel with logging
   - Informational: Metadata only, no acknowledgment

4. **Graceful Degradation Hierarchy:**
   - Level 0: Full function (all channels)
   - Level 1: Metadata loss (lose qualitative context)
   - Level 2: Configuration loss (use defaults)
   - Level 3: Direct call loss (broadcast only)
   - Level 4: Event bus degradation (reduce parallelism)
   - Level 5: Event bus failure (agents independent)

**When It Works, When It Fails:**
- Works when channel characteristics match information needs
- Works when redundancy compensates for individual channel failure
- Fails when channels are overloaded (wrong information in wrong channel)
- Fails when priority hierarchy doesn't match actual priorities

**Scaling Characteristics:**
- Scales through channel separation (parallel processing)
- Hierarchical event buses for large scale
- Topic partitioning and filtering manage subscriber load

**Key Takeaways for Agents:**
- Match channel to information type: Don't put time-critical data in slow channels
- Build explicit priority hierarchy: Deterministic conflict resolution
- Redundancy for critical info: Don't rely on single channel
- Design for degradation: Know how system behaves as channels fail

---

### Perspective 4: Central Communication Hub (Theater Stage Management)

**Core Insight:**
The stage manager's authority derives from being the only entity with the **complete operational picture**. Hub-and-spoke architecture trades distributed coordination complexity for centralized information processing---but the hub is inherently a bottleneck to design around, not fix.

**Mechanisms and How It Works:**

1. **Hub-and-Spoke Architecture:**
   - Orchestrator maintains complete operational state
   - Routes all cross-agent coordination
   - Makes all coordination decisions
   - Agents focus on execution, not coordination

2. **Aggressive Information Filtering:**
   - Exception-based reporting: Silence = nominal
   - Threshold-based escalation: Only deviations above threshold
   - Standardized formats: ACK, PROGRESS, COMPLETE, ERROR, BLOCKED

   ```python
   def should_report(event: Event) -> bool:
       if event.is_state_change(): return True
       if event.is_error() or event.is_blocked(): return True
       if event.duration > expected_duration * 1.5: return True
       if event.error_rate > 0.05: return True
       return False  # Don't report routine progress
   ```

3. **Warning-Standby-Go Protocol:**
   - Warning (60s): Task coming, prepare
   - Standby (10s): Imminent, confirm ready
   - Go: Execute now

   Spreads coordination load over time; reduces hub peak load.

4. **Hierarchical Hub Structure for Scale:**
   ```
   Meta-Orchestrator (global coordination)
   ├── Domain Orchestrator A (local coordination)
   │   ├── Agent A1
   │   └── Agent A2
   └── Domain Orchestrator B
       └── Agent B1
   ```
   Each level has bounded complexity (~8 reports maximum).

**When It Works, When It Fails:**
- Works when coordination complexity justifies centralization
- Works when filtering prevents hub overload
- Fails when hub becomes processing bottleneck
- Fails when hub fails (single point of failure)

**Scaling Characteristics:**
- Horizontal: ~20 agents per orchestrator with aggressive filtering
- Hierarchical: Add domain orchestrators for larger scale
- Each level filters before escalating

**Key Takeaways for Agents:**
- Informational centrality is non-negotiable: Hub must see everything coordination-relevant
- Filtering is essential: Without filtering, hub overloads
- Plan for hub failure: Agents need autonomous modes
- Pre-plan reduces runtime load: Decide in planning what you can

---

### Perspective 5: Chain of Command Routing (Kitchen Brigade)

**Core Insight:**
Hierarchical routing through a coordinator achieves better coordination than unrestricted peer communication **when coordination complexity is high**. Constraint creates capability: By restricting communication to defined channels, complexity becomes tractable.

**Mechanisms and How It Works:**

1. **Hierarchical Routing Rules:**
   - Upward (Execution to Orchestrator): Completion, failure, blocking, escalation
   - Downward (Orchestrator to Execution): Dispatch, priority, configuration
   - Lateral (Peer to Peer): Only within approved scope (coordinated task, bounded interaction)
   - Broadcast: Emergency only

2. **Information Transformation at Each Level:**
   ```
   Execution agent report:
     files_processed: 127, files_remaining: 43, current_file: "parser.py"

   Orchestrator receives:
     progress_percent: 75, status: "in_progress", health: "green"
   ```
   Detail at execution level, abstracted status at coordination level.

3. **Acknowledgment Protocol:**
   Every dispatch requires ACK:
   ```
   Orchestrator: dispatch(task_123)
   Agent: ack(task_123, accepted)
   ...
   Agent: status(task_123, complete, result)
   Orchestrator: status_ack(task_123)
   ```
   ACK closes the loop; without it, orchestrator must poll.

4. **Approved Lateral Communication:**
   Peer communication only when:
   - Orchestrator established coordination frame (both agents assigned related tasks)
   - Interaction scope is bounded (single hand-off, no priority implications)
   - Both report completion to orchestrator

**When It Works, When It Fails:**
- Works when coordination complexity is O(n^2) with peer communication
- Works when synchronization requires single source of truth
- Fails for time-critical paths (multi-hop latency)
- Fails when routing rules don't cover all situations

**Scaling Characteristics:**
- Single orchestrator: 8 agents or less
- Regional coordinators: 9-25 agents (3-5 per region)
- Multi-level hierarchy: 26+ agents
- Each routing level adds ~100ms latency

**Key Takeaways for Agents:**
- Hierarchical by default, peer by exception
- Coordinator coordinates, agents execute: Clear role separation
- ACK closes every loop: No polling, no uncertainty
- Explicit transformation rules: Define what changes at each level

---

### Perspective 6: Distributed Expertise with Central Coordination (NASA Mission Control)

**Core Insight:**
Central coordination is fundamentally an **information aggregation problem bounded by what can flow through the coordinator**. The orchestrator is inherently a bottleneck---this is structural, not a bug to fix. Design must work with this constraint.

**Mechanisms and How It Works:**

1. **Context Window Budget:**
   ```
   Total context budget: 100%
   - Task definition + constraints: ~10%
   - Relevant background/context: ~20%
   - Working space for agent: ~50%
   - Output space: ~20%

   If background exceeds 20%, either:
   - Compress more aggressively
   - Break into smaller tasks
   - Accept partial context
   ```

2. **What Agents Should Report:**
   - Essential (always): Status, confidence, key findings, dependencies, scope boundaries
   - Conditional (if present): Unexpected findings, cross-agent implications
   - Not essential (filter): Detailed reasoning, raw data, intermediate steps

3. **Bottleneck Prevention Strategies:**
   - Exception-based reporting: Only report when notable
   - Direct agent-to-agent handoffs: Where possible without orchestrator
   - Hierarchical orchestration: Domain orchestrators for bounded scope
   - Decision delegation: Define what agents decide autonomously
   - Batch coordination: Discrete checkpoints vs. continuous involvement

4. **Information Aggregation Patterns:**
   - Confidence-weighted integration: Higher confidence inputs weighted more
   - Conflict detection: Check all agent pairs for contradictions
   - Gap detection: Which sub-goals have no agent output?

**When It Works, When It Fails:**
- Works when coordination matched to orchestrator capacity
- Works when information compression preserves decision-relevant content
- Fails when orchestrator can't evaluate specialist outputs
- Fails when implicit context isn't explicitly transferred

**Scaling Characteristics:**
- 2-3 agents: Minimal coordination overhead
- 4-10 agents: Structured protocols, batch coordination
- 10-30 agents: Hierarchical orchestration, domain grouping
- 30+ agents: Multi-tier hierarchy, federated structure

**Key Takeaways for Agents:**
- Minimize what flows through orchestrator: Reserve capacity for true coordination
- Match coordination to orchestrator capacity: Add hierarchy if exceeded
- Make information flow explicit: Don't assume shared context
- Build for aggregation challenges: Expect conflicts, gaps, uncertainty

---

### Perspective 7: Technology-Augmented Decision-Making (Emergency Dispatch)

**Core Insight:**
Human-agent coordination is itself a technology-augmented decision-making problem. The same dynamics---**automation bias, trust calibration, information overload**---that affect humans working with decision support affect humans supervising agents. These dynamics also apply recursively to agents using tools and other agents.

**Mechanisms and How It Works:**

1. **Trust Calibration for Information:**
   | Trust State | Human-Agent Manifestation |
   |-------------|--------------------------|
   | Calibrated | Trust matches agent reliability for task type |
   | Over-trust | Accept agent work without review (automation bias) |
   | Under-trust | Duplicate agent work unnecessarily |

   Trust should vary by task type, change over time, depend on context.

2. **Levels of Automation for Information Flow:**
   | Level | Agent Role | Information Requirement |
   |-------|-----------|------------------------|
   | 4 | Agent suggests approach | Full reasoning and alternatives |
   | 5 | Agent executes if approved | Summary for review |
   | 6 | Agent executes unless vetoed | Exception notification |
   | 7 | Agent executes, then informs | Post-action summary |

3. **Preventing Information Bias:**
   - **Anchoring**: Agent recommendations serve as anchors---require alternatives
   - **Attention tunneling**: Focus on recommendation, miss context---require broader view
   - **Automation bias**: Accept without evaluation---require sampling reviews

4. **Agent-to-Agent Information Trust:**
   Agents must calibrate trust in tools and other agents:
   ```
   Source Reliability:
   - Test results: High (accept if passing)
   - Compiler output: High (ground truth)
   - Documentation: Medium (verify against code)
   - Comments: Low (may be outdated)

   When Sources Conflict:
   - Investigate which more likely correct
   - If can't resolve, escalate to human
   ```

**When It Works, When It Fails:**
- Works when trust is calibrated and maintained through feedback
- Works when humans maintain situational awareness
- Fails when automation bias leads to rubber-stamping
- Fails when skill degradation makes humans unable to evaluate agent work

**Scaling Characteristics:**
- 1-2 agents: Detailed human review possible
- 3-5 agents: Sampling-based review
- 6-10 agents: Statistical oversight
- 10+ agents: Outcome-based oversight, meta-agents checking agents

**Key Takeaways for Agents:**
- Trust calibration is central: Neither over-trust nor under-trust works
- Information should support human decision, not replace it
- Explain reasoning to enable evaluation
- Recursively: Agents using tools face same dynamics

---

## Cross-Cutting Patterns

### What All Perspectives Agree On

1. **Filtering is essential, not optional.**
   Every discipline recognizes that unfiltered information flow destroys coordination:
   - Military: "CCIR focuses only on what changes decisions"
   - Theater: "Exception-based reporting; silence = nominal"
   - Kitchen: "Information transforms at each level"
   - Mission Control: "Minimize what flows through orchestrator"

2. **The hub/coordinator is a bottleneck by design.**
   Central coordination enables coherence but creates a structural bottleneck:
   - All seven perspectives identify coordinator capacity as a limit
   - Solutions include filtering, hierarchy, delegation, batching
   - None propose eliminating the bottleneck; all propose managing it

3. **Information must be relevant to coordination, not comprehensive.**
   Share what changes what others should do:
   - Incident Response: "Coordination-relevant events, not everything"
   - Military: "Decision-linked information only"
   - Mission Control: "Exception-based reporting"

4. **Multiple channels beat single channels.**
   Specialization and redundancy improve robustness:
   - Orchestral: Six distinct channels with priority hierarchy
   - Theater: Party line, ISO channels, private channels
   - Kitchen: Hierarchical routing plus approved lateral

5. **Transformation at level boundaries is mandatory.**
   Information compresses as it flows up; contextualizes as it flows down:
   - Detail at execution level
   - Status at coordination level
   - Aggregate at strategic level

### Where Perspectives Diverge

1. **Push vs. Pull Information Architecture:**
   - Military (push): Commander defines information requirements; staff pushes filtered information
   - Incident Response (pull/publish-subscribe): Agents declare interests; publishers post to topics
   - Theater (push): Hub pushes all coordination; agents report status

   **Why they diverge:** Push works when information needs are predictable (military planning). Pull works when receivers know their needs better than senders (dynamic coordination).

2. **Hierarchical vs. Flat Communication:**
   - Kitchen/Theater: Strictly hierarchical; all coordination through hub
   - Jazz/Incident Response: Peer coordination acceptable; stigmergy through artifacts
   - Orchestral: Hybrid; primary hierarchy with approved peer sections

   **Why they diverge:** Hierarchy provides authority and simplicity but adds latency. Flat provides speed but creates complexity. The right choice depends on coordination complexity vs. time criticality.

3. **Explicit vs. Implicit Coordination:**
   - Military/Theater: Highly explicit; every coordination point defined
   - Jazz: Highly implicit; shared conventions enable coordination without messaging
   - Mission Control: Explicit with implicit shared mental models

   **Why they diverge:** Explicit coordination is reliable but expensive. Implicit coordination is efficient but requires established shared understanding. Teams with shared experience can use more implicit; ad-hoc teams need explicit.

### Synthesis: A Unified Framework

**The Information Flow Triad:**

```
                    WHAT to share
                         |
                  (Filtering)
                         |
    HOW to share ----+-------- WHEN to share
         |                           |
    (Channels)                 (Timing)
         |                           |
    (Hierarchy)               (Events)
```

**Filtering (What):**
- Filter by coordination relevance, not importance
- Define triggers explicitly (thresholds, events)
- Transform at level boundaries (detail to status to aggregate)
- Default to not sharing; require justification to share

**Channels (How):**
- Match channel to information characteristics
- Specialize channels by function (temporal, behavioral, targeted)
- Build redundancy for critical information
- Define priority hierarchy for conflicts

**Timing (When):**
- Event-driven for coordination-relevant changes
- Batch for routine status at checkpoints
- Push for urgent; pull for non-urgent
- Preparation signals before coordinated action

---

## Scaling Analysis

### Small Scale (3-10 Agents)

**What Works:**
- Single orchestrator with direct communication
- All-to-all awareness possible
- Flat coordination viable
- Minimal filtering needed

**Patterns:**
- Hub-and-spoke with exception-based reporting
- Publish-subscribe for topic-based coordination
- Warning-standby-go for synchronized actions

**Metrics:**
- Coordinator utilization < 50%
- Agent wait time < 10% of execution time
- Information overhead < 20% of total tokens

### Medium Scale (10-50 Agents)

**What Changes:**
- Direct communication creates O(n^2) overhead
- Single orchestrator approaches capacity limit
- Need hierarchical structure
- Filtering becomes essential

**Patterns:**
- Domain orchestrators with meta-orchestrator
- Bounded complexity per coordinator (~8 direct reports)
- Explicit transformation rules at each level
- Multi-channel architecture with priority hierarchy

**Transition Triggers:**
- Coordinator utilization > 70%
- Agent wait time > 20% of execution time
- Queue depth growing consistently

**Metrics:**
- Per-orchestrator agent count < 10
- Cross-domain coordination < 20% of total
- Escalation rate 10-25%

### Large Scale (50-1000+ Agents)

**What Changes:**
- Human oversight becomes statistical, not comprehensive
- Need multiple hierarchy levels
- Stigmergic coordination through artifacts essential
- Information filtering is primary design concern

**Patterns:**
- Multi-tier orchestration hierarchy
- Federated structure with domain autonomy
- Event-driven publish-subscribe at scale
- Meta-agents checking agents (automation of oversight)

**Transition Triggers:**
- Human can't review more than sampling
- Cross-domain conflicts frequent
- Coordination latency exceeds task latency

**Metrics:**
- Human oversight: outcome-based, not process-based
- Information loss rate < 5% for critical
- Cascade failure containment within domains

### What Changes and Why at Each Transition

| Transition | Problem | Solution |
|------------|---------|----------|
| 3-10 to 10-50 | Hub overload | Add hierarchy; filter more aggressively |
| 10-50 to 50+ | Human oversight limit | Statistical sampling; meta-agent checking |
| 50+ to 1000+ | Coordination latency | Stigmergy; domain autonomy; outcome-based oversight |

---

## Decision Framework

### When to Use Which Approach

**Push vs. Pull:**
| Use Push When | Use Pull When |
|---------------|---------------|
| Information needs predictable | Receiver knows needs better |
| Time-critical coordination | Exploration or research tasks |
| Clear authority gradient | Peer coordination acceptable |
| Failure means missing critical info | Failure means redundant work |

**Hierarchical vs. Flat:**
| Use Hierarchical When | Use Flat/Peer When |
|----------------------|-------------------|
| Coordination complexity high | Coordination bounded/local |
| Authority resolution needed | No priority conflicts |
| Single source of truth required | Domain expertise symmetric |
| Cross-agent dependencies | Hand-off within established frame |

**Explicit vs. Implicit:**
| Use Explicit When | Use Implicit When |
|------------------|-------------------|
| Novel team/agents | Established shared models |
| High stakes | Routine operations |
| Audit trail required | Speed is critical |
| Trust not yet established | Trust calibrated over time |

### Context Factors That Drive Choices

1. **Coordination Complexity:** How many agents need to coordinate? How complex are dependencies?
   - High complexity -> hierarchical, explicit, filtered
   - Low complexity -> flat, implicit, comprehensive

2. **Time Criticality:** How urgent is coordination? What's the latency budget?
   - High urgency -> push, flat/approved peer, pre-planned
   - Low urgency -> pull, hierarchical, adaptive

3. **Consequence Severity:** What happens if coordination fails?
   - High stakes -> explicit, redundant, human-in-loop
   - Low stakes -> implicit, single channel, autonomous

4. **Trust Level:** How calibrated is trust between agents and with human?
   - Low trust -> explicit, comprehensive reporting
   - High trust -> implicit, exception-based

5. **Agent Heterogeneity:** How different are agent capabilities and domains?
   - High heterogeneity -> transformation at boundaries, domain orchestrators
   - Low heterogeneity -> uniform protocols, flat structure

### Decision Matrix

| Context | Information Flow Pattern |
|---------|-------------------------|
| High complexity + high stakes | Hub with aggressive filtering, explicit protocols, redundant channels |
| High complexity + low stakes | Hub with exception reporting, implicit where trained |
| Low complexity + high stakes | Flat with comprehensive sharing, explicit handoffs |
| Low complexity + low stakes | Flat with implicit coordination, minimal filtering |
| Time-critical + coordinated | Pre-planned, push, preparation signals |
| Time-critical + independent | Stigmergy, post-hoc reconciliation |

---

## Implementation Checklist

### Phase 1: Define Information Architecture

- [ ] Identify coordination-relevant events (what triggers need to share)
- [ ] Define information types and their characteristics
- [ ] Choose push vs. pull for each type
- [ ] Define channels and their specialization
- [ ] Establish priority hierarchy for conflicts

### Phase 2: Implement Filtering

- [ ] Define filtering rules (thresholds, event types)
- [ ] Implement exception-based reporting (silence = nominal)
- [ ] Define transformation rules at level boundaries
- [ ] Establish escalation criteria (what reaches each level)
- [ ] Create standardized message formats

### Phase 3: Build Hub Infrastructure

- [ ] Implement orchestrator state management
- [ ] Define acknowledgment protocols
- [ ] Build multi-channel communication
- [ ] Implement graceful degradation
- [ ] Plan for hub failure (agent autonomy modes)

### Phase 4: Scale Preparation

- [ ] Define hierarchy triggers (when to add levels)
- [ ] Design domain boundaries
- [ ] Build cross-domain coordination protocols
- [ ] Implement metrics and monitoring
- [ ] Create capacity planning model

### Phase 5: Operational Excellence

- [ ] Monitor hub utilization and queue depth
- [ ] Track information loss rate
- [ ] Measure coordination latency
- [ ] Calibrate trust through feedback
- [ ] Iterate on filtering rules based on outcomes

### Success Criteria

- Coordinator utilization < 70% sustained
- Agent wait time < 20% of execution time
- Information overhead < 30% of total tokens
- Critical information delivery > 99%
- Coordination failure rate < 5%

---

## Failure Mode Taxonomy

### Information Sharing Failures

| Failure Mode | Root Cause | Symptoms | Detection | Recovery |
|--------------|------------|----------|-----------|----------|
| **Broadcast overload** | Sharing everything | Context saturation, slow performance | Context utilization > 90% | Event filtering, subscription model |
| **Information starvation** | Sharing nothing | Conflicts, duplicated work | Conflict rate > 10% | Event-driven updates, pull mechanisms |
| **Semantic misalignment** | Same terms, different meanings | Apparent agreement, incoherent results | Integration failures | Shared vocabulary, interpretation protocols |
| **Stale information** | No update mechanism | Actions based on outdated state | Decisions contradict current state | State verification, staleness detection |
| **Partial propagation** | Incomplete distribution | Some agents informed, others not | Inconsistent agent behavior | Subscription verification, broadcast logs |

### Hub/Coordinator Failures

| Failure Mode | Root Cause | Symptoms | Detection | Recovery |
|--------------|------------|----------|-----------|----------|
| **Hub overload** | Volume exceeds capacity | Queue depth growing, latency increasing | Queue > 20, latency > 2x baseline | Filtering, hierarchy, load shedding |
| **Hub unavailable** | Crash or network failure | Agents can't coordinate | Heartbeat timeout | Failover, agent autonomy mode |
| **Hub state corruption** | Update failure, race condition | Incorrect decisions | State consistency checks | State validation, recovery from persistent store |
| **Authority ambiguity** | Multiple hubs, unclear boundaries | Conflicting decisions | Agents receiving conflicting instructions | Clear authority rules, single coordinator per scope |

### Channel Failures

| Failure Mode | Root Cause | Symptoms | Detection | Recovery |
|--------------|------------|----------|-----------|----------|
| **Channel saturation** | Traffic exceeds capacity | Delays, dropped messages | Latency spike, throughput drop | Reduce traffic, increase capacity |
| **Channel cross-contamination** | Wrong info in wrong channel | Event bus carrying rich data | Content audit | Strict channel discipline |
| **Channel conflict** | Channels send incompatible info | Contradictory instructions | Conflict logging | Apply priority hierarchy |
| **Single channel failure** | Partial infrastructure failure | Some info not delivered | Channel health checks | Redundant transmission on remaining |
| **Cascade failure** | One failure overloads others | Sequential channel failures | Correlated health degradation | Circuit breakers, load shedding |

### Trust and Calibration Failures

| Failure Mode | Root Cause | Symptoms | Detection | Recovery |
|--------------|------------|----------|-----------|----------|
| **Automation bias** | Over-trust in agents | Rubber-stamping, missed errors | Error catch rate < 60% | Sampling reviews, calibration events |
| **Under-trust** | Insufficient trust | Duplicated work, slow progress | Override rate > 40% | Build trust through demonstrated performance |
| **Trust transfer** | Trust from one context to another | Trust novel tasks like routine | Errors on novel tasks | Task-specific trust levels |
| **Skill degradation** | Humans rely on agents | Can't function without agents | Manual mode failure | Deliberate skill maintenance |

### Diagnostic Decision Tree

```
SYMPTOM: Information flow problem

CHECK: Are agents getting necessary information?
  NO -> Information starvation
    - Add event-driven updates
    - Implement pull mechanisms
    - Check subscription coverage

  YES -> CHECK: Are agents getting too much information?
    YES -> Information overload
      - Implement filtering rules
      - Move to exception-based reporting
      - Add transformation at levels

    NO -> CHECK: Is information arriving in time?
      NO -> Latency problem
        - Check channel saturation
        - Reduce hierarchy depth
        - Pre-plan where possible

      YES -> CHECK: Is information being interpreted correctly?
        NO -> Semantic misalignment
          - Add shared vocabulary
          - Implement interpretation protocols
          - Verify understanding

        YES -> CHECK: Is coordinator keeping up?
          NO -> Hub bottleneck
            - Increase filtering
            - Add hierarchy levels
            - Delegate decisions

          YES -> Coordination protocol issue
            - Review coordination mechanisms
            - Check priority hierarchy
            - Audit transformation rules
```

---

## Anti-Patterns

### Anti-Pattern 1: Share Everything

**What it looks like:**
- All agents broadcast all state changes to all other agents
- Full context replicated in every agent's window
- "More information is always better"

**Why it's tempting:**
- Seems thorough
- Avoids the work of defining what's relevant
- No one can blame you for not sharing

**Why it fails:**
- Context windows saturate quickly
- Signal lost in noise
- Processing overhead dominates execution
- Coordination complexity becomes O(n^2)

**What to do instead:**
- Define coordination-relevant events explicitly
- Implement exception-based reporting
- Filter by what changes what others should do

### Anti-Pattern 2: Flat Communication at Scale

**What it looks like:**
- All agents communicate directly with all other agents
- No hierarchical structure as agent count grows
- Peer negotiation for all coordination

**Why it's tempting:**
- Simpler conceptually
- No hierarchy to design
- Feels more "distributed"

**Why it fails:**
- O(n^2) communication paths
- No authority for conflict resolution
- No transformation/compression
- Debugging becomes impossible

**What to do instead:**
- Add hierarchy as coordination complexity grows
- Implement domain orchestrators for bounded scope
- Define explicit routing rules

### Anti-Pattern 3: Single Channel for Everything

**What it looks like:**
- All information flows through one channel/bus
- Same channel for urgent and routine, temporal and contextual
- No specialization by information type

**Why it's tempting:**
- Single point to monitor
- Simpler infrastructure
- No channel selection logic

**Why it fails:**
- High-frequency temporal signals compete with low-frequency context
- Priority conflicts unresolved
- No graceful degradation (one failure stops everything)
- Can't optimize channel for information type

**What to do instead:**
- Specialize channels by information characteristics
- Implement priority hierarchy
- Build redundancy for critical information

### Anti-Pattern 4: No Acknowledgment Protocol

**What it looks like:**
- Messages sent without confirmation
- Orchestrator doesn't know if agents received
- "Fire and forget" communication

**Why it's tempting:**
- Less messaging overhead
- Simpler protocols
- Faster nominal case

**Why it fails:**
- Orchestrator must poll to verify (doubles overhead)
- Lost messages create silent failures
- Can't distinguish "didn't receive" from "received but failed"
- Recovery impossible without knowing what was received

**What to do instead:**
- Implement ACK for every coordination message
- Define timeout and retry logic
- Track acknowledgment rate as health metric

### Anti-Pattern 5: Human as Only Filter

**What it looks like:**
- All agent output goes to human
- Human decides what to act on
- No automated filtering or prioritization

**Why it's tempting:**
- Human judgment for everything
- No filtering rules to define
- Feels more controlled

**Why it fails:**
- Human becomes bottleneck at scale
- Automation bias develops (rubber-stamping)
- Human loses situational awareness in volume
- No scalability path

**What to do instead:**
- Define explicit escalation criteria
- Automate filtering with human override
- Use graduated autonomy by task type
- Sample reviews instead of comprehensive

---

## Key Insights

### Insight 1: Filter by Coordination Relevance, Not Importance

Information should flow when it changes what other agents should do---not because it's "important" in abstract. A critical discovery that affects only the discovering agent needs no sharing. A trivial status update that unblocks waiting agents must flow immediately.

**The test:** "If I share this, will it change what any other agent does?" If no, don't share.

### Insight 2: The Hub Bottleneck Is Structural, Not a Bug

Central coordination provides coherence by creating a single point of aggregation. This point is inherently capacity-limited. You cannot "fix" the bottleneck; you can only manage it through filtering, hierarchy, and delegation.

**Accept this constraint and design around it, don't fight it.**

### Insight 3: Transformation at Boundaries Is Not Optional

Information must compress going up (detail to status) and contextualize going down (abstract to specific). Without explicit transformation rules, either detail overwhelms coordinators or agents lack context.

**Define transformation rules explicitly for every level boundary.**

### Insight 4: Multiple Specialized Channels Beat One General Channel

Different information types have different characteristics (frequency, latency tolerance, reliability requirement). Specializing channels enables parallel processing and graceful degradation. One channel creates contention and single point of failure.

**Match channel to information type.**

### Insight 5: Push for Urgent, Pull for Non-Urgent

Push ensures time-critical information arrives without waiting. Pull reduces unnecessary traffic for information that can wait. The choice is about timing, not volume.

**Default to pull; explicitly justify push.**

### Insight 6: Trust Must Be Calibrated and Maintained

Neither automatic trust nor automatic distrust works. Trust should vary by task type, context, and demonstrated performance. Calibration requires feedback loops and periodic verification.

**Trust is earned, maintained, and context-specific.**

### Insight 7: Implicit Coordination Requires Explicit Shared Models

Teams that coordinate without explicit messaging do so because they share mental models, conventions, and expectations. This sharing must happen first, through explicit communication or common training.

**You can't skip to implicit coordination; you must build shared models first.**

### Insight 8: Event-Driven Updates Beat Polling and Broadcasting

Polling creates latency and wastes resources checking unchanged state. Broadcasting overwhelms with irrelevant updates. Event-driven updates share when something coordination-relevant happens---the Goldilocks approach.

**Design around coordination-relevant events.**

### Insight 9: Define Thresholds Explicitly, Not "Notify When Important"

Vague escalation criteria like "notify when important" require judgment that creates inconsistency. Explicit thresholds ("notify if duration > 2x expected") enable consistent, auditable filtering.

**If you can't define a threshold, you haven't understood the requirement.**

### Insight 10: Scale by Adding Hierarchy, Not Stretching the Hub

When coordination load exceeds capacity, the solution is not a bigger hub---it's adding hierarchy. Each level has bounded complexity; scale comes from adding levels with filtering between them.

**Know your coordination capacity limits and hierarchy triggers.**

---

## Related Problems

### Information Flow Connects To:

**Coordination Without Communication:**
- Information flow enables explicit coordination
- Implicit coordination reduces information flow needs
- Shared mental models reduce information transmission requirements

**Conflict Management:**
- Information flow enables conflict detection
- Conflict resolution requires information about conflicting states
- Over-sharing can create unnecessary conflict visibility

**Temporal Coordination:**
- Timing information is a special type of information flow
- Preparation signals are information about upcoming events
- Synchronization points are information flow checkpoints

**Trust and Oversight:**
- Human oversight requires information from agents
- Trust calibration requires feedback about information quality
- Information flow design affects automation bias risk

**Scaling Coordination:**
- Information flow patterns determine scaling characteristics
- Hierarchy adds information transformation costs
- Scale transitions are often triggered by information flow problems

### Problem Dependency Order

1. **Information Flow first:** Without working information flow, nothing else coordinates
2. **Then Temporal Coordination:** Timing depends on information about state
3. **Then Conflict Management:** Detecting conflicts requires information about intentions
4. **Then Trust and Oversight:** Human oversight depends on information reaching humans

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Cross-disciplinary synthesis for multi-agent coordination research
**Status:** Complete

---

## Source Documents

### Primary Sources (7 Perspectives)

1. **Silo Awareness** (Incident Response)
   - `/docs/incident-response/silo-awareness-agent-analysis.md`
   - Focus: Coordination-relevant information sharing, publish-subscribe, transactive memory

2. **Commander's Critical Information Requirements** (Military Command)
   - `/docs/military-command/ccir.md`
   - Focus: Decision-linked requirements, filtering, graduated escalation

3. **Multi-Channel Communication** (Orchestral Conducting)
   - `/docs/orchestral-conducting/multi-channel-communication-agent-analysis.md`
   - Focus: Channel specialization, priority hierarchy, redundancy

4. **Central Communication Hub** (Theater Stage Management)
   - `/docs/theater-stage-management/central-communication-hub-agent-analysis.md`
   - Focus: Hub architecture, aggressive filtering, hierarchical structure

5. **Chain of Command Routing** (Kitchen Brigade)
   - `/docs/kitchen-brigade/chain-of-command-routing-agent-analysis.md`
   - Focus: Hierarchical routing, transformation at levels, ACK protocols

6. **Distributed Expertise with Central Coordination** (Mission Control)
   - `/docs/mission-control/distributed-expertise-central-coordination-agent-analysis.md`
   - Focus: Orchestrator bottleneck, context budgets, aggregation patterns

7. **Technology-Augmented Decision-Making** (Emergency Dispatch)
   - `/docs/emergency-dispatch/technology-augmented-decision-making-agent-analysis.md`
   - Focus: Trust calibration, automation bias, human-agent information exchange

### Cross-References

- Problem mapping: `/.claude/problem-research-mapping.md`
- Phase 2 context: `/.claude/context.md`
