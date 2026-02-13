# Failure Mode Detection Research

**Research Date:** 2026-01-21
**Purpose:** Map research failure modes to our system and design detection strategies

---

## Executive Summary

**Key findings:**
- **14 failure modes identified** from 1,642 multi-agent execution traces
- **9 modes detectable automatically** via message analysis and state tracking
- **5 modes require semantic analysis** (harder to detect programmatically)
- **Detection approach:** Rule-based for simple patterns, statistical for complex

**Recommendation:** Implement **rule-based detector** for 9 detectable modes, log others for manual review

---

## Part 1: Failure Modes from Research

From "Why Do Multi-Agent LLM Systems Fail?" research analyzing 1,642 traces:

### Category 1: Communication Failures

**1. Conversation Resets (2.20%)**
- **Description:** Agent loses context mid-conversation
- **Impact:** Work must restart from beginning
- **Detection:** Track message sequence, detect context loss

**2. Withholding Information (0.85%)**
- **Description:** Agent doesn't share crucial information with others
- **Impact:** Other agents make decisions without full context
- **Detection:** Compare agent knowledge state vs what was shared

**3. Ignoring Input (1.90%)**
- **Description:** Agent receives message but doesn't act on it
- **Impact:** Coordination breaks, dependencies ignored
- **Detection:** Track acknowledgments, verify actions taken

### Category 2: Reasoning/Action Mismatches

**4. Reasoning/Action Mismatch (13.2%)**
- **Description:** Agent's stated reasoning doesn't match its actions
- **Impact:** Unpredictable behavior, breaks expectations
- **Detection:** Parse reasoning vs observe actions (hard)

**5. Wrong Assumptions (6.80%)**
- **Description:** Agent proceeds with incorrect assumptions instead of clarifying
- **Impact:** Work based on wrong foundation
- **Detection:** Track assumption statements, verify against ground truth

**6. Task Derailment (7.40%)**
- **Description:** Agent drifts from assigned task
- **Impact:** Task incomplete, wasted work
- **Detection:** Compare task description vs actions taken

### Category 3: Coordination Issues (From Synthesis)

**7. Deadlock**
- **Description:** Agents waiting for each other indefinitely
- **Impact:** System halts
- **Detection:** Track waiting states, detect cycles

**8. Livelock**
- **Description:** Agents repeatedly retry without progress
- **Impact:** Wasted resources, no completion
- **Detection:** Track action patterns, detect loops

**9. Race Conditions**
- **Description:** Multiple agents access shared resource simultaneously
- **Impact:** Data corruption, inconsistent state
- **Detection:** Track resource access timing, detect overlaps

**10. Resource Conflicts**
- **Description:** Multiple agents need exclusive access
- **Impact:** Blocked execution, priority inversions
- **Detection:** Track resource claims, detect conflicts

### Category 4: Error Propagation

**11. Cascade Failures**
- **Description:** One agent's error triggers errors in others
- **Impact:** System-wide failure from single fault
- **Detection:** Track error sequence, measure propagation depth

**12. Incomplete Recovery**
- **Description:** Agent partially recovers but leaves inconsistent state
- **Impact:** Subtle bugs, downstream failures
- **Detection:** Verify state consistency after recovery

### Category 5: State Management

**13. Memory/Context Loss**
- **Description:** Agent forgets previous context
- **Impact:** Repeated work, inconsistent decisions
- **Detection:** Track context size, detect drops

**14. State Divergence**
- **Description:** Agents have different views of system state
- **Impact:** Coordination breakdowns, conflicts
- **Detection:** Compare agent state snapshots

---

## Part 2: Detection Strategies

### Automatically Detectable (Rule-Based)

**1. Conversation Resets**
```python
def detect_conversation_reset(messages):
    """Detect if agent resets mid-conversation"""
    for i in range(1, len(messages)):
        curr = messages[i]
        prev = messages[i-1]

        # Check if agent references previous message
        if curr["sender"] == prev["recipient"]:
            # Should acknowledge previous message
            if "in_reply_to" not in curr or curr["in_reply_to"] != prev["message_id"]:
                return True, f"Agent {curr['sender']} didn't acknowledge {prev['message_id']}"

    return False, None
```

**2. Ignoring Input**
```python
def detect_ignored_input(messages, actions):
    """Detect if agent ignores received messages"""
    for msg in messages:
        if msg["message_type"] == "task.assignment":
            # Check if agent acknowledged
            acks = [m for m in messages
                    if m["message_type"] == "ack.received"
                    and m["acknowledging_message_id"] == msg["message_id"]]
            if not acks:
                return True, f"Task {msg['task_id']} never acknowledged"

    return False, None
```

