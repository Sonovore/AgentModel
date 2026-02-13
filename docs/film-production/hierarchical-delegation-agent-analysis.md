# Hierarchical Delegation: Architectural Analysis for AI Agent Systems

## Executive Summary

Hierarchical delegation in film production demonstrates how 1,000+ autonomous specialists can coordinate toward a unified creative vision under strict budget and time constraints. The core insight is not merely that work is distributed through a hierarchy, but that **delegation creates leverage through parallel specialization while maintaining coherent purpose**.

For AI agent systems, hierarchical delegation offers a proven framework for scaling agent coordination beyond what flat orchestration can achieve. The key architectural insight: **hierarchy depth prevents bottlenecks rather than creates them**, provided the hierarchy is structured around vision-method separation at each level.

| Film Production Pattern | Agent System Equivalent | Key Constraint |
|------------------------|------------------------|----------------|
| Director's creative vision | Primary agent's goal specification | Must be communicable without loss of intent |
| Department heads | Domain-specialized sub-agents | Must interpret vision for their domain |
| Crew leads | Task execution agents | Must implement without constant oversight |
| Producer's budget/schedule constraints | Resource allocation limits | Absolute constraints that shape all other decisions |
| Production coordinator | State management / message hub | Coordination infrastructure |
| Call sheet | Shared coordination document | Asynchronous synchronization mechanism |
| Second unit | Fully delegated sub-orchestration | Complete operational autonomy within intent boundaries |

**The central architectural claim:** Agent systems attempting to coordinate more than 8-10 parallel agents through flat orchestration will encounter bottlenecks. Film production patterns provide tested solutions for scaling to hundreds of coordinated specialists.

---

## Part I: Translating Film Production Delegation to Agent Systems

### The Core Mapping

Film production operates through two parallel hierarchies - creative and administrative. Agent systems have an analogous dual structure:

**Goal Hierarchy (Creative Equivalent):**
- Primary Agent: Overall goal specification and success criteria
- Domain Sub-Agents: Goal interpretation within specialty domains
- Task Agents: Specific task execution

**Resource Hierarchy (Administrative Equivalent):**
- Resource Allocation Agent: Budget constraints (tokens, compute, API calls)
- Coordination Agent: Scheduling and conflict resolution
- State Manager: Information routing and persistence

These hierarchies must operate simultaneously. A sub-agent receives goal direction from the primary agent while operating under resource constraints from the allocation layer.

### Vision-Method Separation

The most critical pattern for agent delegation is vision-method separation:

**Film Production Pattern:**
"A DP typically describes what they want from a creative viewpoint and may reference specific lights, but it's usually up to the gaffer to decide what lights to use and how."

**Agent System Translation:**
Primary agent describes desired output and may reference example approaches. Sub-agent autonomously selects specific tools, algorithms, or implementation methods.

| Level | Specifies | Delegates |
|-------|-----------|-----------|
| Primary Agent | What success looks like, constraints, priorities | How to achieve it |
| Domain Sub-Agent | Domain-specific success criteria, quality standards | Implementation methods |
| Task Agent | Executes with methods appropriate to task | Nothing (terminal node) |

**Example:**

Bad delegation (over-specification):
```
"Use BeautifulSoup to scrape this website,
extract product names with regex pattern r'<h2 class="product">(.+?)</h2>',
store in SQLite database named products.db"
```

Good delegation (vision-method separation):
```
"Extract all product information from this e-commerce website.
Success criteria: Name, price, description, availability for each product.
Store results for later querying.
Constraint: Complete within 1000 API calls."
```

The second form enables sub-agent expertise. The sub-agent might know that this particular site has an undocumented JSON API that's faster than scraping, or that Postgres is better suited than SQLite for the data volume.

### Three-Dimensional Authority Space

Film production delegates authority across three dimensions simultaneously. Agent systems should do the same:

**1. Goal Dimension (Creative Equivalent)**
- Primary Agent: Overall objective and success criteria
- Sub-Agent: Domain-specific sub-goals
- Task Agent: Task-level success criteria

**2. Method Dimension (Technical Equivalent)**
- Primary Agent: Specifies WHAT not HOW
- Sub-Agent: Full autonomy over methods within domain
- Task Agent: Implementation flexibility

**3. Resource Dimension (Budget Equivalent)**
- Resource Agent: Allocates compute budget
- Sub-Agent: Operates within allocated resources
- Task Agent: Consumes resources within sub-agent allocation

**CLAUDE.md Template for Authority Dimensions:**

```markdown
# Authority Boundaries

## Goal Authority
- Primary agent defines overall success criteria
- Sub-agents define domain-specific success criteria within primary scope
- Task agents do not define goals; they receive them

## Method Authority
- Sub-agents have FULL authority over implementation methods
- Primary agent does not dictate tools, algorithms, or approaches
- Primary agent may suggest approaches but sub-agent decides

## Resource Authority
- Hard limits are HARD - never exceed allocated resources
- Sub-agents may request additional resources through escalation
- Preemptive resource alerts when 80% consumed
```

