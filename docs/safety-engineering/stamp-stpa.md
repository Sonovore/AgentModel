# STAMP and STPA for Agent Safety

Systems-Theoretic Accident Model and Processes (STAMP) and System-Theoretic Process Analysis (STPA) applied to AI agent supervision.

## Background

| Aspect | Description |
|--------|-------------|
| **Creator** | Nancy Leveson (MIT Aeronautics & Astronautics) |
| **Origin** | "Engineering a Safer World" (2011), building on "A New Accident Model for Engineering Safer Systems" (2004) |
| **Core Insight** | Accidents result from inadequate CONTROL, not component failures |
| **Foundation** | Systems theory and control theory, not reliability theory |
| **Key Shift** | Safety is an emergent property of the system, not a property of components |

## Why Traditional Methods Are Insufficient

### The Problem with Fault Trees, FMEA, and Event Chains

Traditional safety analysis methods were designed for simpler, electromechanical systems. They share common assumptions that break down in complex sociotechnical systems:

| Method | Assumption | Why It Fails for Complex Systems |
|--------|------------|----------------------------------|
| **Fault Tree Analysis (FTA)** | Accidents result from chains of component failures | Cannot model software errors, design flaws, or coordination failures |
| **FMEA** | Enumerate all failure modes of components | Software doesn't "fail" like hardware - it does exactly what it's programmed to do |
| **Event Trees** | Linear cause-effect chains explain accidents | Cannot capture emergent behavior or feedback loops |
| **Probabilistic Risk Assessment** | Random failures can be quantified | Software failures are systematic, not random |

### What These Methods Miss

Traditional methods struggle with:

1. **Component Interaction Accidents** - Components work correctly individually but fail together
2. **Software Errors** - Software doesn't degrade; it follows flawed instructions precisely
3. **Human Error** - Humans make decisions that seem rational given their information
4. **Organizational Factors** - Management decisions that create unsafe conditions
5. **Requirements Flaws** - The system does what it was designed to do, but the design was wrong
6. **Emergent Behavior** - System-level properties that cannot be predicted from component analysis

**Leveson's Key Critique:** Almost all traditional risk assessment techniques rely on linear chains of cause and effect. They cannot handle the non-linear, tightly coupled interactions in modern systems.

## STAMP Foundations

### Safety as a Control Problem

STAMP reconceptualizes safety:

| Traditional View | STAMP View |
|------------------|------------|
| Safety = absence of failures | Safety = enforcement of constraints |
| Accidents = chains of failures | Accidents = inadequate control |
| Fix = prevent component failures | Fix = improve control structure |
| Analysis unit = components | Analysis unit = control loops |
| Safety is a component property | Safety is an emergent property |

**Core principle:** Safety is an emergent property that arises from the interactions among system components. It cannot be achieved by making components reliable; it requires that the system's control structure enforces necessary safety constraints.

### Emergent Properties

Emergent properties arise from the system as a whole, not from individual components:

```
Component Level:
[A] works correctly
[B] works correctly
[C] works correctly

System Level:
[A]--[B]--[C] together produce unexpected behavior

The "unexpected behavior" is EMERGENT -
it exists only in the interaction, not in any component.
```

**Safety is emergent.** You cannot make a system safe by making each part safe. The interactions create new hazards that don't exist in the parts.

### Three Basic Concepts of STAMP

1. **Safety Constraints** - The constraints that must be enforced to prevent hazards
2. **Hierarchical Control Structure** - The organizational and technical structure that enforces constraints
3. **Process Model** - Each controller's mental model of the process being controlled

## The Control Structure Concept

### Elements of a Control Loop

