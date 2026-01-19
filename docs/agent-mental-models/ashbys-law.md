# Ashby's Law of Requisite Variety

Exploring how the Law of Requisite Variety applies to AI agent supervision.

## The Law

**"Only variety can absorb variety."**

A controller must have at least as many possible responses as the system it controls has possible states. If the controlled system can be in 20 states and your controller can only distinguish 3, you cannot achieve control.

| Aspect | Description |
|--------|-------------|
| **Creator** | W. Ross Ashby (cyberneticist, 1956) |
| **Domain** | Cybernetics, control theory |
| **Core Insight** | Control requires matching complexity |
| **Implication** | Inadequate supervision variety guarantees failure modes |

## Why This Matters for Agents

Agents have extraordinarily high action variety:

| Agent Can Do | Variety Magnitude |
|--------------|-------------------|
| Write any code | Infinite |
| Run any allowed command | Thousands |
| Make any decision within permissions | Uncountable |
| Interpret instructions in multiple ways | High |
| Fail in creative, unexpected ways | Very high |

Typical supervision has low variety:

| Typical Supervision | Variety |
|---------------------|---------|
| Build pass/fail | 2 states |
| Final output review | 1 checkpoint |
| Success/failure assessment | 2 states |
| "Did it work?" | Binary |

**The mismatch is extreme.** Supervision variety << Agent variety.

## The Variety Gap

```
Agent Action Space
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Correct implementations that pass the build              │  │
│  │  (what you actually want)                                │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Incorrect implementations that pass the build            │  │
│  │  (silent failures - your blind spot)                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Implementations that fail the build                      │  │
│  │  (you see these - high variety here is ok)               │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                │
└────────────────────────────────────────────────────────────────┘

Your supervision (build pass/fail) only distinguishes:
  [Passes build] vs [Fails build]

It cannot distinguish:
  [Correct] vs [Incorrect but passes]
```

**This is the core problem.** Your supervision variety is 2 (pass/fail), but the agent's output variety within "passes" is enormous.

## Dimensions of Agent Variety

Agent variety isn't one-dimensional. The agent can vary along multiple axes:

| Dimension | Example Variations | Detection Difficulty |
|-----------|-------------------|---------------------|
| **Correctness** | Wrong logic, edge cases missed | Medium (tests help) |
| **Completeness** | Partial implementation, missing error handling | Hard |
| **Style** | Inconsistent naming, formatting | Easy (linters) |
| **Architecture** | Wrong abstraction, tight coupling | Very hard |
| **Performance** | O(n^2) vs O(n), memory leaks | Hard |
| **Security** | Injection vulnerabilities, exposed secrets | Very hard |
| **Scope** | Did more/less than asked | Medium |
| **Side Effects** | Unintended file changes, state mutations | Hard |

**Insight:** Each dimension requires its own supervision variety. A build check has zero variety on security, architecture, and completeness dimensions.

## Two Strategies for Requisite Variety

Ashby's Law gives you two options:

### Strategy 1: Increase Supervision Variety

Add more ways to observe and distinguish agent states.

| Supervision Type | Variety Added | What It Catches |
|------------------|---------------|-----------------|
| **Build check** | Pass/Fail | Syntax, type errors, missing deps |
| **Test suite** | Pass/Fail per test | Logic errors in tested paths |
| **Linter** | N warnings/errors | Style, common bugs |
| **Type checker** | N errors | Type mismatches |
| **Security scanner** | N findings | Known vulnerability patterns |
| **Code review** | Human judgment | Architecture, completeness, intent |
| **Runtime testing** | Observed behavior | Integration, performance |

Each tool adds supervision variety on specific dimensions.

### Strategy 2: Reduce Agent Variety

Constrain what the agent can do.

| Constraint | Variety Reduction | Trade-off |
|------------|-------------------|-----------|
| **Sandbox** | No network, limited FS | Limits useful work |
| **Allowed commands** | Explicit whitelist | Must enumerate safe operations |
| **File scope** | Only touch listed files | Agent may need to touch others |
| **Output templates** | Structured responses | Less flexibility |
| **Small tasks** | Limited scope per task | More orchestration overhead |
| **Read-only mode** | No mutations | Can only analyze |

**Key insight:** Reducing agent variety is often easier than increasing supervision variety, but it limits capability.

## Supervision Variety Checklist

For requisite variety, your supervision must distinguish states on every dimension where failures matter:

### Correctness Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| Build passes | Low | Syntax only |
| Unit tests pass | Medium | Depends on test coverage |
| Integration tests pass | Medium-High | Cross-component correctness |
| Property tests pass | High | Edge cases, invariants |
| Hardware test passes | High | Real-world behavior |

### Completeness Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| No checkpoint | Zero | Most common failure |
| Task checklist | Medium | If checklist is comprehensive |
| Code coverage | Medium | Shows what's not tested |
| Manual review | High | Human judgment |

### Security Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| No checkpoint | Zero | Dangerous |
| Bandit/Semgrep | Medium | Known patterns only |
| Secret scanner | Medium | Known secret formats |
| Security review | High | Requires expertise |

### Scope Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| git diff | Medium | Shows what changed |
| File change list | Medium | Did it touch unexpected files? |
| Pre-commit hooks | Medium | Can reject based on patterns |
| Manual review | High | Intent vs. outcome comparison |

## The Logging Requirement

Ashby's Law implies specific logging requirements. If you can't log it, you can't observe it. If you can't observe it, you have zero variety on that dimension.

### What Must Be Logged

| Log Item | Why |
|----------|-----|
| **All commands run** | Detect unexpected operations |
| **All files read** | Understand context agent used |
| **All files modified** | Detect scope creep |
| **Decision points** | Understand reasoning |
| **Errors and retries** | Detect struggling |
| **Time spent** | Detect infinite loops, thrashing |

### Log Analysis Variety

Raw logs are useless without analysis that can distinguish states:

