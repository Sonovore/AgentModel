# Cynefin Framework for Agent Supervision

Exploring how the Cynefin Framework applies to AI agent task assignment and supervision.

## Background

| Aspect | Description |
|--------|-------------|
| **Creator** | Dave Snowden (Cognitive Edge) |
| **Core Insight** | Different situations require fundamentally different approaches |
| **Key Distinction** | You can't analyze your way through every problem |
| **Framework Type** | Sense-making, not categorization |
| **Critical Warning** | Applying the wrong approach for a domain causes failure |

## The Five Domains

```
                    ┌─────────────────┐
                    │    CONFUSED     │
                    │  (Don't know    │
                    │  which domain)  │
                    └────────┬────────┘
                             │
            ┌────────────────┴────────────────┐
            │                                 │
            ▼                                 ▼
    ┌───────────────┐                 ┌───────────────┐
    │    COMPLEX    │                 │  COMPLICATED  │
    │               │                 │               │
    │ Probe-Sense-  │                 │ Sense-Analyze-│
    │   Respond     │                 │    Respond    │
    │               │                 │               │
    │ Cause-effect  │                 │ Cause-effect  │
    │ retrospective │                 │ discoverable  │
    └───────┬───────┘                 └───────┬───────┘
            │                                 │
            │         ┌───────────┐           │
            │         │   CLEAR   │           │
            └────────►│           │◄──────────┘
                      │  Sense-   │
                      │Categorize-│
                      │  Respond  │
                      │           │
                      │ Obvious   │
                      │cause-effect│
                      └─────┬─────┘
                            │
                    (complacent drift)
                            │
                            ▼
                    ┌───────────────┐
                    │    CHAOTIC    │
                    │               │
                    │  Act-Sense-   │
                    │    Respond    │
                    │               │
                    │ No perceivable│
                    │ cause-effect  │
                    └───────────────┘
```

| Domain | Characteristics | Approach | Key Action |
|--------|-----------------|----------|------------|
| **Clear** | Obvious cause-effect, best practices exist | Sense-Categorize-Respond | Apply best practice |
| **Complicated** | Cause-effect discoverable by experts | Sense-Analyze-Respond | Analyze, then act |
| **Complex** | Cause-effect only obvious in hindsight | Probe-Sense-Respond | Experiment first |
| **Chaotic** | No perceivable cause-effect | Act-Sense-Respond | Stabilize immediately |
| **Confused** | Don't know which domain you're in | Gather information | Break down, classify parts |

## The Critical Question for Agent Work

**Before assigning a task to an agent, ask: What domain is this task in?**

The answer determines:
1. How much autonomy to grant
2. What supervision style to use
3. Whether to plan upfront or iterate
4. How to evaluate success

## Domain Identification for Agent Tasks

### Signals That a Task Is Clear

- "Do X the way we always do it"
- Well-documented procedure exists
- Agent has done this successfully many times
- Output format is precisely defined
- Failure modes are known and handled

**Examples:**
- "Add a comment explaining this function"
- "Format this file according to our style guide"
- "Create a standard getter/setter"
- "Run the build and report the result"

### Signals That a Task Is Complicated

- "Figure out the best way to do X"
- Multiple valid approaches exist
- Requires understanding system architecture
- Expert judgment needed on tradeoffs
- Analysis reveals the right answer

**Examples:**
- "Refactor this module to reduce coupling"
- "Optimize this query for performance"
- "Design the API for this feature"
- "Debug this specific, reproducible bug"

### Signals That a Task Is Complex

- "We don't know why this happens"
- Cause-effect relationships are unclear
- System behavior is emergent
- Previous solutions didn't work
- Need to learn more before planning

**Examples:**
- "Figure out why this fails intermittently"
- "Investigate how users actually use this feature"
- "Prototype something to explore the problem space"
- "Find the root cause of this performance degradation"

### Signals That a Task Is Chaotic

- "Everything is broken, fix it now"
- Normal processes have failed
- No time for analysis
- Need to restore stability first
- Understanding comes later

**Examples:**
- "Production is down"
- "Data corruption in progress"
- "Security breach detected"
- "Critical deadline, nothing works"

### Signals That You're Confused

- "I don't know how hard this is"
- Task description is vague
- Could be trivial or impossible
- Multiple interpretations exist
- Need more information to classify

**Examples:**
- "Make the code better"
- "Fix the user experience"
- "This doesn't feel right"
- Unfamiliar codebase, unknown scope