```
              ┌─────────────────────────────────────────────────┐
              │                  CONTROLLER                      │
              │                                                  │
              │   ┌─────────────────────────────────────────┐   │
              │   │           PROCESS MODEL                  │   │
              │   │   (Beliefs about controlled process)     │   │
              │   └─────────────────────────────────────────┘   │
              │                      │                          │
              │   ┌──────────────────┴──────────────────┐      │
              │   │         CONTROL ALGORITHM            │      │
              │   │   (How to select control actions)    │      │
              │   └──────────────────┬──────────────────┘      │
              └──────────────────────┼──────────────────────────┘
                                     │
                          ┌──────────┴──────────┐
                          │   CONTROL ACTIONS    │
                          │   (Commands, directives)
                          └──────────┬──────────┘
                                     │
                                     ▼
                          ┌──────────────────────┐
                          │      ACTUATORS       │
                          │  (Execute actions)   │
                          └──────────┬───────────┘
                                     │
                                     ▼
              ┌──────────────────────────────────────────────────┐
              │              CONTROLLED PROCESS                   │
              │     (The system being controlled)                 │
              └──────────────────────┬───────────────────────────┘
                                     │
                                     ▼
                          ┌──────────────────────┐
                          │       SENSORS        │
                          │  (Observe process)   │
                          └──────────┬───────────┘
                                     │
                          ┌──────────┴──────────┐
                          │      FEEDBACK       │
                          │  (Process state)    │
                          └──────────┬──────────┘
                                     │
                                     └────────────────────────────► Back to Controller
```

### Component Definitions

| Component | Role | Failure Modes |
|-----------|------|---------------|
| **Controller** | Makes decisions about control actions | Wrong decisions, delayed decisions |
| **Process Model** | Controller's beliefs about the process | Inaccurate, incomplete, outdated |
| **Control Algorithm** | Rules for selecting actions | Inadequate, conflicting, missing |
| **Control Actions** | Commands issued by controller | Wrong action, missing action, late action |
| **Actuators** | Execute control actions | Failure to execute, wrong execution |
| **Controlled Process** | The system being controlled | State changes, unexpected behavior |
| **Sensors** | Observe process state | Missing, delayed, inaccurate feedback |
| **Feedback** | Information about process state | Missing, corrupted, misinterpreted |

### Hierarchical Control Structures

Real systems have multiple levels of control:

```
                    ┌───────────────────────┐
                    │    GOVERNANCE         │
                    │    (Regulations,      │
                    │     Standards)        │
                    └───────────┬───────────┘
                                │ Constraints
                                ▼
                    ┌───────────────────────┐
                    │    ORGANIZATION       │
                    │    (Management,       │
                    │     Policies)         │
                    └───────────┬───────────┘
                                │ Policies, Resources
                                ▼
                    ┌───────────────────────┐
                    │    OPERATIONS         │
                    │    (Operators,        │
                    │     Supervisors)      │
                    └───────────┬───────────┘
                                │ Instructions, Monitoring
                                ▼
                    ┌───────────────────────┐
                    │    AUTOMATION         │
                    │    (Software,         │
                    │     Control Systems)  │
                    └───────────┬───────────┘
                                │ Commands
                                ▼
                    ┌───────────────────────┐
                    │    PHYSICAL PROCESS   │
                    │    (Equipment,        │
                    │     Environment)      │
                    └───────────────────────┘
```

Each level controls the level below and receives feedback from it.

## The Process Model: Critical Concept

**The process model is the controller's understanding of the controlled process.** It includes:

- Current state beliefs
- How the process responds to control actions
- Physical laws and constraints
- Other relevant factors

### Why Process Models Cause Accidents

Most accidents in complex systems can be traced to **inadequate process models**:

| Scenario | Process Model Problem |
|----------|----------------------|
| Controller believes process is in State A when it's in State B | Outdated model |
| Controller doesn't know about a relevant variable | Incomplete model |
| Controller assumes linear response but process is non-linear | Incorrect model |
| Multiple controllers have inconsistent models | Coordination failure |

**Leveson's insight:** "Component interaction accidents can usually be explained in terms of incorrect process models."

### Process Model Failures

Process models become incorrect when:

1. **Initial model is wrong** - Built on invalid assumptions
2. **Model not updated** - Process changed but model didn't
3. **Feedback is missing** - No information to update model
4. **Feedback is wrong** - Sensors provide incorrect data
5. **Feedback is misinterpreted** - Controller misunderstands data
6. **Model update is slow** - Time lag between process change and model update

## STPA: The Analysis Method

System-Theoretic Process Analysis (STPA) is the hazard analysis technique built on STAMP.

### STPA Steps

#### Step 1: Define Losses and Hazards

