# Recognition-Primed Decision Making (RPD)

Exploring how Gary Klein's Recognition-Primed Decision model applies to AI agent supervision and the development of agent expertise.

## The Framework

| Aspect | Description |
|--------|-------------|
| **Creator** | Gary Klein (cognitive psychologist), 1980s-1990s |
| **Domain** | Naturalistic decision making, expertise studies |
| **Core Finding** | Experts don't compare options - they recognize situations and act |
| **Research Base** | Fireground commanders, military officers, NICU nurses, chess masters |
| **Key Insight** | Experience builds patterns; patterns enable rapid, effective action |

## Background: How Experts Actually Decide

Klein's research challenged the classical model of decision making (identify options, compare them, select optimal). Studying experts under time pressure, he found something different:

**Classical Model (rarely used by experts):**
```
[Situation] --> [Generate Options] --> [Compare Options] --> [Select Best] --> [Act]
```

**What Experts Actually Do (RPD):**
```
[Situation] --> [Pattern Recognition] --> [Mental Simulation] --> [Act]
                      |                          |
                 "I've seen this"          "Will it work?"
```

Experts don't generate multiple options and compare. They recognize the situation type, retrieve a typical response, mentally simulate whether it will work, and act. If the simulation reveals problems, they adapt the response or (rarely) consider alternatives.

### The Fireground Commander Study

Klein's seminal research studied fireground commanders making life-or-death decisions under time pressure:

| Finding | Implication |
|---------|-------------|
| 80% of decisions used RPD | Experts rarely compare options |
| Average decision time: seconds | Pattern matching is fast |
| First option usually worked | Experience generates good defaults |
| Comparison only when unfamiliar | Novel situations require different process |

The commanders weren't making "optimal" decisions through analysis. They were recognizing situations, retrieving appropriate responses, and adapting them to specifics.

## The RPD Model: Three Variations

Klein identified three variations of increasing complexity:

### Variation 1: Simple Match

```
[Recognize Situation] --> [Know What To Do] --> [Act]
```

The situation is familiar. The response is obvious. No deliberation needed.

**Example:** Experienced firefighter sees specific smoke pattern, immediately knows it's a basement fire, knows the standard approach.

### Variation 2: Diagnose the Situation

```
[Ambiguous Cues] --> [Build Story] --> [Recognize Situation Type] --> [Act]
```

The situation isn't immediately clear. The expert gathers more information, constructs a coherent story, then recognizes the pattern.

**Example:** Fireground commander sees unusual fire behavior, gathers more cues, realizes "this is a flashover about to happen," orders immediate evacuation.

### Variation 3: Evaluate Course of Action

```
[Recognize Situation] --> [Typical Response] --> [Mental Simulation] --> [Works?]
                                                        |                    |
                                                   [Imagine it]         Yes --> Act
                                                                        No --> Adapt/Consider Alternative
```

The expert recognizes the situation and retrieves a typical response, but the response needs validation. Mental simulation runs the action forward to check for problems.

**Example:** Commander knows the standard approach but mentally simulates it and realizes "wait, the building structure won't support that entry point." Adapts the plan.

## The Four Components of RPD

### 1. Cues

What the expert notices in the environment. Experts notice different things than novices.

| Expert | Notices |
|--------|---------|
| **Chess master** | Piece relationships, attack patterns |
| **Firefighter** | Smoke color, flame behavior, building sounds |
| **Nurse** | Subtle vital sign changes, patient color |
| **Developer** | Code structure patterns, naming conventions |

**Key insight:** Experts have learned what to pay attention to. They filter signal from noise automatically.

### 2. Expectancies

What the expert expects to happen given the recognized pattern. If reality violates expectations, the expert knows something is wrong.

```
[Pattern Recognized] --> [Generates Expectancies]
                               |
                         "If this is X, I should see Y"
                               |
                         [Reality Check]
                               |
                    Matches --> Confidence
                    Doesn't Match --> Reassess Pattern
```

**Example:** Firefighter recognizes a standard kitchen fire. Expects fire confined to kitchen. Discovers fire spreading faster than expected. Realizes initial assessment was wrong.

### 3. Relevant Goals

What matters in this situation type. Pattern recognition activates appropriate goals.

| Situation | Primary Goals (in order) |
|-----------|-------------------------|
| **House fire** | Life safety, property preservation, firefighter safety |
| **Production outage** | Restore service, prevent data loss, root cause |
| **Security breach** | Contain damage, preserve evidence, restore security |

