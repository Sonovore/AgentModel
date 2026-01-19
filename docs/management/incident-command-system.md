# Incident Command System for Multi-Agent Coordination

Exploring how ICS principles apply to scaling AI agent coordination.

## Human Practice

| Aspect | Description |
|--------|-------------|
| **Domain** | Emergency response (FEMA, fire services, disaster management) |
| **Purpose** | Scalable, modular command structure for multi-agency incidents |
| **Core Insight** | Expand by adding modules, not by reorganizing |
| **Used For** | Wildfires, disasters, large events, any multi-agency response |
| **Scale** | 1 person to thousands, same structure |

## ICS Core Principles

### 1. Span of Control (3-7 Subordinates)

**Human practice:** One supervisor manages 3-7 subordinates (optimal: 5). This is a hard cognitive limit, not a guideline.

**Why it exists:**
- Humans can't effectively track more than ~7 things at once
- Communication overhead grows non-linearly with team size
- Decision quality degrades with excessive reports

### 2. Modular Organization

**Human practice:** Add capacity by adding modules, not reorganizing. A Type 5 incident has one person. A Type 1 incident has full ICS structure. Same underlying organization, just expanded.

```
Type 5: IC handles everything
Type 4: IC + few helpers, informal
Type 3: IC + Section Chiefs (Ops, Planning, Logistics)
Type 2: Full structure, multiple branches
Type 1: Maximum expansion, potentially thousands
```

### 3. Unified Command

**Human practice:** Multiple agencies, one incident commander (or unified command team). Authority flows from a single point, even when multiple organizations are involved.

### 4. Management by Objectives

**Human practice:** Clear objectives flow down the chain. Each level translates high-level objectives into actionable goals for their subordinates.

### 5. Comprehensive Resource Management

**Human practice:** Track all resources - their type, capability, status (assigned, available, out-of-service), and location.

### 6. Integrated Communications

**Human practice:** Common terminology, interoperability. Everyone uses the same language and can communicate with anyone.

### 7. Chain of Command

**Human practice:** Clear reporting lines. Everyone knows who they report to.

### 8. Unity of Command

**Human practice:** Everyone reports to exactly one supervisor. No one has two bosses.

## ICS Organization Structure

```
                        Incident Commander
                               |
            +------------------+------------------+
            |                  |                  |
       Operations         Planning          Logistics        Finance/Admin
            |                  |                  |                |
       +----+----+        +----+----+       +----+----+       +----+----+
    Branches   Divisions  Resources Situation  Supply Service  Time  Procurement
       |                                          |
    +--+--+                                  +----+----+
  Divisions  Groups                      Communications  Medical
       |
    +--+--+
  Strike Teams  Task Forces  Single Resources
```

## Translation to Agent Coordination

### Span of Control: Coordinator-to-Agent Ratio

| ICS Principle | Agent Equivalent |
|---------------|------------------|
| 3-7 subordinates per supervisor | 3-7 subagents per coordinator |
| Optimal: 5 | Sweet spot: probably lower (3-4) |
| Exceeding span degrades quality | Exceeding span causes dropped context, conflicting instructions |

**Why the limit might be lower for agents:**

Human supervisors have:
- Intuition about subordinate state
- Non-verbal cues
- Shared physical context
- Long-term relationship memory

Agent coordinators lack these. Each subagent relationship is explicit, requiring context tokens and coordination overhead.

**Hypothesis:** Effective agent span of control is 3-4, not 5-7.

### What Happens When You Exceed Span of Control?

ICS response: Add another layer of management.

```
Before (overloaded):
   Coordinator
       |
  +--+--+--+--+--+--+--+--+
  A1 A2 A3 A4 A5 A6 A7 A8 A9

After (proper span):
           Coordinator
               |
       +-------+-------+
       |       |       |
    Lead-1  Lead-2  Lead-3
       |       |       |
    +--+--+ +--+--+ +--+--+
    A1 A2 A3 A4 A5 A6 A7 A8 A9
```

**Agent translation:**
- Don't spawn 10 subagents from one coordinator
- Spawn 2-3 intermediate coordinators, each managing 3-4 workers
- The depth costs tokens but prevents coordination collapse

### Modular Organization: Adding Capacity Without Reorganizing

**ICS approach:** The structure is always the same; you just activate more of it.

