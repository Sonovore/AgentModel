# Agent Management Framework

Mapping Manager Tools' management principles to AI agent supervision. This document identifies where human vs. agent management differs and provides practical implementation guidance.

## Overview

Manager Tools' "Trinity + Delegation" framework has been refined over decades for human management. Some principles translate directly to agent supervision; others require significant adaptation; some don't apply at all.

**Key insight:** Agents need *more structure* and *less motivation* than humans. The opposite of what most managers struggle with.

---

## 1. One-on-Ones → Context & State Management

### The Human Practice

| Aspect | Human Management |
|--------|------------------|
| **Purpose** | Build relationship, understand concerns, career growth |
| **Format** | 30 min weekly, 10/10/10 (their agenda/your agenda/future) |
| **Psychology** | Creates psychological safety, shows investment |
| **Outcome** | Manager "knows their people exceptionally well" |

### Why It Works for Humans

- Humans have implicit organizational knowledge that erodes without reinforcement
- Relationships require ongoing maintenance
- Concerns/blockers often go unspoken without a dedicated forum
- Career growth requires regular guidance and feedback

### Agent Translation

| Aspect | Agent Management |
|--------|------------------|
| **Purpose** | Maintain context continuity, prevent information loss |
| **Format** | State files, handoff protocols, context.md |
| **Mechanism** | Explicit state serialization, not implicit relationship |
| **Outcome** | Agent has necessary context to continue work |

### Key Differences

| Human | Agent |
|-------|-------|
| Relationship-building | Context preservation |
| Implicit knowledge | Explicit state files |
| "How are you feeling?" | "What is your current state?" |
| Weekly cadence | Every session boundary |
| Can ask clarifying questions | Must have context upfront |
| Remembers across conversations | Starts fresh each session |

### Implementation

**State files (from [agent-task-system.md](agent-task-system.md)):**
```
.claude/
├── context.md          # Short-term memory (session → session)
├── tasks.md            # Long-term backlog
└── agents/
    └── operator-001/
        └── state.md    # Agent's working memory
```

**Handoff protocol:**
1. Before session end: Run `/handoff-context`
2. Agent writes: Immediate issues, in-progress work, next steps
3. Next session: Agent reads context.md, resumes with full state

**context.md structure:**
```markdown
# Session Context

## Immediate
(Blockers, things needing attention NOW)

## In Progress
(Current work, active task state)

## Recent Completions
(What just finished, relevant for continuity)

## Next Steps
(Recommended actions)
```

### Edge Cases

- **Context rot:** If context.md isn't updated, subsequent sessions start blind
- **Over-documentation:** Too much context = noise; agent ignores critical info
- **Missing implicit knowledge:** Humans share organizational context automatically; agents need it explicit

### Anti-patterns

- Expecting agents to "remember" anything not in state files
- Treating context.md as a diary instead of actionable state
- Skipping handoff because "it was a small task"

---

## 2. Feedback → Output Validation & Correction

### The Human Practice

| Aspect | Human Management |
|--------|------------------|
| **Purpose** | Communicate about performance constantly |
| **Format** | Immediate, specific, behavioral (not personal) |
| **Types** | Positive (reinforce), negative (correct) |
| **Psychology** | Psychological safety, growth mindset |
| **Outcome** | Continuous performance calibration |

### Why It Works for Humans