**Losses** - Unacceptable outcomes (death, injury, damage, mission failure)

**Hazards** - System states that, in combination with environmental conditions, lead to losses

Example:
- **Loss:** Loss of life, property damage
- **Hazard:** Vehicle in path of another vehicle (if collision occurs, loss results)

#### Step 2: Model the Control Structure

Create a hierarchical control structure diagram showing:
- All controllers (human, automated, organizational)
- Control actions flowing downward
- Feedback flowing upward
- Interfaces between controllers

#### Step 3: Identify Unsafe Control Actions (UCAs)

For each control action, analyze how it could be hazardous using four categories.

### The Four Types of Unsafe Control Actions

| Type | Description | Example (Braking System) |
|------|-------------|-------------------------|
| **1. Not providing causes hazard** | Required control action not given | Driver doesn't brake when obstacle appears |
| **2. Providing causes hazard** | Control action given when should not be | Brakes applied when road is icy (causes skid) |
| **3. Too early/late/wrong order** | Timing or sequence is wrong | Brakes applied too late to avoid collision |
| **4. Stopped too soon/applied too long** | Duration is wrong (continuous actions) | Brakes released before vehicle fully stopped |

**These four categories are provably complete** - any unsafe control action must fall into one of these types.

#### Step 4: Identify Loss Scenarios (Causal Factors)

For each UCA, identify why it might occur. The STPA framework provides structure:

**Control Action Not Executed Correctly:**
- Actuator fails
- Control action blocked
- Wrong process state
- External interference

**Unsafe Control Input:**
- From other controllers
- From external sources
- Conflicting control

**Inadequate Control Algorithm:**
- Flaws in design
- Inadequate for the process
- Degrades over time

**Inadequate Process Model:**
- Wrong initial model
- Model not updated
- Feedback problems (missing, delayed, incorrect)

**Inadequate Feedback/Sensing:**
- Sensor failures
- Missing feedback paths
- Time delays
- Communication failures

## Causal Factors for Unsafe Control

### Controller Failures

| Factor | Description | Example |
|--------|-------------|---------|
| **Inadequate control algorithm** | Controller's decision logic is flawed | Algorithm doesn't handle edge case |
| **Algorithm degradation** | Algorithm becomes inadequate over time | Process changed but algorithm didn't |
| **Mode confusion** | Controller in wrong mode | Thinks system is in manual when in auto |

### Inadequate Process Model

| Factor | Description | Example |
|--------|-------------|---------|
| **Invalid assumptions** | Model built on false premises | Assumed process is linear when it's not |
| **Missing state variables** | Model doesn't include relevant factors | Didn't account for temperature effects |
| **Stale information** | Model not updated with new data | Using yesterday's information |
| **Misinterpretation** | Correct data, wrong conclusion | Misread sensor output |

### Communication and Coordination Failures

| Factor | Description | Example |
|--------|-------------|---------|
| **Missing communication** | Information not transmitted | Alert not sent |
| **Delayed communication** | Information arrives too late | Warning received after action needed |
| **Corrupted communication** | Information is garbled | Bit errors in transmission |
| **Conflicting control** | Multiple controllers give contradictory commands | Two systems both try to control same actuator |

### Feedback Failures

| Factor | Description | Example |
|--------|-------------|---------|
| **Missing feedback** | No information path exists | No sensor for that variable |
| **Inadequate feedback** | Information insufficient for control | Sensor precision too low |
| **Delayed feedback** | Information arrives too late | Batch processing instead of real-time |
| **Incorrect feedback** | Sensors provide wrong data | Calibration drift |

## Agent Application

### What's the Control Structure for Agent Supervision?

