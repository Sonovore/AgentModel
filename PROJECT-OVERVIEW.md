# AgentModel Project Overview

> **Quick Reference Guide for Understanding the AgentModel Project Structure**
>
> Last Updated: 2026-01-20

## Executive Summary

The **AgentModel** project is a comprehensive research initiative exploring how multi-agent systems coordinate work through mental models borrowed from proven real-world domains. Instead of starting from abstract distributed systems theory, this project studies successful human coordination models (military command, surgical teams, air traffic control, jazz ensembles) and extracts universal principles for AI agent orchestration.

**Core Philosophy:** Study what works in reality, extract the underlying principles, adapt for AI agents.

---

## Project Statistics

- **30 mental model disciplines** with dedicated research directories
- **142 research/documentation files** across all domains
- **90+ deep-dive documents** completed in Phase 1
- **10 core problems** that all multi-agent systems must solve
- **Current Phase:** Phase 2 (Synthesis & Integration)

---

## Directory Structure

```
AgentModel/
├── docs/                          # 142 markdown files across 30 domains
│   ├── air-traffic-control/       # 9 files - Safety-critical coordination
│   ├── management/                # 18 files - Organizational frameworks
│   ├── pedagogy/                  # 4 files - Learning & mental model building
│   ├── military-*/                # 20 files across 5 directories
│   ├── [25 more domains]/         # See full list below
│   ├── model-selection-strategy.md
│   └── helper-agents/
├── .claude/                       # Project management & session state
│   ├── CLAUDE.md                  # Operational discipline
│   ├── context.md                 # Phase 2 synthesis plan
│   └── problem-research-mapping.md
└── .git/                          # Version control
```

---

## The 30 Mental Model Categories

### Organizational & Management (30 files)
1. **management** (18) - Manager Tools, OODA Loop, Cynefin, Mission Command
2. **military-hierarchy** (3) - Chain of Command, Span of Control
3. **military-command** (4) - Decision authority patterns
4. **military-coordination** (5) - Multi-agent coordination mechanisms
5. **military-planning** (5) - Strategic and tactical planning
6. **military-doctrine** (5) - Military operational theory
7. **military-communication** (3) - Coordination through messaging

### Safety-Critical Operations (20 files)
8. **air-traffic-control** (9) - Separation Assurance, Conflict Detection, Flow Management
9. **incident-response** (3) - Crisis management and silo awareness
10. **emergency-dispatch** (7) - High-stakes coordination under uncertainty
11. **mission-control** (3) - Mission-critical system oversight
12. **surgical-teams** (3) - High-stakes human coordination

### Operations & Execution (32 files)
13. **lean-manufacturing** (7) - Jidoka, continuous improvement, kaizen
14. **logistics-supply-chain** (4) - Network optimization
15. **kitchen-brigade** (3) - Station-based specialization
16. **film-production** (2) - Temporal synchronization
17. **orchestral-conducting** (4) - Master cuelist, synchronized control
18. **theater-stage-management** (4) - Real-time ceremony coordination
19. **jazz-improvisation** (4) - Emergent coordination, cue-based response

### Knowledge & Learning (12 files)
20. **pedagogy** (4) - Zone of Proximal Development, Scaffolding, Mental Model Building
21. **cognitive-science** (4) - Foundational cognitive theory
22. **helper-agents** (1) - Task Complexity Assessment Agent

### System Architecture (16 files)
23. **distributed-systems** (6) - Consensus, CAP theorem, eventual consistency
24. **control-theory** (4) - Mathematical foundations for coordination
25. **mechanism-design** (4) - Incentive structures
26. **legal-agency** (4) - Authority and accountability structures

### Biological & Organizational Theory (10 files)
27. **biology-cas** (1) - Complex adaptive systems
28. **agile-scrum** (3) - Iterative development
29. **safety-engineering** (4) - STAMP, Swiss cheese model

---

## The 10 Core Problems

Every multi-agent system must solve these fundamental challenges:

1. **Task Decomposition and Assignment** (7 perspectives)
   - Breaking complex goals into assignable tasks
   - Matching agent capability to task requirements

