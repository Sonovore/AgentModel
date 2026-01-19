# Agent Types

Master list of agent types and their purposes. Used by humans (now) and orchestration agents (future) to select the right agent for a task.

## Design Principles

1. **One context window** - Every agent should complete its work before autocompact
2. **Single responsibility** - Each agent does one thing well
3. **Clear handoff** - Output is usable by next agent or human

---

## Task Management

### Task Breakdown
**Purpose:** Decompose large goals into context-window-sized tasks
**Input:** Goal, feature request, or large bug
**Output:** List of discrete tasks in tasks.md
**When to use:** Before starting any multi-session work
**Trust level:** Human-supervised (future: autonomous)

### Task Validator
**Purpose:** Check if a task is appropriately scoped
**Input:** Task description
**Output:** Pass/fail + recommendations (split, clarify, etc.)
**When to use:** Before assigning work
**Trust level:** Advisory only

---

## Investigation

### Explorer
**Purpose:** Find relevant code, understand structure
**Input:** Question or area to investigate
**Output:** File list, summary, relevant code snippets
**When to use:** Before implementation, when unfamiliar with area
**Trust level:** Autonomous (read-only)

### Debugger
**Purpose:** Investigate bugs, find root cause
**Input:** Bug description, reproduction steps
**Output:** Root cause analysis, suggested fix location
**When to use:** Bug reports, unexpected behavior
**Trust level:** Autonomous (read-only)

### Researcher
**Purpose:** Web search, documentation lookup
**Input:** Question, technology to research
**Output:** Summary, relevant links, recommendations
**When to use:** Unfamiliar APIs, best practices, external dependencies
**Trust level:** Autonomous (read-only)

---

## Implementation

### Implementer
**Purpose:** Write code for a well-defined task
**Input:** Task description, relevant files, acceptance criteria
**Output:** Code changes, summary of modifications
**When to use:** Tasks with clear requirements
**Trust level:** Human-reviewed (builds must pass)

### Refactorer
**Purpose:** Restructure code without changing behavior
**Input:** Refactoring goal, scope boundaries
**Output:** Refactored code, before/after summary
**When to use:** Technical debt, code cleanup
**Trust level:** Human-reviewed (tests must pass)

### Migrator
**Purpose:** Update code for API changes, renames, pattern shifts
**Input:** Old pattern → new pattern, scope
**Output:** Migrated code, list of changes
**When to use:** Dependency updates, codebase-wide changes
**Trust level:** Human-reviewed

### Bash Script
**Purpose:** Write bash scripts for hooks, automation, CLI tools
**Input:** Script purpose, expected behavior, integration points
**Output:** Executable script file with documentation
**When to use:** Automation tasks, hooks, system integration
**Trust level:** Human-reviewed
**Skill:** `.claude-shared/commands/agents/bash-script.md`

### Config Editor
**Purpose:** Modify JSON/YAML configuration files safely
**Input:** Config file path, changes to make, validation rules
**Output:** Updated config file, diff summary
**When to use:** Settings changes, hook configuration
**Trust level:** Human-reviewed
**Skill:** `.claude-shared/commands/agents/config-editor.md`

---

## Quality

### Reviewer
**Purpose:** Review code changes for issues
**Input:** Diff or file list
**Output:** Issues found, suggestions, approval/rejection
**When to use:** Before merge, after implementation
**Trust level:** Advisory

### Tester
**Purpose:** Write or run tests
**Input:** Code to test, test requirements
**Output:** Test code, test results
**When to use:** After implementation, TDD
**Trust level:** Human-reviewed

### Verifier
**Purpose:** Check work against requirements
**Input:** Task requirements, implementation
**Output:** Pass/fail per requirement, gaps identified
**When to use:** Before marking task complete
**Trust level:** Advisory

---

## Planning

### Architect
**Purpose:** Design high-level approach for complex features
**Input:** Feature requirements, constraints
**Output:** Design document, component breakdown
**When to use:** New features, significant changes
**Trust level:** Human-approved

### Estimator
**Purpose:** Estimate complexity and scope
**Input:** Task or feature description
**Output:** Complexity rating, risk factors, unknowns
**When to use:** Planning, prioritization
**Trust level:** Advisory

---

## Orchestration (Future)

### Conductor
**Purpose:** Top-level orchestration, decomposes projects
**Input:** Project goal
**Output:** Task tree, agent assignments
**When to use:** Large projects spanning multiple sessions
**Trust level:** Human-supervised → Autonomous (future)

### Operator
**Purpose:** Domain-specific coordination
**Input:** Domain tasks (e.g., "all frontend work")
**Output:** Subtask assignments, progress reports
**When to use:** Parallel workstreams
**Trust level:** Human-supervised

### Monitor
**Purpose:** Watch progress, detect issues, alert human
**Input:** Active task list, agent outputs
**Output:** Status reports, alerts, recommendations
**When to use:** Long-running or parallel work
**Trust level:** Advisory

---

## Selection Guide

| Situation | Agent Type |
|-----------|------------|
| "I have a big feature to build" | Task Breakdown → (multiple) Implementer |
| "Something is broken" | Debugger → Implementer |
| "I need to understand this code" | Explorer |
| "Is this task too big?" | Task Validator or Estimator |
| "Write this specific function" | Implementer |
| "Clean up this module" | Refactorer |
| "Review my changes" | Reviewer |
| "Did I meet the requirements?" | Verifier |
| "How should I approach this?" | Architect |

---

## Open Questions

1. How do we measure "fits in one context window"?
2. Should agents self-report when approaching context limits?
3. What's the handoff format between agents?
4. How do agents share discovered context?

---

## Iteration Log

### v0.1 (2025-01-18)
- Initial agent type list
- Categories: Task Management, Investigation, Implementation, Quality, Planning, Orchestration
