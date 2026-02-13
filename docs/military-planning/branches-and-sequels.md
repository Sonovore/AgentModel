# Branches and Sequels: Military Contingency Planning for Agent Systems

## Executive Summary

Military doctrine has developed sophisticated frameworks for planning under uncertainty over centuries of operational experience. Two concepts stand at the center of this framework: **branches** (contingency plans for responding to situation changes during an operation) and **sequels** (plans for subsequent operations based on current outcomes). This research examines these doctrinal concepts in depth and explores their application to AI agent adaptive planning systems.

---

## 1. Doctrinal Definitions and Core Distinctions

### 1.1 Branches: Responding to Change

A **branch** is formally defined as "a contingency plan or course of action (an option built into the basic plan or course of action) for changing the mission, disposition, orientation, or direction of movement of the force to aid success of the operation based on anticipated events, opportunities, or disruptions caused by enemy actions and reactions."

Key characteristics of branches:
- **Reactive to current operation**: Branches respond to changes within the ongoing mission
- **Triggered by conditions**: Execution depends on specific events or intelligence
- **Maintains operational continuity**: The adjustment happens "mid-stride" rather than starting over
- **Pre-planned but conditional**: Developed during planning but executed only if triggered
- **"Be Prepared To" missions**: Branch plans typically carry this designation

Branches fundamentally answer the question: *What do we do if the situation changes from what we expected during this operation?*

### 1.2 Sequels: Planning Beyond Success

A **sequel** is defined as "major operations that follow the current major operation. Plans for these are based on the possible outcomes (victory, stalemate, or defeat) associated with the current operation."

Key characteristics of sequels:
- **Forward-looking across operations**: Sequels concern what happens after the current mission
- **Outcome-dependent**: Different sequels exist for different results (success, failure, partial success)
- **Positions forces for the future**: Ensures current actions enable future opportunities
- **"On-Order" missions**: Sequel execution typically awaits explicit command
- **Strategic continuity**: Links tactical actions to broader campaign objectives

Sequels answer the question: *What comes next, depending on how this operation concludes?*

### 1.3 The Critical Distinction

The fundamental difference: **branches adjust the current plan while sequels extend beyond it**. A commander facing an unexpected enemy reinforcement needs a branch. A commander planning what to do after capturing an objective needs a sequel.

This distinction has profound implications for planning horizons, resource allocation, and decision-making structures. Branches require immediate readiness; sequels require strategic positioning.

---

## 2. When to Plan Branches vs. Accept Risk

Military planning resources are finite. Not every contingency warrants a fully-developed branch plan. Doctrine provides frameworks for deciding when detailed contingency planning is worth the investment.

### 2.1 The Planning Threshold Concept

The **planning threshold** differentiates between:
- **"Be Prepared To" tasks with dedicated resources**: Fully planned branches with allocated forces and materials
- **Unresourced contingency tasks**: Acknowledged possibilities without detailed planning

Decision-makers set this threshold based on:
- Probability of the contingency occurring
- Consequences if it occurs without a prepared response
- Cost of preparing the branch plan (time, cognitive resources, force allocation)
- Available slack in planning capacity

### 2.2 The EMLCOA/EMDCOA Framework

Military planning doctrine structures contingency thinking around two key enemy courses of action:

**Enemy's Most Likely Course of Action (EMLCOA)**
- What the adversary will probably do based on doctrine, capabilities, and situation
- The base plan is optimized against this scenario
- Requires the deepest analysis and most complete response planning

**Enemy's Most Dangerous Course of Action (EMDCOA)**
- The worst-case scenario that exploits weaknesses in the friendly plan
- Cannot be identified until after the friendly plan is developed
- Requires at least one contingency branch to counter

The correct sequence: (1) Develop EMLCOA, (2) Create base plan against EMLCOA, (3) Identify EMDCOA by examining plan vulnerabilities, (4) Develop contingency branch for EMDCOA.

This framework prevents both over-planning (preparing for every possibility) and under-planning (ignoring dangerous scenarios).