| Analysis | Distinguishes |
|----------|---------------|
| Command whitelist check | Allowed vs. disallowed commands |
| File scope check | Expected vs. unexpected file access |
| Error rate | Smooth progress vs. struggling |
| Pattern matching | Known-bad patterns in output |

## Checkpoint Design

Where checkpoints exist determines where you have supervision variety.

### Poor Checkpoint Design (Low Variety)

```
[Task Start] ─────────────────────────────────────────► [Task End]
                                                              │
                                                        [Build Check]

Supervision variety: 1 checkpoint, 2 states (pass/fail)
```

### Better Checkpoint Design (Higher Variety)

```
[Task Start] ──► [Plan] ──► [Implement] ──► [Test] ──► [Task End]
                   │            │             │             │
              [Review Plan]  [Build]     [Run Tests]   [Final Review]
                   │            │             │             │
                [Human OK?]  [Pass/Fail]  [Pass/Fail]  [Human OK?]
```

Each checkpoint adds variety at different points where failure can occur.

### Checkpoint Variety Requirements

| Phase | Failure Modes | Required Supervision Variety |
|-------|---------------|------------------------------|
| **Planning** | Wrong approach, misunderstood requirements | Human review or verifier agent |
| **Implementation** | Logic errors, incomplete, wrong scope | Build, tests, diff review |
| **Integration** | Breaks other things, doesn't fit architecture | Integration tests, system tests |
| **Deployment** | Works in dev, fails in prod | Staging environment, canary |

## Verifier Agents: Adding Variety Through Agents

One way to increase supervision variety is to use agents to supervise agents.

### Simple Verifier Pattern

```
[Worker Agent] ──► [Output] ──► [Verifier Agent] ──► [Approved/Rejected]
```

**But this just moves the problem.** Now you need supervision variety for the verifier agent.

### Variety-Increasing Patterns

| Pattern | How It Increases Variety |
|---------|-------------------------|
| **Adversarial verifier** | Actively tries to find problems (different search strategy) |
| **Diverse verifiers** | Multiple verifiers with different prompts/models |
| **Checklist verifier** | Explicit list of things to check (structured variety) |
| **Red team verifier** | Specifically looks for security/safety issues |

### Verifier Limitations

Verifiers cannot add variety beyond their own capabilities:

- Cannot catch bugs they can't detect
- May agree with wrong answers (correlated errors)
- Add latency and cost
- Still need human oversight at some level

**Insight:** Verifier agents are variety multipliers, not variety sources. The variety ultimately comes from the verification criteria, which a human must define.

## Permission Scoping as Variety Reduction

Limiting permissions reduces agent variety directly.

