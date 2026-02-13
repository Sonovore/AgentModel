# PACE Plan: Military Communication Doctrine for Resilient Systems

## Executive Summary

PACE (Primary, Alternate, Contingency, Emergency) is a communication planning methodology developed by the U.S. military to ensure reliable communications regardless of circumstances. This document examines PACE doctrine at multiple levels of depth, exploring not just the surface-level concept of "backup communication methods" but the deeper principles of trigger conditions, pre-briefed procedures, lost communications protocols, and failure modes. The goal is to extract transferable principles for designing resilient AI agent communication systems.

---

## 1. Doctrinal Definition and Origins

### What is PACE?

PACE is a methodology used to build communication plans that establish redundancy and resilience. The acronym stands for:

- **Primary**: The preferred, most effective method of communication under normal conditions
- **Alternate**: A common but less-optimal backup method, often monitored concurrently with primary
- **Contingency**: A method that works but is slower, more expensive, or less convenient
- **Emergency**: The last-resort option when all else fails; typically the most time-consuming and inconvenient

The U.S. military developed PACE to ensure units can maintain mission command even when primary communication systems fail. As stated in Army doctrine, a PACE plan "designates the order in which an element will move through available communications systems until contact can be established with the desired distant element."

### Core Principle: Independence of Methods

A foundational requirement of PACE is that each method must be **completely separate and independent** of the other systems. Failure of any component or process in one method should not affect any other means to communicate.

For example, listing email, Facebook, and texting as three levels of a PACE plan provides no value if they all depend on the same device and cellular data connection. The same communications path or method should never appear more than once in a PACE plan.

### Relationship to Mission Command

PACE planning exists within the broader context of **mission command** doctrine, which emphasizes:

- Clear commander's intent and desired end state
- Decentralized execution within defined constraints
- Subordinate initiative and autonomous action when communications are disrupted

As Joint Publication 3-0 states: "The commander's intent is a clear and concise expression of the purpose of the operation and the desired military end state that supports mission command, provides focus to the staff, and helps subordinate and supporting commanders act to achieve the commander's desired results without further orders, even when the operation does not unfold as planned."

This is critical: PACE planning assumes that at some point, all communication methods may fail. The doctrine is not just about having backups; it is about enabling coherent action in the absence of communication.

---

## 2. Criteria for Selecting Methods at Each Level

### The Three Selection Factors

Determining which communication method goes in each slot (P/A/C/E) requires balancing three factors:

1. **Security**: How secure is the communication method against interception or compromise?
2. **Performance**: How well does the method perform in the operational environment?
3. **Reliability and Convenience**: How dependable and easy to use is the method?

### Characteristics by Level

| Level | Typical Characteristics | Military Examples |
|-------|------------------------|-------------------|
| **Primary** | Best, most reliable, fastest, highest bandwidth | UHF tactical radio |
| **Alternate** | Effective but less convenient; may be monitored alongside primary | Satellite radio, encrypted cell phones |
| **Contingency** | Slower, more expensive, less convenient; works when P and A fail | HF long-range radio |
| **Emergency** | Most time-consuming, costly, inconvenient; absolute last resort | Physical messenger (runner), light signals, bullhorns |

### Additional Planning Factors

Beyond the three primary factors, comprehensive PACE planning must consider:

- **Users**: Who needs to communicate with whom?
- **Technology**: What systems are available and interoperable?
- **Time**: How quickly must messages be delivered?
- **Quality**: What fidelity/bandwidth is required?
- **Training**: Can all operators use all systems?
- **Cost**: What resources are available?

### The Nesting Requirement

Leaders must "nest" their PACE plans with higher commands and complement adjacent and subordinate units. Nesting means more than ensuring each echelon has the same equipment; it means ensuring each echelon can transmit information freely and effectively up, down, and across the command structure.

---

## 3. Trigger Conditions for Transitioning Between Levels

### The Fundamental Challenge

One of the most difficult aspects of PACE implementation is understanding when to transition from one level to the next. As practitioners note: "This transition between the sender and receiver of information must occur simultaneously, without the benefit of being choreographed by some communications means."

