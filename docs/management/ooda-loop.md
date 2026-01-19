# Boyd's OODA Loop

Exploring how the OODA Loop applies to AI agent task execution and supervision.

## Human Practice

| Aspect | Description |
|--------|-------------|
| **Origin** | USAF Colonel John Boyd, 1950s-1970s |
| **Cycle** | Observe, Orient, Decide, Act |
| **Core Insight** | Getting inside the opponent's decision cycle creates advantage |
| **Key Emphasis** | Agility and tempo beat raw speed or power |

The OODA Loop emerged from Boyd's analysis of why F-86 pilots achieved 10:1 kill ratios against technically superior MiG-15s in Korea. The answer was not aircraft superiority but pilot agility - the ability to cycle through decisions faster than opponents.

Boyd emphasized that **Orient is the schwerpunkt (focal point)** of the loop. It's where mental models live, and it shapes how everything else works. Observation is filtered through orientation; decisions emerge from orientation; actions test orientation.

### Correction: Not Actually a Loop

Boyd's actual diagram is not a simple loop. It's **multiple feedback paths with Orient at the center:**

```
                    ┌─────────────────────────────────────────┐
                    │                                         │
                    v                                         │
              ┌──────────┐     ┌──────────┐     ┌──────────┐ │
Observation ──│  ORIENT  │────>│  DECIDE  │────>│   ACT    │─┘
     ^        └──────────┘     └──────────┘     └──────────┘
     │              │                                 │
     │              │         (IG&C)                  │
     │              └────────────────────────────────>│
     │                                                │
     └────────────────────────────────────────────────┘
```

Key insight: There's a **direct path from Orient to Act** that bypasses Decide entirely. Boyd called this Implicit Guidance and Control (IG&C).

**Agent application:** Agents don't progress linearly through phases. They oscillate, skip back, sometimes act directly from orientation without explicit decision. The goal is to develop orientation so good that IG&C handles most situations.

## Initial Translation: Task Execution Cycle

The obvious mapping:

| OODA Phase | Agent Activity |
|------------|----------------|
| Observe | Read files, grep codebase, examine context |
| Orient | Parse CLAUDE.md, understand task requirements, build mental model |
| Decide | Plan implementation approach |
| Act | Write code, make changes |

This is accurate but shallow. Every agent already does this. The interesting questions are: Where do agents get stuck? What would a "faster OODA loop" mean? What is "getting inside the opponent's loop" for an agent?

## Destruction and Creation: Boyd's Epistemology

Boyd's unpublished paper "Destruction and Creation" describes how mental models are built:

1. **Destructive Deduction:** Take apart existing mental models, break them into components
2. **Creative Induction:** Reassemble components into new patterns that better match reality

This isn't passive learning. It's **active destruction of inadequate models** followed by reconstruction.

**Agent application:** Orientation isn't accumulating information - it's actively destroying and rebuilding mental models. An agent that reads 50 files but never questions its assumptions has not oriented. An agent that reads 5 files and realizes "wait, my assumption about the architecture is wrong" has oriented better.

| Orientation Failure | What's Missing |
|--------------------|----------------|
| Read many files, same conclusion | No destruction - confirming existing model |
| Keep trying same approach | No creation - not synthesizing new pattern |
| "I understand" then wrong action | Shallow orientation - no integration |

**Practical implication:** Good orientation requires finding information that **contradicts** current understanding, not just confirms it.

## The Five Elements of Orientation

Boyd identified five inputs that shape orientation:

| Element | Human Context | Agent Equivalent |
|---------|---------------|------------------|
| **Genetic Heritage** | Innate cognitive patterns | Model training, base capabilities |
| **Cultural Traditions** | Learned social patterns | CLAUDE.md, project conventions |
| **Previous Experiences** | Personal history | Session context, prior tool outputs |
| **New Information** | Current sensory input | Current observation (grep, file reads) |
| **Analysis/Synthesis** | The destruction/creation engine | Processing that builds mental model |

**Agent insight:** Four of these are inputs. Only one (Analysis/Synthesis) is the actual process. Most agent optimization focuses on inputs (better CLAUDE.md, more context). Little focuses on improving the synthesis process itself.

### Cultural Traditions as Orientation Shortcut

CLAUDE.md is the agent's cultural tradition. Well-developed culture lets agents skip expensive orientation:

| Without CLAUDE.md | With CLAUDE.md |
|-------------------|----------------|
| Read code, infer patterns | Patterns pre-documented |
| Guess conventions | Conventions explicit |
| Orient from scratch | Orient from baseline |

**Goal state:** CLAUDE.md so complete that IG&C (Orient→Act) handles most routine tasks. The agent doesn't "decide" - it just knows from orientation.

## Implicit Guidance and Control (IG&C)

