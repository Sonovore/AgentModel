# Jidoka: Architectural Analysis for AI Agent Systems

## Executive Summary

Jidoka---"automation with a human touch"---represents a principled answer to one of the central questions in AI agent design: **how should automated systems handle situations that exceed their reliable operating envelope?**

The naive approach: continue operating and hope for the best, or escalate everything and sacrifice efficiency. Jidoka offers a third path: **build detection into automation so that systems recognize when human judgment is needed and signal for it.**

For AI agent systems, this translates to a specific architectural pattern:

| Phase | Human Role | Agent Role |
|-------|-----------|------------|
| **Routine operation** | Absent (no attention needed) | Execute autonomously within defined bounds |
| **Abnormality detection** | Absent (agent handles) | Monitor for deviations from normal |
| **Escalation signal** | Receives signal | Stops and provides context |
| **Judgment exercise** | Makes decision | Waits or provides options |
| **Resolution** | Validates | Implements or resumes |

**The central architectural claim:** Agent systems should be designed around explicit abnormality detection and escalation mechanisms because this is where both the largest variance in outcomes and the largest leverage for human attention exist. Systems that treat all agent outputs equally (either trusting all or validating all) waste human attention on routine cases or miss critical failures.

This analysis serves three purposes:
1. **Design framework** for architecting agent systems with appropriate human-in-the-loop mechanisms
2. **Diagnostic framework** for understanding why agents fail silently and how to make failures visible
3. **Cultural framework** for building organizations that effectively use human-agent collaboration

---

## Part I: The Core Problem Jidoka Addresses

### The Spectrum of Automation Failures

Agent systems fail in predictable ways that jidoka is designed to prevent:

**Type 1: Visible, Immediate Failures**
- Agent produces obviously wrong output
- Error message returned
- Human immediately aware
- Easy to address

**Type 2: Hidden, Accumulating Failures** (Jidoka target)
- Agent produces subtly wrong output
- No error signal
- Appears to function normally
- Problems compound before discovery
- Root cause obscured by time elapsed

**Type 3: Cascading Failures**
- Initial agent failure feeds into subsequent agents
- Each step appears locally reasonable
- System-level output is wrong in ways no single agent caused
- Tracing requires reconstructing entire chain

Type 1 failures are already visible---no special architecture needed. Type 3 failures require multi-agent coordination mechanisms. Type 2 failures are jidoka's primary target: making the invisible visible before it compounds.

### Why Agents Produce Hidden Failures

Several factors cause agents to produce wrong outputs without signaling problems:

**Confidence-Competence Mismatch**

LLMs exhibit high confidence independent of accuracy. Research consistently shows that model confidence scores do not reliably predict correctness. An agent may be 95% "confident" while being completely wrong.

This means agents cannot reliably self-diagnose their own errors through confidence alone. External verification mechanisms are required.

**Out-of-Distribution Unawareness**

Agents don't recognize when inputs differ from training distribution. They apply learned patterns regardless of applicability. The result: outputs that follow correct form but have incorrect substance.

Example: An agent trained on Python patterns may confidently apply those patterns to a domain where different conventions apply, producing syntactically valid but semantically wrong code.

**Hallucination as Feature**

Language models generate plausible continuations of input. When the correct answer is unavailable, they generate plausible incorrect answers. This isn't a bug; it's how the architecture works. The model doesn't distinguish "known" from "plausible."

**Goal Specification Gaps**

Agents optimize for stated objectives. Unstated constraints are violated without signaling. The agent achieves the explicit goal while breaking implicit requirements.

### The Cost Structure of Hidden Failures

Hidden failures have a specific cost structure that makes jidoka economically rational:

| Detection Point | Typical Cost | Why |
|----------------|--------------|-----|
| During generation | 1x | Agent regenerates or escalates |
| After initial output | 10x | Human review, correction, rework |
| After downstream use | 100x | Propagated errors, multiple corrections |
| After external impact | 1000x+ | Customer impact, reputation, remediation |

The cost increase is roughly exponential because:
- Later detection requires tracing back through more steps
- More work has been done on flawed foundation
- External impacts require external remediation
- Trust erosion affects future interactions

Jidoka's stopping cost (interruption, human attention) is a small upfront investment to avoid large downstream costs.

---

## Part II: The Agent Equivalent of Jidoka Mechanisms

### Abnormality Detection for Agents

