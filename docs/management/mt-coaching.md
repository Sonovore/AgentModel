# Manager Tools: Coaching

Exploring how the Coaching concept applies to AI agent supervision.

## Human Practice

| Aspect | Description |
|--------|-------------|
| **Purpose** | Regularly ask for improved performance |
| **Format** | Goal-setting, skill development, 5 min/week |
| **Distinction from Feedback** | Feedback = past behavior, Coaching = future improvement |
| **Psychology** | Growth mindset, mastery motivation, stretch goals |
| **Focus** | Long-term capability building, not immediate correction |

## The Obvious Objection

Agents don't "grow" or "develop skills." Each session is independent. The agent that struggled yesterday doesn't exist today. Skills can't accumulate in an entity with no persistent memory.

**This objection is correct but incomplete.** It only considers coaching the agent. There are three other coaching targets that do persist.

## The Four Coaching Targets

```
┌─────────────────────────────────────────────────────────────────┐
│                    HUMAN-AGENT SYSTEM                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌──────────┐         ┌──────────┐         ┌──────────┐      │
│    │  Human   │ ──────► │ CLAUDE.md│ ──────► │  Agent   │      │
│    │ (learns) │         │ (evolves)│         │(stateless)│     │
│    └──────────┘         └──────────┘         └──────────┘      │
│         │                    │                    │             │
│         │                    │                    │             │
│         └────────────────────┴────────────────────┘             │
│                              │                                  │
│                     ┌────────┴────────┐                         │
│                     │ System Behavior │                         │
│                     │    (emergent)   │                         │
│                     └─────────────────┘                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Coaching Target | Persistence | Growth Mechanism |
|-----------------|-------------|------------------|
| **Agent** | None | N/A (stateless) |
| **Human** | Full | Learning, practice, judgment |
| **CLAUDE.md** | Full | Revision, refinement |
| **Human-Agent System** | Full | Workflow improvement, trust calibration |

**Key insight:** Coaching doesn't target the agent. It targets everything around the agent.

## Coaching Target 1: The Human

The human is the only entity that actually "grows" in the traditional sense.

### What Skills Develop?

| Skill | Description | Coaching Equivalent |
|-------|-------------|---------------------|
| **Prompt Engineering** | Crafting effective instructions | Deliberate practice with progressively harder tasks |
| **Task Decomposition** | Breaking problems into agent-sized chunks | Review task history, identify decomposition failures |
| **Capability Calibration** | Knowing what agents can/can't do | Test boundaries, track results |
| **Context Management** | Deciding what context to provide | A/B test context strategies |
| **Quality Assessment** | Evaluating agent output quickly | Develop heuristics, checklists |
| **Recovery** | Handling agent failures gracefully | Practice recovery scenarios |

### Coaching Questions for the Human

Traditional coaching: "What skill do you want to develop?"

Agent supervision coaching:
- "Where do you lose time with agents?"
- "What agent failures frustrate you most?"
- "What would you delegate if you trusted the agent more?"
- "What patterns do you keep correcting?"
- "What tasks are you avoiding giving to agents?"

### Stretch Goals for Humans

| Current State | Stretch Goal |
|---------------|--------------|
| Review every agent commit | Review only flagged commits |
| Write detailed prompts | Trust agent to fill in gaps |
| Fix agent mistakes manually | Coach agent to self-correct in-context |
| Single-agent workflows | Multi-agent orchestration |
| Task-level delegation | Session-level delegation |

**Insight:** Human coaching in agent work is about building trust through competence - the human's competence at supervision, not the agent's competence at execution.

## Coaching Target 2: CLAUDE.md

CLAUDE.md is the "habit layer" (from mt-feedback.md). Coaching it means deliberate improvement over time, not just reactive fixes.

### Feedback vs. Coaching for CLAUDE.md

| Feedback (Reactive) | Coaching (Proactive) |
|---------------------|----------------------|
| Agent made mistake → add instruction | Review CLAUDE.md weekly → identify gaps |
| Fix what's broken | Improve what's working |
| Patch symptoms | Address root causes |
| Respond to failures | Anticipate needs |

### CLAUDE.md Coaching Practice

**Weekly 5-minute review:**

1. **Audit recent sessions:**
   - What corrections appeared repeatedly?
   - What worked better than expected?
   - Any new task types attempted?

2. **Ask coaching questions:**
   - "What instruction would have prevented the most friction?"
   - "What instruction is outdated given model improvements?"
   - "What instruction is too vague to be useful?"
   - "What implicit knowledge should be explicit?"

3. **Set improvement goals:**
   - "This week, refine the error handling guidance"
   - "Prune instructions that duplicate model defaults"
   - "Add examples for the tricky edge case"

### CLAUDE.md Maturity Model

| Level | Characteristics | Coaching Focus |
|-------|-----------------|----------------|
| **1. Absent** | No CLAUDE.md | Create minimal version |
| **2. Reactive** | Patches accumulated over time | Organize, consolidate |
| **3. Organized** | Clear sections, no contradictions | Add proactive guidance |
| **4. Anticipatory** | Prevents problems before they occur | Optimize for efficiency |
| **5. Minimal** | Maximum effect, minimum tokens | Maintain and adapt |

**Insight:** Most CLAUDE.md files plateau at Level 2 or 3. Coaching moves them toward Level 5.

## Coaching Target 3: The Human-Agent System

The system is more than its parts. Coaching the system means improving the interaction patterns, workflows, and trust calibration.

### System Capabilities to Develop

| Capability | Description | Development Path |
|------------|-------------|------------------|
| **Trust Calibration** | Knowing when to trust agent output | Track outcomes, adjust thresholds |
| **Handoff Quality** | Seamless context transfer | Refine handoff protocols |
| **Failure Recovery** | Getting back on track after problems | Practice recovery workflows |
| **Parallel Operation** | Human and agent working simultaneously | Design async patterns |
| **Escalation** | Agent knows when to ask for help | Tune escalation triggers |

### System Stretch Goals

```
Current: Human reviews all agent work
Stretch: Human reviews samples based on confidence scores

