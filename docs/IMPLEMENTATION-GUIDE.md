# Implementation Guide: The Magnificent Seven Agent Patterns

**Model**: Claude Opus 4.5 (claude-opus-4-5-20251101)
**Date**: 2026-01-20
**Purpose**: Practical implementation guide for building the top-scoring mental models into working agent systems

---

## ⚠️ IMPLEMENTATION DEFERRED - EXPERIMENTAL VALIDATION PHASE

**Status:** This implementation guide is **on hold** pending experimental validation.

**Rationale:** Following Boyd's OODA Loop, we identified that we were jumping from Observe (research) to Decide/Act (implementation) without sufficient Orient (empirical testing). This guide represents theory-driven implementation, but we don't yet know:
- Which models actually work best for AI agents in practice
- Which task types benefit from which coordination patterns
- Where models break at scale
- What the real bottlenecks and failure modes are

**Current Phase:** See `docs/EXPERIMENTAL-FRAMEWORK.md` for the testing approach that will validate (or invalidate) these recommendations.

**What we kept from this guide:**
- Day 1-2 foundation work (Shared Language/Grammar) - conventions and schemas are needed for any coordination model
- Core concepts and rationale - still valuable as hypotheses to test

**This guide will be revised** after Phase 3 (Experimental Testing) with data-driven recommendations based on actual test results.

---

## Overview

This guide provides concrete, step-by-step implementation instructions for the seven mental models that scored 25/25 in the prioritization analysis. These models form the foundation for effective AI agent orchestration.

**The Magnificent Seven:**
1. Shared Language/Grammar (Jazz) - Communication foundation
2. Central Communication Hub (Theater) - Architecture pattern
3. Jidoka (Lean Manufacturing) - Error handling
4. Station-Based Specialization (Kitchen) - Agent boundaries
5. Cue-Based Coordination (Theater) - Timing protocol
6. Master Cuelist (Theater) - Workflow documentation
7. Distributed Expertise with Central Coordination (Mission Control) - Scaling pattern

---

## Part I: Quick Start (Implementation Checklist)

### Week 1-2: Foundation

**Days 1-2: Shared Language/Grammar**
- [ ] Create `.agent-conventions/` directory structure
- [ ] Document naming conventions
- [ ] Define message schemas (JSON/YAML)
- [ ] Add conventions to CLAUDE.md
- [ ] Implement basic schema validation

**Days 3-4: Central Communication Hub**
- [ ] Design orchestrator agent role
- [ ] Define communication channels (status, escalation, task, broadcast)
- [ ] Implement hub-and-spoke message routing
- [ ] Create channel selection rules

**Day 5: Integration Testing**
- [ ] Test message flow through hub
- [ ] Verify convention compliance
- [ ] Document any gaps found

### Week 3-4: Error Handling & Specialization

**Days 6-8: Jidoka (Error Detection)**
- [ ] Define stop conditions and thresholds
- [ ] Implement anomaly detection checks
- [ ] Create escalation signal protocol
- [ ] Build tiered escalation system

