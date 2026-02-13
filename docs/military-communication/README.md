# Military Communication

Mental models from military communication doctrine applied to AI agent information exchange.

## Purpose

Military communication systems are designed for clarity, reliability, and efficiency under adverse conditions. The protocols, formats, and disciplines developed for military communication offer patterns for agent-to-agent and human-to-agent information exchange.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Message Formats and Protocols

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| SALUTE Reports | Tactical reporting | Structured observation format (Size, Activity, Location, Unit, Time, Equipment) |
| SITREP | Situation reports | Standardized status updates |
| SPOTREP | Spot reports | Immediate significant information |
| 9-Line MEDEVAC | Medical evacuation | Structured request format |
| 5-Paragraph Order | Operations orders | Standard order format (SMEAC) |

### Brevity and Clarity

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Brevity Codes | Tactical communication | Short standardized phrases (WILCO, ROGER, etc.) |
| Prowords | Radio procedure | Procedural words for clarity (OVER, OUT, BREAK) |
| Read-Back / Hear-Back | Safety communication | Confirming understanding |
| Challenge and Reply | Authentication | Verifying identity |
| Phonetic Alphabet | NATO | Unambiguous letter communication |

### Information Flow

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Push vs Pull | Information management | Automatic vs requested information |
| Need to Know | Security principle | Information compartmentalization |
| Commander's Critical Information Requirements | C2 | What must be reported immediately |
| Priority Intelligence Requirements | Intelligence | What we need to learn |
| Information Requirements | Planning | What we need to decide |

### Communication Discipline

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| EMCON (Emission Control) | Electronic warfare | When to stay silent |
| Net Discipline | Radio operations | Orderly use of shared channels |
| Message Precedence | Military comms | FLASH, IMMEDIATE, PRIORITY, ROUTINE |
| Authentication | Security | Verifying message authenticity |
| Communications Security (COMSEC) | Security | Protecting information in transit |

### Degraded Communications

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| PACE Plan | Contingency comms | Primary, Alternate, Contingency, Emergency |
| Lost Communications Procedures | Aviation | Pre-briefed actions when comms fail |
| Radio Silence | Tactical operations | Operating without communication |
| Runner/Messenger | Traditional | Human backup when technology fails |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| 5-Paragraph Order (SMEAC) | Very High | Medium | 1 - Critical |
| CCIR / PIR / IR | Very High | Medium | 1 - Critical |
| Read-Back / Hear-Back | High | Low | 1 |
| Push vs Pull | High | Low | 1 |
| PACE Plan | High | Low | 1 |
| Brevity Codes | Medium | Low | 2 |
| Message Precedence | Medium | Low | 2 |
| SALUTE Reports | Medium | Low | 2 |

## Key Questions

1. What's the agent equivalent of a 5-paragraph order? (Situation, Mission, Execution, Admin, Command/Signal)
2. How do you implement "read-back" for agents - verifying understanding?
3. What's the PACE plan for agent communication? (Primary method fails, then what?)
4. When should information be "pushed" vs "pulled" in agent systems?
5. What's "CCIR" for agents - what must the human know immediately?
6. How do you handle "lost comms" - agents that stop responding?

## Related Directories

- [military-command](../military-command/) - CCIRs and decision-making
- [military-coordination](../military-coordination/) - Synchronized action
- [distributed-systems](../distributed-systems/) - Communication protocols
- [safety-engineering](../safety-engineering/) - Failure handling
