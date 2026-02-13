# Technology-Augmented Decision-Making: Architectural Analysis for AI Agent Systems

## Executive Summary

Technology-Augmented Decision-Making (TADM) research provides critical insights for AI agent system design because **human-AI agent coordination is itself a technology-augmented decision-making problem.** When a human supervises AI agents, the human is the decision-maker working with agents as augmentation. The same dynamics of trust, bias, and failure modes that affect dispatchers working with decision support systems affect users working with AI agents.

This creates a recursive insight: TADM research teaches us both how to design agent systems (agents as augmentation for humans) and how to understand agent behavior (agents as augmented decision-makers themselves).

| TADM Concept | Human Supervising Agents | Agent Internal Processing |
|--------------|-------------------------|--------------------------|
| **Automation bias** | Human accepts agent outputs without critical evaluation | Agent accepts tool outputs without verification |
| **Skill degradation** | Human loses skills when agents always help | Agent loses capability when tools always available |
| **Trust calibration** | Human must calibrate trust in agent outputs | Agent must calibrate trust in tool/source reliability |
| **Expertise paradox** | Experts may be hurt by agent assistance | Expert-level agents may be hurt by augmentation |
| **Decision transformation** | Human's job changes from "doing" to "supervising" | Agent's job changes when tools are added |

**The central architectural claim:** The failure modes of technology-augmented decision-making are not limited to humans working with technology. They apply to any decision-making system that relies on augmentation---including AI agents that use tools, consult sources, or coordinate with other agents. Understanding TADM enables designing both better human-agent interaction and better agent-tool interaction.

---

## Part I: The Fundamental Parallel

### 1.1 Human-Agent Supervision as Technology-Augmented Decision-Making

When a human works with AI agents, the interaction follows TADM patterns:

**The human's decision transforms:**

Without agents: "How should I solve this problem?"

With agents: "Should I accept the agent's approach, modify it, or intervene?"

This is the same transformation TADM research documents for dispatchers. The human is no longer a primary problem-solver---they are a supervisor evaluating agent recommendations.

**TADM dynamics apply directly:**

| TADM Dynamic | Manifestation in Agent Supervision |
|--------------|-----------------------------------|
| Automation bias | Accepting agent outputs without review; trusting agent because "it's usually right" |
| Skill degradation | Losing ability to do tasks agents handle; becoming dependent on agent assistance |
| Trust calibration | Need to know when to trust agent work vs. when to verify |
| Expertise paradox | Expert developers may be hurt by agent assistance; novices benefit more |
| Out-of-the-loop | Supervisors lose situational awareness when agents work autonomously |

### 1.2 Modes of Human-Agent Interaction

Mapping TADM interaction modes to agent supervision:

| Mode | Agent Role | Human Role | Example |
|------|-----------|-----------|---------|
| **Agent as Information Source** | Researches and reports findings | Decides what to do with findings | Agent searches codebase, reports relevant files |
| **Agent as Analyst** | Interprets information, provides assessment | Evaluates assessment, decides action | Agent reviews PR, assesses quality issues |
| **Agent as Advisor** | Recommends specific actions | Decides whether to authorize | Agent proposes code changes |
| **Agent as Executor** | Decides and acts within scope | May veto or redirect | Agent implements within boundaries |

**The optimal mode depends on:**
- Task novelty (novel → lower autonomy)
- Consequence severity (high stakes → lower autonomy)
- Time pressure (high pressure → higher autonomy)
- Trust level (low trust → lower autonomy)
- Human oversight capacity (limited capacity → higher autonomy)

### 1.3 What Information Do Humans Need to Supervise Agent Decisions?

Effective human supervision requires:

**Situational Awareness:**
- What is the agent trying to accomplish? (Goal)
- What has the agent done so far? (History)
- What is the agent about to do? (Intention)
- What does the agent's environment look like? (Context)

**Decision Rationale:**
- Why is the agent recommending/taking this action?
- What alternatives did the agent consider?
- What tradeoffs is the agent making?
- What uncertainties affect the decision?