### 2.3 Factors Favoring Branch Development

Develop a full branch plan when:
- The contingency significantly alters mission success probability
- Response timing is critical (no time for real-time replanning)
- Resource pre-positioning is required
- Coordination across multiple units is complex
- The triggering conditions can be reliably detected
- The branch can share substantial structure with the base plan

### 2.4 Factors Favoring Risk Acceptance

Accept risk without detailed branch planning when:
- The contingency is low-probability
- Consequences are manageable through adaptation
- Branch preparation costs exceed potential benefits
- The situation would require complete replanning regardless
- Detection capabilities cannot reliably identify the trigger conditions
- Resources are better allocated to improving the base plan

---

## 3. Decision Support Matrices and Triggers

The value of branch plans depends on knowing when to execute them. Military planning has developed sophisticated tools for managing this transition.

### 3.1 The Decision Support Matrix (DSM)

The DSM is a staff product that organizes:
- **Decision Point (DP)**: Location/time where a decision is required
- **Criteria**: Conditions to evaluate at the decision point
- **Actions/Options**: What can be done based on criteria evaluation
- **Responsible Unit**: Who observes, reports, and/or acts
- **Timeline**: When the decision must be made

A well-developed DSM transforms abstract contingencies into actionable decision rules.

### 3.2 The Decision Support Template (DST)

The DST provides the graphic representation, showing:
- Decision points overlaid on the operational map/timeline
- Named Areas of Interest (NAIs) where intelligence collection occurs
- Target Areas of Interest (TAIs) where actions may be taken
- The relationships between observation, decision, and action

### 3.3 Trigger Construction

Effective triggers follow a conditional logic structure:

```
IF [condition observed at NAI]
AND [additional conditions met]
THEN [execute branch action at TAI/DP]
```

Example from doctrine:
> "IF we identify an enemy company (-) east of Phase Line Red, AND we have identified minimal enemy forces north of XXX, THEN we will displace Alpha to battle position 4A to block penetration in the south."

This structure makes explicit:
- What to look for
- What additional context matters
- What action follows
- Who is responsible

### 3.4 Decision Point Placement

Decision points must be placed to allow sufficient time for action execution. The DP appears "at a point representing the last possible point at which the commander can make his decision" before the action must begin. Placing it earlier provides more flexibility; placing it later allows more information gathering.

This creates a fundamental tension: **decide early with less information, or decide late with less response time**.

---

## 4. Fragmentary Orders (FRAGOs) for Branch Execution

When a branch is triggered, execution occurs through a Fragmentary Order (FRAGO).

### 4.1 FRAGO Definition and Purpose

A FRAGO is "an abbreviated operation order issued as needed to change or modify an order or to execute a branch or sequel." It is not a complete replan but an adaptation of the existing order.

Key characteristics:
- **Abbreviated format**: Only addresses changed elements
- **References base order**: "No change" suffices for unaffected portions
- **Rapid dissemination**: Designed for speed over completeness
- **Maintains synchronization**: Updates all affected units simultaneously

### 4.2 FRAGO Structure

While FRAGOs have no mandated format, they typically follow an abbreviated OPORD structure:
1. **Situation**: Brief update on enemy/friendly changes driving the FRAGO
2. **Mission**: Modified mission statement (if changed)
3. **Execution**: New tasks for subordinate units
4. **Sustainment**: Logistics/support changes
5. **Command and Signal**: Communication/control changes

Each paragraph either provides new information or states "No change."

### 4.3 Pre-Planned FRAGOs

For anticipated branches, FRAGOs can be substantially pre-planned. Desert Storm famously used numbered FRAGPLANs (e.g., "FRAGPLAN 7") that could be invoked by reference when triggering conditions occurred. This approach:
- Minimizes communication bandwidth during execution
- Reduces decision-making load at critical moments
- Ensures all units have consistent understanding
- Enables faster transition to contingency operations

---

## 5. Resource Pre-Positioning for Branch Execution

A branch plan is only as good as the ability to execute it. This requires thoughtful resource positioning.