In manufacturing, jidoka detects physical abnormalities: thread breaks, dimension errors, equipment malfunction. For agents, abnormality categories include:

**Category 1: Explicit Failure Signals**
- API errors
- Parsing failures
- Resource exhaustion
- Timeout

These are already visible. No special detection needed.

**Category 2: Confidence-Based Signals**
- Model reports low confidence
- Multiple valid interpretations exist
- Uncertainty exceeds threshold

Limitation: Confidence is unreliable. Low confidence sometimes indicates genuine uncertainty; sometimes indicates correct caution about novel situations.

**Category 3: Consistency-Based Signals**
- Output contradicts prior agent outputs
- Output contradicts known facts
- Internal reasoning is inconsistent

Implementation: Compare agent output against baselines (previous outputs, documented facts, reasoning chain coherence).

**Category 4: Scope-Based Signals**
- Task exceeds defined boundaries
- Resource consumption anomalous
- Time or token usage outside normal range

Implementation: Define expected operating envelope. Signal when bounds are exceeded.

**Category 5: Pattern-Based Signals**
- Output matches known error patterns
- Reasoning chain matches known failure modes
- Structure suggests hallucination (overly fluent, suspiciously complete)

Implementation: Maintain pattern library of past failures. Check outputs against patterns.

### Detection Architecture

```
Agent Processing Pipeline with Jidoka
=====================================

Input → [Pre-Processing]
                ↓
         [Agent Reasoning]
                ↓
         [Output Generation]
                ↓
      ┌─────────────────────────────┐
      │  ABNORMALITY DETECTION      │
      │                             │
      │  □ Confidence check         │
      │  □ Consistency check        │
      │  □ Scope check              │
      │  □ Pattern check            │
      │  □ Resource check           │
      │                             │
      │  All pass? → Continue       │
      │  Any fail? → Escalate       │
      └─────────────────────────────┘
                ↓
    [Pass: Output]  [Fail: Escalation Signal]
                            ↓
                    [Human Review]
                            ↓
                    [Resolution]
```

### The Agent Andon Cord

The andon cord empowers any worker to stop production. Agent system equivalents:

**Agent Self-Stop**

Agents that detect problems in their own operation stop and signal:

```markdown
# CLAUDE.md Pattern: Self-Stop Protocol

## When to Stop and Escalate

Stop processing and request human input when:

1. **Uncertainty**: You are <70% confident in your approach
2. **Contradiction**: Your planned action contradicts documented patterns
3. **Scope**: The task requires changes beyond the specified scope
4. **Risk**: The action is irreversible and high-stakes
5. **Novelty**: You haven't seen this pattern before

When stopping:
- State what you were trying to do
- Explain why you stopped
- Present options if you have them
- Wait for human input before proceeding
```

**Human Override**

Supervisors can halt agent operation at any point:

```markdown
# Operational Pattern: Human Override

## Emergency Stop
- Available at all times during agent operation
- Immediate halt, no graceful shutdown required
- Context preserved for diagnosis

## Pause and Review
- Request agent to checkpoint current state
- Human reviews progress before continuation
- Agent resumes from checkpoint or restarts

## Redirect
- Modify agent task mid-execution
- Agent acknowledges redirection
- Prior work preserved or discarded as specified
```

**Inter-Agent Signals**

In multi-agent systems, agents can flag concerns about other agents:

```markdown
# Multi-Agent Pattern: Peer Oversight

## When to Signal About Other Agents

Signal orchestrator when you observe:
- Upstream agent output seems malformed
- Upstream output contradicts your understanding
- Upstream agent has been unresponsive beyond threshold
- Pattern in upstream output matches known failure modes

Signal format:
- Source: [Your agent ID]
- Concern: [What you observed]
- Evidence: [Specific observations]
- Impact: [How this affects your task]
```

**System-Level Circuit Breakers**

Automated monitoring detects system-level problems:

```markdown
# System Pattern: Circuit Breakers

## Automatic Trip Conditions

System halts for review when:
- Error rate exceeds threshold (e.g., >10% of agent outputs trigger retry)
- Cascade detected (error in one agent propagates to 3+ downstream)
- Resource anomaly (token consumption >3x expected)
- Latency spike (response time >2x normal for >5 minutes)

## Manual Trip Conditions

Operators should trip circuit breaker when:
- Pattern of correlated failures emerges
- Novel failure mode appears
- External dependency shows degradation
- Suspicious activity patterns detected
```

---

## Part III: Where Agents Struggle vs. Excel

