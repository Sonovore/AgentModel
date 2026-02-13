# Emergency Dispatch

Mental models from emergency dispatch applied to AI agent triage, multi-agency coordination, and protocol-driven decisions.

## Purpose

Emergency dispatch systems excel at rapidly triaging high-volume, high-stakes requests and coordinating multiple specialized agencies toward resolution. They balance competing objectives (speed vs accuracy, specialized response vs availability), handle resource constraints, and increasingly augment human judgment with AI recommendations. These patterns address how AI agents can support human decision-makers in complex, time-critical scenarios.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Triage and Prioritization

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Protocol-Driven Triage | Medical/dispatch practice | Systematic assessment using decision trees |
| Severity Classification | Emergency systems | Categorizing requests by urgency and resources needed |
| Resource Allocation | Dispatch operations | Matching available resources to incident needs |
| Priority Queuing | Emergency dispatch | Reordering requests based on criticality |
| Escalation Triggers | Dispatch protocols | Automatic escalation when thresholds exceeded |

### Multi-Agency Coordination

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Multi-Agency Coordination | Emergency management | Coordinating across organizational boundaries |
| Incident Command System | Emergency management | Unified structure for complex incidents |
| Agency Handoffs | Dispatch practice | Transferring incident between specialized teams |
| Cross-Agency Communication | Emergency practice | Clear protocols between different agencies |
| Resource Proximity Optimization | Dispatch operations | Routing to nearest capable resources |

### Technology and Decision Support

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Technology-Augmented Decision-Making | Modern dispatch | Human decision-makers using AI recommendations |
| Computer-Aided Dispatch | Emergency systems | Systems augmenting but not replacing human judgment |
| Data-Driven Risk Assessment | Dispatch analytics | Using historical patterns for prioritization |
| Recommendation vs Mandate | Decision support | Distinguishing advisory from binding decisions |

### Virtual Networks and Coordination

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Virtual Networks | Dispatch systems | Dynamic teams formed for specific incidents |
| Temporary Authority Structures | Emergency response | Clear but temporary command relationships |
| Network Awareness | Multi-agency systems | Understanding which agencies are involved |
| Information Sharing Standards | Inter-agency coordination | Common data formats and protocols |

### AI-Assisted Prioritization

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| AI-Assisted Prioritization | Modern emergency systems | Machine learning improving triage decisions |
| Human Veto | Hybrid systems | Humans retaining ability to override AI |
| Confidence Levels | AI systems | System expressing certainty in recommendations |
| Explainability Requirements | AI governance | Showing rationale for AI-influenced decisions |
| Continuous Calibration | AI operations | Adjusting AI models based on outcomes |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| **Protocol-Driven Triage** | Very High | Low | 1 - Critical |
| **Multi-Agency Coordination** | Very High | High | 1 - Critical |
| **Technology-Augmented Decision-Making** | Very High | High | 1 - Critical |
| **Severity Classification** | High | Low | 1 |
| **Resource Allocation** | High | Medium | 2 |
| **AI-Assisted Prioritization** | High | High | 2 |
| **Incident Command System** | High | High | 2 |
| **Virtual Networks** | Medium | Medium | 3 |
| **Continuous Calibration** | Medium | Medium | 3 |

## Key Questions

1. What should AI-augmented triage look like - where does the human stay in the loop?
2. How do you express multi-agency coordination constraints to agents?
3. What's the equivalent of "resource proximity optimization" for computational agents?
4. How do protocol-driven decisions scale when protocols conflict or are incomplete?
5. What explainability is required for AI recommendations in high-stakes decisions?
6. How do you handle requests that don't fit standard protocols or categories?

## Related Directories

- [air-traffic-control](../air-traffic-control/) - Deconfliction and flow management
- [incident-response](../incident-response/) - Multi-team coordination at scale
- [mission-control](../mission-control/) - Specialized team coordination
- [theater-stage-management](../theater-stage-management/) - Central coordination hub
- [military-command](../military-command/) - Decision-making under uncertainty