This creates a paradox: you cannot use the failed communication method to coordinate the switch to a new method.

### Types of Triggers

#### Condition-Based Triggers

These triggers activate based on observable system states:

- **Communication failure**: Primary system stops working
- **Degradation**: Signal quality falls below acceptable threshold
- **Security compromise**: Suspicion that communications are intercepted
- **Electronic warfare**: Detection of jamming or interference
- **Infrastructure damage**: Physical destruction of communication nodes

#### Time-Based Triggers

These triggers activate based on elapsed time:

- **Scheduled check-in windows**: "If no contact by 1400, switch to Alternate"
- **Monitoring schedules**: "Monitor alternate frequency at 15-minute intervals on the hour"
- **Duration thresholds**: "If no response within 60 seconds, proceed to next level"

Aviation provides concrete examples of time-based triggers:
- 60 seconds without transmission while being vectored to final approach
- 15 seconds without transmission on ASR final approach
- 5 seconds without transmission on PAR final approach

#### Latency-Based Triggers

Modern operations often involve data transmission where timing matters:

- Establishing what data is important to the mission
- Determining how much time can pass before delivery
- Defining acceptable latency for each category of information

This informs which PACE level is appropriate for different types of communication.

### The Automation Question

Historically, transitioning between PACE levels required human intervention, "resulting in unnecessary downtime and stress on end-users in emergency situations." Modern systems increasingly explore automatic network failover to simplify PACE implementation and enhance reliability by eliminating human error during high-pressure moments.

However, automatic failover introduces its own risks: false positives, unnecessary transitions, and potential security implications of switching to less secure backup channels.

---

## 4. Pre-Briefed Procedures: The "And-Then" Problem

### Why Pre-Briefing Matters

Since switching to the next PACE level is not intuitive and cannot be coordinated via the failed communication method, it must be planned and practiced in advance. All key stakeholders must know:

- What to do at each level
- Under what conditions to change methods
- How to recognize that others have changed methods

As doctrine emphasizes: "This is why the education, training, and exercise piece is so important. Emergency communications ecosystem participants have to understand that the decision to transition to other parts of the plan may have to occur in a vacuum."

### Commander's Intent as the Ultimate Pre-Brief

Mission command doctrine provides the answer to "what do we do when we can't communicate at all?" The commander's intent serves as the ultimate pre-briefed instruction, enabling subordinates to:

- Understand the purpose of the operation
- Know the desired end state
- Act within defined boundaries
- Make autonomous decisions that align with mission objectives

As Prussian doctrine (the origin of mission command) stated: "If execution of an order was rendered impossible, an officer should seek to act in line with the intention behind it."

### Branch Plans and Sequels

Military planning uses specific constructs for pre-briefed contingencies:

- **Branch Plan**: A contingency built into the base plan to exploit success or deal with unexpected enemy action; typically discovered during wargaming
- **Sequel**: A subsequent operation based on possible outcomes of the current operation

Both should have explicit **execution criteria**, reviewed and updated based on assessment of current operations. Standard terminology includes:

- **"On Order" (O/O)**: Execute only when directed by commander at a specific time
- **"Be Prepared To" (BPT)**: May need to execute; prepare in advance for rapid execution

### Default Actions in Communications

Aviation doctrine provides clear examples of pre-briefed default actions for lost communications:

The "AVEenue of FAME" mnemonic for route:
- **A**ssigned: Fly the route per last ATC clearance
- **V**ectored: Fly direct from failure point to specified fix
- **E**xpected: Fly the route ATC advised you to expect
- **F**iled: Fly the route on your flight plan

For altitude, the rule is to fly the **highest** of:
- Minimum en route altitude (MEA)
- Expected altitude
- Assigned altitude

These deterministic rules ensure that even without communication, all parties can predict behavior.

---

## 5. Lost Communications Procedures

### The DDIL Environment

Modern military doctrine uses the term **DDIL** (Denied, Degraded, Intermittent, Limited) to describe communication challenges:

- **Denied**: Complete loss of connectivity (physical separation, jamming, infrastructure damage)
- **Degraded**: Reduced quality (slower transfer, lower signal quality, increased errors)
- **Intermittent**: Sporadic availability with frequent, unpredictable disruptions
- **Limited**: Constrained bandwidth, range, or data transfer rates