```
Small task:         Root Agent (does the work)

Medium task:        Root Orchestrator
                           |
                    +------+------+
                    |      |      |
                   A1     A2     A3

Large task:         Root Orchestrator
                           |
              +------------+------------+
              |            |            |
         Coordinator-1  Coordinator-2  Coordinator-3
              |            |            |
          +---+---+    +---+---+    +---+---+
          A1 A2 A3     A4 A5 A6     A7 A8 A9
```

**Agent modules (standard ICS sections, translated):**

| ICS Section | Agent Equivalent | Responsibility |
|-------------|------------------|----------------|
| **Operations** | Implementation Agents | Do the actual work (code, analysis, etc.) |
| **Planning** | Planning Agents | Break down tasks, assess requirements |
| **Logistics** | Infrastructure Agents | Manage resources, context, communication |
| **Finance/Admin** | (No direct equivalent) | Token tracking? Cost management? |

**Key insight:** Define standard agent "modules" that can be activated as needed. Don't redesign the structure for each project.

### Unified Command: Handling Multiple Principals

**ICS problem:** Fire department, police, EMT all arrive. Who's in charge?

**ICS solution:** Unified command - representatives from each agency form a command team. They present a single set of objectives to the organization below them.

**Agent problem:** Multiple "principals" (humans) give instructions. Or: multiple CLAUDE.md files, multiple context sources, conflicting guidance.

**Agent solutions:**

1. **Hierarchy of authority:**
   ```
   User instruction (highest)
       |
   Session context
       |
   CLAUDE.md
       |
   Model defaults (lowest)
   ```

2. **Conflict resolution protocol:**
   - Detect conflict
   - Escalate to human
   - Don't guess

3. **Multi-agent unified command:**
   - One designated root agent receives instructions
   - Root translates into consistent objectives
   - Subagents don't receive conflicting directives

**Anti-pattern:** Multiple humans each directly instructing different subagents. This violates unity of command.

### Management by Objectives: Objective Flow

**ICS approach:**

```
IC: "Contain fire to Building A, protect Building B, evacuate Sector 3"
    |
Operations Chief: "Division A - contain. Division B - protect. Division C - evacuate."
    |
Division Supervisor: "Task Force 1 - north flank. Task Force 2 - south flank."
    |
Task Force Leader: "Engine 1 - lay hose here. Engine 2 - ladder there."
```

**Agent translation:**

```
Human: "Add dark mode to the application"
    |
Orchestrator: "Agent 1 - create toggle component. Agent 2 - implement theme context.
               Agent 3 - update existing components. Agent 4 - run tests."
    |
Agent 2: "I need to create ThemeContext.tsx with dark/light state,
          export useTheme hook, integrate with existing AuthProvider."
```

**Objective detail by level:**

| Level | Objective Granularity | Example |
|-------|----------------------|---------|
| Human | Outcome | "Add dark mode" |
| Root Orchestrator | Features | "Toggle, Context, Styling, Integration" |
| Coordinator | Tasks | "Create ThemeContext with state and hook" |
| Worker Agent | Actions | "Write file, test import, verify type safety" |

**Key insight:** Each level translates, not just passes through. The translation adds specificity appropriate to that level's scope.

### Resource Tracking: Agent State Management

**ICS resource categories:**

| Status | Description |
|--------|-------------|
| Assigned | Working on a task |
| Available | Ready for assignment |
| Out-of-Service | Unavailable (broken, resting, etc.) |

**Agent equivalent:**

| Status | Agent Meaning |
|--------|---------------|
| Running | Context window active, working on task |
| Complete | Task finished, context available for review |
| Failed | Task failed, needs intervention |
| Pending | Queued but not started |
| Terminated | Context destroyed, no longer accessible |

**ICS resource tracking:**

- What resources do I have?
- Where are they?
- What are they doing?
- What can they do?

**Agent equivalent questions:**

- How many agents are active?
- What task is each working on?
- What's each agent's status?
- What capabilities does each agent have (model, tools, context)?

**Implementation:**

```
# status.json (managed by orchestrator)
{
  "agents": [
    {"id": "impl-1", "status": "running", "task": "theme-context", "started": "..."},
    {"id": "impl-2", "status": "complete", "task": "toggle-component", "result": "success"},
    {"id": "impl-3", "status": "failed", "task": "style-migration", "error": "timeout"}
  ],
  "summary": {"running": 1, "complete": 1, "failed": 1, "pending": 0}
}
```

### Integrated Communications: Common Terminology

**ICS approach:** All agencies use the same terminology. No jargon, no agency-specific codes.

**Agent translation:**