Current: Agent completes tasks, human evaluates
Stretch: Agent evaluates own work, flags concerns

Current: Single agent per task
Stretch: Agent ensemble with voting

Current: Human manages context
Stretch: Context management agent handles it
```

### Coaching the Trust Relationship

Trust is not binary (trust/don't trust). It's multidimensional:

| Dimension | Coaching Focus |
|-----------|----------------|
| **Correctness trust** | "Will the output be right?" |
| **Completeness trust** | "Will the output be complete?" |
| **Judgment trust** | "Will it ask vs. guess appropriately?" |
| **Scope trust** | "Will it stay within boundaries?" |
| **Self-assessment trust** | "Will it know when it's uncertain?" |

**Coaching question:** "Which trust dimension is limiting you most?"

## Model Selection: Hiring vs. Developing

Traditional coaching assumes you're developing the person you have. Agent work adds a new option: **selecting a different capability level**.

| Human Parallel | Agent Equivalent |
|----------------|------------------|
| Train junior to senior | Haiku for simple, Opus for complex |
| Promote within | Upgrade model tier for same task |
| Hire specialist | Use domain-specific fine-tune |
| Fire and replace | Demote trust level, reduce scope |

**Insight:** Sometimes "coaching" an agent means recognizing the task needs a different model, not better instructions.

### When to Select vs. When to Coach (Instructions)

| Symptom | Select Different Model | Coach Instructions |
|---------|----------------------|-------------------|
| Wrong answers despite clear prompt | Yes | No |
| Right answers with too much guidance | Maybe | Yes |
| Inconsistent quality | Yes (model limitation) | Maybe (instruction ambiguity) |
| Missing edge cases | Maybe | Yes |
| Slow/expensive | Yes (use smaller model) | No |

## Stretch Goals for Agents?

Traditional stretch goals push someone beyond their comfort zone to grow. Agents don't have comfort zones or growth, but there's an analogous concept: **capability boundary probing**.

### Capability Boundary Probing

```
Known Capability Zone
        │
        ▼
