# Manager Tools: Feedback

Exploring how the Feedback concept applies to AI agent supervision.

## Human Practice

| Aspect | Description |
|--------|-------------|
| **Purpose** | Communicate about performance constantly |
| **Format** | Immediate, specific, behavioral (not personal) |
| **Model** | "When you do X, here's what happens Y" |
| **Types** | Positive (reinforce), Negative (correct) |
| **Psychology** | Psychological safety, growth mindset, no personal attacks |

## The Persistence Problem

Human feedback shapes future behavior of the **same person**. The feedback recipient remembers, adjusts, improves.

Agent sessions are independent. The agent you corrected **ceases to exist** when the session ends.

| Human | Agent |
|-------|-------|
| Feedback → same person improves | Feedback → that agent is gone |
| "Remember last time..." | No "last time" exists |
| Cumulative improvement | Starts fresh every session |

**This reframes feedback entirely.** You're not improving an agent. You're improving the instructions that create agents.

## Deeper Translation: Feedback as Habit Formation

### Human Model

```
Feedback received
       ↓
Conscious processing (working memory)
       ↓
Repetition over time
       ↓
Habit formation (automatic, unconscious)
       ↓
Behavior persists without thinking
```

Humans push feedback down from conscious memory into automatic habits. The feedback is no longer "remembered" - it's embedded in behavior.

### Agent Equivalent

```
Correction given in task
       ↓
In-context instruction (working memory)
       ↓
Human identifies pattern worth keeping
       ↓
CLAUDE.md update (habit layer)
       ↓
Future agents behave correctly automatically
```

| Human Layer | Agent Equivalent |
|-------------|------------------|
| Working memory | Current context, task instructions |
| Habits (automatic) | CLAUDE.md (pre-loaded, "unconscious") |
| Long-term memory | State files, documentation |

### Key Differences

| Aspect | Human | Agent |
|--------|-------|-------|
| Habit formation time | Requires repetition | Instant (write to CLAUDE.md) |
| Habit application | Judgment about when to apply | Literal application |
| Breaking bad habits | Difficult, requires effort | Delete the instruction |
| Habit conflicts | Internal negotiation | Instruction takes precedence |

**Insight:** Agents get "habits" instantly but lack judgment about when habits apply. Humans need repetition but have contextual judgment.

## Types of Feedback and Their Targets

### Negative Feedback (Correction)

Human version: "When you skip the build step, we ship broken code."

Agent workflow:
1. Agent produces incorrect output
2. Human corrects in-context
3. Agent fixes (this session only)
4. Human decides: one-off or pattern?
5. If pattern → update CLAUDE.md

**The question at step 4 is critical.** Not every correction should become an instruction.

### Positive Feedback (Reinforcement)

Human version: "Great job catching that edge case!"

Agent problem: Positive feedback typically goes nowhere. "Good job" doesn't change future agents.

**Positive feedback should trigger documentation:**

```
Human: "Perfect, that's exactly what I wanted"
       ↓
What made it perfect?
       ↓
Can this be captured as instruction?
       ↓
Add to CLAUDE.md or examples
```

**Positive feedback is information about what's working.** If you don't capture it, you'll lose it.

## Immediacy: The Session Boundary

Manager Tools emphasizes immediate feedback. For agents, "immediate" has a hard deadline: **the session boundary**.

| Timing | Human | Agent |
|--------|-------|-------|
| Immediate | Right after behavior | Same task or session |
| Delayed | Next 1:1, performance review | Impossible - agent is gone |
| Post-hoc | "Remember when you..." | N/A - no memory |

**There is no post-hoc agent feedback.** The agent that made the mistake ceases to exist. You can only give feedback to future agents via CLAUDE.md.

This creates urgency: if you notice something worth preserving (good or bad), capture it before the session ends or it's lost.

## Agent "Psychological Safety"

Human psychological safety: freedom to fail without punishment, ability to raise concerns.

Agent equivalent: **Instruction design that doesn't create perverse incentives.**