**3. Deadlock**
```python
def detect_deadlock(agents):
    """Detect circular waiting dependencies"""
    waiting_for = {}  # agent_id -> what it's waiting for

    for agent in agents:
        if agent["status"] == "blocked":
            waiting_for[agent["id"]] = agent["blocked_by"]

    # Check for cycles
    def has_cycle(agent_id, visited):
        if agent_id in visited:
            return True
        if agent_id not in waiting_for:
            return False

        visited.add(agent_id)
        return has_cycle(waiting_for[agent_id], visited)

    for agent_id in waiting_for:
        if has_cycle(agent_id, set()):
            return True, f"Deadlock detected involving {agent_id}"

    return False, None
```

**4. Livelock**
```python
def detect_livelock(agent_history, window=5):
    """Detect repeated actions without progress"""
    if len(agent_history) < window:
        return False, None

    recent = agent_history[-window:]
    actions = [h["action"] for h in recent]

    # Check for repeated pattern
    if len(set(actions)) == 1:  # Same action repeated
        # Check if state changed
        states = [h["state_hash"] for h in recent]
        if len(set(states)) == 1:  # State unchanged
            return True, f"Agent repeating {actions[0]} without progress"

    return False, None
```

**5. Race Conditions**
```python
def detect_race_condition(resource_accesses):
    """Detect simultaneous resource access"""
    for r in resources:
        accesses = [a for a in resource_accesses if a["resource_id"] == r]
        accesses.sort(key=lambda x: x["timestamp"])

        for i in range(1, len(accesses)):
            curr = accesses[i]
            prev = accesses[i-1]

            # Check for overlapping access
            if curr["start_time"] < prev["end_time"]:
                return True, f"Race condition on {r} between {prev['agent']} and {curr['agent']}"

    return False, None
```

**6. Resource Conflicts**
```python
def detect_resource_conflict(resource_claims):
    """Detect multiple agents claiming same resource"""
    by_resource = {}
    for claim in resource_claims:
        resource_id = claim["resource_id"]
        if resource_id not in by_resource:
            by_resource[resource_id] = []
        by_resource[resource_id].append(claim)

    conflicts = []
    for resource_id, claims in by_resource.items():
        if len(claims) > 1:
            # Multiple simultaneous claims
            agents = [c["agent_id"] for c in claims]
            conflicts.append((resource_id, agents))

    if conflicts:
        return True, f"Resource conflicts detected: {conflicts}"
    return False, None
```

**7. Cascade Failures**
```python
def detect_cascade_failure(errors, threshold=3):
    """Detect error propagation"""
    if len(errors) < threshold:
        return False, None

    # Sort by timestamp
    errors.sort(key=lambda x: x["timestamp"])

    # Check if errors follow quickly after one another
    for i in range(1, len(errors)):
        time_delta = errors[i]["timestamp"] - errors[i-1]["timestamp"]
        if time_delta < 1000:  # Within 1 second
            # Check if error in agent B caused by error in agent A
            if errors[i]["agent_id"] != errors[i-1]["agent_id"]:
                propagation_depth = count_propagation(errors, i)
                if propagation_depth >= threshold:
                    return True, f"Cascade failure: {propagation_depth} agents affected"

    return False, None
```

**8. Deadlock (Enhanced with Timeout)**
```python
def detect_timeout_deadlock(agents, timeout_ms=30000):
    """Detect agents blocked longer than timeout"""
    import time
    current_time = time.time() * 1000

    for agent in agents:
        if agent["status"] == "blocked":
            blocked_duration = current_time - agent["blocked_since"]
            if blocked_duration > timeout_ms:
                return True, f"Agent {agent['id']} blocked for {blocked_duration}ms"

    return False, None
```

**9. State Divergence**
```python
def detect_state_divergence(agent_states):
    """Detect inconsistent views of system state"""
    state_hashes = {}
    for agent_id, state in agent_states.items():
        state_hash = hash_state(state)
        if state_hash not in state_hashes:
            state_hashes[state_hash] = []
        state_hashes[state_hash].append(agent_id)

    if len(state_hashes) > 1:
        # Multiple different states
        return True, f"State divergence: {len(state_hashes)} different views"

    return False, None
```

### Requires Semantic Analysis (Harder)

**10. Reasoning/Action Mismatch**
- Requires parsing natural language reasoning
- Comparing to observed actions
- LLM-based analysis needed