**Confidence Calibration:**
- How confident is the agent in its approach?
- What is the basis for that confidence?
- What could make the agent wrong?
- When should the human trust vs. verify?

**Failure Indicators:**
- What would indicate the agent is failing?
- What does the agent not know that it should?
- Where are the boundaries of agent competence?
- What errors has the agent made before?

---

## Part II: Where Agents Struggle vs. Excel as Augmentation

### 2.1 Agents as Augmentation: Strengths

**Consistent application:** Unlike human decision support that varies with fatigue and stress, agents apply their training consistently.

**Comprehensive processing:** Agents can process more information than humans, potentially improving information gathering.

**Speed:** Agents can analyze faster than humans can evaluate, enabling rapid iteration.

**Availability:** Agents don't require rest, don't have bad days, and scale with demand.

**Documentation:** Agent reasoning can be logged, enabling post-hoc analysis impossible with human-only decisions.

### 2.2 Agents as Augmentation: Weaknesses

**Calibration failures:** Agents often display high confidence even when wrong. Confidence expression may not correlate with actual reliability.

**Novel situation blindness:** Agents trained on past data may not recognize when a situation is outside their training distribution.

**Explanation limitations:** Agent explanations are often post-hoc rationalizations, not actual reasoning. Users may develop false confidence from explanations.

**Context limitations:** Agents' finite context windows limit situational awareness, potentially missing relevant information.

**Verification difficulty:** Humans often cannot effectively evaluate agent work, especially for complex or specialized tasks.

### 2.3 The Trust Calibration Challenge

TADM research identifies trust calibration as central to effective augmentation:

| Trust State | Human-AI Dispatch | Human-Agent Development |
|-------------|-------------------|------------------------|
| **Calibrated** | Trust matches AI reliability | Trust matches agent reliability for task type |
| **Over-trust** | Follow AI despite contrary evidence | Accept agent work without review |
| **Under-trust** | Override AI when it's correct | Duplicate agent work unnecessarily |

**Agent-specific trust challenges:**

- **Task-specific reliability varies:** Agent may be excellent at code generation but poor at architecture decisions. Trust should vary by task type.

- **Reliability changes over time:** As agent capabilities evolve, trust calibration must update. Yesterday's unreliable agent may be today's reliable one (and vice versa).

- **Context affects reliability:** Same agent may be reliable on well-documented codebases but unreliable on novel or undocumented ones.

- **Feedback is delayed:** Unlike dispatch where outcomes are visible quickly, agent errors in code may not manifest until much later.

---

## Part III: Automation Bias in Agent Supervision

### 3.1 Manifestations of Automation Bias

**Accepting agent recommendations without critical evaluation:**
- "The agent said to use this pattern, so I'll use it"
- Not checking agent reasoning against own understanding
- Treating agent output as starting point rather than hypothesis

**Assuming agent has considered everything human would:**
- "The agent must have thought about edge cases"
- Not asking about alternatives considered
- Assuming comprehensive analysis when agent may have been shallow

**Following suggestions because "the agent knows the codebase":**
- Deferring to agent's apparent knowledge
- Not recognizing when agent knowledge is incomplete or wrong
- Treating pattern matching as understanding

**Approving agent work without reviewing it carefully:**
- Skimming agent output
- Approving because "it looks right"
- Rubber-stamping when busy or tired

### 3.2 Risk Factors for Automation Bias

| Factor | Why It Increases Bias |
|--------|----------------------|
| Agent usually correct | Builds expectation that checking is wasted effort |
| Review takes effort | Path of least resistance is accepting |
| Agent explanations sound reasonable | Creates illusion of understanding |
| No immediate consequences | Errors don't provide instant feedback |
| High workload | Cognitive resources depleted |
| Trust already established | Default to following without reevaluation |

### 3.3 Countermeasures for Automation Bias

**Periodic detailed review even when trusting agent:**
```markdown
# Automation Bias Prevention Protocol

## Sampling Protocol
Every [N]th agent task, perform full review:
- Read all agent-modified code
- Trace logic through changes
- Verify against requirements
- Check for missed edge cases

## Calibration Events
Weekly: One task where you deliberately look for agent errors
- Don't accept first output
- Require agent to show alternatives
- Question confident assertions
```

