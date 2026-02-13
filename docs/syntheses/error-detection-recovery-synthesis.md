# Error Detection and Recovery: Cross-Disciplinary Synthesis

## Problem Statement

### Why This Matters

Error detection and recovery is the resilience backbone of multi-agent systems. Unlike single-agent failures that produce localized effects, errors in multi-agent systems cascade---one agent's subtle mistake becomes another agent's corrupted input, which becomes a third agent's confidently wrong output. By the time errors become visible at the system boundary, significant work has been built on a flawed foundation.

The challenge is threefold: **detecting errors early** (before they propagate), **recovering gracefully** (without losing good work), and **learning from failures** (preventing recurrence). Systems that treat all outputs as equally trustworthy or that collapse entirely on any error fail to achieve the reliability required for autonomous operation.

### When This Occurs in Multi-Agent Systems

Error detection and recovery becomes critical when:
- Agents produce outputs that subsequent agents consume as inputs (pipeline errors)
- Agents modify shared state that affects other agents' behavior (state corruption)
- Agent confidence does not reliably indicate accuracy (silent failures)
- Multiple agents contribute to emergent system behavior (attribution difficulty)
- Errors interact in unexpected ways across agent boundaries (cascade effects)
- The system must continue operating despite partial failures (graceful degradation)

### What Breaks If You Get It Wrong

**Undetected errors:**
- Subtle bugs propagate through the entire pipeline before surfacing
- Downstream agents treat corrupted outputs as valid inputs
- Human review sees polished final output built on flawed foundations
- Root cause becomes obscured as error transforms through multiple agents

**Poor recovery mechanisms:**
- Single agent failure halts entire system (fragile architecture)
- Retry storms amplify load during degraded conditions
- Incomplete recovery leaves system in inconsistent state
- Recovery actions create new errors (fix causes break)

**No learning from failures:**
- Same error patterns recur repeatedly
- Detection mechanisms never improve
- Latent conditions accumulate until catastrophic alignment
- Organizations lose trust in agent systems after preventable failures

### Scope and Boundaries

This synthesis addresses:
- How agents detect their own errors and limitations
- Mechanisms for detecting errors at agent boundaries
- Recovery strategies that preserve good work while correcting failures
- Cascade prevention through isolation and circuit breakers
- Graceful degradation when full functionality is unavailable
- Learning loops that improve detection over time

It does not deeply address:
- Conflict between agents (separate synthesis)
- Information flow architectures (separate synthesis)
- Task decomposition that affects error boundaries (separate synthesis)

---

## Perspectives

### Perspective 1: Normal Accident Theory (Safety Engineering)

**Core Insight:**
Normal Accident Theory argues that in systems with **interactive complexity** AND **tight coupling**, accidents are not failures of implementation but inevitable consequences of system structure. The combination of unexpected interactions (triggering novel failure modes) with fast propagation (preventing intervention) guarantees eventual catastrophic outcomes---regardless of how carefully the system is designed or operated.

**Mechanisms and How It Works:**

1. **The Two Dimensions That Determine Accident Potential:**

   | Dimension | Description | Agent System Indicators |
   |-----------|-------------|------------------------|
   | **Interactive Complexity** | Unfamiliar sequences, unexpected connections, feedback loops, multiple control parameters | Agents interpret natural language, outputs become context for other agents, emergent coordination behavior |
   | **Tight Coupling** | Time-dependent processes, invariant sequences, single path to goal, little slack | Synchronous pipelines, shared context windows, sequential dependencies, user waiting |

   The danger zone is high on both dimensions. Most current multi-agent architectures sit there.

2. **Why Errors Cascade:**

   Interactive complexity **triggers** unexpected failure combinations:
   ```
   Agent A: Subtle logical error in generated code
       ↓
   Agent B (review): Looks reasonable, approves
       ↓
   Agent C (testing): Writes tests that pass (doesn't cover edge case)
       ↓
   Agent D (docs): Documents incorrect behavior as intended
       ↓
   Human receives: Professional package built on corrupted foundation
   ```

   Tight coupling **propagates** those failures before detection:
   - No pause point exists between agents
   - Each agent immediately consumes previous output
   - By the time error is visible, cascade is complete

3. **The Redundancy Paradox:**

   | Naive Assumption | Reality |
   |------------------|---------|
   | More reviewer agents = safer | Each reviewer adds complexity (new failure modes) |
   | Backup systems catch errors | Common-mode failures defeat redundancies simultaneously |
   | Safety layers prevent accidents | Safety systems can themselves become accident sources |

   Redundancy works only when you know the failure modes you're defending against. In complex systems, dangerous failures are precisely the ones you don't anticipate---they bypass all redundancies through pathways you never imagined.

4. **Design for Loose Coupling:**

   | Tight Coupling Pattern | Loose Coupling Alternative |
   |------------------------|---------------------------|
   | Agent B waits for Agent A | Agent B reads from queue when ready |
   | Shared context window | Independent contexts per agent |
   | Sequential pipeline | Parallel branches with later aggregation |
   | Single path through workflow | Multiple acceptable paths to completion |
   | Real-time processing | Batch with checkpoints |

**When It Works, When It Fails:**
- Works when system architecture is a conscious design choice, not accident
- Works when efficiency is traded for resilience deliberately
- Fails when pressure to optimize removes slack and buffers
- Fails when success normalizes risky operation (drift toward danger)

**Scaling Characteristics:**
- Small scale: Direct coordination manageable, complexity still present
- Medium scale: Complexity increases faster than capability
- Large scale: Some architectures are simply unsafe at scale---redesign required

**Key Takeaways for Agents:**
- Complexity and coupling determine accident potential, not component quality
- Adding agents is not always adding capability---may be adding failure modes
- Design for loose coupling even at efficiency cost
- Accept that some architectures cannot be made safe---don't build them

---

### Perspective 2: Swiss Cheese Model (Safety Engineering)

**Core Insight:**
The Swiss Cheese Model reconceptualizes accidents as organizational phenomena rather than individual failures. Defenses are like slices of Swiss cheese---each has holes. Accidents occur when holes in multiple defense layers momentarily align, creating a trajectory from hazard to harm. The crucial insight: **holes are not static**. They continuously open, close, and shift position based on active failures (immediate errors) and latent conditions (systemic weaknesses waiting to combine).