| Permission Level | Agent Variety | Supervision Needed |
|------------------|---------------|-------------------|
| Full access | Maximum | Maximum |
| No network | Reduced | Less (can't exfiltrate) |
| Read-only | Much reduced | Minimal (can't break things) |
| Single file | Minimal | Very low |

### Permission Design Strategy

1. **Enumerate necessary permissions** for the task
2. **Grant only those permissions**
3. **Agent variety is now bounded** by permission space
4. **Supervision variety can now match**

This is why sandboxing works: it doesn't increase supervision variety, it reduces agent variety to match available supervision.

## Rollback and Requisite Variety

Does the ability to undo change the variety requirement?

### Rollback Changes the Stakes, Not the Requirement

| Scenario | Supervision Variety Needed |
|----------|---------------------------|
| No rollback | High (mistakes are permanent) |
| Easy rollback | Lower (can recover from mistakes) |
| Automatic rollback on failure | Lower (system self-corrects) |

**But:** Rollback doesn't help you detect failures. It helps you recover from detected failures.

You still need supervision variety to know when to rollback.

### Rollback + Detection

```
[Agent Output] ──► [Detector] ──► [Good? No] ──► [Rollback]
                       │
                  [Requires supervision variety!]
```

**Insight:** Rollback is recovery variety, not detection variety. You need both.

## Practical Variety Audit

### Step 1: Enumerate Agent Variety

For your specific use case, what can the agent do?

```
Agent can:
- [ ] Write code in these languages: ___
- [ ] Run these commands: ___
- [ ] Access these files/directories: ___
- [ ] Make these decisions: ___
- [ ] Fail in these ways: ___
```

### Step 2: Enumerate Supervision Variety

What can your supervision distinguish?

```
Supervision can distinguish:
- [ ] Build pass vs. fail
- [ ] Tests pass vs. fail (coverage: __%)
- [ ] These error conditions: ___
- [ ] These scope violations: ___
- [ ] These security issues: ___
```

### Step 3: Find the Gap

| Dimension | Agent Variety | Supervision Variety | Gap |
|-----------|---------------|---------------------|-----|
| Correctness | High | Medium (tests) | Medium |
| Completeness | High | Low (no check) | HIGH |
| Security | Medium | Zero | CRITICAL |
| Scope | High | Low (diff review) | High |
| Style | Medium | High (linter) | None |

### Step 4: Close the Gaps

For each gap, either:
1. **Add supervision** (tools, checkpoints, human review)
2. **Reduce agent variety** (constraints, permissions, scope)
3. **Accept the risk** (explicitly, documented)

## Anti-Patterns

### "The Build Passed" Fallacy

```
"The build passed, so it's correct."
```

Build passing gives you 1 bit of information. Agent output variety is enormous. This is catastrophically insufficient supervision variety.

### "I'll Review It Later" Fallacy

```
"I'll review the final output."
```

Human review is high variety, but it's:
- Expensive (human time)
- Error-prone (human attention limits)
- Late (damage may be done)

If agent variety is very high and your only supervision is end-point human review, you will miss things.

### "Trust But Verify" Without Verification

```
"I trust the agent but I'll verify."
```

What is your verification? Does its variety match the agent's action variety?

If your verification is "skim the diff," your verification variety is much lower than you think.

### "Tests Will Catch It" Without Adequate Tests

```
"I have tests, so I'll know if it's broken."
```

Tests only catch what they test. Test variety is bounded by:
- Coverage (lines/branches touched)
- Assertion quality (what's actually checked)
- Edge case inclusion (unusual inputs)

If your test variety is low, "tests pass" tells you little.

## The Fundamental Trade-off

```
               High Capability / High Risk
                          │
                          │
    ┌─────────────────────┴─────────────────────┐
    │                                           │
    │   Agent with broad permissions            │
    │   + weak supervision                      │
    │   = many uncontrolled states              │
    │   = VARIETY MISMATCH                      │
    │                                           │
    └─────────────────────┬─────────────────────┘
                          │
           ┌──────────────┼──────────────┐
           │              │              │
           ▼              ▼              ▼
    ┌───────────┐  ┌───────────┐  ┌───────────┐
    │ Increase  │  │ Reduce    │  │ Accept    │
    │ supervision│  │ agent     │  │ risk      │
    │ variety   │  │ variety   │  │ explicitly│
    └───────────┘  └───────────┘  └───────────┘
         │              │              │
         │              │              │
         ▼              ▼              ▼
    More tools,    Sandboxing,    Documented
    more checks,   smaller tasks, risk
    more review    less power     acceptance
```

## Requisite Variety in Multi-Agent Systems

When agents orchestrate other agents, variety compounds:

```
Orchestrator variety × Worker variety = Total system variety
```

### Supervision Implications

| Layer | Variety Source | Supervision Needed |
|-------|----------------|-------------------|
| Worker agents | Task execution | Task-specific checks |
| Orchestrator | Task assignment, coordination | Meta-level oversight |
| System | Emergent behavior | System-level monitoring |

**Key insight:** Supervising the orchestrator is not the same as supervising the workers. You need variety at each level.

### Orchestrator-Specific Failure Modes

- Assigns wrong tasks to wrong workers
- Misinterprets worker output
- Coordinates incorrectly
- Loses track of system state
- Creates deadlocks or infinite loops

These need supervision variety separate from worker supervision.

## Summary: The Requisite Variety Imperative

1. **Agent variety is enormous.** Far more than most people intuit.

2. **Supervision variety is typically inadequate.** "Build passes" is not enough.

3. **The gap guarantees failures.** Not might cause - guarantees.

4. **You have two options:** Increase supervision variety or reduce agent variety.

5. **Both have costs.** More supervision = more overhead. Less variety = less capability.

6. **Pick your constraints.** Decide where to spend your supervision budget.

7. **Make the trade-off explicit.** Document what you're not checking and why.

The question is not "will the agent fail?" but "will your supervision detect the failure when it happens?"

If your supervision variety is less than the agent's failure variety, the answer is no.

## Open Questions

1. **Minimum viable variety:** What's the minimum supervision variety needed for common agent tasks?

2. **Variety measurement:** How do you quantify supervision variety in practice?

3. **Variety allocation:** Given limited supervision budget, where should variety be invested?

4. **Adaptive variety:** Can supervision variety adjust based on agent behavior?

5. **Variety decay:** Does supervision variety decay as agents find ways around checks?

6. **Correlated failures:** How do you handle verification that has correlated failures with the agent?

## Systems to Build

- [ ] **Variety audit tool:** Enumerate agent vs. supervision variety for a task
- [ ] **Gap analyzer:** Identify dimensions with supervision variety gaps
- [ ] **Checkpoint designer:** Suggest checkpoints to close variety gaps
- [ ] **Permission scoper:** Minimize agent variety for a given task
- [ ] **Verification composer:** Combine verifiers for additive variety

## Status

**Phase:** Exploration complete. Core insight: supervision variety must match agent variety on every dimension where failures matter. The typical "build pass" check provides catastrophically insufficient variety. Either increase supervision (more checks) or decrease agent variety (more constraints).

# Ashby's Law of Requisite Variety

Exploring how the Law of Requisite Variety applies to AI agent supervision.

## The Law

**"Only variety can absorb variety."**

A controller must have at least as many possible responses as the system it controls has possible states. If the controlled system can be in 20 states and your controller can only distinguish 3, you cannot achieve control.

| Aspect | Description |
|--------|-------------|
| **Creator** | W. Ross Ashby (cyberneticist, 1956) |
| **Domain** | Cybernetics, control theory |
| **Core Insight** | Control requires matching complexity |
| **Implication** | Inadequate supervision variety guarantees failure modes |

## Why This Matters for Agents

Agents have extraordinarily high action variety:

| Agent Can Do | Variety Magnitude |
|--------------|-------------------|
| Write any code | Infinite |
| Run any allowed command | Thousands |
| Make any decision within permissions | Uncountable |
| Interpret instructions in multiple ways | High |
| Fail in creative, unexpected ways | Very high |

Typical supervision has low variety:

| Typical Supervision | Variety |
|---------------------|---------|
| Build pass/fail | 2 states |
| Final output review | 1 checkpoint |
| Success/failure assessment | 2 states |
| "Did it work?" | Binary |

**The mismatch is extreme.** Supervision variety << Agent variety.

## The Variety Gap

```
Agent Action Space
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Correct implementations that pass the build              │  │
│  │  (what you actually want)                                │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Incorrect implementations that pass the build            │  │
│  │  (silent failures - your blind spot)                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Implementations that fail the build                      │  │
│  │  (you see these - high variety here is ok)               │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                │
└────────────────────────────────────────────────────────────────┘

Your supervision (build pass/fail) only distinguishes:
  [Passes build] vs [Fails build]

It cannot distinguish:
  [Correct] vs [Incorrect but passes]
```

**This is the core problem.** Your supervision variety is 2 (pass/fail), but the agent's output variety within "passes" is enormous.

## Dimensions of Agent Variety

Agent variety isn't one-dimensional. The agent can vary along multiple axes:

| Dimension | Example Variations | Detection Difficulty |
|-----------|-------------------|---------------------|
| **Correctness** | Wrong logic, edge cases missed | Medium (tests help) |
| **Completeness** | Partial implementation, missing error handling | Hard |
| **Style** | Inconsistent naming, formatting | Easy (linters) |
| **Architecture** | Wrong abstraction, tight coupling | Very hard |
| **Performance** | O(n^2) vs O(n), memory leaks | Hard |
| **Security** | Injection vulnerabilities, exposed secrets | Very hard |
| **Scope** | Did more/less than asked | Medium |
| **Side Effects** | Unintended file changes, state mutations | Hard |

**Insight:** Each dimension requires its own supervision variety. A build check has zero variety on security, architecture, and completeness dimensions.

## Two Strategies for Requisite Variety

Ashby's Law gives you two options:

### Strategy 1: Increase Supervision Variety

Add more ways to observe and distinguish agent states.

| Supervision Type | Variety Added | What It Catches |
|------------------|---------------|-----------------|
| **Build check** | Pass/Fail | Syntax, type errors, missing deps |
| **Test suite** | Pass/Fail per test | Logic errors in tested paths |
| **Linter** | N warnings/errors | Style, common bugs |
| **Type checker** | N errors | Type mismatches |
| **Security scanner** | N findings | Known vulnerability patterns |
| **Code review** | Human judgment | Architecture, completeness, intent |
| **Runtime testing** | Observed behavior | Integration, performance |

Each tool adds supervision variety on specific dimensions.

### Strategy 2: Reduce Agent Variety

Constrain what the agent can do.

| Constraint | Variety Reduction | Trade-off |
|------------|-------------------|-----------|
| **Sandbox** | No network, limited FS | Limits useful work |
| **Allowed commands** | Explicit whitelist | Must enumerate safe operations |
| **File scope** | Only touch listed files | Agent may need to touch others |
| **Output templates** | Structured responses | Less flexibility |
| **Small tasks** | Limited scope per task | More orchestration overhead |
| **Read-only mode** | No mutations | Can only analyze |

**Key insight:** Reducing agent variety is often easier than increasing supervision variety, but it limits capability.

## Supervision Variety Checklist

For requisite variety, your supervision must distinguish states on every dimension where failures matter:

### Correctness Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| Build passes | Low | Syntax only |
| Unit tests pass | Medium | Depends on test coverage |
| Integration tests pass | Medium-High | Cross-component correctness |
| Property tests pass | High | Edge cases, invariants |
| Hardware test passes | High | Real-world behavior |

### Completeness Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| No checkpoint | Zero | Most common failure |
| Task checklist | Medium | If checklist is comprehensive |
| Code coverage | Medium | Shows what's not tested |
| Manual review | High | Human judgment |

### Security Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| No checkpoint | Zero | Dangerous |
| Bandit/Semgrep | Medium | Known patterns only |
| Secret scanner | Medium | Known secret formats |
| Security review | High | Requires expertise |

### Scope Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| git diff | Medium | Shows what changed |
| File change list | Medium | Did it touch unexpected files? |
| Pre-commit hooks | Medium | Can reject based on patterns |
| Manual review | High | Intent vs. outcome comparison |

## The Logging Requirement

Ashby's Law implies specific logging requirements. If you can't log it, you can't observe it. If you can't observe it, you have zero variety on that dimension.

### What Must Be Logged

| Log Item | Why |
|----------|-----|
| **All commands run** | Detect unexpected operations |
| **All files read** | Understand context agent used |
| **All files modified** | Detect scope creep |
| **Decision points** | Understand reasoning |
| **Errors and retries** | Detect struggling |
| **Time spent** | Detect infinite loops, thrashing |

### Log Analysis Variety

Raw logs are useless without analysis that can distinguish states:

| Analysis | Distinguishes |
|----------|---------------|
| Command whitelist check | Allowed vs. disallowed commands |
| File scope check | Expected vs. unexpected file access |
| Error rate | Smooth progress vs. struggling |
| Pattern matching | Known-bad patterns in output |

## Checkpoint Design

Where checkpoints exist determines where you have supervision variety.

### Poor Checkpoint Design (Low Variety)

```
[Task Start] ─────────────────────────────────────────► [Task End]
                                                              │
                                                        [Build Check]

Supervision variety: 1 checkpoint, 2 states (pass/fail)
```

### Better Checkpoint Design (Higher Variety)

```
[Task Start] ──► [Plan] ──► [Implement] ──► [Test] ──► [Task End]
                   │            │             │             │
              [Review Plan]  [Build]     [Run Tests]   [Final Review]
                   │            │             │             │
                [Human OK?]  [Pass/Fail]  [Pass/Fail]  [Human OK?]
```

Each checkpoint adds variety at different points where failure can occur.

### Checkpoint Variety Requirements

| Phase | Failure Modes | Required Supervision Variety |
|-------|---------------|------------------------------|
| **Planning** | Wrong approach, misunderstood requirements | Human review or verifier agent |
| **Implementation** | Logic errors, incomplete, wrong scope | Build, tests, diff review |
| **Integration** | Breaks other things, doesn't fit architecture | Integration tests, system tests |
| **Deployment** | Works in dev, fails in prod | Staging environment, canary |

## Verifier Agents: Adding Variety Through Agents

One way to increase supervision variety is to use agents to supervise agents.

### Simple Verifier Pattern

```
[Worker Agent] ──► [Output] ──► [Verifier Agent] ──► [Approved/Rejected]
```

**But this just moves the problem.** Now you need supervision variety for the verifier agent.

### Variety-Increasing Patterns

| Pattern | How It Increases Variety |
|---------|-------------------------|
| **Adversarial verifier** | Actively tries to find problems (different search strategy) |
| **Diverse verifiers** | Multiple verifiers with different prompts/models |
| **Checklist verifier** | Explicit list of things to check (structured variety) |
| **Red team verifier** | Specifically looks for security/safety issues |

### Verifier Limitations

Verifiers cannot add variety beyond their own capabilities:

- Cannot catch bugs they can't detect
- May agree with wrong answers (correlated errors)
- Add latency and cost
- Still need human oversight at some level

**Insight:** Verifier agents are variety multipliers, not variety sources. The variety ultimately comes from the verification criteria, which a human must define.

## Permission Scoping as Variety Reduction

Limiting permissions reduces agent variety directly.

| Permission Level | Agent Variety | Supervision Needed |
|------------------|---------------|-------------------|
| Full access | Maximum | Maximum |
| No network | Reduced | Less (can't exfiltrate) |
| Read-only | Much reduced | Minimal (can't break things) |
| Single file | Minimal | Very low |

### Permission Design Strategy

1. **Enumerate necessary permissions** for the task
2. **Grant only those permissions**
3. **Agent variety is now bounded** by permission space
4. **Supervision variety can now match**

This is why sandboxing works: it doesn't increase supervision variety, it reduces agent variety to match available supervision.

## Rollback and Requisite Variety

Does the ability to undo change the variety requirement?

### Rollback Changes the Stakes, Not the Requirement

| Scenario | Supervision Variety Needed |
|----------|---------------------------|
| No rollback | High (mistakes are permanent) |
| Easy rollback | Lower (can recover from mistakes) |
| Automatic rollback on failure | Lower (system self-corrects) |

**But:** Rollback doesn't help you detect failures. It helps you recover from detected failures.

You still need supervision variety to know when to rollback.

### Rollback + Detection

```
[Agent Output] ──► [Detector] ──► [Good? No] ──► [Rollback]
                       │
                  [Requires supervision variety!]
```

**Insight:** Rollback is recovery variety, not detection variety. You need both.

## Practical Variety Audit

### Step 1: Enumerate Agent Variety

For your specific use case, what can the agent do?

```
Agent can:
- [ ] Write code in these languages: ___
- [ ] Run these commands: ___
- [ ] Access these files/directories: ___
- [ ] Make these decisions: ___
- [ ] Fail in these ways: ___
```

### Step 2: Enumerate Supervision Variety

What can your supervision distinguish?

```
Supervision can distinguish:
- [ ] Build pass vs. fail
- [ ] Tests pass vs. fail (coverage: __%)
- [ ] These error conditions: ___
- [ ] These scope violations: ___
- [ ] These security issues: ___
```

### Step 3: Find the Gap

| Dimension | Agent Variety | Supervision Variety | Gap |
|-----------|---------------|---------------------|-----|
| Correctness | High | Medium (tests) | Medium |
| Completeness | High | Low (no check) | HIGH |
| Security | Medium | Zero | CRITICAL |
| Scope | High | Low (diff review) | High |
| Style | Medium | High (linter) | None |

### Step 4: Close the Gaps

For each gap, either:
1. **Add supervision** (tools, checkpoints, human review)
2. **Reduce agent variety** (constraints, permissions, scope)
3. **Accept the risk** (explicitly, documented)

## Anti-Patterns

### "The Build Passed" Fallacy

```
"The build passed, so it's correct."
```

Build passing gives you 1 bit of information. Agent output variety is enormous. This is catastrophically insufficient supervision variety.

### "I'll Review It Later" Fallacy

```
"I'll review the final output."
```

Human review is high variety, but it's:
- Expensive (human time)
- Error-prone (human attention limits)
- Late (damage may be done)

If agent variety is very high and your only supervision is end-point human review, you will miss things.

### "Trust But Verify" Without Verification

```
"I trust the agent but I'll verify."
```

What is your verification? Does its variety match the agent's action variety?

If your verification is "skim the diff," your verification variety is much lower than you think.

### "Tests Will Catch It" Without Adequate Tests

```
"I have tests, so I'll know if it's broken."
```

Tests only catch what they test. Test variety is bounded by:
- Coverage (lines/branches touched)
- Assertion quality (what's actually checked)
- Edge case inclusion (unusual inputs)

If your test variety is low, "tests pass" tells you little.

## The Fundamental Trade-off

```
               High Capability / High Risk
                          │
                          │
    ┌─────────────────────┴─────────────────────┐
    │                                           │
    │   Agent with broad permissions            │
    │   + weak supervision                      │
    │   = many uncontrolled states              │
    │   = VARIETY MISMATCH                      │
    │                                           │
    └─────────────────────┬─────────────────────┘
                          │
           ┌──────────────┼──────────────┐
           │              │              │
           ▼              ▼              ▼
    ┌───────────┐  ┌───────────┐  ┌───────────┐
    │ Increase  │  │ Reduce    │  │ Accept    │
    │ supervision│  │ agent     │  │ risk      │
    │ variety   │  │ variety   │  │ explicitly│
    └───────────┘  └───────────┘  └───────────┘
         │              │              │
         │              │              │
         ▼              ▼              ▼
    More tools,    Sandboxing,    Documented
    more checks,   smaller tasks, risk
    more review    less power     acceptance
```

## Requisite Variety in Multi-Agent Systems

When agents orchestrate other agents, variety compounds:

```
Orchestrator variety × Worker variety = Total system variety
```

### Supervision Implications

| Layer | Variety Source | Supervision Needed |
|-------|----------------|-------------------|
| Worker agents | Task execution | Task-specific checks |
| Orchestrator | Task assignment, coordination | Meta-level oversight |
| System | Emergent behavior | System-level monitoring |

**Key insight:** Supervising the orchestrator is not the same as supervising the workers. You need variety at each level.

### Orchestrator-Specific Failure Modes

- Assigns wrong tasks to wrong workers
- Misinterprets worker output
- Coordinates incorrectly
- Loses track of system state
- Creates deadlocks or infinite loops

These need supervision variety separate from worker supervision.

## Summary: The Requisite Variety Imperative

1. **Agent variety is enormous.** Far more than most people intuit.

2. **Supervision variety is typically inadequate.** "Build passes" is not enough.

3. **The gap guarantees failures.** Not might cause - guarantees.

4. **You have two options:** Increase supervision variety or reduce agent variety.

5. **Both have costs.** More supervision = more overhead. Less variety = less capability.

6. **Pick your constraints.** Decide where to spend your supervision budget.

7. **Make the trade-off explicit.** Document what you're not checking and why.

The question is not "will the agent fail?" but "will your supervision detect the failure when it happens?"

If your supervision variety is less than the agent's failure variety, the answer is no.

## Open Questions

1. **Minimum viable variety:** What's the minimum supervision variety needed for common agent tasks?

2. **Variety measurement:** How do you quantify supervision variety in practice?

3. **Variety allocation:** Given limited supervision budget, where should variety be invested?

4. **Adaptive variety:** Can supervision variety adjust based on agent behavior?

5. **Variety decay:** Does supervision variety decay as agents find ways around checks?

6. **Correlated failures:** How do you handle verification that has correlated failures with the agent?

## Systems to Build

- [ ] **Variety audit tool:** Enumerate agent vs. supervision variety for a task
- [ ] **Gap analyzer:** Identify dimensions with supervision variety gaps
- [ ] **Checkpoint designer:** Suggest checkpoints to close variety gaps
- [ ] **Permission scoper:** Minimize agent variety for a given task
- [ ] **Verification composer:** Combine verifiers for additive variety

## Status

**Phase:** Exploration complete. Core insight: supervision variety must match agent variety on every dimension where failures matter. The typical "build pass" check provides catastrophically insufficient variety. Either increase supervision (more checks) or decrease agent variety (more constraints).

# Ashby's Law of Requisite Variety

Exploring how the Law of Requisite Variety applies to AI agent supervision.

## The Law

**"Only variety can absorb variety."**

A controller must have at least as many possible responses as the system it controls has possible states. If the controlled system can be in 20 states and your controller can only distinguish 3, you cannot achieve control.

| Aspect | Description |
|--------|-------------|
| **Creator** | W. Ross Ashby (cyberneticist, 1956) |
| **Domain** | Cybernetics, control theory |
| **Core Insight** | Control requires matching complexity |
| **Implication** | Inadequate supervision variety guarantees failure modes |

## Why This Matters for Agents

Agents have extraordinarily high action variety:

| Agent Can Do | Variety Magnitude |
|--------------|-------------------|
| Write any code | Infinite |
| Run any allowed command | Thousands |
| Make any decision within permissions | Uncountable |
| Interpret instructions in multiple ways | High |
| Fail in creative, unexpected ways | Very high |

Typical supervision has low variety:

| Typical Supervision | Variety |
|---------------------|---------|
| Build pass/fail | 2 states |
| Final output review | 1 checkpoint |
| Success/failure assessment | 2 states |
| "Did it work?" | Binary |

**The mismatch is extreme.** Supervision variety << Agent variety.

## The Variety Gap

```
Agent Action Space
+----------------------------------------------------------------+
|                                                                |
|  +----------------------------------------------------------+  |
|  | Correct implementations that pass the build              |  |
|  |  (what you actually want)                                |  |
|  +----------------------------------------------------------+  |
|                                                                |
|  +----------------------------------------------------------+  |
|  | Incorrect implementations that pass the build            |  |
|  |  (silent failures - your blind spot)                     |  |
|  +----------------------------------------------------------+  |
|                                                                |
|  +----------------------------------------------------------+  |
|  | Implementations that fail the build                      |  |
|  |  (you see these - high variety here is ok)               |  |
|  +----------------------------------------------------------+  |
|                                                                |
+----------------------------------------------------------------+

Your supervision (build pass/fail) only distinguishes:
  [Passes build] vs [Fails build]

It cannot distinguish:
  [Correct] vs [Incorrect but passes]
```

**This is the core problem.** Your supervision variety is 2 (pass/fail), but the agent's output variety within "passes" is enormous.

## Dimensions of Agent Variety

Agent variety isn't one-dimensional. The agent can vary along multiple axes:

| Dimension | Example Variations | Detection Difficulty |
|-----------|-------------------|---------------------|
| **Correctness** | Wrong logic, edge cases missed | Medium (tests help) |
| **Completeness** | Partial implementation, missing error handling | Hard |
| **Style** | Inconsistent naming, formatting | Easy (linters) |
| **Architecture** | Wrong abstraction, tight coupling | Very hard |
| **Performance** | O(n^2) vs O(n), memory leaks | Hard |
| **Security** | Injection vulnerabilities, exposed secrets | Very hard |
| **Scope** | Did more/less than asked | Medium |
| **Side Effects** | Unintended file changes, state mutations | Hard |

**Insight:** Each dimension requires its own supervision variety. A build check has zero variety on security, architecture, and completeness dimensions.

## Two Strategies for Requisite Variety

Ashby's Law gives you two options:

### Strategy 1: Increase Supervision Variety

Add more ways to observe and distinguish agent states.

| Supervision Type | Variety Added | What It Catches |
|------------------|---------------|-----------------|
| **Build check** | Pass/Fail | Syntax, type errors, missing deps |
| **Test suite** | Pass/Fail per test | Logic errors in tested paths |
| **Linter** | N warnings/errors | Style, common bugs |
| **Type checker** | N errors | Type mismatches |
| **Security scanner** | N findings | Known vulnerability patterns |
| **Code review** | Human judgment | Architecture, completeness, intent |
| **Runtime testing** | Observed behavior | Integration, performance |

Each tool adds supervision variety on specific dimensions.

### Strategy 2: Reduce Agent Variety

Constrain what the agent can do.

| Constraint | Variety Reduction | Trade-off |
|------------|-------------------|-----------|
| **Sandbox** | No network, limited FS | Limits useful work |
| **Allowed commands** | Explicit whitelist | Must enumerate safe operations |
| **File scope** | Only touch listed files | Agent may need to touch others |
| **Output templates** | Structured responses | Less flexibility |
| **Small tasks** | Limited scope per task | More orchestration overhead |
| **Read-only mode** | No mutations | Can only analyze |

**Key insight:** Reducing agent variety is often easier than increasing supervision variety, but it limits capability.

## Supervision Variety Checklist

For requisite variety, your supervision must distinguish states on every dimension where failures matter:

### Correctness Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| Build passes | Low | Syntax only |
| Unit tests pass | Medium | Depends on test coverage |
| Integration tests pass | Medium-High | Cross-component correctness |
| Property tests pass | High | Edge cases, invariants |
| Hardware test passes | High | Real-world behavior |

### Completeness Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| No checkpoint | Zero | Most common failure |
| Task checklist | Medium | If checklist is comprehensive |
| Code coverage | Medium | Shows what's not tested |
| Manual review | High | Human judgment |

### Security Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| No checkpoint | Zero | Dangerous |
| Bandit/Semgrep | Medium | Known patterns only |
| Secret scanner | Medium | Known secret formats |
| Security review | High | Requires expertise |

### Scope Dimension

| Checkpoint | Variety | Notes |
|------------|---------|-------|
| git diff | Medium | Shows what changed |
| File change list | Medium | Did it touch unexpected files? |
| Pre-commit hooks | Medium | Can reject based on patterns |
| Manual review | High | Intent vs. outcome comparison |

## The Logging Requirement

Ashby's Law implies specific logging requirements. If you can't log it, you can't observe it. If you can't observe it, you have zero variety on that dimension.

### What Must Be Logged

| Log Item | Why |
|----------|-----|
| **All commands run** | Detect unexpected operations |
| **All files read** | Understand context agent used |
| **All files modified** | Detect scope creep |
| **Decision points** | Understand reasoning |
| **Errors and retries** | Detect struggling |
| **Time spent** | Detect infinite loops, thrashing |

### Log Analysis Variety

Raw logs are useless without analysis that can distinguish states:

| Analysis | Distinguishes |
|----------|---------------|
| Command whitelist check | Allowed vs. disallowed commands |
| File scope check | Expected vs. unexpected file access |
| Error rate | Smooth progress vs. struggling |
| Pattern matching | Known-bad patterns in output |

## Checkpoint Design

Where checkpoints exist determines where you have supervision variety.

### Poor Checkpoint Design (Low Variety)

```
[Task Start] ----------------------------------------> [Task End]
                                                            |
                                                      [Build Check]

Supervision variety: 1 checkpoint, 2 states (pass/fail)
```

### Better Checkpoint Design (Higher Variety)

```
[Task Start] --> [Plan] --> [Implement] --> [Test] --> [Task End]
                   |            |             |             |
              [Review Plan]  [Build]     [Run Tests]   [Final Review]
                   |            |             |             |
                [Human OK?]  [Pass/Fail]  [Pass/Fail]  [Human OK?]
```

Each checkpoint adds variety at different points where failure can occur.

### Checkpoint Variety Requirements

| Phase | Failure Modes | Required Supervision Variety |
|-------|---------------|------------------------------|
| **Planning** | Wrong approach, misunderstood requirements | Human review or verifier agent |
| **Implementation** | Logic errors, incomplete, wrong scope | Build, tests, diff review |
| **Integration** | Breaks other things, doesn't fit architecture | Integration tests, system tests |
| **Deployment** | Works in dev, fails in prod | Staging environment, canary |

## Verifier Agents: Adding Variety Through Agents

One way to increase supervision variety is to use agents to supervise agents.

### Simple Verifier Pattern

```
[Worker Agent] --> [Output] --> [Verifier Agent] --> [Approved/Rejected]
```

**But this just moves the problem.** Now you need supervision variety for the verifier agent.

### Variety-Increasing Patterns

| Pattern | How It Increases Variety |
|---------|-------------------------|
| **Adversarial verifier** | Actively tries to find problems (different search strategy) |
| **Diverse verifiers** | Multiple verifiers with different prompts/models |
| **Checklist verifier** | Explicit list of things to check (structured variety) |
| **Red team verifier** | Specifically looks for security/safety issues |

### Verifier Limitations

Verifiers cannot add variety beyond their own capabilities:

- Cannot catch bugs they can't detect
- May agree with wrong answers (correlated errors)
- Add latency and cost
- Still need human oversight at some level

**Insight:** Verifier agents are variety multipliers, not variety sources. The variety ultimately comes from the verification criteria, which a human must define.

## Permission Scoping as Variety Reduction

Limiting permissions reduces agent variety directly.

| Permission Level | Agent Variety | Supervision Needed |
|------------------|---------------|-------------------|
| Full access | Maximum | Maximum |
| No network | Reduced | Less (can't exfiltrate) |
| Read-only | Much reduced | Minimal (can't break things) |
| Single file | Minimal | Very low |

### Permission Design Strategy

1. **Enumerate necessary permissions** for the task
2. **Grant only those permissions**
3. **Agent variety is now bounded** by permission space
4. **Supervision variety can now match**

This is why sandboxing works: it doesn't increase supervision variety, it reduces agent variety to match available supervision.

## Rollback and Requisite Variety

Does the ability to undo change the variety requirement?

### Rollback Changes the Stakes, Not the Requirement

| Scenario | Supervision Variety Needed |
|----------|---------------------------|
| No rollback | High (mistakes are permanent) |
| Easy rollback | Lower (can recover from mistakes) |
| Automatic rollback on failure | Lower (system self-corrects) |

**But:** Rollback doesn't help you detect failures. It helps you recover from detected failures.

You still need supervision variety to know when to rollback.

### Rollback + Detection

```
[Agent Output] --> [Detector] --> [Good? No] --> [Rollback]
                       |
                  [Requires supervision variety!]
```

**Insight:** Rollback is recovery variety, not detection variety. You need both.

## Practical Variety Audit

### Step 1: Enumerate Agent Variety

For your specific use case, what can the agent do?

```
Agent can:
- [ ] Write code in these languages: ___
- [ ] Run these commands: ___
- [ ] Access these files/directories: ___
- [ ] Make these decisions: ___
- [ ] Fail in these ways: ___
```

### Step 2: Enumerate Supervision Variety

What can your supervision distinguish?

```
Supervision can distinguish:
- [ ] Build pass vs. fail
- [ ] Tests pass vs. fail (coverage: __%)
- [ ] These error conditions: ___
- [ ] These scope violations: ___
- [ ] These security issues: ___
```

### Step 3: Find the Gap

| Dimension | Agent Variety | Supervision Variety | Gap |
|-----------|---------------|---------------------|-----|
| Correctness | High | Medium (tests) | Medium |
| Completeness | High | Low (no check) | HIGH |
| Security | Medium | Zero | CRITICAL |
| Scope | High | Low (diff review) | High |
| Style | Medium | High (linter) | None |

### Step 4: Close the Gaps

For each gap, either:
1. **Add supervision** (tools, checkpoints, human review)
2. **Reduce agent variety** (constraints, permissions, scope)
3. **Accept the risk** (explicitly, documented)

## Anti-Patterns

### "The Build Passed" Fallacy

```
"The build passed, so it's correct."
```

Build passing gives you 1 bit of information. Agent output variety is enormous. This is catastrophically insufficient supervision variety.

### "I'll Review It Later" Fallacy

```
"I'll review the final output."
```

Human review is high variety, but it's:
- Expensive (human time)
- Error-prone (human attention limits)
- Late (damage may be done)

If agent variety is very high and your only supervision is end-point human review, you will miss things.

### "Trust But Verify" Without Verification

```
"I trust the agent but I'll verify."
```

What is your verification? Does its variety match the agent's action variety?

If your verification is "skim the diff," your verification variety is much lower than you think.

### "Tests Will Catch It" Without Adequate Tests

```
"I have tests, so I'll know if it's broken."
```

Tests only catch what they test. Test variety is bounded by:
- Coverage (lines/branches touched)
- Assertion quality (what's actually checked)
- Edge case inclusion (unusual inputs)

If your test variety is low, "tests pass" tells you little.

## The Fundamental Trade-off

```
               High Capability / High Risk
                          |
                          |
    +---------------------+---------------------+
    |                                           |
    |   Agent with broad permissions            |
    |   + weak supervision                      |
    |   = many uncontrolled states              |
    |   = VARIETY MISMATCH                      |
    |                                           |
    +-----------------------+-------------------+
                          |
           +--------------+---------------+
           |              |               |
           v              v               v
    +-----------+   +-----------+   +-----------+
    | Increase  |   | Reduce    |   | Accept    |
    | supervision   | agent     |   | risk      |
    | variety   |   | variety   |   | explicitly|
    +-----------+   +-----------+   +-----------+
         |              |               |
         |              |               |
         v              v               v
    More tools,    Sandboxing,    Documented
    more checks,   smaller tasks, risk
    more review    less power     acceptance
```

## Requisite Variety in Multi-Agent Systems

When agents orchestrate other agents, variety compounds:

```
Orchestrator variety x Worker variety = Total system variety
```

### Supervision Implications

| Layer | Variety Source | Supervision Needed |
|-------|----------------|-------------------|
| Worker agents | Task execution | Task-specific checks |
| Orchestrator | Task assignment, coordination | Meta-level oversight |
| System | Emergent behavior | System-level monitoring |

**Key insight:** Supervising the orchestrator is not the same as supervising the workers. You need variety at each level.

### Orchestrator-Specific Failure Modes

- Assigns wrong tasks to wrong workers
- Misinterprets worker output
- Coordinates incorrectly
- Loses track of system state
- Creates deadlocks or infinite loops

These need supervision variety separate from worker supervision.

## Summary: The Requisite Variety Imperative

1. **Agent variety is enormous.** Far more than most people intuit.

2. **Supervision variety is typically inadequate.** "Build passes" is not enough.

3. **The gap guarantees failures.** Not might cause - guarantees.

4. **You have two options:** Increase supervision variety or reduce agent variety.

5. **Both have costs.** More supervision = more overhead. Less variety = less capability.

6. **Pick your constraints.** Decide where to spend your supervision budget.

7. **Make the trade-off explicit.** Document what you're not checking and why.

The question is not "will the agent fail?" but "will your supervision detect the failure when it happens?"

If your supervision variety is less than the agent's failure variety, the answer is no.

## Open Questions

1. **Minimum viable variety:** What's the minimum supervision variety needed for common agent tasks?

2. **Variety measurement:** How do you quantify supervision variety in practice?

3. **Variety allocation:** Given limited supervision budget, where should variety be invested?

4. **Adaptive variety:** Can supervision variety adjust based on agent behavior?

5. **Variety decay:** Does supervision variety decay as agents find ways around checks?

6. **Correlated failures:** How do you handle verification that has correlated failures with the agent?

## Systems to Build

- [ ] **Variety audit tool:** Enumerate agent vs. supervision variety for a task
- [ ] **Gap analyzer:** Identify dimensions with supervision variety gaps
- [ ] **Checkpoint designer:** Suggest checkpoints to close variety gaps
- [ ] **Permission scoper:** Minimize agent variety for a given task
- [ ] **Verification composer:** Combine verifiers for additive variety

## Status

**Phase:** Exploration complete. Core insight: supervision variety must match agent variety on every dimension where failures matter. The typical "build pass" check provides catastrophically insufficient variety. Either increase supervision (more checks) or decrease agent variety (more constraints).

