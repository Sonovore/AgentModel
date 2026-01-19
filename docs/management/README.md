# Management Frameworks

Mental models from management theory, organizational behavior, and decision science applied to AI agent supervision.

## Purpose

Each framework offers a different lens for thinking about agent management. Some concepts translate directly; others require significant adaptation; some reveal gaps in current thinking.

## Status

**Current phase:** Gathering - exploring frameworks, documenting insights, not yet building systems.

## Frameworks

### Completed (Priority 1)

| Framework | File | Key Insight |
|-----------|------|-------------|
| **Manager Tools** | | |
| MT: One-on-Ones | `mt-one-on-ones.md` | Capability calibration, observation surfacing |
| MT: Feedback | `mt-feedback.md` | Feedback → habit formation (CLAUDE.md refinement) |
| MT: Coaching | `mt-coaching.md` | Four coaching targets: Human, CLAUDE.md, System, not Agent |
| MT: Delegation | `mt-delegation.md` | Capacity scaling vs development, Auftragstaktik connection |
| **Decision & Control** | | |
| OODA Loop | `ooda-loop.md` | Orient as bottleneck, Implicit Guidance & Control, Einheit |
| Cynefin Framework | `cynefin.md` | Domain-based supervision (Clear/Complicated/Complex/Chaotic) |
| Ashby's Law | `ashbys-law.md` | Supervision variety must match agent variety |
| **Organizational** | | |
| Mission Command | `mission-command.md` | Prerequisites (Einheit, Vertrauen), backbrief pattern |
| Principal-Agent Theory | `principal-agent.md` | Hidden action/information, frozen incentives, monitoring |
| Incident Command System | `incident-command-system.md` | Span of control (3-7), modular scaling, unified command |
| **Stability** | | |
| Circuit Breaker Pattern | `circuit-breaker.md` | Fail fast, prevent cascade, dynamic trust via state machine |
| **Leadership & Trust** | | |
| Situational Leadership | `situational-leadership.md` | Three-style model (Direct/Explore/Delegate) based on task characteristics |
| Trust Development | `trust-development.md` | Multi-dimensional trust (Ability, Integrity, Benevolence), domain-specific |
| **Decision Making** | | |
| Recognition-Primed Decision | `recognition-primed-decision.md` | Pattern matching works, but agents can't learn from feedback |
| **Responsibility** | | |
| RACI Matrix | `raci-matrix.md` | Agents can be Responsible but never Accountable |

### Priority 3: Maybe Later

- Viable System Model (Stafford Beer) - Completeness check for systems
- Team Topologies - Agent type organization patterns
- Chaos Engineering - Proactive failure testing
- Cognitive Load Theory - Context window optimization

## Document Structure

Each framework gets a file per concept:
- `mt-one-on-ones.md` - Manager Tools: One-on-Ones
- `mt-feedback.md` - Manager Tools: Feedback
- `ooda-loop.md` - Boyd's OODA Loop

## Related Documents

- [Agent Management Framework](../agent-management-framework.md) - Synthesized guidance (update after exploration)
- [Agent Types](../agent-types.md) - Agent specializations
- [Agent Task System](../agent-task-system.md) - Coordination patterns