**Explicit disagreement practice:**
```markdown
# Disagreement Practice

Before approving agent work, explicitly ask:
- What would I do differently if doing this myself?
- What is the agent NOT considering?
- What assumption is the agent making that I haven't verified?

Require yourself to identify at least one concern before approving.
```

**Metrics on agent error rate and human catch rate:**
```markdown
# Catch Rate Tracking

Track:
- Agent errors discovered in code review
- Agent errors discovered in production
- Agent errors discovered by tests
- Errors caught by human before merge

Calculate:
- Human catch rate = (errors caught by human) / (total agent errors)
- Target: >80% catch rate
- If below target: Increase review intensity
```

---

## Part IV: Skill Degradation and Agent Assistance

### 4.1 Skills at Risk

When humans rely on agents, specific skills may atrophy:

| Skill | How Agent Assistance Affects It |
|-------|--------------------------------|
| Code reading comprehension | Agent summarizes; human stops reading deeply |
| Debugging | Agent diagnoses; human loses troubleshooting intuition |
| Architecture understanding | Agent navigates; human loses mental map |
| Writing skills | Agent generates; human loses composition ability |
| Pattern recognition | Agent matches; human stops developing intuition |
| Tool knowledge | Agent operates tools; human forgets how |

### 4.2 The Skill Degradation Paradox

Skills most needed when agents fail are least available because agents usually succeed:

- **When agent can't solve a problem:** Human needs deep skills to take over
- **When agent makes subtle error:** Human needs expertise to detect it
- **When agent is unavailable:** Human needs full capability to proceed
- **When situation is novel:** Human needs judgment agent wasn't trained for

**But these skills have atrophied because agents handled similar situations.**

### 4.3 Countermeasures for Skill Degradation

**Deliberate "manual mode" practice:**
```markdown
# Skill Maintenance Protocol

## Weekly Practice
One task per week completed without agent assistance:
- No code generation
- No codebase navigation assistance
- Manual debugging
- Manual test writing

## Skill Assessment
Monthly assessment of key skills:
- Can you navigate this codebase without agent?
- Can you debug this issue without agent?
- Can you write this function without agent?

If skill has degraded: Increase manual practice for that skill.
```

**Agents that teach rather than just do:**
```markdown
# Teaching Mode Configuration

When agent completes task, require explanation:
- What approach did you take?
- What alternatives were considered?
- What would you teach someone about this problem?

Don't just accept output---understand it.
```

**Career paths requiring demonstrated independent capability:**
```markdown
# Capability Verification

Before promoting/advancing:
- Demonstrated skill without agent assistance
- Passed assessment on core competencies
- Completed substantial task without agent help
```

---

## Part V: TADM Failure Modes in Agent Supervision

### 5.1 Mode Confusion

**Definition:** Uncertainty about what mode agent is in and what behavior to expect.

**Manifestations:**
- Unclear whether agent is actively working or waiting
- Confusion about agent's current scope and limitations
- Misunderstanding about what agent can see (inputs available)
- Uncertainty about whether agent recommendations are current

**CLAUDE.md pattern:**
```markdown
# Agent Mode Visibility

## Status Indicators
Agent must always indicate:
- Current mode: [ANALYZING, PLANNING, EXECUTING, WAITING]
- Current scope: [what files/context being considered]
- Current confidence: [HIGH/MEDIUM/LOW on current approach]

## Mode Transitions
When changing modes, agent announces:
- "Transitioning from ANALYZING to EXECUTING"
- "Scope expanding to include [additional context]"
```

### 5.2 Anchoring and Insufficient Adjustment

**Definition:** Agent recommendations serve as anchors that humans adjust from insufficiently.

**Manifestations:**
- Agent suggests approach A; human might consider A' or A'' but not B
- Agent confidence of 75% adjusted but not enough when context suggests 30%
- Agent's problem framing constrains human's solution space