---

## Part II: Where Agents Struggle vs. Excel

### Where Agents Excel (vs. Human Film Crews)

**1. Parallel Observation (100-1000x faster)**
Agents can read 50 files simultaneously while a human reads one. The observation phase is essentially free.

**Agent advantage:** In pre-production-equivalent activities (gathering requirements, mapping dependencies, identifying relevant code), agents dramatically outperform human crews.

**2. Action Execution (10-100x faster)**
Once decision is made, agents implement instantly. No typing errors, no fatigue.

**Agent advantage:** For well-specified tasks, agents execute far faster than human crews.

**3. Perfect Memory Within Context**
Agents don't forget what they read within a session. Every file read is available for reference.

**Agent advantage:** For tasks that fit within context window, agents maintain better working memory than humans.

**4. No Ego or Politics**
Agents don't defend wrong positions to save face. They don't have turf to protect.

**Agent advantage:** Delegation conflicts that plague human film crews (who owns this decision?) can be resolved cleanly through explicit authority specification.

### Where Agents Struggle (vs. Human Film Crews)

**1. Orientation / Mental Model Building (0.1-10x human speed, high variance)**
Humans build context through years of experience. Agents must rebuild from observation each session.

**Agent limitation:** Film department heads have internalized thousands of pattern-context mappings. Agents have CLAUDE.md and session context.

**Film Equivalent:** "Department heads should meet before production starts, matching successful studios like Disney/Pixar where the entire crew becomes adept at speaking and understanding each individual's needs."

This pre-production alignment that human crews can achieve through meetings and shared experience is difficult for agents to replicate. They must rebuild context each session.

**2. Trust Calibration**
Human film crews build trust through repeated collaboration. "Experienced directors received broad creative authority."

**Agent limitation:** How do you trust an agent? Previous session performance doesn't persist. The "experienced director" pattern doesn't translate directly.

**Mitigation:** Capability verification before delegation. Test agents on representative tasks before giving broad authority.

**3. Implicit Knowledge**
Human film crews share implicit knowledge through culture. A gaffer knows what a DP means by "warm lighting" without explicit specification.

**Agent limitation:** Everything must be explicit. "Warm lighting" in CLAUDE.md must be defined: "Warm lighting: Color temperature 2700-3200K, diffused sources, minimal harsh shadows."

**Mitigation:** Comprehensive CLAUDE.md that makes implicit knowledge explicit.

**4. Context Persistence Across Sessions**
A film crew carries context across days of production. They remember yesterday's decisions.

**Agent limitation:** Each session starts fresh. Context documents help but imperfectly capture nuanced state.

**Mitigation:** Explicit context handoff documents. Session summaries. State persistence infrastructure.

**5. Creative Judgment Under Ambiguity**
Film department heads make creative judgment calls when intent is unclear. The production designer interprets "old and spooky" into specific visual choices.

**Agent limitation:** Agents may interpret literally or request clarification for every ambiguity.

**Mitigation:** Rich examples in CLAUDE.md. Graduated autonomy based on verified capability.

---

## Part III: Bottleneck Identification

### The Primary Agent Bottleneck

**Film Production Pattern:**
"As productions scale up—especially with crowd scenes or multiple units—additional coordination roles like the 2nd 2nd AD help divide and conquer."

The director cannot directly coordinate 1,000 crew. They would become the bottleneck. The solution is hierarchy: director coordinates 8 department heads, each coordinates 8 crew leads, each coordinates 15 crew.

**Agent System Equivalent:**
A primary agent cannot directly coordinate 50 sub-agents. Every coordination message routes through the primary, creating queueing delays.

**Bottleneck Diagnosis:**
- Primary agent context filled with coordination overhead
- Sub-agent wait times increase with sub-agent count
- Primary agent spends more tokens on coordination than actual work
- Task completion rate plateaus as sub-agent count increases

**Solution from Film:**
Add coordination agents that handle routine coordination. Primary agent communicates intent; coordination agents handle scheduling and conflict resolution.

### The Approval Bottleneck

**Film Production Pattern:**
"When key employees are overloaded with approvals and decision-making, bottlenecks form and workflows significantly slow down."

If the director must approve every VFX shot iteration (500 shots x 3-5 iterations = 1,500-2,500 approvals), production extends by years.

**Solution from Film:**
Progressive delegation. VFX Supervisor approves iterations 1-3. Director only reviews when VFX Supervisor judges shot is ready.

**Agent System Equivalent:**
If primary agent must approve every sub-agent action:
```
Sub-agent completes task → waits for approval → Primary agent reviews → approves/rejects → Sub-agent continues
```

