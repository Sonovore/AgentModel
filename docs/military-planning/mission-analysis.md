# Mission Analysis: From Military Doctrine to Agent Task Decomposition

## Overview

Mission Analysis is the critical first step in military decision-making that transforms broad directives into actionable understanding. In the Military Decision-Making Process (MDMP), it occupies Step 2 of 7 and contains 18-19 substeps, making it the most comprehensive phase of planning. Many experienced commanders consider it the most important step because it defines the problem, clarifies scope, and establishes the foundation for all subsequent planning.

This document examines mission analysis through the lens of military doctrine (MDMP and TLP) and explores its application to AI agent task decomposition. The goal is to extract principles that help agents understand not just what they are told to do, but what they actually need to accomplish.

## The Role of Mission Analysis in Military Planning

### Military Decision-Making Process (MDMP)

MDMP is the Army's principal planning methodology for battalion and higher echelons with staff support. The seven steps are:

1. **Receipt of Mission** - Initial notification and time allocation
2. **Mission Analysis** - Understanding the problem (18-19 substeps)
3. **COA Development** - Generating options
4. **COA Analysis** - Testing options through wargaming
5. **COA Comparison** - Evaluating options against criteria
6. **COA Approval** - Commander selects approach
7. **Orders Production** - Translating decision into executable orders

Mission analysis serves as the bridge between receiving vague or incomplete guidance and understanding what actually needs to be accomplished. As doctrine states: "Mission Analysis is the first step of the Command Estimate/Tactical Decision Making Process. It is defined as the process of identifying all the required tasks for a specific mission, and producing your own mission statement."

The outputs of Mission Analysis include:
- Approved problem statement
- Approved mission statement
- Initial Commander's Intent
- Initial Commander's Critical Information Requirements (CCIR)
- Updated Intelligence Preparation of the Battlefield (IPB)
- Assumptions
- Resource shortfalls
- Course of Action evaluation criteria

### Troop Leading Procedures (TLP)

TLP is the streamlined version for small-unit leaders (company and below) operating with limited or no staff. Its eight steps are:

1. Receive the Mission
2. Issue a Warning Order
3. Make a Tentative Plan
4. Start Necessary Movement
5. Reconnoiter
6. Complete the Plan
7. Issue the Complete Order
8. Supervise

In TLP, mission analysis occurs primarily in Step 3 (Make a Tentative Plan) and is condensed due to time constraints. Leaders use METT-TC analysis (Mission, Enemy, Terrain, Troops, Time, Civil Considerations) to rapidly assess the situation. The 1/3-2/3 Rule applies: leaders should use no more than one-third of available time for their own planning, reserving two-thirds for subordinates to plan and prepare.

## The Task Hierarchy: Specified, Implied, and Essential

The core of mission analysis is decomposing higher headquarters' orders into three categories of tasks. This decomposition reveals the gap between what is explicitly stated and what must actually happen.

### Specified Tasks

**Definition:** Tasks clearly and explicitly stated in the higher headquarters' order.

Specified tasks are found throughout the Operations Order (OPORD), particularly in:
- Paragraph 2 (Mission)
- Paragraph 3 (Execution - concept of operations, tasks to subordinate units, coordinating instructions)
- Annexes and overlays

**Examples of specified tasks:**
- "Seize Objective FOX"
- "Reconnoiter Route BLUE"
- "Assist the forward passage of 1st Platoon, B Company"
- "Maintain a two-battalion reserve"

Specified tasks appear straightforward, but their simplicity can be deceptive. The order "seize Objective FOX" does not specify how to approach the objective, what enemy resistance to expect, or how to consolidate after seizure.

### Implied Tasks

**Definition:** Tasks not explicitly stated but required to accomplish specified tasks or the overall mission.

Implied tasks are developed and deduced by the commander and staff through:
- Detailed analysis of higher headquarters' orders
- Analysis of enemy situation and courses of action
- Terrain analysis
- Knowledge of doctrine and history
- Reconnaissance (actual or map)

**Key characteristics of implied tasks:**
- Not specifically stated in the OPORD or OPLAN
- MUST be accomplished to satisfy any specified task
- NOT routine, inherent, or SOP-based tasks (these are excluded)

**Classic examples:**

