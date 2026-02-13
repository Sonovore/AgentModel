# Adaptability and Context Changes: Cross-Disciplinary Synthesis

## Problem Statement

### Why This Matters

Adaptability is the meta-capability that determines whether an agent system can survive contact with reality. No plan survives unchanged, no model is complete, no environment is static. The gap between designed behavior and effective behavior in novel situations is bridged only by adaptation.

For multi-agent systems, adaptability is not just an individual agent property---it is a system property. An agent that adapts well in isolation may destabilize a coordinated system. A system of rigid agents may be more predictable but fragile. The challenge is **enabling agents to adapt appropriately: recognizing when adaptation is needed, choosing between replanning and adjustment, and evolving coordination patterns without breaking existing coordination**.

### When This Occurs in Multi-Agent Systems

Adaptation becomes necessary when:
- Environmental conditions change (dependencies fail, resources become unavailable, new constraints emerge)
- Requirements shift (scope changes, priorities reorder, success criteria evolve)
- Team composition changes (agents added, removed, or degraded)
- Mental models prove incorrect (initial understanding was wrong, patterns don't apply)
- Plans fail during execution (obstacles encountered, assumptions violated)
- Tempo must change (urgency increases, blocking conditions arise)

### What Breaks If You Get It Wrong

**Under-adaptation (rigidity):**
- Plans continue despite changed conditions, leading to wasted effort or failure
- Agents persist with incorrect mental models, compounding errors
- System cannot recover from unexpected situations
- Brittle failure modes where small changes cause total breakdown

**Over-adaptation (thrashing):**
- Constant replanning prevents execution progress
- Agents oscillate between approaches without completing any
- Coordination breaks as agents change behavior unpredictably
- Coordination overhead dominates useful work

**Misaligned adaptation (incoherent):**
- Individual agents adapt but system-wide coordination breaks
- Agents adapt at different rates, creating inconsistency
- Local adaptation optimizes against global objectives
- Recovery attempts create new failures

### Scope and Boundaries

This synthesis addresses:
- Recognizing when adaptation is needed (triggers, signals, detection)
- Deciding between replanning and execution adjustment
- Maintaining coordination during adaptation
- Meta-learning and improvement cycles
- Evolving conventions over time

It does not deeply address:
- Initial plan creation (separate from adaptation)
- Steady-state coordination (covered in other syntheses)
- Error recovery as emergency response (distinct from adaptation)

---

## Perspectives

### Perspective 1: OODA Loop (Military/Management)

**Core Insight:**
The OODA Loop (Observe-Orient-Decide-Act) frames adaptation as a continuous cycle, not a one-time adjustment. The deeper insight is that **Orient---the construction and destruction of mental models---is the center of gravity for adaptive capability**. Agents that can rapidly destroy incorrect models and build correct ones adapt faster than agents that accumulate incremental corrections.

**Mechanisms and How It Works:**

1. **Observe-Orient Feedback:**
   Observation feeds orientation, but orientation also shapes observation. Agents see what their mental model predicts; disconfirming evidence may be filtered out.

   | Observation Type | Adaptation Signal |
   |------------------|-------------------|
   | Confirming evidence | Continue current approach |
   | Disconfirming evidence | Trigger re-orientation |
   | Novel situation | Require explicit orientation |
   | Pattern violation | Signal mental model failure |

   The key: actively seek disconfirming evidence. Confirmation bias prevents adaptation.

2. **Destruction and Creation Cycle:**
   Boyd emphasized that orientation requires actively destroying inadequate mental models before building new ones. Incremental patching of flawed models compounds errors.

   ```
   Current model → Disconfirming evidence → Destroy model
                                                 ↓
   New observation ← Fresh orientation ← Creation phase
   ```

   Agents often resist model destruction (sunk cost, coordination implications). Explicit triggers for "stop and re-orient" are necessary.

3. **Implicit Guidance and Control (IG&C):**
   Experienced practitioners operate via IG&C---pattern recognition that bypasses deliberate decision. This is fast but not adaptive; it applies existing patterns without question.

   | Mode | Speed | Adaptability |
   |------|-------|--------------|
   | IG&C (pattern match) | Fast | Low (applies known patterns) |
   | Deliberate OODA | Slow | High (builds new patterns) |

   Systems need mechanisms to **interrupt IG&C when patterns don't apply**. Novel situations require deliberate orientation, not pattern matching.

4. **Tempo as Adaptation Speed:**
   Boyd's tempo concept: the ability to cycle through OODA faster than the environment changes. If the environment changes faster than agents can adapt, agents are always responding to stale conditions.

   | Tempo | Implication |
   |-------|-------------|
   | Agent OODA > Environment change rate | Agents stay ahead, adapt proactively |
   | Agent OODA < Environment change rate | Agents lag, react to obsolete situations |
   | Agent OODA << Environment change rate | Agents cannot adapt, overwhelmed |

   Adaptive capacity depends on OODA cycle time. Reducing cycle time improves adaptability up to the limit where observation quality degrades.

**When It Works, When It Fails:**
- Works when agents can observe relevant changes
- Works when agents can destroy and rebuild mental models
- Fails when observation is delayed or filtered by existing orientation
- Fails when agents resist model destruction (incestuous amplification)

**Scaling Characteristics:**
- Individual agent OODA cycles independent
- Shared orientation (Einheit) enables coordinated adaptation
- Coordination adds latency to OODA cycle
- At scale, agents must adapt at different tempos (inner/outer loops)

**Key Takeaways for Agents:**
- Adaptation requires active model destruction, not just information accumulation
- Seek disconfirming evidence to trigger necessary adaptation
- Interrupt pattern-matching (IG&C) for novel situations
- Match OODA tempo to environment change rate

---

### Perspective 2: Cynefin Framework (Management)

**Core Insight:**
Different situations require fundamentally different approaches to adaptation. **Matching your adaptation strategy to the domain is more important than having a powerful adaptation strategy**. Applying the wrong approach creates failures that look like adaptation failures but are actually categorization failures.

**Mechanisms and How It Works:**

1. **The Five Domains:**

   | Domain | Cause-Effect | Appropriate Approach | Adaptation Mode |
   |--------|--------------|---------------------|-----------------|
   | **Clear** | Obvious, repeatable | Sense-Categorize-Respond | Follow best practice, minimal adaptation |
   | **Complicated** | Discoverable by analysis | Sense-Analyze-Respond | Expert analysis, then adapt plan |
   | **Complex** | Retrospectively coherent only | Probe-Sense-Respond | Experiment, then adapt based on results |
   | **Chaotic** | No perceivable pattern | Act-Sense-Respond | Stabilize first, analyze later |
   | **Confused** | Domain unknown | Gather information | Categorize before adapting |

2. **Domain Determines Adaptation Strategy:**

   | Domain | Adaptation Trigger | Adaptation Method |
   |--------|-------------------|-------------------|
   | Clear | Best practice violated | Return to best practice |
   | Complicated | Analysis reveals better approach | Replan based on analysis |
   | Complex | Probe reveals new pattern | Iterate based on learning |
   | Chaotic | Any action that stabilizes | Act to restore stability, analyze later |

   **Critical failure mode:** Using the wrong approach for the domain. Analyzing in Chaotic wastes time. Acting without analysis in Complicated wastes resources. Treating Complex as Complicated leads to premature convergence.

3. **Domain Transitions:**

   ```
   Chaotic → (stabilization) → Complex → (learning) → Complicated → (best practice) → Clear
                                                                            ↓
                                                               (complacent drift) → Chaotic
   ```

   | Transition | Signal | Action |
   |------------|--------|--------|
   | Clear → Chaotic | Best practice fails catastrophically | Switch to Act-Sense-Respond |
   | Chaotic → Complex | Stability restored | Begin probing |
   | Complex → Complicated | Patterns emerge | Begin analysis |
   | Complicated → Clear | Analysis codified | Document best practice |

   Adaptation must include domain re-assessment. A problem that was Complex may become Complicated after learning.

4. **Probing in Complex Domain:**
   The Complex domain requires probes---small experiments to reveal patterns. Probes should be:
   - Safe to fail (bounded consequences)
   - Informative (reveal useful patterns)
   - Multiple and parallel (don't bet on one hypothesis)
   - Followed by sense-making (not just data collection)

   Agents in Complex domains need explicit permission and infrastructure for probing:
   ```markdown
   ## Complex Domain Protocol
   1. Identify that domain is Complex (cause-effect not obvious)
   2. Design probe: small, safe experiment
   3. Execute probe
   4. Observe results without judgment
   5. Build/update mental model from results
   6. Repeat until pattern emerges or escalate
   ```

**When It Works, When It Fails:**
- Works when domain can be correctly identified
- Works when appropriate approach is available for domain
- Fails when domain is misidentified (treating Complex as Clear)
- Fails when agents lack capability for domain's required approach

**Scaling Characteristics:**
- Domain assessment can be local (each agent assesses own context)
- Complex coordination problems may require system-level assessment
- Different agents may be in different domains simultaneously
- Transitions must be communicated to maintain coordination

**Key Takeaways for Agents:**
- First identify what kind of problem you face
- Match adaptation approach to domain
- Accept that some domains require probing, not planning
- Watch for domain transitions that require approach changes

---

### Perspective 3: Friction and Fog of War (Military Doctrine)

**Core Insight:**
Clausewitz's friction and fog are not obstacles to overcome but structural properties of operational reality. **Adaptation is not about eliminating friction but about operating effectively despite it**. Systems designed assuming smooth execution fail; systems designed for friction succeed where perfect systems fail.

**Mechanisms and How It Works:**

1. **Sources of Friction:**

   | Source | Description | Agent Equivalent |
   |--------|-------------|------------------|
   | Physical limitations | Fatigue, resource limits | Context window limits, API rate limits |
   | Information uncertainty | Incomplete, contradictory information | Ambiguous inputs, stale data |
   | Environmental resistance | Weather, terrain | Network failures, dependency outages |
   | Coordination friction | Communication delays, misunderstanding | Inter-agent latency, protocol mismatch |

   Friction is ubiquitous. Every operation encounters resistance. Adaptation must assume friction exists.

2. **The Fog Problem:**
   Agents operate with incomplete and potentially incorrect information. The fog is not just absence of information but active distortion:
   - What you observe may be wrong
   - What you don't observe may be critical
   - Multiple sources contradict
   - Confidence does not correlate with correctness

   Adaptation under fog requires:
   - Acting despite uncertainty
   - Designing for reversibility
   - Maintaining orientation despite incomplete information
   - Expecting to be wrong and planning for correction

3. **Mission Command (Auftragstaktik) Response:**
   The Prussian-German response to friction: **mission command**. Centralized intent with decentralized execution.

   | Component | Description | Adaptation Implication |
   |-----------|-------------|------------------------|
   | Intent | What must be accomplished | Stable reference for adaptation |
   | Initiative | Subordinate discretion | Freedom to adapt methods |
   | Mutual trust | Confidence in others' judgment | Coordinated without central control |
   | Simplicity | Understandable plans | Can be executed despite friction |

   Adaptation should modify methods to achieve intent, not abandon intent. Agents need clear intent to adapt effectively.

4. **Friction-Tolerant Design:**

   | Principle | Implementation |
   |-----------|----------------|
   | Simplicity | Plans simple enough to survive confusion |
   | Redundancy | Multiple paths to objectives |
   | Reversibility | Actions can be undone if wrong |
   | Loose coupling | Components fail independently |
   | Margin | Buffer time, resources, capacity |

   Friction-tolerant systems don't assume smooth execution. They assume friction and design for recovery.

**When It Works, When It Fails:**
- Works when systems expect and design for friction
- Works when intent is clear and stable
- Fails when plans assume perfect execution
- Fails when friction exceeds designed margins

**Scaling Characteristics:**
- Friction scales super-linearly with system complexity
- Tight coupling amplifies friction effects
- Coordination friction increases with agent count
- Margin requirements increase at scale

**Key Takeaways for Agents:**
- Expect friction---don't design assuming smooth execution
- Accept fog---operate despite incomplete information
- Preserve intent while adapting methods
- Design with margins for recovery

---

### Perspective 4: Recognition-Primed Decision Making (Management/Psychology)

**Core Insight:**
Experts adapt rapidly not by analyzing options but by **recognizing situations and retrieving appropriate responses**. Pattern recognition beats analysis for familiar situations. But patterns fail in genuinely novel situations, requiring a different adaptation mode.

**Mechanisms and How It Works:**

1. **The RPD Model:**

   ```
   Situation → Pattern Recognition → Typical Response → Mental Simulation → Act
                     |                                        |
                 (Known?)                              (Will it work?)
                     |                                        |
                   Yes → Fast                           Yes → Act
                   No → Deliberate analysis             No → Modify or reconsider
   ```

   Experts don't generate multiple options and compare. They recognize the situation type, retrieve a typical response, simulate whether it will work, and act. Adaptation for familiar situations is pattern-based.

2. **Variation 1: Simple Match (No Adaptation)**
   ```
   Situation recognized → Response known → Act immediately
   ```
   No adaptation needed. The pattern matches, the response is appropriate. This is IG&C from OODA---fast but not adaptive.

3. **Variation 2: Situation Diagnosis (Adaptive Recognition)**
   ```
   Ambiguous cues → Build story to make sense → Recognize pattern → Act
   ```
   Adaptation occurs in the story-building phase. Agent gathers more cues, constructs coherent interpretation, then recognizes the pattern. This is adaptive pattern-matching.

4. **Variation 3: Response Evaluation (Adaptive Response)**
   ```
   Pattern recognized → Typical response → Simulate → Doesn't work → Modify response
   ```
   The pattern matches, but the typical response needs adaptation. Mental simulation reveals problems; response is modified to fit the specific situation. This is adaptation within pattern.

5. **When Patterns Fail:**

   | Signal | Meaning | Required Action |
   |--------|---------|-----------------|
   | No pattern matches | Genuinely novel situation | Switch to deliberate analysis |
   | Pattern matches but simulation fails | Pattern applies but context differs | Adapt response |
   | Multiple patterns match | Ambiguous situation | Gather more cues, diagnose |
   | Pattern matched but outcome failed | Pattern was wrong | Destroy pattern, learn |

   RPD requires knowing when patterns don't apply. Agents need explicit "pattern failure" detection.

6. **Expectancy Generation and Violation:**
   Experts generate expectations from recognized patterns. Violation of expectations signals adaptation need:

   | Expectancy | Reality | Implication |
   |------------|---------|-------------|
   | Matches | Matches | Continue, pattern valid |
   | High confidence | Violated | Strong signal for adaptation |
   | Low confidence | Violated | Gather more information |
   | Not generated | N/A | Novel situation, deliberate |

   Agents should explicitly generate predictions and compare to outcomes. Expectancy violation is an adaptation trigger.

**When It Works, When It Fails:**
- Works when situations are within experience base
- Works when patterns are well-calibrated to current domain
- Fails when situations are genuinely novel
- Fails when patterns are outdated or miscalibrated

**Scaling Characteristics:**
- Pattern libraries are local to each agent
- Shared patterns (via CLAUDE.md) enable coordinated rapid response
- Pattern accumulation across agents requires explicit mechanisms
- Pattern conflicts between agents create coordination problems

**Key Takeaways for Agents:**
- Pattern recognition enables rapid adaptation within known territory
- Generate expectations explicitly and watch for violations
- Recognize when patterns don't apply (novel situations)
- Switch to deliberate analysis when patterns fail

---

### Perspective 5: Mental Model Building (Pedagogy)

**Core Insight:**
Adaptation capability depends on mental model quality. **Agents don't adapt by changing behavior---they adapt by updating mental models, from which new behavior follows**. Systems that focus on behavioral correction without addressing underlying models create fragile, shallow adaptation.

**Mechanisms and How It Works:**

1. **Three Levels of Conceptual Error:**

   | Level | Error Type | Correction Difficulty |
   |-------|------------|----------------------|
   | Level 1 | False beliefs (wrong facts) | Easy: provide correct information |
   | Level 2 | Flawed models (wrong structure) | Medium: restructure relationships |
   | Level 3 | Category mistakes (wrong ontology) | Hard: recategorize before correcting |

   Adaptation difficulty depends on error level. Level 1 errors are simple corrections. Level 3 errors require recognizing the entire conceptual framework is wrong.

2. **Why More Data Doesn't Fix Model Problems:**
   New information is interpreted through existing models. If the model is wrong, new data is assimilated incorrectly:

   ```
   Wrong model → Interprets new data → Confirms wrong model
                                           ↓
                                    Incestuous amplification
   ```

   Adaptation requires:
   - Dissatisfaction with existing model (something doesn't fit)
   - Intelligibility of new model (can understand alternative)
   - Plausibility of new model (seems reasonable)
   - Fruitfulness of new model (solves problems old model couldn't)

   Simply providing correct information doesn't create these conditions.

3. **Elicit-Confront-Resolve Cycle:**
   Effective adaptation requires surfacing the current model, confronting it with disconfirming evidence, and resolving to a new model:

   ```
   1. Elicit: What does the agent think is happening?
   2. Confront: Present evidence that doesn't fit
   3. Resolve: Support construction of new model
   ```

   This mirrors Boyd's destruction-creation cycle. The agent must destroy the old model before building the new one.

4. **Adaptive Pathways:**
   Complex model changes require progressive scaffolding:

   ```
   Current model → Bridging model → Intermediate model → Target model
   ```

   Agents cannot jump directly from fundamentally wrong models to correct ones. Intermediate models provide stepping stones.

5. **Model Consistency for Coordination:**
   Multi-agent adaptation requires model consistency:

   | Situation | Problem | Solution |
   |-----------|---------|----------|
   | Agents have same model | One agent adapts, others don't | Propagate model update |
   | Agents have different models | Coordination assumes wrong model | Synchronize before adapting |
   | Model update breaks contracts | Dependent agents fail | Version models, migrate |

**When It Works, When It Fails:**
- Works when agents can introspect on their models
- Works when confrontation with evidence is possible
- Fails when agents can't articulate their models
- Fails when evidence is interpreted through wrong model

**Scaling Characteristics:**
- Model adaptation is individual
- Model synchronization creates coordination overhead
- Shared documentation (CLAUDE.md) is model specification
- Model drift across agents creates inconsistency

**Key Takeaways for Agents:**
- Adaptation is model change, not behavior change
- Surface current models to enable confrontation
- More data doesn't fix wrong models---destruction does
- Multi-agent adaptation requires model synchronization

---

### Perspective 6: Feedback Loops (Control Theory)

**Core Insight:**
Continuous adaptation requires feedback loops. But **feedback is not inherently stabilizing**---the dynamics of feedback determine whether adaptation converges or oscillates. Poorly tuned feedback creates adaptation pathologies worse than no adaptation.

**Mechanisms and How It Works:**

1. **Feedback Loop Dynamics:**

   | Parameter | Effect | Adaptation Implication |
   |-----------|--------|------------------------|
   | Gain (K) | Correction intensity | High gain → fast but may overshoot |
   | Delay | Time between error and correction | Delay causes phase shift, instability |
   | Bandwidth | How fast changes can be tracked | Low bandwidth → can't track fast changes |
   | Phase margin | Distance from instability | Low margin → oscillation risk |

   Adaptation is a feedback system. Error detection triggers correction, which changes output, which is observed...

2. **Gain Tuning for Adaptation:**

   | Gain Level | Adaptation Behavior |
   |------------|---------------------|
   | Too low | Slow adaptation, persistent error |
   | Optimal | Fast adaptation, minimal overshoot |
   | Too high | Overcorrection, oscillation |
   | Much too high | Instability, thrashing |

   The challenge: calibrating gain for the specific context. Different situations require different adaptation intensity.

3. **Delay Causes Instability:**
   When correction is based on stale observation, the correction may be wrong for the current state:

   ```
   Time 0: Observe error E
   Time 1: Decide correction C for error E
   Time 2: Apply correction C
   Time 3: Error has already changed to E', C is wrong
   Time 4: New correction based on observation of wrong correction
   ...oscillation...
   ```

   Adaptation delay must be less than environment change rate. Otherwise, agents are always correcting for past conditions.

4. **Multiple Feedback Loops (Cascade Control):**

   | Loop | Timescale | Purpose |
   |------|-----------|---------|
   | Inner (fast) | Within task | Adjust execution approach |
   | Outer (slow) | Across tasks | Adjust overall patterns |
   | Meta (slowest) | Across sessions | Adjust documentation, conventions |

   Different adaptation timescales must be separated. Inner loops must settle before outer loops adjust. Otherwise, loops interfere with each other.

5. **Feedforward vs. Feedback:**

   | Type | Mechanism | When to Use |
   |------|-----------|-------------|
   | Feedback | Correct after error | Unknown disturbances |
   | Feedforward | Prevent before error | Known disturbances |

   CLAUDE.md is feedforward control---anticipating errors before they occur. Feedback handles what feedforward misses.

   Optimal adaptation uses both:
   - Feedforward (documentation) prevents known problems
   - Feedback corrects residual and novel problems

6. **Stability Margins:**
   A system needs margins to remain stable despite parameter variation:

   | Margin | What It Provides |
   |--------|------------------|
   | Gain margin | Tolerance for correction intensity changes |
   | Phase margin | Tolerance for delay increases |
   | Robustness | Tolerance for model uncertainty |

   Adaptation that consumes all margins becomes fragile. Conservative adaptation preserves margin for future uncertainty.

**When It Works, When It Fails:**
- Works when feedback dynamics are understood and tuned
- Works when delay is less than change rate
- Fails when gain is miscalibrated (too high or too low)
- Fails when loops interfere with each other

**Scaling Characteristics:**
- Each agent has its own feedback loops
- System-wide feedback requires aggregation
- More agents = more potential interference
- Coordination adds to feedback delay

**Key Takeaways for Agents:**
- Adaptation is a feedback control problem
- Tune gain for context (not maximum)
- Minimize delay between observation and correction
- Separate adaptation timescales to prevent interference

---

## Cross-Cutting Patterns

### What All Perspectives Agree On

1. **Adaptation requires recognizing that current approach is wrong.**
   Every perspective emphasizes detecting the need for adaptation:
   - OODA: Disconfirming evidence triggers re-orientation
   - Cynefin: Domain transitions require approach changes
   - RPD: Expectancy violations signal pattern failure
   - Mental Models: Confrontation with evidence creates dissatisfaction
   - Feedback Loops: Error signal drives correction

2. **More information doesn't fix wrong models.**
   Multiple perspectives warn against the "more data" fallacy:
   - OODA: Incestuous amplification---seeing what you expect
   - Mental Models: New information interpreted through wrong model
   - RPD: Patterns filter what gets noticed

   Effective adaptation requires model destruction, not just information accumulation.

3. **Adaptation has costs---over-adaptation is as bad as under-adaptation.**
   All perspectives acknowledge adaptation costs:
   - OODA: Cycle time trades off with observation quality
   - Cynefin: Wrong approach for domain wastes effort
   - Feedback Loops: High gain causes oscillation

   The goal is appropriate adaptation, not maximum adaptation.

4. **Context determines appropriate adaptation strategy.**
   No single adaptation approach works for all situations:
   - Cynefin: Domain determines approach
   - RPD: Familiar vs. novel requires different modes
   - Feedback Loops: Gain must be tuned for context

   Adaptive systems must adapt their adaptation strategy.

5. **Coordination constrains individual adaptation.**
   Multi-agent adaptation has constraints single agents don't face:
   - OODA: Shared orientation (Einheit) enables coordinated adaptation
   - Mental Models: Model synchronization required for coordination
   - Feedback Loops: Multiple loops can interfere

   Individual adaptation that breaks coordination is counterproductive.

### Where Perspectives Diverge

1. **Emphasis on Speed vs. Accuracy:**
   - OODA: Tempo is crucial; faster cycles are better
   - Cynefin: Match approach to domain; rushing in Complex is wrong
   - Feedback: Bandwidth limits how fast adaptation can be

   **Why they diverge:** Context determines whether speed or accuracy matters more. Combat emphasizes speed; complex problem-solving emphasizes accuracy.

2. **Role of Pattern Recognition:**
   - RPD: Pattern recognition is how experts adapt quickly
   - Mental Models: Patterns can be wrong; model reconstruction needed
   - Cynefin: Patterns only apply in Clear/Complicated domains

   **Why they diverge:** Pattern recognition is powerful within training distribution, dangerous outside it. The question is whether the situation is within known patterns.

3. **Centralized vs. Distributed Adaptation:**
   - Friction/Fog: Mission command enables decentralized adaptation
   - Feedback: Cascade control suggests hierarchical adaptation
   - OODA: Individual OODA loops with shared orientation

   **Why they diverge:** The right approach depends on coordination requirements, communication capability, and expertise distribution.

### Synthesis: The Adaptation Capability Stack

```
Layer 4: Meta-Learning
  ├── Update documentation based on outcomes
  ├── Evolve conventions from experience
  └── Improve adaptation capabilities themselves
           ↑
Layer 3: Strategic Adaptation (Outer Loop)
  ├── Recognize domain transitions
  ├── Modify overall approach
  └── Update mental models
           ↑
Layer 2: Tactical Adaptation (Inner Loop)
  ├── Detect execution deviations
  ├── Adjust plan within constraints
  └── Modify methods, preserve intent
           ↑
Layer 1: Reactive Adaptation (Immediate)
  ├── Handle errors and exceptions
  ├── Retry with backoff
  └── Graceful degradation
           ↑
Layer 0: Stable Foundation
  ├── Clear intent (what to achieve)
  ├── Shared conventions (how to coordinate)
  └── Feedback infrastructure (how to observe)
```

Each layer builds on the one below. Without stable foundation, reactive adaptation has nothing to fall back to. Without reactive adaptation, tactical adjustments don't survive friction. Without tactical adaptation, strategic changes can't be implemented. Without strategic adaptation, meta-learning has no effect.

---

## Scaling Analysis

### Small Scale (3-10 Agents)

**What Works:**
- Direct model synchronization between agents
- Single point of adaptation authority
- Shared context fits in working memory
- High-bandwidth inter-agent communication

**Adaptation Patterns:**
- Immediate propagation of model updates
- Consensus-based adaptation decisions
- Full visibility of all agent states
- Direct correction of individual agents

**Metrics:**
- Model consistency > 95%
- Adaptation latency < 30 seconds
- Recovery from friction < 5 minutes

### Medium Scale (10-50 Agents)

**What Changes:**
- Direct synchronization becomes O(n^2) expensive
- Single authority becomes bottleneck
- Shared context exceeds working memory
- Need hierarchical adaptation structure

**Adaptation Patterns:**
- Domain-grouped adaptation (agents adapt within domains)
- Delegated adaptation authority (domain leads)
- Summary-level model propagation
- Inner/outer loop separation

**Transition Triggers:**
- Model synchronization latency > 1 minute
- Adaptation authority utilization > 70%
- Coordination failures during adaptation > 5%

**Metrics:**
- Within-domain consistency > 95%
- Cross-domain consistency > 90%
- Adaptation latency < 2 minutes

### Large Scale (50-1000+ Agents)

**What Changes:**
- Cannot track individual agent models
- Statistical adaptation patterns required
- Hierarchical authority essential
- Convention-based coordination dominates

**Adaptation Patterns:**
- Federated adaptation (domain-level autonomy)
- Evolutionary convention changes (gradual propagation)
- Outcome-based adaptation triggers
- Damped, slow outer loops

**Transition Triggers:**
- Human cannot track all adaptation activity
- Adaptation interference causes oscillation
- Convention drift exceeds tolerance

**Metrics:**
- Outcome metrics (task success) > direct model tracking
- Adaptation stability (no oscillation) > adaptation speed
- Convention compliance > 95%

### What Changes and Why at Each Transition

| Transition | Problem | Solution |
|------------|---------|----------|
| 3-10 to 10-50 | Synchronization expensive | Domain grouping, delegation |
| 10-50 to 50+ | Authority bottleneck | Federated structure |
| 50+ to 1000+ | Direct coordination impossible | Convention-based, statistical |

---

## Decision Framework

### When to Trigger Adaptation

| Signal | Confidence | Action |
|--------|------------|--------|
| Explicit failure (error, exception) | High | Immediate tactical adaptation |
| Expectancy violation (outcome != prediction) | Medium-High | Investigate, likely adapt |
| Performance degradation (slower, harder) | Medium | Gather more evidence, probably adapt |
| Pattern mismatch (doesn't fit known types) | Medium | Diagnose domain, select approach |
| Weak signal (something seems off) | Low | Monitor closely, don't adapt yet |

### Replanning vs. Execution Adjustment

| Indicator | Replan | Adjust Execution |
|-----------|--------|------------------|
| Intent still valid | No | Yes |
| Methods working | No | Yes |
| Fundamental assumptions violated | Yes | No |
| New constraints discovered | Yes | No |
| Expected friction | No | Yes |
| Domain has changed | Yes | No |
| Problem remains same type | No | Yes |

**Decision Tree:**
```
Is the intent still achievable?
├── No → Escalate (problem beyond current scope)
└── Yes → Are methods working?
    ├── Yes → Minor friction, adjust and continue
    └── No → Have fundamental assumptions changed?
        ├── Yes → Replan from new understanding
        └── No → Tactical adjustment to methods
```

### Context Factors That Drive Adaptation Approach

| Factor | Low Value | High Value |
|--------|-----------|------------|
| Uncertainty | Analyze then act | Probe to learn |
| Time pressure | Careful adaptation | Fast, accept imperfection |
| Stakes | Aggressive adaptation | Conservative, preserve margin |
| Reversibility | Commit and adapt | Experiment safely |
| Coordination requirements | Individual adaptation | Synchronized adaptation |

---

## Implementation Checklist

### Phase 1: Establish Adaptation Foundation

- [ ] Define clear intent for all tasks
- [ ] Document expected patterns (CLAUDE.md)
- [ ] Implement state observation (what agents can see)
- [ ] Create error detection infrastructure
- [ ] Define domain categorization (Clear/Complicated/Complex)

### Phase 2: Implement Reactive Adaptation

- [ ] Error handling with retry and backoff
- [ ] Graceful degradation paths
- [ ] Timeout-based recovery
- [ ] Circuit breakers for cascade prevention
- [ ] Logging for adaptation events

### Phase 3: Implement Tactical Adaptation

- [ ] Expectancy generation and checking
- [ ] Deviation detection mechanisms
- [ ] Plan adjustment within constraints
- [ ] Method modification while preserving intent
- [ ] Coordination during tactical changes

### Phase 4: Implement Strategic Adaptation

- [ ] Domain transition detection
- [ ] Mental model surfacing
- [ ] Disconfirming evidence search
- [ ] Model destruction-creation cycle
- [ ] Synchronized model updates across agents

### Phase 5: Implement Meta-Learning

- [ ] Outcome tracking for adaptation decisions
- [ ] Pattern extraction from successful adaptations
- [ ] Convention evolution process
- [ ] Documentation update triggers
- [ ] Adaptation capability improvement

### Success Criteria

- Recovery from unexpected friction: < 5 minutes
- Adaptation oscillation incidents: 0
- Model consistency across agents: > 95%
- Task completion despite obstacles: > 90%
- Adaptation overhead: < 15% of task time

---

## Failure Mode Taxonomy

### Detection Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| Missed signals | Continue wrong approach | Observation gap | Improve observation coverage |
| Signal ignored | Evidence present but not acted on | Incestuous amplification | Seek disconfirming evidence |
| False positive | Adapt when not needed | Noise in observations | Filter, threshold tuning |
| Late detection | Adapt after damage done | Observation delay | Reduce detection latency |

### Diagnosis Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| Wrong domain | Analyze in Chaotic, act in Complex | Domain misidentification | Explicit domain assessment |
| Wrong level | Fix symptoms not cause | Shallow diagnosis | Check model-level errors |
| Wrong scope | Local fix for system problem | Scope misjudgment | Broader observation |

### Response Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| Overcorrection | Oscillation, thrashing | Gain too high | Reduce correction intensity |
| Undercorrection | Persistent error | Gain too low | Increase correction intensity |
| Wrong timescale | Fast loop fights slow loop | Loop interference | Separate timescales |
| Uncoordinated | Individual adapts, system breaks | Missing synchronization | Coordinate model updates |

### Learning Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| No update | Same errors repeat | No meta-learning | Implement outcome tracking |
| Wrong lesson | Adapts to noise | Overfitting to incidents | Aggregate before learning |
| Obsolete patterns | Old solutions to new problems | Stale conventions | Regular convention review |

### Diagnostic Decision Tree

```
SYMPTOM: Adaptation-related problem

CHECK: Was adaptation needed?
├── No (false positive) → Improve signal filtering, raise thresholds
└── Yes → Was adaptation detected?
    ├── No (missed signal) → Improve observation, add detection
    └── Yes → Was diagnosis correct?
        ├── No → Review domain assessment, check model level
        └── Yes → Was response appropriate?
            ├── No → Tune gain, check timescale, verify coordination
            └── Yes → Was learning captured?
                ├── No → Implement meta-learning
                └── Yes → Unexpected; investigate deeper
```

---

## Anti-Patterns

### Anti-Pattern 1: The Perfect Plan Fallacy

**What it looks like:**
- Extensive upfront planning assuming smooth execution
- No adaptation infrastructure because "the plan handles everything"
- Surprise and confusion when plans don't survive contact

**Why it's tempting:**
- Planning feels productive
- Uncertainty is uncomfortable
- Adaptation seems like failure

**Why it fails:**
- Friction is structural, not optional
- Plans always diverge from reality
- No plan survives contact with environment

**What to do instead:**
- Plan for adaptation, not just execution
- Build margin for friction
- Expect plans to change; design for change

### Anti-Pattern 2: Adapt to Everything

**What it looks like:**
- Constant replanning on every signal
- No stable reference point
- Agents in perpetual adjustment mode

**Why it's tempting:**
- Responsiveness feels virtuous
- Ignoring signals feels risky
- Adaptation is what we're supposed to do

**Why it fails:**
- Oscillation and thrashing
- Never complete anything
- Coordination impossible when everything changes
- Noise drives system

**What to do instead:**
- Filter signals; separate noise from pattern
- Threshold before adapting
- Preserve stable elements while adapting others
- Accept that some friction is normal

### Anti-Pattern 3: Individual Adaptation Without Coordination

**What it looks like:**
- Each agent adapts independently
- No model synchronization
- Adaptation breaks coordination contracts

**Why it's tempting:**
- Local adaptation is simple
- Coordination overhead is expensive
- "I know what I need to do"

**Why it fails:**
- Agents develop inconsistent models
- Coordination based on outdated assumptions
- Individual optimization harms system

**What to do instead:**
- Synchronize model updates
- Version coordination contracts
- Announce adaptation before acting
- Maintain Einheit (shared orientation)

### Anti-Pattern 4: Pattern Matching in Novel Situations

**What it looks like:**
- Apply familiar patterns regardless of fit
- "This is like that other time..."
- Force-fit solutions that don't match

**Why it's tempting:**
- Pattern matching is fast and comfortable
- Novel situations are uncertain
- Past success breeds confidence

**Why it fails:**
- Novel situations genuinely require novel approaches
- Force-fitting creates worse problems
- Confidence doesn't equal correctness

**What to do instead:**
- Explicitly check if patterns apply
- Recognize genuinely novel situations
- Switch to deliberate analysis when patterns don't fit
- Probe in Complex domains

### Anti-Pattern 5: Ignoring Adaptation Feedback

**What it looks like:**
- Adapt but don't verify adaptation worked
- No outcome tracking for adaptations
- Same adaptation problems repeat

**Why it's tempting:**
- Adapting feels like problem solved
- Verification takes effort
- Moving on to next task

**Why it fails:**
- Adaptation may be wrong
- No learning from adaptation outcomes
- Meta-improvement impossible

**What to do instead:**
- Verify adaptation effectiveness
- Track adaptation outcomes
- Learn from both successful and failed adaptations
- Update conventions based on patterns

---

## Key Insights

### Insight 1: Adaptation Is Model Change, Not Behavior Change

Behavioral adaptation without mental model updates is shallow and fragile. Effective adaptation updates the underlying model, from which new behavior follows naturally. Focus on model quality, not just action modification.

**The test:** Can the agent explain why it's adapting, not just that it's adapting?

### Insight 2: Adaptation Triggers Require Disconfirming Evidence

Confirmation bias filters observations through existing models. Agents that only seek confirming evidence never see reasons to adapt. Active search for disconfirming evidence is essential for detecting adaptation needs.

**The test:** Does the agent look for evidence it might be wrong?

### Insight 3: Domain Determines Adaptation Approach

There is no universal adaptation strategy. Clear domains need best-practice return. Complicated domains need analysis. Complex domains need probing. Chaotic domains need immediate action. Matching approach to domain matters more than having a powerful approach.

**The test:** Does the agent assess what kind of problem it faces before choosing how to adapt?

### Insight 4: Feedback Dynamics Determine Adaptation Quality

Adaptation is a feedback control problem. High gain causes oscillation. Delay causes instability. Interference between loops causes chaos. Tuning adaptation parameters for the specific context is essential.

**The test:** Is adaptation gain calibrated, or does every correction have the same intensity?

### Insight 5: Coordination Constrains Adaptation

Individual adaptation that breaks coordination is counterproductive. Multi-agent systems need synchronized adaptation---model updates propagated, contracts maintained, orientation shared. Einheit (shared mental models) enables coordinated adaptation.

**The test:** Does adaptation preserve or break coordination with other agents?

### Insight 6: Meta-Learning Improves Adaptation Capability

The ability to adapt is itself subject to improvement. Tracking adaptation outcomes, extracting patterns from successful adaptations, and evolving conventions based on experience creates compounding adaptation capability.

**The test:** Does the system get better at adapting over time?

### Insight 7: Friction Is Structural, Not Optional

Plans that assume smooth execution fail. Adaptation is not failure---it's the normal response to friction that is built into operational reality. Design for friction; expect adaptation; build margins.

**The test:** Does the plan have margin for adaptation, or does it assume perfect execution?

### Insight 8: Pattern Recognition Is Fast But Limited

Pattern matching enables rapid adaptation within the training distribution. But it fails for genuinely novel situations. The critical skill is recognizing when patterns don't apply and switching to deliberate analysis.

**The test:** Can the agent recognize genuinely novel situations?

### Insight 9: Timescales Must Be Separated

Fast adaptation (within task) and slow adaptation (across tasks) and very slow adaptation (meta-learning) must operate at different timescales. Mixing timescales causes interference and instability.

**The test:** Are different adaptation loops operating at appropriate, separated timescales?

### Insight 10: Feedforward Reduces Feedback Burden

Documentation (CLAUDE.md) is feedforward control---preventing known errors before they occur. Good feedforward reduces the adaptation burden on feedback. Investment in documentation pays off in reduced adaptation overhead.

**The test:** How much adaptation is required because of undocumented situations vs. genuinely novel situations?

---

## Related Problems

### Adaptability Connects To:

**Error Detection and Recovery:**
- Errors are adaptation triggers
- Recovery is a form of adaptation
- Error cascades require adaptation to contain

**Coordination Without Communication:**
- Shared conventions (Einheit) enable coordinated adaptation
- Implicit coordination reduces adaptation coordination overhead
- Convention changes require explicit coordination

**Information Flow:**
- Observation infrastructure enables adaptation detection
- Information delays affect adaptation dynamics
- Model synchronization is information flow

**Scaling Coordination:**
- Adaptation patterns change with scale
- Hierarchical adaptation at large scale
- Convention-based adaptation scales better

**Trust and Oversight:**
- Autonomous adaptation requires trust
- Human oversight for strategic adaptation
- Adaptation decisions need accountability

### Problem Dependency Order

1. **Information Flow first:** Can't adapt to what you can't observe
2. **Error Detection:** Know when something is wrong
3. **Coordination patterns:** Stable foundation for adaptation
4. **Tactical adaptation:** Handle friction
5. **Strategic adaptation:** Handle model changes
6. **Meta-learning:** Improve adaptation over time

Adaptability depends on information flow and benefits from good coordination patterns. It enables robust operation despite uncertainty and supports continuous improvement.

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Cross-disciplinary synthesis for multi-agent coordination research
**Status:** Complete

---

## Source Documents

### Primary Sources (6 Perspectives)

1. **OODA Loop** (Military/Management)
   - `/docs/management/ooda-loop-agent-analysis.md`
   - Focus: Observe-orient-decide-act cycle, tempo, destruction-creation, IG&C

2. **Cynefin Framework** (Management)
   - `/docs/management/cynefin.md`
   - Focus: Domain matching, Clear/Complicated/Complex/Chaotic, probing

3. **Friction and Fog of War** (Military Doctrine)
   - `/docs/military-doctrine/friction-fog-of-war.md`
   - Focus: Structural resistance, mission command, friction-tolerant design

4. **Recognition-Primed Decision Making** (Management/Psychology)
   - `/docs/management/recognition-primed-decision.md`
   - Focus: Pattern recognition, expectancy violation, expert adaptation

5. **Mental Model Building** (Pedagogy)
   - `/docs/pedagogy/mental-model-building-agent-analysis.md`
   - Focus: Model change, elicit-confront-resolve, adaptive pathways

6. **Feedback Loops** (Control Theory)
   - `/docs/control-theory/feedback-loops.md`
   - Focus: Gain tuning, stability margins, cascade control, feedforward

### Supplementary Sources

- **Emergent Coordination** (Jazz Improvisation)
  - `/docs/jazz-improvisation/emergent-coordination-agent-analysis.md`
  - Focus: Self-repair mechanisms, error tolerance without stopping

### Cross-References

- Problem mapping: `/.claude/problem-research-mapping.md`
- Related synthesis: `/docs/syntheses/conflict-management-synthesis.md`
- Related synthesis: `/docs/syntheses/coordination-without-communication-synthesis.md`
- Related synthesis: `/docs/syntheses/scaling-coordination-synthesis.md`