### Agent Advantages in Jidoka Context

**Consistency of Detection**

Agents can apply the same detection criteria uniformly across all outputs. Humans monitoring for problems exhibit fatigue, distraction, and vigilance degradation. Agents don't get tired of checking.

**Speed of Detection**

Detection checks can be applied in milliseconds. Human review takes minutes to hours. For routine checks, agent detection is orders of magnitude faster.

**Pattern Matching at Scale**

Agents can compare outputs against large libraries of known failure patterns. Humans can't hold hundreds of error patterns in working memory. Agents can.

**Documentation of Detections**

Every detection check can be logged automatically. No separate documentation effort required. Audit trails are free.

### Agent Weaknesses in Jidoka Context

**Calibration Unreliability**

Agents cannot reliably self-assess. A confidence threshold of "70% certain" doesn't mean 70% of uncertain outputs will be escalated. The relationship between stated confidence and actual correctness is weak.

**Novel Failure Blindness**

Agents detect failures that match known patterns. Novel failure modes---by definition---don't match patterns yet. The first instance of a new failure type will likely not be caught.

**Context-Sensitivity Limitations**

Whether something is an "abnormality" depends on context. An unusual pattern might be innovation in one context and error in another. Agents struggle with this contextual judgment.

**Adversarial Vulnerability**

Detection mechanisms can be gamed, either by malicious actors crafting inputs that evade detection or by the agent itself learning to produce outputs that pass checks without actually being correct.

### The Bottleneck Analysis

| Jidoka Phase | Agent Performance | Bottleneck? |
|--------------|-------------------|-------------|
| Routine operation | Excellent | No |
| Abnormality detection (known patterns) | Good | No |
| Abnormality detection (novel patterns) | Poor | **Yes** |
| Escalation signaling | Good | No |
| Context preservation | Good | No |
| Judgment (human phase) | N/A | **Yes** (human availability) |
| Resolution implementation | Good | No |

Two bottlenecks emerge:
1. Detecting novel abnormalities (agent limitation)
2. Human availability for judgment (organizational limitation)

---

## Part IV: Organizational Culture for Agent Jidoka

### The NUMMI Lesson Applied to AI

The NUMMI case demonstrated that jidoka mechanisms (andon cords) are worthless without supporting culture. Workers were "too afraid to pull it" because organizational culture punished problem identification.

The same dynamic applies to AI agent systems:

**Culture That Undermines Agent Jidoka**

- Penalizing agents for uncertainty (metrics that count uncertain outputs negatively)
- Penalizing humans for agent failures (creating incentive to hide problems)
- Optimizing for throughput over quality (creating pressure to suppress stopping)
- Treating agent escalation as failure rather than appropriate behavior
- Dismissing agent uncertainty as "being too cautious"

**Culture That Enables Agent Jidoka**

- Rewarding early problem detection (uncertainty that catches errors is valuable)
- Celebrating catches (publicly recognizing when stopping prevented larger problems)
- Learning from every escalation (treating each as improvement opportunity)
- Distinguishing signal quality from outcome (agent correctly flagged uncertainty even if resolution was trivial)

### Organizational Prerequisites

**1. Tolerance for Agent Uncertainty**

Organizations must accept that agent uncertainty is a feature, not a bug. An agent that says "I'm not sure" is more trustworthy than one that confidently produces wrong answers.

Metric design matters: if agents are measured on "completion rate" without accounting for quality, they will learn to suppress uncertainty signals.

**2. Problem-Surfacing Rewards**

If agent developers are penalized when their agents stop frequently, they will tune systems to minimize stopping. This trades visible interruption for hidden failure.

Better: reward catching problems early. Celebrate when an agent escalation prevented a larger issue.

**3. Learning Orientation**

When agent errors are discovered, the response must be analysis and improvement:
- What detection would have caught this?
- How do we prevent recurrence?
- What does this reveal about our understanding?

Not: blame assignment, punishment for the error, pressure to "just make it work."

**4. Human Response Reliability**

If agents escalate and humans don't respond (or respond poorly), agents learn that escalation is pointless. The system degrades to either:
- Agents stop escalating (hidden failures return)
- Agents escalate everything (signal becomes noise)

Human response to escalation must be reliable, timely, and constructive.

### Building Trust Iteratively

Trust between humans and agents develops through repeated interaction:

