# RACI Matrix

**Source:** Project Management methodology for role clarity

## Framework Summary

RACI is a responsibility assignment matrix that clarifies roles for tasks and deliverables. It prevents gaps (nobody owns it) and overlaps (multiple owners conflict) by forcing explicit assignment of four distinct roles.

## The Four Roles

| Role | Definition | Quantity | Communication |
|------|------------|----------|---------------|
| **Responsible (R)** | Does the work, executes the task | One or more | Active participant |
| **Accountable (A)** | Owns the outcome, signs off, bears consequences | **Exactly ONE** | Final authority |
| **Consulted (C)** | Provides input before decision/action | Zero or more | Two-way |
| **Informed (I)** | Notified after decision/action | Zero or more | One-way |

### The Critical Rule

**Exactly one Accountable per task.** This is non-negotiable. Multiple Accountables means no one is truly accountable.

## How RACI Prevents Problems

### Gap Prevention
- Forces explicit assignment of who does the work (R)
- Requires naming who owns the outcome (A)
- Identifies who should provide expertise (C)
- Specifies who needs to know (I)

### Overlap Prevention
- Enforces "exactly one Accountable" per task
- Distinguishes between input (Consulted) and execution (Responsible)
- Clarifies one-way notification (Informed) vs. two-way input (Consulted)

## Agent Application

### The Central Insight: Agents Cannot Be Accountable

Accountability requires:
- Bearing consequences for outcomes
- Making judgment calls about success
- Having something at stake

Agents lack all three. Therefore:

| Role | Can Agent Hold It? | Why |
|------|-------------------|-----|
| **Responsible** | Yes | Agent can do the work |
| **Accountable** | **No** | Agent cannot bear consequences |
| **Consulted** | Yes | Agent can provide codebase knowledge |
| **Informed** | Yes | Agent can receive status updates |

### RACI for Human-Agent Tasks

| Task | Human | Agent |
|------|-------|-------|
| Write code | A | R |
| Review code | A, R | C |
| Approve PR | A, R | I |
| Run tests | A | R |
| Deploy to production | A, R | C or I |
| Define requirements | A, R | C |

**Human is ALWAYS Accountable** - this is the fundamental rule.

### Multi-Agent RACI

When multiple agents are involved:

| Task | Human | Agent A | Agent B |
|------|-------|---------|---------|
| Research | A | R | I |
| Implement | A | C | R |
| Verify | A, R | I | I |

Even with multiple agents, exactly one human remains Accountable.

## Practical Implications

1. **Every delegated task needs a named human owner**
   - Not "the team" or "someone" - a specific person
   - That person is Accountable regardless of who does the work

2. **Responsibility can be delegated; accountability cannot**
   - Agent can be Responsible for writing code
   - Human remains Accountable for the code quality

3. **The approval gate transfers responsibility, not accountability**
   - Before approval: Agent produced it
   - After approval: Human approved it
   - Human was Accountable the entire time

4. **CLAUDE.md represents delegated judgment**
   - Agent is Responsible for following conventions
   - Human is Accountable for whether conventions are right

5. **Consultation requires response time**
   - If agent is Consulted, workflow must pause for agent input
   - If agent is Informed, workflow continues without waiting

## Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No Accountable | "Who owns this?" confusion | Assign exactly one A |
| Multiple Accountable | Conflicts, buck-passing | Reduce to one A |
| Responsible without Accountable | Work done but not owned | Add A who reviews |
| Accountable without Responsible | Owner but no executor | Add R or A does work |
| Everyone Consulted | Decision paralysis | Reduce C, increase I |

## Common Agent Scenarios

### Bug Fix
- **Human**: A (owns the outcome)
- **Agent**: R (does the investigation and fix)
- **Code owners**: C (consulted on approach)
- **Team**: I (informed when merged)

### New Feature
- **Human**: A (owns the outcome)
- **Human**: C (consulted on requirements)
- **Agent**: R (implements)
- **Reviewers**: C (consulted on implementation)
- **Team**: I (informed when shipped)

### Production Incident
- **On-call human**: A (owns resolution)
- **Agent**: R (gathers diagnostics), C (suggests fixes)
- **Human**: R (executes fix - agent shouldn't touch prod)
- **Stakeholders**: I (informed of status)

## Connection to Other Frameworks

- **ICS**: "Unity of Command" = "One Accountable"
- **Principal-Agent Theory**: Human (principal) is always Accountable; agent cannot be
- **Cynefin**: Clear domains allow more R delegation; Complex domains require human R
- **Delegation Levels**: RACI clarifies what each level means operationally

## Key Insight

**Agents can do work (Responsible) but cannot own outcomes (Accountable).** Every task delegated to an agent still has a human Accountable for the result. RACI makes this explicit and prevents the illusion that delegation transfers accountability.
