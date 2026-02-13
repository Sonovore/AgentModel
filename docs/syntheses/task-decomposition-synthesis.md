# Task Decomposition and Assignment: Cross-Disciplinary Synthesis

## Problem Statement

### Why This Matters

Task decomposition and assignment is the foundation of multi-agent coordination. Before agents can communicate, coordinate, or resolve conflicts, someone must decide what each agent does. Poor decomposition creates cascading failures: tasks too large overflow context windows, tasks too small create coordination overhead, mismatched assignments waste capability, and unclear boundaries cause conflicts.

The challenge is not merely "break work into pieces"---it is **determining optimal granularity, matching task complexity to agent capability, managing dependencies, and assigning work based on specialization**.

### When This Occurs in Multi-Agent Systems

Task decomposition and assignment challenges emerge whenever:
- A complex goal requires breaking into agent-executable units
- Multiple agents with different capabilities are available
- Tasks have dependencies that constrain execution order
- Agent capability varies (different models, contexts, tools)
- Resources (tokens, time, API calls) must be allocated across tasks
- Quality requirements vary across different parts of the work

### What Breaks If You Get It Wrong

**Tasks too large (insufficient decomposition):**
- Context window overflow: Agent can't hold task + context + working space
- Compounding errors: One mistake early cascades through entire task
- No parallelization: Serial execution even when parallelism was possible
- Unclear progress: Can't tell where things failed or succeeded
- Recovery impossible: Must restart from beginning on failure

**Tasks too small (excessive decomposition):**
- Coordination overhead: More time coordinating than executing
- Context thrashing: Essential context doesn't fit with tiny tasks
- Lost coherence: Individual pieces correct but don't fit together
- Handoff failures: Information lost between fragments
- Human bottleneck: Too many approval points

**Task-agent mismatch:**
- Wasted capability: Opus-tier agents on Haiku-tier tasks
- Quality failures: Simple agents on complex tasks fail or hallucinate
- Dependency violations: Assigning task before prerequisites complete
- Boundary conflicts: Multiple agents claim same work

### Scope and Boundaries

This synthesis addresses:
- How to determine optimal task granularity
- Matching task complexity to agent capability
- Handling dependencies between tasks
- Hierarchical vs. sequential decomposition
- Assignment strategies based on specialization

It does not deeply address:
- Information flow between agents (separate synthesis)
- Conflict resolution when assignments overlap (separate synthesis)
- Temporal synchronization of parallel tasks (separate synthesis)

---

## Perspectives

### Perspective 1: Mission Analysis (Military Planning)