**Mechanisms and How It Works:**

1. **Active Failures vs. Latent Conditions:**

   | Type | Timing | Visibility | Duration | Location |
   |------|--------|------------|----------|----------|
   | **Active Failures** | Immediate effect | Usually apparent | Short-lived | Sharp end (execution) |
   | **Latent Conditions** | Long incubation | Often hidden | Long-lasting | Blunt end (organization) |

   For agent systems:
   - **Active failures:** Hallucinations, misinterpretations, execution errors
   - **Latent conditions:** Poor CLAUDE.md, stale context, miscalibrated trust, inadequate testing

   **The resident pathogen metaphor:** Latent conditions are like dormant pathogens waiting to combine with active failures. Punishing active failures without addressing latent conditions guarantees recurrence.

2. **The Organizational Layers:**

   ```
   SYSTEM DESIGN (Blunt End)
   - Model selection, architecture choices, scope definition
              ↓ Creates conditions for
   CONFIGURATION (Supervision Level)
   - Prompt engineering, permission scoping, context management
              ↓ Creates conditions for
   OPERATIONAL CONDITIONS (Preconditions)
   - Context window state, task complexity, external pressures
              ↓ Creates conditions for
   EXECUTION (Sharp End)
   - Interpretation, planning, action, self-assessment
              ↓
   [OUTCOME: Success or Failure]
   ```

   By the time you reach execution (the "sharp end"), outcomes are largely determined by upstream factors. Fixing only execution errors ignores the causal chain from the "blunt end."

3. **Why Holes Are Dynamic:**

   | Dynamic Factor | How Holes Shift in Agent Systems |
   |----------------|----------------------------------|
   | Context drift | Earlier context fades; new context may conflict |
   | Prompt rot | CLAUDE.md outdated as codebase evolves |
   | Capability changes | Model updates change behavior unexpectedly |
   | User adaptation | Workarounds create implicit dependencies |
   | Normalization of deviance | Small failures without consequence expand acceptable risk |
   | Load variations | High task volume degrades verification thoroughness |

4. **Hard vs. Soft Defenses:**

   | Defense Type | Examples | Reliability |
   |--------------|----------|-------------|
   | **Hard (Engineered)** | Sandboxing, permission systems, token limits, type checking | High - technical enforcement |
   | **Soft (Procedural)** | Human review, CLAUDE.md guidance, prompt instructions, trust calibration | Variable - depends on attention, quality |

   **Critical insight:** Agent systems currently rely heavily on soft defenses. These are the most vulnerable layers. Investment in hard defenses (technical enforcement) provides more reliable protection.

5. **Error Types Requiring Different Interventions:**

   | Error Type | Mechanism | Agent Example | Fix |
   |------------|-----------|---------------|-----|
   | **Slips** | Execution differs from intention | Says "edit file X," edits file Y | Better interfaces, forcing functions |
   | **Lapses** | Memory failure mid-process | Forgets earlier context, repeats work | Checkpointing, context management |
   | **Rule-based mistakes** | Wrong rule applied | Uses pattern that doesn't fit | Better training, decision support |
   | **Knowledge-based mistakes** | Reasoning failure in novel situations | Hallucination, wrong diagnosis | Explicit uncertainty, escalation |
   | **Violations** | Intentional rule-breaking | Ignores CLAUDE.md for perceived benefit | Understanding why rules are broken |

**When It Works, When It Fails:**
- Works when organizational layers are explicitly identified and managed
- Works when investment prioritizes hard defenses over soft
- Fails when sharp-end blame culture prevents systemic learning
- Fails when latent conditions accumulate without detection

**Scaling Characteristics:**
- Any scale: The model applies universally
- Larger systems have more layers, more holes, more alignment possibilities
- Scaling requires systematic latent condition tracking

**Key Takeaways for Agents:**
- Agent execution errors are symptoms; latent conditions are root causes
- Map organizational layers before deployment; identify latent conditions
- Invest in hard defenses first; soft defenses are unreliable
- Track dynamic factors that shift holes over time

---

### Perspective 3: STAMP/STPA (Safety Engineering)

**Core Insight:**
Systems-Theoretic Accident Model and Processes (STAMP) reconceptualizes safety as a control problem. Accidents result from **inadequate control**, not component failures. Safety is an emergent property of the system that arises from interactions among components---it cannot be achieved by making components reliable; it requires that the control structure enforces necessary safety constraints.

**Mechanisms and How It Works:**

1. **Safety as Control, Not Reliability:**

   | Traditional View | STAMP View |
   |------------------|------------|
   | Safety = absence of failures | Safety = enforcement of constraints |
   | Accidents = chains of failures | Accidents = inadequate control |
   | Fix = prevent component failures | Fix = improve control structure |
   | Safety is a component property | Safety is an emergent property |

2. **The Control Loop:**

   ```
   ┌─────────────────────────────────────────────────┐
   │              CONTROLLER (Human/Agent)            │
   │   Process Model: Beliefs about controlled process│
   │   Control Algorithm: How to select actions       │
   └──────────────────────┬──────────────────────────┘
                          │ Control Actions
                          ▼
   ┌─────────────────────────────────────────────────┐
   │              CONTROLLED PROCESS                  │
   │     (Codebase, system, environment)             │
   └──────────────────────┬──────────────────────────┘
                          │ Feedback (via sensors)
                          ▼
                   Back to Controller
   ```

   **Key components:**
   - **Process Model:** The controller's understanding of the process
   - **Control Algorithm:** Rules for selecting actions
   - **Feedback:** Information about process state

3. **The Four Types of Unsafe Control Actions (UCAs):**

   | Type | Description | Agent Supervision Example |
   |------|-------------|---------------------------|
   | **1. Not providing when should** | Required action not given | Human doesn't intervene when agent is failing |
   | **2. Providing when shouldn't** | Action given inappropriately | Human interrupts agent during critical operation |
   | **3. Too early/late/wrong order** | Timing or sequence wrong | Approval given before verification complete |
   | **4. Stopped too soon/applied too long** | Duration wrong | Monitoring stops before task complete |

   These four categories are **provably complete**---any unsafe control action must fall into one of these types.

