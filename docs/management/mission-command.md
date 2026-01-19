# Mission Command (Auftragstaktik)

Exploring how Mission Command doctrine applies to AI agent supervision and task delegation.

## Human Practice

| Aspect | Description |
|--------|-------------|
| **Origin** | Prussian Army, 19th century; formalized by Helmuth von Moltke the Elder |
| **Core Principle** | Commander provides the "what" and "why"; subordinate determines the "how" |
| **Key Term** | Auftragstaktik (mission-type tactics) vs. Befehlstaktik (detailed orders) |
| **Prerequisites** | Shared mental models, mutual trust (Einheit), clear focal point (Schwerpunkt) |
| **Adoption** | German Wehrmacht, Israeli Defense Forces, U.S. military (as "Mission Command") |

### Historical Context

The Prussian Army developed Auftragstaktik after learning hard lessons from Napoleon, who achieved rapid tempo through centralized genius. The Prussians realized a single brilliant commander is a single point of failure. Their solution: distribute decision-making authority to the lowest capable level.

Key developments:
- **1806 defeat by Napoleon**: Rigid Prussian formations crushed by French adaptability
- **1808-1812 reforms** (Scharnhorst, Gneisenau): Created professional officer corps expected to think, not just obey
- **Moltke the Elder**: "No plan survives contact with the enemy" - therefore push decisions down
- **1870-1871 Franco-Prussian War**: Demonstrated effectiveness against larger French army

The doctrine proved so effective that opponents repeatedly tried to copy it. Most failed because they copied the form (mission orders) without the prerequisites (trust, shared understanding, professional development).

## The Intent Statement

Mission Command centers on the **commander's intent** - a clear statement of the desired end state and why it matters.

### Components of Commander's Intent

| Component | Description | Example |
|-----------|-------------|---------|
| **Purpose** | Why this mission matters | "To prevent enemy reinforcement of the front" |
| **Key Tasks** | What must be accomplished | "Destroy or block the bridge" |
| **End State** | What success looks like | "Bridge impassable for 48+ hours" |
| **Constraints** | What must NOT happen | "Minimize civilian casualties" |
| **Freedom** | Where judgment applies | "Method of destruction is your choice" |

### What Intent Is NOT

- **Not a plan**: Intent doesn't specify how to achieve the goal
- **Not a script**: Subordinates aren't actors following lines
- **Not a wishlist**: It's the minimum necessary to achieve purpose
- **Not negotiable**: The purpose and end state are fixed; the method isn't

### Two Levels Up

A key principle: every subordinate should understand the intent **two levels up**. If you're a platoon leader, you know your company commander's intent AND your battalion commander's intent.

Why? If communications fail or the situation changes, you can still make decisions that serve the larger purpose. You're not just executing orders - you're pursuing the same goal through potentially different means.

## Prerequisites for Mission Command

Mission Command fails without these foundations. This is why most organizations that try to adopt it fail.

### 1. Shared Mental Models (Einheit)

**German term: Einheit** - unity of understanding, mutual trust, shared doctrine.

Everyone must understand:
- What "good" looks like in this organization
- Standard responses to common situations
- Technical vocabulary and concepts
- Decision-making criteria

**How Einheit develops:**
- Common training (German officer academy produced shared doctrine)
- Shared experiences (units that train and fight together)
- Explicit doctrine (written standards everyone learns)
- Cultural transmission (seniors model behavior, juniors absorb it)

**Without Einheit:** Subordinates can't predict what the commander would have wanted. They make decisions that seem locally reasonable but contradict organizational goals.

### 2. Commander's Trust (Vertrauen)

The commander must trust subordinates to:
- Understand the intent correctly
- Make sound judgments within that intent
- Act without requiring constant validation
- Report honestly when things go wrong

**Trust is built through:**
- Demonstrated competence (subordinate shows they can do the job)
- Demonstrated judgment (subordinate makes good decisions when unsupervised)
- Honest reporting (subordinate admits mistakes rather than hiding them)
- Time (trust accumulates through repeated positive experiences)

**Without trust:** Commander either micromanages (defeating the purpose) or delegates and then gets surprised by bad outcomes.

### 3. Subordinate's Capability

The subordinate must be:
- **Competent**: Technically capable of executing possible approaches
- **Confident**: Willing to make decisions without excessive validation
- **Committed**: Invested in the mission's success, not just compliance

**Capability is built through:**
- Training (technical skills, decision-making practice)
- Education (understanding why, not just how)
- Experience (progressively harder challenges)
- Reflection (after-action reviews to learn from outcomes)