### 5.1 The Pre-Positioning Concept

Military doctrine emphasizes **Pre-positioned War Reserve Materiel (PWRM)**: "materiel strategically located to facilitate a timely response in support of combatant commander requirements during the initial phases of an operation."

Pre-positioning serves branch execution by:
- Reducing response time when branches are triggered
- Decreasing demand on transportation during transitions
- Enabling actions that would otherwise be logistically impossible
- Providing redundancy if primary plans fail

### 5.2 Types of Pre-Positioned Resources

**Starter Stock**: Resources positioned for immediate operational use
**Swing Stock**: Resources positioned to support multiple contingencies across different areas

For branch planning, the relevant question is: *What resources must be in position before we know whether this branch will execute?*

### 5.3 The Pre-Positioning Trade-off

Pre-positioning resources for contingencies that may not occur has costs:
- Resources are committed and unavailable for other uses
- Positioning reveals potential courses of action to adversaries
- Maintenance and protection of pre-positioned assets consumes effort
- If the branch never executes, the investment is "wasted"

Effective planning balances these costs against the value of rapid branch execution.

---

## 6. Application to AI Agent Adaptive Planning

The branches-and-sequels framework offers direct applicability to AI agent systems operating in uncertain environments.

### 6.1 Mapping Concepts to Agent Systems

| Military Concept | Agent System Analog |
|-----------------|---------------------|
| Branch | Conditional alternative plan within current task |
| Sequel | Post-task planning based on outcomes |
| Decision Point | Checkpoint where plan validity is assessed |
| FRAGO | Plan modification message to sub-agents |
| NAI | Information gathering action/query |
| TAI | Action execution target |
| EMLCOA | Expected environment/user behavior |
| EMDCOA | Failure mode requiring contingency |
| Pre-positioned resources | Pre-computed solutions, cached context |

### 6.2 Agent Branch Planning

Agents can develop branches for anticipated complications:

```
Base Plan: Query database A, transform results, return to user

Branch 1 (Database Unavailable):
  Trigger: Connection timeout or error response
  Action: Fall back to cached results with staleness warning

Branch 2 (Results Too Large):
  Trigger: Result count exceeds threshold
  Action: Apply pagination, request user filtering criteria

Branch 3 (Ambiguous Query):
  Trigger: Multiple valid interpretations detected
  Action: Present interpretations, request clarification
```

Each branch is pre-planned with clear triggers and actions, avoiding expensive real-time replanning.

### 6.3 Agent Sequel Planning

Sequels enable agents to maintain momentum across task boundaries:

```
Current Task: Generate initial draft of document

Sequel (Success):
  Condition: Draft accepted
  Next: Proceed to formatting and polish phase

Sequel (Revision Needed):
  Condition: User requests changes
  Next: Enter revision cycle with change tracking

Sequel (Rejection):
  Condition: Approach fundamentally wrong
  Next: Return to requirements gathering with new questions
```

Planning sequels prevents the "now what?" pause after task completion.

### 6.4 Agent Decision Support Structures

Agents can implement DSM-like structures:

```python
decision_point = {
    "id": "DP_API_RESPONSE",
    "location": "after_api_call",
    "criteria": {
        "success": "status_code == 200",
        "rate_limited": "status_code == 429",
        "server_error": "status_code >= 500",
        "timeout": "response_time > threshold"
    },
    "actions": {
        "success": "continue_base_plan",
        "rate_limited": "execute_branch_backoff",
        "server_error": "execute_branch_retry",
        "timeout": "execute_branch_alternate_source"
    }
}
```

---

## 7. Pre-Computing vs. Real-Time Replanning

A central tension in contingency planning: how much to pre-compute versus computing on demand.

### 7.1 Arguments for Pre-Computation (Branch Plans)

**Speed**: Pre-planned branches execute faster than real-time planning
**Consistency**: Pre-computation allows review and validation
**Coordination**: Multiple actors can synchronize on pre-planned contingencies
**Cognitive load**: Decision-makers need only recognize triggers, not invent responses
**Resource positioning**: Pre-positioning requires advance planning