1. **River Crossing:** If the specified task is "Seize Objective ALPHA" and a river lies between your position and the objective (not mentioned in the OPORD), identifying and planning a river-crossing operation is an implied task.

2. **Obstacle Handover:** During a relief-in-place mission, obstacle-handover coordination between units, if not specified, is an implied task.

3. **Reconnaissance:** Before conducting a movement to contact, route reconnaissance may be implied even if not explicitly directed.

**The derivation process:**

A mature staff does not simply write "conduct river crossing" and move on. They analyze the task: Where is the river narrow enough? Where are the approaches solid enough? What is the angle of the banks for bridge emplacement? An immature staff captures things the commander already knows; a mature staff focuses on what the commander needs.

### Essential Tasks

**Definition:** Those tasks from the specified and implied task lists that MUST be accomplished to complete the overall mission.

Essential tasks have specific characteristics:
- Failure to accomplish results in mission failure
- Define the "WHAT" portion of the restated mission
- Are listed chronologically in the restated mission
- Become the basis for the unit's mission statement

**The filtering process:**

From a potentially long list of specified and implied tasks, the commander identifies which are truly essential - which ones, if not accomplished, mean the mission fails. This is the "so what" determination. Not every task carries equal weight; essential tasks are the critical few that define success.

**Example distinction:**

For an operation to seize a bridge:
- **Specified tasks:** "Seize Bridge ALPHA. Prevent enemy reinforcement across the river."
- **Implied tasks:** Conduct route reconnaissance. Establish blocking positions on far side. Coordinate with adjacent units. Prepare for counterattack.
- **Essential tasks:** Seize intact bridge. Deny enemy use of crossing site. (These define mission success - without an intact bridge or with enemy still crossing, the mission fails regardless of other accomplishments.)

## Constraints, Limitations, and Boundaries

Mission analysis identifies the boundaries of acceptable action through constraints and limitations.

### Constraints (Must Do)

Constraints restrict freedom of action by specifying things the unit MUST do. They are non-negotiable requirements imposed by higher headquarters.

**Examples:**
- "Maintain a two-battalion reserve"
- "Occupy designated battle positions"
- "Coordinate all fires above Phase Line BLUE with Division"
- "All movements must occur during hours of darkness"

Constraints can be issued through:
- Warning Orders (WARNORDs)
- Operations Orders (OPORDs)
- Policy memorandums
- Verbal orders

### Restrictions (Must Not Do)

Restrictions are limitations placed on the command that prohibit certain actions.

**Examples:**
- "Do not conduct reconnaissance prior to H-Hour"
- "Limit of advance is Phase Line YELLOW"
- "Do not destroy civilian infrastructure"
- "Do not engage targets beyond the fire support coordination line without approval"

### The Interplay of Constraints and Restrictions

Together, constraints and restrictions define the operating envelope. A commander might have wide latitude in HOW to accomplish the mission but strict requirements about WHAT must or must not be done. Understanding this envelope is critical because:

1. Violating constraints can cause mission failure for the higher headquarters
2. Violating restrictions can cause unintended strategic consequences
3. Both limit the solution space for course of action development

## Assumptions and Their Validation

### The Nature of Assumptions

An assumption is "a supposition on the current situation or a presupposition on the future course of events, either or both assumed to be true in the absence of positive proof, necessary to enable the commander in the process of planning to complete an estimate of the situation and make a decision."

Assumptions replace missing or unknown information to enable continued planning. However, they introduce risk - every assumption is a potential point of failure.

### Requirements for Valid Assumptions

Each assumption must be:
1. **Valid** - Is the assumption likely to occur? Is it reasonable?
2. **Necessary** - Can planning continue without this assumption?

If an assumption is not necessary, discard it. If it is not valid (unlikely to be true), the plan may be built on a false foundation.

### Categories of Assumptions

Assumptions typically fall into four categories:
1. **Time** - Assumptions about timelines, deadlines, durations
2. **Political** - Assumptions about authorization, rules of engagement, national will
3. **Enemy** - Assumptions about adversary capabilities, intentions, reactions
4. **Friendly Forces** - Assumptions about own-force capabilities, availability, readiness

### Prioritizing Assumptions by Risk