2. **Coordination Without Communication** (8 perspectives)
   - Synchronizing without explicit messaging
   - Pattern recognition, shared context, implicit understanding

3. **Conflict Management** (6 perspectives)
   - Detecting conflicts before they occur
   - Resolving resource conflicts

4. **Information Flow** (7 perspectives)
   - What information must flow where
   - Centralized vs. distributed architectures

5. **Temporal Coordination** (7 perspectives)
   - Synchronizing across time horizons
   - Just-in-time vs. buffer-based approaches

6. **Trust and Oversight** (6 perspectives)
   - Building appropriate trust levels
   - Monitoring without micromanagement

7. **Error Detection and Recovery** (6 perspectives)
   - Circuit breaker patterns
   - Self-healing vs. centralized repair

8. **Scaling Coordination** (8 perspectives) **[Priority Focus]**
   - What works at 3 agents vs. 30 vs. 300
   - Pattern transitions as scale increases

9. **Multi-Objective Optimization** (6 perspectives)
   - Balancing competing goals
   - Dynamic priority adjustment

10. **Adaptability** (6 perspectives)
    - Adapting to changing conditions
    - Learning loops and resilience

---

## Document Patterns

### Standard Structure

Each domain follows this pattern:
```
docs/[discipline]/
├── README.md                           # Overview and framework
├── [model-name].md                     # Deep dive on specific model
├── [model-name]-three-level.md         # 3 explanatory levels (5-10yr, HS, expert)
└── [model-name]-agent-analysis.md      # Adaptation to AI agents
```

### Deep-Dive Documents Include

1. **Executive Summary** - Core insight in 1-2 sentences
2. **Core Concept** - What it is and why it matters
3. **How It Works** - Mechanisms and processes
4. **Scaling Characteristics** - Behavior at different scales
5. **When It Fails** - Failure modes and limitations
6. **Key Takeaways for Agents** - Adaptation principles
7. **Mental Models Used** - Related frameworks
8. **Integration Points** - Connections to other problems

### Three-Level Explanations

Progressive pedagogical approach:
- **Level 1:** Ages 5-10 (intuitive, story-based)
- **Level 2:** High school graduate (conceptual, frameworks)
- **Level 3:** Expert (formal theory, research-based)

---

## Task Complexity & Model Selection

### Model Selection Strategy

| Model | Speed | Cost | Best For |
|-------|-------|------|----------|
| **Haiku** | Fastest | 1x | Simple, pattern-based tasks |
| **Sonnet** | Fast | ~20x | Research, analysis, writing |
| **Opus** | Slower | ~60x | Complex reasoning, novel synthesis |

### Complexity Assessment Framework

6-dimensional scoring (0-12 points):

1. **Novelty** - Well-established or cutting-edge?
2. **Ambiguity** - Clear answers or competing views?
3. **Required Depth** - How many layers of understanding?
4. **Integration Complexity** - Single discipline or 4+ fields?
5. **Abstraction Level** - Concrete or theoretical?
6. **Stakes** - Cost of failure (low, medium, high)?

**Routing:**
- 0-4 points → Haiku
- 5-8 points → Sonnet
- 9-12 points → Opus

---

## Project Phases

### Phase 1: Complete ✓

**Phase 1.1: Discipline Identification**
- Created directories for 14 new domains
- Established mental model inventories

**Phase 1.2: Deep Research (31 models across 4 batches)**
- Batch 1: 8 Opus-level models (~6,000 lines)
- Batch 2: 10 Opus-level models (~7,700 lines)
- Batch 3: 10 Sonnet-level models (~10,600 lines)
- Batch 4: 3 Sonnet-level models (~2,900 lines)
- **Total:** 90+ research documents

### Phase 2: In Progress (Synthesis)

**Goal:** Create 10 comprehensive synthesis documents integrating 6-8 disciplinary perspectives per core problem.

**Each synthesis includes:**
- Problem statement and scope
- 6-8 disciplinary perspectives
- Scaling analysis (3-10 vs. 10-50 vs. 50-1000+ agents)
- Decision frameworks
- Implementation checklists
- Failure mode taxonomy
- Anti-patterns
- Key synthesized insights