With 10 sub-agents each producing 5 outputs, that's 50 approval cycles. The primary agent becomes the limiting factor.

**Solution:**
1. **Confidence-based escalation:** Sub-agents proceed autonomously for high-confidence decisions; escalate low-confidence decisions
2. **Batch approval:** Primary agent reviews 10 outputs at once, not one at a time
3. **Peer review:** Sub-agents review each other before escalating to primary
4. **Domain delegation:** Domain sub-agents approve within their domain; primary only reviews cross-domain decisions

**CLAUDE.md Template for Approval Thresholds:**

```markdown
# Escalation Thresholds

## Proceed Autonomously (No Approval Needed)
- Confidence > 90% on approach
- Reversible actions (can be undone if wrong)
- Within allocated resources
- Consistent with documented patterns

## Request Approval Before Proceeding
- Confidence < 70% on approach
- Irreversible actions (data modification, external API calls)
- Resource usage > 50% of allocation
- Novel patterns not in documentation
- Cross-domain implications

## Immediate Escalation Required
- Confidence < 50%
- Potential safety/security implications
- Contradictory requirements detected
- Resource allocation would be exceeded
```

### The Information Aggregation Bottleneck

**Film Production Pattern:**
"The 1st AD aggregates information from all departments and provides overall production status."

The director doesn't receive individual task status from 1,000 crew. They receive aggregated status: "We're on schedule" or "Camera is 30 minutes behind."

**Agent System Equivalent:**
If primary agent receives full output from every task agent, context fills with detail.

```
Task Agent 1: [500 tokens of detail]
Task Agent 2: [500 tokens of detail]
...
Task Agent 50: [500 tokens of detail]
= 25,000 tokens of status, leaving minimal context for actual work
```

**Solution:**
Hierarchical aggregation. Domain sub-agents aggregate task agent outputs. Primary agent receives domain summaries.

```
Domain Sub-Agent A: "Search complete. Found 12 relevant files. Key findings: [3 bullet points]"
Domain Sub-Agent B: "Implementation complete. All tests passing."
Domain Sub-Agent C: "Documentation updated. 2 sections revised."
```

**Information Granularity by Level:**

| Recipient | Information Level | Example |
|-----------|------------------|---------|
| Primary Agent | Strategic summary | "Authentication refactor complete. Tests pass. Ready for review." |
| Domain Sub-Agent | Tactical detail | "Modified 4 files. Test coverage increased from 72% to 89%." |
| Task Agent | Full detail | "Line 47 in auth.ts: changed from callback to async/await." |

---

## Part IV: Optimization Patterns

### Pattern 1: Pre-Execution Alignment (Pre-Production Investment)

**Film Pattern:**
"Meetings give department heads the chance to flag problems before they reach set, as it's always cheaper and easier to fix an issue during prep than when the clock is ticking on a shoot day."

**Agent Implementation:**
Before spawning sub-agents, invest in alignment:

```markdown
## Pre-Delegation Checklist

Before delegating to sub-agents:

1. [ ] Goal decomposed into sub-goals (one per sub-agent)
2. [ ] Dependencies mapped (which sub-goals block which)
3. [ ] Interface contracts defined (how sub-agents communicate results)
4. [ ] Resource allocation determined (budget per sub-agent)
5. [ ] Success criteria specified (how to validate sub-agent output)
6. [ ] Shared state defined (what all sub-agents need access to)

Only spawn sub-agents when checklist complete.
```

**Why this works:**
Pre-execution alignment is expensive but predictable. Execution without alignment creates unpredictable coordination costs. Front-loading reduces total cost.

### Pattern 2: Asynchronous Coordination via Shared State

**Film Pattern:**
Call sheets distributed evening before filming. Each department reads their section and self-prepares without real-time coordination.

**Agent Implementation:**
Create coordination documents that sub-agents reference for self-synchronization:

```markdown
## Task Manifest (Equivalent to Call Sheet)

### Task: Authentication Refactor
**Status:** In Progress
**Dependencies:** None
**Blocks:** API Update, Documentation Update

### Assigned Sub-Agents:
- Auth Agent: Modifying auth.service.ts, auth.middleware.ts
- Test Agent: Updating auth.test.ts (WAIT for Auth Agent completion)
- Doc Agent: Updating auth.md (WAIT for Auth Agent completion)

### Interface Contract:
Auth Agent produces:
- Modified files with new async/await pattern
- List of exported function signature changes
- Migration notes for consumers

Test Agent expects:
- Stable auth.service.ts before writing tests
- Function signature list to validate coverage

### Shared State Location:
/state/auth-refactor.json
```

Sub-agents reference this document, update their status, and coordinate without message passing.

### Pattern 3: Domain Sub-Agent Architecture (Department Head Pattern)