**Key insight:** The recognized pattern determines which goals are active. Experts don't decide what to optimize for; the situation type tells them.

### 4. Typical Actions

What to do in this situation type. Retrieved automatically when pattern is recognized.

**The response isn't optimal - it's satisfactory and fast.** Experts don't search for the best response. They retrieve a typical response that has worked before.

Klein calls this "satisficing" (Simon): finding a good-enough solution quickly rather than searching for the optimal one slowly.

## Mental Simulation: The Validation Step

Before acting, experts mentally simulate the action:

```
[Proposed Action] --> [Mental Walkthrough]
                            |
                      "Imagine doing this..."
                            |
                      "What happens next?"
                            |
                      "Any problems?"
                            |
                     [Problems Found?]
                            |
                    No --> Proceed
                    Yes --> Modify or Reconsider
```

### What Mental Simulation Does

| Function | How It Works |
|----------|--------------|
| **Spot flaws** | "This won't work because..." |
| **Identify prerequisites** | "I need to do X first" |
| **Predict side effects** | "This will also cause Y" |
| **Build confidence** | "Yes, this should work" |

### Mental Simulation Limitations

Mental simulation is powerful but bounded:

- **Can only simulate what you've experienced:** Novel failure modes are invisible
- **Limited working memory:** Can only track a few variables
- **Confirmation bias:** May simulate success path, miss failure paths
- **Time constraints:** Under pressure, simulation is truncated

---

## Agent Translation

### The Core Mapping

| RPD Component | Agent Equivalent |
|---------------|------------------|
| **Pattern recognition** | CLAUDE.md + training + codebase patterns |
| **Mental simulation** | Reasoning about approach before acting |
| **Expectancies** | Predictions about what should happen |
| **Typical actions** | Standard approaches for recognized situations |
| **Cue recognition** | What the agent notices in codebase/context |

### Do Agents Use RPD?

Current AI agents show RPD-like behavior:

| RPD Element | Agent Evidence |
|-------------|----------------|
| **Pattern matching** | Yes - strong at recognizing code patterns, problem types |
| **Retrieval of typical response** | Yes - often produces standard solutions immediately |
| **Mental simulation** | Partial - can reason about approach, but simulation is shallow |
| **Expectancy generation** | Weak - doesn't automatically predict what should happen |
| **Cue recognition** | Variable - depends on context provided |

**Key observation:** Agents are strong at pattern matching and retrieval, weaker at simulation and expectancy.

### Where RPD Applies to Agents

**Agents approximate RPD when:**

| Condition | Why RPD-like |
|-----------|--------------|
| Well-documented codebase | Patterns are recognizable |
| Standard problem type | Training includes similar cases |
| Clear CLAUDE.md conventions | "Typical action" is explicit |
| Familiar language/framework | Pattern library is rich |

**Agents need deliberative analysis when:**

| Condition | Why RPD Fails |
|-----------|---------------|
| Novel problem | No pattern to match |
| Ambiguous requirements | Can't recognize situation type |
| Conflicting patterns in codebase | Multiple "typical" responses |
| Outside training distribution | Pattern matching unreliable |

### Agent "Experience" Is Different

Human experts build patterns through years of experience:

```
Human Expert:
  [Experience 1] + [Experience 2] + ... + [Experience N]
                            |
                    [Pattern Library]
                            |
                    [RPD Capability]
```

Agent "expertise" comes from:

```
AI Agent:
  [Training Data] --> [Model Weights] --> [Implicit Pattern Library]
                                               |
                                    [RPD-like Capability]
                                               +
                              [Session Context] --> [Temporary Patterns]
```

**Critical difference:** Human patterns are built through feedback loops. The expert remembers when patterns worked and when they failed. Agent patterns are frozen at training time.

**Implication:** Agents may have broad pattern libraries but lack calibration about when patterns apply. They can match patterns but may not know which match is appropriate.

### Building Agent "Expertise" Through CLAUDE.md

If RPD requires patterns + expectancies + typical actions, CLAUDE.md can provide these:

| RPD Element | CLAUDE.md Equivalent |
|-------------|---------------------|
| **Patterns** | "When you see X, this usually means Y" |
| **Expectancies** | "After doing X, you should see Y" |
| **Typical actions** | "The standard approach is X" |
| **Relevant goals** | "In this codebase, prioritize X over Y" |
| **Cues to notice** | "Pay attention to X in this project" |

**Example CLAUDE.md for RPD-like behavior:**