4. **Why Process Models Cause Accidents:**

   Most accidents in complex systems trace to **inadequate process models**:

   | Process Model Problem | Agent System Example |
   |----------------------|----------------------|
   | Outdated model | Agent thinks codebase state is X when it's Y |
   | Incomplete model | Agent doesn't know about hidden dependency |
   | Incorrect model | Agent assumes linear response when it's non-linear |
   | Model not updated | Agent uses stale context, misses recent changes |
   | Feedback misinterpreted | Agent misunderstands error message |

   **Leveson's insight:** "Component interaction accidents can usually be explained in terms of incorrect process models."

5. **Feedback Failures in Agent Systems:**

   | Feedback Type | Purpose | Failure Mode |
   |---------------|---------|--------------|
   | Build results | Did code compile? | Only catches syntax errors |
   | Test results | Does code work? | Tests may be incomplete |
   | Progress reports | Human tracks state | Agent may misrepresent |
   | Error reports | Human can intervene | Agent may not recognize errors |
   | Questions | Get missing information | Agent may not know to ask |

**When It Works, When It Fails:**
- Works when control structures are explicitly designed and analyzed
- Works when process model alignment is verified continuously
- Fails when feedback is missing, delayed, or misinterpreted
- Fails when control algorithms don't cover novel situations

**Scaling Characteristics:**
- Small scale: Single control loop relatively simple
- Medium scale: Hierarchical control structures needed
- Large scale: Multiple controllers require coordination; process model consistency becomes critical

**Key Takeaways for Agents:**
- Agent reliability is necessary but not sufficient; control structure must be adequate
- Supervision is a control problem: "Is the control loop functioning correctly?"
- Process models (what agent believes, what human believes, reality) are the weak point
- Use four UCA types systematically: not providing, providing, timing, duration

---

### Perspective 4: Circuit Breaker Pattern (Distributed Systems)

**Core Insight:**
The Circuit Breaker pattern prevents cascade failures by failing fast when components are unhealthy. Instead of waiting for slow timeouts or retrying endlessly, the circuit breaker "trips" and immediately returns failure---protecting the system from resource exhaustion and preventing one failure from becoming many failures.

**Mechanisms and How It Works:**

1. **The Three States:**

   ```
   ┌─────────────┐
   │   CLOSED    │───── Failure threshold exceeded ─────→ ┌─────────────┐
   │ (Normal     │                                         │    OPEN     │
   │  operation) │←──── Success threshold met ─────────── │ (Failing    │
   └─────────────┘                                         │  fast)      │
         ↑                                                 └─────────────┘
         │                                                       │
         │         ┌─────────────┐                               │
         │         │  HALF-OPEN  │←───── Timeout expires ────────┘
         └─────────│ (Testing    │
         Success   │  recovery)  │─────── Failure ───→ Back to OPEN
                   └─────────────┘
   ```

   | State | Behavior | Transition |
   |-------|----------|------------|
   | **Closed** | Normal operation, failures counted | → Open when threshold exceeded |
   | **Open** | All requests fail immediately | → Half-Open after timeout |
   | **Half-Open** | Limited test requests | → Closed on success, Open on failure |

2. **Why Fast Failure Matters:**

   | Slow Failure | Fast Failure |
   |--------------|--------------|
   | Wait 30s for timeout | Return error in 10ms |
   | Hold resources open | Release immediately |
   | Block calling threads | Free caller to handle error |
   | Resource exhaustion spreads | Failure stays contained |

   Slow failures cause cascade failures. Threads waiting on timeouts can't handle other work. Connection pools fill up. Eventually the caller fails too.

3. **Cascade Failure in Agent Systems:**

   ```
   Agent A: Code generation (failing - producing bugs)
            ↓
   Agent B: Code review (reviewing buggy code, approving it)
            ↓
   Agent C: Testing (writing tests for buggy implementation)
            ↓
   Agent D: Documentation (documenting incorrect behavior)
            ↓
   Human: Debugging a mess that looks professionally done
   ```

   Without circuit breakers, downstream agents trust upstream output. If Agent A produces garbage, everything built on that garbage is also garbage.

4. **Agent Circuit Breaker Implementation:**

   | Failure Type | Detection | Circuit Breaker Response |
   |--------------|-----------|-------------------------|
   | **Hallucination** | Verification agent, human review | Trip after N unverified claims |
   | **Task misunderstanding** | Output doesn't match intent | Trip after repeated misalignment |
   | **Loop/spin** | Token budget exhausted | Trip on budget exceed |
   | **Regression** | Previously working capability fails | Trip immediately, investigate |
   | **Capability boundary** | Agent cannot do what's asked | Trip, route elsewhere |

5. **Bulkheads for Isolation:**

   | Capability | Bulkhead | Effect of Failure |
   |------------|----------|-------------------|
   | Code generation | Own circuit breaker | Code tasks fail, others continue |
   | Code review | Own circuit breaker | Review fails, generation continues |
   | Testing | Own circuit breaker | Tests fail, code tasks continue |

   Single circuit breaker for all capabilities means one failing capability takes down everything. Separate breakers enable graceful degradation.

6. **Recovery Strategies:**

   | Strategy | When to Use |
   |----------|-------------|
   | **Automatic (after timeout)** | Transient failures, no config change needed |
   | **Manual reset required** | Security violations, data corruption, repeated trips |
   | **Progressive timeout (exponential backoff)** | Each trip increases Open duration |
   | **Canary recovery** | Test with task designed to detect failure mode |

**When It Works, When It Fails:**
- Works when failures are detectable through output verification
- Works when alternative paths exist (human fallback, other agents)
- Fails when failure detection is slow (subtle semantic errors)
- Fails when no alternative exists (critical path with no fallback)

**Scaling Characteristics:**
- Any scale: Pattern applies universally
- More agents = more potential cascade paths = more circuit breakers needed
- Hierarchical breakers: task-level, agent-level, capability-level, pipeline-level, system-level