### 7.2 Arguments for Real-Time Replanning

**Flexibility**: Actual situations rarely match anticipated contingencies exactly
**Resource efficiency**: Avoid planning for contingencies that never occur
**Information advantage**: Real-time planning uses latest information
**Novel situations**: Pre-computation cannot anticipate truly unexpected events

### 7.3 The Military Solution: Layered Approach

Doctrine advocates a hybrid approach:
1. **Fully-developed branches** for high-probability, high-consequence contingencies
2. **Outlined responses** for moderate contingencies (decision logic without full detail)
3. **Acceptance of replanning** for low-probability or novel situations

This maps to agent systems:
1. **Hard-coded branches** for common failure modes
2. **Parameterized response templates** for variable situations
3. **LLM reasoning** for genuinely novel circumstances

### 7.4 The Speed-Information Trade-off

Pre-computed plans are fast but may be suboptimal given actual conditions.
Real-time replanning is optimal for actual conditions but slow.

The decision framework:
- When response time is critical, favor pre-computation
- When optimality is critical, favor real-time planning
- When both matter, use pre-computation for initial response while initiating detailed replanning

---

## 8. Failure Modes in Contingency Planning

Understanding how contingency planning fails helps agents avoid common pitfalls.

### 8.1 Planning Failures

**Over-planning**: Developing contingencies for every possibility exhausts planning resources and can delay base plan development. The military term is "analysis paralysis."

**Under-planning**: Failing to develop contingencies for likely or dangerous scenarios leaves forces unprepared when those scenarios occur.

**Stale plans**: Contingencies developed early may not reflect current conditions. Plans require continuous assessment and update.

**Misaligned triggers**: Decision criteria that don't match actual observables render branches unusable.

**Resource conflicts**: Multiple contingencies requiring the same resources cannot execute simultaneously.

### 8.2 Execution Failures

**Trigger recognition failure**: The triggering conditions occur but aren't recognized, so the branch never executes.

**Delayed execution**: The trigger is recognized too late for effective branch execution.

**Coordination breakdown**: Different units execute different plans due to communication failures.

**Branch mismatch**: The actual situation doesn't match any pre-planned branch closely enough for clean execution.

**Sequel gap**: Current operation ends without clear sequel, causing loss of initiative.

### 8.3 The Mirror-Imaging Trap

A particularly dangerous cognitive failure in contingency planning is **mirror-imaging**: assuming adversaries (or systems, or users) will think and act as the planner would. This leads to contingencies that address imagined rather than actual scenarios.

In agent systems, this manifests as building contingencies for failures the developer would make, rather than failures users or external systems actually produce.

### 8.4 Mitigation Strategies

**Red teaming**: Have separate individuals/processes attempt to defeat the base plan to identify EMDCOA scenarios.

**Wargaming**: Walk through plans against various scenarios to identify gaps and validate branches.

**Historical analysis**: Study past failures to identify recurring contingency needs.

**Continuous assessment**: Treat plans as hypotheses requiring ongoing validation, not fixed documents.

**Execution monitoring**: Actively check whether the situation matches planning assumptions.

---

## 9. Recognizing When to Invoke Contingencies

For agents, the challenge of contingency planning shifts from *development* to *recognition*: knowing when pre-planned responses apply.

### 9.1 Explicit Trigger Conditions

The simplest approach uses explicit conditional logic:
```
IF response.status_code == 429 THEN execute_rate_limit_branch()
```

Clear, fast, and deterministic, but limited to anticipated and precisely specifiable conditions.

### 9.2 Pattern Recognition

More sophisticated triggers use pattern matching across multiple signals:
```
IF (response_time > usual_mean + 2*std_dev)
   AND (error_rate > baseline * 1.5)
   AND (time_of_day in peak_hours)
THEN execute_degraded_performance_branch()
```

This catches situations that don't match any single criterion but collectively indicate a contingency.

### 9.3 Anomaly Detection