- Humans respond to social feedback (approval/disapproval)
- Delayed feedback loses impact (can't remember context)
- Behavioral focus prevents defensiveness
- Positive feedback motivates repetition

### Agent Translation

| Aspect | Agent Management |
|--------|------------------|
| **Purpose** | Verify output quality, catch errors before they propagate |
| **Format** | Verification gates, quality checks, automated validation |
| **Types** | Pass/fail, specific corrections, requirement gaps |
| **Mechanism** | Explicit checking, not social pressure |
| **Outcome** | Output meets requirements before acceptance |

### Key Differences

| Human | Agent |
|-------|-------|
| "Great job on the presentation!" | Build passed: ✓ |
| "Next time, try..." | Error: Missing null check at line 47 |
| Needs psychological safety | Can be prescriptive |
| May get defensive | No emotional response |
| Feedback shapes future behavior | Feedback shapes *this* output only |
| Intrinsic motivation matters | Instructions are motivation |

**Critical difference:** Human feedback shapes *future* behavior. Agent feedback shapes *current* output. Agents don't "learn" from feedback in a session—they comply or don't.

### Implementation

**Verification agents (from [agent-types.md](agent-types.md)):**

| Agent | Purpose | Output |
|-------|---------|--------|
| Reviewer | Code quality check | Issues, suggestions, approval |
| Verifier | Requirements check | Pass/fail per requirement |
| Tester | Test execution | Test results, coverage |

**Quality gates:**
```
Agent output
    ↓
Automated checks (build, lint, tests)
    ↓
Verifier agent (optional)
    ↓
Human review (required at trust levels 0-2)
    ↓
Accept or correct
```

**Correction pattern:**
```markdown
## Output Rejected

**Issue:** Function lacks error handling for null input
**Location:** Core/Src/process.c:147
**Required fix:** Add null check before dereferencing

Resubmit after correction.
```

### Edge Cases

- **False positives:** Overly strict verification rejects valid output
- **False negatives:** Verification misses actual issues
- **Feedback loops:** Agent "learns" wrong lesson if verifier has bugs
- **Verification overhead:** Too many gates = bottleneck

### Anti-patterns

- Praising agents ("Great job!") — wastes tokens, no effect
- Vague feedback ("This doesn't look right") — agents need specifics
- Delayed feedback (after several tasks) — agents don't connect feedback to past work
- Emotional framing ("I'm disappointed") — no effect, confuses the model

---

## 3. Coaching → Capability Refinement

### The Human Practice

| Aspect | Human Management |
|--------|------------------|
| **Purpose** | Regularly ask for improved performance |
| **Format** | Goal-driven skill development, 5 min/week |
| **Focus** | Long-term capability building |
| **Psychology** | Growth mindset, mastery motivation |
| **Outcome** | Employee becomes more capable over time |

### Why It Works for Humans

- Humans can learn and improve with practice
- Skills compound over time
- Mastery is intrinsically motivating
- Investment in growth builds loyalty

### Agent Translation

| Aspect | Agent Management |
|--------|------------------|
| **Purpose** | Improve output quality through better instructions |
| **Format** | CLAUDE.md refinement, prompt engineering |
| **Focus** | Instruction optimization, not agent "growth" |
| **Mechanism** | Better prompts = better output |
| **Outcome** | System produces better results |

### Key Differences

| Human | Agent |
|-------|-------|
| "Practice this skill" | Refine instructions in CLAUDE.md |
| Skills develop over time | Instructions apply immediately |
| Remembers past coaching | Starts fresh each session |
| Can generalize learnings | Only follows explicit instructions |
| Intrinsic motivation to improve | No desire to improve |
| Career progression | No career |

**Critical insight:** You don't coach agents—you refine their instructions. An agent doesn't "get better at testing" through practice. You write better testing instructions.

### Implementation

**CLAUDE.md refinement cycle:**
```
1. Agent produces output
2. Identify systematic issues (not one-offs)
3. Update CLAUDE.md with explicit guidance
4. Test on new tasks
5. Iterate
```

**Example refinement:**

Before:
```markdown
## Testing
Write tests for new code.
```

After (refined through observation):
```markdown
## Testing
- Write tests BEFORE marking implementation complete
- Test edge cases: null input, empty collections, boundary values
- Verify tests actually fail when code is broken (mutation testing mindset)
- Integration tests for any cross-module changes
```

**Agent type specialization (from [agent-types.md](agent-types.md)):**

Instead of coaching one agent to be better at everything:
- Use Implementer for code writing
- Use Tester for test writing
- Use Reviewer for code review

Specialized instructions > general coaching.

### Edge Cases

- **Over-specification:** CLAUDE.md becomes so detailed it's ignored
- **Contradictory instructions:** New guidance conflicts with old
- **Context-dependent behavior:** What works in one area fails in another
- **Model limitations:** Some improvements require model upgrade, not better prompts

### Anti-patterns

- Expecting agents to "remember" coaching from previous sessions
- Treating CLAUDE.md updates as "feedback" to the agent
- Trying to develop agent "skills" through repetition
- Assuming agents will generalize from examples

---

## 4. Delegation → Task Assignment & Autonomy Levels

### The Human Practice

| Aspect | Human Management |
|--------|------------------|
| **Purpose** | Push work down to develop organizational capability |
| **Format** | Assign tasks with appropriate autonomy level |
| **Psychology** | Growth through challenge, trust-building |
| **Outcome** | Team capability increases over time |

### Why It Works for Humans

- Humans grow through stretch assignments
- Delegation builds trust (both directions)
- Autonomy is motivating
- Manager capacity scales through delegation

### Agent Translation

| Aspect | Agent Management |
|--------|------------------|
| **Purpose** | Execute work within defined boundaries |
| **Format** | Task assignment with explicit permission scope |
| **Mechanism** | Hard permission boundaries, not judgment |
| **Outcome** | Work completed within guardrails |

### Key Differences

| Human | Agent |
|-------|-------|
| "Use your judgment" | Explicit permission boundaries |
| Grows from challenge | No growth from challenge |
| Builds trust over time | Trust defined by permission level |
| Can ask clarifying questions mid-task | Must have context upfront |
| Managers delegate to develop people | Humans delegate for capacity |
| Risk: employee makes bad judgment call | Risk: agent exceeds boundaries |

**Critical difference:** Human delegation develops *people*. Agent delegation scales *capacity*. The goal isn't agent growth—it's human bandwidth.

### Implementation

**Task scoping (from [agent-task-system.md](agent-task-system.md)):**

Task must fit in one context window. Sizing heuristics:
- Can be described completely in <500 words
- Touches <10 files
- Has clear acceptance criteria
- No "investigate then decide" steps

**Permission scoping:**
```markdown
## Permissions for Task 001

- May read: Core/Src/display/*.c, Core/Inc/display/*.h
- May modify: Core/Src/display/tft.c only
- May NOT: Create new files, modify headers, run destructive git commands
- Build: Required before marking complete
- Tests: Run display_tests, must pass
```

**Task Breakdown pattern:**
```
Large goal
    ↓
Task Breakdown agent
    ↓
Discrete tasks (each fits context window)
    ↓
Human validates scope
    ↓
Assign to Implementer agents
```

### Edge Cases

- **Scope creep:** Agent interprets task broadly, touches unintended areas
- **Under-scoping:** Task too small, overhead exceeds value
- **Blocking dependencies:** Task can't complete without information from another task
- **Permission gaps:** Agent needs access it wasn't granted

### Anti-patterns

- Delegating for "agent development" (agents don't develop)
- Vague task boundaries ("improve the display code")
- No permission scoping ("just fix it")
- Expecting agents to ask when stuck (they may hallucinate instead)

---

## 5. Where the Mapping Breaks Down

These human management concepts have **no agent equivalent**:

### Trust Building

| Human | Agent |
|-------|-------|
| Trust grows through demonstrated reliability | Trust is a configuration setting |
| Betrayed trust damages relationship | Permission revocation is instant |
| Takes time to rebuild | Reset by changing settings |

**Implication:** Don't "build trust" with agents. Define trust levels and permission boundaries upfront.

### Motivation

| Human | Agent |
|-------|-------|
| Intrinsic motivation matters | No motivation concept |
| Recognition, growth, purpose | Instructions are "motivation" |
| Can be demoralized | Cannot be demoralized |

**Implication:** Don't try to motivate agents. Write clear instructions.

### Career Development

| Human | Agent |
|-------|-------|
| Has career aspirations | No career |
| Benefits from growth opportunities | Doesn't grow |
| Retention matters | No retention concept |

**Implication:** Don't plan agent "career paths."

### Interpersonal Dynamics

| Human | Agent |
|-------|-------|
| Team dynamics matter | No team dynamics |
| Communication styles vary | Communication is prompt/response |
| Personality conflicts possible | No personality |

**Implication:** Focus on task handoff, not "team cohesion."

---

## 6. Where Agents Need MORE Than Humans

Agents require things humans get implicitly:

### Explicit Context

| Human | Agent |
|-------|-------|
| Absorbs organizational context | Needs everything explicit |
| Asks questions naturally | May hallucinate if context missing |
| Has domain expertise | Only knows what's in prompt |

**Implication:** Over-communicate context. Include:
- Relevant code paths
- Acceptance criteria
- Non-obvious constraints
- Links to related tasks

### Hard Permission Boundaries

| Human | Agent |
|-------|-------|
| Uses judgment for edge cases | Follows permissions literally |
| Can justify boundary-crossing | Will cross boundaries if instructions allow |
| Social consequences for violations | No social consequences |

**Implication:** Define explicit boundaries. Never rely on agent "judgment" for safety.

### Precise Task Scoping

| Human | Agent |
|-------|-------|
| Can handle ambiguity | Ambiguity → hallucination or wrong path |
| Asks clarifying questions | May not realize clarification needed |
| Can pivot mid-task | Context window limits mid-task pivots |

**Implication:** Fully scope tasks before assignment. Include "if X, then Y" branches.

### State Persistence

| Human | Agent |
|-------|-------|
| Remembers across conversations | Starts fresh each session |
| Builds mental model over time | Mental model = current context only |
| Can recall past decisions | Past decisions must be in state files |

**Implication:** Serialize everything important. If it's not written down, it doesn't exist.

---

## 7. Autonomy Levels

Defining how much independence an agent gets based on demonstrated reliability.

### Level Definitions

| Level | Human Analog | Agent Behavior | Trust Required | Review Required |
|-------|--------------|----------------|----------------|-----------------|
| **0** | New hire shadowing | Agent observes, human executes | None | N/A |
| **1** | Junior asking for approval | Agent suggests, human decides | Minimal | Every action |
| **2** | Mid-level with review | Agent acts, human approves before commit | Moderate | Before commit |
| **3** | Senior with spot checks | Agent acts, human monitors async | High | Sampling only |
| **4** | Trusted expert | Agent autonomous within boundaries | Very high | Exceptions only |

### Level 0: Observer

**Agent behavior:** Watches human work, may suggest but never executes.

**Use case:**
- New agent type being evaluated
- High-risk domain (production, security)

**Human analog:** Day-one employee shadowing

**Failure mode:** N/A (agent doesn't act)

### Level 1: Suggester

**Agent behavior:** Proposes actions, human approves each one.

**Use case:**
- Initial deployment of new agent type
- Unfamiliar codebase areas
- Learning what the agent does well/poorly

**Human analog:** Junior asking "Should I do X?"

**Failure mode:** Bad suggestions waste human time

**Example:**
```
Agent: I suggest adding null check at line 147
Human: Approved, proceed
Agent: Done. Next, I suggest refactoring the loop...
Human: No, skip that
```

### Level 2: Actor with Review

**Agent behavior:** Executes task, human reviews before permanent changes.

**Use case:**
- Standard implementation work
- Agents that have proven reliable at Level 1
- Any work touching critical paths

**Human analog:** PR review required

**Failure mode:** Approval fatigue → rubber-stamping

**Example:**
```
Agent: Task complete. Changes staged:
- Core/Src/display/tft.c: Added null check
- Build: Passed
Ready for review.
```

### Level 3: Autonomous with Monitoring

**Agent behavior:** Executes and commits, human monitors asynchronously.

**Use case:**
- Routine tasks in well-understood areas
- High-volume work where review bottlenecks
- Agents with strong track record

**Human analog:** Senior engineer with spot-checks

**Failure mode:** Missed errors compound over time

**Example:**
```
Agent: [Running in background]
Agent: Completed 5 tasks, committed changes
Agent: Summary: [list of changes]
Human: [Reviews later, finds issue in task 3]
```

### Level 4: Fully Autonomous

**Agent behavior:** Plans and executes within defined boundaries, escalates only on boundary violations or blockers.

**Use case:**
- Mature agent types with proven reliability
- Well-bounded domains (test writing, documentation)
- Emergency capacity scaling

**Human analog:** Trusted expert, minimal oversight

**Failure mode:** Boundary violations, drift from goals

**Example:**
```
Human: Fix all display bugs in the backlog
Agent: [Reads backlog, plans approach]
Agent: [Executes 12 tasks over 4 hours]
Agent: Complete. 10 fixed, 2 blocked (need hardware access)
```

---

## 8. Trust Progression

How agents move between autonomy levels.

### Promotion Criteria

| From → To | Criteria | Evidence Required |
|-----------|----------|-------------------|
| 0 → 1 | Agent produces reasonable suggestions | 5+ valid suggestions reviewed |
| 1 → 2 | Suggestions consistently correct | 10+ approved without modification |
| 2 → 3 | No critical issues in reviews | 20+ reviews with no rollbacks |
| 3 → 4 | Extended autonomous operation without issues | 50+ tasks without intervention |

### Demotion Triggers

| Severity | Trigger | Action |
|----------|---------|--------|
| Minor | Output needs correction | Note for trend tracking |
| Moderate | Review catches bug that would have shipped | Note; 3+ → demotion |
| Serious | Boundary violation | Immediate demotion to Level 1 |
| Critical | Security issue, data loss | Immediate demotion to Level 0 |

### Validation Mechanisms

**At each level:**

| Level | Validation | Frequency |
|-------|------------|-----------|
| 1 | Human reviews every suggestion | 100% |
| 2 | Human reviews every output | 100% |
| 3 | Automated checks + sampling | 20-50% human review |
| 4 | Automated checks + exception monitoring | <10% human review |

### Regression Handling

When an agent at Level 3+ starts failing:

1. **Detect:** Monitoring catches increased error rate
2. **Assess:** Is this task-specific or general degradation?
3. **Demote:** Drop to Level 2 for the affected task type
4. **Investigate:** Why did quality drop? (prompt drift, task complexity, model behavior)
5. **Remediate:** Update instructions, scope boundaries, or validation
6. **Re-promote:** After demonstrating recovery

---

## 9. Failure Modes

What can go wrong in agent management and how to detect/prevent it.

### Context Loss

**Description:** Agent loses critical information across session boundaries.

**Symptoms:**
- Agent re-asks questions that were already answered
- Agent makes changes that contradict previous decisions
- Work quality degrades over multi-session tasks

**Causes:**
- Handoff not executed before session end
- context.md not read at session start
- Context too verbose (critical info buried)

**Prevention:**
- Enforce `/handoff-context` before `/clear`
- Startup checklist reads context.md
- Keep context.md focused (not a diary)

**Detection:**
- Agent asks "what should I do?" when task is in progress
- Changes conflict with documented decisions

### Goal Misalignment

**Description:** Agent optimizes for the wrong thing.

**Symptoms:**
- Task marked "complete" but requirements not met
- Agent takes unexpected path to completion
- Output technically correct but practically useless

**Causes:**
- Vague acceptance criteria
- Metrics that don't capture actual goal
- Underspecified constraints

**Prevention:**
- Explicit acceptance criteria for every task
- Verifier agent checks requirements
- Human review at Level 2+

**Detection:**
- Verifier fails tasks that agent marked complete
- Human review finds systematic gaps

### Permission Creep

**Description:** Agent requests or assumes more access than needed.

**Symptoms:**
- Agent modifies files outside stated scope
- Agent requests broad permissions "just in case"
- Scope of changes expands from original task

**Causes:**
- Permissions not explicitly bounded
- Agent "helpfully" fixing adjacent issues
- Vague task boundaries

**Prevention:**
- Explicit permission lists per task
- Diff-based scope verification
- Task scope explicitly states "modify ONLY X"

**Detection:**
- File change audit shows unexpected modifications
- Permission requests exceed task requirements

### Feedback Loops

**Description:** Agent learns wrong patterns from misconfigured validation.

**Symptoms:**
- Agent produces outputs that pass validation but are wrong
- Quality degrades after automation added
- Verifier and agent "agree" on incorrect output

**Causes:**
- Verifier has bugs
- Validation criteria misaligned with actual requirements
- Self-referential validation (agent marks own work correct)

**Prevention:**
- Verifier developed independently from implementer
- Human sampling even at high autonomy levels
- Multiple independent validation sources

**Detection:**
- Downstream issues from "verified" work
- Human sampling finds errors that passed automation

### Coordination Failures

**Description:** Multi-agent work produces conflicts or gaps.

**Symptoms:**
- Agents modify same file, causing merge conflicts
- Work duplicated across agents
- Gaps between agent responsibilities

**Causes:**
- Overlapping task assignments
- No coordination protocol
- State files not updated atomically

**Prevention:**
- Clear task boundaries (file-level ownership)
- Sequential execution for dependent tasks
- Atomic state updates with handoff protocol

**Detection:**
- Merge conflicts in agent output
- Verifier finds missing functionality
- Duplicate changes in different files

---

## 10. Anti-Patterns

Common mistakes in agent management and their corrections.

### Treating Agents Like Humans

| Anti-pattern | Why It's Wrong | Correction |
|--------------|----------------|------------|
| "Great job!" (praise) | No effect; wastes tokens | State requirements clearly |
| "Use your best judgment" | Agents need explicit guidance | Define decision criteria |
| "I trust you to figure it out" | May hallucinate if stuck | Provide complete context |
| Building relationship over sessions | Sessions are independent | Use state files |
| Career development planning | Agents don't have careers | Focus on instruction refinement |

### Treating Agents Like Scripts

| Anti-pattern | Why It's Wrong | Correction |
|--------------|----------------|------------|
| Step-by-step micromanagement | Undermines agent reasoning | State goal and constraints |
| Specifying exact implementation | May miss better approaches | Specify requirements, not how |
| No autonomy at any level | Doesn't scale | Appropriate trust levels |
| Never updating based on output | Misses improvement opportunities | Iterate on CLAUDE.md |

### Over-Delegation

| Anti-pattern | Why It's Wrong | Correction |
|--------------|----------------|------------|
| "Fix all bugs" | Too broad, can't fit context window | Task Breakdown first |
| Autonomous mode on day one | No track record | Start at Level 1 |
| No permission boundaries | Risk of unintended changes | Explicit permission lists |
| Trusting autonomous monitoring | False sense of security | Maintain sampling |

### Under-Delegation

| Anti-pattern | Why It's Wrong | Correction |
|--------------|----------------|------------|
| Human reviews every line change | Bottleneck, doesn't scale | Appropriate trust levels |
| Never promoting past Level 1 | Wastes agent capability | Track and promote |
| Repeating context every task | Inefficient | Use state files |
| Never running agents in parallel | Underutilizes capacity | Operator pattern |

### Context Dumping

| Anti-pattern | Why It's Wrong | Correction |
|--------------|----------------|------------|
| Including entire codebase in context | Overwhelms agent, noise | Relevant files only |
| "Read everything in the repo" | Context window limit | Targeted exploration |
| Massive CLAUDE.md | Gets ignored | Focused instructions |
| Every past decision in context.md | Buries current state | Keep context.md minimal |

---

## Summary: Management Principle Translation

| Manager Tools Principle | Agent Translation | Key Difference |
|------------------------|-------------------|----------------|
| **One-on-Ones** | State management, handoff protocols | Explicit state, not relationship |
| **Feedback** | Output validation, quality gates | Immediate & prescriptive, no psychology |
| **Coaching** | CLAUDE.md refinement, specialization | Better instructions, not agent growth |
| **Delegation** | Task scoping, permission boundaries | Explicit boundaries, not judgment |

**The fundamental shift:** Human management develops *people*. Agent management scales *capacity*. Focus on clear instructions, explicit boundaries, and systematic validation—not relationships, motivation, or growth.

---

## Related Documents

- [Agent Task System](agent-task-system.md) - File-based coordination, state management
- [Agent Types](agent-types.md) - Specialized agents, trust levels, selection guide

## Sources

- [Manager Tools - The Trinity](https://www.manager-tools.com/faq/what-are-trinity-one-ones-feedback-coaching-delegation)
- [Manager Tools - One-on-Ones Guide](https://www.manager-tools.com/one-on-one-meetings-guide)
- [CMR Berkeley - Principal-Agent Perspective](https://cmr.berkeley.edu/2025/07/rethinking-ai-agents-a-principal-agent-perspective/)
- [ClaudeLog - Agent Engineering](https://claudelog.com/mechanics/agent-engineering/)
- [Anthropic - Building Agents with Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [claude-flow Framework](https://github.com/ruvnet/claude-flow)

---

## Iteration Log

### v0.1 (2025-01-18)
- Initial document creation
- Four Manager Tools principles mapped
- Autonomy levels defined (0-4)
- Trust progression criteria
- Failure modes and anti-patterns documented