**Key Takeaways for Agents:**
- Fail fast is kindness---don't waste resources on doomed tasks
- Bulkheads isolate failures; single breaker creates single point of failure
- Trust is dynamic: Closed = high trust, Open = low trust, Half-Open = testing
- Recovery requires testing---don't assume agent is recovered

---

### Perspective 5: Emergent Coordination Self-Repair (Jazz Improvisation)

**Core Insight:**
Jazz musicians recover from errors without stopping---the music continues regardless. This isn't achieved through explicit error correction protocols but through **error tolerance built into the coordination grammar**. When one musician makes a mistake, others adapt around it, often incorporating the "error" into the evolving musical direction. The system absorbs errors rather than propagating them.

**Mechanisms and How It Works:**

1. **Playing Through Errors:**

   | Jazz Approach | Agent Equivalent |
   |---------------|------------------|
   | Don't stop when error occurs | Continue with degraded functionality |
   | Other musicians adapt to error | Other agents route around failed agent |
   | Sometimes incorporate error | Treat unexpected output as alternative approach |
   | Rhythm section maintains stability | Core services remain available |

   The key insight: **recovery without stopping** requires error tolerance at every level. Systems that halt on any error cannot achieve this.

2. **Graceful Degradation Hierarchy:**

   ```
   Level 0: Full Functionality
   All agents available, all features operational

   Level 1: Reduced Agents
   Some agents unavailable
   - Continue with reduced parallelism
   - Queue work for unavailable agents
   - Do not fail entire workflows

   Level 2: Reduced Features
   Some capabilities unavailable
   - Continue with available capabilities
   - Clearly mark unavailable features

   Level 3: Minimal Operation
   Critical agents only
   - Handle only essential operations
   - Queue non-essential work
   - Alert for human attention
   ```

3. **Error Tolerance vs. Error Blindness:**

   | Error Tolerance | Error Blindness |
   |-----------------|-----------------|
   | Acknowledge error, continue operation | Ignore error, assume success |
   | Degrade functionality appropriately | Maintain illusion of full capability |
   | Surface error for later analysis | Hide error, lose information |
   | Prevent cascade while preserving progress | Either cascade or ignore |

   Error tolerance is not ignoring errors---it's handling them in ways that preserve system operation while maintaining visibility.

4. **Recovery Without Explicit Protocols:**

   Jazz achieves recovery through **shared grammar**, not explicit recovery procedures:

   | Grammar Element | Recovery Effect |
   |-----------------|-----------------|
   | Shared harmonic conventions | Other players know where to go even if one is lost |
   | Predictable phrase structures | Easy to find re-entry point |
   | Rhythmic foundation | Always know where "one" is |
   | Call-and-response patterns | Natural synchronization points |

   For agents, this translates to: **invest in conventions that make recovery implicit**. If agents share strong enough conventions, they can recover from errors without explicit coordination.

5. **The "Mistake as Feature" Principle:**

   Jazz musicians sometimes turn mistakes into features:
   ```
   Musician plays "wrong" note
        ↓
   Others hear it as intentional
        ↓
   Ensemble follows the new direction
        ↓
   "Mistake" becomes interesting variation
   ```

   For agents: some "errors" are alternative approaches. Systems that rigidly enforce single correct paths miss opportunities for creative solutions. Design for flexibility in what counts as correct.

**When It Works, When It Fails:**
- Works when shared grammar is strong enough to enable implicit recovery
- Works when errors are local and don't corrupt global state
- Fails when "error" actually corrupts downstream data
- Fails when no shared convention exists for the situation

**Scaling Characteristics:**
- Small ensembles: Direct mutual adaptation
- Larger groups: Need "rhythm section" equivalent (stable core services)
- Very large: Hierarchical grouping, sub-ensembles with interfaces

**Key Takeaways for Agents:**
- Design for operation despite errors, not operation assuming no errors
- Graceful degradation requires pre-planned degradation levels
- Error tolerance is not error blindness---surface errors while continuing
- Strong conventions enable recovery without explicit protocols

---

### Perspective 6: Jidoka - Automation with Human Touch (Lean Manufacturing)

**Core Insight:**
Jidoka---"automation with a human touch"---provides a principled answer to when automated systems should stop and escalate to humans. The naive approaches (continue and hope, or escalate everything) either miss critical failures or sacrifice efficiency. Jidoka offers a third path: **build detection into automation so systems recognize when human judgment is needed**.

**Mechanisms and How It Works:**

1. **The Abnormality Detection Philosophy:**

   | Phase | Human Role | Agent Role |
   |-------|-----------|------------|
   | Routine operation | Absent | Execute autonomously |
   | Abnormality detection | Absent | Monitor for deviations |
   | Escalation signal | Receives signal | Stops, provides context |
   | Judgment exercise | Makes decision | Waits or provides options |
   | Resolution | Validates | Implements or resumes |

2. **Abnormality Categories for Agents:**

   | Category | Examples | Detection Method |
   |----------|----------|------------------|
   | **Explicit failures** | API errors, parsing failures, timeouts | Already visible |
   | **Confidence signals** | Low confidence, multiple interpretations | Threshold checking |
   | **Consistency signals** | Contradicts prior outputs, contradicts facts | Baseline comparison |
   | **Scope signals** | Exceeds boundaries, anomalous resource use | Envelope monitoring |
   | **Pattern signals** | Matches known error patterns | Pattern library matching |

3. **Tiered Escalation:**

   ```
   Tier 0: Routine Proceed
   - High confidence (>90%), familiar task, low stakes
   - Action: Execute, log

   Tier 1: Proceed with Caution
   - Moderate confidence (70-90%), known task with variation
   - Action: Execute, note concerns, flag for review

   Tier 2: Checkpoint Required
   - Low confidence (50-70%), unfamiliar elements
   - Action: Checkpoint, request confirmation before proceeding

   Tier 3: Full Stop
   - Very low confidence (<50%), unknown territory, high stakes
   - Action: Stop, full context dump, wait for human
   ```

4. **The Hidden Failure Cost Curve:**

   | Detection Point | Typical Cost | Why |
   |----------------|--------------|-----|
   | During generation | 1x | Agent regenerates or escalates |
   | After initial output | 10x | Human review, correction, rework |
   | After downstream use | 100x | Propagated errors, multiple corrections |
   | After external impact | 1000x+ | Customer impact, remediation |

   Jidoka's stopping cost (interruption, human attention) is a small upfront investment to avoid large downstream costs.