**Core Insight:**
Mission analysis reveals that the gap between **specified tasks** (what you're told) and **essential tasks** (what actually defines success) is where decomposition earns its value. A mature decomposition process surfaces implied tasks---the unstated prerequisites and dependencies that must be accomplished for the explicit tasks to succeed.

**Mechanisms and How It Works:**

1. **Three-Tier Task Classification:**
   - **Specified Tasks:** Explicitly stated in the order/request
   - **Implied Tasks:** Not stated but required to accomplish specified tasks (derived through analysis of dependencies, context, domain knowledge)
   - **Essential Tasks:** From both lists, those that MUST be accomplished---failure means mission failure

   The filtering process: Not every task is essential. Essential tasks are the critical few that define success. This is the "so what" determination.

2. **The Restated Mission (5 Ws):**
   After analysis, formulate understanding as:
   - WHO: The executing unit/agent
   - WHAT: Essential tasks in execution order
   - WHEN: Time constraints and deadlines
   - WHERE: Target environment/system/files
   - WHY: Purpose (from higher-level concept of operations)

   The WHY is most important---it enables adaptation when conditions change.

3. **Constraints and Restrictions:**
   - **Constraints (Must Do):** Non-negotiable requirements ("Maintain a two-battalion reserve")
   - **Restrictions (Must Not Do):** Prohibited actions ("Do not modify production database directly")

   Together they define the operating envelope---wide latitude in HOW, strict requirements in WHAT must/must not be done.

4. **Assumption Management:**
   Decomposition requires assumptions about context, environment, dependencies. Each assumption introduces risk. Requirements:
   - Is assumption valid (likely true)?
   - Is assumption necessary (planning can't continue without it)?
   - What happens if assumption proves false?

   High-risk assumptions need contingency branches.

**When It Works, When It Fails:**
- Works when goals are well-defined with clear success criteria
- Works when domain knowledge enables identification of implied tasks
- Fails when novel situations don't fit established patterns
- Fails when time pressure prevents thorough analysis
- Fails when assumptions can't be validated before commitment

**Scaling Characteristics:**
- Small scale: Single analyst can decompose
- Medium scale: Staff sections analyze in parallel, then integrate
- Large scale: Hierarchical decomposition---each level decomposes their portion
- The 1/3-2/3 rule: Commander uses max 1/3 of time for planning; 2/3 for subordinates to plan and execute

**Key Takeaways for Agents:**
- Surface the implicit: Much of what's needed isn't stated
- Identify what's essential: Not all tasks are equal---which define success?
- Respect boundaries: Constraints and restrictions define acceptable action
- Manage assumptions explicitly: Every inference is a potential failure point
- Connect tasks to purpose: Always understand WHY---it enables adaptation

---

### Perspective 2: Military Decision Making Process (MDMP)

**Core Insight:**
MDMP demonstrates that task decomposition is one step in a **larger planning process**---you can't decompose well in isolation. The seven-step process provides structure: receipt of mission, mission analysis (decomposition), COA development, COA analysis (wargaming), COA comparison, COA approval, orders production. Each step builds on previous outputs; errors early compound later.

**Mechanisms and How It Works:**

1. **Structured Decomposition Process:**
   Mission analysis (Step 2) contains 17-19 substeps including:
   - Analyze higher headquarters' plan/order
   - Perform initial intelligence preparation
   - Determine specified, implied, essential tasks
   - Review available assets and identify resource shortfalls
   - Identify constraints
   - Develop assumptions
   - Begin risk management

   This thoroughness is why mission analysis takes ~30% of planning time.

2. **Time Management (1/3-2/3 Rule):**
   ```
   Battalion (1/3):    0600 - 1400 (8 hours)
   Companies (2/3):    1400 - 1800 (4 hours for their 1/3)
   Platoons (2/3):     1800 - 2400 (6 hours for their 1/3)
   ```

   Perfect decomposition at the top is worthless if subordinates can't plan and prepare their portions. Time allocation is part of decomposition.

3. **Parallel vs. Sequential Planning:**
   - **Sequential:** Each echelon completes before subordinates begin (most complete, most time)
   - **Parallel:** Multiple echelons plan simultaneously (saves time, requires active collaboration)

   Parallel planning requires warning orders to enable subordinate planning before complete higher order.

4. **Running Estimates:**
   Continuous assessment maintained throughout planning:
   - Track current conditions and resources
   - Update facts and assumptions
   - Identify changes affecting plan viability
   - Support rapid decision making during execution

   Running estimates are state management across planning iterations.

5. **Deliberate vs. Rapid Planning:**
   - **Full MDMP:** Complex, high-stakes, unfamiliar, multiple valid approaches
   - **Abbreviated/RDSP:** Familiar, time-constrained, clear situation, single obvious approach

   Rapid Decision-Making (RDSP) is 30-40% faster, prioritizes timely over optimal.

**When It Works, When It Fails:**
- Works when thoroughness is more valuable than speed
- Works when planning resources (staff) are available
- Fails when time pressure requires immediate action
- Fails when situation is too dynamic for deliberate planning
- Fails when stovepiped efforts don't integrate

**Scaling Characteristics:**
- Battalion and higher: Full MDMP with staff support
- Company and below: Troop Leading Procedures (8 steps, compressed)
- Time-constrained: Abbreviated MDMP or RDSP
- Each level decomposes within their scope; aggregates for higher

**Key Takeaways for Agents:**
- Planning is sequential and cumulative: Errors early compound later
- Time management is critical: Balance planning vs. execution time
- Running estimates maintain context: Update understanding as information arrives
- Products enable coordination: Clear outputs at each step (mission statement, intent, orders)
- Know when to abbreviate: Full process isn't always appropriate

---

### Perspective 3: Task Complexity Assessment (Helper Agents)

**Core Insight:**
Task complexity assessment provides a **quantitative framework** for matching task decomposition to agent capability. Six dimensions (novelty, ambiguity, depth, integration, abstraction, stakes) scored 0-2 produce a 0-12 complexity score that routes tasks to appropriate model tiers (Haiku/Sonnet/Opus).

**Mechanisms and How It Works:**

1. **Six Assessment Dimensions:**

   | Dimension | 0 (Low) | 1 (Medium) | 2 (High) |
   |-----------|---------|------------|----------|
   | **Novelty** | Well-established, documented | Mix of established/emerging | Cutting-edge, little literature |
   | **Ambiguity** | Clear, single authority | Multiple sources, minor variations | Conflicting experts, competing frameworks |
   | **Depth** | Surface understanding | 2-3 layers deep | 4+ layers to first principles |
   | **Integration** | Single discipline | 2-3 related disciplines | 4+ disparate disciplines |
   | **Abstraction** | Concrete, step-by-step | Mix of concrete/conceptual | Highly theoretical/philosophical |
   | **Stakes** | Easy to redo, non-critical | Some cost to redo, affects project | Expensive/impossible to redo |

2. **Routing Thresholds:**
   ```
   0-4:  Haiku  - Simple, well-defined, low complexity
   5-8:  Sonnet - Moderate complexity, standard analysis
   9-12: Opus   - High complexity, deep reasoning required
   ```

3. **Adjustment Factors:**
   - **Increase tier:** Previous similar tasks failed, high quality requirements, time-sensitive, explicit thoroughness request
   - **Decrease tier:** Budget constraints, exploratory/draft acceptable, time abundant, low failure risk

4. **Complexity-Based Decomposition:**
   If a task scores above agent capability threshold:
   - Break into subtasks that individually score within capability
   - Each subtask should be independently completable
   - Aggregate subtask outputs to achieve original goal

**When It Works, When It Fails:**
- Works when dimensions can be assessed before execution
- Works when complexity is decomposable (high-scoring task can become multiple medium-scoring)
- Fails when complexity is irreducible (some tasks are inherently complex)
- Fails when dimensions interact non-linearly
- Fails when assessment requires domain expertise agent lacks

**Scaling Characteristics:**
- Assessment itself is low-complexity (can use Haiku)
- Calibration requires feedback: Did routed tasks succeed?
- Domain-specific profiles may be needed (research vs. coding)
- Learning loop: Adjust thresholds based on observed outcomes

**Key Takeaways for Agents:**
- Measure complexity systematically: Six dimensions provide structure
- Match complexity to capability: Don't assign Opus tasks to Haiku
- Decompose if above threshold: Break high-complexity into medium-complexity
- Track calibration: Did routing decisions lead to success?
- Domain matters: Same task may be different complexity in different domains

---

### Perspective 4: Zone of Proximal Development (Pedagogy)

**Core Insight:**
The Zone of Proximal Development (ZPD) reveals that task assignment is not just about current capability but about the **interaction between agent, task, and support system**. Tasks should be assigned within the ZPD---achievable with scaffolding but beyond independent capability---to optimize both execution success and capability development.

**Mechanisms and How It Works:**

1. **Three-Zone Model:**
   ```
   ┌─────────────────────────────────────────────────────────────────┐
   │  IMPOSSIBLE (Above ZPD)                                         │
   │  - Fails even with maximum scaffolding                          │
   │  - Hallucination rates spike, errors compound                   │
   ├─────────────────────────────────────────────────────────────────┤
   │  OPERATIONAL ZPD (Achievable with Scaffolding)                  │
   │  - Succeeds with appropriate support                            │
   │  - Sweet spot for capability development                        │
   ├─────────────────────────────────────────────────────────────────┤
   │  INDEPENDENT (Below ZPD)                                        │
   │  - Succeeds without assistance                                  │
   │  - Scaffolding adds overhead without benefit                    │
   └─────────────────────────────────────────────────────────────────┘
   ```

2. **Task Difficulty Dimensions:**
   | Dimension | Low Difficulty | High Difficulty |
   |-----------|----------------|-----------------|
   | Reasoning steps | Single inference | Multi-step chain |
   | Context length | Short, focused | Long, complex |
   | Domain knowledge | Common patterns | Specialized domain |
   | Ambiguity | Fully specified | Underspecified |
   | Tool coordination | Single tool | Multiple tools in sequence |
   | Long-horizon planning | Immediate | Extended temporal scope |
   | Error tolerance | Forgiving | Strict |
   | Integration complexity | Isolated | Many dependencies |

3. **ZPD-Calibrated Decomposition:**
   - **Below ZPD tasks:** Batch together, route to simpler agent, automate
   - **Within ZPD tasks:** Assign with appropriate scaffolding
   - **Above ZPD tasks:** Decompose until subtasks are within ZPD

   If decomposition can't bring tasks within ZPD: escalate to human.

4. **Scaffolding Response Curves:**
   ```
   Task type A:
     No scaffolding: 30% → Light: 70% → Heavy: 90%
     → Strong scaffolding response, within ZPD

   Task type B:
     No scaffolding: 20% → Light: 25% → Heavy: 30%
     → Weak scaffolding response, likely above ZPD

   Task type C:
     No scaffolding: 95% → Light: 95% → Heavy: 95%
     → No scaffolding response, below ZPD
   ```

**When It Works, When It Fails:**
- Works when ZPD boundaries are measurable
- Works when scaffolding can be calibrated to need
- Fails when ZPD boundaries are unstable or unknown
- Fails when scaffolding doesn't help (task above ZPD)
- Fails when task is inherently outside all agent ZPDs

**Scaling Characteristics:**
- Individual: Each agent has its own ZPD profile
- Collective: Multi-agent systems have collective ZPD exceeding individuals
- But: Coordination costs can reduce effective collective ZPD
- ZPD expands over time with capability development (for learning systems)

**Key Takeaways for Agents:**
- ZPD is relational: Not fixed agent property but agent-task-support interaction
- Match scaffolding to zone: Too much below ZPD, too little above ZPD
- Track scaffolding response: How much does support improve success?
- Decompose to within ZPD: If task is above, break until subtasks are within
- Route to appropriate capability: Simple tasks to simple agents

---

### Perspective 5: Station-Based Specialization (Kitchen Brigade)

**Core Insight:**
Station-based specialization reveals that agent boundaries should emerge from **constraint convergence**---where capability, data domain, technique clusters, timing profiles, and security requirements naturally align---rather than arbitrary assignment. Natural boundaries are obvious, stable, and self-enforcing.

**Mechanisms and How It Works:**

1. **Constraint Convergence Analysis:**

   | Constraint Type | Questions to Ask |
   |-----------------|-----------------|
   | **Capability** | What tools does this need? APIs? Permissions? |
   | **Data Domain** | What data to access? Own vs. read-only vs. excluded? |
   | **Technique Cluster** | What reasoning patterns? Prompt strategies? |
   | **Timing Profile** | Fast-response? Deliberative? Batch? |
   | **Security** | What isolation? Audit? Approval gates? |

   Where constraints converge, you've found a natural task boundary and agent assignment.

2. **Station Definition Pattern:**
   ```markdown
   ## Agent: [Name]

   **Capability Constraints:**
   - Tools: [List]
   - Permissions: [File access, API access]
   - Resources: [Memory, compute, rate limits]

   **Data Domain:**
   - Owns (read/write): [Files, directories]
   - Reads (read-only): [Reference data]
   - Cannot access: [Explicitly excluded]

   **Technique Cluster:**
   - Primary techniques: [Reasoning patterns]
   - Validation methods: [Self-verification]

   **Interface Contract:**
   - Inputs: [Type, description, validation]
   - Outputs: [Type, description, guarantees]
   ```

3. **Assignment Strategies:**
   - **Specialist assignment:** Task clearly within one station's constraints
   - **Tournant (swing) assignment:** Task outside defined boundaries, generalist fallback
   - **Multi-station coordination:** Complex task requiring orchestrated specialists

4. **Handoff Patterns:**
   - Explicit interface contracts between stations
   - Quality verification at boundaries (the "pass")
   - Orchestrator manages multi-station work

**When It Works, When It Fails:**
- Works when constraint convergence creates clear boundaries
- Works when work volume justifies specialization
- Fails when boundaries are arbitrary (need constant policing)
- Fails when tasks span multiple domains without clear handoffs
- Fails when specialization overhead exceeds efficiency gains

**Scaling Characteristics:**
- Small: 3-5 specialists + tournant sufficient
- Medium: Add stations as recurring patterns emerge
- Large: Sub-specialize (e.g., "code" splits to "frontend" + "backend" + "test")
- Each specialization adds coordination overhead---justify it

**Key Takeaways for Agents:**
- Discover boundaries through constraint analysis: Don't assign arbitrarily
- Include generalist capacity: Pure specialization is brittle (tournant pattern)
- Define clear interfaces: Integration only works with explicit contracts
- Accept that some tasks span boundaries: Orchestrator coordinates these
- Specialize incrementally: Start broad, split when warranted by evidence

---

### Perspective 6: Hierarchical Delegation (Film Production)

**Core Insight:**
Hierarchical delegation demonstrates that **scale is enabled by structure, not hindered by it**. The largest, most complex productions use the deepest hierarchies because that's what makes them possible. Delegation creates leverage through parallel specialization while maintaining coherent purpose via vision-method separation at each level.

**Mechanisms and How It Works:**

1. **Vision-Method Separation:**
   At each level, specifier defines WHAT (vision), delegate decides HOW (method).

   | Level | Specifies | Delegates |
   |-------|-----------|-----------|
   | Primary Agent | What success looks like, constraints, priorities | How to achieve it |
   | Domain Sub-Agent | Domain-specific success criteria | Implementation methods |
   | Task Agent | Executes with appropriate methods | Nothing (terminal) |

   **Bad delegation (over-specification):**
   ```
   "Use BeautifulSoup to scrape this website,
   extract product names with regex pattern r'...',
   store in SQLite database named products.db"
   ```

   **Good delegation (vision-method separation):**
   ```
   "Extract all product information from this e-commerce website.
   Success criteria: Name, price, description, availability for each.
   Store results for later querying.
   Constraint: Complete within 1000 API calls."
   ```

   The second form enables sub-agent expertise. The sub-agent might know there's an undocumented JSON API faster than scraping.

2. **Three-Dimensional Authority Space:**
   - **Goal Dimension:** Primary defines objective, sub-agents interpret for domain, task agents receive specific tasks
   - **Method Dimension:** Primary specifies WHAT not HOW; sub-agents have full method autonomy
   - **Resource Dimension:** Hard limits flow down; consumption tracked against budget

3. **Hierarchy Depth Formula:**
   ```
   Required depth = ceil(log_7(total_agents))

   Examples:
   - 5 agents: 1 level
   - 20 agents: 2 levels
   - 100 agents: 3 levels
   - 500 agents: 4 levels
   ```

   Primary agent should coordinate no more than 8 direct sub-agents. When more needed, add hierarchy level.

4. **Second Unit Pattern (Sub-Orchestration):**
   For complex sub-problems, delegate to sub-orchestrators:
   - Primary defines intent, success criteria, resource budget, interface
   - Sub-orchestrator manages decomposition, sub-agent spawning, coordination, result aggregation
   - Primary reviews final output, not intermediate steps

   This enables: Primary → 5 sub-orchestrators → 5 task agents each = 25 agents with primary span of 5.

5. **Pre-Execution Alignment:**
   Before spawning sub-agents, invest in alignment:
   - Goal decomposed into sub-goals (one per sub-agent)
   - Dependencies mapped (which sub-goals block which)
   - Interface contracts defined
   - Resource allocation determined
   - Success criteria specified

   Pre-execution alignment is expensive but predictable. Execution without alignment creates unpredictable coordination costs.

**When It Works, When It Fails:**
- Works when coordination complexity justifies hierarchy investment
- Works when vision can be communicated without loss of intent
- Fails when hierarchy depth exceeds intent propagation fidelity
- Fails when sub-agents can't interpret vision for their domain
- Fails when coordination latency exceeds task latency

**Scaling Characteristics:**
| Scale | Hierarchy Depth | Pattern |
|-------|-----------------|---------|
| Small (3-5) | 2 levels | Primary → Task |
| Medium (10-30) | 3 levels | Primary → Domain → Task |
| Large (50-100) | 4 levels | Primary → Domain → Task + Coordination |
| Very Large (100+) | 5+ levels | Primary → Sub-orchestrators → Domain → Task |

**Key Takeaways for Agents:**
- Specify WHAT, delegate HOW: Enable sub-agent expertise
- Add hierarchy to prevent bottleneck: ~8 direct reports maximum
- Pre-plan before spawning: Front-load coordination decisions
- Use sub-orchestrators for complex domains: Fully delegated sub-problems
- Trust calibration matters: Progressive autonomy based on demonstrated performance

---

## Cross-Cutting Patterns

### What All Perspectives Agree On

1. **Decomposition must surface the implicit.**
   Every discipline recognizes that explicit tasks are insufficient:
   - Military: "Implied tasks must be identified through analysis"
   - Kitchen: "Constraint analysis reveals natural boundaries"
   - Film: "Pre-execution alignment surfaces hidden dependencies"
   - Pedagogy: "ZPD assessment reveals true task difficulty"

2. **Task-capability matching is essential.**
   Assignment must consider capability:
   - Military: "Essential tasks determine required capability"
   - Helper Agents: "6-dimension complexity routing"
   - Pedagogy: "ZPD-calibrated assignment"
   - Kitchen: "Constraint convergence defines who handles what"
   - Film: "Trust calibration for graduated autonomy"

3. **Dependencies constrain decomposition.**
   You can't decompose arbitrarily:
   - Military: "Specified → Implied → Essential depends on sequence"
   - MDMP: "Dependencies mapped before COA development"
   - Film: "Pre-execution dependency mapping"
   - Kitchen: "Interface contracts between stations"

4. **Granularity involves tradeoffs.**
   There's no "right" size---context determines:
   - Too large: Context overflow, no parallelism, recovery impossible
   - Too small: Coordination overhead, context thrashing, lost coherence
   - Optimal: "Fits in context window with working space"

5. **Hierarchical structure enables scale.**
   Flat coordination breaks at scale:
   - MDMP: "Battalion+ uses MDMP with staff; company uses TLP"
   - Film: "log_7(agents) determines required hierarchy depth"
   - Kitchen: "Regional coordinators for 9-25 agents"
   - Mission Control: "Domain orchestrators for 10+ agents"

6. **Pre-execution investment reduces runtime cost.**
   Front-load decomposition effort:
   - Military: "Mission analysis takes 30% of planning time"
   - Film: "Meetings prevent problems before they reach set"
   - Kitchen: "Mise en place before service"
   - All: "Pre-planning is cheaper than runtime coordination"

### Where Perspectives Diverge

1. **How Much Decomposition is Enough:**
   - **Military (thorough):** 17-19 substeps in mission analysis, ~30% of time
   - **Lean/Rapid (minimal):** RDSP prioritizes timely over optimal, single COA
   - **Film (adaptive):** Pre-production investment proportional to production scale

   **Why they diverge:** Stakes and time pressure differ. High-stakes, time-available favors thoroughness. Time-critical, recoverable favors speed.

2. **Centralized vs. Distributed Decomposition:**
   - **Military (centralized):** Commander owns mission analysis; staff supports
   - **Kitchen (distributed):** Each station owns their prep; expediter coordinates
   - **Film (hierarchical):** Department heads decompose within their domain

   **Why they diverge:** Authority structure and expertise distribution differ. Centralized works when single authority has complete view. Distributed works when domain expertise is distributed.

3. **Static vs. Dynamic Assignment:**
   - **Kitchen (static):** Stations are persistent; tasks route to stations
   - **Film (project):** Team assembled per project; roles assigned at start
   - **Pedagogy (adaptive):** Assignment adapts as capability changes

   **Why they diverge:** Stability of agent pool differs. Persistent agents favor static assignment. Ephemeral agents favor dynamic.

4. **Depth of Decomposition:**
   - **Military:** Decompose to essential tasks (mission-success level)
   - **Kitchen:** Decompose to station boundaries (specialist level)
   - **Film:** Decompose to individual shots/tasks (atomic level)
   - **MDMP:** Decompose to COA-sufficient level (planning level)

   **Why they diverge:** Purpose of decomposition differs. Execution needs atomics; planning needs COA-level; coordination needs boundaries.

### Synthesis: A Unified Framework

**The Decomposition Triad:**

```
               GRANULARITY
                    |
           (How small to break)
                    |
  CAPABILITY ------+------ DEPENDENCIES
       |                        |
  (Who can do it)        (What blocks what)
       |                        |
  (Matching)              (Sequencing)
```

**Granularity (How Small):**
- Lower bound: Meaningful unit with clear success criteria
- Upper bound: Fits in agent context window with working space
- Tradeoff: Smaller = more handoffs; larger = less parallelism
- Rule of thumb: If task can fail at multiple independent points, it's too large

**Capability (Who Does It):**
- Assess task complexity (6 dimensions or similar)
- Match to agent capability (model tier, domain expertise)
- Consider ZPD: Achievable with scaffolding but stretching
- Include generalist capacity for boundary-spanning work

**Dependencies (What Order):**
- Map before assigning (blocking relationships)
- Critical path determines minimum time
- Independent tasks enable parallelism
- Circular dependencies must be broken

---

## Scaling Analysis

### Small Scale (3-10 Agents)

**What Works:**
- Single orchestrator can decompose and assign directly
- Flat coordination viable
- Dependencies simple enough to track mentally
- Full deliberate decomposition affordable

**Patterns:**
- Mission analysis lite: Specified + key implied tasks
- Direct assignment: Orchestrator assigns each task
- Simple dependency tracking: List or simple DAG
- All-in-one orchestrator: Decomposition + assignment + coordination

**Metrics:**
- Decomposition time < 20% of total execution time
- Task-agent match success > 80% first try
- Dependency violations < 5%

### Medium Scale (10-50 Agents)

**What Changes:**
- Single orchestrator approaches capacity limit
- Dependencies become complex (DAG not list)
- Need hierarchical decomposition
- Specialization boundaries become important

**Patterns:**
- Domain-level decomposition: Orchestrator breaks to domains; domain leads break further
- Constraint-converged assignment: Natural boundaries guide assignment
- Parallel planning: Domains decompose simultaneously with coordination
- Pre-execution alignment: Invest more in dependency mapping

**Transition Triggers:**
- Orchestrator context > 70% utilization
- Dependency tracking errors increasing
- Re-assignment rate > 20%

**Metrics:**
- Per-domain decomposition independent
- Cross-domain dependencies explicitly mapped
- Assignment success > 75% first try

### Large Scale (50-1000+ Agents)

**What Changes:**
- Multi-level hierarchy mandatory
- Domain orchestrators own their decomposition
- Primary orchestrator focuses on domain boundaries and cross-domain dependencies
- Sub-orchestration pattern for complex domains

**Patterns:**
- Hierarchical decomposition: Primary → Domain → Task levels
- Parallel domain decomposition: Domains work independently
- Vision-method separation at each level: What vs. How
- Second unit pattern: Fully delegated sub-orchestration

**Transition Triggers:**
- Single domain has > 20 agents
- Cross-domain dependencies dominate
- Coordination latency exceeds task latency

**Metrics:**
- Hierarchy depth = ceil(log_7(agents))
- Domain autonomy: < 20% decisions require primary
- Intent fidelity: Sub-agent understanding matches primary intent > 90%

### What Changes and Why at Each Transition

| Transition | Problem | Solution |
|------------|---------|----------|
| 3-10 to 10-50 | Orchestrator overload | Add domain level; parallel planning |
| 10-50 to 50+ | Domain complexity | Sub-orchestrators; hierarchy deepens |
| 50+ to 1000+ | Cross-domain coordination | Federated structure; vision-method separation critical |

---

## Decision Framework

### When to Use Which Decomposition Approach

**Thoroughness vs. Speed:**
| Use Thorough (Military/MDMP) When | Use Rapid (RDSP/Abbreviated) When |
|-----------------------------------|-----------------------------------|
| High stakes, errors costly | Low stakes, recoverable |
| Time available | Time constrained |
| Novel situation | Familiar pattern |
| Multiple valid approaches | Single obvious approach |
| Complex dependencies | Simple/linear dependencies |

**Hierarchical vs. Flat:**
| Use Hierarchical When | Use Flat When |
|----------------------|---------------|
| > 8 agents needed | < 8 agents |
| Multi-domain expertise required | Single domain |
| Complex dependencies | Simple dependencies |
| Scale expected to grow | Scale fixed/small |

**Static vs. Dynamic Assignment:**
| Use Static (Station) When | Use Dynamic (Project) When |
|---------------------------|---------------------------|
| Work types predictable | Work types vary |
| Agents persist across tasks | Agents are ephemeral |
| Specialization depth valuable | Flexibility more valuable |
| Volume justifies specialization | Volume low/variable |

### Context Factors That Drive Choices

1. **Task Complexity:** How complex is the original goal?
   - High complexity → More thorough decomposition, more levels
   - Low complexity → Simpler decomposition, flatter structure

2. **Time Pressure:** How much time is available?
   - High pressure → Abbreviated process, single COA
   - Low pressure → Full process, multiple options compared

3. **Consequence Severity:** What if decomposition is wrong?
   - High stakes → More validation, human review of decomposition
   - Low stakes → Faster, accept some rework

4. **Agent Capability Variance:** How different are available agents?
   - High variance → More careful matching, complexity assessment
   - Low variance → Simpler assignment, any qualified agent

5. **Dependency Complexity:** How interrelated are tasks?
   - High dependencies → More dependency mapping, sequencing care
   - Low dependencies → Parallel assignment, simple coordination

### Decision Matrix

| Context | Decomposition Approach |
|---------|----------------------|
| High stakes + time available | Full mission analysis with COA comparison |
| High stakes + time constrained | Abbreviated MDMP with directed COA |
| Low stakes + novel | Moderate analysis, test decomposition |
| Low stakes + familiar | Rapid decomposition from pattern |
| Many agents + domain diversity | Hierarchical with domain sub-orchestrators |
| Few agents + homogeneous | Flat direct assignment |
| High dependency complexity | Thorough dependency mapping, sequential-heavy |
| Low dependencies | Maximize parallelism, simple coordination |

---

## Implementation Checklist

### Phase 1: Task Understanding

- [ ] Identify specified tasks (explicitly stated requirements)
- [ ] Surface implied tasks (dependencies, prerequisites, domain requirements)
- [ ] Determine essential tasks (which define success vs. supporting)
- [ ] Identify constraints (must do) and restrictions (must not do)
- [ ] Document assumptions and their risk levels
- [ ] Formulate restated understanding (5 Ws)

### Phase 2: Complexity Assessment

- [ ] Score task complexity (novelty, ambiguity, depth, integration, abstraction, stakes)
- [ ] Map to agent capability thresholds
- [ ] Identify tasks above current capability (need decomposition or escalation)
- [ ] Identify tasks below capability (batch or route to simpler agent)
- [ ] Assess scaffolding requirements for ZPD-boundary tasks

### Phase 3: Decomposition

- [ ] Break tasks above threshold into subtasks within capability
- [ ] Validate each subtask has clear success criteria
- [ ] Ensure subtasks are independently completable
- [ ] Map dependencies between subtasks
- [ ] Identify critical path and parallelization opportunities
- [ ] Validate total subtasks achievable with available resources

### Phase 4: Assignment

- [ ] Analyze constraint convergence for natural assignment
- [ ] Match tasks to agents by capability profile
- [ ] Respect dependencies in assignment sequence
- [ ] Ensure no agent overloaded while others idle
- [ ] Define interfaces between agents for handoffs
- [ ] Identify tournant/fallback for boundary-spanning work

### Phase 5: Hierarchy (If Scale Requires)

- [ ] Determine hierarchy depth needed: ceil(log_7(agents))
- [ ] Define domain boundaries for domain sub-orchestrators
- [ ] Establish vision-method separation at each level
- [ ] Create pre-execution alignment protocol
- [ ] Define escalation and approval thresholds
- [ ] Plan for sub-orchestrator autonomy limits

### Success Criteria

- Task completion rate > 80% first try
- Dependency violation rate < 5%
- Context utilization 40-80% (not starved, not overflowed)
- Coordination overhead < 25% of total execution
- Escalation rate 10-25% (not too autonomous, not too dependent)

---

## Failure Mode Taxonomy

### Decomposition Failures

| Failure Mode | Root Cause | Symptoms | Detection | Recovery |
|--------------|------------|----------|-----------|----------|
| **Missing implied tasks** | Insufficient analysis | Execution blocks on unmet prerequisites | "Can't proceed, X not done" | Re-analyze for implied tasks |
| **Over-decomposition** | Excessive fragmentation | Coordination overhead dominates | >40% time in coordination | Consolidate related tasks |
| **Under-decomposition** | Insufficient breakdown | Context overflow, compound errors | Task failures at random points | Break further, establish checkpoints |
| **Wrong granularity** | Mismatched to capability | High failure rate on "simple" tasks | Capability-task mismatch | Re-assess complexity, re-route |
| **Ignored dependencies** | Incomplete analysis | Out-of-order execution | Agent working on blocked task | Map dependencies before assignment |
| **Assumption failure** | Unvalidated inference | Plan invalidated by reality | Assumed state doesn't exist | Explicit assumption tracking, validation |

### Assignment Failures

| Failure Mode | Root Cause | Symptoms | Detection | Recovery |
|--------------|------------|----------|-----------|----------|
| **Capability mismatch** | Wrong complexity assessment | Quality failures or wasted capacity | High error rate or low utilization | Recalibrate complexity assessment |
| **Boundary collision** | Overlapping assignments | Multiple agents modify same state | Conflict detection | Explicit boundary documentation |
| **Orphan tasks** | Tasks outside all boundaries | Tasks never picked up | Timeout with no agent claim | Tournant activation, boundary expansion |
| **Dependency violation** | Assignment before prerequisites | Agent can't proceed | Blocks immediately after start | Dependency graph validation |
| **Load imbalance** | Uneven distribution | Some agents overwhelmed, others idle | Utilization metrics | Rebalance or scale |

### Hierarchy Failures

| Failure Mode | Root Cause | Symptoms | Detection | Recovery |
|--------------|------------|----------|-----------|----------|
| **Intent degradation** | Too many hierarchy levels | Sub-agents misunderstand goal | Output doesn't match intent | Flatten hierarchy, improve communication |
| **Over-specification** | Primary dictates HOW | Sub-agent expertise not leveraged | Sub-agent asks about methods | Vision-method separation |
| **Under-specification** | Insufficient vision clarity | Sub-agents diverge | Conflicting sub-agent outputs | Clearer vision, explicit criteria |
| **Bottleneck at level** | Insufficient hierarchy depth | Queue depth at orchestrator | Growing backlog | Add hierarchy level |
| **Coordination overhead** | Excessive hierarchy depth | More time coordinating than executing | High % overhead | Flatten where possible |

### Diagnostic Decision Tree

```
SYMPTOM: Task decomposition/assignment problem

CHECK: Are tasks completing successfully?
  NO → CHECK: Where are tasks failing?
    At start → Dependency or prerequisite issue
      - Verify dependencies mapped
      - Check for missing implied tasks
    Mid-execution → Capability or granularity issue
      - Reassess complexity
      - Check for over/under decomposition
    At integration → Handoff or interface issue
      - Verify interface contracts
      - Check boundary definitions

  YES → CHECK: Is efficiency acceptable?
    NO → CHECK: What's consuming time?
      Coordination → Too much decomposition or hierarchy
        - Consolidate tasks
        - Flatten hierarchy where possible
      Waiting → Dependency or sequencing issue
        - Find parallelization opportunities
        - Rebalance load
      Rework → Quality or capability issue
        - Improve task-capability matching
        - Add scaffolding or checkpoints

    YES → System performing well, maintain
```

---

## Anti-Patterns

### Anti-Pattern 1: Decompose by Convenience, Not Constraint

**What it looks like:**
- Tasks broken by whoever thought of them first
- Assignments based on "who's available"
- No analysis of natural boundaries or capability match
- "Just split it in half"

**Why it's tempting:**
- Faster to start
- Avoids analysis effort
- Feels pragmatic

**Why it fails:**
- Boundaries require constant policing
- Wrong agents get wrong tasks
- Integration fails at arbitrary boundaries
- No basis for improving decomposition

**What to do instead:**
- Analyze constraint convergence before assigning
- Match task complexity to agent capability
- Let natural boundaries guide decomposition
- Document and refine boundaries based on outcomes

### Anti-Pattern 2: Specify Methods, Not Vision

**What it looks like:**
- Task descriptions include implementation details
- "Use this library, this pattern, this approach"
- Sub-agents can't exercise expertise
- All decisions flow through primary

**Why it's tempting:**
- Feels like maintaining control
- Reduces uncertainty
- Primary knows one way that works

**Why it fails:**
- Sub-agent expertise unused
- Worse approaches imposed
- Primary becomes bottleneck
- Scale limited by primary knowledge

**What to do instead:**
- Specify WHAT success looks like, not HOW
- Provide constraints and criteria, not methods
- Let specialists select methods within their domain
- Review outcomes, not approaches

### Anti-Pattern 3: Flat at Scale

**What it looks like:**
- 20+ agents all coordinated by one orchestrator
- No domain boundaries or hierarchy
- Every task assigned directly from top
- O(n) assignments per decision

**Why it's tempting:**
- Simpler conceptually
- No hierarchy design effort
- All information at one point

**Why it fails:**
- Orchestrator becomes bottleneck
- Context window saturates
- Assignment time grows linearly
- No domain expertise in decomposition

**What to do instead:**
- Add hierarchy when approaching ~8 direct reports
- Define domain boundaries
- Let domain sub-orchestrators decompose within domain
- Primary focuses on cross-domain coordination

### Anti-Pattern 4: Skip Dependency Mapping

**What it looks like:**
- Tasks assigned without dependency analysis
- "Just work on it and we'll figure it out"
- Agents discover blocks during execution
- Lots of waiting and re-coordination

**Why it's tempting:**
- Faster to start
- Dependency analysis is work
- "Dependencies will be obvious"

**Why it fails:**
- Agents start blocked tasks
- Wasted parallel effort
- Integration requires restart
- Can't identify critical path

**What to do instead:**
- Map dependencies before assignment
- Identify critical path
- Assign in dependency order
- Parallelize only independent tasks

### Anti-Pattern 5: One-Size-Fits-All Granularity

**What it looks like:**
- All tasks broken to same size
- "Each task should take about 10 minutes"
- No consideration of task-specific factors
- Simple and complex treated same

**Why it's tempting:**
- Predictable task units
- Easier planning
- Simpler load balancing

**Why it fails:**
- Simple tasks over-decomposed (coordination overhead)
- Complex tasks under-decomposed (context overflow)
- Capability not matched
- Some agents starved, some overwhelmed

**What to do instead:**
- Size tasks by complexity and capability match
- Let simple tasks stay simple
- Break complex tasks until within capability
- Accept variance in task size

---

## Key Insights

### Insight 1: Surface the Implicit Before Decomposing

Much of what needs to be done isn't stated. Implied tasks---the prerequisites, dependencies, and domain requirements that analysis reveals---often dominate actual work. Decomposition that only addresses specified tasks is incomplete.

**The test:** "Can each task succeed independently, or does it depend on something not yet identified?"

### Insight 2: Match Task Complexity to Agent Capability

Don't assign Opus-tier tasks to Haiku-tier agents (quality failures) or Haiku-tier tasks to Opus-tier agents (wasted capacity). Systematic complexity assessment enables appropriate matching. When a task exceeds available capability, decompose until subtasks fit.

**The test:** "Is this task within the assignee's ZPD---achievable with scaffolding but stretching?"

### Insight 3: Dependencies Constrain Decomposition More Than Preferences

You can't decompose however you want and then map dependencies. Dependencies emerge from the work itself. Ignoring them means agents block, parallelize incorrectly, or produce incoherent results.

**The test:** "If I assign these tasks in parallel, will any block on another?"

### Insight 4: Natural Boundaries Beat Arbitrary Ones

Boundaries that emerge from constraint convergence---where capability, data domain, technique, timing, and security requirements align---are obvious, stable, and self-enforcing. Arbitrary boundaries require constant policing and create integration problems.

**The test:** "Would this assignment still make sense to someone who didn't know our organizational history?"

### Insight 5: Specify Vision, Not Methods

At each level, the assigner specifies WHAT success looks like; the assignee decides HOW. This enables sub-agent expertise, reduces bottlenecks, and improves outcomes. Over-specification wastes the value of having specialized agents.

**The test:** "Am I telling them what to achieve, or how to achieve it?"

### Insight 6: Hierarchy Enables Scale

Flat coordination works for small agent counts but breaks around 8-10 direct reports. Adding hierarchy---domain sub-orchestrators, sub-orchestrators for complex domains---enables scale while maintaining coordination. Each level filters and transforms rather than passing everything through.

**The test:** "Does my primary orchestrator have more than 8 direct coordination relationships?"

### Insight 7: Pre-Execution Investment Reduces Runtime Cost

Thorough decomposition and alignment before execution is expensive but predictable. Execution without alignment creates unpredictable coordination costs, rework, and failure. The military spends ~30% of planning time on mission analysis for good reason.

**The test:** "Have I invested enough in understanding before assigning?"

### Insight 8: Include Generalist Capacity

Pure specialization is brittle. Tasks outside defined boundaries have no owner. The tournant pattern---a generalist agent that can cover boundary-spanning work and overflow---provides essential resilience.

**The test:** "If a task doesn't fit any specialist, who handles it?"

### Insight 9: Decomposition Approach Should Match Context

Full mission analysis isn't always warranted; abbreviated planning isn't always sufficient. Stakes, time pressure, novelty, and capability variance determine appropriate decomposition depth. Know when to be thorough and when to be fast.

**The test:** "Given what's at stake and the time available, is this the right level of decomposition effort?"

### Insight 10: Track and Calibrate

Decomposition and assignment are skills that improve with feedback. Track success rates, failure modes, and patterns. Calibrate complexity thresholds, assignment strategies, and hierarchy depth based on outcomes. Static rules become stale.

**The test:** "What have I learned from recent decomposition outcomes that should change my approach?"

---

## Related Problems

### Task Decomposition Connects To:

**Information Flow:**
- Decomposition creates information boundaries (who needs to know what)
- Handoffs between tasks require information transfer
- Dependencies require state sharing mechanisms

**Coordination Without Communication:**
- Good decomposition reduces communication needs
- Clear boundaries enable implicit coordination
- Shared understanding of decomposition enables autonomous execution

**Conflict Management:**
- Boundary clarity prevents assignment conflicts
- Dependency mapping prevents resource contention
- Clear ownership reduces territorial disputes

**Temporal Coordination:**
- Dependencies determine sequencing
- Parallel tasks require synchronization
- Critical path determines minimum time

**Scaling Coordination:**
- Decomposition hierarchy is coordination hierarchy
- Hierarchy depth determined by scale
- Domain boundaries become coordination boundaries

### Problem Dependency Order

1. **Task Decomposition first:** Can't coordinate what you haven't decomposed
2. **Then Assignment:** Tasks must exist before agents can be assigned
3. **Then Information Flow:** Information needs emerge from task structure
4. **Then Temporal Coordination:** Timing depends on task dependencies
5. **Then Scaling:** Scale solutions build on decomposition structure

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Cross-disciplinary synthesis for multi-agent coordination research
**Status:** Complete

---

## Source Documents

### Primary Sources (6 Perspectives)

1. **Mission Analysis** (Military Planning)
   - `/docs/military-planning/mission-analysis.md`
   - Focus: Specified/implied/essential tasks, constraints, assumption management

2. **Military Decision Making Process (MDMP)** (Military Planning)
   - `/docs/military-planning/mdmp.md`
   - Focus: Structured planning process, time management, running estimates

3. **Task Complexity Assessment** (Helper Agents)
   - `/docs/helper-agents/task-complexity-assessment.md`
   - Focus: 6-dimension complexity scoring, capability-based routing

4. **Zone of Proximal Development** (Pedagogy)
   - `/docs/pedagogy/zone-of-proximal-development-agent-analysis.md`
   - Focus: ZPD-calibrated assignment, scaffolding, capability matching

5. **Station-Based Specialization** (Kitchen Brigade)
   - `/docs/kitchen-brigade/station-based-specialization-agent-analysis.md`
   - Focus: Constraint convergence, natural boundaries, tournant pattern

6. **Hierarchical Delegation** (Film Production)
   - `/docs/film-production/hierarchical-delegation-agent-analysis.md`
   - Focus: Vision-method separation, hierarchy depth, sub-orchestration

### Note on Coverage

The problem-research mapping listed 7 perspectives including "Scaffolding (Pedagogy)" which did not exist as a separate document. The ZPD document incorporates scaffolding concepts extensively, so the synthesis draws on 6 source documents covering all substantive perspectives.

### Cross-References

- Problem mapping: `/.claude/problem-research-mapping.md`
- Phase 2 context: `/.claude/context.md`
- Related synthesis: `/docs/syntheses/information-flow-synthesis.md`