## Supervision Styles by Domain

### Clear Domain Supervision

```
Human: "Do X"
Agent: Does X using established pattern
Human: Spot-check result
```

| Aspect | Approach |
|--------|----------|
| **Autonomy** | High - agent can execute independently |
| **Instructions** | Brief, reference established patterns |
| **Checkpoints** | End of task only |
| **Review Depth** | Light - verify completion |
| **Trust Level** | Delegate and verify |

**Risk:** Treating Clear as simpler than it is. Even "obvious" tasks can have edge cases the agent misses.

### Complicated Domain Supervision

```
Human: "Do X, considering A, B, C"
Agent: Analyzes options, proposes approach
Human: Reviews analysis, approves direction
Agent: Executes approved approach
Human: Reviews implementation
```

| Aspect | Approach |
|--------|----------|
| **Autonomy** | Medium - agent proposes, human approves |
| **Instructions** | Detailed context, constraints, goals |
| **Checkpoints** | After analysis, after implementation |
| **Review Depth** | Medium - evaluate reasoning and result |
| **Trust Level** | Collaborate on approach |

**Risk:** Analysis paralysis. Agent keeps analyzing instead of acting. Human keeps adding constraints instead of deciding.

### Complex Domain Supervision

```
Human: "Explore X, report what you find"
Agent: Probes, observes, reports
Human: Reviews findings, directs next probe
Agent: Probes again with new direction
[Repeat until pattern emerges]
Human: Decides on action based on accumulated learning
```

| Aspect | Approach |
|--------|----------|
| **Autonomy** | Low initially, increases as patterns emerge |
| **Instructions** | Questions to answer, not solutions to implement |
| **Checkpoints** | After each probe cycle |
| **Review Depth** | High - learning is the goal |
| **Trust Level** | Explore together |

**Risk:** Premature convergence. Deciding you understand the pattern before you actually do. Treating Complex like Complicated.

### Chaotic Domain Supervision

```
Human: "Stop the bleeding"
Agent: Acts immediately to stabilize
Human: Confirms stability
Agent: Reports what was done
Human: Decides next steps
```

| Aspect | Approach |
|--------|----------|
| **Autonomy** | Very high for immediate action, then drops |
| **Instructions** | Emergency directive only |
| **Checkpoints** | After immediate action, then continuous |
| **Review Depth** | Post-mortem after stability |
| **Trust Level** | Trust for triage, verify everything |

**Risk:** Staying in chaotic mode after stability returns. Emergency shortcuts become permanent. Also: agent may not recognize what "stable" means without explicit criteria.

### Confused Domain Supervision

```
Human: "What kind of problem is this?"
Agent: Gathers information, reports structure
Human: Classifies sub-problems into domains
Human: Assigns sub-problems with appropriate supervision
```

| Aspect | Approach |
|--------|----------|
| **Autonomy** | Information gathering only |
| **Instructions** | "Explore and report, don't act" |
| **Checkpoints** | Continuous |
| **Review Depth** | Classification is the goal |
| **Trust Level** | Verify classification |

**Risk:** Acting before understanding. The goal is to get OUT of Confused, not to solve the problem while confused.

## Failure Modes: Wrong Domain Treatment

### Treating Complex Like Complicated

**What happens:** You try to analyze your way to a solution before you have enough information.

```
Human: "Debug this intermittent failure"
Agent: [Spends hours analyzing code]
Agent: "Based on my analysis, the problem is X"
[Implements fix]
[Problem still occurs]
[Repeat]
```

**Correct approach:** Probe first. Add logging. Reproduce in controlled conditions. Gather data. Pattern emerges. THEN analyze.

**Agent symptom:** Long, confident analysis that doesn't solve the problem.

### Treating Complicated Like Clear

**What happens:** You apply a standard solution to a problem that requires expert analysis.

```
Human: "Make this faster"
Agent: [Applies generic optimization patterns]
[Performance unchanged or worse]
```

**Correct approach:** Profile first. Identify actual bottleneck. Design solution for THIS system.

**Agent symptom:** "Best practice" solutions that don't fit the specific context.

### Treating Clear Like Complicated

**What happens:** Over-analysis of a simple task. Wasted time.

```
Human: "Add a null check here"
Agent: "Let me analyze all the places this function is called,
       consider the architectural implications,
       evaluate three different approaches..."
```

**Correct approach:** Just add the null check.