**CLAUDE.md pattern:**
```markdown
# Anti-Anchoring Protocol

## Multiple Options Requirement
For significant decisions, agent must provide:
- Primary recommendation with rationale
- At least one alternative approach with rationale
- Explicit tradeoffs between options

## Confidence Challenge
Before accepting agent's high-confidence recommendation:
- What would make this wrong?
- What evidence would lower confidence?
- What alternatives weren't considered?
```

### 5.3 Attention Tunneling

**Definition:** Narrowed attention focus causing important information outside focus to be missed.

**Manifestations:**
- Focusing on agent's recommendation while missing context cues
- Attending to agent output while missing broader system state
- Concentrating on primary recommendation while ignoring caveats

**CLAUDE.md pattern:**
```markdown
# Attention Management

## Context Requirements
Agent output must include:
- Primary recommendation
- Relevant context that affects recommendation
- Known limitations of current analysis
- What wasn't analyzed and why

## Periodic Reorientation
Every [N] interactions, explicitly check:
- Am I aware of overall project state?
- What context might I be missing?
- Has something changed that affects prior decisions?
```

### 5.4 Inappropriate Trust Transfer

**Definition:** Trust from one context applied to another where not warranted.

**Manifestations:**
- Trusting agent for novel tasks based on routine task performance
- Trusting agent explanations as much as agent code
- Trusting agent on unfamiliar codebase based on familiar codebase performance

**CLAUDE.md pattern:**
```markdown
# Trust Specificity

## Trust by Task Type
| Task Type | Trust Level | Verification Required |
|-----------|-------------|----------------------|
| Code formatting | High | None |
| Simple implementation | Medium | Review output |
| Complex logic | Low | Detailed review |
| Architecture decisions | Very Low | Independent analysis |
| Security-sensitive | Very Low | Expert review |

## Context Transfer Warning
When working in new context (new codebase, new domain, new task type):
- Reset trust assumptions
- Require additional verification
- Build trust incrementally through demonstrated performance
```

---

## Part VI: Designing for Appropriate Reliance

### 6.1 The Levels of Automation for Agent Systems

Mapping Parasuraman's LOA framework to agent systems:

| Level | Agent Behavior | Human Role | When Appropriate |
|-------|---------------|-----------|-----------------|
| 1 | Agent provides no assistance | Human does everything | Agent unavailable |
| 2 | Agent provides information | Human interprets and decides | Research tasks |
| 3 | Agent narrows options | Human evaluates options | Exploratory work |
| 4 | Agent suggests one approach | Human evaluates recommendation | Standard tasks |
| 5 | Agent executes if human approves | Human reviews before action | Moderate trust |
| 6 | Agent executes unless human vetoes (time-limited) | Human monitors | Higher trust, time pressure |
| 7 | Agent executes, then informs | Human reviews after | High trust tasks |
| 8 | Agent informs only if asked | Human spot-checks | Routine operations |
| 9 | Agent informs only if it decides to | Human monitors exceptions | Highly routine |
| 10 | Agent acts autonomously | Human uninvolved | Full automation |

**For agent development systems, typical operating range is 4-7:**
- Level 4-5 for novel or high-stakes tasks
- Level 6-7 for routine tasks with established trust
- Level 8+ rarely appropriate due to error consequences

### 6.2 Active Engagement Design

**Problem:** Passive monitoring leads to out-of-the-loop failures.

**Solution:** Design for active engagement.

```markdown
# Active Engagement Requirements

## Checkpoint Protocol
Agent pauses for human engagement at:
- Task understanding confirmation
- Approach selection
- Before irreversible actions
- After significant progress

## Engagement Requirements
At each checkpoint, human must:
- Read agent's understanding (not just confirm)
- Evaluate agent's approach (not just approve)
- Consider alternatives (not just accept default)
- Document any concerns

## Anti-Rubber-Stamping
If human approves N checkpoints in <X seconds total:
- Flag potential rubber-stamping
- Require explicit justification for approval speed
```

### 6.3 Reasoning Transparency

**Problem:** Agent outputs without reasoning create false confidence.

**Solution:** Require and display reasoning.