**Expected Output:** 15,000-25,000 lines of synthesis material

---

## Key Files to Read First

### 1. Foundational Mental Model Research
- `docs/pedagogy/mental-model-building.md` (740 lines)
  - Cognitive science foundations
  - How humans build understanding
  - Application to AI agents

- `docs/pedagogy/mental-model-building-three-level.md` (350 lines)
  - Pedagogical approach at three levels

### 2. Project Strategy
- `docs/model-selection-strategy.md` (268 lines)
  - Task routing framework
  - Complexity assessment methodology

- `.claude/context.md`
  - Current phase status
  - Next steps and priorities

### 3. Helper Agent Design
- `docs/helper-agents/task-complexity-assessment.md` (300 lines)
  - Meta-agent pattern for task routing
  - Example of applying mental models to agent design

### 4. Domain Examples (Choose 2-3)
- `docs/air-traffic-control/` (9 files) - Safety-critical coordination
- `docs/management/` (18 files) - Organizational frameworks
- `docs/lean-manufacturing/` (7 files) - Operational excellence
- `docs/pedagogy/` (4 files) - Learning and improvement

### 5. Core Problem Mapping
- `.claude/problem-research-mapping.md`
  - Maps 10 core problems to 60+ research documents
  - Cross-reference guide

---

## Cross-Cutting Principles

Emerging patterns across all 30 domains:

### 1. Explicit vs. Implicit Communication
- When can teams synchronize without talking?
- When does explicit communication become necessary?

### 2. Centralized vs. Distributed Control
- When to centralize decisions vs. distribute?
- How scale influences this choice

### 3. Time Horizons
- Different layers operate at different speeds
- Coordinating across time scales

### 4. Feedback Loops
- Error detection requires timely feedback
- Learning requires reflection on failures

### 5. Progressive Complexity
- Start simple, add features as scale increases
- Each phase has different requirements

---

## Application to Prompt Improvement

### Mental Model Categories for Agent Trees

Based on research, these categories are particularly relevant for building agent orchestration for prompt and reasoning improvement:

#### Pedagogical Foundation
- Mental Model Building
- Zone of Proximal Development
- Scaffolding
- Worked Examples

#### Coordination Patterns
- Shared Mental Models
- Cue-Based Coordination
- Call and Response

#### Quality & Verification
- Error Detection and Recovery
- Circuit Breaker Pattern
- Jidoka (Autonomous Quality Control)

#### Organizational Structure
- OODA Loop (Observe, Orient, Decide, Act)
- Cynefin Framework (domain-based supervision)
- Hierarchical Delegation

#### Information Architecture
- Information Flow Patterns
- Multi-Channel Communication
- Shared Language

#### Scaling Patterns
- Span of Control (3-7 direct reports)
- Task Organization
- Hierarchical Escalation

### Proposed Agent Tree Structure

```
Root: Orchestrator Agent (Cynefin Framework)
├── Level 2: Analysis & Routing
│   ├── Task Complexity Assessment
│   ├── Pedagogical Stage Assessment
│   └── Scaling Context Detector
├── Level 3: Specialized Improvement
│   ├── Mental Model Builder
│   ├── Coordination Architect
│   ├── Error Detector
│   └── Information Flow Optimizer
└── Level 4: Domain-Specific Experts
    ├── Safety-Critical Expert
    ├── Scaling Pattern Expert
    └── Trust & Oversight Specialist
```

---

## How to Use This Project

### For Understanding Agent Coordination
1. Identify which of the 10 core problems you're facing
2. Read the synthesis document for that problem (when Phase 2 complete)
3. Review relevant domain-specific documents
4. Apply mental models to your specific use case

### For Building New Agents
1. Review `docs/helper-agents/task-complexity-assessment.md` for pattern
2. Identify which mental models apply to your agent's purpose
3. Study those mental models in depth
4. Design agent using principles from multiple disciplines

### For Scaling Existing Systems
1. Assess current system size and target size
2. Review scaling analysis in relevant synthesis documents
3. Identify pattern transitions that occur at your scale
4. Implement appropriate coordination mechanisms

---

## Research Methodology

### Why These Domains?