Staff may prioritize assumptions in terms of consequence:
- **Highest priority:** Assumptions that, if wrong, cause mission failure
- **Medium priority:** Assumptions that, if wrong, lead to partial mission failure
- **Lower priority:** Assumptions that, if wrong, affect timing and tempo

High-priority assumptions are essential for identifying branches (contingency plans) and sequels (follow-on operations).

### Assumption Management

Key principles:
- Replace assumptions with facts as soon as possible
- Develop information requirements to validate assumptions
- Plan branches for cases where critical assumptions prove false
- Brief the commander on which assumptions carry the highest risk

As doctrine notes: "Assumptions induce risk into operational planning." Every assumption should be treated as a temporary placeholder for truth, not a permanent foundation.

## Restating the Mission: The Five Ws

The culmination of mission analysis is the restated mission - a clear, concise statement that captures the unit's purpose in the operation. The restated mission answers five questions:

1. **WHO** - The unit executing the mission
2. **WHAT** - The essential tasks and type of operation (listed chronologically)
3. **WHEN** - The time specified in the order
4. **WHERE** - The objective or location
5. **WHY** - The unit's purpose (from the higher headquarters' concept of operations)

### Example Format

"2d Brigade (WHO) conducts movement to contact (operation) commencing 25 Feb 2024 (WHEN) to clear (WHAT/task) enemy forces from AO Zack (WHERE) to allow its use for division rear area operations (WHY/purpose)."

### The Importance of "Why"

The purpose (why) is arguably the most important element because it:
- Connects the unit's actions to the higher headquarters' intent
- Enables subordinates to adapt when conditions change
- Provides the metric for evaluating success

A unit might accomplish all specified tasks and still fail the mission if those tasks do not achieve the purpose. Conversely, a unit might deviate from specified tasks but succeed if the purpose is achieved.

## Commander's Intent and Mission Command

Mission analysis operates within the broader philosophy of Mission Command - "the Army's approach to command and control that empowers subordinate decision-making and decentralized execution appropriate to the situation."

### Commander's Intent

Commander's intent is "a clear and concise expression of the purpose of the operation and the desired military end state that supports mission command." It contains:

1. **Purpose** - Why the operation is being conducted
2. **Key Tasks** - Critical activities that contribute to success
3. **End State** - What conditions look like when the operation succeeds

The intent must be understood two echelons below the issuing commander. This enables disciplined initiative - subordinates can act without further orders when the situation changes because they understand what the commander is trying to achieve.

### The Trust Foundation

Mission command requires mutual trust:
- Commanders trust subordinates to make decisions within intent
- Subordinates trust commanders will accept and support their decisions
- Both parties accept that mistakes will happen when taking aggressive action

This trust enables speed. As doctrine states: "Mission command provides the means to operate at the speed of the problem."

## Application to Agent Task Decomposition

The military's mission analysis framework offers direct parallels for AI agent systems, particularly in how agents understand, decompose, and execute tasks from human principals.

### Mapping Military Concepts to Agent Systems

| Military Concept | Agent System Analog |
|-----------------|---------------------|
| Higher HQ Order | User prompt or task instruction |
| Commander's Intent | Underlying user goal/desired outcome |
| Specified Tasks | Explicitly stated requirements |
| Implied Tasks | Unstated prerequisites and dependencies |
| Essential Tasks | Success criteria / definition of done |
| Constraints | Explicit rules (must do) |
| Restrictions | Boundaries (must not do) |
| Assumptions | Inferences about context, environment, resources |
| Restated Mission | Agent's internal task representation |

### How Agents Should Identify Implied Tasks

Like a mature military staff, effective agents must go beyond surface-level task capture to identify implied requirements:

1. **Analyze dependencies:** What must be true before the specified task can begin? What resources, information, or conditions are prerequisites?

2. **Consider the environment:** What context is assumed but not stated? File locations, system states, authentication requirements?

3. **Examine the gap:** What lies between current state and desired end state that is not explicitly addressed?

4. **Apply domain knowledge:** What does accomplishing this type of task typically require? What do users normally expect even if unstated?

5. **Check for logical completeness:** Does the set of specified tasks actually achieve the stated purpose? What is missing?

**Example - User prompt:** "Deploy the application to production"

**Specified task:** Deploy application to production environment

