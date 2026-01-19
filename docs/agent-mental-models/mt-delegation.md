# Manager Tools: Delegation

Exploring how the Delegation concept applies to AI agent supervision.

## Human Practice

| Aspect | Description |
|--------|-------------|
| **Purpose** | Push work down to grow organizational capability |
| **Psychological Benefit** | Growth through stretch assignments, trust-building |
| **Manager Benefit** | Scalability - manager capacity multiplied by team |
| **Failure Mode** | Managers who don't delegate become bottlenecks |
| **Levels** | From "do this exactly" to "handle this area, report back" |

## The Core Problem

Human delegation has two outputs:
1. **Work gets done** (immediate)
2. **Delegate grows** (long-term)

For agents, output #2 doesn't exist. Agents don't grow from responsibility. The agent that struggled yesterday doesn't exist today. There's no skill accumulation, no confidence building, no "learning by doing."

**This isn't a translation problem - it's a category error.** Applying human delegation psychology to agents is like motivating a compiler.

So what IS delegation for agents?

## Delegation Without Development

Strip away the developmental psychology and delegation becomes:

**Delegation = task assignment + autonomy level + feedback loop**

For humans, the autonomy level starts low and increases as the person develops. For agents, autonomy level is a configuration choice - it doesn't "progress" based on agent experience because agents don't have experience.

| Human Delegation | Agent Delegation |
|------------------|------------------|
| Autonomy increases as delegate develops | Autonomy set by human based on task/risk |
| Trust builds through track record | Trust is permission configuration |
| "Stretch assignments" accelerate growth | No growth to accelerate |
| Delegate remembers past delegations | Each delegation starts fresh |
| Investment in person yields compound returns | No compounding - same effort every time |

**Key insight:** Human delegation is an investment (put in effort now, get multiplied returns later). Agent delegation is an expense (effort in, output out, nothing accumulates).

## What Delegation IS For Agents

If delegation doesn't develop agents, its purpose must be purely operational:

### 1. Capacity Scaling

Humans have 8-10 productive hours. Agents have infinite hours.

| Constraint | Human | Agent |
|------------|-------|-------|
| Time | Limited | Unlimited |
| Parallel work | 1 task (some multitasking) | Many parallel agents |
| Fatigue | Degrades performance | No fatigue |
| Context switching cost | High | Per-agent context, no switching |

**Agent delegation is about capacity, not development.** You delegate to agents because you don't have the hours, not because they need the experience.

### 2. Capability Matching

Some tasks are better suited to agents:

| Agent-suited | Human-suited |
|--------------|--------------|
| Repetitive, pattern-following | Novel, judgment-heavy |
| Large codebase searches | Aesthetic decisions |
| Bulk transformations | Stakeholder negotiation |
| Documentation generation | Strategic prioritization |
| Test writing | User experience evaluation |

**Delegation to agents is about task-capability fit, not employee development.** You match task requirements to agent strengths.

### 3. Human Attention Management

The scarcest resource isn't compute or agent hours - it's human attention.

```
Human attention budget:
- Review agent output: 5 min
- Do the work yourself: 60 min

Net savings: 55 min (if agent output is acceptable)
Net cost: -5 min (if you reject and redo)
```

**Agent delegation is attention arbitrage.** You're trading review time for execution time.

## Delegation Levels: A Different Meaning

Manager Tools' delegation levels map to increasing autonomy:

| Level | Human | Meaning |
|-------|-------|---------|
| 1 | Tell | Do exactly this |
| 2 | Sell | Do this, here's why |
| 3 | Consult | What do you think? I'll decide |
| 4 | Agree | Discuss until we reach consensus |
| 5 | Advise | I recommend, you decide |
| 6 | Inquire | You decide, tell me after |
| 7 | Delegate | You own this area |

For humans, these levels track with development. Junior employees start at 1-2, progress to 6-7 as they grow.

For agents, levels map to **task characteristics**, not agent maturity:

