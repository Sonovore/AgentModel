# Boyd's OODA Loop: Architectural Analysis for AI Agent Systems

## Executive Summary

The OODA Loop---Observe, Orient, Decide, Act---is commonly misunderstood as a linear decision cycle. Boyd's actual insight was deeper: **Orient is the center of gravity that shapes all other phases, and the ability to re-orient faster than an adversary creates decisive advantage.**

For AI agent systems, this reframing transforms OODA from a descriptive model of agent behavior into a prescriptive framework for agent architecture. The key insight is not that agents cycle through OODA phases (they do, obviously), but that **the asymmetric performance of agents across OODA phases creates specific architectural constraints and opportunities**.

| Phase | Agent vs. Human | Architectural Implication |
|-------|-----------------|---------------------------|
| **Observe** | 100-1000x faster | Observation is essentially free; the question is what to observe, not whether to observe |
| **Orient** | 0.1-10x (highly variable) | **This is the bottleneck.** Agent success depends on orientation quality, which depends on factors agents don't control |
| **Decide** | 10-100x faster (when oriented) | Decisions are cheap once oriented; the failure mode is deciding before orientation completes |
| **Act** | 10-100x faster | Actions are cheap but irreversible; the challenge is acting on correct orientation |

**The central architectural claim of this document:** Agent systems should be designed around the Orient phase because that is where both the largest variance and the largest opportunity exist. Systems that optimize Observe, Decide, or Act without addressing Orient hit diminishing returns. Systems that optimize Orient achieve compounding gains.

This analysis serves three purposes:
1. **Design framework** for architecting agent systems that account for orientation constraints
2. **Diagnostic framework** for understanding why agents fail and how to fix them
3. **Template** for applying other mental models to agent architecture through systematic analysis

---

## Part I: Boyd's Framework---Beyond the Textbook Summary

### What Practitioners Think They Understand

The surface-level understanding: "OODA is a decision loop. Agents observe, orient, decide, and act. Faster loops win."

This framing treats OODA as a linear sequence. It implies that optimization means speeding up each phase. It suggests that agent improvement is about reducing latency.

This understanding is dangerously incomplete.

### What Boyd Actually Argued

Boyd's OODA framework emerged from his study of air combat in Korea, where F-86 Sabres achieved 10:1 kill ratios against MiG-15s despite the MiG's superior speed, climb rate, and ceiling. The explanation was not faster reaction time but better orientation capability.

The F-86's bubble canopy provided 360-degree visibility. Pilots could see threats from all directions. The MiG-15's framed canopy limited pilot vision to narrow sectors. This observational advantage enabled F-86 pilots to orient to the tactical situation faster than MiG pilots could.

But Boyd's insight went deeper. He observed that pilots who could re-orient mid-engagement---updating their mental model as the situation changed---outperformed pilots who stuck to their initial orientation regardless of new information.

**The key insight: OODA is not about speed through the loop. It is about adaptability within the loop, especially the ability to destroy and rebuild mental models in the Orient phase.**

### The Actual Diagram: Orient at the Center

Boyd's actual OODA diagram is not a simple loop:

```
                         Implicit Guidance & Control (IG&C)
                    ┌──────────────────────────────────────────┐
                    │                                          │
                    v                                          │
              ┌──────────┐     ┌──────────┐     ┌──────────┐  │
Observation ──┤  ORIENT  ├────>│  DECIDE  ├────>│   ACT    ├──┘
     ^        └──────────┘     └──────────┘     └──────────┘
     │              │                                 │
     │              │     Feedback loops from        │
     │              │     all phases back to         │
     │              v     Observe and Orient         │
     │         ┌────────────────────────────────────>│
     │         │                                     │
     └─────────┴─────────────────────────────────────┘
```

Critical features often omitted:

1. **Multiple feedback paths**: Every phase feeds back to Observe and Orient, not just Act
2. **Implicit Guidance & Control (IG&C)**: A direct path from Orient to Act that bypasses Decide entirely
3. **Orient as the schwerpunkt**: Orient determines what observations are sought, what decisions are considered, what actions are available

The IG&C path is particularly important. Boyd observed that experienced pilots do not consciously decide in combat. They act from orientation. The situation is recognized; the appropriate action is implicit in the recognition. Decision is a separate phase only for novel situations where orientation does not immediately indicate action.

### Destruction and Creation: The Epistemology of Orientation

Boyd's unpublished 1976 paper "Destruction and Creation" describes the cognitive process underlying orientation:

**Destruction**: Taking apart existing mental models, identifying their components, examining their assumptions

**Creation**: Reassembling components into new configurations that better match observed reality

This is not passive learning. It is active destruction of inadequate models followed by creative reconstruction. Boyd drew on Godel's incompleteness theorems and Heisenberg's uncertainty principle to argue that no mental model can perfectly capture reality. All models are incomplete and will eventually fail. The adaptive response is not to build better models but to build faster destruction-creation cycles.

**Agent application**: Orientation is not accumulating information. It is actively questioning assumptions and rebuilding mental models. An agent that reads 50 files and confirms its initial hypothesis has not oriented. An agent that reads 5 files and realizes its initial hypothesis was wrong has oriented better.

### The Five Elements of Orientation

Boyd identified five inputs that shape orientation:

| Element | Description | Agent Equivalent |
|---------|-------------|------------------|
| **Genetic Heritage** | Innate cognitive patterns shaped by evolution | Model architecture and training |
| **Cultural Traditions** | Learned patterns from social context | CLAUDE.md, project conventions, organizational norms |
| **Previous Experiences** | Personal history of situations and outcomes | Session context, prior tool outputs, conversation history |
| **New Information** | Current sensory input about the environment | Current observations (grep results, file contents, API responses) |
| **Analysis/Synthesis** | The destruction-creation engine that processes inputs | The cognitive process that builds mental models from the above |

Four of these are inputs. Only Analysis/Synthesis is the process. Most agent optimization focuses on inputs: better CLAUDE.md (cultural traditions), more context (previous experiences), more observations (new information). Little focuses on improving the synthesis process itself.

This is a significant insight for agent architecture. The quality of orientation depends not just on what information is available but on how that information is processed into mental models. Two agents with identical inputs can have radically different orientation quality.

---

## Part II: Why Orient Is the Bottleneck

### The Asymmetric Agent

Consider what happens when an agent receives a task:

**Observation is essentially instant.** An agent can grep a codebase in milliseconds, read 20 files in parallel, process thousands of lines without fatigue. The cost of observation is effectively zero. The question is not "should I observe?" but "what should I observe?"

**Action is fast and mechanical.** Once an agent has decided what to do, execution is rapid: perfect syntax, no typos, fast iteration. The bottleneck is not typing speed.

**Decision is fast once orientation is complete.** Given a clear understanding of the situation and available options, agents decide quickly. They have no ego to defend, no sunk cost fallacy, no fatigue-induced slowdown.