```
              ┌─────────────────────────────────────────────────┐
              │           HUMAN SUPERVISOR                       │
              │                                                  │
              │   Process Model:                                 │
              │   - What the agent is capable of                 │
              │   - Current task state                           │
              │   - Agent's understanding (believed)             │
              │   - System constraints                           │
              │                                                  │
              │   Control Algorithm:                             │
              │   - When to intervene                            │
              │   - What guidance to provide                     │
              │   - When to approve/reject                       │
              └──────────────────────┬──────────────────────────┘
                                     │
                          Control Actions:
                          - Task instructions
                          - Approvals/rejections
                          - Corrections
                          - Stop commands
                                     │
                                     ▼
              ┌─────────────────────────────────────────────────┐
              │                  AI AGENT                        │
              │                                                  │
              │   Process Model:                                 │
              │   - Understanding of task                        │
              │   - Model of codebase/system                     │
              │   - Expected effects of actions                  │
              │   - Constraints and requirements                 │
              │                                                  │
              │   Control Algorithm:                             │
              │   - How to break down task                       │
              │   - How to select actions                        │
              │   - When to ask for help                         │
              └──────────────────────┬──────────────────────────┘
                                     │
                          Control Actions:
                          - Code changes
                          - Commands executed
                          - Files modified
                          - API calls made
                                     │
                                     ▼
              ┌─────────────────────────────────────────────────┐
              │            CODEBASE / SYSTEM                     │
              │                                                  │
              │   (The technical environment being modified)     │
              └──────────────────────┬───────────────────────────┘
                                     │
                          Feedback to Agent:
                          - Build results
                          - Test results
                          - Error messages
                          - System state
                                     │
                                     └──────────────────────────────┐
                                                                    │
              ┌─────────────────────────────────────────────────────┘
              │
              │         Feedback to Human:
              ▼         - Agent progress reports
              │         - Request for approval
              │         - Completion claims
              │         - Error reports
              │
              └───────────────────────────────────────────────────────► Back to Human
```

### Unsafe Control Actions for Agent Supervision

Applying the four UCA types to human supervision of agents:

#### 1. Not Providing Control Action (When Should)

| UCA | Hazard | Example Scenario |
|-----|--------|------------------|
| Human doesn't intervene when agent is failing | Agent continues making incorrect changes | Agent in loop, producing garbage, human not watching |
| Human doesn't correct agent's misunderstanding | Agent proceeds with wrong interpretation | Agent asks clarifying question, human doesn't answer |
| Human doesn't stop agent when scope exceeded | Agent modifies unintended parts of system | Agent "helpfully" refactors beyond task |
| Human doesn't provide required information | Agent guesses incorrectly | Agent needs context about system constraints |

#### 2. Providing Control Action (When Shouldn't)

| UCA | Hazard | Example Scenario |
|-----|--------|------------------|
| Human interrupts agent during critical operation | Operation left in inconsistent state | Stop command during database migration |
| Human provides contradictory instructions | Agent confused, takes wrong action | "Make it faster but don't change anything" |
| Human overrides correct agent decision | Agent forced to take wrong action | Human "corrects" agent that was actually right |
| Human micromanages routine task | Delays, introduces errors, wastes human time | Approving every trivial change |

#### 3. Control Action Too Early/Late/Wrong Order

| UCA | Hazard | Example Scenario |
|-----|--------|------------------|
| Human provides approval before verification | Incorrect output accepted | Rubber-stamping without review |
| Human intervenes after damage done | Intervention too late to prevent harm | Noticing error after deployment |
| Human gives instructions before context | Agent misunderstands | "Fix the bug" before explaining which bug |
| Human reviews wrong phase first | Misses architectural problems | Reviews code before reviewing design |

#### 4. Control Action Stopped Too Soon/Applied Too Long

| UCA | Hazard | Example Scenario |
|-----|--------|------------------|
| Human stops monitoring before task complete | Agent failure undetected | Assuming agent will finish correctly |
| Human maintains tight control beyond necessary | Wastes human time, slows agent | Micromanaging competent agent on familiar task |
| Human withdraws oversight before trust established | Premature autonomy, undetected failures | "Agent seemed to work once, let it run unsupervised" |
| Human continues intervening after agent capable | Impedes agent effectiveness | Not allowing agent to develop competence |

### What's the Agent's Process Model?

The agent's process model is its understanding of:

| Component | What Agent Believes | How It Can Be Wrong |
|-----------|--------------------|--------------------|
| **Task requirements** | What "done" looks like | Misinterpreted instructions |
| **Codebase state** | How the system currently works | Outdated understanding, wrong assumptions |
| **Effect of actions** | What will happen when agent acts | Unexpected side effects, wrong predictions |
| **Constraints** | What is allowed/forbidden | Missing constraints, wrong priorities |
| **Human expectations** | What human wants | Misaligned goals, different implicit assumptions |