**Agent symptom:** Excessive analysis, asking many clarifying questions for trivial tasks.

### Treating Chaotic Like Anything Else

**What happens:** You try to understand/analyze/plan while the house is on fire.

```
Human: "Production is down!"
Agent: "Let me analyze the codebase to understand
       the architecture before making changes..."
```

**Correct approach:** Act to stabilize. Understand later.

**Agent symptom:** Inappropriate process-following during emergencies.

## Boundary Dynamics

Cynefin domains have important boundary transitions that apply to agent work.

### Complacent Drift: Clear to Chaotic

Systems in the Clear domain can catastrophically collapse into Chaos if:
- Best practices become stale
- Edge cases accumulate unhandled
- Assumptions become invalid

**Agent implication:** Tasks you've "always done this way" can suddenly fail catastrophically. Complacency about Clear tasks is dangerous.

**Mitigation:** Periodic review of "always works" tasks. Monitor for new failure modes.

### Emergence: Complex to Complicated

As you probe in the Complex domain, patterns emerge. Eventually you understand enough to analyze. The problem moves to Complicated.

**Agent implication:** Don't stay in probe-mode forever. Recognize when you have enough information to shift to analysis.

**Signal:** Probes start returning predictable results. You can explain what happened BEFORE it happens.

### Stabilization: Chaotic to Complex

After emergency action restores stability, you're in Complex. You don't understand what happened yet, but you have time to probe.

**Agent implication:** After fixing an emergency, don't immediately return to normal operations. Investigate.

**Signal:** Immediate danger passed. System is functional but not understood.

## Agent-Specific Considerations

### Agents Default to Complicated Treatment

Agents naturally want to:
1. Gather context
2. Analyze options
3. Propose solution
4. Execute

This is the Complicated approach. It's wrong for Clear (wasted effort) and Complex (premature analysis) and Chaotic (too slow).

**Implication:** Explicitly tell agents which domain they're operating in. Don't let them default to Sense-Analyze-Respond.

### Agents Struggle with Complex Domain

The Probe-Sense-Respond cycle requires:
1. Acting without a plan
2. Observing results
3. Learning from observation
4. Deciding next probe based on learning

Agents are better at executing plans than iterating toward understanding. They may:
- Probe once and immediately analyze
- Treat initial observations as definitive
- Not know when to stop probing

**Mitigation:** Human drives the probe cycle. Agent executes probes and reports raw observations. Human decides when enough is known.

### Agents Need Explicit Chaotic Mode Permission

Agents follow instructions carefully. In Chaotic domain, you need to break things:
- Skip tests
- Make risky changes
- Act before understanding

**Mitigation:** Explicit permission: "We're in emergency mode. Do whatever stops the bleeding. We'll clean up later."

### Confusion Is Human's Job

The Confused domain requires meta-judgment: "What kind of problem is this?" This is hard to delegate.

**Implication:** Human must recognize when they're confused and resist assigning tasks until they've classified the domain.

## Practical Decision Flow

```
┌─────────────────────────────────────────────────────────────┐
│                  RECEIVING A NEW TASK                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ Do I understand │
                    │ what "done"     │
                    │ looks like?     │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼ No                          ▼ Yes
    ┌─────────────────┐          ┌─────────────────┐
    │    CONFUSED     │          │ Is there a      │
    │                 │          │ known working   │
    │ Gather info,    │          │ approach?       │
    │ break down,     │          └────────┬────────┘
    │ classify parts  │                   │
    └─────────────────┘        ┌──────────┴──────────┐
                               │                     │
                               ▼ Yes                 ▼ No
                     ┌─────────────────┐   ┌─────────────────┐
                     │     CLEAR       │   │ Is cause-effect │
                     │                 │   │ discoverable    │
                     │ Apply the       │   │ through         │
                     │ known approach  │   │ analysis?       │
                     └─────────────────┘   └────────┬────────┘
                                                    │
                                         ┌──────────┴──────────┐
                                         │                     │
                                         ▼ Yes                 ▼ No
                               ┌─────────────────┐   ┌─────────────────┐
                               │   COMPLICATED   │   │ Is system       │
                               │                 │   │ currently       │
                               │ Analyze, then   │   │ stable?         │
                               │ act             │   └────────┬────────┘
                               └─────────────────┘            │
                                                   ┌──────────┴──────────┐
                                                   │                     │
                                                   ▼ Yes                 ▼ No
                                         ┌─────────────────┐   ┌─────────────────┐
                                         │     COMPLEX     │   │     CHAOTIC     │
                                         │                 │   │                 │
                                         │ Probe to learn, │   │ Act to          │
                                         │ then respond    │   │ stabilize       │
                                         └─────────────────┘   └─────────────────┘
```