**Orientation is where variance explodes.** The time and success rate of orientation depends on factors largely outside the agent's control: quality of documentation, consistency of codebase patterns, clarity of task specification, presence of contradictory information.

This asymmetry has architectural implications. If observation, decision, and action are fast while orientation is slow and variable, then:

1. **Observation quantity is cheap.** Agents can afford to observe broadly before narrowing focus
2. **Orientation quality is expensive.** The cost of re-orientation after failed action exceeds the cost of thorough initial orientation
3. **Decision velocity is misleading.** Fast decisions based on bad orientation are worse than slow decisions based on good orientation
4. **Action reversibility matters.** Irreversible actions lock in orientation errors; reversible actions allow recovery

### How Orientation Fails in Agents

Agent orientation failures follow predictable patterns:

**Failure Mode 1: Orientation from insufficient observation**

The agent reads 3 files, forms a hypothesis, and acts. The hypothesis was based on an unrepresentative sample. The action fails. The agent reads 3 more files, forms a new hypothesis, and acts. The pattern repeats.

This is not an observation failure (the agent could have observed more) but an orientation failure (the agent treated incomplete observation as complete).

**Diagnosis**: Agent consistently fails on first attempt but succeeds on subsequent attempts with more information.

**Root cause**: Premature orientation---treating initial hypothesis as fact rather than hypothesis.

**Mitigation**: Explicit orientation checkpoints. Before acting, require the agent to report its mental model. Supervisor validates before action proceeds.

**Failure Mode 2: Orientation that ignores contradictions**

The agent observes pattern A in three files and pattern B in two files. Rather than investigating the contradiction, it picks one pattern and ignores the other. The chosen pattern turns out to be deprecated/legacy/exceptional.

**Diagnosis**: Agent's implementation follows a pattern that exists in the codebase but is not the canonical pattern.

**Root cause**: Orientation without integration---observed contradictions but did not reconcile them.

**Mitigation**: CLAUDE.md that explicitly documents canonical vs. deprecated patterns. Confirmation bias checks (see below).

**Failure Mode 3: Orientation that confirms bias**

The agent has an initial hypothesis. It searches for confirming evidence. It finds confirming evidence (because any codebase has multiple patterns). It orients to its initial hypothesis. It acts. The action is wrong because the initial hypothesis was wrong.

This is Boyd's "incestuous amplification"---orientation corrupting observation. The agent sees what it expects to see.

**Diagnosis**: Agent confidently implements the wrong approach despite having access to correct patterns.

**Root cause**: Observation filtered by orientation. Search patterns found what orientation expected to find.

**Mitigation**: Require disconfirming evidence search. Before implementing, agent must find and evaluate evidence against its approach.

**Failure Mode 4: Orientation to the wrong level of abstraction**

The agent orients to syntactic patterns (how code is formatted) rather than semantic patterns (what code means). It replicates syntax while missing semantics. The code compiles but doesn't work.

**Diagnosis**: Agent produces code that follows local conventions but violates architectural intent.

**Root cause**: Shallow orientation---pattern matching without understanding.

**Mitigation**: Architecture documentation that explains why, not just what. Examples with commentary explaining the reasoning.

**Failure Mode 5: Orientation lock-in**

The agent orients to a mental model and commits to it. New information arrives that contradicts the model. The agent filters or dismisses the new information rather than destroying and rebuilding its model.

**Diagnosis**: Agent keeps trying the same failed approach despite changing conditions.

**Root cause**: Inability or unwillingness to destroy current orientation.

**Mitigation**: Explicit re-orientation triggers. After N failures, agent must report its mental model and explicitly identify what could be wrong with it.

### Measuring Orientation Quality

A fundamental challenge: **orientation quality is invisible until action reveals it.** You cannot directly observe an agent's mental model. You can only observe the actions that emerge from that model.

This creates a measurement problem. By the time you know orientation was wrong, the agent has already acted. The cost has been incurred.

**Proxy metrics for orientation quality:**

1. **First-try success rate**: High rate suggests good orientation before action. Low rate suggests action before orientation.

2. **Questions asked during orient phase**: Questions indicate the agent recognizes gaps in its understanding. No questions might indicate premature confidence.

3. **Contradictions identified**: Agent that reports "I see conflicting patterns X and Y" is orienting more thoroughly than agent that ignores conflicts.

4. **Orientation pre-flight accuracy**: Agent reports its mental model before acting. Supervisor validates or corrects. Accuracy of agent's pre-flight orientation is a direct (though costly) measure.

5. **Re-orientation frequency**: Agent that frequently revises its approach mid-task is either orienting poorly or facing genuinely novel situations. Distinguish by examining whether early orientation was adequate.

**Direct measurement (expensive but valuable):**

Orientation pre-flight protocol:

```
Before implementing, agent reports:
1. "I understand the problem as: [problem statement]"
2. "I understand the codebase context as: [architectural understanding]"
3. "I understand the relevant patterns as: [patterns identified]"
4. "I understand the constraints as: [constraints identified]"
5. "My planned approach is: [approach] because [reasoning]"

Supervisor validates each element before agent proceeds.
```

This is expensive---it requires human review before every action. But it provides direct measurement of orientation quality and catches orientation failures before they become action failures.

For high-stakes tasks, this cost is justified. For routine tasks, sample-based review calibrates trust and identifies systematic orientation gaps.

---

## Part III: Implicit Guidance and Control (IG&C)

### What IG&C Is

Boyd's IG&C represents the fast path from Orient directly to Act, bypassing Decide. For experienced pilots, this is the dominant mode: the situation is recognized, and appropriate action follows without conscious deliberation.

This is not instinct (which is Genetic Heritage). It is trained pattern recognition. The pilot has encountered similar situations before. The appropriate response has been internalized. The "decision" is implicit in the recognition.

### Why IG&C Matters for Agents

Every decision that requires explicit deliberation consumes time and creates opportunity for error. If an agent must decide "should I run tests after making changes?" every time, it:
- Spends cycles on a question that has a consistent answer
- Creates opportunity to decide wrongly
- Cannot achieve tempo on routine tasks

When the answer becomes implicit in orientation---"of course I run tests, that's how this codebase works"---the agent operates faster and more reliably.

**The goal of agent system design should be maximizing the proportion of agent behavior that operates via IG&C.** This means:
- Documenting conventions so thoroughly that agents don't need to decide
- Providing examples so clear that agents pattern-match rather than reason
- Building orientation infrastructure that makes the right action obvious

### Developing IG&C Systematically

IG&C develops through repeated exposure to situations and outcomes. The pilot who has seen a hundred MiG engagements doesn't think about responses; responses have become automatic.

For agents, IG&C development means:

**Step 1: Identify recurring decisions**

Track what decisions agents make repeatedly. If "should I run tests?" appears 47 times, it's a candidate for IG&C.

**Step 2: Determine canonical answers**

For each recurring decision, determine the canonical answer. "Always run tests" or "Run tests when modifying business logic but not for documentation changes."

**Step 3: Encode in orientation**

