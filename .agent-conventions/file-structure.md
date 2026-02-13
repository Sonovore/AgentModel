# File Structure Conventions

**Purpose:** Define consistent file organization patterns that make code predictable and navigable for agents.

## Directory Structure

```
project-root/
├── .agent-conventions/       # This directory - conventions documentation
│   ├── *.md                 # Convention category docs
│   └── schemas/             # Message and data schemas
├── agents/                   # Agent definitions and configurations
│   ├── orchestrator/        # Orchestrator agent config
│   ├── specialists/         # Specialist agent configs
│   └── tournant/            # Generalist fallback config
├── workflows/                # Cuelist and workflow definitions
│   ├── cuelists/            # Master cuelists for common tasks
│   └── templates/           # Workflow templates
├── coordination/             # Coordination infrastructure
│   ├── hub/                 # Central communication hub
│   ├── protocols/           # Cue-based coordination protocols
│   └── escalation/          # Jidoka escalation handlers
└── monitoring/               # Measurement and validation
    ├── metrics/             # Metric collection
    └── dashboards/          # Monitoring dashboards
```

## File Placement Rules

### Agent Configurations

- **Location:** `agents/{role}/`
- **Format:** YAML files
- **Naming:** `agent-{name}.yaml`
- **Example:** `agents/specialists/agent-code-reviewer.yaml`

### Message Schemas

- **Location:** `.agent-conventions/schemas/`
- **Format:** JSON Schema or YAML
- **Naming:** `schema-{message-type}.{yaml|json}`
- **Example:** `.agent-conventions/schemas/schema-task-assignment.yaml`

### Cuelists (Workflows)

- **Location:** `workflows/cuelists/`
- **Format:** YAML
- **Naming:** `cuelist-{workflow-name}.yaml`
- **Example:** `workflows/cuelists/cuelist-code-review-process.yaml`

### Coordination Protocols

- **Location:** `coordination/protocols/`
- **Format:** YAML or Python modules
- **Naming:** `{protocol-name}-protocol.yaml` or `{protocol-name}_protocol.py`
- **Example:** `coordination/protocols/cue-based-protocol.yaml`

## File Organization Principles

### 1. Separation of Concerns

- **Configuration** (YAML) separate from **implementation** (code)
- **Conventions** (documentation) separate from **enforcement** (validators)
- **Workflows** (cuelists) separate from **execution** (agents)

### 2. Discoverability

- Related files grouped in same directory
- Naming patterns indicate purpose
- README.md in each major directory explaining contents

### 3. Version Control Friendly

- Text formats (YAML, JSON, Markdown) preferred over binary
- One logical unit per file (don't combine multiple agents in one config)
- Small files over large monoliths

## Import/Dependency Conventions

### Python Imports

```python
# Standard library
import json
from pathlib import Path

# Third-party
import yaml
from jsonschema import validate

# Project - absolute imports from project root
from agents.orchestrator import OrchestratorAgent
from coordination.hub import CentralHub
from coordination.protocols.cue_protocol import CueBasedProtocol
```

### Configuration References

Use relative paths from project root:

```yaml
# In agent config
specializations:
  - schema: .agent-conventions/schemas/schema-task-assignment.yaml
  - workflow: workflows/cuelists/cuelist-standard-task.yaml
```

## Rationale

- **Predictable structure** enables agents to locate files without searching
- **Consistent naming** allows pattern-matching and automation
- **Clear boundaries** prevent files from being placed incorrectly
- **Separation of concerns** makes it clear what can change independently

## Validation

- All files must be in their designated locations
- Naming patterns must match conventions
- Directory structure should match the template above