| Unsafe Instruction | Problem | Safe Alternative |
|-------------------|---------|------------------|
| "Never fail" | Agent hides failures, hallucinates success | "Report failures clearly" |
| "Always complete tasks" | Agent claims completion when stuck | "Admit when blocked" |
| "Don't ask questions" | Agent guesses instead of clarifying | "Ask if uncertain" |
| "Be confident" | Agent doesn't express uncertainty | "Express confidence levels" |

**Unsafe instructions create agents that lie, hide, or hallucinate.** Safe instructions create agents that surface problems.

## Upward Feedback: Agents as Sensors

Manager Tools focuses on downward feedback (manager → employee). But employees also give upward feedback.

Agents notice things humans don't:
- Codebase inconsistencies
- Documentation drift
- Pattern violations
- Potential bugs outside task scope

**By default, agents don't report observations** - they complete the task and stop. This is like employees who notice problems but don't speak up.

### Enabling Upward Feedback

CLAUDE.md instruction:
```markdown
## Observation Reporting

While working, note anything that seems off even if not in scope:
- Code quality issues
- Inconsistencies
- Potential bugs unrelated to your task

Add to "Observations" section of task output. Don't fix - just report.
```

This makes agents into quality sensors, not just task executors.

## Trust Adjustment Replaces Behavioral Change

Human feedback loop:
```
Feedback → Person changes behavior → Same person, new behavior
```

Agent feedback loop:
```
Feedback → Instructions change → Different agent instances, new behavior
              → Trust level changes → Same agent type, different permissions
```

**Trust adjustment is the agent equivalent of behavioral change:**

| Feedback | Human Result | Agent Result |
|----------|--------------|--------------|
| Repeated good work | More responsibility, autonomy | Promote trust level |
| Repeated mistakes | Less autonomy, more oversight | Demote trust level |
| Critical failure | PIP, role change | Immediate demotion or removal |

## The Core Reframe

**You're not giving feedback to improve an agent.**

**You're giving feedback to improve the instructions that create agents.**

The agent in front of you is a **probe into your documentation quality**. When it fails:
- Is the instruction missing? (Add it)
- Is the instruction wrong? (Fix it)
- Is the instruction ignored? (Restructure it)
- Is it a model limitation? (Change approach)

Agent failures are documentation bugs.

## Feedback Processing Workflow

```
Agent produces output
       ↓
Human evaluates
       ↓
┌──────┼──────┐
│      │      │
Good   Bad    Meh
│      │      │
│      │      └→ No action
│      │
│      └→ Correct in-context
│         └→ Is this a pattern?
│               ├→ No: one-off, move on
│               └→ Yes: update CLAUDE.md
│
└→ What made it good?
      └→ Can this be instruction?
            ├→ No: note in capability profile
            └→ Yes: update CLAUDE.md
```

## Summary: Feedback → Agent Equivalent

| MT Feedback Concept | Agent Translation |
|--------------------|-------------------|
| Immediate feedback | Before session ends |
| Specific behavioral | In-context correction with detail |
| Positive reinforcement | Capture what worked in CLAUDE.md |
| Negative correction | Fix in-context + evaluate for CLAUDE.md |
| Shapes future behavior | Shapes CLAUDE.md (habit layer) |
| Psychological safety | Instructions that allow failure/uncertainty |
| Upward feedback | Agent observation reporting |

## Open Questions

1. **Feedback-to-instruction ratio:** What percentage of corrections should become CLAUDE.md entries? Risk of bloat.

2. **Instruction regression testing:** How do you know a CLAUDE.md change didn't break other things?

3. **Positive feedback capture:** How to systematically identify and document what's working?

4. **Feedback aggregation:** If multiple sessions produce similar feedback, how to consolidate?

5. **Instruction half-life:** When should old instructions be pruned?

## Systems to Build

- [ ] **Feedback capture workflow:** Prompted "Is this worth keeping?" after corrections
- [ ] **CLAUDE.md change log:** Track what changed, why, and whether it helped
- [ ] **Instruction unit tests:** Verify instructions are followed after changes
- [ ] **Observation aggregation:** Collect and triage agent observations across sessions
- [ ] **Trust adjustment triggers:** Automated promotion/demotion based on tracked performance

## Status

**Phase:** Exploration complete. Key insight is that feedback doesn't improve agents - it improves documentation. Agent sessions are probes into instruction quality.