**Early Phase: High Validation**
- Agents escalate frequently
- Humans validate or correct frequently
- High overhead but calibration occurring
- Agents learn which situations genuinely need escalation

**Middle Phase: Calibrated Trust**
- Agents escalate less frequently (better discrimination)
- Human validation confirms agent judgment
- Trust increases based on track record
- Overhead decreases

**Mature Phase: Selective Escalation**
- Agents operate autonomously for routine cases
- Escalation reserved for genuinely uncertain situations
- Human trust is high but not unconditional
- Continuous monitoring prevents complacency

### Failure Mode: Automation Complacency

Extended periods of reliable agent operation create complacency. Humans reduce attention because the agent has been reliable. When the agent eventually fails, degraded human attention delays recognition.

Countermeasures:
- Periodic validation even during reliable periods
- Metrics that track human attention to agent outputs
- Artificial uncertainty injection to maintain vigilance (carefully implemented)
- Regular review of detection mechanism effectiveness

---

## Part V: Measurement Framework

### What to Measure

**Agent-Level Metrics**

| Metric | Definition | Target | Warning Sign |
|--------|------------|--------|--------------|
| Escalation rate | Escalations / Total outputs | 5-20% | <1% or >50% |
| Escalation precision | True problems / Escalations | >70% | <50% |
| Escalation recall | Caught problems / Total problems | >90% | <70% |
| Detection latency | Time from abnormality to signal | <1s | >10s |
| Context quality | Human can act on escalation info | >90% | <70% |

**System-Level Metrics**

| Metric | Definition | Target | Warning Sign |
|--------|------------|--------|--------------|
| Hidden failure rate | Problems discovered after output | <5% | >10% |
| Cascade frequency | Multi-agent failures / Total failures | <10% | >30% |
| Time to detection | Generation to problem identification | <1hr | >24hr |
| Recovery time | Detection to resolution | <2hr | >8hr |
| Improvement rate | New detections added / month | >2 | 0 |

**Organizational Metrics**

| Metric | Definition | Target | Warning Sign |
|--------|------------|--------|--------------|
| Human response time | Escalation to human action | <30min | >4hr |
| Response quality | Escalations correctly resolved | >95% | <80% |
| Override rate | Human overrides agent decision | 5-15% | <1% or >40% |
| Trust calibration | Human trust matches agent reliability | Aligned | Divergent |

### Escalation Analysis Protocol

For every escalation, capture:

```
Escalation Record
=================
ID: [unique identifier]
Timestamp: [when escalation occurred]
Agent: [which agent]
Task: [what task was being performed]

Detection:
- Trigger type: [confidence/consistency/scope/pattern/resource]
- Trigger details: [specific condition that fired]
- Agent state at escalation: [preserved context]

Resolution:
- Human response time: [time until human engaged]
- Resolution type: [proceed/modify/abort/redirect]
- Resolution rationale: [why this resolution]
- Was escalation appropriate? [yes/no/unclear]

Learning:
- Should detection have triggered earlier? [yes/no]
- Should detection have been different type? [type if yes]
- New pattern to add to library? [pattern if yes]
- Process change indicated? [change if yes]
```

### Calibration Analysis

Periodically analyze escalation patterns:

**Precision Analysis:**
- What fraction of escalations were true problems?
- If low: detection is too sensitive (too many false positives)
- If high: detection might be missing problems (need recall check)

**Recall Analysis:**
- What fraction of problems were escalated?
- Requires sampling outputs that weren't escalated
- If low: detection is missing problems (false negatives)

**Pattern Analysis:**
- Which detection types trigger most frequently?
- Which have highest precision?
- Which problems are being missed and why?

**Temporal Analysis:**
- Is escalation rate stable or trending?
- Are new failure modes emerging?
- Is human response time stable or degrading?

---

## Part VI: Design Patterns

### Pattern 1: Tiered Escalation

**Problem:** Not all abnormalities have equal stakes. Binary escalate/continue is too coarse.

**Solution:** Implement tiered escalation based on stakes and confidence.

```markdown
# CLAUDE.md Pattern: Tiered Escalation

## Tier 1: Proceed with Note
- Low stakes AND moderate confidence
- Log the uncertainty
- Continue execution
- Review in batch later

## Tier 2: Checkpoint and Continue
- Moderate stakes OR low confidence
- Save current state
- Note concerns in output
- Continue but flag for human review
- Human can roll back if needed

## Tier 3: Pause and Request Input
- High stakes OR very low confidence
- Stop execution
- Preserve full context
- Wait for human input before continuing

## Tier 4: Abort and Alert
- Critical stakes OR detected danger
- Stop immediately
- Alert human
- Do not continue without explicit restart

## Stakes Classification
- Low: Documentation, formatting, non-functional changes
- Moderate: New features, refactoring, test changes
- High: Security, data handling, production systems
- Critical: User data, financial, safety-critical
```