```markdown
## Pattern: Audio Timing Bug

**Recognition cues:**
- Bug involves timing between audio and display
- Symptoms include dropouts, glitches, desync
- Usually manifests under load

**Typical cause:**
- DMA conflict between audio and display
- ISR priority inversion
- Buffer underrun

**Standard investigation:**
1. Check ISR priorities
2. Check DMA channel conflicts
3. Verify buffer sizes and timing margins

**Expected behavior after fix:**
- Audio should be glitch-free under display load
- Timing margins should be >2ms
```

This explicitly encodes the RPD components: recognition cues, typical causes (pattern types), standard approach (typical action), and expectancies.

### The Mental Simulation Gap

RPD's Variation 3 (mental simulation) is where agents are weakest:

| Human Expert Simulation | Agent Simulation |
|------------------------|------------------|
| Runs forward from experience | Runs forward from reasoning |
| Draws on muscle memory | No physical intuition |
| Unconsciously tracks side effects | Explicit analysis required |
| "Feels" when something is wrong | Must be prompted to check |

**Agents don't automatically validate approaches before acting.** They need explicit prompting or structure to simulate.

**Mitigation: Explicit simulation prompt:**

```markdown
Before implementing, simulate:
1. Walk through each step mentally
2. What could go wrong at each step?
3. What side effects might occur?
4. What would prove this approach is wrong?
```

This forces the explicit reasoning that experts do implicitly.

### The Expectancy Problem

Human experts generate expectancies automatically:

```
Human: [Recognizes pattern] --> [Automatically expects outcomes]
                                      |
                              "If this is X, I should see Y"
                                      |
                              [Reality doesn't match] --> [Alert!]
```

Agents don't automatically generate and check expectancies:

```
Agent: [Recognizes pattern] --> [Acts] --> [Moves on]
                                             |
                                    [Doesn't check if result matches expectations]
```

**Mitigation: Explicit expectancy checking:**

```markdown
After completing the change:
1. What did you expect to happen?
2. What actually happened?
3. Any surprising results?
4. Does the outcome match your expectations?
```

This builds the feedback loop that human expertise relies on.

---

## Supervision Implications

### The Trust Calibration Problem

RPD works because experts have calibrated confidence:

| Expert Confidence | Reliability |
|------------------|-------------|
| High confidence, familiar pattern | Usually correct |
| Low confidence, unfamiliar pattern | Knows to be careful |
| High confidence, unfamiliar pattern | Dangerous - overconfident |

**Agent calibration is problematic:**

- Agents may have high confidence in areas of weak training
- Agents may not recognize when they're outside their competence
- Confidence doesn't correlate reliably with correctness

**Supervision implication:** You cannot trust agent self-assessment of confidence. Use external signals:

| Signal | What It Indicates |
|--------|-------------------|
| Task novelty | Is this similar to known patterns? |
| Response speed | Fast response = pattern match. Slow = deliberation. |
| Hedging language | "I think" vs "The answer is" |
| Asking for clarification | Agent recognizes ambiguity |

### When to Allow RPD-like Speed

**Allow fast pattern-matching when:**

| Condition | Why Safe |
|-----------|----------|
| Clear domain (Cynefin) | Best practice exists |
| Established CLAUDE.md patterns | Typical action is documented |
| High-quality tests | Wrong pattern match is caught |
| Low stakes | Failure is recoverable |

**Require deliberation when:**

| Condition | Why Deliberate |
|-----------|----------------|
| Complex/Complicated domain | Analysis needed |
| Novel situation for agent | Pattern library may not apply |
| High stakes | Can't afford pattern mismatch |
| Agent expresses uncertainty | Possible recognition failure |

### Supervision by Domain + RPD

Combining Cynefin with RPD:

| Cynefin Domain | RPD Appropriateness | Supervision Approach |
|----------------|--------------------|-----------------------|
| **Clear** | High - patterns known | Let agent use RPD, spot-check |
| **Complicated** | Medium - analyze then RPD | Require analysis phase, then allow RPD execution |
| **Complex** | Low - no patterns yet | Probe first, no RPD until patterns emerge |
| **Chaotic** | Variable - act fast, but may be novel | Allow RPD for stabilization, deliberate after |

### Developing Agent "Expertise"

Human expertise develops through:
1. **Experience:** Encountering many situations
2. **Feedback:** Learning which responses worked
3. **Reflection:** Building explicit mental models
4. **Calibration:** Adjusting confidence based on outcomes