**Film Pattern:**
Department heads interpret director's vision for their domain and manage their own hierarchies.

**Agent Implementation:**
Domain sub-agents own specific capability domains:

```markdown
## Domain Sub-Agent Architecture

### Code Agent (Domain: Code Modification)
- Receives: Task description, success criteria, constraints
- Owns: All code file modifications
- Manages: Syntax checking, style compliance, test execution
- Reports: Changes made, test results, confidence level

### Research Agent (Domain: Information Gathering)
- Receives: Questions, scope boundaries, depth requirements
- Owns: All observation operations (file reads, searches, web fetches)
- Manages: Source evaluation, relevance filtering, synthesis
- Reports: Findings summary, source citations, confidence level

### Review Agent (Domain: Verification)
- Receives: Artifacts to review, criteria
- Owns: All verification operations
- Manages: Test execution, style checking, security scanning
- Reports: Pass/fail, issues found, recommendations

Primary agent delegates to domain sub-agents by domain, not by file or task.
```

### Pattern 4: Second Unit Pattern (Full Operational Delegation)

**Film Pattern:**
"Directors may delegate the assembly of second unit photography to the Second Unit Director."

The second unit operates independently, guided by director's intent, returning completed work.

**Agent Implementation:**
For complex sub-problems, delegate to sub-orchestrators:

```markdown
## Sub-Orchestrator Pattern

For tasks requiring multiple coordinated steps:

1. Primary agent defines:
   - Overall intent (what should be accomplished)
   - Success criteria (how to validate)
   - Resource budget (hard limits)
   - Interface (expected output format)

2. Sub-orchestrator receives intent and manages:
   - Task decomposition
   - Sub-agent spawning
   - Coordination within sub-task
   - Result aggregation

3. Primary agent reviews:
   - Final output (not intermediate steps)
   - Resource consumption (within budget?)
   - Success criteria (met?)

Example: "Refactor authentication to use OAuth2"
- Sub-orchestrator breaks into: research, design, implement, test, document
- Sub-orchestrator manages 5 task agents
- Primary agent receives: refactored auth module, test results, documentation
```

This enables scaling. Primary agent coordinates 5 sub-orchestrators. Each sub-orchestrator coordinates 5 task agents. 25 agents coordinated with primary agent span of 5.

### Pattern 5: Progressive Trust Calibration

**Film Pattern:**
"Experienced directors received broad creative authority within budget parameters."

Trust earned through track record.

**Agent Implementation:**
Graduated autonomy based on verified performance:

```markdown
## Trust Levels

### Level 1: Training Wheels
- All outputs require explicit approval
- No resource allocation beyond minimum
- Used for: New agent types, novel domains, high-stakes tasks

### Level 2: Supervised Autonomy
- Routine outputs proceed without approval
- Escalate on low confidence
- Sample-based review (10% of outputs)
- Used for: Agents with some verified track record

### Level 3: Trusted Autonomy
- Full autonomy within defined boundaries
- Escalate only on boundary violations
- Exception-based review
- Used for: Agents with strong verified track record

### Trust Calibration:
- Track first-try success rate per agent type
- Promote after 10 consecutive successes
- Demote after 2 failures
- Domain-specific trust (agent may be Level 3 for code, Level 1 for docs)
```

### Pattern 6: Coordination Hub (Production Coordinator Pattern)

**Film Pattern:**
"Production coordinators must maintain clear communication with various departments and vendors to ensure production runs smoothly."

"Coordinators act as a central point of contact for cast, crew, vendors, and locations, reducing miscommunications and ensuring everyone is aligned."

**Agent Implementation:**
Dedicated coordination agent manages information flow:

```markdown
## Coordination Agent Responsibilities

### State Management
- Maintains canonical state document
- Resolves conflicting updates
- Provides consistent view to all sub-agents

### Message Routing
- Routes messages between sub-agents
- Filters redundant messages
- Escalates messages requiring primary agent attention

### Conflict Detection
- Monitors for resource conflicts
- Detects dependency violations
- Alerts on coordination failures

### Status Aggregation
- Collects sub-agent status updates
- Aggregates into primary agent summary
- Maintains progress tracking

Coordination Agent does NOT make goal decisions. It manages information flow.
```

---

## Part V: Measurement Framework

### Primary Metrics

| Metric | Definition | Target | Diagnostic |
|--------|------------|--------|------------|
| **First-Try Success Rate** | Tasks completed without retry | >70% | Low rate indicates delegation failures |
| **Delegation Depth Efficiency** | Tasks completed / hierarchy levels used | Increasing trend | Flat/decreasing indicates unnecessary hierarchy |
| **Coordination Overhead** | Coordination tokens / work tokens | <20% | High overhead indicates bottlenecks |
| **Approval Wait Time** | Time between sub-agent completion and approval | <5% of task time | High wait indicates approval bottleneck |
| **Context Utilization at Completion** | Context used when sub-agent completes | 60-80% | >90% risks context reset; <40% indicates task too small |