The fast path that bypasses Decide entirely: Orient → Act.

Boyd observed that experienced pilots don't consciously decide in combat. They act from orientation. The decision is implicit in the situation recognition.

**Agent application:**

| Explicit Decision (slow) | Implicit Guidance (fast) |
|-------------------------|-------------------------|
| "Should I run the build?" | CLAUDE.md says always build |
| "What naming convention?" | Conventions documented, just apply |
| "How to handle this error?" | Error handling pattern in examples |

**Well-documented conventions let agents skip "deciding."** Every decision that becomes convention is a decision removed from the critical path.

**Goal for agent systems:** Eliminate the Orient→Decide step for routine situations. Reserve explicit decision-making for genuinely novel situations.

## Orient as the Bottleneck

Boyd called Orient the most important phase because it's where mental models exist. For agents, this translates to:

**Agent orientation consists of:**
- CLAUDE.md and project instructions (cultural traditions)
- Codebase patterns already observed (past experiences)
- Language model training (genetic inheritance)
- Current task context (new information)
- Synthesis of the above (analysis/synthesis)

### Key Insight: Agents Can Observe Faster Than They Can Orient

Agents can grep a codebase in milliseconds. They can read 20 files in parallel. Observation is essentially instant.

But **orientation is where agents struggle:**
- Conflicting patterns in codebase (which is canonical?)
- Ambiguous instructions (what did the human actually mean?)
- Missing context (why does this weird pattern exist?)
- Outdated mental models (assuming patterns that changed)

**The agent OODA bottleneck is Orient, not Observe.**

This explains a common failure mode: agents that grep extensively, read many files, then make changes that miss the point. They observed plenty but failed to orient correctly.

### Orient Generates Options

Only the Orient phase creates new possibilities. Observe just gathers data. Decide selects from available options. Act executes.

**A stuck agent is almost always an orientation problem, not a decision problem.**

| Symptom | Misdiagnosis | Actual Problem |
|---------|--------------|----------------|
| "Can't decide what to do" | Decision paralysis | Orient hasn't generated options |
| "Tried everything, nothing works" | Bad luck | Orient generated wrong option space |
| "Keeps making same mistake" | Execution failure | Orient locked into wrong model |

**Agent application:** When an agent is stuck, don't give it more observations (files to read). Help it re-orient (question assumptions, reframe problem).

### Implication: Invest in Orientation Infrastructure

| Investment | Effect on Agent OODA |
|------------|---------------------|
| Comprehensive CLAUDE.md | Pre-loads orientation, reduces cycle time |
| Naming conventions doc | Reduces orientation ambiguity |
| Architecture decision records | Explains "why", accelerates orientation |
| Examples of good changes | Calibrates mental models |

Poor documentation forces agents to spend cycles orienting from raw observation. Good documentation front-loads orientation.

## Incestuous Amplification

Boyd warned that **orientation corrupts observation**. We see what we expect to see. Evidence that fits our model gets noticed; evidence that contradicts gets filtered out.

In military context: intelligence services that confirm leadership's existing beliefs, missing disconfirming evidence.

**Agent manifestation:**

| Behavior | What's Happening |
|----------|------------------|
| Grep finds "confirming" patterns | Stopped searching after first match |
| "The codebase does X" | Based on 3 files, 50 contradict |
| Implements wrong approach confidently | Oriented wrong, filtered observations to fit |

**Mitigation: Search for what would prove me wrong.**

```
Before: "Find examples of how errors are handled"
After: "Find examples that contradict my error handling assumption"
```

**Practical agent instruction:**

```markdown
## Confirmation Bias Check

Before implementing, actively search for:
- Code that does it differently than you planned
- Comments explaining why the obvious approach doesn't work
- Tests that would fail with your approach
```

## Tempo vs. Speed

Boyd distinguished tempo (rhythm, cadence) from raw speed. The goal isn't to move fast - it's to control the rhythm of engagement.

### Variety and Rapidity

Boyd required both for adaptability:
- **Variety:** Range of options available
- **Rapidity:** Speed of cycling through options

| Combination | Result |
|-------------|--------|
| Variety + Rapidity | Adaptive, hard to predict |
| Variety, no rapidity | Has options but too slow to use them |
| Rapidity, no variety | Fast but predictable |
| Neither | Static, easily outmaneuvered |

**Agent application:** Variety without orientation = random thrashing. An agent that tries many things quickly but without updating its model is just generating noise.

Rapidity without variety = tunnel vision. An agent that acts fast but only considers one approach gets stuck on hard problems.

### Task Granularity as Tempo

For agents, tempo translates to understanding **task granularity:**

| Approach | Tempo Characteristic |
|----------|---------------------|
| One huge task | Single slow loop - fragile, no recovery from mis-orientation |
| Many tiny tasks | Rapid loops - but overhead dominates, loses coherence |
| Right-sized tasks | Sustainable tempo - complete loops, ability to re-orient |