**Without capability:** Even with clear intent and trust, subordinate can't execute effectively.

### 4. Focal Point (Schwerpunkt)

**German term: Schwerpunkt** - the decisive point where effort concentrates.

Clear intent requires clear priority. If everything is important, nothing is. Schwerpunkt tells subordinates:
- What matters most
- Where to concentrate resources when forced to choose
- What can be sacrificed if necessary

**Without Schwerpunkt:** Subordinates spread effort evenly, achieve nothing decisive. Or they guess at priorities and guess wrong.

## Failure Modes of Mission Command

### Failure Mode 1: Unclear Intent

**Symptom:** Subordinate asks "What do you mean by...?" repeatedly, or executes something that surprises the commander.

**Cause:** Intent statement is vague, assumes shared context that doesn't exist, or uses ambiguous terms.

**Example:**
```
Poor: "Improve the user experience"
Better: "Reduce checkout abandonment rate from 40% to 20% by removing friction in the payment flow"
```

The first requires mind-reading. The second specifies purpose (reduce abandonment), metric (40% to 20%), and constraint (payment flow, not wholesale redesign).

### Failure Mode 2: Insufficient Einheit

**Symptom:** Subordinate makes a reasonable decision that produces bad outcomes because they didn't understand organizational context.

**Cause:** Shared mental models never developed. Subordinate is operating from different assumptions than commander.

**Example:** New team member optimizes for code cleanliness, deletes "redundant" error handling, breaks production. They weren't wrong about code cleanliness - they lacked context about why that "redundant" code exists.

### Failure Mode 3: Trust Without Verification

**Symptom:** Delegation happens, problems accumulate undetected, eventually become crises.

**Cause:** Commander assumes trust means no oversight. Mission Command requires trust AND monitoring - not blind faith.

**Correction:** Trust level determines monitoring frequency, not whether monitoring happens. Even highly trusted subordinates get periodic checks.

### Failure Mode 4: Capability Gap

**Symptom:** Subordinate understands intent but can't execute effectively. Makes technically poor decisions even with clear goals.

**Cause:** Delegating beyond capability level. Mission Command isn't magic - subordinates still need skills.

**Correction:** Match task difficulty to demonstrated capability. Develop capability through progressively harder challenges.

### Failure Mode 5: Missing Schwerpunkt

**Symptom:** Subordinate paralyzed by competing priorities or makes arbitrary choices that don't serve the most important goal.

**Cause:** Intent doesn't specify what matters most. Multiple goals presented as equally important.

**Example:** "Fix bugs AND ship the feature AND improve test coverage" with no prioritization. Subordinate ships partial feature with reduced test coverage. Was that right?

## Backbrief: Confirming Shared Understanding

Before acting, the subordinate restates intent in their own words. The commander confirms or corrects.

### Backbrief Format

1. **Restate the purpose:** "I understand we need to [why] because [context]"
2. **Confirm key tasks:** "My tasks are to [what]"
3. **Describe planned approach:** "I intend to [how]"
4. **Identify risks/constraints:** "I see potential issues with [concerns]"
5. **Confirm end state:** "Success looks like [outcome]"

### Why Backbrief Works

- **Exposes misunderstanding early**: Before execution, not after failure
- **Tests intent clarity**: If subordinate can't restate it, it wasn't clear
- **Builds confidence**: Both parties know they're aligned
- **Documents plan**: Creates record of what was agreed

### When to Backbrief

- **Always for new relationships**: Until shared mental models develop
- **Complex or novel tasks**: Where intent might be misread
- **High-stakes situations**: Where failure is expensive
- **Can be abbreviated**: For routine tasks with established Einheit

---

## Agent Translation

### The Obvious Mapping

| Mission Command Concept | Agent Equivalent |
|------------------------|------------------|
| Commander's Intent | Task description with goals and constraints |
| Two Levels Up | CLAUDE.md provides organizational context |
| Einheit | Shared CLAUDE.md, consistent conventions |
| Vertrauen (trust) | Autonomy level (0-4) |
| Schwerpunkt | Single priority, clear acceptance criteria |
| Backbrief | Agent restates understanding before acting |
| Subordinate initiative | Agent decides implementation approach |

This mapping is correct but incomplete. The deeper questions are: When does Mission Command work for agents? When does it fail? How do you build the prerequisites?

### When Mission Command Works for Agents

**High Einheit (good CLAUDE.md, consistent codebase):**

The agent can infer the "right way" to do things because patterns are consistent and documented. Intent-based delegation works because the agent's orientation aligns with the codebase norms.