### Delegation Quality Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| **Vision Clarity** | Sub-agent understanding matches primary intent (sampled) | >90% |
| **Method Autonomy** | Sub-agents select own methods (vs. dictated) | >80% |
| **Escalation Appropriateness** | Escalated decisions required escalation | >95% |
| **Parallel Efficiency** | Actual parallelism / potential parallelism | >70% |

### Diagnostic Indicators

**Bottleneck Detection:**
- Primary agent context filled with coordination > work: Coordination bottleneck
- Approval queue growing: Approval bottleneck
- Sub-agent wait times high: Resource or dependency bottleneck
- Retry rates high: Delegation clarity or trust calibration issue

**Delegation Failure Indicators:**
- Sub-agent asks many clarifying questions: Insufficient vision specification
- Sub-agent makes wrong methodological choices: Over-specification constraining expertise
- Multiple sub-agents modify same state: Authority boundary violation
- Sub-agent exceeds resource allocation: Resource constraint not enforced

---

## Part VI: Failure Mode Taxonomy

### Delegation Failures

| Failure Mode | Symptom | Root Cause | Mitigation |
|--------------|---------|------------|------------|
| **Unclear Authority** | Sub-agents conflict on who owns decision | Overlapping authority boundaries | Explicit boundary documentation |
| **Over-Delegation** | Sub-agent makes poor decisions | Authority given beyond competence | Trust calibration, progressive autonomy |
| **Under-Delegation** | Primary agent bottleneck | Authority retained that should delegate | Approval threshold review |
| **Vision-Method Confusion** | Sub-agent asks about implementation details | Primary specified HOW not WHAT | Re-delegate with vision focus |
| **Missing Constraints** | Sub-agent exceeds resource/time limits | Constraints not communicated | Explicit constraint specification |

### Coordination Failures

| Failure Mode | Symptom | Root Cause | Mitigation |
|--------------|---------|------------|------------|
| **State Inconsistency** | Sub-agents working from different assumptions | No canonical state | Coordination agent, shared state doc |
| **Dependency Violation** | Sub-agent starts before dependency complete | Dependencies not mapped | Pre-execution dependency mapping |
| **Resource Contention** | Sub-agents compete for limited resource | No resource allocation | Explicit resource budgets |
| **Information Loss** | Primary agent missing critical sub-agent info | Excessive aggregation | Escalation triggers for critical info |

### Hierarchy Failures

| Failure Mode | Symptom | Root Cause | Mitigation |
|--------------|---------|------------|------------|
| **Flat Bottleneck** | Primary coordinates too many sub-agents | Insufficient hierarchy depth | Add coordinator level |
| **Excessive Hierarchy** | High latency, low throughput | Too many levels for task complexity | Flatten hierarchy for simple tasks |
| **Coherence Loss** | Sub-agent outputs inconsistent | Insufficient shared context | More explicit shared state |

### Trust Failures

| Failure Mode | Symptom | Root Cause | Mitigation |
|--------------|---------|------------|------------|
| **Unwarranted Trust** | Sub-agent failures in autonomous mode | Trust calibration too generous | Demote trust level, increase sampling |
| **Excessive Distrust** | Approval bottleneck | Trust calibration too conservative | Sample-based verification, graduated promotion |
| **Trust Inconsistency** | Unpredictable escalation behavior | Trust criteria unclear | Explicit trust level documentation |

---

## Part VII: Multi-Agent Implications

### Scaling Patterns from Film Production

Film production scales from 20-person indie to 2,000-person blockbuster through systematic hierarchy deepening:

| Scale | Hierarchy Depth | Coordination Pattern | Agent System Equivalent |
|-------|-----------------|---------------------|------------------------|
| Small (3-5 agents) | 2 levels | Direct coordination | Primary → Task Agents |
| Medium (10-30 agents) | 3 levels | Hub-and-spoke | Primary → Domain Sub-Agents → Task Agents |
| Large (50-100 agents) | 4 levels | Hierarchical + coordination agents | Primary → Domain → Task + Coordination layer |
| Very Large (100+ agents) | 5+ levels | Multiple sub-orchestrators | Primary → Sub-orchestrators → Domain → Task |

### Span of Control Constraints

Film production research suggests optimal span of control is 5-8 direct reports.

**Agent System Translation:**
- Primary agent should coordinate no more than 8 direct sub-agents
- When >8 sub-agents needed, add hierarchy level
- Coordination agents don't count against goal hierarchy span (they're infrastructure)

