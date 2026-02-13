# Naming Conventions

**Purpose:** Establish consistent naming patterns that enable agents to predict behavior and reduce coordination overhead.

## File Naming

- **Test files:** `*.test.ts` (NOT `*.spec.ts`)
- **Agent configs:** `agent-*.yaml`
- **Schemas:** `schema-*.json` or `schema-*.yaml`
- **Convention docs:** `*.md` in `.agent-conventions/`

## Variable Naming

- **Booleans:** `is*`, `has*`, `should*`, `can*`
  - Examples: `isComplete`, `hasErrors`, `shouldRetry`
- **Collections:** Plural nouns (NOT singular with `List` suffix)
  - Examples: `tasks`, `agents`, `messages` (NOT `taskList`)
- **Constants:** SCREAMING_SNAKE_CASE
  - Examples: `MAX_RETRIES`, `DEFAULT_TIMEOUT`
- **Functions/Methods:** Verb phrases in camelCase
  - Examples: `executeTask`, `validateMessage`, `escalateError`

## Task IDs

- **Format:** `DOMAIN-NNN` where DOMAIN is 3-4 uppercase letters, NNN is 3+ digits
  - Examples: `CODE-100`, `TEST-200`, `DOC-300`
- **Leave gaps:** Use 100, 200, 300 (NOT 1, 2, 3) to allow insertions
- **Inserted tasks:** Use decimals for tasks added between planned tasks
  - Example: If you need a task between CODE-100 and CODE-200, use CODE-100.5

## Message Types

Use dot notation for hierarchical classification:

- **Task dispatch:** `task.assignment`, `task.update`, `task.complete`
- **Status updates:** `status.progress`, `status.blocked`, `status.ready`
- **Escalations:** `escalation.error`, `escalation.timeout`, `escalation.conflict`
- **Acknowledgments:** `ack.received`, `ack.understood`, `ack.completed`
- **Coordination:** `coord.warning`, `coord.standby`, `coord.go`

## Agent IDs

- **Format:** `role-identifier` in kebab-case
  - Examples: `orchestrator-main`, `specialist-code`, `specialist-test`
- **Reserved IDs:**
  - `orchestrator` or `orchestrator-*`: Central coordinator
  - `tournant` or `tournant-*`: Generalist fallback agents
  - `hub` or `hub-*`: Communication hub components

## Reserved Terms

**NEVER use these casually in messages or variable names. They have specific protocol meanings:**

- **GO:** Execution trigger (orchestrator only)
- **STOP:** Immediate halt signal (Jidoka)
- **WARNING:** Preparation phase beginning (cue protocol)
- **STANDBY:** Ready to execute, awaiting GO (cue protocol)
- **ACKNOWLEDGED:** Receipt confirmed with understanding
- **BLOCKED:** Cannot proceed, requires intervention
- **ESCALATE:** Route to higher authority
- **CRITICAL:** Highest priority, immediate attention

## Rationale

Each convention exists to:
1. **Reduce ambiguity** - Agents know what to expect
2. **Enable prediction** - Agents can anticipate each other's behavior
3. **Prevent conflicts** - Clear boundaries prevent stepping on each other
4. **Support tooling** - Consistent patterns enable automation

## Validation

Convention violations are defects, not style choices. All agent messages should be validated against documented conventions before being processed.