5. **Learning Loop Integration:**

   ```
   Escalation occurs
        ↓
   Human resolves
        ↓
   Classify outcome:
   - True positive (correct escalation)
   - False positive (unnecessary escalation)
   - Near miss (different problem than flagged)
        ↓
   Extract learning:
   - Should detection trigger earlier/differently?
   - New pattern to add to library?
   - Documentation gap to fill?
        ↓
   Implement improvement
        ↓
   Track recurrence
   ```

6. **Organizational Culture Requirements:**

   | Undermining Culture | Enabling Culture |
   |--------------------|------------------|
   | Penalizing uncertainty | Rewarding early detection |
   | Optimizing throughput over quality | Celebrating catches |
   | Treating escalation as failure | Learning from every escalation |
   | Dismissing "too cautious" agents | Distinguishing signal quality from outcome |

   **The NUMMI lesson:** Jidoka mechanisms are worthless without supporting culture. Workers were "too afraid to pull the andon cord" because culture punished problem identification.

**When It Works, When It Fails:**
- Works when abnormality categories are well-defined
- Works when human response to escalation is reliable and timely
- Fails when culture penalizes escalation
- Fails when novel abnormalities don't match detection patterns

**Scaling Characteristics:**
- Single agent: Straightforward detection and escalation
- Multiple agents: Central escalation handling with distributed detection
- Large scale: Human response capacity becomes bottleneck

**Key Takeaways for Agents:**
- Build detection into automation; don't treat all outputs equally
- Tiered escalation matches response to stakes and confidence
- Early detection is economically rational (cost curve)
- Culture must support escalation or mechanisms become decoration

---

## Cross-Cutting Patterns

### What All Perspectives Agree On

**1. Early Detection Is Paramount**

Every perspective emphasizes catching errors as early as possible:
- Normal Accidents: Tight coupling propagates errors before intervention
- Swiss Cheese: Latent conditions must be found before they combine
- STAMP: Process model misalignment must be caught before action
- Circuit Breaker: Fast failure prevents cascade
- Jazz: Errors absorbed locally don't propagate
- Jidoka: Detection during generation costs 1x; after impact costs 1000x

**2. Explicit Boundaries Enable Recovery**

All perspectives advocate for clear boundaries:
- Normal Accidents: Loose coupling through boundaries (queues, independent contexts)
- Swiss Cheese: Defense layers with independent failure modes
- STAMP: Control structures with explicit feedback loops
- Circuit Breaker: Bulkheads isolating capabilities
- Jazz: Role boundaries (rhythm section vs. soloists)
- Jidoka: Escalation tiers with defined transitions

**3. Single Point of Failure Must Be Avoided**

Every perspective warns against concentrated failure:
- Normal Accidents: Complex interactions create unexpected failure paths
- Swiss Cheese: Common-mode failures defeat redundant defenses
- STAMP: Single controller with inadequate process model
- Circuit Breaker: Single breaker means single failure takes down everything
- Jazz: Need stable core (rhythm section) independent of individuals
- Jidoka: Human response capacity as single bottleneck at scale

**4. Learning From Failures Is Essential**

All perspectives emphasize systematic improvement:
- Normal Accidents: Understand why certain structures produce inevitable accidents
- Swiss Cheese: Identify latent conditions before they combine
- STAMP: Analyze control structure failures, improve feedback
- Circuit Breaker: Half-Open state tests recovery; adjust thresholds based on data
- Jazz: Mistakes sometimes become features; conventions evolve
- Jidoka: Every escalation is a learning opportunity

**5. Human Judgment Has a Specific, Critical Role**

Every perspective identifies where human involvement is essential:
- Normal Accidents: Humans provide loose coupling through time buffer
- Swiss Cheese: Soft defenses require human attention
- STAMP: Humans are controllers in the control structure
- Circuit Breaker: Manual reset for certain failure types
- Jazz: Shared mental models require human construction
- Jidoka: Human judgment for abnormal situations

### Where Perspectives Diverge

**1. Automation vs. Human Involvement**

| Perspective | Bias | Rationale |
|-------------|------|-----------|
| Normal Accidents | Skeptical of automation | Complexity breeds inevitable accidents |
| Swiss Cheese | Neutral | Both hard and soft defenses needed |
| STAMP | Structured | Humans are controllers; design the control loop |
| Circuit Breaker | Automation-friendly | Automate detection, reserve humans for recovery |
| Jazz | Human-centric | Human conventions enable emergent coordination |
| Jidoka | Balanced | Automation for routine, humans for abnormal |

**2. Prevention vs. Recovery**