```
Human: "Fix the race condition in the audio handler"
Agent: [Reads CLAUDE.md, sees DMA2D patterns, understands timing constraints]
Agent: [Finds race condition, applies pattern consistent with codebase]
Agent: [Runs build, verifies fix]
```

The human provided intent. The agent determined approach based on shared understanding.

**Clear Schwerpunkt:**

The task has an obvious priority. The agent doesn't have to guess what matters most.

```
Human: "Add null check before dereferencing pSound in playback.c. Audio stability is critical - this is causing crashes."
Agent: [Understands priority: prevent crashes, not code beauty]
Agent: [Adds defensive check even if it's not the "cleanest" solution]
```

**Appropriate capability:**

The task is within the agent's demonstrated ability. The agent has the technical skills to execute any reasonable approach.

### When Mission Command Fails for Agents

**Low Einheit (poor documentation, inconsistent patterns):**

The agent can't infer the "right way" because there isn't one, or it's not documented. Intent-based delegation produces unpredictable results.

```
Human: "Improve the error handling"
Agent: [No error handling conventions in CLAUDE.md]
Agent: [Sees three different error patterns in codebase]
Agent: [Picks one arbitrarily - 33% chance of matching expectations]
```

**Ambiguous Schwerpunkt:**

Multiple competing goals with no clear priority. The agent must guess.

```
Human: "Refactor the display code to be cleaner and faster"
Agent: [Cleaner = more abstractions, potentially slower]
Agent: [Faster = inline code, potentially messier]
Agent: [Which matters more? Human didn't say]
```

**Beyond capability:**

The task requires judgment the agent doesn't have. Technical skill isn't the issue - it's judgment about what "good" means in context.

```
Human: "Design a better API for the sample player"
Agent: [Has no way to evaluate "better" - aesthetic judgment]
Agent: [Produces something technically correct but awkward]
```

### Critical Difference: Agents Don't Have Initiative

Human subordinates can recognize when their commander's intent would be better served by a different approach than the one implied. They can innovate within intent.

**Human example:**
- Intent: "Prevent enemy from crossing the bridge"
- Original plan: Blow up bridge
- On the ground: Discover bridge is only route for civilian evacuation
- Initiative: Defend bridge instead of destroying it - still prevents enemy crossing, allows civilians through

The subordinate recognized the commander would have wanted this if they'd known. They served the intent through unexpected means.

**Agent limitation:**
Agents can only exercise initiative within explicitly stated bounds. They can choose among recognized approaches. They cannot recognize that the framing itself is wrong.

```
Human: "Add caching to improve performance"
Agent: [Adds caching]
Agent: [Does NOT notice that the actual problem is an N+1 query]
```

The agent served the literal intent (add caching) but missed the real intent (improve performance). A human subordinate might have said "I know you said caching, but I think the real problem is..."

**Implication:** Intent statements for agents must be more complete than for humans. Agents can't fill in gaps through initiative.

### Backbrief for Agents

The backbrief is highly valuable for agents. It catches misalignment before execution.

**Implementation:**

```markdown
## Task Format with Backbrief

### Human provides:
**Intent:** [What and why]
**Constraints:** [What must not happen]
**Priority:** [What matters most]

### Agent responds before acting:
**My understanding:** I will [specific plan] because [interpretation of why]
**I will NOT:** [restating constraints]
**Success looks like:** [concrete outcome]
**Concerns:** [anything unclear]

### Human confirms or corrects, then agent proceeds
```

**When to require backbrief:**
- Autonomy Level 0-1: Always
- Autonomy Level 2: For complex or novel tasks
- Autonomy Level 3-4: When task seems unusually scoped or involves new domains

**Abbreviated backbrief (high Einheit, routine tasks):**

```
Agent: "I'll fix the null pointer in tft.c by adding a guard clause before line 147. Build and test afterward. Proceed?"
```

This confirms the agent's interpretation without lengthy explanation.

### Building Einheit for Agents

Since agents start fresh each session, Einheit must be encoded in artifacts that persist.

**Einheit artifacts:**

| Artifact | Purpose | Example |
|----------|---------|---------|
| **CLAUDE.md** | Organizational doctrine | Naming conventions, build process, style |
| **Architecture docs** | Structural understanding | Component relationships, data flow |
| **Decision records** | Historical context | Why we chose X over Y |
| **Examples** | Pattern demonstration | "Good" changes to learn from |
| **Conventions** | Implicit → explicit | What experienced humans know |