**The "autocompact problem" is a tempo problem.** When context resets mid-task, the agent loses orientation and must rebuild from observation. This is like a fighter pilot blacking out mid-engagement.

**Task boundaries should align with complete OODA loops.** A task should:
1. Start with sufficient context to orient
2. Allow full observation of what's needed
3. Reach a decision
4. Complete the action
5. Produce output that enables the next loop

Breaking a task mid-loop (via autocompact) destroys tempo.

## Four Organizational Qualities

Boyd identified four qualities that enable effective organizations:

| Quality | Military Context | Agent Application |
|---------|------------------|-------------------|
| **Fingerspitzengefuhl** | Intuitive feel, trained instinct | Pattern exposure through examples; agent "knows" from training |
| **Einheit** | Mutual trust, shared understanding | CLAUDE.md as shared mental model; conventions eliminate coordination |
| **Schwerpunkt** | Focus of effort, main point | Clear task objectives; single priority, not competing goals |
| **Auftragstaktik** | Mission-type orders | Supervisor provides intent, agent figures out execution |

### Auftragstaktik: Intent-Based Delegation

Traditional orders: "Move to grid reference X, set up position Y, engage at time Z."

Auftragstaktik: "Prevent enemy from crossing the river. Use your judgment."

**Agent application:**

| Command Style | Example | Result |
|---------------|---------|--------|
| Micromanagement | "Edit line 47, change X to Y" | Agent executes literally, misses related issues |
| Intent-based | "Fix the race condition in the audio handler" | Agent understands goal, finds best approach |

**Good task descriptions give intent, not procedure.** The agent has better visibility into the codebase than the supervisor. Let it orient and decide.

### Einheit: Why Centralization Fails

Boyd argued that centralized command creates bottlenecks. The central node must process all information and make all decisions. It becomes overwhelmed.

**Alternative: Shared orientation enables implicit coordination.** If everyone has the same mental model, they can act independently without coordination overhead.

**Agent application for multi-agent systems:**

| Architecture | Problem |
|--------------|---------|
| Central orchestrator decides everything | Bottleneck, single point of failure, no parallelism |
| Agents share orientation (same CLAUDE.md) | Implicit coordination, can work in parallel |

**Einheit is why CLAUDE.md matters more than orchestration logic.** Agents with shared orientation coordinate implicitly.

## Getting Inside the Problem's Loop

Boyd's famous concept is "getting inside the opponent's OODA loop" - acting in ways that disrupt the opponent's ability to orient.

For agents, there's no adversary. But there's an analogous concept: **getting inside the problem's loop.**

A complex codebase "pushes back" against changes:
- Dependencies create cascading requirements
- Hidden coupling creates unexpected failures
- Technical debt creates friction

An agent that can **anticipate the problem's reactions** operates effectively:

| Approach | OODA Analogy |
|----------|--------------|
| Make change, hit error, fix, repeat | Reactive - outside the problem's loop |
| Grep for dependencies first, make coordinated changes | Proactive - inside the problem's loop |
| Understand the architecture, predict side effects | Dominant - controlling tempo |

**Agents get "inside the problem's loop" through better orientation:**
- Understanding dependency patterns
- Knowing which files couple
- Anticipating build failures before they happen

An agent that makes one coordinated change beats an agent that makes five reactive fixes.

## Disruption and Uncertainty

Boyd noted that disrupting opponent orientation creates confusion. In combat, this means feints, unpredictability, overwhelming with stimuli.

For agent supervision, this translates to **orientation-hostile patterns:**

| Pattern | Effect on Agent OODA |
|---------|---------------------|
| Contradictory CLAUDE.md sections | Orientation conflict, decision paralysis |
| Inconsistent codebase patterns | Multiple competing mental models |
| Undocumented conventions | Forced to guess, high error rate |
| Frequent context resets | Orientation never stabilizes |

**An agent working on a chaotic codebase with poor docs is like a pilot being jammed.** The observation data is noise, orientation never converges, decisions become random.

This suggests a **"hostile OODA" diagnostic:** If an agent keeps making wrong decisions despite access to information, check whether the information is orientation-compatible or orientation-hostile.

## Where Agents Beat Humans

Boyd's insight was that F-86 cockpit visibility let pilots observe and orient faster than MiG pilots with poor visibility. Superior observation-orientation capability beat superior aircraft.

**Where do agents have superior OODA capability?**

| Phase | Agent Advantage | Agent Disadvantage |
|-------|-----------------|-------------------|
| Observe | Parallel file reads, instant grep, tireless | No physical world access, limited tool set |
| Orient | Consistent application of documented patterns | Struggles with undocumented/implicit knowledge |
| Decide | No ego, no sunk cost bias, no fatigue | Can't evaluate "taste", aesthetics, user experience |
| Act | Perfect syntax, no typos, fast execution | Limited to text-based actions |