**Implied tasks (a mature agent might identify):**
- Verify tests pass
- Check that required environment variables are configured
- Ensure database migrations are current
- Confirm sufficient resources are available
- Create rollback plan
- Update monitoring and alerting
- Notify relevant stakeholders

**Essential task:** Application running correctly in production, serving users

### Agents and Constraint Recognition

Agents must recognize both explicit and implicit constraints:

**Explicit constraints (from prompt/system instructions):**
- "Use only approved libraries"
- "Do not modify production database directly"
- "All changes must be logged"

**Implicit constraints (from context/domain):**
- Security requirements for the environment
- Coding standards of the codebase
- Organizational policies
- Resource limitations

### Agents and Assumption Management

Agents face unique challenges with assumptions:

1. **Assumptions are often unavoidable:** Limited context forces agents to make assumptions about intent, environment, and expectations.

2. **Assumptions should be surfaced:** Rather than silently assuming, agents should identify critical assumptions and validate them when stakes are high.

3. **Assumption failure should trigger adaptation:** When an assumption proves false (file doesn't exist, command fails, environment differs), agents should re-evaluate their approach rather than blindly proceeding.

4. **High-risk assumptions warrant confirmation:** If an assumption, if wrong, would cause significant harm or waste, the agent should seek clarification from the user.

### The Agent's Restated Mission

Before executing, an agent should internally formulate its understanding:

- **WHO:** This agent instance
- **WHAT:** Essential tasks (in order of execution)
- **WHEN:** Any time constraints or deadlines
- **WHERE:** Target environment/system/files
- **WHY:** User's underlying goal (not just the literal request)

This internal restatement helps ensure the agent has truly understood the task before acting.

## Failure Modes in Mission Analysis

Military doctrine and practice have identified numerous failure modes that apply equally to agent systems.

### Failure Mode 1: Insufficient Analysis

**Military manifestation:** Rushing through mission analysis to begin COA development. Taking 10% of time on MA instead of the recommended 30%.

**Agent manifestation:** Immediately executing without fully parsing the request. Missing implications, dependencies, or constraints because of eagerness to act.

**Mitigation:** Enforce deliberate analysis before execution. Build in explicit "understanding" phases.

### Failure Mode 2: Immature Task Identification

**Military manifestation:** Simply listing "conduct river crossing" without analyzing the specific requirements, locations, and resources needed.

**Agent manifestation:** Identifying surface tasks without exploring depth. Treating "deploy application" as a single task rather than decomposing into constituent requirements.

**Mitigation:** Train agents to probe deeper on each identified task. Ask "what does accomplishing this actually require?"

### Failure Mode 3: Copy-Paste Planning

**Military manifestation:** Using archived files from similar missions without proper adaptation to current conditions.

**Agent manifestation:** Applying cached patterns or templates without verifying they fit the current context.

**Mitigation:** Require validation that prior approaches apply. Treat each task as potentially unique until confirmed otherwise.

### Failure Mode 4: Unvalidated Assumptions

**Military manifestation:** Making assumptions as a checklist item without actually testing or tracking them.

**Agent manifestation:** Proceeding on inferences that were never verified. Assuming file locations, permissions, or states that may not be true.

**Mitigation:** Track assumptions explicitly. Validate critical assumptions before dependent actions.

### Failure Mode 5: Missing CCIRs Tied to Decisions

**Military manifestation:** Information requirements not connected to actual decision points.

**Agent manifestation:** Gathering information that does not inform the actual task. Not identifying what information gaps would change the approach.

**Mitigation:** Connect information needs to decisions. For each uncertainty, ask "what would I do differently if I knew this?"

### Failure Mode 6: Failure to Identify Decision Points

**Military manifestation:** Plans without clear criteria for when to adapt or abort.

**Agent manifestation:** Linear execution without checkpoints. No criteria for when to pause, ask for help, or change approach.

**Mitigation:** Pre-identify decision points. Define conditions that should trigger re-evaluation.

### Failure Mode 7: Ignoring Time/Distance Analysis

**Military manifestation:** Not calculating how long constituent actions take, leading to impossible timelines.

**Agent manifestation:** Not estimating task complexity or execution time. Committing to approaches that cannot complete within constraints.

**Mitigation:** Estimate scope before committing. Flag when tasks may exceed available resources or time.

### Failure Mode 8: Coordination Gaps

**Military manifestation:** Assuming coordination happened when it did not. Units acting on incomplete shared understanding.

**Agent manifestation:** In multi-agent systems, assuming other agents have completed their work or share understanding when they do not.

**Mitigation:** Explicit coordination checkpoints. Verify shared state rather than assuming it.

## Synthesis: Mission Analysis Principles for Agents

Drawing from military doctrine, the following principles should guide agent task understanding:

1. **Understand before acting.** Mission analysis precedes course of action development. Agents should fully parse and decompose tasks before beginning execution.

2. **Surface the implicit.** Much of what is needed is not stated. Agents must identify implied tasks through analysis of dependencies, context, and domain knowledge.

3. **Identify what is essential.** Not all tasks are equal. Determine which tasks define mission success and prioritize accordingly.

4. **Respect boundaries.** Constraints (must do) and restrictions (must not do) define the envelope of acceptable action. Violating them can cause failure even if the core task is accomplished.

5. **Manage assumptions explicitly.** Every inference is a potential point of failure. Validate critical assumptions and plan for cases where they prove false.

6. **Connect tasks to purpose.** Always understand WHY. The purpose enables adaptation when conditions change.

7. **Plan for failure.** Identify decision points, abort criteria, and branches. Know what information would change the approach.

8. **Reserve time for subordinates.** In hierarchical systems, leave sufficient resources for lower levels to plan and execute. The 1/3-2/3 rule applies.

9. **Maintain shared understanding.** In multi-agent contexts, ensure all participants have the same picture before execution.

10. **Iterate and refine.** Mission analysis is not one-and-done. As new information emerges, update the understanding.

## Conclusion

Military mission analysis has evolved over centuries to address a fundamental problem: translating ambiguous, incomplete directives into effective action under uncertainty and time pressure. The framework of specified, implied, and essential tasks - bounded by constraints and limitations, founded on validated assumptions, and unified by commander's intent - provides a robust methodology for task understanding.

For AI agent systems, these principles offer a tested framework for moving beyond literal instruction-following toward true task comprehension. Agents that can identify implied requirements, distinguish essential from peripheral tasks, recognize boundaries, manage assumptions, and connect actions to purpose will more reliably accomplish what users actually need - not just what they literally said.

The gap between specified and essential is where mission analysis earns its value. Closing that gap is the work of understanding.

---

## References

### Primary Doctrinal Sources
- FM 5-0 (Army Planning and Orders Production)
- ADP 5-0 (The Operations Process)
- ADP 6-0 (Mission Command)
- ATP 5-19 (Risk Management)
- FM 101-5 (Staff Organization and Operations)

### Web Sources Consulted
- [Mission Analysis Overview](https://irp.fas.org/doddir/army/miobc/msnanllp.htm) - FAS
- [MDMP Lessons and Best Practices](https://apps.dtic.mil/sti/pdfs/AD1018227.pdf) - DTIC
- [MDMP Comprehensive Guide](https://ohiomilitaryreserve.wordpress.com/2024/07/18/the-military-decision-making-process-mdmp-a-comprehensive-guide/) - Ohio Military Reserve
- [Troop Leading Procedures](https://www.thelightningpress.com/troop-leading-procedures-tlp/) - Lightning Press
- [About MDMP](https://www.thelightningpress.com/about-the-military-decisionmaking-process-mdmp/) - Lightning Press
- [Commander's Intent](https://en.wikipedia.org/wiki/Intent_(military)) - Wikipedia
- [Mission Command](https://en.wikipedia.org/wiki/Mission_command) - Wikipedia
- [Understanding Mission Command](https://www.army.mil/article/106872/understanding_mission_command) - Army.mil
- [Planning: Preventing Preventable Problems](https://www.army.mil/article/284810/planning_preventing_preventable_problems_in_military_decision_making_process) - Army.mil
- [Implied Tasks - The Hidden Implications](https://apps.dtic.mil/sti/pdfs/AD1158248.pdf) - DTIC
- [METT-TC Introduction](https://www.trex-arms.com/what-is-mett-tc-part-1-introduction/) - T.REX Arms
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) - Lilian Weng
- [Understanding the Planning of LLM Agents](https://arxiv.org/abs/2402.02716) - arXiv

---

*Document created for the AgentModel project - research on agent orchestration patterns.*
