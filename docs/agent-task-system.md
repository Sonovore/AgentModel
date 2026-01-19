# Agent Task Management System

A file-based task coordination system for Claude Code that scales from single-session to multi-agent orchestration.

## Design Goals

1. **Human-readable** - Plain markdown, inspectable at any time
2. **Git-friendly** - All state tracked in version control
3. **Scalable** - Same patterns work for 1 agent or 50
4. **No external dependencies** - No Redis, no database, just files
5. **Graceful degradation** - Works manually if automation breaks

## Core Concepts

### Memory Layers

| Layer | File | Scope | Lifespan |
|-------|------|-------|----------|
| Working | TodoWrite (built-in) | Current task | Single session |
| Short-term | `context.md` | Active work | Days (session → session) |
| Long-term | `tasks.md` | Backlog | Weeks/months |
| Agent | `agents/*/state.md` | Agent memory | Agent lifetime |

### Agent Hierarchy

```
Conductor (optional)
    └── Operator (domain specialist)
            └── Worker (task executor)
```

- **Conductor**: Top-level orchestrator, decomposes large goals
- **Operator**: Manages a domain (frontend, backend, testing, etc.)
- **Worker**: Executes a single discrete task

For simple cases, skip Conductor - human acts as conductor, operators do the work.

## File Structure

### Shared Infrastructure (in .claude-shared/, symlinked to .claude/)

```
.claude-shared/
├── commands/
│   ├── assign.md                  # /assign command
│   ├── status.md                  # /status command
│   └── orchestrate.md             # /orchestrate command
├── scripts/
│   └── agent-helpers/             # Scripts for agent coordination
├── docs/
│   └── agent-task-system.md       # This document
└── skills/
    └── agent-worker/              # Skill for worker agents (optional)
```

### Project-Specific State (in .claude/, NOT symlinked)

```
.claude/
├── context.md                     # Short-term memory (current session state)
├── tasks.md                       # Long-term backlog
└── agents/                        # Runtime agent state (project-specific)
    ├── conductor.md               # Top-level orchestrator state (optional)
    ├── operator-001/              # First operator
    │   ├── state.md               # Operator's memory/strategy
    │   ├── task-001.md            # Worker assignment
    │   ├── task-002.md
    │   └── task-003.md
    └── operator-002/              # Second operator
        ├── state.md
        └── task-001.md
```

**Why separate?**
- Shared: Commands, scripts, docs - same across all projects
- Project-specific: Agent state, tasks, context - unique to each project

## File Formats

### context.md (Short-term Memory)

```markdown
# Session Context

## Immediate
(Blockers, things needing attention NOW)

## In Progress
(Current work, state of active tasks)

## Recent Completions
(What just finished, relevant for continuity)

## Next Steps
(Recommended actions)
```

**Updated by:** `/handoff-context` command before `/clear` or session end.

### tasks.md (Long-term Backlog)

```markdown
# Backlog

## Bugs
- [ ] Brief description `#tag` `priority:high`
- [ ] Another bug `priority:low`

## Features
- [ ] Feature description `epic:display-refactor`

## Tooling
- [ ] Improvement to dev workflow
```

**Rules:**
- No completed items (delete when done, history in git)
- No "active" section (that's context.md)
- Simple `[ ]` only - no `[x]` or `[>]`
- Optional tags for filtering/search

### state.md (Operator Memory)

```markdown
# Operator: [name]

## Identity
Role: (what this operator specializes in)
Created: (timestamp)
Agent ID: (for resume)

## Current Strategy
(High-level approach, decisions made)

## Active Tasks
- task-001: (status) (summary)
- task-002: (status) (summary)

