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


# Agent Conventions (MANDATORY)

All agents operating in this system MUST follow conventions in `.agent-conventions/`.

**These are NOT guidelines - they are requirements.** Convention violations are defects.

## Convention Documents

1. **Naming Conventions** - `.agent-conventions/naming.md`
   - File naming: `*.test.ts`, `agent-*.yaml`, `schema-*.json`
   - Variable naming: Booleans (`is*`, `has*`), Collections (plural), Constants (SCREAMING_SNAKE_CASE)
   - Task IDs: `DOMAIN-NNN` format (CODE-100, TEST-200)
   - Message types: Dot notation (`task.assignment`, `status.progress`)
   - Reserved terms: GO, STOP, WARNING, STANDBY, ACKNOWLEDGED, BLOCKED, ESCALATE, CRITICAL

2. **File Structure** - `.agent-conventions/file-structure.md`
   - Directory organization and file placement rules
   - Import/dependency patterns
   - Configuration reference conventions

3. **Message Schemas** - `.agent-conventions/message-schemas.md`
   - All messages MUST be structured (YAML/JSON, not prose)
   - All messages MUST include metadata (sender, timestamp, message_id)
   - All messages MUST validate against schema before sending and upon receiving
   - Schema files in `.agent-conventions/schemas/`

4. **Coordination Protocols** - `.agent-conventions/coordination-protocols.md`
   - **Cue-Based Coordination:** WARNING/STANDBY/GO protocol for multi-agent actions
   - **Hub-and-Spoke:** Central communication routing
   - **Exception-Based Reporting:** Only report state changes, not steady state
   - **Dependency Sequencing:** Tasks execute in dependency order

5. **Error Handling** - `.agent-conventions/error-handling.md`
   - **Jidoka Philosophy:** Detect abnormalities immediately, stop before defects propagate
   - **4-Tier Escalation:** Self-recovery → Orchestrator → Tournant → Human
   - **Stop Conditions:** Schema validation fails, invariant violated, resource unavailable, timeout exceeded
   - **Recovery Strategies:** Retry with backoff, fallback, graceful degradation, escalation

## Message Validation

Before sending ANY message, agents MUST:
1. Validate against schema in `.agent-conventions/schemas/`
2. Add required metadata (message_id, timestamp) if missing
3. Route via hub according to message type

Upon receiving ANY message, agents MUST:
1. Validate structure against schema
2. Check message is addressed to them
3. Send error response if validation fails

## Schema Files

All message types have schemas:
- `schema-task.yaml` - Task assignment, update, complete, failed, handoff
- `schema-status.yaml` - Agent state changes (ready, busy, blocked, idle)
- `schema-coordination.yaml` - WARNING/STANDBY/GO/STOP coordination
- `schema-escalation.yaml` - Error, timeout, conflict, abnormality escalations
- `schema-acknowledgment.yaml` - Receipt, understanding, completion, refusal

## Enforcement

Convention violations will be:
1. Detected by validation tools
2. Escalated as errors
3. Blocked from entering the system
4. Logged for analysis

**Read all convention documents before implementing agent behavior.**