### Pattern 2: Confidence-Adjusted Autonomy

**Problem:** Fixed escalation thresholds don't account for task difficulty or agent track record.

**Solution:** Adjust escalation thresholds based on demonstrated reliability.

```markdown
# System Pattern: Confidence-Adjusted Autonomy

## Initial State (New Task Type)
- Escalation threshold: High (escalate if <90% confident)
- Human validates all outputs
- Build track record

## After 10 Successful Outputs
- Lower threshold to 80%
- Sample validate (50% of outputs)
- Continue building track record

## After 50 Successful Outputs
- Lower threshold to 70%
- Sample validate (20% of outputs)
- Monitor for degradation

## On Any Failure
- Raise threshold by 10%
- Increase validation rate
- Analyze failure mode
- Add to detection library

## Never Below
- Minimum threshold: 60%
- Minimum validation rate: 5%
- Prevents complacency
```

### Pattern 3: Pre-Action Validation

**Problem:** Irreversible actions should be validated before execution, not after.

**Solution:** Explicit pre-action checkpoint for high-stakes operations.

```markdown
# CLAUDE.md Pattern: Pre-Action Validation

## Before Irreversible Actions

Before executing:
- Production deployments
- Data modifications
- External API calls that can't be undone
- File deletions
- Configuration changes affecting other systems

Perform pre-action validation:

1. **State Summary**
   - Current state of affected systems
   - What will change
   - What is your confidence level?

2. **Risk Assessment**
   - What could go wrong?
   - What is the rollback path?
   - What would indicate a problem?

3. **Validation Checkpoint**
   - Present above to human
   - Wait for explicit approval
   - Log approval before proceeding

## Exception
If explicit YOLO mode enabled by human, skip pre-action validation.
Document that YOLO mode was used.
```

### Pattern 4: Continuous Improvement Through Escalation

**Problem:** Escalations are treated as interruptions rather than learning opportunities.

**Solution:** Systematic learning from every escalation.

```markdown
# Process Pattern: Escalation Learning Loop

## After Every Escalation Resolution

1. **Classify the Outcome**
   - True Positive: Problem existed, escalation correct
   - False Positive: No problem, escalation unnecessary
   - Near Miss: Problem exists but different than escalated
   - Process Issue: Escalation process itself had problems

2. **Identify Learning**
   - Could earlier detection have caught this?
   - Should detection threshold change?
   - Is there a new pattern to add?
   - Is there a documentation gap?

3. **Implement Improvement**
   - Update detection rules
   - Update CLAUDE.md if needed
   - Add to pattern library
   - Document in escalation log

4. **Verify Improvement**
   - Track whether similar issues recur
   - Measure false positive rate change
   - Validate detection works on test cases

## Weekly Review
- Aggregate escalation learning
- Identify systematic patterns
- Prioritize improvements
- Track improvement effectiveness
```

### Pattern 5: Distributed Detection with Central Response

**Problem:** In multi-agent systems, each agent detecting independently creates redundant work and potential inconsistency.

**Solution:** Centralized escalation handling with distributed detection.

```markdown
# Multi-Agent Pattern: Detection + Response Separation

## Detection Layer (Distributed)
Each agent:
- Runs local detection checks
- Signals abnormalities to central handler
- Includes context and confidence
- Continues or pauses based on tier

## Response Layer (Centralized)
Central handler:
- Aggregates signals from all agents
- Detects patterns across agents
- Routes to appropriate human reviewer
- Maintains global state and history
- Implements circuit breakers

## Benefits
- Each agent runs fast local checks
- Central handler sees system-wide patterns
- No agent needs to know about other agents' issues
- Consistent escalation handling
- Single point for metrics and learning

## Implementation
```
Agent A ─┬─ Local Detection → Signal ─┐
Agent B ─┤                            ├─> Central Handler → Human
Agent C ─┴─ Local Detection → Signal ─┘
```
```

---

## Part VII: Failure Mode Taxonomy