```markdown
# Reasoning Display Requirements

## For Significant Decisions
Agent must show:
1. What information was considered
2. What assumptions were made
3. What alternatives were evaluated
4. Why the chosen approach was selected
5. What uncertainties affect the recommendation

## Reasoning Quality Check
Human evaluates reasoning for:
- Does reasoning support conclusion?
- Are assumptions valid?
- Were alternatives fairly considered?
- Are uncertainties acknowledged?

## If Reasoning Is Unclear
Do not proceed. Ask agent to clarify reasoning.
```

### 6.4 Confidence Calibration Display

**Problem:** Agent confidence may not match actual reliability.

**Solution:** Calibrated confidence with track record.

```markdown
# Confidence Display Protocol

## Confidence with Calibration
Instead of: "I'm 85% confident in this approach"

Display: "Confidence: HIGH
Track record for similar tasks: 78% correct on first attempt
Factors increasing confidence: [list]
Factors decreasing confidence: [list]"

## Confidence Validation
Track:
- Agent's stated confidence per task
- Actual outcome
- Calculate calibration accuracy

If agent is overconfident (states 90%, correct 70%):
- Flag in interface
- Adjust interpretation of confidence claims
```

---

## Part VII: Agent-to-Agent TADM Dynamics

### 7.1 Agents as Augmented Decision-Makers

TADM dynamics apply not just to humans working with agents, but to agents working with tools and other agents:

| Dynamic | Human Working with AI | Agent Working with Tools/Agents |
|---------|----------------------|--------------------------------|
| Automation bias | Accept AI without evaluation | Accept tool output without verification |
| Trust calibration | Must calibrate trust in AI | Must calibrate trust in tools |
| Skill degradation | Lose skills when AI helps | May lose capability when tools available |
| Anchoring | AI anchors human decisions | First tool output anchors agent approach |

### 7.2 Agent Automation Bias

Agents may exhibit their own automation bias:

**Accepting tool outputs without verification:**
- Agent runs tool, takes output as ground truth
- Agent doesn't verify tool output against other sources
- Agent doesn't recognize when tool might be wrong

**Following first approach without considering alternatives:**
- Agent finds one solution, stops searching
- Agent doesn't consider whether solution is optimal
- Agent anchors on first pattern match

**Trusting sources without calibration:**
- Agent treats all documentation as equally reliable
- Agent doesn't distinguish canonical from deprecated information
- Agent doesn't notice when sources conflict

**CLAUDE.md pattern:**
```markdown
# Tool Output Verification

## Before Accepting Tool Output
- Is this output consistent with other evidence?
- Could the tool have failed or returned partial results?
- Is there a way to verify independently?

## Multiple Source Requirement
For critical facts:
- Verify in multiple places
- If sources conflict, investigate
- If single source, acknowledge uncertainty
```

### 7.3 Agent Trust Calibration

Agents need to calibrate trust in their tools and sources:

```markdown
# Source Reliability Framework

## Source Hierarchy
| Source | Reliability | Treatment |
|--------|-------------|-----------|
| Test results | High | Accept if passing, investigate if failing |
| Compiler output | High | Accept as ground truth |
| Documentation | Medium | Verify against code when possible |
| Comments | Low | May be outdated, verify |
| Conversation history | Medium | May contain errors, verify critical claims |

## Tool Reliability
| Tool | Reliability | Treatment |
|------|-------------|-----------|
| grep/search | High | But may miss results (check patterns) |
| File read | High | But file may be stale |
| Build/test | High | But may have false negatives |
| API calls | Medium | May fail, may return stale data |

## When Sources Conflict
1. Identify the conflict
2. Investigate which source is more likely correct
3. If can't resolve, report conflict to human
```

---

## Part VIII: Measurement Framework

### 8.1 Human-Agent Interaction Metrics

| Metric | Definition | Target | Warning |
|--------|------------|--------|---------|
| **Catch rate** | Human-caught errors / total agent errors | >80% | <60% |
| **Override rate** | Human overrides / total agent recommendations | 5-20% | <2% (rubber-stamping) or >40% (distrust) |
| **Review depth** | Time spent reviewing / agent output complexity | Scales with complexity | Constant time (not adapting) |
| **False override rate** | Incorrect overrides / total overrides | <20% | >40% |
| **Trust calibration** | |actual accuracy - perceived accuracy| | <10% | >25% |