**11. Wrong Assumptions**
- Requires understanding what agent "thinks" vs ground truth
- Semantic comparison
- Hard to automate

**12. Task Derailment**
- Requires comparing task description to actions
- Semantic similarity needed
- Can use embedding distance as proxy

**13. Withholding Information**
- Requires knowing what agent "should" share
- Hard to define objectively
- Heuristics: compare agent knowledge to messages sent

**14. Incomplete Recovery**
- Requires understanding "correct" state post-recovery
- Domain-specific invariants
- Partial automation via state validators

---

## Part 3: FailureDetector Implementation

```python
from dataclasses import dataclass
from typing import List, Optional, Tuple
from enum import Enum

class FailureMode(Enum):
    CONVERSATION_RESET = "conversation_reset"
    IGNORING_INPUT = "ignoring_input"
    DEADLOCK = "deadlock"
    LIVELOCK = "livelock"
    RACE_CONDITION = "race_condition"
    RESOURCE_CONFLICT = "resource_conflict"
    CASCADE_FAILURE = "cascade_failure"
    STATE_DIVERGENCE = "state_divergence"
    # Semantic (manual review)
    REASONING_ACTION_MISMATCH = "reasoning_action_mismatch"
    WRONG_ASSUMPTIONS = "wrong_assumptions"
    TASK_DERAILMENT = "task_derailment"
    WITHHOLDING_INFO = "withholding_info"
    INCOMPLETE_RECOVERY = "incomplete_recovery"

@dataclass
class FailureDetection:
    mode: FailureMode
    detected: bool
    message: Optional[str]
    timestamp: str
    context: dict

class FailureDetector:
    """Detect failure modes in agent execution"""

    def __init__(self):
        self.detections: List[FailureDetection] = []

    def check_all(self, system_state: dict) -> List[FailureDetection]:
        """Run all automated detectors"""
        detectors = [
            self.detect_conversation_reset,
            self.detect_ignoring_input,
            self.detect_deadlock,
            self.detect_livelock,
            self.detect_race_condition,
            self.detect_resource_conflict,
            self.detect_cascade_failure,
            self.detect_state_divergence,
        ]

        for detector in detectors:
            detection = detector(system_state)
            if detection.detected:
                self.detections.append(detection)

        return [d for d in self.detections if d.detected]

    def detect_conversation_reset(self, state: dict) -> FailureDetection:
        # Implementation from above
        pass

    # ... other detectors

    def generate_report(self) -> str:
        """Generate failure detection report"""
        report = ["# Failure Detection Report\\n"]

        if not self.detections:
            report.append("No failures detected.")
            return "\\n".join(report)

        # Group by mode
        by_mode = {}
        for d in self.detections:
            if d.mode not in by_mode:
                by_mode[d.mode] = []
            by_mode[d.mode].append(d)

        for mode, detections in by_mode.items():
            report.append(f"## {mode.value.replace('_', ' ').title()}")
            report.append(f"Count: {len(detections)}\\n")
            for d in detections:
                report.append(f"- {d.message}")
                report.append(f"  Time: {d.timestamp}")
                report.append("")

        return "\\n".join(report)
```

---

## Part 4: Integration with Metrics

```python
# In MetricsCollector, add failure detection
from failure_detector import FailureDetector, FailureMode

class MetricsCollector:
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.failure_detector = FailureDetector()

    def check_failures(self, system_state: dict):
        """Check for failures and log"""
        failures = self.failure_detector.check_all(system_state)
        for failure in failures:
            self._log_event("failure_detected", {
                "mode": failure.mode.value,
                "message": failure.message,
                **failure.context
            })

    # Call check_failures() periodically during experiment
```

---

## Part 5: Key Recommendations

**Implement in phases:**

**Phase 1 (Week 1): Core detectors**
- Deadlock, livelock, race conditions
- Resource conflicts
- Cascade failures
- **Goal:** Detect coordination breakdowns

**Phase 2 (Week 2): Communication detectors**
- Conversation resets
- Ignoring input
- State divergence
- **Goal:** Detect message-passing issues

**Phase 3 (Future): Semantic detectors**
- Reasoning/action mismatch (LLM-based)
- Task derailment (embedding distance)
- Wrong assumptions (heuristics)
- **Goal:** Detect subtle cognitive failures

---

## Conclusion

**9 failure modes detectable automatically with rule-based approaches.**

**Implementation:**
- FailureDetector class (~400 lines)
- Rule-based detection functions
- Integration with MetricsCollector
- Periodic checking during experiments

**Effort:** ~6 hours to implement core detectors

**Status: READY TO IMPLEMENT**
