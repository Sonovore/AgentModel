# Agent Mental Models

Exploration of how established management/decision frameworks apply to AI agent supervision.

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

### Priority 2: Worth Exploring

| Framework | Source | Why |
|-----------|--------|-----|
| Situational Leadership | Hersey/Blanchard | Adjusting autonomy based on task/capability |
| Trust Development | Mayer et al. | Operationalizing trust (ability, integrity, benevolence) |
| Recognition-Primed Decision | Gary Klein | How experts actually decide (pattern → simulate → act) |
| Circuit Breaker Pattern | Michael Nygard | Failure handling, preventing cascade |
| RACI Matrix | Project management | Role clarity in multi-agent systems |

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