┌───────────────────┐
│ Agent succeeds    │ ─────► Expand scope
│ reliably here     │
└───────────────────┘
        │
        ▼
┌───────────────────┐
│ Success rate      │ ─────► This is the boundary
│ drops here        │        Monitor and test
└───────────────────┘
        │
        ▼
┌───────────────────┐
│ Agent fails       │ ─────► Don't assign these tasks
│ reliably here     │        (or change approach)
└───────────────────┘
```

**"Stretch goal" equivalent:** Deliberately assign tasks at the boundary to:
1. Find where the boundary actually is
2. Discover if instruction improvements move the boundary
3. Detect when model updates shift the boundary

### Probing Protocol

1. **Identify candidate task:** Slightly harder than current comfort zone
2. **Assign with observation:** Track success/failure and failure modes
3. **Analyze:** Was it instructions, context, or model capability?
4. **Adjust:** Improve instructions OR note as model limitation
5. **Re-test:** Did the adjustment help?

This is coaching the system by deliberately testing its limits.

## Feedback vs. Coaching Summary

| Aspect | Feedback (mt-feedback.md) | Coaching |
|--------|---------------------------|----------|
| **Time orientation** | Past behavior | Future capability |
| **Trigger** | Something happened | Scheduled/proactive |
| **Target** | CLAUDE.md (immediate) | Human, CLAUDE.md, system (long-term) |
| **Goal** | Correct error | Build capability |
| **Frequency** | As needed | Regular cadence |
| **Scope** | Specific incident | Overall effectiveness |

**Relationship:** Feedback is coaching's raw material. Coaching is strategic use of feedback patterns.

## Practical Coaching Rituals

### Weekly (5 min)

1. Review session friction points
2. One CLAUDE.md improvement
3. One human skill to practice this week

### Monthly (15 min)

1. Audit CLAUDE.md for contradictions and bloat
2. Review capability boundary map - has it shifted?
3. Set one system-level improvement goal

### After Model Updates

1. Run capability calibration suite
2. Review CLAUDE.md for obsolete instructions
3. Probe new capability boundaries

## Open Questions

1. **Coaching frequency:** Weekly is borrowed from human coaching. Is that right for systems that could theoretically improve daily?

2. **Who coaches whom?** Can agents coach humans on prompt engineering? Can agents coach CLAUDE.md directly?

3. **Measurement:** How do you measure "system capability improvement" over time? What metrics matter?

4. **Coaching vs. Tinkering:** When does healthy coaching become counterproductive over-optimization?

5. **Multi-model coaching:** If you use multiple models, do you need separate coaching for each? Or does system-level coaching suffice?

## Systems to Build

- [ ] **Coaching log:** Track interventions and outcomes over time
- [ ] **Capability boundary tracker:** Map where reliability drops off
- [ ] **CLAUDE.md changelog:** What changed, why, did it help
- [ ] **Human skill tracker:** What supervision skills are developing
- [ ] **Model comparison framework:** When to select vs. when to coach

## The Core Reframe

**Traditional coaching:** Develop the person's skills over time.

**Agent system coaching:** Develop the human-agent system's capabilities over time.

The agent doesn't grow. But:
- The human gets better at supervision
- CLAUDE.md gets more effective
- The system achieves more with less friction
- Trust calibration becomes more precise

**Coaching for agents is coaching the system that produces agents, not the agents themselves.**

This is analogous to coaching a sports team vs. coaching individual players. The team has capabilities that emerge from how the players work together. Improving the team means improving coordination, plays, and strategy - not just individual skills.

The human-agent system is the team. Coaching it means improving how human and agent work together, not just improving either one alone.

## Status

**Phase:** Exploration complete. Key insight is that coaching targets persist (human, CLAUDE.md, system) even though agents don't. The coaching cycle operates on the system that creates agents, not on agents themselves.