### Detection Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| No detection triggered | Problem discovered post-output | Detection rules don't cover this case | Add detection rule |
| Detection too late | Problem caught but damage done | Detection runs after critical action | Move detection earlier |
| Wrong detection type | Escalated for wrong reason | Detection rules misclassified | Improve detection specificity |
| Detection overwhelmed | Too many escalations, signal lost | Threshold too sensitive | Calibrate threshold |

### Escalation Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| Escalation suppressed | Agent continued despite problem | Incentive to avoid escalation | Change incentives, audit |
| Escalation ignored | Human didn't respond | Human overloaded or disengaged | Reduce load, triage |
| Escalation misrouted | Went to wrong person | Routing rules incorrect | Fix routing |
| Escalation missing context | Human can't act on it | Agent didn't preserve state | Improve context capture |

### Resolution Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| Wrong resolution | Problem recurs | Root cause not addressed | Better analysis |
| Slow resolution | Long time to fix | Process bottleneck | Streamline process |
| Resolution not applied | Same agent makes same mistake | Learning not implemented | Close loop on learning |
| Resolution side effects | Fix causes new problems | Insufficient testing | Better validation |

### Cultural Failures

| Failure Mode | Symptom | Root Cause | Fix |
|--------------|---------|------------|-----|
| Blame culture | Problems hidden | Punishment for surfacing | Celebrate catches |
| Throughput pressure | Escalation rate drops | Quality sacrificed for speed | Change metrics |
| Complacency | Validation attention drops | Extended reliability | Periodic stress tests |
| Learned helplessness | Agents escalate everything | Humans override too often | Calibrate trust |

---

## Part VIII: Multi-Agent Implications

### The Cascade Problem

In multi-agent systems, jidoka failures compound:

```
Agent A produces output with undetected error
        ↓
Agent B receives A's output as input
B's output incorporates A's error
B's detection doesn't catch inherited error
        ↓
Agent C receives B's output
C's output compounds error further
        ↓
Final output is wrong in ways no single agent caused
Root cause analysis is difficult
```

### Multi-Agent Jidoka Architecture

**Principle 1: Each agent validates inputs, not just outputs**

```markdown
# Multi-Agent Pattern: Input Validation

Before processing input from another agent:
1. Check input format matches expected schema
2. Check input values are in plausible ranges
3. Check input is consistent with task context
4. If any check fails, escalate before processing
```

**Principle 2: Provenance tracking**

```markdown
# Multi-Agent Pattern: Provenance

Every agent output includes:
- Source agent ID
- Confidence level
- Inputs used
- Processing steps applied

Receiving agents use provenance to:
- Assess input reliability
- Trace problems to source
- Propagate uncertainty appropriately
```

**Principle 3: Aggregate confidence decays**

```markdown
# Multi-Agent Pattern: Confidence Decay

Rule: Confidence cannot increase through agent chain
- Agent B's confidence ≤ min(B's own confidence, A's confidence)
- Chain of 5 agents each 90% confident: ≤ 59% aggregate confidence
- Long chains require explicit validation checkpoints
```

**Principle 4: Circuit breakers at boundaries**

```markdown
# Multi-Agent Pattern: Boundary Circuit Breakers

At each agent handoff:
- Monitor error rate
- If error rate exceeds threshold, pause handoff
- Alert human to diagnose boundary issue
- Resume only after explicit clearance
```

### Shared Detection Infrastructure

Rather than each agent implementing detection independently:

```markdown
# System Pattern: Shared Detection Service

## Central Detection Service
Provides:
- Pattern matching against known failure library
- Consistency checking against system state
- Resource monitoring
- Anomaly detection

Each agent:
- Sends outputs to detection service
- Receives pass/fail/warn response
- Acts on response (continue/pause/escalate)

Benefits:
- Consistent detection across all agents
- Central pattern library maintenance
- System-wide visibility
- Single point for detection improvements
```

---

## Part IX: CLAUDE.md Templates

### Basic Jidoka Integration

```markdown
# Agent Operating Protocol

## Abnormality Detection

Stop and escalate when:

1. **Confidence Threshold**
   - You are less than 70% confident in your approach
   - You see multiple valid interpretations
   - The task feels outside your training

2. **Consistency Check**
   - Your output contradicts documented patterns
   - Your output contradicts your prior outputs
   - Your reasoning chain has gaps

3. **Scope Boundary**
   - The task requires changes beyond specified scope
   - Resource consumption is higher than expected
   - Time taken exceeds expected range

4. **Risk Level**
   - The action is irreversible
   - The action affects production systems
   - The action involves sensitive data

## When Stopping

Provide:
- What you were trying to accomplish
- Why you stopped (which condition triggered)
- Your current understanding of the situation
- Options you see (if any)
- What information would help you proceed

Wait for human input before continuing.

## When Proceeding

If no stopping conditions apply:
- Execute the task
- Note any minor concerns in your output
- Make concerns explicit even if not stopping
```