| Perspective | Emphasis | Why |
|-------------|----------|-----|
| Normal Accidents | Prevention (or don't build) | Some systems can't be made safe |
| Swiss Cheese | Prevention (address latent conditions) | Easier to prevent than recover |
| STAMP | Prevention (design control structure) | Adequate control prevents accidents |
| Circuit Breaker | Recovery (fail fast, try again) | Failures will happen; recover quickly |
| Jazz | Recovery (play through) | Continuation is paramount |
| Jidoka | Detection + recovery | Catch early, recover with human help |

**3. Centralized vs. Distributed Error Handling**

| Perspective | Preference | Condition |
|-------------|------------|-----------|
| Normal Accidents | Neither (reduce complexity) | Both add interaction pathways |
| Swiss Cheese | Defense in depth (layers) | Multiple independent defenses |
| STAMP | Hierarchical control | Controllers at each level |
| Circuit Breaker | Per-capability breakers | Isolation through bulkheads |
| Jazz | Distributed (local adaptation) | Shared conventions enable |
| Jidoka | Centralized escalation, distributed detection | Best of both |

### Why Divergences Exist

The perspectives diverge because they emerged from different contexts:

**Safety Engineering (Normal Accidents, Swiss Cheese, STAMP):**
- Emerged from catastrophic failures (nuclear, aviation)
- Bias toward preventing rare but severe accidents
- Accepts efficiency loss for safety

**Distributed Systems (Circuit Breaker):**
- Emerged from service reliability
- Bias toward availability and recovery
- Accepts some failure for overall uptime

**Creative/Production (Jazz, Jidoka):**
- Emerged from continuous operation requirements
- Bias toward continuation despite imperfection
- Accepts some quality variation for flow

For agent systems, the right synthesis depends on stakes:
- **High stakes (data corruption, security):** Lean toward safety engineering
- **Medium stakes (productivity, quality):** Balanced approach
- **Low stakes (exploration, development):** Lean toward recovery-focused

---

## Scaling Analysis

### Small Scale (2-5 Agents)

**What Works:**
- Direct mutual monitoring (each agent can observe others)
- Simple circuit breakers (per-agent or per-task)
- Human-in-the-loop at every transition
- Informal conventions suffice

**Error Detection:**
- All agents can verify each other's outputs
- Human sees full context at each step
- Errors caught within 1-2 steps

**Recovery:**
- Human easily coordinates recovery
- Rollback is straightforward (limited scope)
- Can afford to stop and restart

**Characteristic Failure Mode:**
- Over-reliance on human verification (human becomes bottleneck)
- Insufficient automation of detection

### Medium Scale (5-20 Agents)

**What Works:**
- Hierarchical detection (team leads verify within teams)
- Per-capability circuit breakers with bulkheads
- Human checkpoints at phase boundaries
- Documented conventions (CLAUDE.md) become essential

**Error Detection:**
- Dedicated verification agents or services
- Pattern libraries for known failure modes
- Sampling-based human review

**Recovery:**
- Automated recovery for routine failures
- Human escalation for novel failures
- Some ability to continue with degraded functionality

**Characteristic Failure Mode:**
- Convention drift (different teams develop different practices)
- Detection gaps at team boundaries
- Human attention becomes limiting factor

### Large Scale (20-100+ Agents)

**What Works:**
- Centralized detection infrastructure with distributed sensing
- Hierarchical circuit breakers (agent → capability → team → system)
- Human attention reserved for novel or high-stakes situations
- Strong conventions (shared grammar) essential

**Error Detection:**
- Statistical anomaly detection
- System-level pattern recognition
- Automated triage before human involvement

**Recovery:**
- Automated recovery for vast majority of failures
- Graceful degradation is default operating mode
- Human intervention for category shifts, not individual failures

**Characteristic Failure Mode:**
- Novel failure modes not caught by statistical detection
- Convention enforcement breaks down
- Coordination overhead becomes dominant cost

### Scale Transition Points

**5 Agents → Formalize Conventions**
- Informal conventions become ambiguous
- Need documented CLAUDE.md equivalent
- Detection rules must be explicit

**15 Agents → Hierarchical Detection**
- Single human can't review everything
- Need team structure with verification responsibilities
- Detection becomes distributed

**50 Agents → Statistical Detection**
- Individual review impossible
- Pattern-based detection essential
- Human role shifts to exception handling

**100+ Agents → Recovery-First Architecture**
- Prevention alone insufficient
- Design for continuous partial failure
- Graceful degradation is the normal state

---

## Decision Framework

### When to Use Which Approach

**Question 1: What are the stakes?**

| Stakes | Recommended Approach | Why |
|--------|---------------------|-----|
| Critical (data integrity, security, safety) | Prevention-focused (STAMP, Swiss Cheese) | Consequences of failure justify overhead |
| High (production, customer-facing) | Balanced (Jidoka, Circuit Breaker) | Need both prevention and recovery |
| Medium (internal, recoverable) | Recovery-focused (Circuit Breaker, Jazz) | Speed more valuable than perfection |
| Low (exploration, development) | Minimal (basic circuit breaker) | Over-engineering wastes resources |

**Question 2: How detectable are errors?**

| Detectability | Recommended Approach | Why |
|---------------|---------------------|-----|
| Immediately visible | Circuit Breaker | Fast automated detection/recovery |
| Delayed visibility | Jidoka (tiered escalation) | Human judgment for uncertain cases |
| Hard to detect | Swiss Cheese (defense in depth) | Multiple layers catch different errors |
| May never be detected | Normal Accidents (design review) | Reconsider the architecture |

**Question 3: How reversible is damage?**

| Reversibility | Recommended Approach | Why |
|---------------|---------------------|-----|
| Fully reversible | Jazz (play through) | Recover by trying again |
| Partially reversible | Circuit Breaker + checkpoints | Recover to known good state |
| Difficult to reverse | Jidoka (pre-action validation) | Prevent before damage |
| Irreversible | STAMP (control structure) | Must prevent, cannot recover |

**Question 4: What scale?**

| Scale | Recommended Approach | Why |
|-------|---------------------|-----|
| 2-5 agents | Human-heavy, simple automation | Human attention affordable |
| 5-20 agents | Balanced automation + human checkpoints | Scale demands automation |
| 20-100 agents | Automation-first, human for exceptions | Human attention scarce |
| 100+ agents | Statistical detection, graceful degradation | Individual attention impossible |

### Decision Matrix

```
                          Error Detectability
                    Immediate    Delayed    Hard
              ┌─────────────┬────────────┬────────────┐
   High       │ Circuit     │ Jidoka     │ Swiss      │
   Stakes     │ Breaker +   │ (tiered    │ Cheese +   │
              │ Jidoka      │ escalation)│ STAMP      │
              ├─────────────┼────────────┼────────────┤
   Medium     │ Circuit     │ Circuit    │ Jidoka     │
   Stakes     │ Breaker     │ Breaker +  │ + Swiss    │
              │ alone       │ sampling   │ Cheese     │
              ├─────────────┼────────────┼────────────┤
   Low        │ Basic       │ Basic      │ Reconsider │
   Stakes     │ retry       │ Circuit    │ design     │
              │             │ Breaker    │            │
              └─────────────┴────────────┴────────────┘
```

---

## Implementation Checklist

### Phase 1: Foundation (Before Multi-Agent)

**Detection Infrastructure:**
- [ ] Define abnormality categories relevant to your system
- [ ] Implement explicit failure detection (errors, timeouts)
- [ ] Implement confidence threshold checking
- [ ] Implement consistency checking against baselines
- [ ] Implement scope boundary monitoring
- [ ] Create pattern library of known failure modes

**Recovery Infrastructure:**
- [ ] Implement basic circuit breaker (closed/open/half-open)
- [ ] Define escalation tiers and transitions
- [ ] Create escalation record format
- [ ] Establish human response process
- [ ] Design graceful degradation levels

**Measurement:**
- [ ] Track escalation rate
- [ ] Track hidden failure rate (sampling)
- [ ] Track detection latency
- [ ] Track recovery success rate

### Phase 2: Single-Agent Validation

**Verify:**
- [ ] Agent follows abnormality detection protocol
- [ ] Agent escalates appropriately (not too much, not too little)
- [ ] Human receives actionable escalation context
- [ ] Recovery after escalation works correctly
- [ ] Learning loop captures improvement opportunities

### Phase 3: Multi-Agent Extension

**Detection:**
- [ ] Input validation at agent boundaries
- [ ] Provenance tracking through pipeline
- [ ] Confidence decay through chains
- [ ] Inter-agent concern signaling

**Recovery:**
- [ ] Per-capability circuit breakers
- [ ] Bulkhead isolation
- [ ] Cascade detection and prevention
- [ ] Dependency-aware recovery

### Phase 4: Scale Preparation

**Infrastructure:**
- [ ] Centralized detection service
- [ ] Statistical anomaly detection
- [ ] Hierarchical circuit breakers
- [ ] Automated triage before human involvement

**Process:**
- [ ] Convention documentation complete
- [ ] Detection rule governance
- [ ] Human attention prioritization
- [ ] Continuous improvement process

---

## Failure Mode Taxonomy

### Detection Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| **Undetected error** | Problem discovered post-output | Detection rules don't cover case | Add detection rule |
| **Detection too late** | Caught but damage done | Detection after critical action | Move detection earlier |
| **Wrong detection type** | Escalated for wrong reason | Rules misclassified | Improve specificity |
| **Detection overwhelmed** | Too many escalations | Threshold too sensitive | Calibrate threshold |
| **Novel failure blindness** | New failure type not caught | No pattern in library | Pattern library expansion |

### Recovery Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| **No recovery path** | System halts on error | Recovery not designed | Design recovery for each failure type |
| **Incomplete recovery** | Inconsistent state after recovery | Recovery logic incomplete | Complete recovery protocol |
| **Recovery creates error** | New problem from fix | Side effects not considered | Test recovery paths |
| **Cascade despite recovery** | Error propagates | Recovery too slow | Earlier detection, faster recovery |
| **Recovery thrashing** | Repeated recovery attempts | Not addressing root cause | Escalate to human |

### Organizational Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| **Escalation ignored** | Human doesn't respond | Human overloaded | Reduce load, triage |
| **Escalation suppressed** | Agent continues despite problem | Culture penalizes escalation | Change incentives |
| **Learning not implemented** | Same errors recur | No improvement loop | Close loop on learning |
| **Trust miscalibration** | Over/under-reliance on agents | Trust not updated from evidence | Systematic trust calibration |
| **Complacency** | Validation attention drops | Extended reliability | Periodic stress tests |

### Cascade Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| **Error propagation** | Downstream agents consume bad input | No input validation | Validate at boundaries |
| **Common-mode defeat** | Multiple defenses fail together | Shared vulnerability | Independent failure modes |
| **Correlated failures** | Multiple agents fail simultaneously | Shared dependency | Reduce coupling |
| **Retry amplification** | Retries create overload | No backoff | Exponential backoff, jitter |
| **Recovery cascade** | Fix causes new problems | Dependencies not understood | Map dependencies |

---

## Anti-Patterns

### Anti-Pattern 1: Trust All Outputs Equally

**What it looks like:** All agent outputs go directly to next stage without verification.

**Why it's tempting:** Maximizes throughput, simplest architecture, "the agent is usually right."

**Why it fails:** Errors propagate silently through entire pipeline. By the time error surfaces, significant work is corrupted. Root cause becomes obscured.

**What to do instead:** Verification at boundaries, tiered based on stakes and confidence.

### Anti-Pattern 2: Verify Everything

**What it looks like:** Human reviews every agent output before proceeding.

**Why it's tempting:** Maximum safety, catches all errors, feels responsible.

**Why it fails:** Human becomes bottleneck. Verification attention degrades under volume. Wastes human attention on routine correct outputs.

**What to do instead:** Tiered escalation. Automate routine verification. Reserve human attention for abnormal cases.

### Anti-Pattern 3: No Circuit Breaker (Blind Retry)

**What it looks like:** Task fails → retry immediately → fails → retry → fails...

**Why it's tempting:** Persistence seems virtuous. "Maybe it will work this time."

**Why it fails:** Wastes resources, never gives system time to recover, can accelerate failure through retry storms.

**What to do instead:** Circuit breaker with exponential backoff. Trip after threshold, give system recovery time.

### Anti-Pattern 4: Single Global Circuit Breaker

**What it looks like:** One circuit breaker for all agent capabilities.

**Why it's tempting:** Simple to implement, clear system state.

**Why it fails:** One failing capability takes down all capabilities. No graceful degradation.

**What to do instead:** Per-capability bulkheads. Isolate failures so partial operation continues.

### Anti-Pattern 5: Ignoring Soft Failures

**What it looks like:** Only explicit errors (crashes, timeouts) trigger detection. Semantic errors pass through.

**Why it's tempting:** Easy to detect hard failures. Semantic errors are hard to catch.

**Why it fails:** Most agent failures are soft (wrong output, not no output). Semantic errors are the dangerous ones.

**What to do instead:** Consistency checking, confidence thresholds, pattern matching for known failure modes.

### Anti-Pattern 6: No Learning Loop

**What it looks like:** Errors are fixed individually. No systematic improvement.

**Why it's tempting:** Faster to fix than to analyze. Improvement process takes time.

**Why it fails:** Same error patterns recur. Detection never improves. Latent conditions accumulate.

**What to do instead:** Every escalation is a learning opportunity. Track patterns. Improve detection based on evidence.

### Anti-Pattern 7: Blame the Agent

**What it looks like:** Analysis stops at "the agent made an error." Fix is "tell agent not to do that."

**Why it's tempting:** Visible cause at the "sharp end." Easy to blame.

**Why it fails:** Agent errors are symptoms of latent conditions. Addressing only symptoms guarantees recurrence.

**What to do instead:** Trace causation upstream. What configuration, context, or design enabled the failure? Fix systemic causes.

---

## Key Insights

### 1. Error Detection Is Cheaper Than Error Recovery Is Cheaper Than Error Propagation

The cost curve is exponential. Every stage of propagation multiplies remediation cost. Investment in early detection pays outsized returns. The cheapest error to fix is the one caught before it affects anything else.

### 2. Soft Failures Are More Dangerous Than Hard Failures

Hard failures (crashes, timeouts) are visible and obvious. Soft failures (wrong output) look like correct operation. Systems that only catch hard failures will be surprised by soft failures that cascade through the pipeline. Design detection for semantic correctness, not just operational success.

### 3. Complexity Creates Novel Failure Modes

Every component added creates new interaction pathways. Some of those pathways produce failures no one anticipated. More agents is not always more capability---it may be more failure modes. Add complexity only when the capability gain justifies the failure mode exposure.

### 4. Loose Coupling Is Insurance You Pay Upfront

Tight coupling maximizes efficiency when everything works. Loose coupling (independent contexts, queues, checkpoints) costs efficiency but buys resilience. When errors occur in tightly coupled systems, they cascade before intervention is possible. The "waste" of loose coupling is actually insurance.

### 5. Trust Should Be Earned, Lost, and Re-Earned

Trust in agents should follow evidence:
- Start with low trust (high verification)
- Increase trust as reliability demonstrated
- Lose trust quickly on failure
- Rebuild trust slowly through demonstrated recovery

The Circuit Breaker pattern operationalizes this: Closed = trust, Open = no trust, Half-Open = testing.

### 6. Human Attention Is the Scarcest Resource

At scale, human attention becomes the limiting factor. Systems that require human verification of all outputs don't scale. Systems that need human intervention for all failures don't scale. Reserve human attention for novel situations, high stakes, and genuine uncertainty.

### 7. Some Architectures Cannot Be Made Safe

Normal Accident Theory's uncomfortable conclusion: certain combinations of complexity and coupling produce inevitable accidents regardless of safety measures. The answer is not always "make it safer" but sometimes "don't build it this way." Recognize when architecture redesign is needed.

### 8. Learning From Failures Is a Competitive Advantage

Systems that systematically learn from failures improve their detection, reduce their failure rates, and catch novel failures faster. Systems that treat failures as one-off events to fix and forget repeat the same mistakes. The learning loop is not overhead; it's the mechanism for improvement.

### 9. Graceful Degradation Is Better Than Binary Operation

Systems that either work perfectly or fail completely are fragile. Systems that can operate at reduced capacity---fewer features, slower operation, more human involvement---survive conditions that break fragile systems. Design degradation levels explicitly.

### 10. Culture Determines Whether Mechanisms Work

The best detection and recovery mechanisms fail in cultures that penalize escalation, blame individuals for systemic problems, or optimize for throughput over quality. Mechanisms are necessary but not sufficient. Culture must support error surfacing and learning.

---

## Related Problems

### How This Problem Connects to Others

**Task Decomposition (upstream):**
- How tasks are decomposed affects error boundaries
- Smaller tasks = smaller blast radius
- Clear task boundaries enable independent recovery

**Information Flow (parallel):**
- Error signals must flow to the right places
- Detection information enables intervention
- Propagation speed affects recovery time

**Conflict Management (parallel):**
- Error recovery may conflict with ongoing operations
- Recovery actions may create new conflicts
- Coordination during degraded operation is harder

**Scaling Coordination (downstream):**
- Detection infrastructure must scale
- Human attention becomes scarcer at scale
- Learning loops must work at scale

**Trust and Oversight (parallel):**
- Error history informs trust calibration
- Recovery success affects oversight level
- Detection quality determines appropriate autonomy

### Dependencies and Ordering

**Solve First:**
1. Task Decomposition - affects error blast radius
2. Information Flow - enables detection propagation

**Solve Together:**
3. Error Detection and Recovery (this document)
4. Conflict Management - recovery may cause conflicts
5. Trust and Oversight - detection informs trust

**Solve After:**
6. Scaling Coordination - requires error infrastructure

---

## Sources

### Primary Research Documents

- `/docs/safety-engineering/normal-accidents.md` - Charles Perrow's framework for inevitable accidents in complex systems
- `/docs/safety-engineering/swiss-cheese-model.md` - James Reason's organizational accident causation model
- `/docs/safety-engineering/stamp-stpa.md` - Nancy Leveson's systems-theoretic approach to safety
- `/docs/management/circuit-breaker.md` - Michael Nygard's cascade prevention pattern
- `/docs/jazz-improvisation/emergent-coordination-agent-analysis.md` - Self-repair through shared conventions
- `/docs/lean-manufacturing/jidoka-automation-with-human-touch-agent-analysis.md` - Detection and escalation philosophy

### Foundational Works

- Perrow, C. (1984). *Normal Accidents: Living with High-Risk Technologies*. Basic Books.
- Reason, J. (1990). *Human Error*. Cambridge University Press.
- Reason, J. (1997). *Managing the Risks of Organizational Accidents*. Ashgate.
- Leveson, N. (2011). *Engineering a Safer World*. MIT Press.
- Nygard, M. (2018). *Release It!* (2nd ed.). Pragmatic Bookshelf.
- Ohno, T. (1988). *Toyota Production System*. Productivity Press.

### Related Synthesis Documents

- `/docs/syntheses/conflict-management-synthesis.md` - Related coordination challenges
- `/docs/syntheses/information-flow-synthesis.md` - How error signals propagate
- `/docs/syntheses/scaling-coordination-synthesis.md` - Error handling at scale

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Cross-disciplinary synthesis of error detection and recovery perspectives
**Perspectives Integrated:** 6 (Normal Accidents, Swiss Cheese, STAMP/STPA, Circuit Breaker, Jazz Self-Repair, Jidoka)
**Status:** Complete