**Span Formula:**
```
Required hierarchy depth = ceil(log_7(total_agents))

Examples:
- 5 agents: 1 level (5 < 7)
- 20 agents: 2 levels (ceil(log_7(20)) = ceil(1.53) = 2)
- 100 agents: 3 levels (ceil(log_7(100)) = ceil(2.37) = 3)
- 500 agents: 4 levels (ceil(log_7(500)) = ceil(3.19) = 4)
```

### Einheit Through Shared Documentation

Film production achieves coordination without constant communication through shared understanding:

"Department heads should meet before production starts, matching successful studios like Disney/Pixar where the entire crew becomes adept at speaking and understanding each individual's needs."

**Agent System Translation:**
All agents read same CLAUDE.md. Shared documentation creates implicit coordination.

**CLAUDE.md for Multi-Agent Einheit:**

```markdown
# Multi-Agent Coordination Protocol

## Shared Understanding
All agents in this system share:
- These coordination conventions
- The goal hierarchy documented below
- State access to /state/ directory
- Resource constraints documented in /constraints/

## Implicit Coordination Rules
When modifying files in shared ownership:
- Check /state/file-locks.json before modifying
- Update lock status when starting modification
- Release lock when complete
- If lock held by another agent, wait or work elsewhere

## No-Communication Coordination
Agents should coordinate through state when possible:
- Update progress in /state/progress.json
- Check dependencies in /state/dependencies.json
- Report completion in /state/completed.json

Reserve direct communication for:
- Blocking questions that state doesn't answer
- Conflicts requiring arbitration
- Escalations
```

### The Second Unit Pattern at Scale

For very large agent systems, the second unit pattern enables hierarchical scaling:

```
Primary Agent
├── Sub-Orchestrator A (owns: authentication domain)
│   ├── Code Agent A1
│   ├── Test Agent A2
│   └── Doc Agent A3
├── Sub-Orchestrator B (owns: API domain)
│   ├── Code Agent B1
│   ├── Test Agent B2
│   └── Doc Agent B3
└── Sub-Orchestrator C (owns: database domain)
    ├── Code Agent C1
    ├── Migration Agent C2
    └── Doc Agent C3
```

Primary agent provides intent to sub-orchestrators. Sub-orchestrators manage their domains independently. Primary reviews aggregated results.

This pattern enables:
- Parallel domain work without primary agent bottleneck
- Domain-specialized coordination within each sub-orchestrator
- Scalability through adding sub-orchestrators

---

## Part VIII: CLAUDE.md Templates

### Template 1: Hierarchical Delegation Configuration

```markdown
# Hierarchical Delegation Configuration

## Authority Structure

### Primary Agent (This Agent)
**Authority:**
- Define overall goals and success criteria
- Allocate resources to sub-agents
- Make cross-domain decisions
- Review final outputs

**Delegates to:**
- Domain sub-agents for domain-specific work
- Coordination agent for information management

### Domain Sub-Agents
**Authority:**
- Full method selection within domain
- Task decomposition within domain
- Quality decisions within domain
- Resource allocation to task agents within budget

**Reports to:** Primary agent (strategic summary only)

### Task Agents
**Authority:**
- Implementation decisions within task scope
- Tool selection for task

**Reports to:** Domain sub-agent (full detail)

## Delegation Protocol

### When Delegating:
1. Specify WHAT (goal, success criteria)
2. Specify CONSTRAINTS (resources, time, dependencies)
3. DO NOT specify HOW (methods, tools, algorithms)
4. Provide EXAMPLES if helpful
5. Define INTERFACE (expected output format)

### Template:
```
Goal: [What should be accomplished]
Success Criteria: [How to validate success]
Constraints: [Resource limits, time limits, dependencies]
Interface: [Expected output format]
Examples (optional): [Similar completed work]
```
```

### Template 2: Escalation and Approval

