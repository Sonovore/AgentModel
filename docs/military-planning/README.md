# Military Planning

Mental models from military planning processes applied to AI agent task decomposition and execution.

## Purpose

Military planning processes are designed to handle complexity, uncertainty, and time pressure while producing actionable plans. These methodologies inform how to structure agent tasks and adapt to changing conditions.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Planning Processes

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| MDMP | US Army | Military Decision Making Process (7 steps) |
| MCPP | USMC | Marine Corps Planning Process |
| JPP | Joint doctrine | Joint Planning Process |
| TLP | US Army | Troop Leading Procedures (time-constrained) |
| Design Methodology | Army doctrine | Understanding complex problems before planning |

### Mission Analysis

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Mission Statement | Planning | Task and purpose |
| Specified Tasks | Mission analysis | Explicitly assigned |
| Implied Tasks | Mission analysis | Not stated but necessary |
| Essential Tasks | Mission analysis | Must be accomplished |
| Constraints and Limitations | Mission analysis | What you must/must not do |
| Assumptions | Planning | What we believe without proof |

### Course of Action Development

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| COA Development | MDMP | Generating options |
| COA Analysis (Wargaming) | MDMP | Testing options against scenarios |
| COA Comparison | MDMP | Evaluating options against criteria |
| Decision Matrix | Planning tools | Structured comparison |
| Red Team | Analysis | Adversarial evaluation |

### Execution Planning

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Synchronization Matrix | Planning | Who does what when |
| Execution Matrix | Planning | Tasks, purposes, timelines |
| Decision Support Matrix | Planning | Triggers for decisions |
| Branches and Sequels | Planning | Contingency plans |
| Phase Lines / Objectives | Planning | Progress markers |

### Adaptive Planning

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Running Estimate | Staff process | Continuous reassessment |
| Fragmentary Orders | Execution | Updates to plans |
| Decision Points | Execution | Pre-planned choice moments |
| Triggers | Planning | Conditions that cause action |
| Abort Criteria | Planning | When to stop |

### Time Management

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| 1/3 - 2/3 Rule | Military practice | Use 1/3 of time for planning, give 2/3 to subordinates |
| Backwards Planning | Military practice | Start from deadline, work backwards |
| Parallel Planning | Modern doctrine | Plan while receiving guidance |
| Time-Competitive Planning | Doctrine | Planning faster than the situation changes |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| Mission Analysis (Specified/Implied/Essential) | Very High | Medium | 1 - Critical |
| Branches and Sequels | Very High | Medium | 1 - Critical |
| 1/3 - 2/3 Rule | High | Low | 1 |
| Decision Support Matrix | High | Medium | 1 |
| MDMP Overview | High | High | 2 |
| Wargaming (COA Analysis) | High | High | 2 |
| Red Team | Medium | Medium | 2 |
| Synchronization Matrix | Medium | Medium | 3 |

## Key Questions

1. How do you decompose "commander's intent" into specified/implied/essential tasks for agents?
2. What's "wargaming" for agent task planning - how do you test approaches?
3. How do you build "branches and sequels" into agent workflows?
4. What's the 1/3-2/3 rule for agent task assignment?
5. How do you create "decision support matrices" for agent escalation?
6. What's "red teaming" for agent systems?

## Related Directories

- [military-command](../military-command/) - Commander's intent, decision-making
- [military-coordination](../military-coordination/) - Synchronization
- [management](../management/) - Task breakdown
- [cognitive-science](../cognitive-science/) - Planning under constraints