| ICS Concept | Agent Equivalent |
|-------------|------------------|
| Common terminology | Shared CLAUDE.md |
| Plain language | Explicit, unambiguous instructions |
| Radio protocols | Structured message formats |
| Communication plan | Defined handoff/reporting format |

**Shared CLAUDE.md as ICS "communications plan":**

```markdown
# Shared Agent Instructions (communications plan equivalent)

## Terminology
- "complete" means task succeeded and output verified
- "blocked" means cannot proceed without external input
- "failed" means attempted and hit unrecoverable error

## Reporting Format
Always report: status, summary, blockers, output location

## Escalation
Escalate immediately if: conflicting instructions, security concern, scope unclear
```

**Anti-pattern:** Each agent has different instructions, different terminology, incompatible output formats. Communication breaks down.

### Chain of Command and Unity of Command

**ICS rules:**
- Everyone reports to exactly one supervisor
- Chain should be followed (don't skip levels)
- Span of control maintained at every level

**Agent translation:**

```
GOOD:
   Orchestrator
       |
   Coordinator
       |
   Worker Agent

   Worker reports to Coordinator.
   Coordinator reports to Orchestrator.
   Human talks to Orchestrator.

BAD:
   Orchestrator
       |
   Coordinator ←------- Human (bypassing chain)
       |
   Worker Agent ←------ Human (bypassing two levels)
```

**Why this matters:**
- Coordinator doesn't know what Human told Worker
- Orchestrator's plan is now out of sync
- Conflicting instructions likely

**Exception:** Emergency stop / safety override can bypass chain.

## Scaling Patterns (ICS Type Classification)

ICS classifies incidents by complexity:

| Type | ICS Structure | Agent Equivalent |
|------|---------------|------------------|
| **Type 5** | IC handles all | Single agent, no coordination |
| **Type 4** | IC + few resources | Human + 1-2 agents, informal |
| **Type 3** | Multiple sections | Orchestrator + specialized agents |
| **Type 2** | Full ICS, extended duration | Full structure, multiple coordinators |
| **Type 1** | Maximum complexity | Many agents, layered coordination |

**When to scale up:**

| Signal | Action |
|--------|--------|
| Single agent can complete in one context | Stay Type 5 |
| Need multiple skills but small scope | Type 4 (informal) |
| Scope exceeds single context window | Type 3 (add structure) |
| Multiple concurrent workstreams | Type 2 (full coordination) |
| Massive scope, long duration | Type 1 (maximum structure) |

**When to scale down:**

| Signal | Action |
|--------|--------|
| Overhead exceeds value | Remove coordination layer |
| Single coordinator with one agent | Collapse to direct execution |
| Task complete, agents idle | Terminate unused agents |

## ICS Patterns That Translate Directly

### 1. Operational Periods

**ICS:** Work is organized into operational periods (usually 12-24 hours). At each period change: brief, plan, adjust.

**Agent translation:** Work is organized into context windows. At each context boundary: checkpoint, handoff, summarize.

### 2. Incident Action Plan (IAP)

**ICS:** Each operational period has a written plan: objectives, assignments, resources, communications.

**Agent translation:** Each major task gets a written plan:
- Objectives (what success looks like)
- Assignments (which agent does what)
- Resources (context, files, tools needed)
- Communications (handoff format, reporting cadence)

### 3. Check-In / Demobilization

**ICS:** Resources check in when arriving, check out when leaving. Status is always known.

**Agent translation:**
- Agent spawned: log to status file
- Agent completes: report results, log completion
- Agent fails: log failure, capture context
- No "silent" agent termination

### 4. After Action Review (AAR)

**ICS:** After the incident, review what worked and what didn't.

**Agent translation:** After task completion:
- What agents were used?
- What coordination patterns worked?
- Where did communication break down?
- What CLAUDE.md changes would help next time?

## ICS Patterns That Don't Translate Directly

### 1. Physical Co-location

ICS assumes the command post is a physical place where people can talk face-to-face.

**Agent reality:** Agents can't "walk over" to each other. All communication is explicit, through files or messages.

**Adaptation:** Over-communicate. What would be implicit in person must be explicit in files.

### 2. Human Judgment at Every Level

ICS relies on human judgment, intuition, and adaptation at every level of the hierarchy.

**Agent reality:** Agents follow instructions. They don't have intuition about "what the IC would want."

**Adaptation:** Instructions must be more explicit. Escalation criteria must be defined, not assumed.

### 3. Long-Term Relationships

ICS builds on relationships - trust developed over years of training and working together.

**Agent reality:** Each agent is a fresh context. No accumulated trust.

**Adaptation:** Trust must be encoded in CLAUDE.md and validated through structure, not assumed through relationship.

### 4. Informal Communication

ICS has formal channels but also relies heavily on informal communication ("Hey, did you hear about...").

**Agent reality:** There is no informal channel. All communication is explicit.

**Adaptation:** Build in structured "status sharing" that captures what would otherwise be informal.

## Implementation Recommendations

### 1. Define Standard Agent Modules

Just as ICS has standard sections (Ops, Planning, Logistics), define standard agent types:

```markdown
## Standard Modules

### Operations (Implementation)
- Code agents (write code)
- Test agents (verify code)
- Review agents (assess quality)

### Planning
- Decomposition agents (break down tasks)
- Assessment agents (evaluate requirements)

### Logistics
- Context agents (manage handoffs)
- Status agents (track progress)
```

### 2. Enforce Span of Control

**Hard rule:** No coordinator manages more than 5 agents.

**Implementation:**
```
# Before spawning
if active_subagents >= 5:
    spawn_intermediate_coordinator()
else:
    spawn_worker_agent()
```

### 3. Standardize Communications

**Create templates:**

```markdown
## Agent Status Report Template

**Agent ID:** [identifier]
**Task:** [what was assigned]
**Status:** [running|complete|failed|blocked]
**Summary:** [1-2 sentence summary]
**Output:** [file path or inline result]
**Blockers:** [none, or what's blocking]
**Next:** [what happens next, if known]
```

### 4. Implement Resource Tracking

**Central status file updated by all agents:**

```json
{
  "operational_period": "2024-01-18-session-1",
  "objectives": ["Implement dark mode feature"],
  "resources": {
    "active": [...],
    "complete": [...],
    "failed": [...]
  },
  "communications": {
    "last_update": "...",
    "escalations": [...]
  }
}
```

### 5. Define Escalation Triggers

**Explicit, not assumed:**

```markdown
## Escalation Criteria

Escalate to coordinator immediately if:
- Instructions conflict with each other
- Required file/resource is missing
- Task scope exceeds context window
- Security or safety concern
- Uncertainty about intent

Do NOT guess. Do NOT proceed with assumptions.
```

## Open Questions

1. **Optimal span of control for agents:** Is it really lower than humans? How do we measure this?

2. **Depth vs. breadth trade-off:** More layers = more coordination overhead but better span of control. What's the optimal depth?

3. **Dynamic scaling:** ICS scales up and down during an incident. How do agents add/remove coordination layers dynamically?

4. **Unified command for multiple humans:** What if two humans both have authority? How do agents handle this?

5. **Communication overhead:** ICS communication is cheap (talking). Agent communication costs tokens. How does this change optimal structure?

6. **Failure recovery:** ICS can reassign resources when something fails. How do agents handle mid-task coordinator failure?

7. **Institutional knowledge:** ICS benefits from repeated training and exercises. How do we "train" agent coordination patterns?

## Systems to Build

- [ ] **Span of control enforcer:** Refuse to spawn beyond limit, suggest structure
- [ ] **Status tracking system:** Central file for resource status
- [ ] **Objective cascade template:** How objectives flow from human to worker
- [ ] **Communication protocol:** Standard formats for all agent-to-agent communication
- [ ] **Escalation handler:** Recognize and route escalations
- [ ] **After action review template:** Capture coordination learnings

## The Core Insight

**ICS teaches:** Structure enables scale. Ad-hoc coordination works for small incidents but collapses at scale. Predefined, modular structure allows expansion without reorganization.

**Agent translation:** Multi-agent coordination needs structure, not just spawning. The structure should be:
- Predefined (not invented per-task)
- Modular (expand by adding modules)
- Span-limited (hard cap on supervisor-to-subordinate ratio)
- Communication-standardized (common terminology, common formats)

**The mistake to avoid:** Treating agent coordination as "spawn N agents and let them figure it out." ICS shows this fails. Structure must be explicit.

## Status

**Phase:** Exploration complete. ICS provides a mature framework for thinking about agent coordination at scale. The key principles (span of control, modular organization, unified command, management by objectives) translate well. The main adaptations needed are around explicit communication (no informal channels) and defined judgment (no intuition to fall back on).

**Priority applications:**
1. Span of control enforcement (immediate, high value)
2. Standard agent modules (enables scaling)
3. Communication protocols (prevents breakdown)
4. Resource tracking (visibility into system state)