Each domain was selected because it represents a **proven successful coordination model** operating at scale:

- **Military:** Coordinating thousands under life-or-death constraints
- **Air Traffic Control:** Safety-critical coordination with zero-error tolerance
- **Surgical Teams:** High-stakes human coordination under time pressure
- **Jazz Improvisation:** Emergent coordination without explicit plans
- **Lean Manufacturing:** Optimizing flow and eliminating waste
- **Pedagogy:** Progressive skill development and learning

### Research Process

1. **Identify** mental models used in each domain
2. **Document** how they work in practice
3. **Analyze** scaling characteristics and failure modes
4. **Extract** principles that apply to AI agents
5. **Synthesize** cross-disciplinary insights
6. **Test** through implementation

---

## Contributing to This Project

### Adding New Mental Models

1. Create directory: `docs/[discipline]/`
2. Add `README.md` with overview and model inventory
3. Create deep-dive documents for each model
4. Follow standard document structure
5. Include three-level explanation for complex models
6. Add agent-analysis document showing AI application

### Expanding Existing Research

1. Read existing documents in domain
2. Identify gaps or under-explored areas
3. Create new deep-dive documents
4. Update domain README.md
5. Cross-reference with related domains

### Phase 2 Synthesis

1. Choose one of the 10 core problems
2. Review all research documents tagged for that problem
3. Create synthesis document following template
4. Include scaling analysis and decision frameworks
5. Update `.claude/problem-research-mapping.md`

---

## Integration with Other Projects

### Claude Code Toolkit Integration

This AgentModel research informs the design of:
- Command orchestration patterns
- Hook-based coordination mechanisms
- Multi-agent task routing
- Error detection and recovery

### Prompt Improvement Tool

Mental models from this project provide foundation for:
- Expert persona selection (based on domain analysis)
- Communication style optimization
- Progressive refinement strategies
- Quality verification patterns

---

## Questions This Project Answers

1. **How do you coordinate 3 agents? 30 agents? 300 agents?**
   - Scaling research across all domains

2. **When should agents communicate explicitly vs. implicitly?**
   - Jazz improvisation, surgical teams, ATC coordination patterns

3. **How do you detect and recover from errors in multi-agent systems?**
   - Circuit breakers, Jidoka, safety engineering principles

4. **How do you build trust and appropriate oversight?**
   - Management frameworks, military command structures

5. **What information needs to flow where?**
   - Information architecture across all domains

6. **How do you balance competing objectives?**
   - Multi-objective optimization from all perspectives

7. **How do you make systems adaptable?**
   - Learning loops, feedback mechanisms, resilience patterns

8. **How do you decompose complex tasks?**
   - Military planning, incident response, project management

9. **How do you handle temporal coordination?**
   - Lean manufacturing, film production, orchestral conducting

10. **What are the universal failure modes?**
    - Synthesized across 90+ deep-dive documents

---

## Contact & Version Control

- **Repository:** Git-tracked (`.git/`)
- **Current Branch:** main
- **Project Start:** [See git log for initial commit]
- **Last Major Update:** 2026-01-20 (this overview document)

---

## Quick Start Guide

**New to this project?**

1. Read this overview document (you're doing it!)
2. Read `docs/pedagogy/mental-model-building.md` for foundational concepts
3. Browse `.claude/problem-research-mapping.md` to understand coverage
4. Pick a domain that interests you and explore 2-3 documents
5. Identify which of the 10 core problems relates to your work
6. Deep dive into relevant synthesis documents (Phase 2)

**Ready to contribute?**

1. Review existing research in your chosen domain
2. Follow document structure patterns
3. Cross-reference with related domains
4. Update mapping documents
5. Commit with descriptive messages

---

## Future Directions

### Planned Expansions

- Complete Phase 2 synthesis (10 documents)
- Implement helper agents based on mental models
- Create interactive decision tools
- Build visualization of cross-domain patterns
- Develop training materials for AI agent orchestration

### Open Questions

- How do mental models transfer across contexts?
- What are optimal team sizes for different task types?
- How to measure coordination effectiveness?
- What coordination patterns emerge that aren't in human domains?

---

*This overview is a living document. Update it as the project evolves.*