Add the canonical answer to CLAUDE.md. Not as a rule to follow but as a fact about how this codebase works.

```markdown
# How This Codebase Works

Tests run automatically after code changes. This is not optional.
The build must pass before committing. A failing build is a bug.
Imports use absolute paths from @/. Relative imports are not used.
```

**Step 4: Validate IG&C activation**

Observe whether agents follow conventions without deliberating. If they still explicitly decide, the convention isn't embedded in orientation.

**Step 5: Iterate**

Track new recurring decisions. Expand IG&C coverage over time.

### The Limits of IG&C

IG&C is not appropriate for all situations:

**Novel situations**: When the agent encounters something genuinely new, IG&C provides no guidance. Explicit decision is required.

**High-stakes situations**: When errors are costly or irreversible, explicit decision with validation is appropriate even if IG&C exists.

**Ambiguous situations**: When the situation doesn't clearly match any known pattern, explicit decision resolves ambiguity.

**Conflicting conventions**: When two conventions conflict, explicit decision determines which takes precedence.

The goal is not eliminating Decide entirely but eliminating it for routine situations so agent cognitive capacity is reserved for situations that genuinely require deliberation.

### IG&C Coverage as a System Health Metric

**IG&C coverage** = (actions taken via IG&C) / (total actions)

High coverage indicates mature system with well-documented conventions and consistent patterns. Low coverage indicates either novel work or inadequate orientation infrastructure.

Tracking coverage over time reveals:
- Whether conventions are being documented and internalized
- Whether the problem space is becoming more or less routine
- Whether agent behavior is converging on patterns or diverging

A healthy system shows increasing IG&C coverage for routine tasks while maintaining explicit decision for novel tasks.

---

## Part IV: Tempo and Task Granularity

### Boyd's Concept of Tempo

Boyd distinguished tempo from speed. Speed is raw velocity through the loop. Tempo is rhythm and cadence---the ability to control the engagement's timing.

The pilot who controls tempo forces the opponent to react. The opponent is always one step behind, responding to obsolete information. By the time the opponent completes an OODA cycle, the situation has changed.

### Tempo in Agent Systems

For agents, tempo translates to task granularity---how tasks are sized relative to agent capability.

**The context window problem**: Agents have finite context. Large tasks exceed context capacity, triggering autocompact (context summarization/loss). When context resets mid-task, the agent loses orientation and must rebuild from observation.

This is equivalent to a pilot blacking out mid-engagement. They lose awareness of the situation. When consciousness returns, they must reorient from scratch while the engagement continues.

**The overhead problem**: Small tasks have fixed overhead (starting up, reading CLAUDE.md, initial observation). If tasks are too small, overhead dominates. The agent spends more time orienting than acting.

**The coherence problem**: Tasks too small lose coherence. The agent optimizes locally but misses global structure. Changes that span multiple tasks may be inconsistent.

### Task Sizing for Complete OODA Loops

The optimal task size allows a complete OODA loop within context constraints:

**Well-sized task characteristics:**

1. **Fits in context with margin**: Uses 60-80% of context window, leaving room for re-observation and re-orientation if needed

2. **Has clear scope**: Agent can identify what observation is needed, what patterns are relevant, what success looks like

3. **Allows complete action**: Agent can finish the implementation without needing to hand off mid-stream

4. **Produces observable outcome**: Agent can validate success through tests, builds, or inspection

**Task sizing heuristics:**

| Indicator | Task Too Large | Task Too Small |
|-----------|---------------|----------------|
| Context usage | >90% before completion | <30% at completion |
| Re-orientation needed | Multiple times per task | Never needed |
| Success criteria | Vague or multi-part | Trivial |
| Dependencies | Many external dependencies | No dependencies |
| Typical duration | Hours | Seconds |

**The autocompact diagnostic**: If tasks frequently trigger autocompact before completion, tasks are too large. Break them down.

**The overhead diagnostic**: If agent spends more time reading CLAUDE.md than working on task, tasks are too small. Batch them.

### Tempo Disruption

Just as a pilot can have tempo disrupted, agents can have their OODA rhythm disrupted:

**Context reset disruption**: Autocompact triggers at a critical moment, destroying orientation built over time

**External interruption disruption**: New information arrives mid-task that invalidates current orientation

**Conflicting signal disruption**: Contradictory instructions or patterns create orientation confusion

**Recovery**: When tempo is disrupted, the agent must re-observe and re-orient. This is expensive but necessary. Systems should be designed to minimize disruption and facilitate recovery when disruption occurs.

---

## Part V: Multi-Agent OODA and Einheit

### Boyd's Four Organizational Qualities

Boyd identified four qualities that enable effective organizations:

| Quality | Description | Application |
|---------|-------------|-------------|
| **Fingerspitzengefuhl** | Intuitive feel from deep experience | Pattern exposure through training/examples |
| **Einheit** | Mutual trust and shared understanding | Common CLAUDE.md, shared conventions |
| **Schwerpunkt** | Focus of effort, main point | Clear task priorities, single primary objective |
| **Auftragstaktik** | Mission-type orders (intent-based) | Goal-based task descriptions, not procedure specifications |

### Einheit: Why Shared Orientation Matters

Einheit means "oneness" or "unity"---not hierarchical unity imposed by central command, but organic unity emerging from shared understanding.

When all agents share the same orientation:
- They can predict each other's behavior
- They can coordinate implicitly without explicit communication
- They can act in parallel without stepping on each other's work

**The centralized orchestration problem**: A central orchestrator that must coordinate all agents becomes a bottleneck. The orchestrator must:
- Observe all agent states
- Orient to the system-wide situation
- Decide on task assignments
- Communicate decisions to agents
- Wait for acknowledgment
- Repeat

The orchestrator's OODA loop becomes the system's limiting factor. No agent can act faster than the orchestrator can coordinate.

**The Einheit solution**: If agents share orientation, they coordinate implicitly. The CLAUDE.md that defines conventions also defines implicit coordination protocols.

Example:
```markdown
# File Ownership Conventions

When modifying authentication:
- auth.service.ts: Primary implementation
- auth.middleware.ts: Request validation
- auth.test.ts: Test coverage

All three files should be updated together. If you touch one, update the others.
```

With this shared orientation, three agents can work in parallel:
- Agent A: "I'll update auth.service.ts"
- Agent B: "I'll update auth.middleware.ts"
- Agent C: "I'll update auth.test.ts"

No coordination message required. The assignment is implicit in the shared understanding.

### Requirements for Effective Einheit

**Common documentation**: All agents read the same CLAUDE.md. Divergent documentation creates divergent orientation.

**Consistent conventions**: Patterns must be the same everywhere. Inconsistency forces agents to discover which pattern applies where.

**Explicit interfaces**: Where agents' work areas meet, the interface must be clearly defined. Ambiguous boundaries create overlap and conflict.

**Shared schwerpunkt**: All agents must have the same primary goal. Conflicting goals create implicit conflict even with explicit coordination.

