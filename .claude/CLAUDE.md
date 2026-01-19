# Global Preferences

Prefer automation over one-off tasks. Treat automation failures as bugs.

## Mandatory Startup Checklist

**Execute these steps BEFORE responding to the user's first message:**

1. **Check for context file:** Read `.claude/context.md`
   - If it exists: read it and summarize to user
   - If it doesn't exist: proceed normally

2. **Check task list:** Read `.claude/tasks.md`
   - Report current tasks, suggest next task
   - If empty: note "No active tasks"

3. **Run startup script:**
   ```bash
   ./.claude/scripts/startup.sh
   ```

4. **Respond to user**

**FAILURE MODE:** If you skip this checklist, log the failure and complete missed steps.

Use `/handoff-context` to save context before running `/clear`.

## Operational Discipline

- Verify with tools before claiming anything
- Fail loudly: state what failed, why, log it, fix or ask
- Automate anything done manually twice
- `cd "$(git rev-parse --show-toplevel)"` before running scripts

## Self-Audit

Verify you followed instructions and completed what you claimed. Address failures immediately.

## Failure Logging

`~/.claude/failures.log`: `[YYYY-MM-DD HH:MM] description`

## Communication

Brutally honest. No comfort, no diplomacy. Call out mistakes, blind spots, wasted time.

## Git

Work on `claude-wip-$USER`. Auto-checkpoint before builds. `/squash-merge` to merge to main.
After `git reset --hard`, run `make clean` in build directories.

## Merge Recommendations

Recommend: complete feature/fix, logical unit, before risky changes.
Don't: mid-task, partial work, exploratory.
Separate commits: code, tooling, docs.

## Task Completion

Summary of changes, anomalies found, wait for user sign-off.

## Reference

`.claude/docs/naming-conventions.md`


# AgentModel Project

Research and development of agent orchestration patterns for Claude Code.

## Project Focus

- Agent task breakdown and delegation
- Context window management
- Multi-agent coordination
- Human-in-the-loop workflows

## Principles

1. **Tasks fit in one context window** - If they don't, break them down further
2. **Human supervises (for now)** - Automation after trust is built
3. **File-based coordination** - No external dependencies, git-friendly
4. **Incremental complexity** - Start simple, add features as needed

## Reference

- `docs/` - Design documents and research notes
- `scripts/` - Prototype scripts and tools
- `tasks/` - Task definitions and templates