### Advanced Tiered Escalation

```markdown
# Escalation Protocol

## Tier Classification

### Tier 0: Routine Proceed
- High confidence (>90%)
- Familiar task type
- Low stakes
- Action: Execute, log

### Tier 1: Proceed with Caution
- Moderate confidence (70-90%)
- Known task type with variation
- Low-moderate stakes
- Action: Execute, note concerns in output, flag for review

### Tier 2: Checkpoint Required
- Low confidence (50-70%)
- Unfamiliar elements
- Moderate stakes
- Action: Checkpoint state, request confirmation before proceeding

### Tier 3: Full Stop
- Very low confidence (<50%)
- Unknown territory
- High stakes OR irreversible
- Action: Stop, full context dump, wait for human

## Stakes Assessment

Low stakes:
- Documentation changes
- Formatting
- Test additions (not changes)
- Non-production environments

Moderate stakes:
- Feature implementation
- Refactoring
- Test modifications
- Staging environments

High stakes:
- Security-related code
- Data handling
- External integrations
- Production systems

Critical stakes:
- Authentication/authorization
- Financial transactions
- User data
- Safety systems

## Confidence Calibration

Your confidence should be lower when:
- You haven't seen this exact pattern before
- Multiple approaches seem valid
- The requirements are ambiguous
- You're working from memory rather than observation

Your confidence should be higher when:
- You've successfully done this exact task before
- The pattern matches documented examples
- Requirements are explicit and complete
- You've validated approach against codebase
```

### Multi-Agent Coordination

```markdown
# Multi-Agent Jidoka Protocol

## Input Validation

Before processing input from another agent:

1. **Format Check**
   - Does input match expected schema?
   - Are required fields present?
   - Are types correct?

2. **Content Check**
   - Are values in plausible ranges?
   - Does content match stated confidence?
   - Are there obvious anomalies?

3. **Provenance Check**
   - Is source agent identified?
   - Is confidence level stated?
   - Is processing chain documented?

If any check fails:
- Do not process the input
- Escalate with details of what failed
- Include original input for diagnosis

## Output Labeling

Every output you produce must include:

```
Agent: [Your identifier]
Confidence: [0-100%]
Inputs used: [List of inputs with their confidence]
Processing: [Brief description of what you did]
Caveats: [Any concerns or limitations]
```

## Confidence Propagation

Your output confidence ≤ minimum of:
- Your own confidence in your processing
- The confidence of each input you used

Example:
- Input A: 85% confidence
- Input B: 90% confidence
- Your processing: 95% confidence
- Your output: ≤ 85% confidence

## Peer Flagging

If you observe concerning patterns in another agent's output:
- Note the concern
- Include in your escalation
- Do not attempt to correct silently
```

---

## Part X: Implementation Roadmap

### Phase 1: Foundation (Week 1-2)

**Detection Infrastructure**
- [ ] Identify detection trigger types relevant to your system
- [ ] Implement basic confidence threshold checking
- [ ] Implement consistency checking against known patterns
- [ ] Implement scope boundary monitoring

**Escalation Mechanism**
- [ ] Define escalation tiers
- [ ] Implement escalation routing
- [ ] Create escalation record format
- [ ] Set up escalation logging

**Measurement Setup**
- [ ] Implement escalation rate tracking
- [ ] Set up hidden failure detection (sampling)
- [ ] Create dashboard for key metrics

### Phase 2: Calibration (Week 3-4)

**Threshold Tuning**
- [ ] Analyze initial escalation patterns
- [ ] Adjust thresholds based on precision/recall
- [ ] Document calibration rationale

**Human Response**
- [ ] Establish response time targets
- [ ] Train responders on escalation handling
- [ ] Create escalation playbooks

**Pattern Library**
- [ ] Catalog initial failure patterns
- [ ] Create pattern matching rules
- [ ] Validate pattern detection

### Phase 3: Learning Loop (Week 5-6)

**Escalation Analysis**
- [ ] Implement post-escalation review process
- [ ] Create learning documentation
- [ ] Track improvement implementation