### How Inadequate Agent Process Models Cause Failures

| Process Model Flaw | Resulting Failure | STPA Category |
|-------------------|-------------------|---------------|
| Agent thinks task is X when it's Y | Agent solves wrong problem | Inadequate process model |
| Agent doesn't know about dependency | Agent breaks dependent system | Incomplete model |
| Agent assumes codebase convention | Agent violates actual convention | Invalid assumptions |
| Agent's context outdated | Agent uses stale information | Model not updated |
| Agent misinterprets human feedback | Agent makes wrong correction | Feedback misinterpreted |

### Feedback Loops in Agent Systems

#### Agent-to-Codebase Feedback

| Feedback | Purpose | Failure Mode |
|----------|---------|--------------|
| Build results | Did code compile? | Only catches syntax errors |
| Test results | Does code work? | Tests may be incomplete |
| Linter output | Style conformance | Misses semantic issues |
| Error messages | What went wrong? | May be misleading |

#### Agent-to-Human Feedback

| Feedback | Purpose | Failure Mode |
|----------|---------|--------------|
| Progress reports | Human tracks state | Agent may misrepresent |
| Completion claims | Task done? | Agent thinks done when not |
| Error reports | Human can intervene | Agent may not recognize errors |
| Questions | Get missing information | Agent may not know to ask |

#### Human-to-Agent Feedback

| Feedback | Purpose | Failure Mode |
|----------|---------|--------------|
| Approval/rejection | Accept/reject output | Human may rubber-stamp |
| Corrections | Fix agent errors | May introduce new errors |
| Additional context | Improve agent model | May be misinterpreted |
| Guidance | Steer agent direction | May be too vague |

### Identifying Agent Loss Scenarios

Using STPA structure to enumerate why agent supervision might fail:

#### Why Human Might Not Intervene When Should

1. **Inadequate process model**
   - Human doesn't know agent is struggling
   - Human thinks agent is more capable than it is
   - Human's model of task state is outdated

2. **Inadequate control algorithm**
   - Human doesn't have clear criteria for intervention
   - Human's intervention rules don't cover this case
   - Human's response is too slow

3. **Missing feedback**
   - Agent doesn't report problems
   - Monitoring tools don't show relevant information
   - Feedback is delayed

4. **Conflicting demands**
   - Human attention on other tasks
   - Organizational pressure to not intervene
   - Trust-building exercise overrides safety

#### Why Agent Might Take Unsafe Action

1. **Inadequate process model (agent)**
   - Agent misunderstands requirements
   - Agent's model of codebase is wrong
   - Agent doesn't know about constraints

2. **Inadequate control algorithm (agent)**
   - Agent's decision-making is flawed
   - Agent doesn't recognize it should stop and ask
   - Agent overconfident in wrong approach

3. **Missing feedback (to agent)**
   - Build passes but code is wrong
   - Tests don't cover the issue
   - No feedback on unintended side effects

4. **Communication failures**
   - Instructions were ambiguous
   - Agent asked but answer was unclear
   - Context was incomplete

## Practical Implications

### Designing Better Control Structures

| Principle | Implementation |
|-----------|----------------|
| **Explicit process models** | Document what agent believes about task; human reviews before execution |
| **Feedback at every level** | Don't just check end result; check intermediate states |
| **Clear control algorithms** | Define when human intervenes, don't leave to judgment |
| **Model updates** | Ensure agent and human models update as task progresses |
| **Coordination** | If multiple controllers, ensure consistent models |

### UCA-Based Supervision Checklist

Before assigning a task, analyze potential UCAs:

1. **What could go wrong if I don't intervene when I should?**
   - List scenarios where non-intervention causes hazard
   - For each: How will I know to intervene? What feedback will tell me?

2. **What could go wrong if I intervene when I shouldn't?**
   - List scenarios where intervention causes hazard
   - For each: How will I know NOT to intervene?

3. **What could go wrong with timing?**
   - When is intervention too early? Too late?
   - What determines right timing?