For novel situations, agents need to recognize "something is wrong" even without matching a specific contingency:
- Outputs falling outside expected distributions
- Sequences of events not seen during training/testing
- User behavior significantly diverging from models

Anomaly detection triggers general contingency responses (slow down, gather more information, escalate to human) rather than specific branches.

### 9.4 Cascading Triggers

Some contingencies reveal themselves progressively:
1. Initial indicator suggests possible issue
2. Diagnostic action confirms or rules out
3. If confirmed, branch execution begins

This allows more accurate triggering at the cost of response time.

---

## 10. Synthesis: A Framework for Agent Contingency Planning

Drawing from military doctrine, we can articulate a framework for agent contingency planning:

### 10.1 During Planning Phase

1. **Develop the base plan** optimized for expected conditions (EMLCOA equivalent)

2. **Identify critical assumptions** that, if violated, would undermine the plan

3. **Determine the most dangerous failure mode** (EMDCOA equivalent) by asking "what would cause this plan to fail catastrophically?"

4. **Develop branches** for:
   - The most dangerous failure mode (always)
   - High-probability deviations from expected conditions
   - Contingencies where response time is critical

5. **Design decision points** with:
   - Clear trigger criteria
   - Observation/detection mechanisms
   - Action specifications
   - Timing constraints

6. **Pre-position resources** needed for branch execution:
   - Cached alternative data sources
   - Pre-computed fallback responses
   - Reserved computational capacity

7. **Plan sequels** for success, partial success, and failure outcomes

### 10.2 During Execution Phase

1. **Monitor for trigger conditions** at designated decision points

2. **Recognize when contingencies apply** through explicit triggers, pattern matching, or anomaly detection

3. **Execute branches via FRAGO-equivalent** minimal plan modifications rather than full replanning

4. **Maintain sequel awareness** so completion of current task flows into appropriate next action

5. **Update plans continuously** as execution reveals new information about conditions

### 10.3 Anti-Patterns to Avoid

- Planning only for the happy path
- Developing contingencies without clear triggers
- Pre-planning so extensively that base execution is delayed
- Failing to recognize when actual situations require branch execution
- Treating plan completion as task completion (forgetting sequels)
- Mirror-imaging expected failure modes
- Neglecting continuous plan assessment and update

---

## References and Sources

This research draws from multiple military doctrinal sources and AI planning literature:

### Military Doctrine
- US Army FM 5-0: Army Planning and Orders Production
- US Army ADP 5-0: The Operations Process
- Joint Publication JP 5-0: Joint Planning
- Air Force Doctrine Publication 5-0: Planning
- US Marine Corps MCWP 5-10: Marine Corps Planning Process

### Planning Tools and Techniques
- Decision Support Matrices and Templates (CALL publications)
- Military Decision Making Process (MDMP) documentation
- Campaign Planning Handbook (Army War College)

### AI Planning
- AAAI research on contingent planning and replanning
- IBM documentation on AI agent planning frameworks

---

## Conclusion

The branches-and-sequels framework represents centuries of accumulated wisdom about planning under uncertainty. For AI agent systems, this doctrine offers immediately applicable concepts:

- **Distinguish branches (mid-task adaptations) from sequels (post-task continuations)**
- **Use explicit decision points with clear triggers**
- **Balance pre-computation against real-time replanning based on time criticality**
- **Pre-position resources for contingencies worth preparing**
- **Monitor for trigger conditions during execution**
- **Plan for success, failure, and the gray zones between**

The fundamental insight is that **good planning anticipates the need to deviate from the plan**. An agent that only knows how to execute its base plan is fragile. An agent with well-developed branches and sequels maintains effectiveness across the range of conditions it actually encounters.

As with military operations, the goal is not to predict the future perfectly but to **reduce the decision space during execution** to manageable, pre-analyzed choices. When the unexpected occurs, the question shifts from "what should I do?" to "which prepared response best fits this situation?"

This is the essence of adaptive planning: not rigidity, not pure improvisation, but **prepared flexibility**.
