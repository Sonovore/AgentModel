# Military Command

Mental models from military command theory applied to AI agent supervision and decision-making.

## Purpose

Military command theory addresses how decisions are made and executed under uncertainty, time pressure, and incomplete information. These concepts directly apply to human supervision of AI agents.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Commander's Intent

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Commander's Intent | US Army doctrine | Purpose and end state that guides autonomous action |
| Two Levels Up | Military practice | Understanding context above your level |
| Left and Right Limits | Tactical doctrine | Boundaries within which to operate |
| Essential Tasks | Mission analysis | What MUST be accomplished |
| Implied Tasks | Mission analysis | Tasks not stated but necessary |

### Decision-Making Models

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| MDMP | US Army | Military Decision Making Process (deliberate) |
| TLP | US Army | Troop Leading Procedures (time-constrained) |
| OODA Loop | Boyd | Observe-Orient-Decide-Act (already in management/) |
| Recognition-Primed Decision | Klein | Expert decision-making (already in management/) |
| Rapid Decision Making | USMC | Abbreviated planning under time pressure |

### Command Concepts

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Centralized Planning / Decentralized Execution | Doctrine | Where decisions should be made |
| Mission Command | Modern doctrine | Philosophy of empowered subordinates |
| Commander's Critical Information Requirements | C2 | What the commander must know |
| Decision Points | Planning | Pre-identified moments for decisions |
| Criteria for Success | Planning | How to know if you're winning |

### Control and Feedback

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Fragmentary Orders (FRAGOs) | Military practice | Updates to existing orders |
| Warning Orders (WARNOs) | Military practice | Advance notice of upcoming tasks |
| Commander's Update Brief | Battle rhythm | Regular status synchronization |
| Running Estimate | Staff process | Continuously updated assessment |
| Assumption Validation | Planning | Checking if premises still hold |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| Commander's Intent | Very High | Medium | 1 - Critical |
| CCIR (Critical Information Requirements) | Very High | Medium | 1 - Critical |
| Centralized Planning / Decentralized Execution | Very High | Low | 1 - Critical |
| MDMP | High | High | 1 |
| Decision Points | High | Medium | 2 |
| FRAGOs / WARNOs | Medium | Low | 2 |
| Running Estimate | Medium | Medium | 3 |

## Key Questions

1. How do you express "commander's intent" for an agent task?
2. What's the agent equivalent of "two levels up" - understanding broader context?
3. What are "CCIRs" for agents - information that must reach the human?
4. How do you issue "FRAGOs" - updates to agent tasks mid-execution?
5. What's "centralized planning / decentralized execution" for human-agent teams?

## Related Directories

- [military-hierarchy](../military-hierarchy/) - Organizational structures
- [military-planning](../military-planning/) - Planning processes
- [management](../management/) - Mission Command, OODA Loop
- [cognitive-science](../cognitive-science/) - Decision-making under constraints