| Level | Agent Equivalent | When to Use |
|-------|------------------|-------------|
| 1-2 | Explicit instructions | Novel domains, high risk |
| 3-4 | N/A (agents don't negotiate) | - |
| 5-6 | Intent-based delegation (Auftragstaktik) | Familiar domains, clear success criteria |
| 7 | Autonomous with monitoring | Routine, bounded, verified |

**Agent delegation levels are task-determined, not agent-earned.**

## Connection: Auftragstaktik (from OODA Loop)

Boyd's concept of Auftragstaktik (intent-based orders) is the right frame for agent delegation:

| Traditional Orders | Auftragstaktik |
|-------------------|----------------|
| "Move to grid X, dig in, engage at time Y" | "Prevent enemy from crossing the river" |
| Specify the HOW | Specify the WHAT and WHY |
| Execute literally | Use judgment on execution |

**Good agent delegation = Auftragstaktik:**

| Micromanaged | Intent-Based |
|--------------|--------------|
| "Edit line 47, change X to Y" | "Fix the race condition in audio handler" |
| "Create file A, then B, then C" | "Add tests for the new feature" |
| "Grep for X, then edit Y" | "Make the naming consistent" |

**Why this matters:** Agents have better visibility into the codebase than the human giving instructions. The human knows the goal; the agent sees the code. Intent-based delegation lets the agent use its visibility.

### When NOT to Use Auftragstaktik

Intent-based delegation requires:
- Clear success criteria
- Bounded scope
- Agent has relevant context

Fails when:
- Success is subjective ("make it better")
- Scope is unbounded ("improve the architecture")
- Agent lacks context ("fix the integration" when agent hasn't seen related systems)

## Connection: Coaching the System (from mt-coaching.md)

Human coaching develops the human. Agent coaching develops the system (human + CLAUDE.md + workflows).

**Delegation quality improves through system coaching, not agent coaching:**

| Improve Delegation By | Mechanism |
|-----------------------|-----------|
| Refining CLAUDE.md | Better agent orientation on delegated tasks |
| Refining task templates | More complete handoff, fewer ambiguities |
| Refining acceptance criteria | Clearer success definition |
| Adjusting trust levels | Better autonomy calibration |

**You don't coach agents to be better at receiving delegation. You coach yourself and your system to be better at delegating.**

## Connection: Feedback to Habit (from mt-feedback.md)

In mt-feedback.md, the key insight is that feedback improves CLAUDE.md (the "habit layer"), not the agent.

**Delegation patterns follow the same logic:**

```
Delegation succeeds
       |
What made it work?
       |
Can this become a template/instruction?
       |
Add to CLAUDE.md or task templates
       |
Future delegations inherit the pattern
```

**Recurring delegation patterns should become CLAUDE.md content.**

Example:
- You delegate "fix bug X" successfully three times
- Each time, you include similar context
- That context pattern should move into CLAUDE.md
- Future delegations need less explicit context

### Delegation-to-CLAUDE.md Pipeline

```
One-off delegation (lots of context in prompt)
           |
           v
Recurring delegation (same context each time)
           |
           v
CLAUDE.md instruction (context pre-loaded)
           |
           v
Implicit delegation (just say "fix it")
```

**Goal state: Delegation that requires no explanation because CLAUDE.md already provides orientation.**

This is Boyd's IG&C (Implicit Guidance and Control) applied to delegation. The agent "just knows" how to handle delegated work because the context is pre-loaded.

## When NOT to Delegate to an Agent

Delegation to agents is wrong when:

### 1. Human Judgment Required

| Task Type | Why Not Agent |
|-----------|---------------|
| Strategic prioritization | Trade-offs are values-based |
| Stakeholder communication | Social/political context |
| Aesthetic decisions | "Taste" isn't computable |
| Novel problem domains | No patterns to match |
| High-stakes irreversible actions | Error cost too high |

### 2. Delegation Overhead Exceeds Task

```
Cost to delegate: 10 min (write context, review output)
Cost to do yourself: 8 min

Don't delegate.
```

Small tasks often fail this test. The overhead of explaining to an agent exceeds the work itself.

### 3. Context Can't Be Externalized

Some tasks require implicit knowledge that can't be written down:

| Implicit Knowledge Type | Example |
|------------------------|---------|
| Organizational politics | "Don't change that - Bob owns it" |
| Historical context | "We tried that in 2019, it failed because..." |
| Taste/style | "That's not how we do things here" |
| Future plans | "This will conflict with next quarter's project" |

If the context can't be made explicit, the agent will make decisions without it.

### 4. Verification Is Harder Than Execution

```
Verification cost > Execution cost
```

If checking agent work takes longer than doing it yourself, delegation fails the economics test.

## Failure Modes

### Over-Delegation

| Symptom | Cause | Fix |
|---------|-------|-----|
| Agent output consistently rejected | Tasks too complex/vague | Better decomposition |
| Agent exceeds scope | Boundaries not explicit | Permission scoping |
| Human becomes reviewer bottleneck | Too much work delegated | Prioritize, reject some tasks |
| Quality degrades | Verification neglected | Maintain sampling |

**Over-delegation to agents looks like:** "I delegated it, so I'm done." No - delegation requires verification investment.

### Under-Delegation

| Symptom | Cause | Fix |
|---------|-------|-----|
| Human capacity exhausted | Doing work agents could do | Identify delegatable tasks |
| Same tasks repeated manually | Not recognizing patterns | Look for automation opportunities |
| Agent capability underutilized | Fear of agent errors | Start at low trust, promote |
| CLAUDE.md underdeveloped | Not learning from delegations | Capture patterns that work |

**Under-delegation to agents looks like:** "It's faster to do it myself." Maybe, but you're not building leverage.

## The Delegation Paradox

Human managers who don't delegate become bottlenecks - their team's output is capped by the manager's capacity.

Agent supervisors face a different paradox:

**Delegation to agents doesn't compound.**

Each delegation is a one-time capacity trade. You trade review time for execution time. But unlike human delegation, the agent doesn't get faster or need less oversight. There's no compounding.

**The compounding happens elsewhere:**
- CLAUDE.md improves (orientation pre-loads)
- Task templates improve (handoff gets cleaner)
- Human gets better at delegating (learns agent capability boundaries)
- Trust calibration improves (right autonomy for right tasks)

**You don't compound agent capability. You compound system capability.**

## Practical Delegation Protocol

### Before Delegating

1. **Task sizing:** Does it fit one context window?
2. **Scope clarity:** Can I state explicit boundaries?
3. **Success criteria:** How will I verify completion?
4. **Context externalization:** Can I write down everything the agent needs?
5. **Economics check:** Is delegation overhead less than execution?

### During Delegation

1. **Intent over procedure:** State the goal, not the steps (Auftragstaktik)
2. **Explicit boundaries:** What files, what actions, what's forbidden
3. **Acceptance criteria:** How agent knows it's done
4. **Escalation path:** What to do if blocked

### After Delegation

1. **Verify output:** Don't assume completion = success
2. **Capture patterns:** What worked? Add to CLAUDE.md?
3. **Adjust trust:** Promote or demote based on outcome?
4. **Clean up:** Remove completed task files

## Delegation as Capacity, Not Investment

The fundamental reframe:

| Human Delegation | Agent Delegation |
|------------------|------------------|
| Investment in people | Operational expense |
| Returns compound | Returns are one-time |
| Development is the point | Output is the point |
| Relationship-building | Transaction |
| Delegate grows | System grows |

**You don't delegate to agents to develop them. You delegate to agents to get things done while investing your actual attention elsewhere.**

The development happens in the system around the agent:
- You get better at delegating
- CLAUDE.md gets better at orienting agents
- Task templates get better at scoping
- Trust calibration gets more accurate

**Agent delegation: transactional for agents, developmental for the system.**

## Open Questions

1. **Delegation discovery:** How do you identify tasks that should be delegated vs. done directly? Is there a heuristic beyond "does it fit context window"?

2. **Delegation queuing:** If you can spawn many agents, how do you prioritize the delegation queue? What's the equivalent of "delegate highest-value first"?

3. **Delegation chains:** When agent A delegates to agent B, how does quality degrade across the chain? Is human-to-agent fundamentally different from agent-to-agent?

4. **Verification economics:** What's the actual ratio of verification cost to delegation savings? Is there empirical data on this?

5. **Delegation templates:** Should there be standardized delegation templates for common task types? Would this reduce overhead enough to change the economics?

6. **Inverse delegation:** Can agents "delegate up" to humans? What does that look like? (Escalation? Questions? Explicit requests for judgment?)

## Systems to Build

- [ ] **Delegation log:** Track what gets delegated, outcome quality, time savings
- [ ] **Task template library:** Standardized delegation formats for common tasks
- [ ] **Verification sampling:** Tool to randomly select delegated outputs for deep review
- [ ] **Delegation economics calculator:** Estimate overhead vs. savings for candidate delegations
- [ ] **CLAUDE.md extraction:** Automatically identify recurring delegation context for promotion to instructions

## The Core Reframe

**Traditional delegation:** Develop people through progressive responsibility.

**Agent delegation:** Scale capacity through task distribution.

The agent doesn't grow. But:
- Human capacity multiplies
- System orientation improves (CLAUDE.md)
- Task scoping improves (templates)
- Trust calibration improves (right autonomy for right tasks)

**Delegation to agents is capacity scaling, not people development. The development happens in the system that creates delegation contexts, not in the agents that receive them.**

## Status

**Phase:** Exploration complete. Key insight is that delegation to agents is transactional (capacity scaling), not developmental (building capability). The compounding happens in CLAUDE.md, task templates, and human delegation skill - not in agents themselves. Auftragstaktik (intent-based orders) is the right frame for agent delegation.