### Auftragstaktik: Intent-Based Delegation

Traditional orders specify procedure: "Edit line 47, change X to Y."

Auftragstaktik specifies intent: "Fix the race condition in the audio handler."

The difference matters because:

1. **Agent visibility**: The agent has better visibility into the codebase than the supervisor. The agent can observe patterns and dependencies the supervisor doesn't know about.

2. **Agent judgment**: Given clear intent, the agent can adapt to conditions the supervisor didn't anticipate.

3. **Temporal decoupling**: Intent remains valid even if conditions change. Procedure may become invalid if conditions differ from expectation.

**Task description quality**:

| Quality | Procedure-Based | Intent-Based |
|---------|-----------------|--------------|
| Specificity | "Change line 47" | "Fix the race condition" |
| Context | Implicit (line 47 is the problem) | Explicit (race condition is the problem) |
| Adaptability | If line 47 isn't the issue, agent is stuck | Agent finds actual issue |
| Agent capability use | Agent executes instructions | Agent applies judgment |

Intent-based delegation requires trust. The supervisor must trust that the agent can translate intent into appropriate action. This trust develops through repeated successful translations.

---

## Part VI: Getting Inside the Problem's Loop

### Boyd's Competitive Framing

Boyd's framework is fundamentally competitive: get inside the opponent's OODA loop, disrupt their orientation, force them to react to obsolete information.

For agents, there's no opponent. But there's an analogous concept: **the problem resists solution**. Complex codebases "fight back" against changes through:
- Dependencies that create cascading requirements
- Hidden coupling that creates unexpected failures
- Technical debt that creates friction
- Emergent properties that no single component explains

### Proactive vs. Reactive Problem-Solving