### 8.2 Skill Maintenance Metrics

| Metric | Definition | Target | Warning |
|--------|------------|--------|---------|
| **Independent completion rate** | Tasks completed without agent | Stable | Declining |
| **Manual mode time** | Time to complete without agent | Stable | Increasing (skill loss) |
| **Skill assessment scores** | Periodic skill evaluation | Stable | Declining |
| **Fallback success rate** | Success when agent unavailable | >90% | <70% |

### 8.3 Appropriate Reliance Metrics

| Metric | Definition | Target | Warning |
|--------|------------|--------|---------|
| **Trust-reliability match** | Correlation between trust and actual reliability | >0.8 | <0.5 |
| **Override appropriateness** | Overrides that improved outcome / total overrides | >60% | <40% |
| **Acceptance appropriateness** | Acceptances with good outcome / total acceptances | >90% | <80% |
| **Calibration events completed** | Scheduled trust calibration exercises | 100% | <80% |

---

## Part IX: Design Patterns

### 9.1 Pattern: Graduated Autonomy

**Problem:** Fixed autonomy level doesn't match varying task characteristics.

**Solution:** Autonomy level adapts to task characteristics.

```markdown
# Graduated Autonomy Framework

## Autonomy Level Determination

For each task, assess:
- Novelty: [1-5] How novel is this task type?
- Stakes: [1-5] How severe are consequences of error?
- Trust: [1-5] Track record on similar tasks?
- Time pressure: [1-5] How urgent is completion?

Calculate autonomy: (Trust + Time_pressure) - (Novelty + Stakes) + 5

| Score | Autonomy Level |
|-------|---------------|
| 1-3 | Level 4: Suggest approach, require approval |
| 4-6 | Level 5: Execute if approved |
| 7-9 | Level 6: Execute unless vetoed |
| 10 | Level 7: Execute, inform after |

## Dynamic Adjustment
- Errors → reduce autonomy for similar tasks
- Successful execution → maintain or slightly increase
- Novel situation recognized → drop autonomy
```

### 9.2 Pattern: Calibration Events

**Problem:** Trust calibration drifts over time without feedback.

**Solution:** Scheduled events that test and recalibrate trust.

```markdown
# Calibration Event Protocol

## Weekly Calibration
One task where human:
1. Predicts agent approach before seeing it
2. Predicts agent confidence before seeing it
3. Compares prediction to actual
4. Notes calibration errors

## Monthly Deep Review
One task where human:
1. Does task independently (without looking at agent work)
2. Agent does same task
3. Compare approaches
4. Identify where agent was better, where human was better
5. Update trust calibration based on comparison

## Calibration Metrics
Track:
- Prediction accuracy (how well human predicts agent)
- Relative quality (human vs. agent output quality)
- Trust calibration error (stated trust - revealed trust)
```

### 9.3 Pattern: Failure Surfacing

**Problem:** Agent errors are silent or hidden, preventing learning.

**Solution:** Design systems that surface and attribute failures.

```markdown
# Failure Surfacing Protocol

## Error Classification
Every agent error is classified:
- Type: [syntax, logic, design, requirement, integration]
- Severity: [trivial, minor, moderate, major, critical]
- Detectability: [obvious, hidden, delayed]
- Attribution: [agent error, tool failure, ambiguous input, missing context]

## Feedback Loop
All errors fed back to:
- Error log (for pattern analysis)
- Human calibration (update trust for error type)
- Agent session (if persistent, to inform future behavior)

## Error Pattern Analysis
Weekly review:
- What types of errors is agent making?
- What types is human catching?
- What types are reaching production?
- What systemic changes would reduce errors?
```

### 9.4 Pattern: Explanation Requirements

**Problem:** Agent outputs without explanation create false confidence.

**Solution:** Require structured explanations that enable evaluation.

