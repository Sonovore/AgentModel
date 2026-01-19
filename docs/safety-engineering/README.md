# Safety Engineering

Mental models from safety science, human factors, and high-reliability organizations applied to AI agent supervision.

## Purpose

Safety engineering studies how complex systems fail and how to design for failure containment. These insights are directly applicable: agent systems will fail, and the question is whether failures are contained or catastrophic.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Accident Models

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Swiss Cheese Model | James Reason | Layered defenses, holes aligning |
| Normal Accident Theory | Charles Perrow | Tight coupling + complexity = inevitable accidents |
| Drift into Failure | Sidney Dekker | Gradual normalization of deviance |
| STAMP/STPA | Nancy Leveson | Systems-theoretic accident model |
| Bow-Tie Model | Risk management | Barriers before and after events |

### High Reliability Organizations

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Preoccupation with Failure | Weick & Sutcliffe | Treating near-misses as full failures |
| Reluctance to Simplify | Weick & Sutcliffe | Maintaining nuanced understanding |
| Sensitivity to Operations | Weick & Sutcliffe | Attention to the front line |
| Commitment to Resilience | Weick & Sutcliffe | Bouncing back from errors |
| Deference to Expertise | Weick & Sutcliffe | Authority flows to knowledge, not hierarchy |

### Human Factors

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Skill-Rule-Knowledge Framework | Rasmussen | Different error types at different levels |
| Situation Awareness | Endsley | Perception → Comprehension → Projection |
| Automation Complacency | Parasuraman | Over-trusting automated systems |
| Mode Confusion | Aviation | Misunderstanding system state |
| Automation Bias | Human factors | Accepting automation output uncritically |

### Defense Strategies

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Defense in Depth | Security/safety | Multiple independent barriers |
| Fail-Safe vs Fail-Secure | Safety engineering | Default states on failure |
| Graceful Degradation | Resilience engineering | Reduced function vs total failure |
| Blast Radius | Reliability engineering | Containing failure scope |
| Recovery Time Objective | Disaster recovery | How fast must we recover? |

### Root Cause Analysis

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| 5 Whys | Toyota | Iterative cause identification |
| Fault Tree Analysis | Safety engineering | Top-down failure decomposition |
| FMEA | Quality engineering | Systematic failure mode enumeration |
| Incident Post-Mortems | SRE practice | Blameless retrospectives |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| Swiss Cheese Model | Very High | Low | 1 |
| Normal Accident Theory | Very High | Medium | 1 |
| Automation Complacency/Bias | Very High | Low | 1 |
| HRO Principles | High | Medium | 1 |
| Drift into Failure | High | Medium | 2 |
| STAMP/STPA | High | High | 2 |
| Situation Awareness | Medium | Medium | 2 |
| Skill-Rule-Knowledge | Medium | Medium | 3 |

## Key Questions

1. What's the "Swiss cheese" stack for agent supervision? What are the independent layers?
2. Are agent systems "tightly coupled" in Perrow's sense? (Changes propagate fast, no slack)
3. How do we detect "drift into failure" - gradual acceptance of agent behaviors that were once flagged?
4. What's the equivalent of "deference to expertise" when the expert is an agent?
5. How do we design for automation bias - humans rubber-stamping agent output?

## Related Directories

- [Management](../management/) - Human oversight patterns
- [Control Theory](../control-theory/) - Feedback and stability
- [Distributed Systems](../distributed-systems/) - Failure propagation