**Reactive approach** (outside the problem's loop):

```
Agent makes change to File A
  → Build fails (dependency in File B)
Agent fixes File B
  → Tests fail (test in File C expected old behavior)
Agent fixes File C
  → Integration breaks (File D couples to File A)
Agent fixes File D

Result: 4 OODA cycles, one per discovered dependency
```

**Proactive approach** (inside the problem's loop):

```
Agent orients to problem:
  - Greps for imports of File A → finds Files B, C, D
  - Reads Files B, C, D to understand dependencies
  - Identifies all required changes
Agent makes coordinated change to all 4 files at once

Result: 1 OODA cycle, all dependencies handled proactively
```

The proactive agent "gets inside the problem's loop" by anticipating the problem's reactions before they occur. The key is orientation---understanding the dependency structure before acting.

### Dependency Anticipation as Orientation

To get inside the problem's loop, agents must orient to:

1. **Import graphs**: What depends on what I'm changing?
2. **Test coverage**: What tests exercise the code I'm changing?
3. **Coupling patterns**: What implicit dependencies exist beyond explicit imports?
4. **Architectural constraints**: What invariants must be maintained?

This orientation is expensive. It requires observation beyond the immediate task scope. But it pays off by reducing reactive cycles.

**When to invest in deep orientation:**

- High-coupling areas (changes propagate widely)
- Unfamiliar code (agent lacks mental model)
- Irreversible actions (mistakes are costly)
- Complex interactions (multiple systems involved)

**When shallow orientation suffices:**

- Isolated code (changes don't propagate)
- Well-understood patterns (IG&C applies)
- Reversible actions (mistakes are cheap)
- Simple interactions (one system, clear boundaries)

### Orientation Infrastructure for Proactive Agents

**Dependency mapping documentation**:
```markdown
# High-Coupling Areas

## Authentication Module
Changes to auth affect: API endpoints, middleware, session management, tests
Always check: auth.service.ts, auth.middleware.ts, session.ts, auth.test.ts

## Database Schema
Changes to schema require: migration, model updates, seed data updates, documentation
Process: Create migration first, update models, update seeds, update docs
```

**Architecture decision records**:
```markdown
# ADR-003: Session Storage Strategy

Context: Session data needs to persist across server restarts
Decision: Use Redis for session storage
Consequences:
- Session service depends on Redis connection
- Session data lost if Redis is down
- Tests need Redis mock or real instance

If changing session handling, consider Redis dependency.
```

**Coupling maps**:
```
auth.service.ts → [auth.middleware.ts, session.ts, user.service.ts]
session.ts → [redis.client.ts, auth.service.ts]
api/routes.ts → [auth.middleware.ts, all controllers]
```

These artifacts front-load orientation. The agent doesn't need to discover dependencies through trial and error---they're documented.

---

## Part VII: Orientation-Hostile Environments

### What Makes an Environment Orientation-Hostile

Boyd recognized that orientation can be disrupted. In combat, this means feints, jamming, overwhelming with stimuli, creating ambiguity.

For agent systems, orientation-hostile environments arise from:

**Contradictory documentation**:
```
CLAUDE.md says: "Use async/await for all asynchronous code"
README says: "Use promises for error handling"
Code has both patterns

Agent cannot orient to "correct" approach---both are documented
```

**Inconsistent codebase patterns**:
```
Directory A: Classes with methods
Directory B: Functional components with hooks
Directory C: Mixed, neither pattern dominant

Agent cannot identify canonical pattern---multiple coexist
```

**Undocumented conventions**:
```
Convention: "Tests go in __tests__ for new code, tests/ for legacy"
Documentation: None

Agent must infer convention from examples, prone to error
```

**Missing context**:
```
Code does something unusual. Comment explains nothing. Commit message is "fix".
Agent cannot orient to why the unusual pattern exists.
Agent may "fix" it back to the obvious approach, breaking whatever the unusual pattern was handling.
```

**Frequent context resets**:
```
Task exceeds context window. Autocompact triggers repeatedly.
Agent never stabilizes mental model.
Each action is based on partial, potentially inconsistent orientation.
```

### Diagnosing Orientation-Hostile Conditions

**Symptoms**:
- Agent makes inconsistent decisions on similar tasks
- Agent asks the same questions repeatedly across sessions
- Agent copies wrong patterns despite having read documentation
- Agent success rate is low despite having access to all relevant information
- Agent's mental model, when reported, contradicts codebase reality

**Diagnostic questions**:
1. Is the documentation internally consistent?
2. Are codebase patterns uniform or mixed?
3. Are conventions documented or implicit?
4. Is context for unusual patterns explained?
5. Are tasks sized to complete within context limits?

**If the environment is orientation-hostile, more observation won't help.** The agent can read more files but will remain confused. The fix is environmental, not behavioral:
- Reconcile contradictory docs
- Document canonical patterns
- Explain unusual code
- Size tasks appropriately

### The Jamming Analogy

A pilot whose radar is being jammed cannot orient effectively. The observation data is noise. Increasing radar power doesn't help if the jamming is stronger. The pilot must either defeat the jamming or switch to alternative sensors.

An agent in an orientation-hostile codebase is being "jammed." The observation data (contradictory docs, inconsistent patterns) is noise. More observation doesn't help. The agent must either clarify the noise (ask humans to reconcile docs) or switch to alternative orientation (rely on examples rather than docs).

**Practical CLAUDE.md instruction for hostile environments**:
```markdown
# When Documentation Conflicts

This codebase has historical inconsistencies. If you find conflicting patterns:

1. Check the file's directory. New code (src/v2/) follows Pattern A. Legacy code (src/v1/) follows Pattern B.
2. For new code, always use Pattern A.
3. For legacy code, maintain existing pattern unless specifically asked to migrate.
4. If unclear, ask before proceeding.

# Source of Truth Hierarchy
1. CLAUDE.md (you're reading it)
2. New code in src/v2/
3. Tests (they show intended behavior)
4. README (may be outdated)
5. Legacy code (may not reflect current best practice)
```

---

## Part VIII: Incestuous Amplification

### Boyd's Warning

Boyd warned that orientation corrupts observation. We see what we expect to see. Evidence that confirms our model gets noticed; evidence that contradicts gets filtered out.

In military context: intelligence services that confirm leadership's existing beliefs, missing disconfirming evidence. The Iraq WMD failure is a canonical example.

### Manifestation in Agents

Agents are susceptible to the same bias:

**Pattern 1: Confirmatory search**
```
Agent hypothesizes: "Error handling in this codebase uses try/catch"
Agent searches: grep "try.*catch" --include="*.ts"
Agent finds: 47 matches
Agent concludes: "Error handling uses try/catch"

Reality: 90% of codebase uses Result types. Agent's search pattern found the exceptions.
```

**Pattern 2: First-match anchoring**
```
Agent reads first file. Observes Pattern X.
Agent reads second file. Observes Pattern X again.
Agent orients: "This codebase uses Pattern X"
Agent stops reading.

Reality: Files 3-20 use Pattern Y. Agent's sample was unrepresentative.
```

**Pattern 3: Interpretation filtering**
```
Agent has hypothesis H.
Agent observes evidence E that could support H or ~H.
Agent interprets E as supporting H.

Example: Agent sees function with both sync and async variants.
Agent hypothesis: "This codebase uses sync functions."
Agent interprets: "The async variant is legacy, sync is preferred."
Reality: Sync variant is legacy, async is preferred.
```

### Mitigation Strategies

**Require disconfirming evidence search**:
```markdown
# Confirmation Bias Check (in CLAUDE.md)

Before implementing any pattern:

1. Find 3+ examples of code that follows your planned pattern
2. Search for examples that CONTRADICT your planned pattern
3. If contradictions exist, investigate why before proceeding
   - Is your pattern actually wrong?
   - Is there a context that determines which pattern applies?
   - Is one pattern deprecated?
```

**Explicit hypothesis framing**:
```
Instead of: "The codebase uses X"
Frame as: "Hypothesis: The codebase uses X. Evidence: [files]. Counter-evidence needed."
```

**Devil's advocate search patterns**:
```
After: grep "async.*function" → finds async functions
Also: grep "function.*Promise" → finds promise-returning non-async functions
Also: grep "Result<" → finds Result type usage

Multiple search patterns reveal multiple patterns.
```

**Sample size requirements**:
```markdown
# Pattern Identification Requirements

To claim a pattern is canonical:
- Minimum 5 examples across different directories
- No more than 10% counter-examples
- Explicit check for contradicting patterns
- If pattern varies by context, document the context rule
```

### The Destruction-Creation Response

When incestuous amplification is detected (agent's confident implementation is wrong), the response is not "observe more" but "destroy model and rebuild."

**Destruction**: "My mental model said X. Reality showed Y. My mental model is wrong. What assumption led to X?"

**Creation**: "With assumption corrected, what mental model fits both original evidence and disconfirming evidence?"

This requires the agent to acknowledge model failure, which requires an environment where model failure is not punished. The organizational culture that punishes agent mistakes incentivizes agents to hide mistakes rather than learn from them.

---

## Part IX: Measurement and Validation

### The Orientation Measurement Problem

The fundamental challenge: **orientation is latent. You cannot directly observe an agent's mental model.** You can only observe actions that emerge from that model and infer orientation quality from action success.

This creates problems:
- By the time you know orientation was bad, the agent has already acted
- Good outcomes can occur from bad orientation (luck)
- Bad outcomes can occur from good orientation (noise)
- Correlation between orientation quality and outcome quality is imperfect

### Proposed Measurement Framework

**Phase-Level Metrics**:

| Phase | Direct Metrics | Proxy Metrics |
|-------|----------------|---------------|
| Observe | Files read, lines processed, search queries | Coverage of relevant files, redundancy rate |
| Orient | Pre-flight accuracy (costly) | Questions asked, contradictions noted, first-try success |
| Decide | Decision time, decision changes | Supervisor overrides, justification quality |
| Act | Lines changed, actions taken | Rollback frequency, test pass rate |

**System-Level Metrics**:

| Metric | Definition | Target |
|--------|------------|--------|
| IG&C Coverage | Actions via convention / Total actions | >80% for routine tasks |
| First-Try Success | Tasks completed without retry | >70% |
| Context Efficiency | Context used at completion / Context available | 60-80% |
| Orientation Accuracy | Pre-flight matches reality (sampled) | >90% |
| Coordination Overhead | Messages between agents / Tasks completed | Decreasing trend |

### Orientation Pre-Flight Protocol

For high-stakes or diagnostic purposes, require orientation report before action:

```
Agent orientation pre-flight:

1. TASK UNDERSTANDING
   - Stated goal: [goal as agent understands it]
   - Success criteria: [how agent will know it succeeded]
   - Constraints: [what agent understands it cannot do]

2. CONTEXT UNDERSTANDING
   - Relevant files: [files agent believes are relevant]
   - Patterns observed: [patterns agent identified]
   - Dependencies: [what depends on what]

3. APPROACH
   - Planned action: [what agent intends to do]
   - Rationale: [why this approach]
   - Risks: [what could go wrong]
   - Alternatives considered: [other approaches and why not chosen]

4. CONFIDENCE
   - Orientation confidence: [high/medium/low]
   - Sources of uncertainty: [what agent is unsure about]
```

Supervisor reviews and either:
- Validates (agent proceeds)
- Corrects (agent re-orients and resubmits)
- Escalates (human takes over)

This is expensive but provides direct orientation measurement and catches errors before costly action.

### Validation Through Failure Analysis

When agents fail, analyze OODA phase:

**Observation failure**: Agent didn't observe relevant information that was available
- Diagnosis: What information would have changed the outcome? Was it observable?
- Fix: Better search patterns, broader initial observation, observation checklists

**Orientation failure**: Agent observed information but built wrong mental model
- Diagnosis: What assumption was wrong? Where did it come from?
- Fix: Better documentation, explicit anti-patterns, confirmation bias checks

**Decision failure**: Agent was correctly oriented but chose wrong action
- Diagnosis: What options did agent consider? Why was wrong one chosen?
- Fix: Better decision criteria, clearer priorities, explicit tradeoffs

**Action failure**: Agent had correct decision but failed to execute
- Diagnosis: What went wrong in execution? Tool failure? Syntax error?
- Fix: Better tooling, validation steps, incremental action

Most failures are orientation failures. Tracking failure type distribution validates this claim and identifies improvement priorities.

---

## Part X: Design Patterns

### Pattern 1: Invest in Orientation Infrastructure

**Problem**: Agents spend cycles inferring patterns that could be documented.

**Solution**: Front-load orientation through comprehensive documentation.

```markdown
# CLAUDE.md Structure (Priority Ordered)

1. Architecture Overview
   - System components and their relationships
   - Data flow through the system
   - Key abstractions and their responsibilities

2. Conventions
   - Naming patterns
   - File organization
   - Import style
   - Error handling
   - Testing approach

3. Anti-Patterns
   - Patterns that look right but are wrong
   - Deprecated patterns still in codebase
   - Common mistakes and why they're wrong

4. Decision Criteria
   - When to use Pattern A vs Pattern B
   - Priority order when objectives conflict
   - Explicit tradeoffs

5. Common Tasks
   - Step-by-step for frequent operations
   - Examples of correct implementations
   - Expected outcomes for validation
```

**ROI**: Every hour writing documentation saves 10+ hours of agent re-orientation. Documentation compounds; orientation cost repeats every session.

### Pattern 2: Orientation Pre-Flight

**Problem**: Orientation failures discovered only after costly action.

**Solution**: Require orientation report before significant action.

```
Agent reports:
"I understand this task as: [summary]
I see the relevant patterns as: [patterns]
I plan to: [approach] because [reasoning]
I'll know I succeeded when: [success criteria]"

Supervisor validates or corrects before agent proceeds.
```

**Variants**:
- Full pre-flight for high-stakes tasks
- Sampled pre-flight for routine tasks (10% sample rate)
- Abbreviated pre-flight for time-sensitive tasks

**ROI**: Catch orientation errors before expensive actions. Enables trust calibration through direct measurement.

### Pattern 3: Systematic IG&C Development

**Problem**: Agents repeatedly make decisions that have consistent answers.

**Solution**: Track recurring decisions, convert to conventions.

```
1. Decision logging:
   - What decision was made?
   - What was the answer?
   - How many times has this decision occurred?

2. Threshold review (weekly):
   - Decisions occurring >10 times → Candidate for convention
   - Consistent answers → Document as convention
   - Inconsistent answers → Investigate why and document context rule

3. Convention embedding:
   - Add to CLAUDE.md as fact, not rule
   - "This codebase uses X" not "You should use X"
   - Include rationale for context

4. Validation:
   - Observe whether agents follow convention without deliberation
   - If still deciding, convention not embedded
   - Iterate on framing
```

**ROI**: Each decision converted to convention removes that decision from every future task. Cumulative improvement in task velocity.

### Pattern 4: Confirmation Bias Checks

**Problem**: Agents find confirming evidence, miss contradicting evidence.

**Solution**: Require explicit disconfirming evidence search.

```markdown
# In CLAUDE.md

## Before Implementing Any Pattern

1. Find 3+ examples of code following your planned pattern
2. Search for examples CONTRADICTING your planned pattern:
   - Grep for alternatives
   - Check different directories
   - Look at test files
3. If contradictions exist:
   - Investigate why (context-dependent? deprecated? legacy?)
   - Document your conclusion
   - Proceed only if confident in resolution
```

**ROI**: Prevents orientation lock-in. Catches pattern misidentification before implementation.

### Pattern 5: Task Sizing for Complete OODA Loops

**Problem**: Context resets break orientation mid-task.

**Solution**: Size tasks to complete full OODA loop with margin.

```
Task sizing checklist:

[ ] Clear scope - agent can identify required observation
[ ] Bounded observation - relevant files number <20
[ ] Context budget - estimated usage <80% of window
[ ] Complete action - implementation can finish without handoff
[ ] Observable outcome - success criteria are verifiable

If any check fails, break into smaller tasks.
```

**Task breakdown heuristic**:
```
Original: "Refactor the authentication system"

Too large. Break down:

1. "Audit current auth implementation and document findings"
2. "Design refactored auth structure"
3. "Implement new auth service"
4. "Migrate auth middleware to new service"
5. "Update auth tests for new implementation"
6. "Remove deprecated auth code"

Each task is a complete OODA loop.
```

**ROI**: Prevents context reset disruption. Enables incremental progress with validated checkpoints.

### Pattern 6: Shared Orientation for Multi-Agent (Einheit)

**Problem**: Multiple agents need coordination overhead to work together.

**Solution**: Develop shared orientation that enables implicit coordination.

```markdown
# Shared CLAUDE.md Sections

## Module Ownership
- auth/: Agent A primary, Agent B secondary
- api/: Agent B primary, Agent A secondary
- database/: Shared, require coordination

## Interface Contracts
- Auth exposes: authenticate(token), refreshToken(refresh)
- API expects: auth response in specific format
- Changes to interface require updating both sides

## Implicit Coordination Rules
- Touching auth.service.ts → also touch auth.test.ts
- Changing API response format → update consumer expectations
- Adding database migration → update seeds and docs

## Conflict Resolution
- Primary owner has final say on their module
- Shared modules: first to open PR has priority
- Unresolvable: escalate to human
```

**ROI**: Enables parallel agent operation without explicit coordination messages. Reduces coordination overhead to near-zero for well-defined work.

---

## Part XI: Failure Mode Taxonomy

### Observation Failures

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| Agent reads irrelevant files | Unfocused initial search | Better search patterns, scope constraints |
| Agent misses critical file | Incomplete search coverage | Observation checklists, dependency mapping |
| Agent re-reads same files | No observation caching | Session context management |
| Agent overwhelmed by results | Too broad search | Iterative narrowing, relevance filtering |

### Orientation Failures (Most Common)

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| "Can't decide what to do" | Orient hasn't generated options | Help re-orient, question assumptions |
| Keeps trying failed approach | Orient locked to wrong model | Force model destruction, fresh observation |
| Confident but wrong | Incestuous amplification | Disconfirming evidence requirement |
| Confused by contradictions | Orientation-hostile environment | Reconcile docs, document canonical |
| Follows wrong pattern | Shallow orientation | Deeper examples, architecture docs |
| Misses "why" behind code | No context documentation | ADRs, commit message discipline |

### Decision Failures (Usually Orientation Failures)

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| Analysis paralysis | No decision criteria | Explicit priorities in CLAUDE.md |
| Multi-objective confusion | Competing goals | Clear schwerpunkt |
| Chose wrong approach | Wrong option space | Fix orientation, not decision |
| Overthinking routine task | IG&C not developed | Convert to convention |

### Action Failures

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| Syntax errors | Tool/model issue | Better tooling, validation |
| Logical errors | Orient/Decide failure | Not action problem |
| Broke existing tests | Didn't run tests | IG&C: always run tests |
| Incomplete implementation | Task too large | Better task sizing |
| Wrong files modified | Misidentified scope | Better observation, orientation |

### Tempo Failures

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| Context reset mid-task | Task too large | Break into smaller tasks |
| Excessive overhead | Task too small | Batch related tasks |
| Inconsistent across tasks | Lost coherence | Better task sequencing |
| Repeated re-orientation | Unstable environment | Stabilize docs/code |

---

## Part XII: Cross-Model Synthesis Template

This analysis serves as a template for applying other mental models to agent architecture. The structure enables cross-cutting synthesis across multiple models.

### Template Structure

For each mental model:

**1. Model Overview**
- Origin and historical context
- Core principles and mechanisms
- Why it matters for coordination

**2. Translation Mapping**
- Human domain → Agent domain equivalents
- What translates directly
- What requires reconceptualization

**3. Bottleneck Identification**
- Where do agents struggle with this model's demands?
- What's the asymmetry compared to humans?
- Where is highest-leverage optimization?

**4. Optimization Patterns**
- Concrete design patterns
- CLAUDE.md templates
- Implementation checklists

**5. Measurement Framework**
- What to measure
- Direct vs proxy metrics
- Target values and thresholds

**6. Failure Taxonomy**
- Common failure modes
- Diagnostic indicators
- Remediation patterns

**7. Multi-Agent Implications**
- How model scales
- Coordination requirements
- Shared orientation needs

**8. Integration Points**
- How this model relates to others
- Complementary models
- Conflicting models

### Cross-Model Synthesis Process

When synthesizing insights across models:

**Step 1: Identify the problem**
- What coordination challenge are we addressing?
- What failure modes are we trying to prevent?

**Step 2: Collect perspectives**
- What does OODA say about this problem?
- What does Separation Assurance say?
- What does Jidoka say?
- [... for each relevant model]

**Step 3: Find agreements**
- What do all models agree on?
- What patterns are universal?

**Step 4: Analyze divergences**
- Where do models disagree?
- Why do they diverge?
- What context determines which applies?

**Step 5: Synthesize**
- Common principles (apply always)
- Context-dependent patterns (apply when X)
- Decision framework (how to choose)

**Step 6: Validate**
- Test synthesized patterns against known cases
- Identify edge cases
- Refine framework

### Example: Orientation Problem Across Models

| Model | Perspective on Orientation |
|-------|---------------------------|
| OODA | Orient is the bottleneck; invest in orientation infrastructure |
| Separation Assurance | Orientation is constraint on controllability; maintain recovery margin |
| Jidoka | Orientation failures should be surfaced immediately, not hidden |
| Shared Mental Models | Shared orientation enables implicit coordination |
| Recognition-Primed Decision | Experts orient through pattern matching, not deliberation |

**Synthesis**:
- All models agree orientation is critical
- Orientation failures should be visible (Jidoka, OODA)
- Orientation should be shared (Einheit, Shared Mental Models)
- Orientation can be accelerated through patterns (IG&C, RPD)
- Orientation quality determines action quality (all models)

**Framework**:
1. Invest in orientation infrastructure (documentation, conventions)
2. Surface orientation failures immediately (pre-flight validation)
3. Share orientation across agents (common CLAUDE.md)
4. Develop pattern recognition (IG&C through examples)
5. Maintain orientation margin (don't overcommit to uncertain models)

---

## Part XIII: Concrete Implementation Examples

### Example 1: Orientation Pre-Flight in CLAUDE.md

```markdown
# Orientation Protocol

## Before Any Significant Change

Report your orientation before proceeding:

### 1. Problem Understanding
What problem are you solving? State it in your own words.
What would success look like?

### 2. Codebase Understanding
What files are relevant? (List them)
What patterns do they follow?
What dependencies exist?

### 3. Approach Selection
What approach will you take?
What alternatives did you consider?
Why is your chosen approach better?

### 4. Risk Assessment
What could go wrong?
How would you detect if something went wrong?
What's your rollback plan?

## Wait for validation before proceeding with implementation.
```

### Example 2: Confirmation Bias Check Implementation

```markdown
# Pattern Identification Protocol

## When identifying a codebase pattern:

### Step 1: Initial Hypothesis
After reading initial files, state your hypothesis:
"I believe this codebase uses [pattern] for [situation]."

### Step 2: Confirming Evidence (minimum 3)
Find 3+ examples that support your hypothesis:
- Example 1: [file:line] - [description]
- Example 2: [file:line] - [description]
- Example 3: [file:line] - [description]

### Step 3: Disconfirming Search
Search for counter-examples:
- Alternative pattern grep: [pattern]
- Different directory check: [directory]
- Test file check: [test files]

### Step 4: Reconciliation
If counter-examples exist:
- Are they deprecated? How do you know?
- Are they context-specific? What context?
- Are they exceptions? Why?

### Step 5: Conclusion
State your final conclusion with confidence level:
- High: 5+ confirming, 0 counter-examples
- Medium: 3+ confirming, <20% counter-examples with explanation
- Low: Counter-examples exist without clear explanation

If Low, ask before proceeding.
```

### Example 3: Task Sizing Checklist

```markdown
# Task Sizing Checklist

## Before Starting Task

[ ] SCOPE: Can I identify all files that need to change?
    - If >20 files, consider breaking down

[ ] OBSERVATION: Can I read all relevant files?
    - List the files
    - If >15 files, consider breaking down

[ ] CONTEXT: Will this fit in context window?
    - Estimate: Files + CLAUDE.md + reasoning + output
    - If >80% of context, consider breaking down

[ ] COMPLETION: Can I finish without handing off?
    - If task requires multiple sessions, break down

[ ] VALIDATION: Can I verify success?
    - What tests validate this?
    - What does "done" look like?

## Breaking Down Large Tasks

Original task: [task]

Breakdown approach:
1. Observation/understanding phase as separate task
2. Design/planning phase as separate task
3. Implementation phases by component
4. Testing/validation as separate task
5. Cleanup/documentation as final task

Each sub-task should pass the checklist above.
```

### Example 4: IG&C Development Tracker

```markdown
# Decision Log

## Format
[Date] [Task] [Decision] [Answer] [Recurring?]

## Entries
2024-01-15 auth-fix "Should I run tests?" YES 47th occurrence
2024-01-15 api-update "Which import style?" Absolute from @/ 23rd occurrence
2024-01-16 model-add "Where do types go?" types/ directory 31st occurrence
2024-01-16 test-fix "Use describe or test?" describe() for groups 12th occurrence

## Convention Candidates (>10 occurrences)
- "Always run tests" (47x) → ADDED TO CLAUDE.md
- "Absolute imports from @/" (23x) → ADDED TO CLAUDE.md
- "Types in types/ directory" (31x) → ADDED TO CLAUDE.md
- "describe() for test groups" (12x) → CANDIDATE, review next week

## Review Process (Weekly)
1. Identify decisions >10 occurrences
2. Check answer consistency (>90% same answer)
3. If consistent, add to CLAUDE.md as fact
4. If inconsistent, document context rule
5. Monitor for IG&C activation (decisions decrease)
```

### Example 5: Multi-Agent Coordination via Shared Orientation

```markdown
# Multi-Agent Coordination Protocol

## Module Ownership Map
| Module | Primary | Secondary | Shared |
|--------|---------|-----------|--------|
| auth/ | Agent A | Agent B | - |
| api/ | Agent B | Agent A | - |
| database/ | - | - | Yes |
| config/ | - | - | Yes |

## Implicit Coordination Rules

### File Touch Rules
- Touching X → must also touch Y
- auth.service.ts → auth.test.ts
- api/routes.ts → api/routes.test.ts
- database/schema.ts → database/migrations/, database/seeds/

### Cross-Module Changes
If changing interface between modules:
1. Primary of providing module makes change
2. Primary of consuming module updates consumption
3. No coordination message needed if interface is documented

### Shared Module Protocol
1. First agent to claim work on shared module "owns" it for that task
2. Claim by creating a branch or noting in status
3. Other agents wait or work on non-conflicting areas
4. If conflict, escalate to human

## Conflict Resolution
1. Check if conflict is real (maybe different files)
2. Check module ownership (primary owner decides)
3. Check claim time (first claimer wins on shared)
4. If unresolvable, stop and escalate

## Status Visibility
Each agent maintains status:
- Currently working on: [file/module]
- Blocked on: [dependency if any]
- Available for: [what agent can pick up]
```

---

## Part XIV: Open Questions for Future Research

### Orientation Measurement

1. **Can orientation quality be measured before action?** Current approach is indirect (observe action outcomes). Direct measurement (pre-flight validation) is expensive. Is there a cheap, accurate proxy?

2. **How do you measure orientation accuracy at scale?** Sampling works but misses systematic biases. What's the minimum sample rate for reliable estimation?

3. **Can agents self-assess orientation quality?** LLMs often exhibit high confidence even when wrong. Can calibration techniques improve self-assessment?

### IG&C Development

4. **What's the optimal pace of IG&C development?** Adding conventions too fast may encode errors. Adding too slow wastes decision cycles. What's the right threshold?

5. **How do you detect when IG&C should be destroyed?** Codebases change. Conventions that were correct become incorrect. How do you detect stale IG&C?

6. **Can IG&C development be automated?** Currently requires human judgment to convert decisions to conventions. Can patterns be detected and proposed automatically?

### Multi-Agent Coordination

7. **What's the scaling limit of Einheit-based coordination?** Shared orientation works for small numbers of agents. At what scale does explicit coordination become necessary?

8. **How do you maintain orientation consistency across agents?** If agents have slightly different CLAUDE.md interpretations, Einheit breaks down. How do you ensure consistency?

9. **What's the interaction between agent OODA loops?** Does one agent's action disrupt another's orientation? How do you manage this?

### Environment Optimization

10. **What's the minimum viable orientation infrastructure?** How much documentation is enough? Diminishing returns at what point?

11. **How do you prioritize documentation investments?** Which areas benefit most from orientation infrastructure? How do you identify them?

12. **Can orientation-hostile conditions be automatically detected?** Is there a metric that signals "this codebase is confusing agents" before specific failures occur?

### Cross-Model Integration

13. **When do different mental models conflict?** OODA emphasizes speed; Jidoka emphasizes stopping. How do you reconcile these in agent design?

14. **Can model selection be automated?** Given a problem, which mental models apply? Can agents select appropriate models for their situation?

15. **What's the meta-framework that unifies all models?** Is there a higher-level framework that explains when each model applies?

---

## Part XV: Implementation Roadmap

### Phase 1: Foundations (Weeks 1-2)

**Orientation Infrastructure**
- [ ] Audit current CLAUDE.md completeness
- [ ] Document missing conventions
- [ ] Add anti-patterns section
- [ ] Create architecture overview

**Measurement Setup**
- [ ] Implement first-try success tracking
- [ ] Create decision logging
- [ ] Set up context usage monitoring

### Phase 2: Validation (Weeks 3-4)

**Orientation Pre-Flight**
- [ ] Design pre-flight protocol
- [ ] Implement for high-stakes tasks
- [ ] Begin collecting accuracy data

**Confirmation Bias Checks**
- [ ] Add to CLAUDE.md
- [ ] Validate agents follow protocol
- [ ] Measure impact on success rate

### Phase 3: IG&C Development (Weeks 5-6)

**Decision Tracking**
- [ ] Implement decision log
- [ ] Set up weekly review process
- [ ] Convert first batch of decisions to conventions

**IG&C Monitoring**
- [ ] Track convention adherence
- [ ] Measure decision rate trends
- [ ] Identify candidates for next conversion

### Phase 4: Multi-Agent (Weeks 7-8)

**Einheit Infrastructure**
- [ ] Define module ownership
- [ ] Document implicit coordination rules
- [ ] Create conflict resolution protocol

**Validation**
- [ ] Test with 2 agents on shared codebase
- [ ] Measure coordination overhead
- [ ] Identify Einheit gaps

### Phase 5: Optimization (Ongoing)

**Continuous Improvement**
- [ ] Monthly orientation infrastructure review
- [ ] Weekly IG&C expansion
- [ ] Quarterly failure analysis

**Metrics Dashboards**
- [ ] First-try success rate trend
- [ ] IG&C coverage trend
- [ ] Context efficiency trend

---

## Sources

### Primary Boyd Sources
- Boyd, John. "Destruction and Creation" (1976) - Epistemological foundation
- Boyd, John. "Patterns of Conflict" (1986) - OODA loop presentation
- Boyd, John. "Organic Design for Command and Control" (1987) - Four organizational qualities
- Boyd, John. "The Strategic Game of ? and ?" (1987) - Competition and tempo

### Secondary Analysis
- Richards, Chet. "Certain to Win: The Strategy of John Boyd Applied to Business" (2004)
- Osinga, Frans. "Science, Strategy and War: The Strategic Theory of John Boyd" (2007)
- Coram, Robert. "Boyd: The Fighter Pilot Who Changed the Art of War" (2002)
- Hammond, Grant. "The Mind of War: John Boyd and American Security" (2001)

### Agent Systems Context
- Internal research documents in this repository
- Cross-model synthesis with Separation Assurance, Jidoka, Shared Mental Models

---

## Document Status

**Version:** 2.0 (Opus-level rewrite)
**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Date:** 2026-01-20
**Purpose:** Agent architecture analysis template for cross-model synthesis
**Status:** Deep architectural analysis complete

**Changes from v1.0:**
- Expanded theoretical foundations with Boyd's actual framework
- Added systematic failure mode analysis
- Developed concrete measurement framework
- Created actionable implementation patterns
- Structured for cross-model synthesis
- Added implementation roadmap

**Next Steps:**
- Apply this template to remaining Priority 1 models
- Use for cross-model synthesis in Phase 2
- Validate patterns through implementation