For agents, we can simulate this through:

| Development Path | Implementation |
|-----------------|----------------|
| **Experience** | Rich examples in CLAUDE.md, diverse training |
| **Feedback** | Session feedback, CLAUDE.md updates |
| **Reflection** | After-action analysis, pattern extraction |
| **Calibration** | Track prediction vs outcome, adjust trust |

**The Einheit development cycle (from Mission Command) applies:**

1. Agent makes a decision using pattern matching
2. Outcome is evaluated
3. If pattern matched and worked: document pattern
4. If pattern matched and failed: document anti-pattern
5. If no pattern matched: add new pattern
6. Next agent benefits from accumulated patterns

---

## Could Agents Develop True RPD?

This is a deeper question about agent architecture.

### What Would Agent RPD Require?

| RPD Component | Current Agents | What Would Be Needed |
|---------------|----------------|---------------------|
| **Pattern library** | Present (frozen in weights) | Updateable pattern library |
| **Pattern matching** | Strong | Strong (already have) |
| **Expectancy generation** | Weak | Automatic prediction generation |
| **Mental simulation** | Weak | Better forward modeling |
| **Calibrated confidence** | Very weak | Experience-based confidence |
| **Feedback integration** | None (within session) | Learning from outcomes |

### The Feedback Loop Problem

Human RPD is self-improving:

```
[Experience] --> [Pattern Match] --> [Action] --> [Outcome]
                                                      |
                          [Feedback] <----------------+
                              |
                    [Adjust Patterns]
```

Agent RPD is static:

```
[Training] --> [Frozen Patterns] --> [Pattern Match] --> [Action] --> [Outcome]
                                                                          |
                                                                     [No feedback to patterns]
```

**Implication:** Agents can use RPD-like decision making but cannot improve it through experience within a session or across sessions.

### Workarounds for the Feedback Problem

**1. CLAUDE.md as Pattern Accumulator:**

Human updates CLAUDE.md based on agent outcomes. The pattern library improves, but through human mediation.

**2. Session Context as Temporary Calibration:**

Within a session, agents can build temporary calibration:
- First task outcome informs second task confidence
- Early mistakes adjust later behavior
- But this resets between sessions

**3. Fine-tuning on Outcomes:**

Train model on successful vs. unsuccessful task completions. Patterns shift toward what worked.

**4. Verifier-Mediated Feedback:**

Verifier agent provides immediate feedback, influencing subsequent actions within session.

---

## What This Means for Supervision

### The Core Insight

**RPD explains why experienced humans can supervise effectively with minimal effort, and why agent supervision is harder.**

Human expert supervisors use RPD:
- Recognize situation type at a glance
- Know what to check
- Spot anomalies against expectancies
- Fast feedback cycle

This is why:
- Senior developers review PRs quickly (pattern recognition)
- Experienced managers know when something is wrong (expectancy violation)
- Experts seem to make decisions "intuitively" (invisible pattern matching)

**Agent supervision lacks RPD on the supervisor side when:**
- Supervisor isn't expert in the domain
- Supervisor is overwhelmed (no time for pattern matching)
- Patterns haven't been explicitly documented

**Implication:** Good supervision requires either expert supervisors (human RPD) or documented patterns (explicit RPD equivalent for non-experts).

### RPD-Informed CLAUDE.md Design

To enable RPD-like behavior, CLAUDE.md should include:

| Section | Purpose |
|---------|---------|
| **Situation Types** | What patterns exist in this codebase |
| **Recognition Cues** | How to identify each situation type |
| **Typical Responses** | Standard approach for each type |
| **Expectancies** | What should happen after each response |
| **Anomaly Signals** | What indicates the pattern match was wrong |

**Example section:**

```markdown
## Situation: Build Failure

### Recognition Cues
- `make` returns non-zero
- Compiler errors in output
- Linker errors about undefined symbols

### Typical Responses by Subtype

#### Missing Include
**Cue:** "undeclared identifier"
**Typical Response:** Add missing #include
**Expected Outcome:** Build succeeds; file change localized

#### Missing Dependency
**Cue:** "undefined reference to"
**Typical Response:** Check third_party/, update BUILD
**Expected Outcome:** Build succeeds; BUILD file changed

### Anomaly Signals
- Fix didn't work --> Misrecognized situation type
- Required touching many files --> Problem is systemic, not local
- Build passes but tests fail --> Fix was incomplete
```