## Blocked
(What's waiting, why)

## Completed This Session
(Recent completions for context)

## Notes
(Learnings, things to remember)
```

### task-XXX.md (Worker Assignment)

```markdown
# Task XXX: [Brief Title]

## Assignment
Owner: (agent_id or "unclaimed")
Status: pending | claimed | in_progress | blocked | complete | failed
Parent: (operator ID)
Created: (timestamp)
Updated: (timestamp)

## Input
(What the worker needs to know to execute)
- Context: ...
- Requirements: ...
- Files involved: ...
- Acceptance criteria: ...

## Output
(Filled in by worker)
- Result: ...
- Changes made: ...
- Files modified: ...
- Issues encountered: ...

## Handoff Notes
(For next agent if work continues)
```

## Workflows

### Single Agent (Current Mode)

```
Human → context.md → Claude → TodoWrite (in-session) → /handoff-context → context.md
```

No agents/ directory needed. Just context.md + tasks.md.

### Human + Operators

```
Human assigns from tasks.md
    ↓
Creates operator-XXX/task-001.md
    ↓
Spawns operator agent with Task tool
    ↓
Operator claims task, executes
    ↓
Operator writes output to task-001.md
    ↓
Human reviews, moves to context.md or deletes
```

### Full Orchestration (Conductor)

```
Human: "Fix all display bugs"
    ↓
Conductor reads tasks.md
    ↓
Creates operator-display/ with tasks
    ↓
Spawns operator agents (parallel)
    ↓
Operators spawn workers for subtasks
    ↓
Workers execute, write results
    ↓
Operators aggregate, report to conductor
    ↓
Conductor updates context.md, marks tasks.md complete
```

## Commands

### Existing
- `/handoff-context` - Update context.md before session end

### Proposed
- `/assign <task>` - Create task file, optionally spawn agent
- `/status` - Show all agent/task states
- `/orchestrate <goal>` - Conductor mode: decompose and delegate
- `/claim <task-id>` - Mark task as owned by current agent
- `/complete <task-id>` - Mark task done, write output

## State Transitions

```
Task States:
pending → claimed → in_progress → complete
                 ↘ blocked → in_progress
                 ↘ failed

Operator States:
idle → active → waiting → idle
            ↘ blocked
```

## Coordination Rules

### Ownership
- Only one agent owns a task at a time
- Owner writes agent_id to task file on claim
- Other agents skip claimed tasks

### File Locking
- For now: trust single-writer (one agent per task)
- Future: lock files or atomic writes if conflicts arise

### Handoff Protocol
1. Worker completes task
2. Worker writes Output section
3. Worker sets Status: complete
4. Worker writes Handoff Notes if follow-up needed
5. Parent operator reads result
6. Parent creates new task or reports up

## Example: Bug Fix Flow

**Initial state:**
```markdown
# tasks.md
## Bugs
- [ ] PLAY resets slider LEDs `priority:high`
```

**Human runs:** `/assign "PLAY resets slider LEDs"`

**System creates:** `.claude/agents/operator-001/task-001.md`
```markdown
# Task 001: Fix PLAY Resets Slider LEDs

## Assignment
Owner: unclaimed
Status: pending
Parent: human
Created: 2025-01-18

## Input
- Bug: Pressing PLAY clears the mix/decay/pitch LED state
- Files likely involved: Core/Src/led.c, Core/Src/play.c
- Acceptance: PLAY button does not affect slider LED state

## Output
(pending)
```

**Human spawns agent:**
```
Task(prompt="Read .claude/agents/operator-001/task-001.md, investigate and fix", run_in_background=true)
```

**Agent claims, works, completes:**
```markdown
## Assignment
Owner: agent-abc123
Status: complete
...

## Output
- Root cause: LED_Clear() called unconditionally in Play_Start()
- Fix: Added state preservation before clear, restore after
- Files modified: Core/Src/play.c (lines 145-152)
- Tested: Build succeeds, needs hardware verification

## Handoff Notes
Hardware test required. If LEDs still reset, check LED_UpdateAll() timing.
```

**Human reviews, deletes task file, removes from tasks.md**

## Open Questions

1. **Task ID generation** - Sequential? UUID? Timestamp-based?
2. **Cleanup policy** - Delete completed tasks immediately? Archive?
3. **Failure handling** - Retry? Reassign? Escalate to human?
4. **Concurrency** - How many parallel agents is practical?
5. **Context size** - How much to include in agent prompts?

## Iteration Log

### v0.1 (2025-01-18)
- Initial design
- File structure defined
- Basic workflows documented

---

## References

- [Claude Code Multi-Agent Orchestration](https://www.theunwindai.com/p/claude-code-s-hidden-multi-agent-orchestration-now-open-source)
- [Running 10+ Claude Instances in Parallel](https://dev.to/bredmond1019/multi-agent-orchestration-running-10-claude-instances-in-parallel-part-3-29da)
- [claude-flow Framework](https://github.com/ruvnet/claude-flow)