In DDIL environments, communications may fail at the most critical moments. PACE planning is the primary framework for building resilience against DDIL conditions.

### Operating Without Communication

When all PACE levels fail, doctrine relies on:

1. **Commander's Intent**: The pre-briefed purpose and end state that enables autonomous action
2. **Standard Operating Procedures (SOPs)**: Default behaviors that require no coordination
3. **Pre-formatted Reports**: Structured communication templates that minimize transmission requirements
4. **Nodal Operations**: Self-contained units able to operate largely on their own with only sporadic contact to command

As one expert noted: "We should take it as a given that in places, our communications are going to break and fail." This has driven development of decentralized approaches where units operate semi-independently across battlefield domains.

### Historical Example: Bravo Two Zero

The SAS patrol depicted in the Bravo Two Zero account demonstrates catastrophic PACE failure:

- The patrol rapidly moved through all PACE levels
- Even the emergency system proved ineffective
- The outcome was an isolated patrol having to escape and evade through hostile territory

This case study illustrates that PACE planning, while essential, cannot guarantee communications will succeed. The ultimate fallback is the ability to operate coherently without any external coordination.

---

## 6. Time-Based vs. Condition-Based Triggers: A Deeper Analysis

### Advantages of Time-Based Triggers

- **Predictability**: All parties know when to check alternate channels
- **No detection required**: Don't need to detect failure; just check at scheduled times
- **Synchronized transitions**: Both sender and receiver switch simultaneously
- **Works in complete denial**: Even total communication loss doesn't prevent the switch

### Disadvantages of Time-Based Triggers

- **Latency**: May wait unnecessarily when faster response is possible
- **Rigidity**: Cannot adapt to rapidly changing conditions
- **Enemy exploitation**: Predictable patterns may be vulnerable to adversary action

### Advantages of Condition-Based Triggers

- **Responsiveness**: Switch immediately when problems are detected
- **Efficiency**: Don't waste time on scheduled checks if primary is working
- **Adaptability**: Can respond to specific failure modes appropriately

### Disadvantages of Condition-Based Triggers

- **Synchronization problem**: Sender and receiver may detect failure at different times
- **Detection reliability**: May not recognize degradation until too late
- **Coordination paradox**: How do you coordinate the switch using a failed channel?

### Hybrid Approaches

Effective PACE implementations often combine both:

- Condition-based triggers for rapid response to obvious failures
- Time-based windows for systematic checks when condition-based detection is unreliable
- Scheduled monitoring of alternate frequencies even while primary is operational

---

## 7. Failure Modes in PACE Planning

### Design-Level Failures

#### Inadequate Primary/Alternate Systems

"If the Primary and Alternate systems at hand are not designed for the particular purpose or indeed not fit for the requirement then the communications plan starts on a back foot and is open to failure from the outset."

#### Underinvestment in Contingency/Emergency

There is often "a lack of investment into Contingency and Emergency systems across a multitude of international organizations." These are frequently "hopeful placeholders" rather than robust backups. If Primary and Alternate fail (as they often do), weak C/E solutions "won't just limit operational effectiveness, they could expose teams to catastrophic consequences."

#### Technology Obsolescence

"The time it takes to bring a new Primary or Alternate system into service means most of what's deployed today is already behind the curve." Systems designed for 15-20 year lifecycles often enter service already facing threats they weren't designed for.

### Operational Failures

#### Capability Degradation on Transition

When switching systems within PACE, users experience "some loss in capability, whether that is quality of voice and/or reduction in bandwidth." As complexity increases, message throughput decreases, requiring more concise, formal, and structured communication.

#### Training Gaps

"The individuals who will operate the Alternate, Contingency, and Emergency means of communications will need regular training and experiences using these systems." Without this, operators may not know how to use backup systems when needed.

#### Synchronization Failures

The transition "must occur simultaneously, without the benefit of being choreographed by some communications means." If sender switches but receiver doesn't, communication remains broken despite available channels.

### Environmental Failures