This gives the agent (and human reviewer) explicit patterns for RPD-like operation.

---

## Open Questions

1. **Can agents develop calibrated confidence?** Or is this fundamentally requiring feedback loops they don't have?

2. **Is CLAUDE.md-as-pattern-library sufficient?** Or do agents need architectural changes to truly benefit from RPD?

3. **How do you detect pattern mismatch?** When an agent uses the wrong pattern, what signals this?

4. **Can agents generate expectancies?** If prompted to predict outcomes, are those predictions accurate enough to use for validation?

5. **What's the right prompting for mental simulation?** How do you get agents to genuinely simulate vs. superficially walk through steps?

6. **Transfer of patterns:** Can patterns learned in one codebase transfer to another? How similar must codebases be?

7. **Pattern interference:** When the agent has conflicting patterns (from training vs. CLAUDE.md), which wins?

8. **Novice supervisor problem:** If the human supervisor isn't an expert, how do they recognize when agent RPD has failed?

---

## Systems to Build

- [ ] **Pattern library template:** CLAUDE.md structure that encodes RPD components
- [ ] **Expectancy checker:** Agent predicts outcome before acting; system compares to actual outcome
- [ ] **Recognition confidence tracker:** Log when agent seems to "pattern match" vs. "deliberate"
- [ ] **Anomaly detector:** Flag when outcomes don't match expected patterns
- [ ] **Pattern extraction tool:** Analyze successful tasks to extract patterns for CLAUDE.md
- [ ] **Simulation prompter:** Structured prompt that forces genuine mental simulation
- [ ] **Calibration tracker:** Compare agent confidence signals to actual outcomes over time

---

## Summary

Recognition-Primed Decision Making explains how experts decide under pressure: pattern recognition, not option comparison. This has direct implications for agent supervision:

**What RPD reveals:**

1. **Experts don't compare options.** They recognize situations and retrieve typical responses. Good CLAUDE.md enables this for agents.

2. **Mental simulation validates.** Before acting, experts simulate the approach. Agents need explicit prompting to do this.

3. **Expectancies catch errors.** Experts know what should happen and notice when it doesn't. Agents need explicit expectancy tracking.

4. **Expertise requires feedback loops.** Human patterns improve through experience. Agent patterns are frozen at training time.

5. **Calibrated confidence matters.** Experts know when they're uncertain. Agent confidence is poorly calibrated.

**For agent supervision:**

- **Enable RPD in Clear domains:** Document patterns so agents can match-and-act
- **Require deliberation in Complex domains:** Pattern matching fails when patterns don't exist
- **Build explicit expectancies:** Force agents to predict before they act
- **Track pattern match quality:** Log recognition vs. outcomes to build calibration data
- **Human-mediate the feedback loop:** Since agents can't update their patterns, update CLAUDE.md based on outcomes

**The key insight:** Agents can exhibit RPD-like behavior (pattern matching, typical responses) but lack the feedback loops that make human RPD self-improving. Supervision must either provide those feedback loops externally (CLAUDE.md updates) or compensate for their absence (more verification, explicit simulation).

---

## Sources

### Gary Klein's Work
- Klein, Gary. "Sources of Power: How People Make Decisions" (1998) - Primary RPD exposition
- Klein, Gary. "The Power of Intuition" (2003) - Practical applications
- Klein, Gary. "Seeing What Others Don't" (2013) - Insight and pattern recognition
- Klein, Orasanu, et al. "Decision Making in Action" (1993) - Naturalistic decision research

### Related Work
- Kahneman, Daniel & Klein, Gary. "Conditions for Intuitive Expertise: A Failure to Disagree" (2009) - When intuition can be trusted
- Simon, Herbert. "Models of Bounded Rationality" (1982) - Satisficing concept
- Dreyfus, Hubert & Dreyfus, Stuart. "Mind Over Machine" (1986) - Skill acquisition model

### Framework Connections
- OODA Loop (Boyd) - RPD maps to Orient and the IG&C fast path
- Cynefin - Clear domain aligns with RPD; Complex domain requires different approach
- Mission Command - Einheit enables shared patterns; expertise enables delegation

---

## Status

**Phase:** Initial exploration complete. Core insight: RPD explains expert decision-making as pattern recognition + simulation, not option comparison. Agents show strong pattern matching but weak simulation and no feedback loop. Supervision should enable RPD in appropriate domains while compensating for missing calibration and feedback.

**Next:** Build expectancy checker and pattern extraction tool to operationalize RPD concepts.