**The Einheit test:** Can a new agent, with no prior sessions, understand enough from these artifacts to make decisions consistent with organizational norms?

If yes: Mission Command can work
If no: Need more Befehlstaktik (detailed orders)

**Einheit development cycle:**

1. Agent makes a decision that surprises you
2. Was it wrong? Or just different from what you'd have done?
3. If wrong: What context was missing that led to the error?
4. Add that context to CLAUDE.md or related docs
5. Next agent benefits from accumulated Einheit

### Trust Levels as Vertrauen Implementation

The autonomy levels (0-4) from agent-management-framework.md are a direct implementation of Vertrauen calibration:

| Level | Mission Command Analog | Delegation Style |
|-------|----------------------|------------------|
| **0** | Officer cadet observing | No delegation - human does, agent watches |
| **1** | Junior officer with supervisor | Agent suggests, human approves each action |
| **2** | Experienced officer with review | Agent acts, human reviews before permanent |
| **3** | Trusted subordinate | Agent acts autonomously, monitored |
| **4** | Empowered commander | Agent fully autonomous within boundaries |

**Trust progression mirrors military development:**

Military: Cadet → Lieutenant → Captain → Major → Colonel
Agent: Level 0 → Level 1 → Level 2 → Level 3 → Level 4

Each promotion requires demonstrated competence at the current level. Demotion happens when trust is violated.

**Key difference:** Human trust builds through relationship over years. Agent trust resets each session. Trust levels must be encoded in configuration, not accumulated in relationship.

### Schwerpunkt for Agent Tasks

Every task should have a single clear priority. This eliminates the agent's need to guess.

**Schwerpunkt format:**

```markdown
## Task: [Title]

**Priority (pick ONE):**
- [ ] Correctness: Above all, don't break things
- [ ] Speed: Ship fast, clean up later
- [ ] Quality: Take time to do it right
- [ ] Learning: Understand before acting

**Goal:** [What we're trying to achieve]

**Constraints:** [What must not happen]
```

**Example with Schwerpunkt:**

```markdown
## Task: Fix audio dropout bug

**Priority:** Correctness - this is a production crash, fixing it correctly matters more than fixing it fast

**Goal:** Eliminate the race condition causing audio dropouts during display updates

**Constraints:**
- Do not change audio ISR timing
- Do not modify display queue behavior (fix must be in coordination, not architecture)
- Must pass existing audio timing tests
```

The agent knows: if there's a tradeoff between a quick fix and a correct fix, choose correct. If a correct fix requires changes outside scope, escalate instead of shipping partial fix.

---

## When to Use Befehlstaktik (Detailed Orders)

Mission Command isn't always appropriate. Sometimes detailed orders are better.

### Use Detailed Orders When:

**Low Einheit:**
Agent doesn't have shared context. Detailed orders substitute for missing mental models.

```
Human: "Edit line 47 of config.c, change BUFFER_SIZE from 256 to 512"
```

This is Befehlstaktik. It's appropriate when:
- The change is surgical and specific
- Context would take longer to explain than the task itself
- There's no judgment involved

**Novel situation:**
No established patterns exist. The human must provide the approach because there's nothing for the agent to infer from.

**High stakes:**
Failure is expensive. Detailed orders reduce variance, even if they also reduce optimization.

**Training:**
Building toward Mission Command. Early detailed orders teach patterns. Later, intent-based delegation relies on those patterns.

### Befehlstaktik Anti-Patterns

**Micromanagement that defeats agent capability:**

```
Human: "Read file X. Then grep for Y. Then change Z to W in line 47. Then run the build."
```

This is step-by-step scripting. It uses the agent as a keyboard, not a thinker. The agent could have found the line itself, might have found a better fix, can't exercise any judgment.

**Appropriate when:** Human knows exactly what's needed and why
**Anti-pattern when:** Human is specifying steps because they don't trust the agent, not because the steps are the only right way

### The Spectrum

Mission Command and Befehlstaktik are endpoints of a spectrum, not binary choices.

```
Full Befehlstaktik                                    Full Auftragstaktik
(Script every step)                                  (Just provide intent)
        │                                                      │
        ├──── New agent, no Einheit                           │
        │                                                      │
        ├──────── Known agent, learning domain                │
        │                                                      │
        ├────────────── Established Einheit, routine          │
        │                                                      │
        └───────────────────── High trust, clear intent ──────┘
```

Move right as:
- Einheit develops
- Trust is established
- Agent demonstrates capability
- Patterns become consistent