#### Electronic Warfare

"Failure of communications can be driven by many factors but one... is denial or disruption of service through Electronic Warfare (EW)." Many primary systems were developed when EW threats were minimal, making them vulnerable to modern adversary capabilities.

#### Single-Point-of-Failure in Backup Channels

Switching from S-band to another S-band frequency when being jammed is less effective than changing to C-band. Backup channels must genuinely differ in their vulnerability profile.

---

## 8. Application to AI Agent Communication Resilience

### The Agent Communication Problem

AI agents face communication challenges analogous to military operations:

- **API failures**: Services become unavailable
- **Rate limiting**: Throughput is throttled
- **Latency spikes**: Response times become unacceptable
- **Context window exhaustion**: Information capacity is exceeded
- **Model degradation**: Output quality deteriorates under load

Like military units, agents need to maintain operational capability even when communication systems fail.

### Mapping PACE to Agent Systems

| Military Level | Agent Equivalent | Example |
|----------------|------------------|---------|
| **Primary** | Preferred API/service | Claude API via direct connection |
| **Alternate** | Backup API endpoint | Secondary region, alternative model |
| **Contingency** | Degraded operation mode | Cached responses, reduced capability |
| **Emergency** | Minimal viable function | Logging only, safe state, human escalation |

### Agent-Specific Failure Modes

Research on agentic AI systems identifies failure patterns that map to PACE concerns:

- **Planner starvation**: Endless reasoning loops without resolution
- **Memory entrenchment**: Poisoned data persisting across sessions
- **Behavioral drift**: Gradual deviation from expected logic
- **Systemic collapse**: Cascading breakdown across perception, memory, planning, tools, and output

### Graceful Degradation for Agents

Robust AI systems implement graceful degradation rather than binary success/failure:

> "Rather than failing entirely, the system should automatically route to alternative tools that provide similar functionality, even if they're less sophisticated."

A tiered degradation strategy might include:
1. Primary agent with full reasoning and planning capabilities
2. Fallback to simpler, faster, more robust model
3. Fallback to rule-based systems
4. Fallback to logging and human escalation

### The Commander's Intent Analog

For agents, the analog to commander's intent is clear **goal specification** and **constraints**:

- What is the agent trying to accomplish?
- What boundaries must it respect?
- What decisions can it make autonomously?
- What should it do if it cannot communicate for guidance?

Without this, an agent that loses communication with its orchestrator has no basis for continued action.

---

## 9. Designing Fallback Protocols for Agents

### Pre-Briefed Default Actions

Like military pre-briefed procedures, agents need explicit default behaviors:

```
IF cannot reach primary orchestrator:
  THEN attempt alternate endpoint
  IF alternate fails after N retries:
    THEN enter contingency mode (reduced capability)
    IF contingency unavailable:
      THEN enter emergency mode (safe state, log everything, await human)
```

### Time-Based vs. Condition-Based for Agents

**Condition-based triggers** (agent context):
- API returns error code
- Response latency exceeds threshold
- Output quality metric falls below acceptable level
- Resource utilization exceeds limits

**Time-based triggers** (agent context):
- Check orchestrator heartbeat every N seconds
- If no response within timeout, escalate
- Scheduled synchronization points for long-running tasks
- Periodic health checks even when operations appear normal

### The Synchronization Problem for Agents

Like military units, agents face the challenge of coordinated transitions:

- If agent A switches to backup channel but agent B doesn't know, coordination breaks
- Pre-agreed fallback rendezvous points (like alternate frequencies) are needed
- Shared state or consensus mechanisms may be required for multi-agent systems

### Human-in-the-Loop as Emergency Level

For agent systems, human escalation often serves as the Emergency level:

- When all automated fallbacks fail
- When the situation requires judgment beyond agent capabilities
- When the cost of autonomous action exceeds acceptable risk

This maps directly to mission command's emphasis on human supervision during the trust-building phase.

---

## 10. Key Principles for Agent System Design

### From Military Doctrine

