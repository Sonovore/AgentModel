#!/usr/bin/env python3
"""
Message Schema Validator

Validates agent messages against YAML schemas in .agent-conventions/schemas/.

Usage:
    from coordination.validate_message import validate_message, ValidationError

    try:
        validate_message(message_dict)
        print("Message is valid")
    except ValidationError as e:
        print(f"Validation failed: {e}")

Philosophy:
    - Prevention > Detection > Resolution
    - Messages must validate BEFORE sending and UPON receiving
    - Schema violations are defects, not warnings
"""

import json
import uuid
import yaml
from datetime import datetime, UTC
from pathlib import Path
from typing import Dict, Any, Optional
from jsonschema import validate, ValidationError as JsonSchemaValidationError, Draft202012Validator


class ValidationError(Exception):
    """Raised when message validation fails."""
    pass


class SchemaLoader:
    """Loads and caches YAML schemas from .agent-conventions/schemas/"""

    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.schema_dir = self.project_root / ".agent-conventions" / "schemas"
        self._schema_cache = {}

    def load_schema(self, message_type: str) -> Dict[str, Any]:
        """
        Load schema for given message type.

        Args:
            message_type: Message type in dot notation (e.g., "task.assignment")

        Returns:
            Schema dictionary

        Raises:
            ValidationError: If schema file not found or invalid
        """
        # Map message type to schema file
        schema_mapping = {
            "task": "schema-task.yaml",
            "status": "schema-status.yaml",
            "coord": "schema-coordination.yaml",
            "escalation": "schema-escalation.yaml",
            "ack": "schema-acknowledgment.yaml",
        }

        category = message_type.split(".")[0]
        schema_filename = schema_mapping.get(category)

        if not schema_filename:
            raise ValidationError(f"Unknown message category: {category}")

        # Check cache
        if schema_filename in self._schema_cache:
            return self._schema_cache[schema_filename]

        # Load from file
        schema_path = self.schema_dir / schema_filename
        if not schema_path.exists():
            raise ValidationError(f"Schema file not found: {schema_path}")

        try:
            with open(schema_path, "r") as f:
                schema = yaml.safe_load(f)
            self._schema_cache[schema_filename] = schema
            return schema
        except Exception as e:
            raise ValidationError(f"Failed to load schema {schema_filename}: {e}")


# Global schema loader instance
_schema_loader = SchemaLoader()


def validate_message(message: Dict[str, Any]) -> None:
    """
    Validate message against its schema.

    Args:
        message: Message dictionary to validate

    Raises:
        ValidationError: If message does not conform to schema
    """
    # Check basic structure
    if not isinstance(message, dict):
        raise ValidationError(f"Message must be a dictionary, got {type(message)}")

    required_base_fields = ["message_id", "timestamp", "sender", "recipient", "message_type"]
    missing_fields = [f for f in required_base_fields if f not in message]
    if missing_fields:
        raise ValidationError(f"Missing required fields: {', '.join(missing_fields)}")

    # Validate message_type format
    message_type = message.get("message_type")
    if not isinstance(message_type, str) or "." not in message_type:
        raise ValidationError(
            f"message_type must be in dot notation (category.type), got: {message_type}"
        )

    # Load schema for this message type
    try:
        schema = _schema_loader.load_schema(message_type)
    except ValidationError as e:
        raise ValidationError(f"Schema loading failed: {e}")

    # Validate against JSON Schema
    try:
        validator = Draft202012Validator(schema)
        validator.validate(message)
    except JsonSchemaValidationError as e:
        # Format error message with path and details
        path = ".".join(str(p) for p in e.path) if e.path else "root"
        raise ValidationError(
            f"Schema validation failed at '{path}': {e.message}\n"
            f"Failed value: {e.instance}"
        )


def add_metadata(message: Dict[str, Any]) -> Dict[str, Any]:
    """
    Add required metadata fields to message if missing.

    Args:
        message: Message dictionary

    Returns:
        Message with metadata added
    """
    if "message_id" not in message:
        message["message_id"] = str(uuid.uuid4())

    if "timestamp" not in message:
        message["timestamp"] = datetime.now(UTC).isoformat().replace("+00:00", "Z")

    return message


def validate_and_prepare(message: Dict[str, Any]) -> Dict[str, Any]:
    """
    Add metadata if missing, then validate message.

    Convenience function for sending messages.

    Args:
        message: Message dictionary to prepare and validate

    Returns:
        Validated message with metadata

    Raises:
        ValidationError: If validation fails
    """
    message = add_metadata(message)
    validate_message(message)
    return message


def format_validation_error(error: ValidationError) -> Dict[str, Any]:
    """
    Format validation error as an escalation message.

    Args:
        error: ValidationError instance

    Returns:
        Escalation message dictionary
    """
    return {
        "message_type": "escalation.error",
        "severity": "HIGH",
        "category": "validation",
        "description": f"Message validation failed: {str(error)}",
        "context": {
            "operation": "Message validation",
            "expected": "Message conforming to schema",
            "actual": "Schema validation error",
        },
        "suggested_action": "Review message structure against schema documentation",
        "can_retry": False,
        "requires_human": True,
    }


# Example usage
if __name__ == "__main__":
    # Example: Valid task assignment message
    task_message = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "sender": "orchestrator-main",
        "recipient": "specialist-code",
        "message_type": "task.assignment",
        "task_id": "CODE-100",
        "task": {
            "description": "Implement user authentication",
            "priority": "high",
            "dependencies": ["CODE-050"],
            "acceptance_criteria": [
                "User can log in with email/password",
                "Session persists across page reloads",
            ],
        },
    }

    try:
        validate_message(task_message)
        print("✓ Task message is valid")
    except ValidationError as e:
        print(f"✗ Validation failed: {e}")

    # Example: Invalid message (missing required field)
    invalid_message = {
        "message_type": "task.assignment",
        "sender": "orchestrator-main",
        # Missing: message_id, timestamp, recipient, task_id
    }

    try:
        validate_message(invalid_message)
        print("✓ Invalid message passed validation (THIS SHOULD NOT HAPPEN)")
    except ValidationError as e:
        print(f"✓ Invalid message correctly rejected: {e}")

    # Example: Status message
    status_message = {
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "sender": "specialist-code",
        "recipient": "orchestrator-main",
        "message_type": "status.busy",
        "status": "busy",
        "context": {
            "current_task": "CODE-100",
            "capacity": {
                "current_load": 75,
                "available_capacity": 25,
            },
        },
    }

    try:
        validate_message(status_message)
        print("✓ Status message is valid")
    except ValidationError as e:
        print(f"✗ Validation failed: {e}")

    # Example: Using validate_and_prepare
    minimal_message = {
        "sender": "specialist-test",
        "recipient": "orchestrator-main",
        "message_type": "status.ready",
        "status": "ready",
    }

    try:
        prepared = validate_and_prepare(minimal_message)
        print(f"✓ Minimal message prepared and validated")
        print(f"  Added message_id: {prepared['message_id']}")
        print(f"  Added timestamp: {prepared['timestamp']}")
    except ValidationError as e:
        print(f"✗ Preparation failed: {e}")