4. **What could go wrong with duration?**
   - How will I know when to stop oversight?
   - How will I know if I've stopped too soon?

### Process Model Alignment Protocol

Ensure agent and human have consistent process models:

1. **Explicit task model** - Agent states its understanding; human confirms
2. **Explicit constraint model** - Agent states what it believes is forbidden; human corrects
3. **Explicit state model** - Agent reports current understanding of system state
4. **Model update triggers** - Define when models must be re-synchronized

### Feedback Design Principles

Design feedback loops to catch process model failures:

| Feedback Type | Catches | Example |
|---------------|---------|---------|
| **State feedback** | Current state misunderstanding | "What files will you modify?" |
| **Intent feedback** | Goal misunderstanding | "What are you trying to achieve?" |
| **Prediction feedback** | Effect misunderstanding | "What do you expect to happen?" |
| **Constraint feedback** | Constraint misunderstanding | "What are you not allowed to do?" |

## Key Insight

**Accidents happen not because components fail, but because the CONTROL of the system is inadequate.**

For agent systems, this means:

1. **Agent reliability is necessary but not sufficient.** A perfectly capable agent can still cause accidents if the control structure is inadequate.

2. **Supervision is a control problem.** The question is not "Is the agent good?" but "Is the control loop functioning correctly?"

3. **Process models are the weak point.** Most agent failures trace to misalignment between what the agent believes, what the human believes, and reality.

4. **Feedback must update process models.** If feedback doesn't cause model updates, the control loop is broken.

5. **Four ways control fails.** For any control action, check: not providing, providing, timing, duration.

The STAMP/STPA framework transforms agent supervision from "watch the agent" to "engineer the control structure." It provides systematic tools to identify where control can fail and what feedback is needed to prevent it.

## Connections to Other Models

| Model | Relationship to STAMP/STPA |
|-------|---------------------------|
| **Ashby's Law of Requisite Variety** | Supervision variety must match agent variety - STAMP shows where variety is needed in the control structure |
| **OODA Loop** | OODA is a control loop; STAMP provides structure to analyze OODA failures |
| **Cynefin** | Domain determines appropriate control structure; Complex domain needs different feedback loops than Clear |
| **Principal-Agent Theory** | Information asymmetry is a process model problem - agent knows more than principal |
| **Trust Development** | Trust = confidence that process models are aligned and control will be adequate |

## Open Questions

1. **Multi-agent control structures:** When agents supervise agents, how do we ensure aligned process models?

2. **Autonomous model updates:** How can agents safely update their own process models without human confirmation?

3. **Process model observability:** How do we make the agent's process model visible to the human?

4. **UCA evolution:** Do new UCA types emerge as agents become more capable?

5. **Feedback latency:** What's the maximum tolerable delay in feedback loops before control breaks down?

6. **Hierarchical process models:** How do process model errors propagate through hierarchical control structures?

## Systems to Build

- [ ] **Control structure modeler:** Tool to visualize agent supervision as control structures
- [ ] **UCA generator:** Systematic enumeration of unsafe control actions for common agent tasks
- [ ] **Process model diff:** Compare agent's stated understanding with human's expectations
- [ ] **Feedback adequacy checker:** Analyze whether feedback is sufficient to update process models
- [ ] **Causal scenario library:** Common loss scenarios for agent supervision

## References

- Leveson, N. G. (2011). *Engineering a Safer World: Systems Thinking Applied to Safety.* MIT Press. [Available as free PDF](https://library.oapen.org/handle/20.500.12657/26043)
- Leveson, N. G. (2004). "A New Accident Model for Engineering Safer Systems." *Safety Science.*
- STPA Handbook (MIT)
- [STAMP/STPA informed characterization of Factors Leading to Loss of Control in AI Systems](https://arxiv.org/html/2512.17600)
- [Systematic Hazard Analysis for Frontier AI using STPA](https://arxiv.org/html/2506.01782)

## Status

**Phase:** Deep research complete. STAMP/STPA provides a rigorous framework for analyzing agent supervision as a control problem. The key insight is that accidents result from inadequate control, not component failures. For agents, this means focusing on control structure design, process model alignment, and systematic feedback - not just agent capability.