1. **Independence of channels**: Each fallback must fail independently; no shared dependencies
2. **Pre-briefed triggers**: Define when to transition before the need arises
3. **Training on all levels**: Test backup systems regularly, not just primary
4. **Intent-based autonomy**: Enable coherent action even without communication
5. **Synchronized transitions**: Both parties must know when to switch

### For Agent Systems

1. **Redundant APIs and models**: Don't depend on single provider or endpoint
2. **Explicit fallback policies**: Document and implement graceful degradation
3. **Regular failover testing**: Exercise backup paths before they're needed
4. **Clear goal specification**: Enable autonomous progress toward objectives
5. **Coordination protocols**: Define how agents recognize and respond to failures

### The Ultimate Lesson

PACE planning is not about having backup communication methods. It is about maintaining mission effectiveness across the full spectrum of communication capability, from perfect to completely absent. The same principle applies to agent systems: design for the entire range of conditions, not just the happy path.

---

## References and Sources

### Military Doctrine and PACE Methodology
- [PACE (communication methodology) - Wikipedia](https://en.wikipedia.org/wiki/PACE_(communication_methodology))
- [US Army Infantry Magazine - A Short Note on PACE Plans](https://www.benning.army.mil/infantry/magazine/issues/2013/Jul-Sep/pdfs/Ryan.pdf)
- [CISA - Leveraging the PACE Plan into the Emergency Communications Ecosystem](https://www.cisa.gov/resources-tools/resources/leveraging-pace-plan-emergency-communications-ecosystem)
- [QinetiQ - Building a PACE plan that holds](https://www.qinetiq.com/en/blogs/how-to-build-a-pace-plan-that-works)
- [QinetiQ - Why PACE Implementations Fail to Deliver Assured Battlefield Communications](https://www.qinetiq.com/en/blogs/why-pace-implementations-fail-to-deliver-assured-battlefield-communications)
- [Systematic - Optimizing PACE Military Communications for Mission Success](https://systematic.com/int/industries/defence/products/deep-dives/pace-communications/)

### Mission Command and Commander's Intent
- [Mission command - Wikipedia](https://en.wikipedia.org/wiki/Mission_command)
- [US Army - Mission command requires sharp commander's intent](https://www.army.mil/article/215297/mission_command_requires_sharp_commanders_intent)
- [The Field Grade Leader - The Commander's Intent in Mission Command](https://fieldgradeleader.themilitaryleader.com/cdr-intent/)

### DDIL and Degraded Communications
- [ExecutiveBiz - DDIL: How DOD Seeks to Operate in Low Bandwidth Environments](https://www.executivebiz.com/articles/ddil-dod-cyber-cloud-cjadc2-low-bandwidth)
- [REDCOM - Communications Challenges in DIL Environments](https://www.redcom.com/dil-environments/)
- [C4ISRNet - Military must train to fight when communications break down](https://www.c4isrnet.com/battlefield-tech/2023/04/26/experts-military-must-train-to-fight-through-communications-breakdown/)

### AI Agent Resilience and Failure Modes
- [AWS Architecture Blog - Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents/)
- [Cloud Security Alliance - Cognitive Degradation Resilience for Agentic AI](https://cloudsecurityalliance.org/blog/2025/11/10/introducing-cognitive-degradation-resilience-cdr-a-framework-for-safeguarding-agentic-ai-systems-from-systemic-collapse)
- [Concentrix - 12 Failure Patterns of Agentic AI Systems](https://www.concentrix.com/insights/blog/12-failure-patterns-of-agentic-ai-systems/)
- [GoCodeo - Error Recovery and Fallback Strategies in AI Agent Development](https://www.gocodeo.com/post/error-recovery-and-fallback-strategies-in-ai-agent-development)
- [Galileo - A Guide to AI Agent Reliability for Mission Critical Systems](https://galileo.ai/blog/ai-agent-reliability-strategies)

### Lost Communications Procedures
- [SKYbrary - Loss of Communication](https://skybrary.aero/articles/loss-communication)
- [Life is a Special Operation - What is a PACE Plan?](https://lifeisaspecialoperation.com/pace/)
- [Domestic Preparedness - PACEing a Communications Resilience Plan](https://domesticpreparedness.com/communication-interoperability/paceing-a-communications-resilience-plan/)
