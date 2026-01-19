# Proactive Handoff Design

## Core Principle

**Tasks should complete in a single context window.** If they don't, the task needs further breakdown—not a multi-window persistence mechanism.

---

## Tracking File Roles

Three files, three distinct purposes:

| File | Role | Updated | Content |
|------|------|---------|---------|
| **session-state.md** | Live operational state | Automatic (hooks) | Files touched, running agents, immediate next action |
| **context.md** | Strategic checkpoint | Automatic (on git commit) | What was accomplished, key decisions, recommendations |
| **tasks.md** | Backlog | Manual | Things to do eventually |

### Separation of Concerns

```
session-state.md          context.md              tasks.md
─────────────────        ─────────────────       ─────────────────
"What's happening        "What happened          "What we might
 right now"               at last commit"         do someday"

- Modified files         - Commit summary        - Bugs
- Next step              - Decisions made        - Features
- Running agents         - What's next           - Research
                         - Recommendations
```

### Update Triggers

| File | Trigger | Mechanism |
|------|---------|-----------|
| session-state.md | Every Edit/Write | PostToolUse hook |
| session-state.md | Manual | `proactive-handoff.sh next "step"` |
| context.md | Every git commit | Post-commit hook (TODO) |
| tasks.md | Manual | Human editing |

---

## Current Implementation

### What We Track (session-state.md)
- **Modified Files** — Auto-captured via PostToolUse hook on Edit/Write
- **Running Agents** — Placeholder (needs hook integration)
- **Next Steps** — Manual via `proactive-handoff.sh next`
- **Session Timestamps** — Start time, last updated

### Hooks Configured
- `PostToolUse` → Track file modifications
- `PreCompact` → Save state backup
- `SessionStart` → Load previous state, initialize fresh

### Files
| File | Purpose |
|------|---------|
| `.claude/session-state.md` | Live session state |
| `.claude/session-state.md.bak` | Backup before compaction |
| `.claude/session-history.log` | Audit trail of cleanups |

---

## TODO: Commit-Triggered context.md Update

### Concept

Every git commit is a natural milestone. Update `context.md` automatically when commits happen:

```
GIT COMMIT
    │
    ├─→ Post-commit hook runs
    │       ├─→ Get commit message, files changed
    │       ├─→ Append to context.md "Commits" section
    │       └─→ Clear session-state.md "Modified Files" (already committed)
    │
    └─→ context.md now reflects latest checkpoint
```

### What to Capture

```markdown
## Recent Commits

### [2026-01-18 20:15] abc1234 - Implement proactive handoff
- Files: proactive-handoff.sh, post-edit-hook.sh, settings.json
- Next: Test with friend, decide on context.md automation
```

### Implementation Options

1. **Git post-commit hook** (`.git/hooks/post-commit`)
   - Runs after every commit
   - Can call a script to update context.md
   - Limitation: Only runs on manual commits, not auto-checkpoints

2. **Wrapper around git commit**
   - Intercept commit command
   - More control but more complexity

3. **Part of auto-checkpoint logic**
   - Modify `pre-compact.sh` to update context.md when it commits
   - Already runs at key moments

### context.md New Format

```markdown
# Session Context

## Current State
<!-- Brief summary of where we are -->

## Recent Commits
<!-- Auto-updated by post-commit hook -->

### [timestamp] hash - message
- Files: list
- Next: inferred or manual

## Decisions
<!-- Key decisions made (manual) -->

## Recommendations
<!-- What to do next session (manual) -->
```

### Open Questions

1. Should auto-checkpoint commits update context.md? (Could be noisy)
2. How to infer "Next" from commit? (Maybe don't - keep manual)
3. Should we clear session-state.md files on commit? (They're committed now)

---

## Decisions Made

### Added
| Feature | Rationale |
|---------|-----------|
| **Next Steps** | Critical when interrupted; "where was I?" |
| **File tracking** | Know what changed this session |
| **Cleanup mechanism** | Prevent state bloat |
| **History log** | Audit trail for debugging |

### Deferred
| Feature | Rationale |
|---------|-----------|
| **Decision Log** | Tasks fit in one window; decisions don't span sessions |
| **Session Goals** | Quick sessions by default; goals are implicit |
| **Problems/Solutions** | Manual effort, defer until pain is felt |
| **Semantic memory** | Too complex for current needs |

### Already Handled Elsewhere
| Feature | How |
|---------|-----|
| **Git state** | Auto-commit after code edits (existing) |
| **Milestone commits** | TODO: Add commit at major plan starts |

---

## Future Consideration: Task-Type Awareness

Different tasks need different context tracking:

| Task Type | Duration | Context Needs |
|-----------|----------|---------------|
| **Quick fix** | <10 min | Minimal — just file list |
| **Single feature** | 1 session | Current implementation sufficient |
| **Complex feature** | Multi-session | Would need Decision Log, but should be broken down instead |
| **Investigation** | Variable | May need problem/solution tracking |

### Idea: Dynamic Context Mode

Claude could detect when a task is becoming complex and prompt the user:

```
⚠️ This task appears to be growing beyond a single session.
Options:
1. Break it down into smaller tasks now
2. Switch to "extended context" mode (adds Decision Log, Goals)
3. Continue as-is
```

**Implementation:** Could be a PreToolUse hook that analyzes task complexity, or a periodic check based on:
- Number of files modified
- Time elapsed
- Todo list length
- Context usage percentage

**Status:** Not implemented. Revisit when we have more experience with the base system.

---

## TODO

- [x] Add "Next Steps" section to session-state.md template
- [ ] Implement commit-triggered context.md update
  - Post-commit hook or integrate with auto-checkpoint
  - Capture: commit hash, message, files changed
  - Clear session-state.md "Modified Files" after commit
- [ ] Investigate hook for agent tracking (SubagentStart/SubagentStop?)
- [ ] Consider task-type detection mechanism

---

## Changelog

### 2026-01-18 (continued)
- Clarified roles: session-state.md (live), context.md (checkpoint), tasks.md (backlog)
- Designed commit-triggered context.md update (not yet implemented)
- Rule: context.md updates on git commits, not manually

### 2026-01-18
- Initial implementation: file tracking, cleanup, session-start integration
- Decided against Decision Log (tasks should fit in one window)
- Added Next Steps as priority feature
- Documented task-type awareness as future consideration