## Task Type Tendencies (Not Rules)

Different task types tend toward different domains, but context can shift them.

| Task Type | Typical Domain | But Sometimes... |
|-----------|----------------|------------------|
| Add comment | Clear | Confused if you don't understand the code |
| Bug fix (reproducible) | Complicated | Complex if root cause unclear |
| Bug fix (intermittent) | Complex | Complicated once pattern found |
| New feature (spec'd) | Complicated | Complex if requirements unclear |
| New feature (exploratory) | Complex | Complicated once direction clear |
| Refactoring | Complicated | Clear if pattern is mechanical |
| Production incident | Chaotic initially | Complex after stabilization |
| Performance optimization | Complicated | Complex if bottleneck unknown |
| Research | Complex | Complicated once approach chosen |

**Key insight:** Domain is about what you know, not what the task is. The same task can be Clear for an expert and Complicated for a novice.

## Mapping to Autonomy Levels

Cynefin domains map to appropriate autonomy:

| Domain | Autonomy Level | Rationale |
|--------|----------------|-----------|
| Clear | High | Best practice exists, just execute |
| Complicated | Medium | Need human judgment on analysis |
| Complex | Variable | High for probes, low for interpretation |
| Chaotic | High then Low | Emergency authority, then tight control |
| Confused | Low | Classification is human's job |

## Cynefin + OODA Loop

If you're also using OODA (Observe, Orient, Decide, Act), Cynefin tells you how to use it:

| Domain | OODA Emphasis |
|--------|---------------|
| Clear | Minimal O-O-D, heavy A (just act) |
| Complicated | Heavy O-O-D, careful A |
| Complex | Rapid OODA cycles (probe-observe-probe) |
| Chaotic | A first, then O-O-D |
| Confused | O-O only (don't decide or act yet) |

## Summary: Domain-Appropriate Supervision

| Domain | Question to Ask Agent | Instruction Pattern |
|--------|----------------------|---------------------|
| Clear | "Do X using standard approach" | Brief, procedural |
| Complicated | "Analyze X, propose approach, await approval" | Detailed context, explicit approval gate |
| Complex | "Probe X, report observations, await next direction" | Questions, not solutions |
| Chaotic | "Stabilize X immediately, report actions taken" | Emergency override, action-first |
| Confused | "Gather information about X, report structure" | Exploration only, no action |

## The Core Reframe

**Traditional task assignment:** "Here's the task, go do it."

**Cynefin-informed task assignment:** "Here's the task. It's in the [domain] domain. Use [approach]."

The domain determines EVERYTHING about how to work:
- How much planning to do (a lot vs. none)
- When to act (after analysis vs. immediately)
- What success looks like (execution vs. learning)
- How to supervise (spot-check vs. continuous)

**If you don't know the domain, you can't supervise correctly.** And if you apply the wrong supervision style, you'll fail - not because the agent failed, but because you set up the wrong process.

## Open Questions

1. **Can agents self-identify domain?** Should they? Or is that always human judgment?

2. **Domain disagreement:** What if agent thinks task is Clear but human thinks it's Complex?

3. **Domain transition:** How do you recognize when a task has moved from Complex to Complicated? What signals this?

4. **Multi-domain tasks:** Large tasks may span multiple domains. How to decompose along domain boundaries?

5. **Domain-specific prompting:** Should CLAUDE.md have different instruction sets for different domains?

6. **Probe design:** In Complex domain, what makes a good probe vs. a bad probe?

7. **Chaotic recovery:** How do you know when stability is restored and you can move to Complex?

## Systems to Build

- [ ] **Domain classifier:** Checklist/decision tree to identify task domain
- [ ] **Domain-specific instruction templates:** Pre-built prompts for each domain
- [ ] **Transition detector:** Signals that domain has shifted
- [ ] **Probe library:** Reusable probes for common Complex situations
- [ ] **Emergency playbook:** Chaotic domain response patterns

## Status

**Phase:** Initial exploration complete. Core framework mapped to agent supervision. The key insight is that domain determines supervision style - you can't use one approach for all tasks. Most failures come from domain misidentification, not execution problems.