```markdown
# Explanation Protocol

## Explanation Requirements by Task Type

### Implementation Tasks
Required explanation:
- What pattern is being followed
- Why this pattern (not alternatives)
- What assumptions are being made
- What edge cases are handled (and not handled)

### Analysis Tasks
Required explanation:
- What information was considered
- What information was not available
- What conclusions were drawn
- What confidence level and why

### Design Tasks
Required explanation:
- What constraints were balanced
- What tradeoffs were made
- What alternatives were considered
- Why this design over alternatives

## Explanation Evaluation
Human evaluates:
- Does explanation support conclusion?
- Are assumptions made explicit and reasonable?
- Are tradeoffs acknowledged?
- Is confidence appropriate?
```

### 9.5 Pattern: Human-in-the-Loop for Novel Situations

**Problem:** Agent may not recognize when situation is outside training.

**Solution:** Explicit novelty detection with human escalation.

```markdown
# Novelty Detection Protocol

## Novelty Indicators
Agent watches for:
- No similar examples in training/documentation
- Conflicting patterns in codebase
- Unusual requirements or constraints
- High uncertainty in multiple components
- User explicitly marks as novel

## Novelty Response
When novelty detected:
1. Flag to human: "This situation appears novel because [reasons]"
2. Reduce autonomy: Require explicit approval for approach
3. Request guidance: "Should I proceed with [approach] or do you want to provide direction?"
4. Document: Whatever approach is taken becomes example for future

## Post-Novel-Task Review
After completing novel task:
- Was approach successful?
- Should this become standard pattern?
- Update documentation to prevent future novelty
```

---

## Part X: Multi-Agent Implications

### 10.1 TADM Dynamics in Multi-Agent Systems

When multiple agents coordinate, TADM dynamics multiply:

**Inter-agent automation bias:**
- Agent A accepts Agent B's output without verification
- No agent questions the "chain of reasoning" through multiple agents
- Errors compound through trust chains

**Trust network complexity:**
- Human must calibrate trust in each agent
- Each agent must calibrate trust in other agents
- Trust calibration becomes O(n^2) problem

**Skill degradation cascade:**
- Specialized agents lose generalist capability
- Generalist agents lose specialized capability
- System becomes brittle to agent failures

### 10.2 Human Oversight Scaling

TADM research highlights a scaling problem:

| Agent Count | Human Oversight Feasibility |
|-------------|---------------------------|
| 1-2 | Detailed review possible |
| 3-5 | Sampling-based review |
| 6-10 | Statistical oversight only |
| 10+ | Outcome-based oversight |

**Implication:** As agent systems scale, human oversight must become:
- More automated (meta-agents checking agents)
- More statistical (sampling, not comprehensive)
- More outcome-based (check results, not process)

This creates new TADM problems: humans supervising agent-supervision-systems, with all the same bias and calibration challenges at a meta-level.

### 10.3 Cross-Reference: Related Models

| Related Model | TADM Connection |
|--------------|-----------------|
| **OODA Loop** | Orient phase determines whether to trust augmentation; augmentation can corrupt orientation through automation bias |
| **Multi-Agency Coordination** | Human supervising multiple agents faces same challenges as commander supervising multiple agencies |
| **Shared Mental Models** | Effective augmentation requires shared mental model between human and agent about task, approach, and constraints |
| **Jidoka** | "Stop and surface problems" counters automation bias by making failures visible |

---

## Part XI: Implementation Examples

### 11.1 CLAUDE.md Template for TADM-Aware Agent Behavior

```markdown
# Technology-Augmented Decision-Making Awareness

## Agent Self-Awareness

### Confidence Calibration
I track my own reliability:
- Task types where I'm historically accurate: [list]
- Task types where I'm historically less accurate: [list]
- Current task type: [classification]
- Historical accuracy for this type: [percentage]

### Novelty Detection
I flag novel situations when:
- No similar examples in documentation
- Multiple conflicting patterns
- Unusual constraints or requirements
- High uncertainty in analysis

### Explanation Requirements
For significant outputs, I always provide:
- What I considered
- What assumptions I made
- What alternatives exist
- Why I chose this approach
- What could make me wrong

## Supporting Human Calibration

### Trust Calibration Support
I help you calibrate trust by:
- Reporting confidence with historical accuracy
- Flagging when situation differs from my strengths
- Admitting uncertainty explicitly
- Pointing out what I might be missing

### Anti-Automation-Bias Support
I actively counter automation bias by:
- Asking clarifying questions before executing
- Offering alternatives, not just primary recommendation
- Flagging assumptions that need verification
- Suggesting when you should verify my work

### Skill Maintenance Support
I preserve your skills by:
- Explaining reasoning, not just providing answers
- Teaching patterns, not just applying them
- Suggesting when you might want to do something yourself
- Supporting your learning, not replacing your thinking
```