**Days 9-12: Station-Based Specialization**
- [ ] Analyze constraint convergence for your domain
- [ ] Define 3-5 initial specialist agents
- [ ] Document agent boundaries (what each does/doesn't do)
- [ ] Create interface contracts between agents
- [ ] Implement tournant (generalist fallback) agent

**Days 13-14: Integration Testing**
- [ ] Test specialist handoffs
- [ ] Verify Jidoka stops propagate correctly
- [ ] Test fallback to tournant agent

### Week 5-6: Coordination

**Days 15-18: Cue-Based Coordination**
- [ ] Implement WARNING/STANDBY/GO protocol
- [ ] Create acknowledgment message types
- [ ] Define timing thresholds per task type
- [ ] Build auto-follow chain support

**Days 19-21: Master Cuelist**
- [ ] Document all workflows in cuelist format
- [ ] Implement hierarchical task numbering
- [ ] Add trigger conditions to each task
- [ ] Define contingency paths

### Week 7-8: Scaling & Optimization

**Days 22-28: Distributed Expertise**
- [ ] Implement full hub-and-spoke architecture
- [ ] Add hierarchical orchestration (if >10 agents)
- [ ] Create conflict resolution protocol
- [ ] Implement result aggregation
- [ ] Build measurement dashboard

**Days 29-30: Validation & Documentation**
- [ ] Run full integration tests
- [ ] Measure baseline metrics
- [ ] Document operational procedures
- [ ] Create runbooks for common failures

---

## Part II: The Magnificent Seven - Implementation Details

### 1. Shared Language/Grammar (Jazz)

**What You're Building:**
Explicit documentation of conventions that enable implicit coordination. When all agents "speak the same language," coordination overhead drops dramatically.

**Source:** `docs/jazz-improvisation/shared-language-grammar-agent-analysis.md`

#### Step 1: Create Convention Directory (Day 1)

```bash
# Create the conventions directory
mkdir -p .agent-conventions/

# Create core category files
touch .agent-conventions/naming.md
touch .agent-conventions/file-structure.md
touch .agent-conventions/error-handling.md
touch .agent-conventions/coordination-protocols.md
touch .agent-conventions/message-schemas.md
```

#### Step 2: Document Naming Conventions

```markdown
# .agent-conventions/naming.md

## File Naming
- Test files: `*.test.ts` (NOT `*.spec.ts`)
- Agent configs: `agent-*.yaml`
- Schemas: `schema-*.json`

## Variable Naming
- Booleans: `is*`, `has*`, `should*`
- Collections: plural nouns
- Constants: SCREAMING_SNAKE_CASE

## Task IDs
- Format: `DOMAIN-NNN` (e.g., `CODE-100`, `TEST-200`)
- Leave gaps for insertions (100, 200, 300)
- Use decimals for inserted tasks (100.5)

## Message Types
- Task dispatch: `task.*`
- Status updates: `status.*`
- Escalations: `escalation.*`
- Acknowledgments: `ack.*`

## Rationale
Each convention exists to reduce ambiguity and enable
agents to predict each other's behavior.
```

#### Step 3: Define Message Schemas

```yaml
# .agent-conventions/schemas/task-assignment.yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - message_id
  - timestamp
  - sender
  - recipient
  - message_type
  - task_id
  - description
properties:
  message_id:
    type: string
    format: uuid
  timestamp:
    type: string
    format: date-time
  sender:
    type: string
    description: "Agent ID of sender"
  recipient:
    type: string
    description: "Agent ID of recipient"
  message_type:
    type: string
    enum: ["task.assignment", "task.update", "task.complete"]
  task_id:
    type: string
    pattern: "^[A-Z]+-[0-9]+(\\.\\d+)*$"
  description:
    type: string
  priority:
    type: string
    enum: ["critical", "high", "normal", "low"]
    default: "normal"
  deadline:
    type: string
    format: date-time
  dependencies:
    type: array
    items:
      type: string
  context:
    type: object
```

#### Step 4: CLAUDE.md Integration

```markdown
# Add to your CLAUDE.md

## Shared Language

This codebase uses documented conventions in `.agent-conventions/`.

### Before Implementing
1. Read relevant convention docs
2. Follow conventions exactly (no variation)
3. If pattern isn't documented, ask before inventing

### Convention Categories
- Naming: `.agent-conventions/naming.md`
- File structure: `.agent-conventions/file-structure.md`
- Error handling: `.agent-conventions/error-handling.md`
- Coordination: `.agent-conventions/coordination-protocols.md`
- Schemas: `.agent-conventions/schemas/`

### Reserved Terms (NEVER use casually)
- "GO": Execution trigger (orchestrator only)
- "STOP": Immediate halt signal
- "ACKNOWLEDGED": Receipt confirmed
- "BLOCKED": Cannot proceed

### Message Format
Use structured YAML/JSON for inter-agent messages, not prose.

### Violation = Bug
Deviating from conventions is a defect, not a style choice.
```

#### Step 5: Validation Implementation

```python
# validate_conventions.py
import json
import jsonschema
from pathlib import Path

class ConventionValidator:
    def __init__(self, schema_dir: str = ".agent-conventions/schemas"):
        self.schema_dir = Path(schema_dir)
        self.schemas = self._load_schemas()

    def _load_schemas(self) -> dict:
        schemas = {}
        for schema_file in self.schema_dir.glob("*.json"):
            with open(schema_file) as f:
                schemas[schema_file.stem] = json.load(f)
        return schemas

    def validate_message(self, message: dict, schema_name: str) -> tuple[bool, str]:
        """Validate a message against a schema."""
        if schema_name not in self.schemas:
            return False, f"Unknown schema: {schema_name}"

        try:
            jsonschema.validate(message, self.schemas[schema_name])
            return True, "Valid"
        except jsonschema.ValidationError as e:
            return False, str(e.message)

    def check_naming_convention(self, name: str, convention_type: str) -> bool:
        """Check if a name follows conventions."""
        conventions = {
            "task_id": r"^[A-Z]+-[0-9]+(\.\d+)*$",
            "agent_id": r"^[a-z]+-agent(-[a-z]+)*$",
            "message_type": r"^[a-z]+\.[a-z_]+$"
        }
        import re
        pattern = conventions.get(convention_type)
        if not pattern:
            return True  # No convention defined
        return bool(re.match(pattern, name))

# Usage
validator = ConventionValidator()
is_valid, error = validator.validate_message(message, "task-assignment")
if not is_valid:
    raise ConventionViolation(f"Message validation failed: {error}")
```

#### Success Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Convention violations per task | <1% | Track validation failures |
| Schema compliance rate | 100% | Automated validation |
| "How should I..." decisions | Decreasing | Monitor agent clarification requests |
| Coordination message count | Decreasing | Count messages per task |

#### Common Pitfalls

1. **Too many conventions too fast** - Start with 10-15 core ones
2. **Conventions without rationale** - Agents need to understand why
3. **Unenforced conventions** - Validation must be automatic
4. **Natural language in messages** - Use structured formats

---

### 2. Central Communication Hub (Theater)

**What You're Building:**
A hub-and-spoke architecture where one orchestrator maintains complete informational centrality while specialized agents execute within their domains.

**Source:** `docs/theater-stage-management/central-communication-hub-agent-analysis.md`

#### Step 1: Design Hub Architecture

```
CENTRAL HUB (Orchestrator)
├── Receives all status updates
├── Filters information (exception-based)
├── Routes tasks to specialists
├── Maintains global state view
└── Issues coordinated commands

COMMUNICATION CHANNELS
├── Status Channel: Periodic state reports
├── Escalation Channel: Problems requiring attention
├── Task Channel: Work assignments
├── Broadcast Channel: System-wide announcements
└── Private Channel: Point-to-point (rare)
```

#### Step 2: Implement Channel Architecture

```python
# hub.py
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Dict, List
from queue import PriorityQueue
import asyncio

class ChannelType(Enum):
    TASK = "task"           # Orchestrator -> Agent
    STATUS = "status"       # Agent -> Orchestrator
    ESCALATION = "escalation"  # Agent -> Orchestrator (priority)
    BROADCAST = "broadcast"    # Orchestrator -> All
    PRIVATE = "private"        # Point-to-point

@dataclass
class Message:
    channel: ChannelType
    sender: str
    recipient: str  # or "ALL" for broadcast
    message_type: str
    payload: dict
    priority: int = 5  # 1=highest, 10=lowest
    timestamp: str = ""

class CentralHub:
    def __init__(self):
        self.agents: Dict[str, "Agent"] = {}
        self.message_queue: PriorityQueue = PriorityQueue()
        self.global_state: Dict[str, dict] = {}
        self.filters: Dict[str, Callable] = {}

    def register_agent(self, agent_id: str, agent: "Agent"):
        """Register an agent with the hub."""
        self.agents[agent_id] = agent
        self.global_state[agent_id] = {"status": "idle"}

    def route_message(self, message: Message):
        """Route a message through the hub."""
        # Apply filters
        if not self._should_process(message):
            return  # Filtered out

        # Update global state if status message
        if message.channel == ChannelType.STATUS:
            self._update_state(message)

        # Route based on channel type
        if message.channel == ChannelType.BROADCAST:
            for agent_id, agent in self.agents.items():
                if agent_id != message.sender:
                    agent.receive(message)
        elif message.channel == ChannelType.ESCALATION:
            # Priority handling - process immediately
            self._handle_escalation(message)
        else:
            # Normal routing
            if message.recipient in self.agents:
                self.agents[message.recipient].receive(message)

    def _should_process(self, message: Message) -> bool:
        """Apply exception-based filtering."""
        # Status messages: only process if non-nominal
        if message.channel == ChannelType.STATUS:
            if message.payload.get("status") == "nominal":
                # Just update state, don't process further
                self._update_state(message)
                return False
        return True

    def _update_state(self, message: Message):
        """Update global state from status message."""
        self.global_state[message.sender] = {
            "status": message.payload.get("status"),
            "last_update": message.timestamp,
            "task": message.payload.get("current_task")
        }

    def _handle_escalation(self, message: Message):
        """Handle escalation with priority."""
        # Log escalation
        print(f"ESCALATION from {message.sender}: {message.payload}")
        # Add to priority queue for orchestrator processing
        self.message_queue.put((message.priority, message))

    def get_system_status(self) -> dict:
        """Get aggregated system status."""
        return {
            "agents": self.global_state,
            "queue_depth": self.message_queue.qsize(),
            "agent_count": len(self.agents)
        }
```

#### Step 3: CLAUDE.md Template for Hub

```markdown
# Add to CLAUDE.md

## Hub Communication Protocol

### Channel Selection
| Message Type | Channel | Reason |
|--------------|---------|--------|
| Task dispatch | TASK | Work assignment |
| Progress update | STATUS | Routine reporting |
| Problem/blocker | ESCALATION | Requires decision |
| System alert | BROADCAST | All must know |
| Agent-specific config | PRIVATE | Only one recipient |

### Reporting Rules
- Report exceptions, not normal operation
- "Silence = nominal" is the default
- Include task_id in all messages
- Use structured format (no prose)

### Hub Responsibilities
- Aggregate status across agents
- Detect patterns in exceptions
- Route tasks by capability
- Maintain system-wide view
- Single point for human interface

### Agent Responsibilities
- Report to hub, not to each other
- Accept tasks from hub only
- Acknowledge all dispatches
- No direct agent-to-agent coordination (except within explicit scope)
```

#### Step 4: Implement Filtering Rules

```python
# filtering.py
class ExceptionBasedFilter:
    """Filter routine messages, pass exceptions."""

    def __init__(self):
        self.thresholds = {
            "duration_multiplier": 1.5,  # Report if >1.5x expected
            "error_rate": 0.05,          # Report if >5% errors
            "queue_depth": 10,           # Report if queue >10
        }

    def should_report(self, event: dict) -> bool:
        """Determine if event should be reported to hub."""
        # Always report state changes
        if event.get("is_state_change"):
            return True

        # Always report problems
        if event.get("is_error") or event.get("is_blocked"):
            return True

        # Report threshold breaches
        if event.get("duration", 0) > event.get("expected_duration", 1) * self.thresholds["duration_multiplier"]:
            return True

        if event.get("error_rate", 0) > self.thresholds["error_rate"]:
            return True

        # Otherwise, don't report
        return False
```

#### Success Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Hub availability | 99.9% | <99% |
| Message latency | <100ms | >500ms |
| Filter ratio | >80% routine filtered | <60% |
| Routing accuracy | >95% | <90% |

#### Common Pitfalls

1. **Hub overload** - Filter more aggressively
2. **Single point of failure** - Plan failover/redundancy
3. **Information loss** - Don't filter too aggressively
4. **Peer coordination** - All coordination must go through hub

---

### 3. Jidoka (Lean Manufacturing)

**What You're Building:**
"Automation with a human touch" - agents that detect abnormalities, stop immediately, and signal for help rather than propagating errors.

**Source:** `docs/lean-manufacturing/jidoka-automation-with-human-touch-agent-analysis.md`

#### Step 1: Define Stop Conditions

```yaml
# .agent-conventions/jidoka-stop-conditions.yaml
stop_conditions:
  confidence:
    threshold: 0.7
    description: "Stop if confidence below 70%"

  consistency:
    check: "output_contradicts_prior"
    description: "Stop if output contradicts documented patterns"

  scope:
    check: "exceeds_defined_boundaries"
    description: "Stop if task requires changes beyond scope"

  risk:
    check: "irreversible_high_stakes"
    description: "Stop before irreversible high-stakes actions"

  resource:
    token_usage_multiplier: 3.0
    time_multiplier: 2.0
    description: "Stop if resource consumption exceeds 3x/2x expected"

  novelty:
    check: "pattern_not_seen_before"
    description: "Stop on novel situations outside training"

escalation_tiers:
  tier_1:
    name: "Proceed with Note"
    conditions: "low_stakes AND moderate_confidence"
    action: "Log concern, continue, flag for batch review"

  tier_2:
    name: "Checkpoint and Continue"
    conditions: "moderate_stakes OR low_confidence"
    action: "Save state, note concerns, continue with human review flag"

  tier_3:
    name: "Pause and Request Input"
    conditions: "high_stakes OR very_low_confidence"
    action: "Stop, preserve context, wait for human"

  tier_4:
    name: "Abort and Alert"
    conditions: "critical_stakes OR detected_danger"
    action: "Stop immediately, alert human, do not continue"
```

#### Step 2: Implement Anomaly Detection

```python
# jidoka.py
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List

class EscalationTier(Enum):
    PROCEED_WITH_NOTE = 1
    CHECKPOINT_CONTINUE = 2
    PAUSE_REQUEST_INPUT = 3
    ABORT_ALERT = 4

@dataclass
class AbnormalitySignal:
    trigger_type: str  # confidence, consistency, scope, risk, resource, novelty
    trigger_details: str
    current_state: dict
    suggested_actions: List[str]
    tier: EscalationTier

class JidokaDetector:
    def __init__(self, config: dict):
        self.config = config
        self.confidence_threshold = config.get("confidence_threshold", 0.7)
        self.resource_multiplier = config.get("resource_multiplier", 3.0)

    def check(self, context: dict) -> Optional[AbnormalitySignal]:
        """Run all abnormality checks. Return signal if any fail."""

        # Confidence check
        if context.get("confidence", 1.0) < self.confidence_threshold:
            return self._create_signal(
                "confidence",
                f"Confidence {context['confidence']:.2f} below threshold {self.confidence_threshold}",
                context,
                self._determine_tier(context, "confidence")
            )

        # Consistency check
        if self._check_consistency_violation(context):
            return self._create_signal(
                "consistency",
                "Output contradicts prior outputs or documented patterns",
                context,
                EscalationTier.PAUSE_REQUEST_INPUT
            )

        # Scope check
        if context.get("scope_exceeded"):
            return self._create_signal(
                "scope",
                f"Task requires changes beyond scope: {context.get('scope_violation')}",
                context,
                EscalationTier.PAUSE_REQUEST_INPUT
            )

        # Risk check
        if context.get("irreversible") and context.get("high_stakes"):
            return self._create_signal(
                "risk",
                "Irreversible high-stakes action detected",
                context,
                EscalationTier.ABORT_ALERT
            )

        # Resource check
        if context.get("token_usage", 0) > context.get("expected_tokens", 1000) * self.resource_multiplier:
            return self._create_signal(
                "resource",
                f"Token usage {context['token_usage']} exceeds {self.resource_multiplier}x expected",
                context,
                EscalationTier.CHECKPOINT_CONTINUE
            )

        return None  # All checks passed

    def _check_consistency_violation(self, context: dict) -> bool:
        """Check for consistency with prior outputs."""
        # Implementation would compare against stored patterns
        return context.get("contradicts_prior", False)

    def _determine_tier(self, context: dict, trigger_type: str) -> EscalationTier:
        """Determine escalation tier based on context."""
        stakes = context.get("stakes", "moderate")
        confidence = context.get("confidence", 0.5)

        if stakes == "critical":
            return EscalationTier.ABORT_ALERT
        elif stakes == "high" or confidence < 0.5:
            return EscalationTier.PAUSE_REQUEST_INPUT
        elif stakes == "moderate" or confidence < 0.7:
            return EscalationTier.CHECKPOINT_CONTINUE
        else:
            return EscalationTier.PROCEED_WITH_NOTE

    def _create_signal(self, trigger_type: str, details: str,
                       context: dict, tier: EscalationTier) -> AbnormalitySignal:
        """Create an abnormality signal with suggested actions."""
        suggestions = {
            EscalationTier.PROCEED_WITH_NOTE: ["Log concern", "Continue execution", "Flag for review"],
            EscalationTier.CHECKPOINT_CONTINUE: ["Save state", "Note concerns", "Continue with review flag"],
            EscalationTier.PAUSE_REQUEST_INPUT: ["Stop execution", "Preserve context", "Wait for human input"],
            EscalationTier.ABORT_ALERT: ["Stop immediately", "Alert human", "Do not continue"]
        }

        return AbnormalitySignal(
            trigger_type=trigger_type,
            trigger_details=details,
            current_state=context,
            suggested_actions=suggestions[tier],
            tier=tier
        )
```

#### Step 3: CLAUDE.md Template for Jidoka

```markdown
# Add to CLAUDE.md

## Error Handling: Jidoka Protocol

### Stop Conditions
Stop and escalate when:

1. **Confidence**: You are <70% confident in your approach
2. **Consistency**: Your output contradicts documented patterns
3. **Scope**: Task requires changes beyond specified scope
4. **Risk**: Action is irreversible and high-stakes
5. **Resource**: Consumption exceeds 3x expected
6. **Novelty**: Pattern not seen before

### Escalation Tiers

**Tier 1 - Proceed with Note** (low stakes, moderate confidence)
- Log the concern
- Continue execution
- Flag for batch review later

**Tier 2 - Checkpoint and Continue** (moderate stakes OR low confidence)
- Save current state
- Note concerns in output
- Continue but flag for human review

**Tier 3 - Pause and Request Input** (high stakes OR very low confidence)
- Stop execution immediately
- Preserve full context
- Wait for explicit human approval

**Tier 4 - Abort and Alert** (critical stakes OR detected danger)
- Stop immediately
- Alert human operator
- Do NOT continue without explicit restart

### On Stop - Provide:
- What you were trying to accomplish
- Why you stopped (which condition triggered)
- Current state snapshot
- Suggested recovery options
- What information would help proceed

### Never:
- Attempt automatic recovery from anomalies
- Continue after detecting problems
- Clean up state before signaling (preserve evidence)
- Assume the anomaly is benign
```

#### Success Metrics

| Metric | Target | Warning Sign |
|--------|--------|--------------|
| Escalation rate | 5-20% | <1% or >50% |
| Escalation precision | >70% true problems | <50% |
| Escalation recall | >90% problems caught | <70% |
| Detection latency | <1s | >10s |
| Hidden failure rate | <5% | >10% |

#### Common Pitfalls

1. **Thresholds too low** - Stops too often, loses productivity
2. **Thresholds too high** - Misses real problems
3. **Incomplete signals** - Not providing enough context for resolution
4. **Cleaning up state** - Destroying evidence needed for debugging

---

### 4. Station-Based Specialization (Kitchen)

**What You're Building:**
Agents with clear domain boundaries where boundaries emerge from constraint convergence—not arbitrary assignment.

**Source:** `docs/kitchen-brigade/station-based-specialization-agent-analysis.md`

#### Step 1: Analyze Constraint Convergence

Before defining agents, analyze where constraints naturally cluster:

```markdown
## Constraint Analysis Worksheet

### Capability Constraints (Tools)
- What tools does each task type require?
- Group tasks by tool requirements

### Data Domain Constraints
- What data does each task type access?
- Who owns (write) vs reads data?

### Technique Constraints
- What reasoning patterns work for each domain?
- What validation approaches apply?

### Timing Constraints
- Fast tasks (<5s)?
- Deliberative tasks (minutes)?
- Batch tasks (hours)?

### Security Constraints
- What isolation is required?
- What approval gates?

### Convergence Points
Where 3+ constraint types cluster = natural agent boundary
```

#### Step 2: Define Specialist Agents

```yaml
# .agent-conventions/agents/code-agent.yaml
agent:
  id: code-agent
  type: specialist

domain:
  owns:
    - "Source code files"
    - "Configuration files"
  reads:
    - "Documentation"
    - "Test results"
  cannot_access:
    - "Production credentials"
    - "User data"

capabilities:
  tools:
    - file_read
    - file_write
    - code_execution
    - git_operations
  techniques:
    - "AST analysis"
    - "Pattern matching"
    - "Refactoring"

timing:
  profile: deliberative
  expected_latency: "30s-5min"
  timeout: "10min"

boundaries:
  does:
    - "Write and modify code"
    - "Refactor existing code"
    - "Fix bugs in code"
  does_not:
    - "Write documentation (-> doc-agent)"
    - "Write tests (-> test-agent)"
    - "Deploy code (-> deploy-agent)"
    - "Make architectural decisions (-> orchestrator)"

interface:
  inputs:
    - type: task_assignment
      required: [task_id, description, file_paths]
  outputs:
    - type: task_complete
      includes: [changed_files, summary, confidence]

handoff_protocol:
  to_test_agent:
    trigger: "Code changes complete"
    provides: [changed_files, change_summary]
  to_doc_agent:
    trigger: "API changes"
    provides: [api_changes, code_comments]
```

#### Step 3: Implement Tournant (Fallback) Agent

```yaml
# .agent-conventions/agents/tournant-agent.yaml
agent:
  id: tournant-agent
  type: generalist-fallback

role:
  description: "Handle tasks outside specialist boundaries or overflow"

capabilities:
  can_cover:
    - code-agent (at reduced quality)
    - test-agent (at reduced quality)
    - doc-agent (at reduced quality)
  proficiency: "Acceptable but not specialist-level"

activation_triggers:
  - "Specialist agent timeout (>60s)"
  - "Specialist agent error rate (>10%)"
  - "Queue depth at specialist (>5 tasks)"
  - "Task type not matching any specialist"
  - "Explicit orchestrator assignment"

limitations:
  - "Not for recurring work (specialize instead)"
  - "Not for high-quality requirements"
  - "Not for security-sensitive work"

escalation:
  threshold: "If tournant confidence <60%"
  action: "Escalate to human"
```

#### Step 4: Define Interface Contracts

```python
# contracts.py
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AgentOutput:
    """Standard output format for all specialist agents."""
    agent_id: str
    task_id: str
    status: str  # complete, partial, blocked, failed
    confidence: float  # 0.0 to 1.0
    summary: str
    outputs: dict  # Agent-specific outputs
    dependencies_discovered: List[str]
    caveats: List[str]

@dataclass
class HandoffPackage:
    """Standard handoff between agents."""
    source_agent: str
    target_agent: str
    task_id: str
    context: dict  # What the receiving agent needs
    outputs_from_source: dict
    expected_action: str

class StationContract:
    """Enforce station boundaries and contracts."""

    def __init__(self, agent_config: dict):
        self.agent_id = agent_config["agent"]["id"]
        self.domain = agent_config["domain"]
        self.boundaries = agent_config["boundaries"]

    def validate_task(self, task: dict) -> tuple[bool, str]:
        """Check if task is within this agent's domain."""
        task_type = task.get("type", "")

        # Check if explicitly in our domain
        if task_type in self.boundaries.get("does", []):
            return True, "In domain"

        # Check if explicitly NOT in our domain
        for excluded in self.boundaries.get("does_not", []):
            if task_type in excluded:
                return False, f"Outside domain: {excluded}"

        # Ambiguous - request clarification
        return False, "Ambiguous task - request routing clarification"

    def validate_output(self, output: AgentOutput) -> bool:
        """Validate output meets contract requirements."""
        required_fields = ["agent_id", "task_id", "status", "confidence", "summary"]
        for field in required_fields:
            if not getattr(output, field, None):
                return False
        return True
```

#### Step 5: CLAUDE.md Template for Stations

```markdown
# Add to CLAUDE.md

## Station: [STATION_NAME]

### Domain Definition
**Owns (read/write):**
- [List data/files this agent owns]

**Reads (read-only):**
- [List data/files this agent can read]

**Cannot Access:**
- [List explicitly excluded data]

### Boundaries
**This agent DOES:**
- [List responsibilities]

**This agent DOES NOT (route to other agents):**
- [Responsibility] → [other-agent]
- [Responsibility] → [other-agent]

### Input Requirements
- task_id: Required
- description: Required
- [domain-specific inputs]

### Output Format
```yaml
agent_id: [this agent]
task_id: [from input]
status: complete|partial|blocked|failed
confidence: 0.0-1.0
summary: "One sentence summary"
outputs:
  [domain-specific outputs]
caveats:
  - [Any limitations or uncertainties]
```

### Handoff Protocol
When handing off to another agent:
1. Verify your work is complete
2. Package outputs in standard format
3. Include context the receiving agent needs
4. Signal orchestrator, not the receiving agent directly
```

#### Success Metrics

| Metric | Target | Alert |
|--------|--------|-------|
| Domain coverage | 100% tasks fit a station | Orphan tasks appearing |
| Boundary clarity | No overlaps | Duplicate processing |
| Context efficiency | <60% window per agent | Context overflow |
| Handoff success rate | >99% | Integration failures |

---

### 5. Cue-Based Coordination (Theater)

**What You're Building:**
A three-phase commitment protocol (WARNING/STANDBY/GO) that enables precise triggering with preparation time.

**Source:** `docs/theater-stage-management/cue-based-coordination-agent-analysis.md`

#### Step 1: Implement Three-Phase Protocol

```python
# cue_protocol.py
from enum import Enum
from dataclasses import dataclass
from typing import Optional
import asyncio

class CuePhase(Enum):
    PLANNED = "planned"
    WARNED = "warned"
    STANDBY = "standby"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"

@dataclass
class CueMessage:
    phase: str  # warning, standby, go
    task_id: str
    agent_id: str
    payload: Optional[dict] = None
    estimated_start_seconds: Optional[int] = None

@dataclass
class CueAck:
    task_id: str
    agent_id: str
    phase: str
    status: str  # preparing, ready, not_ready, executing
    ready_in_seconds: Optional[int] = None
    reason: Optional[str] = None

class CueCoordinator:
    def __init__(self, hub: "CentralHub"):
        self.hub = hub
        self.task_states: dict[str, CuePhase] = {}
        self.pending_acks: dict[str, asyncio.Future] = {}

    async def execute_task(self, task_id: str, agent_id: str,
                          payload: dict, use_warning: bool = True) -> dict:
        """Execute a task using the three-phase protocol."""

        # Phase 1: WARNING (if needed)
        if use_warning:
            warning_ack = await self._send_warning(task_id, agent_id, payload)
            if warning_ack.status == "failed":
                return {"status": "failed", "phase": "warning", "reason": warning_ack.reason}

            # Wait for preparation
            await asyncio.sleep(warning_ack.ready_in_seconds or 30)

        # Phase 2: STANDBY
        standby_ack = await self._send_standby(task_id, agent_id, payload)
        if standby_ack.status != "ready":
            return {"status": "failed", "phase": "standby", "reason": standby_ack.reason}

        # Phase 3: GO
        result = await self._send_go(task_id, agent_id)
        return result

    async def _send_warning(self, task_id: str, agent_id: str,
                           payload: dict) -> CueAck:
        """Send WARNING and wait for ACK."""
        self.task_states[task_id] = CuePhase.WARNED

        message = CueMessage(
            phase="warning",
            task_id=task_id,
            agent_id=agent_id,
            estimated_start_seconds=60,
            payload=payload
        )

        # Create future for ACK
        ack_future = asyncio.Future()
        self.pending_acks[f"{task_id}:warning"] = ack_future

        # Send message
        self.hub.route_message(message)

        # Wait for ACK with timeout
        try:
            ack = await asyncio.wait_for(ack_future, timeout=10.0)
            return ack
        except asyncio.TimeoutError:
            return CueAck(task_id=task_id, agent_id=agent_id,
                         phase="warning", status="failed",
                         reason="ACK timeout")

    async def _send_standby(self, task_id: str, agent_id: str,
                           payload: dict) -> CueAck:
        """Send STANDBY and wait for ready confirmation."""
        self.task_states[task_id] = CuePhase.STANDBY

        message = CueMessage(
            phase="standby",
            task_id=task_id,
            agent_id=agent_id,
            payload=payload
        )

        ack_future = asyncio.Future()
        self.pending_acks[f"{task_id}:standby"] = ack_future

        self.hub.route_message(message)

        try:
            ack = await asyncio.wait_for(ack_future, timeout=5.0)
            return ack
        except asyncio.TimeoutError:
            return CueAck(task_id=task_id, agent_id=agent_id,
                         phase="standby", status="not_ready",
                         reason="ACK timeout")

    async def _send_go(self, task_id: str, agent_id: str) -> dict:
        """Send GO and wait for execution result."""
        self.task_states[task_id] = CuePhase.RUNNING

        message = CueMessage(
            phase="go",
            task_id=task_id,
            agent_id=agent_id
        )

        self.hub.route_message(message)

        # Agent executes and reports completion through normal channels
        # This would integrate with the hub's completion tracking
        return {"status": "executing", "task_id": task_id}

    def receive_ack(self, ack: CueAck):
        """Process an acknowledgment from an agent."""
        key = f"{ack.task_id}:{ack.phase}"
        if key in self.pending_acks:
            self.pending_acks[key].set_result(ack)
```

#### Step 2: Implement Auto-Follow Chains

```python
# autofollow.py
from dataclasses import dataclass
from typing import List, Optional
import asyncio

@dataclass
class ChainStep:
    task_id: str
    agent_id: str
    delay_seconds: float = 0
    condition: Optional[str] = None  # e.g., "previous.success"

@dataclass
class AutoFollowChain:
    chain_id: str
    steps: List[ChainStep]

class ChainExecutor:
    def __init__(self, coordinator: CueCoordinator):
        self.coordinator = coordinator
        self.active_chains: dict[str, bool] = {}

    async def execute_chain(self, chain: AutoFollowChain) -> dict:
        """Execute an auto-follow chain from a single trigger."""
        self.active_chains[chain.chain_id] = True
        results = []

        for i, step in enumerate(chain.steps):
            # Check if chain was cancelled
            if not self.active_chains.get(chain.chain_id):
                return {"status": "cancelled", "completed_steps": results}

            # Wait for delay
            if step.delay_seconds > 0:
                await asyncio.sleep(step.delay_seconds)

            # Check condition
            if step.condition and not self._evaluate_condition(step.condition, results):
                continue  # Skip this step

            # Execute step (skip warning for chain steps - already committed)
            result = await self.coordinator.execute_task(
                step.task_id,
                step.agent_id,
                {},  # Payload from chain config
                use_warning=False  # Auto-follow skips warning
            )

            results.append({"step": i, "task_id": step.task_id, "result": result})

            if result.get("status") == "failed":
                # Chain failed - stop execution
                return {"status": "failed", "failed_at": i, "results": results}

        return {"status": "complete", "results": results}

    def cancel_chain(self, chain_id: str):
        """Cancel an active chain."""
        self.active_chains[chain_id] = False

    def _evaluate_condition(self, condition: str, results: list) -> bool:
        """Evaluate a condition based on previous results."""
        if condition == "previous.success":
            return results and results[-1].get("result", {}).get("status") != "failed"
        return True
```

#### Step 3: CLAUDE.md Template for Cues

```markdown
# Add to CLAUDE.md

## Cue Protocol

### Three-Phase Protocol

**WARNING (t-60s):**
- Orchestrator sends warning with context
- Agent begins resource allocation
- Agent loads required context
- Agent responds with readiness estimate

**STANDBY (t-10s):**
- Orchestrator sends standby
- Agent confirms ready or not_ready
- If not_ready: include reason
- Resources locked, no new preparation

**GO (t=0):**
- Orchestrator sends go
- Agent executes immediately
- No clarification requests allowed
- Report completion when done

### Agent Response to Cues

**On WARNING:**
```yaml
type: warning_ack
task_id: [from warning]
status: preparing
ready_in_seconds: 30
```

**On STANDBY:**
```yaml
type: standby_ack
task_id: [from standby]
status: ready  # or not_ready
can_execute: true
reason: null  # or reason if not_ready
```

**On GO:**
- Execute immediately
- No acknowledgment (execution IS acknowledgment)
- Report completion through status channel

### When to Skip Phases

Skip WARNING for:
- Fast tasks (<5 seconds)
- Pre-prepared resources
- Auto-follow chain steps

Skip STANDBY for:
- Very fast tasks (<3 seconds)
- Stateless operations
- Already-confirmed readiness

### Reserved Word: "GO"
- ONLY orchestrator sends "go" messages
- Agents must NEVER use "go" in communications
- Use alternatives: "proceed", "continue", "begin"
```

#### Success Metrics

| Metric | Target | Alert |
|--------|--------|-------|
| Warning-to-ready time | <60s | >120s |
| Standby ACK rate | >99% | <95% |
| Go-to-execution latency | <100ms | >500ms |
| Chain completion rate | >99% | <95% |

---

### 6. Master Cuelist (Theater)

**What You're Building:**
Comprehensive workflow documentation that serves as the "program" for agent orchestration.

**Source:** `docs/theater-stage-management/master-cuelist-agent-analysis.md`

#### Step 1: Create Cuelist Schema

```yaml
# .agent-conventions/schemas/cuelist-entry.yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - task_id
  - description
  - trigger
  - agent
properties:
  task_id:
    type: string
    pattern: "^[A-Z]+-[0-9]+(\\.\\d+)*$"
    description: "Hierarchical task ID (e.g., CODE-100, CODE-100.5)"

  description:
    type: string
    description: "Human-readable task description"

  trigger:
    type: object
    properties:
      type:
        type: string
        enum: ["conditional", "timed", "manual", "autofollow"]
      conditions:
        type: array
        items:
          type: object
      after_task:
        type: string
      delay_seconds:
        type: number

  agent:
    type: string
    description: "Agent ID to execute this task"

  warning_seconds:
    type: integer
    default: 60

  dependencies:
    type: array
    items:
      type: string

  intent:
    type: object
    properties:
      purpose:
        type: string
      importance:
        type: string
        enum: ["required", "important", "optional"]
      alternatives:
        type: array
        items:
          type: string

  success_criteria:
    type: array
    items:
      type: string

  on_failure:
    type: object
    properties:
      retry:
        type: integer
      fallback:
        type: string
      skip_if:
        type: string

  autofollow:
    type: array
    items:
      type: object
      properties:
        task:
          type: string
        delay_seconds:
          type: number
        condition:
          type: string
```

#### Step 2: Example Cuelist

```yaml
# workflows/feature-implementation.cuelist.yaml
cuelist:
  id: feature-implementation
  version: "1.0.0"
  phase: development  # development, staging, production

tasks:
  - task_id: CODE-100
    description: "Analyze existing codebase patterns"
    trigger:
      type: manual
    agent: code-agent
    warning_seconds: 30
    intent:
      purpose: "Understand existing patterns before making changes"
      importance: required
    success_criteria:
      - "Pattern analysis complete"
      - "Recommendations documented"
    on_failure:
      retry: 2

  - task_id: CODE-200
    description: "Implement feature code"
    trigger:
      type: conditional
      conditions:
        - task: CODE-100
          state: complete
    agent: code-agent
    dependencies:
      - CODE-100
    warning_seconds: 60
    intent:
      purpose: "Create the feature implementation"
      importance: required
    success_criteria:
      - "Code compiles"
      - "No linting errors"
    on_failure:
      retry: 1
      fallback: "CODE-200-ALT"
    autofollow:
      - task: TEST-300
        delay_seconds: 5

  - task_id: TEST-300
    description: "Generate and run tests"
    trigger:
      type: autofollow
      after_task: CODE-200
    agent: test-agent
    dependencies:
      - CODE-200
    warning_seconds: 30
    intent:
      purpose: "Ensure code works correctly"
      importance: required
    success_criteria:
      - "Tests pass"
      - "Coverage meets threshold"

  - task_id: DOC-400
    description: "Update documentation"
    trigger:
      type: conditional
      conditions:
        - task: TEST-300
          state: complete
        - task: CODE-200
          output: api_changes_detected
    agent: doc-agent
    dependencies:
      - CODE-200
      - TEST-300
    warning_seconds: 30
    intent:
      purpose: "Keep documentation in sync"
      importance: important
    on_failure:
      skip_if: "no_api_changes"
```

#### Step 3: Cuelist Executor

```python
# cuelist_executor.py
import yaml
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class CuelistTask:
    task_id: str
    description: str
    trigger: dict
    agent: str
    dependencies: List[str]
    intent: dict
    success_criteria: List[str]
    on_failure: dict
    autofollow: List[dict]
    warning_seconds: int = 60

class CuelistExecutor:
    def __init__(self, coordinator: "CueCoordinator", hub: "CentralHub"):
        self.coordinator = coordinator
        self.hub = hub
        self.task_states: Dict[str, str] = {}
        self.task_outputs: Dict[str, dict] = {}

    def load_cuelist(self, filepath: str) -> List[CuelistTask]:
        """Load cuelist from YAML file."""
        with open(filepath) as f:
            data = yaml.safe_load(f)

        tasks = []
        for task_data in data.get("tasks", []):
            tasks.append(CuelistTask(
                task_id=task_data["task_id"],
                description=task_data["description"],
                trigger=task_data.get("trigger", {}),
                agent=task_data["agent"],
                dependencies=task_data.get("dependencies", []),
                intent=task_data.get("intent", {}),
                success_criteria=task_data.get("success_criteria", []),
                on_failure=task_data.get("on_failure", {}),
                autofollow=task_data.get("autofollow", []),
                warning_seconds=task_data.get("warning_seconds", 60)
            ))
        return tasks

    async def execute_cuelist(self, tasks: List[CuelistTask]) -> dict:
        """Execute a cuelist, respecting dependencies and triggers."""
        results = {}

        for task in tasks:
            # Check trigger conditions
            if not self._check_trigger(task):
                continue

            # Check dependencies
            if not self._check_dependencies(task):
                results[task.task_id] = {"status": "blocked", "reason": "Dependencies not met"}
                continue

            # Execute task
            result = await self._execute_task(task)
            results[task.task_id] = result

            # Handle failure
            if result["status"] == "failed":
                recovery = await self._handle_failure(task, result)
                results[task.task_id] = recovery

        return results

    def _check_trigger(self, task: CuelistTask) -> bool:
        """Check if task's trigger conditions are met."""
        trigger = task.trigger
        trigger_type = trigger.get("type", "manual")

        if trigger_type == "manual":
            return True  # Manual tasks always ready

        if trigger_type == "conditional":
            for condition in trigger.get("conditions", []):
                dep_task = condition.get("task")
                required_state = condition.get("state", "complete")
                if self.task_states.get(dep_task) != required_state:
                    return False
            return True

        if trigger_type == "autofollow":
            after_task = trigger.get("after_task")
            return self.task_states.get(after_task) == "complete"

        return False

    def _check_dependencies(self, task: CuelistTask) -> bool:
        """Check if all dependencies are met."""
        for dep in task.dependencies:
            if self.task_states.get(dep) != "complete":
                return False
        return True

    async def _execute_task(self, task: CuelistTask) -> dict:
        """Execute a single task using cue protocol."""
        result = await self.coordinator.execute_task(
            task.task_id,
            task.agent,
            {"description": task.description, "intent": task.intent},
            use_warning=True
        )

        self.task_states[task.task_id] = result.get("status", "unknown")
        self.task_outputs[task.task_id] = result

        return result

    async def _handle_failure(self, task: CuelistTask, result: dict) -> dict:
        """Handle task failure according to on_failure rules."""
        on_failure = task.on_failure

        # Try retries
        retry_count = on_failure.get("retry", 0)
        for i in range(retry_count):
            retry_result = await self._execute_task(task)
            if retry_result["status"] != "failed":
                return retry_result

        # Try fallback
        fallback = on_failure.get("fallback")
        if fallback:
            # Execute fallback task (would need to look it up)
            pass

        # Check skip condition
        skip_if = on_failure.get("skip_if")
        if skip_if and self._evaluate_condition(skip_if):
            return {"status": "skipped", "reason": skip_if}

        return result

    def _evaluate_condition(self, condition: str) -> bool:
        """Evaluate a condition string."""
        # Simple implementation - would be more sophisticated in production
        return False
```

#### Step 4: CLAUDE.md Template for Cuelist

```markdown
# Add to CLAUDE.md

## Workflow Documentation (Master Cuelist)

### Cuelist Structure
Every workflow must be documented in `.workflows/` as a cuelist:

```yaml
task_id: DOMAIN-NNN      # Hierarchical ID
description: "What"       # Human-readable
trigger:                  # When to execute
  type: conditional
  conditions: [...]
agent: agent-id           # Who executes
dependencies: [...]       # What must complete first
intent:                   # Why this exists
  purpose: "..."
  importance: required|important|optional
success_criteria: [...]   # How to know it worked
on_failure:              # What to do if it fails
  retry: N
  fallback: "task-id"
```

### Numbering Convention
- Use DOMAIN-NNN format (CODE-100, TEST-200)
- Leave gaps for insertions (100, 200, 300)
- Use decimals for inserted tasks (100.5)
- NEVER renumber existing tasks

### Trigger Types
- **conditional**: When specified conditions met
- **timed**: At specific time/interval
- **manual**: Human-initiated
- **autofollow**: Automatic after previous task

### Required Fields
- task_id, description, agent, trigger (minimum)
- intent.purpose, intent.importance (for all non-trivial tasks)
- success_criteria (for all production tasks)

### Documentation Rule
- Every workflow must be in cuelist
- No undocumented agent actions
- Update cuelist BEFORE changing workflow
```

---

### 7. Distributed Expertise with Central Coordination (Mission Control)

**What You're Building:**
The complete hub-and-spoke architecture where specialist agents report to a central orchestrator.

**Source:** `docs/mission-control/distributed-expertise-central-coordination-agent-analysis.md`

#### Step 1: Orchestrator Design

```python
# orchestrator.py
from dataclasses import dataclass
from typing import List, Dict, Optional
import asyncio

@dataclass
class TaskAssignment:
    task_id: str
    agent_id: str
    description: str
    context: dict
    constraints: dict
    authority_boundaries: dict
    escalation_criteria: List[str]
    output_format: dict

class Orchestrator:
    """Central coordinator following Mission Control principles."""

    def __init__(self, hub: "CentralHub", coordinator: "CueCoordinator"):
        self.hub = hub
        self.coordinator = coordinator
        self.agents: Dict[str, dict] = {}  # agent_id -> capabilities
        self.active_tasks: Dict[str, dict] = {}
        self.global_context: dict = {}

    async def execute_mission(self, goal: str, context: dict) -> dict:
        """Execute a mission by decomposing, assigning, and integrating."""

        # Phase 1: Decomposition
        tasks = self._decompose_goal(goal, context)

        # Phase 2: Assignment
        assignments = self._assign_tasks(tasks)

        # Phase 3: Parallel Execution
        results = await self._execute_tasks(assignments)

        # Phase 4: Integration
        integrated = self._integrate_results(results)

        return integrated

    def _decompose_goal(self, goal: str, context: dict) -> List[dict]:
        """Decompose goal into agent-sized tasks."""
        # This would use an LLM or rule-based decomposition
        # Returns list of task specifications
        return []

    def _assign_tasks(self, tasks: List[dict]) -> List[TaskAssignment]:
        """Assign tasks to appropriate agents."""
        assignments = []
        for task in tasks:
            agent_id = self._select_agent(task)
            assignments.append(TaskAssignment(
                task_id=task["id"],
                agent_id=agent_id,
                description=task["description"],
                context=self._prepare_context(task),
                constraints=task.get("constraints", {}),
                authority_boundaries=self._get_authority(agent_id),
                escalation_criteria=self._get_escalation_criteria(task),
                output_format=self._get_output_format(agent_id)
            ))
        return assignments

    def _select_agent(self, task: dict) -> str:
        """Select best agent for task based on capabilities."""
        task_type = task.get("type", "general")
        for agent_id, capabilities in self.agents.items():
            if task_type in capabilities.get("domains", []):
                return agent_id
        return "tournant-agent"  # Fallback

    def _prepare_context(self, task: dict) -> dict:
        """Prepare context for agent, respecting context budget."""
        # Context budget: ~20% of agent's context window
        context = {
            "task_background": task.get("background", ""),
            "relevant_outputs": self._get_relevant_outputs(task),
            "global_constraints": self.global_context.get("constraints", {})
        }
        return context

    async def _execute_tasks(self, assignments: List[TaskAssignment]) -> Dict[str, dict]:
        """Execute tasks, some in parallel where possible."""
        # Group by dependencies
        independent = [a for a in assignments if not self._has_dependencies(a)]
        dependent = [a for a in assignments if self._has_dependencies(a)]

        results = {}

        # Execute independent tasks in parallel
        parallel_results = await asyncio.gather(
            *[self._execute_single(a) for a in independent]
        )
        for assignment, result in zip(independent, parallel_results):
            results[assignment.task_id] = result

        # Execute dependent tasks sequentially
        for assignment in dependent:
            if self._dependencies_met(assignment, results):
                result = await self._execute_single(assignment)
                results[assignment.task_id] = result

        return results

    async def _execute_single(self, assignment: TaskAssignment) -> dict:
        """Execute a single task using cue protocol."""
        return await self.coordinator.execute_task(
            assignment.task_id,
            assignment.agent_id,
            {
                "description": assignment.description,
                "context": assignment.context,
                "constraints": assignment.constraints,
                "output_format": assignment.output_format
            }
        )

    def _integrate_results(self, results: Dict[str, dict]) -> dict:
        """Integrate results from all agents."""
        # Conflict detection
        conflicts = self._detect_conflicts(results)

        # Gap detection
        gaps = self._detect_gaps(results)

        # Synthesis
        integrated = {
            "summary": self._synthesize_summary(results),
            "key_findings": self._extract_findings(results),
            "conflicts": conflicts,
            "gaps": gaps,
            "confidence": self._aggregate_confidence(results),
            "raw_results": results
        }

        return integrated

    def _detect_conflicts(self, results: Dict[str, dict]) -> List[dict]:
        """Detect conflicts between agent outputs."""
        conflicts = []
        result_list = list(results.items())
        for i, (id1, r1) in enumerate(result_list):
            for id2, r2 in result_list[i+1:]:
                if self._outputs_conflict(r1, r2):
                    conflicts.append({
                        "agents": [id1, id2],
                        "nature": "conflicting outputs"
                    })
        return conflicts

    def _detect_gaps(self, results: Dict[str, dict]) -> List[str]:
        """Detect gaps in coverage."""
        # Compare expected outputs to actual
        return []

    def _outputs_conflict(self, r1: dict, r2: dict) -> bool:
        """Check if two outputs conflict."""
        # Implementation would compare outputs semantically
        return False

    def _synthesize_summary(self, results: Dict[str, dict]) -> str:
        """Create integrated summary from all results."""
        summaries = [r.get("summary", "") for r in results.values()]
        return " ".join(summaries)  # Would be more sophisticated

    def _extract_findings(self, results: Dict[str, dict]) -> List[str]:
        """Extract and deduplicate key findings."""
        findings = []
        for result in results.values():
            findings.extend(result.get("findings", []))
        return list(set(findings))

    def _aggregate_confidence(self, results: Dict[str, dict]) -> float:
        """Aggregate confidence across agents."""
        confidences = [r.get("confidence", 0.5) for r in results.values()]
        if not confidences:
            return 0.5
        return sum(confidences) / len(confidences)

    def _has_dependencies(self, assignment: TaskAssignment) -> bool:
        """Check if assignment has dependencies."""
        return bool(assignment.context.get("dependencies", []))

    def _dependencies_met(self, assignment: TaskAssignment, results: dict) -> bool:
        """Check if all dependencies are satisfied."""
        deps = assignment.context.get("dependencies", [])
        return all(d in results for d in deps)

    def _get_relevant_outputs(self, task: dict) -> dict:
        """Get outputs from other agents relevant to this task."""
        return {}

    def _get_authority(self, agent_id: str) -> dict:
        """Get authority boundaries for agent."""
        return self.agents.get(agent_id, {}).get("authority", {})

    def _get_escalation_criteria(self, task: dict) -> List[str]:
        """Get escalation criteria for task."""
        return [
            "Confidence below 70%",
            "Task cannot be completed as specified",
            "Cross-agent dependency discovered",
            "Novel situation outside training"
        ]

    def _get_output_format(self, agent_id: str) -> dict:
        """Get expected output format for agent."""
        return {
            "required": ["status", "confidence", "summary", "findings"],
            "optional": ["caveats", "dependencies_discovered"]
        }
```

#### Step 2: CLAUDE.md Template for Orchestrator

```markdown
# Add to CLAUDE.md (for orchestrator agent)

## Orchestrator Role

### Responsibilities
- Decompose goals into agent-sized tasks
- Assign tasks to appropriate specialists
- Coordinate cross-agent dependencies
- Integrate results from multiple agents
- Handle conflicts and gaps
- Interface with human

### What Orchestrator DOES
- Initial task decomposition
- Task assignment and routing
- Cross-agent conflict resolution
- Result integration and synthesis
- Escalation decisions
- Human communication

### What Orchestrator Does NOT Do
- Execute specialist tasks directly
- Micromanage agent execution
- Re-check work it can't evaluate
- Hold information agents need (route directly)
- Make decisions agents can make

### Information Flow

**Provide to agents:**
- Clear goal description
- Relevant context (within budget)
- Constraints and boundaries
- Authority boundaries
- Escalation criteria
- Output format requirements

**Receive from agents:**
- Task status (complete/partial/blocked/failed)
- Confidence level
- Key findings
- Dependencies discovered
- Caveats and uncertainties

### The Bottleneck Rule
The orchestrator is the limiting factor. Minimize what flows through it.
- Use exception-based reporting
- Enable direct agent-to-agent handoffs where possible
- Batch coordination at checkpoints
- Reserve orchestrator for true coordination
```

---

## Part III: Integration Patterns

### How the Seven Work Together

```
┌─────────────────────────────────────────┐
│     SHARED LANGUAGE/GRAMMAR             │
│  (Foundation for all communication)      │
└───────────────────┬─────────────────────┘
                    │
┌───────────────────▼─────────────────────┐
│     CENTRAL COMMUNICATION HUB           │
│   (Architecture for coordination)        │
└───────────────────┬─────────────────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
┌─────────┐  ┌───────────┐  ┌─────────────┐
│ STATION │  │DISTRIBUTED│  │ CUE-BASED   │
│ SPECIAL │◄►│ EXPERTISE │◄►│COORDINATION │
│ -IZATION│  │ + CENTRAL │  │             │
└────┬────┘  └─────┬─────┘  └──────┬──────┘
     │             │               │
     └─────────────┼───────────────┘
                   │
    ┌──────────────▼──────────────────┐
    │        MASTER CUELIST           │
    │  (Documentation of all workflows)│
    └──────────────┬──────────────────┘
                   │
    ┌──────────────▼──────────────────┐
    │           JIDOKA                │
    │    (Error handling throughout)   │
    └─────────────────────────────────┘
```

### Integration Checklist

**Week 1-2: Foundation Layer**
- [ ] Shared Language enables Hub communication
- [ ] Hub implements Station boundaries
- [ ] Jidoka integrated into all agents

**Week 3-4: Coordination Layer**
- [ ] Cue Protocol uses Shared Language messages
- [ ] Master Cuelist documents all workflows
- [ ] Stations execute Cuelist tasks

**Week 5-6: Scaling Layer**
- [ ] Distributed Expertise built on Hub
- [ ] Hierarchical orchestration if >10 agents
- [ ] Full integration testing

### Dependencies Between Models

| Model | Depends On | Enables |
|-------|------------|---------|
| Shared Language | - | All others |
| Central Hub | Shared Language | Station routing, Cue distribution |
| Jidoka | Shared Language | Safe autonomy |
| Station Specialization | Hub | Distributed Expertise |
| Cue-Based Coordination | Shared Language, Hub | Master Cuelist |
| Master Cuelist | All above | Production workflows |
| Distributed Expertise | All above | Scale |

### Potential Conflicts

1. **Hub bottleneck vs. Station autonomy**
   - Resolution: Exception-based reporting, direct handoffs within scope

2. **Jidoka stops vs. Cue timing**
   - Resolution: Jidoka takes precedence; missed cues trigger recovery

3. **Cuelist rigidity vs. adaptation**
   - Resolution: Intent metadata enables intelligent deviation

---

## Part IV: Validation Framework

### Leading Indicators (Early Signs)

| Model | Leading Indicator | Target | Warning |
|-------|-------------------|--------|---------|
| Shared Language | Convention violation rate | <1% | >5% |
| Hub | Message latency | <100ms | >500ms |
| Jidoka | Escalation rate | 5-20% | <1% or >50% |
| Station | Boundary collision rate | <5% | >10% |
| Cue | ACK success rate | >99% | <95% |
| Cuelist | Coverage rate | 100% | <90% |
| Distributed | Orchestrator load | <40% | >70% |

### Lagging Indicators (Outcomes)

| Model | Lagging Indicator | Target | Warning |
|-------|-------------------|--------|---------|
| Shared Language | Coordination time | Decreasing | Increasing |
| Hub | System throughput | Increasing | Plateaued |
| Jidoka | Hidden failure rate | <5% | >10% |
| Station | Task completion rate | >95% | <90% |
| Cue | Execution sync variance | <100ms | >500ms |
| Cuelist | Workflow success rate | >95% | <90% |
| Distributed | Integration quality | >90% | <80% |

### Diagnostic Tests

**For Shared Language:**
```bash
# Random audit: Do 10 random messages follow all conventions?
python scripts/audit_conventions.py --sample 10

# Cross-agent check: Do agents make same naming choices?
python scripts/consistency_check.py
```

**For Jidoka:**
```bash
# Inject known anomalies, verify detection
python scripts/test_jidoka.py --inject-anomalies

# Check escalation quality
python scripts/review_escalations.py --last 7d
```

---

## Part V: Troubleshooting Guide

### Common Implementation Failures

#### Failure: Agents Ignore Conventions
**Symptom:** Violation rate >5%
**Root Cause:** Conventions not in CLAUDE.md or not enforced
**Fix:**
1. Verify conventions are in CLAUDE.md
2. Add automated validation
3. Make validation fail loudly
4. Track violations as bugs

#### Failure: Hub Becomes Bottleneck
**Symptom:** Queue depth >10, latency >500ms
**Root Cause:** Too much routing through hub
**Fix:**
1. Increase filtering (exception-based only)
2. Enable direct agent-to-agent for within-scope handoffs
3. Add hierarchical orchestration (domain orchestrators)
4. Batch non-urgent updates

#### Failure: Jidoka Stops Too Often
**Symptom:** Escalation rate >50%
**Root Cause:** Thresholds too sensitive
**Fix:**
1. Analyze false positives
2. Raise confidence threshold (70% → 60%)
3. Add context-specific thresholds
4. Improve agent calibration

#### Failure: Jidoka Misses Problems
**Symptom:** Hidden failure rate >10%
**Root Cause:** Thresholds too permissive or checks incomplete
**Fix:**
1. Analyze missed failures
2. Add detection rules for missed patterns
3. Lower thresholds where appropriate
4. Add novel failure detection

#### Failure: Station Boundaries Unclear
**Symptom:** Tasks falling through cracks, duplicate processing
**Root Cause:** Boundaries not explicitly documented
**Fix:**
1. Document boundary cases explicitly
2. Create default owner for ambiguous cases
3. Add tournant agent for edge cases
4. Review and refine boundaries weekly

#### Failure: Cue Protocol Timeouts
**Symptom:** ACK timeout rate >5%
**Root Cause:** Agents not responding in time
**Fix:**
1. Increase timeout thresholds
2. Add agent health monitoring
3. Pre-warm agents before critical sequences
4. Implement failover to alternate agents

#### Failure: Cuelist Staleness
**Symptom:** Workflows don't match cuelist
**Root Cause:** Changes made without updating documentation
**Fix:**
1. Make cuelist update mandatory before changes
2. Add automated cuelist validation
3. Regular cuelist audits
4. Version control all cuelists

---

## Part VI: Measurement Dashboard

### Recommended Metrics

```markdown
## Daily Dashboard

### Shared Language Metrics
- Convention violations: X/day (target: <5)
- Schema validation failures: X/day (target: 0)
- New conventions needed: X/week (track emerging patterns)

### Hub Metrics
- Messages through hub: X/hour
- Hub processing latency: Xms p50, Xms p99 (target: <100ms)
- Filter ratio: X% filtered (target: >80%)
- Queue depth: X messages (target: <10)

### Jidoka Metrics
- Escalation rate: X% (target: 5-20%)
- True positive rate: X% (target: >70%)
- Mean time to resolution: X minutes
- Hidden failures discovered: X/week (target: <5)

### Station Metrics
- Tasks per station: X/day
- Boundary collisions: X/day (target: <5)
- Tournant usage: X% (target: <10%)
- Handoff success rate: X% (target: >99%)

### Cue Metrics
- Warning ACK rate: X% (target: >99%)
- Standby ready rate: X% (target: >99%)
- Go-to-execution latency: Xms (target: <100ms)
- Chain completion rate: X% (target: >99%)

### Cuelist Metrics
- Workflow coverage: X% (target: 100%)
- Cuelist freshness: X days since update
- Trigger accuracy: X% correct evaluations

### Orchestrator Metrics
- Tasks coordinated: X/hour
- Integration success rate: X%
- Conflict detection rate: X/integration
- Human escalation rate: X%
```

---

## Part VII: Code Examples Summary

All code examples in this guide:

1. **validate_conventions.py** - Convention validation
2. **hub.py** - Central Communication Hub
3. **filtering.py** - Exception-based filtering
4. **jidoka.py** - Anomaly detection
5. **contracts.py** - Station interface contracts
6. **cue_protocol.py** - Three-phase coordination
7. **autofollow.py** - Auto-follow chains
8. **cuelist_executor.py** - Cuelist execution
9. **orchestrator.py** - Central orchestration

---

## Part VIII: References

### Source Documents

| Model | Source Document |
|-------|-----------------|
| Shared Language/Grammar | `docs/jazz-improvisation/shared-language-grammar-agent-analysis.md` |
| Central Communication Hub | `docs/theater-stage-management/central-communication-hub-agent-analysis.md` |
| Jidoka | `docs/lean-manufacturing/jidoka-automation-with-human-touch-agent-analysis.md` |
| Station-Based Specialization | `docs/kitchen-brigade/station-based-specialization-agent-analysis.md` |
| Cue-Based Coordination | `docs/theater-stage-management/cue-based-coordination-agent-analysis.md` |
| Master Cuelist | `docs/theater-stage-management/master-cuelist-agent-analysis.md` |
| Distributed Expertise | `docs/mission-control/distributed-expertise-central-coordination-agent-analysis.md` |

### Related Documents

- Prioritization Analysis: `docs/AGENT-MODEL-PRIORITIZATION.md`
- Problem-Research Mapping: `.claude/problem-research-mapping.md`
- Synthesis Documents: `docs/syntheses/`

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Practical implementation guide for the Magnificent Seven agent patterns
**Status:** Complete
