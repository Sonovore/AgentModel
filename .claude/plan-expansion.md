# AgentModel Expansion Plan

## Overview

Expand the mental model research to cover additional disciplines, define operator-helper-agents, and create a selection system for matching tasks to models/skills.

## Phase 1: New Discipline Research

### 1.1 Create Directories and READMEs

Create directories for high-relevance disciplines:

| Directory | Focus | Priority |
|-----------|-------|----------|
| orchestral-conducting/ | Ensemble coordination, non-verbal communication, tempo | High |
| theater-stage-management/ | Cue-based coordination, real-time production | High |
| air-traffic-control/ | Deconfliction, flow management, safety-critical decisions | High |
| emergency-dispatch/ | Triage, multi-agency coordination, protocol-driven | High |
| mission-control/ | Specialized team coordination, CAPCOM, autonomous transitions | High |
| incident-response/ | SOC operations, time-critical multi-team response | High |
| lean-manufacturing/ | Toyota Production System, JIT, kaizen, pull systems | High |
| kitchen-brigade/ | Station-based specialization, service coordination | Medium-High |
| jazz-improvisation/ | Emergent coordination, shared grammar, self-repair | Medium-High |
| logistics-supply-chain/ | Network optimization, flow, multi-objective balancing | Medium-High |
| agile-scrum/ | Sprint cycles, ceremonies, scaling frameworks | Medium-High |
| surgical-teams/ | Safety-critical hierarchies, non-verbal coordination | Medium |
| film-production/ | Phase-based projects, hierarchical delegation | Medium |
| pedagogy/ | Scaffolding, zone of proximal development | Medium |

**Estimated work:** 14 directories with READMEs listing models to explore

### 1.2 Deep Research on New Disciplines

For each high-priority discipline, research 3-5 key mental models:
- ~45-60 deep-dive documents
- Same methodology as military research (2-3 layers deep)

### 1.3 "Does Not Apply" Sections (Deferred)

Add "Models That Don't Translate" sections to existing and new READMEs.
- Lower priority - do after core research
- Focus on preventing misapplication

---

## Phase 2: Operator-Helper-Agents

### 2.1 Define Helper Agent Specifications

Create `docs/helper-agents/` directory with specifications for:

**Planning Phase:**
| Agent | Purpose |
|-------|---------|
| Task Decomposition | Break complex requests into executable subtasks |
| Estimation | Provide effort/complexity estimates with confidence bounds |
| Dependency Mapper | Identify task dependencies, parallelization opportunities |

**Assignment Phase:**
| Agent | Purpose |
|-------|---------|
| Capability Matching | Match tasks to agents based on demonstrated performance |
| Load Balancing | Distribute work to optimize throughput |
| Readiness Assessment | Validate preconditions before assignment |

**Execution Phase:**
| Agent | Purpose |
|-------|---------|
| Progress Tracking | Monitor execution, detect stalls/drift |
| Quality Validation | Assess work quality against criteria |
| Risk Detection | Early warning system for emerging problems |

**Communication Phase:**
| Agent | Purpose |
|-------|---------|
| Context Synthesis | Curate relevant context for agents |
| Summarization | Distill outputs for handoffs/reporting |
| Status Reporting | Generate stakeholder-appropriate updates |

**Adaptation Phase:**
| Agent | Purpose |
|-------|---------|
| Replanning | Adjust plans when reality diverges |
| Escalation Decision | Determine when/how to escalate to humans |
| Resource Reallocation | Shift resources to optimize outcomes |

**Meta-Agents:**
| Agent | Purpose |
|-------|---------|
| Learning | Extract lessons, improve future orchestration |
| Conflict Resolution | Handle competing priorities, resource contention |

### 2.2 Deep Research for Helper Agents

For each helper agent type:
- Research relevant mental models from all disciplines
- Document required capabilities
- Define input/output specifications
- Identify failure modes

---

## Phase 3: Selection System Research (Mental Models First)

### 3.1 Research Data Structuring Mental Models

Before building a database, research mental models for:

| Topic | Source Discipline | Why It Matters |
|-------|-------------------|----------------|
| Knowledge Graphs | Computer Science | Structural backbone for skill relationships |
| Faceted Classification | Information Architecture | Multi-dimensional filtering |
| Case-Based Reasoning | AI/Cognitive Science | Learning from past task-skill pairings |
| Ontologies | Knowledge Engineering | Formal reasoning about applicability |
| Vector Embeddings | ML/NLP | Semantic similarity matching |

### 3.2 Design Selection System (After Research)

Design a hybrid architecture:
1. Knowledge graph for structure (skills, prerequisites, relationships)
2. Vector embeddings for fast semantic retrieval
3. Faceted metadata for constraint filtering
4. Rules/CBR for decision logic

**Defer implementation until mental models are understood.**

---

## Phase 4: Backlog (Lower Priority)

- [ ] "Does not apply" comprehensive audit of existing disciplines
- [ ] Skills framework (distinct from mental models)
- [ ] Selection system implementation
- [ ] Synthesis documents connecting models across disciplines

---

## Execution Order

1. **Phase 1.1:** Create 14 new discipline directories with READMEs (1 task)
2. **Phase 1.2:** Deep research on new disciplines (~45-60 agents, batched)
3. **Phase 2.1:** Create helper-agents directory with specifications (1 task)
4. **Phase 2.2:** Research mental models for helper agents (~17 agents)
5. **Phase 3.1:** Research data structuring mental models (~5 agents)
6. **Review and iterate**

---

## Questions Requiring Clarification

1. Should new disciplines be in `docs/` at the same level as military-* directories?
2. Priority order for Phase 1.2 disciplines?
3. Any disciplines to exclude from the list?
