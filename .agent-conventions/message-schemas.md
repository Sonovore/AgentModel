# Message Schemas

**Purpose:** Define the structure and validation rules for all inter-agent messages.

## Schema Philosophy

**All messages MUST:**
1. **Be structured** (YAML/JSON, not prose)
2. **Include metadata** (sender, timestamp, message ID)
3. **Validate against schema** (before sending and upon receiving)
4. **Follow naming conventions** (message_type dot notation)

## Common Message Structure

All messages share this base structure:

```yaml
message_id: "uuid-v4-string"
timestamp: "2026-01-20T10:30:00Z"  # ISO 8601 UTC
sender: "agent-id-kebab-case"
recipient: "agent-id-kebab-case"  # or "broadcast" for all agents
message_type: "category.specific-type"
# ... message-specific fields
```

## Message Categories

### Task Messages

**Purpose:** Assign, update, and track task execution

**Types:**
- `task.assignment` - Initial task dispatch
- `task.update` - Progress update or modification
- `task.complete` - Task finished successfully
- `task.failed` - Task could not be completed
- `task.handoff` - Transfer task to different agent

**Schema:** `.agent-conventions/schemas/schema-task.yaml`

### Status Messages

**Purpose:** Report agent state changes

**Types:**
- `status.ready` - Agent available for work
- `status.busy` - Agent executing task
- `status.blocked` - Agent waiting on dependency
- `status.idle` - Agent has no assigned work

**Schema:** `.agent-conventions/schemas/schema-status.yaml`

### Coordination Messages

**Purpose:** Synchronize multi-agent actions

**Types:**
- `coord.warning` - Prepare for coordinated action
- `coord.standby` - Ready and awaiting go signal
- `coord.go` - Execute coordinated action
- `coord.stop` - Halt current operation

**Schema:** `.agent-conventions/schemas/schema-coordination.yaml`

### Escalation Messages

**Purpose:** Report errors and abnormalities

**Types:**
- `escalation.error` - Error requiring intervention
- `escalation.timeout` - Operation exceeded time limit
- `escalation.conflict` - Resource or timing conflict
- `escalation.abnormality` - Unexpected but non-critical condition

**Schema:** `.agent-conventions/schemas/schema-escalation.yaml`

### Acknowledgment Messages

**Purpose:** Confirm message receipt and understanding

**Types:**
- `ack.received` - Message received (may not understand yet)
- `ack.understood` - Message understood, will comply
- `ack.completed` - Requested action completed
- `ack.refused` - Cannot comply with request

**Schema:** `.agent-conventions/schemas/schema-acknowledgment.yaml`

## Schema Locations

All schemas are in `.agent-conventions/schemas/`:

```
.agent-conventions/schemas/
├── schema-task.yaml
├── schema-status.yaml
├── schema-coordination.yaml
├── schema-escalation.yaml
└── schema-acknowledgment.yaml
```

## Validation Process

### Sending Agent

```python
# Before sending any message
def send_message(message: dict) -> None:
    # 1. Validate against schema
    schema = load_schema(message["message_type"])
    if not validate(message, schema):
        raise ValidationError("Message does not match schema")

    # 2. Add required metadata if missing
    if "message_id" not in message:
        message["message_id"] = str(uuid.uuid4())
    if "timestamp" not in message:
        message["timestamp"] = datetime.utcnow().isoformat() + "Z"

    # 3. Send via hub
    hub.route_message(message)
```

### Receiving Agent

```python
# Upon receiving any message
def receive_message(message: dict) -> None:
    # 1. Validate structure
    schema = load_schema(message["message_type"])
    if not validate(message, schema):
        # Send error back to sender
        send_error_response(message, "Schema validation failed")
        return

    # 2. Check message is for this agent
    if message["recipient"] not in [agent.id, "broadcast"]:
        raise ValueError("Message not addressed to this agent")

    # 3. Process message
    handle_message(message)
```

## Schema Versioning

Schemas may evolve over time. Version them:

```yaml
# In schema file
$schema: "https://json-schema.org/draft/2020-12/schema"
$id: "https://project/schemas/task/v2"
version: "2.0.0"
# ... rest of schema
```

### Compatibility Rules

- **Patch version (2.0.X):** Backwards compatible (add optional fields only)
- **Minor version (2.X.0):** Backwards compatible (deprecate but don't remove)
- **Major version (X.0.0):** Breaking changes (require migration)

## Example: Task Assignment Message

```yaml
message_id: "550e8400-e29b-41d4-a716-446655440000"
timestamp: "2026-01-20T14:30:00Z"
sender: "orchestrator-main"
recipient: "specialist-code"
message_type: "task.assignment"
task:
  task_id: "CODE-100"
  description: "Implement user authentication feature"
  priority: "high"
  deadline: "2026-01-21T14:30:00Z"
  dependencies:
    - "CODE-050"  # Design doc must be complete
  context:
    repository: "https://github.com/org/repo"
    branch: "feature/auth"
    acceptance_criteria:
      - "User can log in with email/password"
      - "Session persists across page reloads"
      - "Password reset functionality works"
  resources:
    - type: "file"
      path: "docs/auth-design.md"
    - type: "api"
      endpoint: "https://api.service.com/auth"
```

## Example: Escalation Message

```yaml
message_id: "650e8400-e29b-41d4-a716-446655440001"
timestamp: "2026-01-20T15:45:00Z"
sender: "specialist-code"
recipient: "orchestrator-main"
message_type: "escalation.error"
error:
  severity: "HIGH"
  category: "resource"
  task_id: "CODE-100"
  description: "Cannot access required API endpoint"
  context:
    operation: "Authentication API call"
    expected: "200 OK response"
    actual: "503 Service Unavailable"
    endpoint: "https://api.service.com/auth"
  suggested_action: "Verify API service is running or provide alternative endpoint"
  can_retry: true
  retry_after: "2026-01-20T16:00:00Z"  # Retry in 15 minutes
  requires_human: false  # Orchestrator can resolve
```

## Rationale

- **Structured formats** enable validation and tooling
- **Schemas prevent malformed messages** from entering the system
- **Common structure** reduces cognitive load
- **Validation at boundaries** catches errors early
- **Versioning allows evolution** without breaking existing agents

## Validation

- Every message type has a schema
- All messages validate before being sent
- All messages validate upon receipt
- Schema violations are escalated as errors