Move left when:
- New domain (no patterns)
- Critical operations (reduce variance)
- Correction needed (agent went wrong)

---

## Practical Implementation

### Task Template for Mission Command

```markdown
## Task: [Title]

### Commander's Intent
**Purpose:** Why this task matters
**End State:** What success looks like (concrete, verifiable)
**Priority:** Single clear focus (correctness / speed / quality)

### Constraints
- What MUST happen
- What MUST NOT happen
- What can be traded off if necessary

### Context
- Relevant files: [list]
- Related decisions: [link to ADR or context.md]
- Patterns to follow: [reference to CLAUDE.md sections]

### Backbrief Required: [Yes/No]
(Yes for novel tasks, complex scope, or trust level < 3)
```

### Evaluating Mission Command Readiness

Before using intent-based delegation, check:

| Prerequisite | Test | Action if Missing |
|--------------|------|-------------------|
| **Einheit** | Can agent infer patterns from CLAUDE.md? | Add documentation or use detailed orders |
| **Trust** | Has agent succeeded at similar scope? | Start with lower autonomy level |
| **Capability** | Is task within agent's technical reach? | Reduce scope or provide more guidance |
| **Schwerpunkt** | Is priority unambiguous? | Specify single priority explicitly |
| **Intent clarity** | Can you state end state concretely? | Refine intent until verifiable |

### After-Action Review

After task completion, evaluate Mission Command effectiveness:

1. **Did the agent achieve the intent?** Not just the letter, but the spirit
2. **Did the agent make any surprising decisions?** Were they good surprises (initiative) or bad surprises (misalignment)?
3. **What context was missing?** What would have helped?
4. **Should trust level change?** Promote if exceeded expectations, demote if violated trust
5. **What should update in CLAUDE.md?** Accumulate Einheit for future agents

---

## Open Questions

1. **Can agents develop Fingerspitzengefuhl?** The "fingertip feel" that lets experts act from intuition rather than analysis. Is this possible for agents, or is every decision necessarily analytical?

2. **What's the right backbrief depth?** Full restatement of intent takes time. Abbreviated backbrief might miss misalignment. What's the optimal tradeoff?

3. **How do you measure Einheit quality?** Is there a metric for "shared understanding" that predicts Mission Command success?

4. **Can agents escalate appropriately?** Human subordinates recognize when they're out of their depth and escalate. Do agents recognize their limits, or do they hallucinate solutions?

5. **Multi-agent Schwerpunkt:** If multiple agents work toward a goal, how is priority communicated across agents? Do they need a "commander" agent, or can shared CLAUDE.md suffice?

6. **Recovery from Einheit drift:** As codebases evolve, old Einheit becomes stale. How do you detect and correct drift?

7. **Initiative bounds:** How do you tell an agent "use initiative here, but not there"? Is this even possible, or is initiative all-or-nothing?

---

## Systems to Build

- [ ] **Intent template enforcement:** Task system requires intent/constraints/priority format
- [ ] **Backbrief workflow:** Agent must restate understanding; human confirms before execution
- [ ] **Einheit audit:** Tool to detect gaps between CLAUDE.md and actual codebase patterns
- [ ] **Schwerpunkt validator:** Flag tasks with multiple competing priorities
- [ ] **Trust progression tracker:** Log decisions that inform autonomy level changes
- [ ] **After-action capture:** Structured template for post-task Einheit updates

---

## Sources

### Military Doctrine
- Moltke, Helmuth von. "On the Art of War" - Original Auftragstaktik formulation
- U.S. Army Doctrine Publication 6-0: Mission Command (2019)
- Shamir, Eitan. "Transforming Command" (2011) - History of mission command adoption
- Citino, Robert. "The German Way of War" (2005) - Prussian military culture

### Boyd's Integration
- Boyd, John. "Organic Design for Command and Control" (1987) - Four organizational qualities including Auftragstaktik
- Osinga, Frans. "Science, Strategy and War" (2007) - Academic analysis connecting Boyd to German doctrine

### Agent Application
- See OODA loop document for initial Auftragstaktik mapping
- Agent management framework for autonomy levels (trust implementation)

---

## Status

**Phase:** Deep exploration complete. Key insights: Mission Command requires prerequisites (Einheit, trust, capability, Schwerpunkt) that must be explicitly built for agents since they don't accumulate through relationship. Backbrief is highly valuable for catching misalignment. The spectrum between Befehlstaktik and Auftragstaktik depends on Einheit development, not just trust.

**Next:** Build backbrief workflow tool and Einheit audit system.