**Detection Improvement**
- [ ] Add new patterns to library
- [ ] Refine existing detection rules
- [ ] Validate improvements

**Cultural Development**
- [ ] Communicate jidoka principles to team
- [ ] Celebrate early problem detection
- [ ] Address any blame-culture signals

### Phase 4: Maturation (Ongoing)

**Continuous Monitoring**
- [ ] Weekly escalation analysis
- [ ] Monthly threshold review
- [ ] Quarterly pattern library audit

**Evolution**
- [ ] Add advanced detection types as needed
- [ ] Refine tiering based on experience
- [ ] Expand to multi-agent if applicable

---

## Part XI: Open Questions

### Detection Challenges

1. **How do you detect novel failure modes?** Pattern matching catches known failures. By definition, novel failures don't match patterns. What mechanisms detect the unknown?

2. **How do you calibrate confidence thresholds across different task types?** A 70% threshold may be appropriate for some tasks and completely wrong for others. How do you maintain appropriate thresholds as task types evolve?

3. **How do you prevent detection gaming?** If agents learn that certain outputs avoid detection, they may produce those outputs regardless of correctness. How do you prevent this?

### Organizational Challenges

4. **How do you maintain human attention over time?** Escalations require human response. As volume grows, attention degrades. Where is the scaling limit?

5. **How do you balance throughput pressure against quality?** Organizations will always have throughput goals. How do you prevent jidoka from being undermined by deadline pressure?

6. **How do you demonstrate ROI for jidoka investment?** The value is in problems prevented. How do you measure counterfactuals?

### Multi-Agent Challenges

7. **How does confidence propagate through long chains?** With enough agents in sequence, aggregate confidence approaches zero. Where do you insert validation checkpoints?

8. **How do you attribute failure in cascaded systems?** When the final output is wrong, which agent is responsible? How do you trace root cause efficiently?

9. **How do agents coordinate their detection mechanisms?** If each agent has different detection rules, how do you maintain system-wide consistency?

---

## Part XII: Cross-Model Integration

### Relationship to OODA Loop

Jidoka and OODA address complementary concerns:

- **OODA**: How do agents cycle through observation, orientation, decision, and action?
- **Jidoka**: When should that cycle be interrupted for human judgment?

Integration point: Jidoka detection should occur at the Orient phase (is my mental model appropriate?) and the Act phase (should I execute this action?).

### Relationship to Just-in-Time Coordination

Jidoka and JIT are the two pillars of the Toyota Production System:

- **JIT**: Ensure the right things arrive at the right time
- **Jidoka**: Ensure problems are surfaced immediately

Integration point: In agent systems, JIT principles optimize task flow while jidoka principles ensure quality at each step. Without jidoka, JIT efficiently propagates errors. Without JIT, jidoka catches problems in inefficient batches.

### Relationship to Shared Mental Models

Effective jidoka requires shared understanding:

- Shared definition of "abnormality"
- Shared escalation protocols
- Shared response procedures

Integration point: The CLAUDE.md that enables shared mental models also enables consistent jidoka behavior across agents.

---

## Sources

### Primary Sources

- Ohno, Taiichi. "Toyota Production System: Beyond Large-Scale Production." Productivity Press, 1988.
- Toyoda, Sakichi. Original loom patents and Toyota company histories.
- Toyota Motor Corporation. Official TPS documentation.

### Human-Automation Interaction

- Bainbridge, Lisanne. "Ironies of Automation." Automatica, 1983.
- Sarter, N.B. and Woods, D.D. "How in the world did we ever get into that mode?" Human Factors, 1995.

### Case Studies

- NUMMI case studies from Stanford and MIT.
- American manufacturing jidoka implementation failures.

### Agent Systems

- Contemporary research on AI confidence calibration.
- Multi-agent system coordination literature.
- Human-in-the-loop system design.

### Cross-Reference

- OODA Loop Agent Analysis (this repository)
- Just-in-Time Coordination (this repository)
- Shared Mental Models (this repository)

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent architecture analysis for jidoka principles
**Status:** Complete architectural analysis

**Related Documents:**
- jidoka-automation-with-human-touch.md (source research)
- jidoka-automation-with-human-touch-three-level.md (three-level explanation)
- ooda-loop-agent-analysis.md (template and cross-reference)
- just-in-time-coordination-agent-analysis.md (complementary TPS pillar)