### 11.2 Human Supervisor Protocol

```markdown
# Human Supervision Protocol

## Pre-Task
Before assigning task to agent:
- What is my expected approach? (Anchor check)
- What would good output look like?
- What verification will I perform?

## During-Task
While agent works:
- Am I maintaining situational awareness?
- Am I ready to intervene if needed?
- Am I checking assumptions, not just progress?

## Post-Task
After agent completes:
- Did I actually review, or rubber-stamp?
- Did I consider alternatives to agent's approach?
- What would I have done differently?
- Is my trust calibration appropriate?

## Periodic
Regular maintenance:
- Weekly: Complete one task without agent
- Monthly: Deep comparison of my work vs. agent work
- Quarterly: Skill assessment independent of agent
```

---

## Part XII: Conclusion

### Key Insights

1. **Human-agent interaction is technology-augmented decision-making.** All the failure modes documented in TADM research---automation bias, skill degradation, trust calibration failures---apply to humans working with AI agents.

2. **The decision transforms, not just the process.** When agents are introduced, humans shift from "doing the task" to "supervising agent doing the task." These require different skills and have different failure modes.

3. **Trust calibration is central.** Neither over-trusting (automation bias) nor under-trusting (wasted capability) produces good outcomes. Calibrated trust requires active maintenance.

4. **Skills atrophy without use.** Humans who rely on agents lose capability they need when agents fail or face novel situations. Deliberate skill maintenance is required.

5. **Agents themselves face TADM dynamics.** Agents using tools and other agents face analogous automation bias and trust calibration challenges.

### The Meta-Insight

TADM research reveals a recursive structure:
- Humans supervise agents (TADM dynamics apply)
- Agents use tools (TADM dynamics apply)
- Agents coordinate with agents (TADM dynamics apply)
- Humans supervise agent-systems (TADM dynamics at meta-level)

At every level, the same principles apply: trust must be calibrated, automation bias must be countered, skills must be maintained, novel situations must be recognized.

Designing effective agent systems requires applying TADM principles at every level of the stack---not just at the human-agent interface, but throughout the system architecture.

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent architecture analysis applying TADM principles
**Status:** Complete

---

## Sources

### Primary Research

- Technology-Augmented Decision-Making source document (this repository): `/docs/emergency-dispatch/technology-augmented-decision-making.md`

### TADM Foundations

- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A Model for Types and Levels of Human Interaction with Automation. *IEEE Transactions on Systems, Man, and Cybernetics*.

- Lee, J. D., & See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*.

- Mosier, K. L., & Skitka, L. J. (1996). Human Decision Makers and Automated Decision Aids. In *Automation and Human Performance*.

### Automation Bias Research

- Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does Automation Bias Decision-Making? *International Journal of Human-Computer Studies*.

- Cummings, M. L. (2004). Automation Bias in Intelligent Time Critical Decision Support Systems. *AIAA*.

### Human-AI Teaming

- Miller, T. (2019). Explanation in Artificial Intelligence. *Artificial Intelligence*.

- Bansal, G., et al. (2021). Does the Whole Exceed its Parts? *CHI*.

- O'Neill, T., et al. (2022). Human-Autonomy Teaming. *Human Factors*.

### Cross-References in This Repository

- OODA Loop analysis: `/docs/management/ooda-loop-agent-analysis.md`
- Multi-Agency Coordination: `/docs/emergency-dispatch/multi-agency-coordination-agent-analysis.md`
- Shared Mental Models: `/docs/incident-response/shared-mental-models.md`