**Agents have faster OODA loops for well-documented, pattern-following tasks.**

For tasks where orientation requires human judgment, implicit knowledge, or real-world feedback, human OODA loops are faster because humans can orient on information agents can't access.

## Summary: OODA Loop - Agent Equivalent

| OODA Concept | Human Context | Agent Equivalent |
|--------------|---------------|------------------|
| Observe | Gather information from environment | Read files, grep, explore codebase |
| Orient | Build mental model from experience + culture + observation | Parse CLAUDE.md + codebase patterns + task context |
| Decide | Select action based on mental model | Plan implementation approach |
| Act | Execute and observe results | Write code, run builds, test |
| IG&C (Orient→Act) | Trained instinct bypasses conscious decision | Conventions so clear that agent "just knows" |
| Tempo | Rhythm and cadence of engagement | Task granularity and completion rate |
| Getting inside opponent's loop | Disrupt their orientation | Anticipate problem's dependencies/side effects |
| Schwerpunkt (Orient) | Where mental models live | Quality of CLAUDE.md + codebase documentation |
| Loop disruption | Jamming, feints, overwhelming | Contradictory docs, inconsistent patterns |
| Destruction/Creation | Active model rebuilding | Question assumptions, synthesize new understanding |
| Incestuous amplification | Seeing what you expect | Grep for confirming evidence, miss contradictions |
| Fingerspitzengefuhl | Trained intuition | Pattern exposure in training/examples |
| Einheit | Shared understanding | Common CLAUDE.md enables implicit coordination |
| Auftragstaktik | Intent-based delegation | Give goal, let agent figure out execution |

## Open Questions

1. **Measuring orientation quality:** How do you know if an agent has oriented correctly before it acts? Current approach: let it act, observe failures, correct.

2. **Orientation pre-loading:** Could agents do orientation passes before the human gives a task? Build the mental model proactively?

3. **Orientation drift:** As codebases change, agent mental models become stale. How to detect when re-orientation is needed?

4. **Multi-agent tempo:** If multiple agents work a codebase, how do their OODA loops interact? Does one agent's action disrupt another's orientation?

5. **Optimal task size:** What's the relationship between task size and OODA loop efficiency? Too small = overhead dominates. Too large = can't complete loop before context reset.

6. **Orient-heavy tasks:** Some tasks are mostly orientation (understanding legacy code) with minimal action. Current tools optimize for action. Should there be orientation-specialized tools?

7. **IG&C development:** How do you systematically develop conventions until IG&C handles most cases? What's the path from "agent must decide" to "agent just knows"?

8. **Incestuous amplification mitigation:** How do you force agents to seek disconfirming evidence without making every task twice as long?

9. **Einheit without rigidity:** How do you maintain shared orientation across agents while still allowing local adaptation?

## Systems to Build

- [ ] **Orientation pre-flight:** Task decomposition step where agent reports its orientation before acting ("Here's what I understand about this codebase section")
- [ ] **Codebase orientation index:** Pre-computed summaries that accelerate agent orientation (not just file paths, but architectural understanding)
- [ ] **OODA loop tracing:** Log which files agent observed, how it oriented, what it decided, what it acted on - for post-hoc analysis of failures
- [ ] **Task sizing heuristics:** Rules for breaking tasks to ensure complete OODA loops within context windows
- [ ] **Orientation consistency checker:** Tool that detects contradictory patterns in CLAUDE.md or codebase (orientation-hostile conditions)
- [ ] **Confirmation bias checker:** Prompt that forces agent to search for contradicting evidence before implementing
- [ ] **IG&C development tracker:** Log decisions that should become conventions; track which decisions repeat
- [ ] **Einheit validator:** Check that multiple CLAUDE.md files across repos maintain compatible orientation

## Sources

- Boyd, John. "Destruction and Creation" (1976) - Epistemological foundation
- Boyd, John. "Patterns of Conflict" (1986) - OODA loop presentation
- Boyd, John. "Organic Design for Command and Control" (1987) - Four organizational qualities
- Richards, Chet. "Certain to Win" (2004) - Boyd's ideas applied to business
- Osinga, Frans. "Science, Strategy and War: The Strategic Theory of John Boyd" (2007) - Academic analysis of Boyd's work

## Status

**Phase:** Deep analysis integrated. Key insights: Orient generates options (stuck = orientation problem), IG&C is the goal state, incestuous amplification is a real agent failure mode, Einheit explains why shared CLAUDE.md matters more than orchestration.

**Next:** Build the confirmation bias checker and IG&C development tracker.