```markdown
# Escalation and Approval Protocol

## Autonomous Operation (No Approval Needed)
- Confidence > 85% on approach
- Reversible actions
- Within resource allocation
- Following documented patterns
- Single-domain scope

## Escalate for Approval
- Confidence < 70%
- Irreversible actions
- Resource consumption > 80% of allocation
- Cross-domain implications
- Contradictory requirements

## Immediate Escalation
- Confidence < 50%
- Security/safety implications
- Would exceed resource allocation
- Blocking other agents

## Escalation Format
```
ESCALATION REQUEST
Type: [Approval/Clarification/Resource/Conflict]
Confidence: [%]
Context: [What led to this decision point]
Options: [Options considered with tradeoffs]
Recommendation: [What I would do if autonomous]
Blocking: [What's blocked pending resolution]
```

## Approval Response Format
```
APPROVED: [option] with notes: [any modifications]
REJECTED: [reason] with alternative: [what to do instead]
CLARIFICATION: [additional context] - re-assess and proceed or re-escalate
```
```

### Template 3: Information Flow

```markdown
# Information Flow Protocol

## Upward Flow (to Primary Agent)
**Include:**
- Goal completion status (done/blocked/in-progress)
- Success criteria validation (met/not met/partial)
- Resource consumption (% of allocation)
- Blockers requiring primary decision
- Cross-domain dependencies discovered

**Exclude:**
- Implementation details
- Tool selection rationale
- Intermediate states
- Task-level progress

**Format:**
```
STATUS: [Domain Name]
Progress: [X]% complete
Key outcomes: [1-3 bullets]
Blockers: [if any]
Resource: [X]% of budget consumed
Next: [what happens next]
```

## Downward Flow (to Task Agents)
**Include:**
- Specific task goal
- Success criteria for task
- Resource allocation for task
- Dependencies (what must complete first)
- Interface requirements (output format)

**Exclude:**
- Higher-level context (unless directly relevant)
- Other agents' tasks
- Political/strategic considerations

## Lateral Flow (Agent to Agent)
**Include:**
- Interface contract fulfillment ("my output X is ready")
- Dependency signals ("I need Y before I can proceed")
- Conflict detection ("we're both modifying Z")

**Route Through:** State documents when possible, direct message when urgent
```

### Template 4: Coordination Agent Specification

```markdown
# Coordination Agent Specification

## Role
The coordination agent manages information flow and state consistency.
The coordination agent does NOT make goal decisions.

## Responsibilities

### State Management
- Maintain /state/canonical.json as single source of truth
- Resolve conflicting updates (last-write-wins with conflict log)
- Provide consistent state view on request

### Message Routing
- Route messages to appropriate recipients
- Filter duplicate messages
- Escalate messages tagged URGENT to primary agent

### Conflict Detection
Monitor for:
- Multiple agents claiming same file lock
- Dependency cycles
- Resource over-allocation
- Goal inconsistencies

On detection:
- Log conflict to /state/conflicts.json
- Alert affected agents
- Escalate to primary if unresolved after 2 cycles

### Status Aggregation
- Collect status updates from all agents
- Aggregate into /state/summary.json every 10 operations
- Maintain /state/progress.json for dependency tracking

## Constraints
- NO goal decisions
- NO method recommendations
- NO approval authority
- Pure information management
```

---

## Part IX: Implementation Roadmap

### Phase 1: Foundation (Single Primary + Task Agents)

**Week 1-2:**
- [ ] Implement vision-method separation in task delegation
- [ ] Create escalation protocol
- [ ] Establish information granularity by level
- [ ] Document authority boundaries

**Validation:**
- Task agents execute without method specification
- Escalation triggers appropriately
- Primary agent receives summaries not details

### Phase 2: Domain Specialization (Add Domain Sub-Agents)

**Week 3-4:**
- [ ] Define domain boundaries (code, research, review, documentation)
- [ ] Create domain sub-agent specifications
- [ ] Implement hierarchical aggregation
- [ ] Test delegation to domain level

**Validation:**
- Domain sub-agents manage their own task agents
- Primary coordinates 3-5 domain agents, not 15+ task agents
- Information aggregates appropriately at each level

### Phase 3: Coordination Infrastructure

**Week 5-6:**
- [ ] Implement coordination agent
- [ ] Create shared state management
- [ ] Establish asynchronous coordination protocol
- [ ] Test lateral coordination without message passing

**Validation:**
- Coordination overhead < 20% of work tokens
- Agents coordinate through state when appropriate
- Conflicts detected and resolved

### Phase 4: Sub-Orchestration (Second Unit Pattern)

**Week 7-8:**
- [ ] Implement sub-orchestrator capability
- [ ] Test full operational delegation
- [ ] Validate sub-orchestrator independence
- [ ] Measure scaling characteristics

**Validation:**
- Sub-orchestrator manages domain independently
- Primary reviews results, not process
- Can add sub-orchestrators without primary bottleneck

### Phase 5: Trust Calibration

**Week 9-10:**
- [ ] Implement trust level tracking
- [ ] Create graduated autonomy protocol
- [ ] Test trust promotion/demotion
- [ ] Validate appropriate escalation rates

**Validation:**
- Trust levels adjust based on performance
- Escalation rate decreases as trust builds
- Failures trigger appropriate trust demotion

---

## Part X: Integration with Other Models

### OODA Loop Integration

Hierarchical delegation and OODA interact through orientation:

**Shared orientation enables delegation.** When sub-agents share orientation with primary agent (through CLAUDE.md), they can make autonomous decisions that align with primary intent. This is film production's "shared vision" that enables parallel work.

**Delegation distributes OODA cycles.** Instead of primary agent completing full OODA for every decision, sub-agents complete OODA for domain decisions. Primary agent's OODA focuses on strategic decisions.

**IG&C through convention.** When delegation patterns become convention (documented in CLAUDE.md), agents delegate via IG&C - no explicit decision needed. "Of course I delegate code work to code agent" becomes automatic.

### Jidoka Integration

Jidoka (stop-and-fix on defect) applies to hierarchical delegation:

**Delegation failure triggers escalation.** When sub-agent cannot complete delegated task, they stop and escalate. They don't proceed with broken assumptions.

**Quality built in at each level.** Each hierarchy level validates before passing upward. Task agent validates task. Domain agent validates domain output. Primary validates cross-domain coherence.

**Andon signal through escalation.** Escalation is the Andon cord. It signals "something is wrong here" and triggers attention from appropriate level.

### Shared Mental Models Integration

Hierarchical delegation requires shared mental models:

**CLAUDE.md as shared mental model.** All agents reading same documentation develops shared understanding of patterns, conventions, and coordination protocols.

**Vision propagation through hierarchy.** Primary agent's intent propagates through hierarchy, getting domain-specific interpretation at each level. This requires shared understanding of how to interpret intent.

**Einheit through documentation.** Film production's Einheit (unity) comes from crews understanding each other's needs. Agent Einheit comes from comprehensive shared documentation.

### Related Research Documents

- `docs/management/ooda-loop-agent-analysis.md` - OODA framework for agent systems
- `docs/lean-manufacturing/jidoka.md` - Stop-and-fix quality patterns
- `docs/surgical-teams/shared-mental-models.md` - Team cognition patterns
- `docs/kitchen-brigade/chain-of-command-routing.md` - Information routing patterns
- `docs/theater-stage-management/master-cuelist.md` - Coordination sequencing

---

## Part XI: Open Questions

### Delegation Calibration

1. **Optimal delegation depth for task complexity?** How do you determine whether a task needs 2-level or 4-level hierarchy?

2. **Trust calibration across sessions?** How do you persist trust levels when agent instances don't persist?

3. **Dynamic hierarchy adjustment?** Should hierarchy depth adjust during execution based on observed complexity?

### Coordination Efficiency

4. **Coordination overhead bounds?** What's the theoretical minimum coordination overhead for N agents?

5. **State vs. message tradeoffs?** When is asynchronous state-based coordination better than direct messaging?

6. **Conflict resolution protocols?** How do you resolve conflicts between sub-orchestrators with overlapping domains?

### Scaling Limits

7. **Maximum effective agent count?** At what scale do hierarchical coordination benefits plateau?

8. **Hierarchy depth limits?** How deep can hierarchy go before intent degradation becomes problematic?

9. **Sub-orchestrator autonomy?** How much should sub-orchestrators deviate from primary intent based on local observation?

---

## Conclusion

Hierarchical delegation in film production demonstrates that **scale is enabled by structure, not hindered by it**. The largest, most complex productions use the deepest hierarchies because that's what makes them possible.

For AI agent systems, hierarchical delegation offers:

1. **Bottleneck prevention** through hierarchical structure maintaining manageable span of control
2. **Expertise leverage** through vision-method separation enabling specialized sub-agents
3. **Parallel work** through pre-execution alignment enabling autonomous execution
4. **Scalability** through sub-orchestration pattern enabling 10x+ agent coordination
5. **Coherence** through shared documentation propagating intent through hierarchy

The key insight: delegation is not about distributing tasks but about creating leverage through parallel specialization while maintaining coherent purpose. The hierarchy is not a chain of command but a network of expertise connected by shared intent.

Film production has refined these patterns through a century of practice coordinating thousands of specialists. These patterns - adapted for agent systems - provide a tested blueprint for scaling beyond what flat orchestration can achieve.

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent architecture analysis for hierarchical delegation patterns
**Source:** Research document `docs/film-production/hierarchical-delegation.md`
**Template:** Based on `docs/management/ooda-loop-agent-analysis.md`

---

## Sources

### Primary Research
- Source research document: `docs/film-production/hierarchical-delegation.md`

### Film Production Sources
- Film Crew: Every Job on a Movie Set, Explained | Backstage
- The Definitive Film Crew Hierarchy Chart - Assemble
- The Essential Guide to Director Agreements | Wrapbook
- Summary of Directors' Creative Rights Under the DGA Basic Agreement of 2020
- Art Department in Film & TV | Production Design Roles & Hierarchy
- The Complete Role and Responsibilities of a VFX Supervisor | Cinema Engineer
- The Role of the Second Unit Director in Film - Assemble
- The Call Sheet: A Production Lifeline - Filmustage
- How to Coordinate with Crew and Department Heads for Film Scheduling | LinkedIn

### Related Agent Analysis Documents
- `docs/management/ooda-loop-agent-analysis.md` - Template and cross-reference
- `docs/film-production/hierarchical-delegation.md` - Primary source research
