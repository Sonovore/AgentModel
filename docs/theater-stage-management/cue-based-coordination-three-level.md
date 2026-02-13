# Cue-Based Coordination: Three-Level Explanation

## Level 1: Ages 5-10

### The "Ready, Set, Go!" Game

Have you ever played "Ready, Set, Go!" before running a race? That's exactly how theaters work when they put on shows!

**The Problem: Too Many Things at Once**

Imagine you're putting on a puppet show for your family. You need to:
- Turn on the lights
- Play the music
- Move the puppets
- Make sound effects

Now imagine doing ALL of those at the EXACT same time! It's really hard!

In real theaters, there are even MORE things happening:
- Big lights changing colors
- Sound effects like thunder
- Giant scenery moving
- Curtains opening and closing
- And many more!

**The Stage Manager's Secret**

The Stage Manager is like the conductor of an orchestra. They don't play any instruments—they just tell everyone WHEN to play!

They use special words, just like "Ready, Set, Go!":

**"Warning!"** = "Get ready, something is coming soon!"
(Like when mom says "We're leaving in 5 minutes!")

**"Standby!"** = "It's almost time, be ready RIGHT NOW!"
(Like when mom says "Put your shoes on, we're going!")

**"GO!"** = "Do it NOW!"
(Like when mom says "Let's go!")

**The Special Rule**

Here's a super important rule in theaters: Only ONE person—the Stage Manager—can say the word "GO."

Why? Because if someone else said "GO" by accident, people might do their jobs at the wrong time! Imagine if the lights turned off when they should stay on. Oops!

So if you work in a theater and you're on the special walkie-talkie, you NEVER say "go." You say things like "start" or "begin" instead.

**Everyone Gets Ready Together**

Let's say the Stage Manager needs the lights to change AND the music to play at the same time. Here's what they do:

1. "Warning: Lights and Sound!" (Both helpers start getting ready)
2. "Standby: Lights and Sound!" (Both helpers have their hands on buttons)
3. "Lights and Sound... GO!" (Both helpers push their buttons at the exact same time!)

And just like magic, everything happens together!

**The Big Lesson**

When lots of people need to do things at exactly the right time, having special signals like "Warning," "Standby," and "Go" helps everyone be ready without being confused.

---

## Level 2: High School Graduate

### How Theater Coordinates Hundreds of Technical Events in Real-Time

When you watch a professional theater production, you're witnessing an intricate dance of technical elements: lights fade and shift color, sound effects punctuate moments, scenery flies in and out, projections appear and disappear. A Broadway musical might have 400+ technical cues—discrete moments where something changes. And these must happen with split-second precision, synchronized to live performers whose timing varies slightly each night.

How does this coordination happen? Through a system called cue-based coordination—a multi-phase commitment protocol refined over a century of live performance.

**What is a Cue?**

A cue is a signal for an action to take place. But that simple definition understates the sophistication of the system. A theatrical cue consists of three parts:

1. **The preface**: What element is changing (e.g., "Lights 47")
2. **The action**: The trigger word ("go")
3. **The trigger**: What observable event drives the call (a line of dialogue, a music note, an actor's movement)

The stage manager doesn't execute the technical work—they coordinate specialists who do. The stage manager watches the performance, and at the precise moment a cue should fire, they call "Lights 47... go." The lighting operator immediately executes the preprogrammed effect.

**The Three-Phase Protocol**

Cues don't just appear suddenly. They follow a three-phase commitment protocol:

**Warning (60 seconds before)**
"Warning, Lights 47, Sound 12."

This alerts operators that these cues are approaching. Operators can:
- Finish other tasks
- Position themselves at their consoles
- Verify their equipment is ready
- Mentally prepare for the upcoming action

For mechanical cues (scenery moving, equipment rigging), this warning time is essential—crew members need to physically get into position.

**Standby (10-30 seconds before)**
"Standby, Lights 47, Sound 12."

This is the commitment phase. Operators must:
- Be in position with hands on controls
- Give full attention to the upcoming cue
- Acknowledge they're ready ("Standing by" or "Copy")

The standby is the "trigger armed" state. Everything is ready; the operator is waiting for only one word.

**Go (execution moment)**
"Lights 47... go."

Immediate execution. No hesitation, no decision-making—pure reflex response.

**Why the Syntax Matters**

Notice the word order: "Lights 47... go." The department and cue number come FIRST. The word "go" comes LAST.

This is a safety protocol. If "go" came first ("Go, Lights 47!"), an operator hearing garbled audio might execute on just "go" before hearing which cue was called. By putting "go" last, operators hear the complete identification before the trigger word.

Similarly, standbys begin with "standby": "Standby, Lights 47." This prevents anyone from accidentally triggering a cue by hearing "Lights 47" out of context.

**Acknowledgment: Closing the Loop**

Communication is bidirectional. After standby, operators acknowledge:
- "Standing by, Lights"
- "Sound copy"
- "Rail standing by"

This confirms the operator heard the standby and is ready. If the stage manager doesn't hear acknowledgment, they know something is wrong—perhaps the operator didn't hear, or they're not ready.

After "go," acknowledgment is usually unnecessary (operators are executing), except for cues whose execution isn't visible to the stage manager. For a long fade or an effect the SM can't see, operators report: "Lights 47 taken" or "Running."

**Self-Cues and Visual Cues**

Not every cue is called by the stage manager. Some operators "self-cue" based on what they observe:

**Followspot operators** track performers with spotlights. They don't take individual cues from the stage manager because performer movement varies nightly. Instead, they have a "plot sheet" specifying which performer to track, when to pick them up, what color and intensity to use. They execute autonomously while staying on the headset network for coordination.

**Visual cues** trigger based on observation. When an actor flips a light switch, the lighting operator triggers the effect based on what they see, not what the stage manager calls. This reduces communication latency when split-second timing matters.

The decision framework: **Central cues when timing is predetermined and must synchronize. Autonomous cues when reactive and the operator observes better than the coordinator.**

**Cue Numbering**

Cues use hierarchical numbering to accommodate revision:
- Lights: LQ 1, LQ 2, LQ 3...
- Sound: SQ 1, SQ 2, SQ 3...

Or universal numbering: Q1, Q2, Q3...

The key: leave gaps for insertion. Initial cues might be numbered 10, 20, 30... so when new cues are discovered during tech rehearsal, they become 15, 17, 25 without renumbering everything else. Or use decimals: 47.5 between 47 and 48.

Why does this matter? Because changing cue numbers requires updating:
- The stage manager's calling script
- Every operator's cue sheet
- Automation programming
- Rehearsal notes referencing cue numbers

Gaps in numbering provide insertion points without disruption.

**Failure and Recovery**

When cues go wrong:

**Missed cue**: The stage manager stays calm, assesses impact, and decides whether to skip to the next cue or attempt recovery.

**Early execution**: Usually can't be undone. Subsequent cues adapt to compensate.

**Communication failure**: Operators are trained to continue autonomously. Followspot operators already self-cue. Sound operators often run from their own script. The show continues.

**Post-show**: Debrief, document what went wrong, update the calling script, rehearse the correction.

The governing principle: "Stay calm, deal with it, move on." The show must continue.

**Why This Matters Beyond Theater**

Cue-based coordination embodies several principles applicable far beyond the stage:

1. **Multi-phase commitment**: Warning → Standby → Go separates preparation from execution
2. **Clear protocols**: Reserved words, specific syntax, acknowledgment requirements
3. **Autonomous vs. orchestrated**: Central coordination for predetermined, local execution for reactive
4. **Explicit dependencies**: Documented triggers and sequences
5. **Graceful degradation**: Continue despite failures; fix afterward

These same principles apply anywhere multiple agents must coordinate precise actions under time pressure—from software orchestration to emergency response to manufacturing.

---

## Level 3: Expert

### Cue-Based Coordination: A Commitment Protocol for Distributed Real-Time Systems

Theatrical cue-based coordination is frequently dismissed as simple "telling people what to do." This understanding misses the sophisticated distributed systems architecture that enables hundreds of precisely-timed state transitions across dozens of autonomous operators, with human performers introducing timing variability, all running continuously without the ability to pause, retry, or rollback.

Cue-based coordination is better understood as a **multi-phase commitment protocol for triggering autonomous execution in distributed real-time systems**—a protocol refined over a century of live performance to balance preparation time, execution precision, and autonomous operation.

**The Coordination Problem**

Theater presents a multi-agent coordination challenge:
- **Multiple autonomous operators**: Lighting, sound, fly rail, automation, followspots, performers—each operating independently
- **Precise timing requirements**: Cues must execute within fractions of a second of intended moments
- **Dependencies between actions**: One cue may depend on another's completion
- **No central executor**: The stage manager coordinates but doesn't perform the work
- **Real-time constraints**: Shows run continuously; there is no "pause and debug"
- **Variable timing**: Performer pacing varies performance-to-performance

This is isomorphic to multi-agent AI systems: autonomous agents, timing coordination, dependencies, central orchestration without central execution, continuous operation, and environmental variability.

**Why Not Central Execution?**

Modern technology enables central execution—automated show control systems could operate every light, sound effect, and motorized element from a single computer. Yet the cue-based model persists because:

**Cognitive load**: No single entity can monitor all information needed to execute all actions optimally. The stage manager watches the performance; they cannot simultaneously watch lighting levels, sound mixing, rigging positions, and performer locations.

**Domain expertise**: Technical operators understand their domains better than the coordinator. The lighting operator knows the feel of their board, the quirks of their fixtures, the micro-adjustments that make effects look right.

**Real-time adaptation**: Operators make adjustments invisible to the coordinator. The sound operator rides the mix as performers' vocal dynamics change. The followspot operator tracks a performer's ad-libbed movement.

**Failure resilience**: If communication fails, operators can continue autonomously. They have scripts, they can watch the performance, they can self-cue.

**Scalability**: Central execution doesn't scale. One coordinator calling 400+ cues to 20+ operators maintains tractable cognitive load. One executor performing 400+ actions across 20+ systems cannot.

The cue system achieves **coordination without centralized execution**—the stage manager provides timing signals; autonomous operators execute within their domains.

**The Three-Phase Protocol as Commitment Mechanism**

The warning/standby/go protocol is not merely polite advance notice—it's a multi-phase commitment mechanism:

**Warning Phase (t-60s): Resource Allocation**
- Operators allocate attention from other tasks
- Physical preparation begins (positioning, equipment staging)
- Mental preparation (rehearsing the upcoming action)
- Analogous to: Memory allocation, context loading, pre-warming caches

At warning, operators transition from "idle" to "preparing." They're not yet committed to execute, but resources are being allocated.

**Standby Phase (t-30s): Commitment**
- Final verification that resources are ready
- Psychological contract established
- Acknowledgment required (closes the communication loop)
- Analogous to: "Transaction ready to commit," prepared state

At standby, operators are committed. They've acknowledged readiness. The stage manager knows they're prepared. There's a contract: when "go" comes, execution will happen.

**Go Phase (t=0): Execution Trigger**
- Atomic trigger with no decision-making
- Immediate execution
- No acknowledgment expected (operators are executing)
- Analogous to: "Commit now," execution signal

The three phases separate **resource preparation**, **readiness confirmation**, and **execution triggering**—each with different timing requirements and failure modes.

**Protocol Syntax as Safety Mechanism**

The cue call syntax encodes safety:

**Standby syntax**: "Standby [element] [number]"
- "Standby" is a prefix, never a suffix
- Prevents accidental triggering from hearing cue number out of context
- Requires the reserved word first

**Go syntax**: "[Element] [number]... go"
- "Go" is a suffix, never a prefix
- Operators hear complete cue identification before trigger word
- The pause (represented by "...") separates identification from trigger
- If transmission is garbled, operators wait for clear identification

**Reserved word**: "Go" is reserved exclusively for execution triggers
- No other use of "go" is permitted on headsets
- Alternatives: "proceed," "continue," "start"
- This is a **reserved keyword** in the communication protocol

These syntactic constraints prevent entire categories of errors—premature execution, wrong cue execution, accidental triggering from casual speech.

**Orchestrated vs. Autonomous Execution**

The cue system distinguishes between centrally orchestrated and locally autonomous execution:

**Stage Manager-Called Cues (Orchestrated)**:
- Lighting state changes
- Sound playback triggers
- Fly rail movements
- Automation sequences
- Major scenic changes

These have **predetermined timing** and often require **multi-system synchronization**. The stage manager maintains the authoritative timeline.

**Self-Cues (Autonomous)**:
- Followspot tracking
- Some sound effects (actor-triggered)
- Practical effects (light switches)
- Certain projection elements

These are **reactive to environmental conditions** that the operator observes better than the coordinator.

**Hybrid (Autonomous within Orchestrated Context)**:
- Followspot operators don't take individual cues
- But their plot sheets synchronize to lighting cue numbers
- "At LQ 47, pick up actor entering stage left"
- Autonomous execution within orchestrator-defined coordination frame

The decision framework:
- **Central orchestration when**: Timing predetermined, multi-system sync required, coordinator can observe trigger as well as operator
- **Autonomous execution when**: Reactive to performer variation, operator has superior observability, communication latency would cause unacceptable delay

**Dependency and Sequencing Mechanisms**

Cues have explicit dependencies:

**Sequential Dependencies**:
- LQ 45 (fade to black, 3 seconds)
- SQ 12 (thunder, must wait for blackout)
- FLY 7 (fly in clouds, can start during fade)

The stage manager calls these in sequence, respecting timing dependencies.

**Auto-Follow (Choreographed Transitions)**:
Modern show control systems implement automatic sequencing:
- Cue 10 starts
- After 3 seconds, Cue 11 auto-triggers
- After 1 second, Cue 12 auto-triggers
- No manual "go" commands for each

Auto-follow chains allow complex sequences from a single "go," reducing stage manager cognitive load and improving timing precision.

**Cluster Cues (Synchronized Multi-System)**:
Complex moments require coordinated clusters:
- Actor opens door: Lights, sound, projection, followspots all change simultaneously

Calling pattern:
"Standby Lights 52 and 53, Sound 19 and 20"
[Acknowledgments]
"Lights 52, Sound 19... go"
[0.5 second delay]
"Lights 53, Sound 20... go"

Cluster coordination requires all operators ready (ACKs received) before any execute.

**Conditional Execution**:
Some cues branch:
- "If actor exits stage left, take LQ 47A"
- "If actor exits stage right, take LQ 47B"

The stage manager resolves the condition before standby, calling the appropriate cue.

**Failure Modes and Recovery Patterns**

The cue system has characteristic failure modes:

**Missed Cue**: Cue doesn't execute when called
- Causes: Operator didn't hear, wasn't ready, equipment failure
- Recovery: Stage manager assesses impact; skip and continue or call again
- Pattern: Accept the failure, adapt subsequent cues, debrief post-show

**Early Execution**: Cue fires before trigger
- Causes: Operator misinterpreted standby as go, auto-follow timing error, visual cue taken prematurely
- Recovery: Usually irrecoverable; adapt subsequent cues to compensate
- Pattern: Adjust timing of dependent cues to accommodate

**Cascade Failure**: One missed cue triggers downstream failures
- Scenario: Fade to black missed → thunder plays in full light → effect ruined → performers confused
- Recovery: Stage manager must decide: skip ahead, reset to known state, or adapt in place
- Pattern: Accept partial failure, prioritize critical path, minimize visible impact

**Communication Failure**: Headset system fails
- Recovery: Operators continue autonomously using their cue sheets and visual observation
- Pattern: Graceful degradation; operators have sufficient information to self-cue most actions

**Recovery Protocol**: "Stay calm, deal with it, move on"
- Panic spreads and compounds errors
- The show must continue
- Fix after performance; debrief and improve

**Rehearsal as Progressive Integration Testing**

The cue system develops through staged rehearsals:

**Dry Tech** (Component Testing):
- Technical rehearsal without performers
- Each cue executed in isolation
- Verify: Does each cue work?

**Cue-to-Cue** (Integration Testing):
- Technical rehearsal with performers, skipping non-technical scenes
- Cues executed in context with triggers
- Verify: Do cues fire at correct moments?

**Wet Tech** (System Testing):
- Full run-through with all elements
- Continuous operation
- Verify: Does the sequence work end-to-end?

**Tech Rehearsal** (Load Testing):
- Full rehearsal at performance pace
- No stops except for critical failures
- Verify: Can the system operate continuously?

This mirrors software testing: unit → integration → system → stress.

**Application Principles for Distributed Agent Systems**

Cue-based coordination reveals principles for any system coordinating distributed agents:

**1. Multi-Phase Commitment for Resource-Heavy Operations**

Don't send execute commands directly. Send prepare → confirm → execute sequences:
- Warning: Allocate resources, load context
- Standby: Verify readiness, acknowledge
- Go: Immediate execution

This separates resource preparation (slow) from execution (fast) and enables early failure detection (NACK at standby).

**2. Central Orchestration for Predetermined, Autonomous for Reactive**

The orchestrator triggers predetermined state transitions. Agents self-trigger for reactive responses:
- Orchestrated: Data pipeline stages, coordinated deployments
- Autonomous: Monitoring responses, real-time processing
- Hybrid: Autonomous within orchestrated constraints

**3. Explicit Dependencies Enable Parallelization and Recovery**

Implicit dependencies (relying on execution order) are fragile. Explicit dependencies enable:
- Parallel execution of independent tasks
- Clear critical path identification
- Recovery planning (which failures cascade?)

**4. Reserved Trigger Words Prevent Accidental Execution**

Define reserved keywords for execution triggers. Validate at protocol level:
- "go" only from orchestrator
- No casual use of trigger keywords
- Protocol enforcement, not just convention

**5. Acknowledgment Verifies Readiness**

Silence doesn't mean success. Require explicit acknowledgment:
- After standby: "Ready" or "Not ready"
- After go (for non-obvious): "Running" or "Complete"
- Timeout on missing ACK: Escalate

**6. Auto-Follow for Choreographed Sequences**

When timing is deterministic and tight, auto-follow reduces:
- Orchestrator cognitive load
- Communication latency
- Timing jitter from human reaction time

Single trigger initiates choreographed state machine.

**7. Graceful Degradation Over Catastrophic Failure**

Systems should continue despite failures:
- Skip non-critical failed operations
- Adapt subsequent operations to compensate
- Log for post-mortem; don't stop for debug

**8. Progressive Testing Reveals Integration Issues**

Unit testing is insufficient. Integration testing at multiple levels:
- Component: Individual agents work
- Integration: Agent communication works
- System: Complete workflows execute
- Stress: Continuous operation under load

**The Core Insight**

Cue-based coordination succeeds because it defines a **protocol, not a pattern**. The stage manager doesn't succeed because they're smart—they succeed because the cue system provides a rigorous, testable protocol for triggering autonomous execution.

For AI agent systems:
- Define the protocol explicitly
- Encode safety in syntax
- Separate preparation from execution from recovery
- Respect the boundary between orchestration and autonomous execution
- Test progressively; fail gracefully; adapt continuously

The show goes on—because the protocol ensures it can.

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Three-level explanation (ages 5-10, high school, expert) for cross-disciplinary mental model research

---

## Sources

### Primary Sources

- Cue-Based Coordination deep research document (docs/theater-stage-management/cue-based-coordination.md)

### Stage Management Cue Systems

- Cue (theatrical) - Wikipedia
- Stage Management - Calls and Cans and Comms - TheatreCrafts
- Calling cues? (warning vs standby) - SMNetwork.org
- Running shows and calling cues - Fiveable
- How To Call Cues (Part 1): Basics of Calling a Show - Everything Backstage

### Cue Sheets and Documentation

- Theatre Template: Master Cue Sheet - Theaterish
- What is a Cue Sheet? Best Practices & Free Template - StagTimer
- Theatrecrafts - Stage Management - Prompt Book
- The Complete Stage Manager - The Calling Script

### Technical Rehearsals

- How Stage Managers Shepherd Tech Rehearsals - Dramatics Magazine
- Technical rehearsals and cue-to-cue - Fiveable

### Show Control and Automation

- Cue Sequences - QLab 5 Documentation
- Wait Cues - QLab 5 Documentation
- Show control - Wikipedia

### Cross-References

- Master Cuelist (docs/theater-stage-management/master-cuelist.md)
- Central Communication Hub (docs/theater-stage-management/central-communication-hub.md)
- Chain of Command Routing (docs/kitchen-brigade/chain-of-command-routing.md)
