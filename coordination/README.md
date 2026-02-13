# Agent Coordination System

This directory contains the core coordination infrastructure for the AgentModel system.

## Setup

Install dependencies:

```bash
# Create virtual environment (first time only)
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Unix/macOS
# OR
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

## Message Validation

All agent messages MUST validate against schemas in `.agent-conventions/schemas/`.

### Usage

```python
from coordination.validate_message import validate_message, validate_and_prepare, ValidationError

# Example 1: Validate existing message
message = {
    "message_id": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-01-20T14:30:00Z",
    "sender": "orchestrator-main",
    "recipient": "specialist-code",
    "message_type": "task.assignment",
    "task_id": "CODE-100",
    "task": {
        "description": "Implement authentication",
        "priority": "high"
    }
}

try:
    validate_message(message)
    print("Message is valid")
except ValidationError as e:
    print(f"Validation failed: {e}")

# Example 2: Add metadata and validate in one step
minimal_message = {
    "sender": "specialist-code",
    "recipient": "orchestrator-main",
    "message_type": "status.ready",
    "status": "ready"
}

try:
    prepared = validate_and_prepare(minimal_message)
    # prepared now has message_id and timestamp added
    send_to_hub(prepared)
except ValidationError as e:
    print(f"Validation failed: {e}")
```

### Testing

Run the validation tests:

```bash
.venv/bin/python coordination/validate_message.py
```

Expected output:
```
✓ Task message is valid
✓ Invalid message correctly rejected: Missing required fields: message_id, timestamp, recipient
✓ Status message is valid
✓ Minimal message prepared and validated
  Added message_id: [uuid]
  Added timestamp: [timestamp]
```

## Directory Structure

```
coordination/
├── README.md              # This file
├── validate_message.py    # Message schema validator
├── hub/                   # Central communication hub (TBD)
├── protocols/             # Coordination protocols (TBD)
└── escalation/            # Jidoka escalation handlers (TBD)
```

## Conventions

All code in this directory MUST follow conventions in `.agent-conventions/`:
- Naming conventions
- File structure
- Message schemas
- Coordination protocols
- Error handling (Jidoka)

**Convention violations are defects, not style choices.**

## Next Steps (Day 3-4)

- Design orchestrator agent role
- Implement central communication hub
- Create hub-and-spoke message routing
- Define channel selection rules
