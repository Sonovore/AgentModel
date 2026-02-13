# Military Hierarchy

Mental models from military organizational structures applied to AI agent systems.

## Purpose

Military hierarchies have evolved to balance centralized control with distributed execution, clear accountability with adaptive response. Understanding these structures informs how to organize multi-agent systems.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Command Structures

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Chain of Command | Military fundamentals | Clear lines of authority and responsibility |
| Unity of Command | Principles of war | One boss per subordinate |
| Span of Control | Organizational theory | Limits on direct reports (3-7 typically) |
| Staff vs Line | Military organization | Advisory vs command authority |
| Dual-Hatting | Joint operations | Same person in multiple command roles |

### Echelons and Levels

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Tactical/Operational/Strategic | Military theory | Different levels of abstraction and time horizon |
| Echelon Above/Below | Army doctrine | Responsibilities at each level |
| Higher/Adjacent/Lower | Coordination | Relationships in the hierarchy |
| Task Organization | Military practice | Temporary restructuring for missions |
| Modular Force Design | Modern doctrine | Plug-and-play unit composition |

### Authority Relationships

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| OPCON/TACON/ADCON | US Joint doctrine | Different types of control relationships |
| Supported/Supporting | Joint doctrine | Who has priority for resources |
| Command Relationships | Joint Pub 1 | Formal authority structures |
| Coordinating Authority | Joint doctrine | Authority to coordinate without command |

### Distributed Structures

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Mission Command | Modern doctrine | Decentralized execution within intent |
| Auftragstaktik | German doctrine | Mission-type orders (already in management/) |
| Network-Centric Warfare | RMA theory | Flattened hierarchies with information sharing |
| Self-Synchronization | NCW theory | Units coordinating without central direction |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| Tactical/Operational/Strategic | Very High | Medium | 1 - Critical |
| OPCON/TACON/ADCON | Very High | Medium | 1 - Critical |
| Span of Control | High | Low | 1 (already in ICS) |
| Task Organization | High | Medium | 1 |
| Staff vs Line | Medium | Low | 2 |
| Network-Centric Warfare | Medium | High | 2 |
| Self-Synchronization | Medium | High | 3 |

## Key Questions

1. What's the right "span of control" for agent supervision?
2. How do tactical/operational/strategic levels map to agent task decomposition?
3. What's the difference between OPCON (operational control) and TACON (tactical control) for agents?
4. How do you "task organize" agents for specific missions?
5. Can agents "self-synchronize" or does that require capabilities they lack?

## Related Directories

- [military-command](../military-command/) - Decision authority
- [military-coordination](../military-coordination/) - Working together
- [management](../management/) - ICS, organizational patterns
- [legal-agency](../legal-agency/) - Authority structures
