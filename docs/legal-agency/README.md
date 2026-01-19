# Legal Agency

Mental models from legal theory of agency, fiduciary duty, and liability applied to AI agent supervision.

## Purpose

Legal frameworks for agency have evolved over centuries to handle delegation, authority, liability, and duty of care. These battle-tested concepts provide guidance for agent governance that CS research hasn't yet reinvented.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Agency Fundamentals

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Principal-Agent Relationship | Agency law | The foundational delegation structure |
| Actual vs Apparent Authority | Agency law | What agent can do vs what others believe agent can do |
| Express vs Implied Authority | Agency law | Explicit grants vs reasonable inference |
| Scope of Authority | Agency law | Boundaries of delegated power |
| Ratification | Agency law | Principal accepting unauthorized acts after the fact |

### Liability & Responsibility

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Vicarious Liability | Tort law | Principal liable for agent's acts within scope |
| Respondeat Superior | Employment law | "Let the master answer" |
| Independent Contractor vs Employee | Employment law | Control determines liability |
| Joint & Several Liability | Tort law | Multiple parties, full responsibility each |
| Indemnification | Contract law | Shifting liability by agreement |

### Fiduciary Duties

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Duty of Care | Fiduciary law | Reasonable skill and diligence |
| Duty of Loyalty | Fiduciary law | Act in principal's interest, not own |
| Duty of Obedience | Fiduciary law | Follow lawful instructions |
| Duty to Inform | Fiduciary law | Disclose material information |
| Business Judgment Rule | Corporate law | Deference to good-faith decisions |

### Authority & Limits

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Ultra Vires | Corporate law | Acts beyond granted authority |
| Delegation of Delegation | Agency law | Can agent delegate to sub-agents? |
| Emergency Authority | Agency law | Expanded scope in emergencies |
| Termination of Authority | Agency law | When delegation ends |
| Notice & Reliance | Agency law | Third party's reasonable expectations |

### Accountability Structures

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Audit Rights | Contract law | Principal's right to inspect |
| Reporting Obligations | Regulatory law | Required disclosures |
| Conflict of Interest | Fiduciary law | When agent interests diverge |
| Self-Dealing | Fiduciary law | Agent benefiting from position |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| Actual vs Apparent Authority | Very High | Low | 1 |
| Scope of Authority | Very High | Low | 1 |
| Vicarious Liability | Very High | Medium | 1 |
| Duty of Care/Loyalty | High | Low | 1 |
| Duty to Inform | High | Low | 2 |
| Ultra Vires | High | Low | 2 |
| Delegation of Delegation | Medium | Medium | 2 |
| Business Judgment Rule | Medium | Medium | 3 |

## Key Questions

1. What's "apparent authority" for an AI agent? What do third parties reasonably assume it can do?
2. How does vicarious liability apply when the "agent" is software? (Emerging legal question)
3. What's the agent's duty to inform? When must it escalate vs act autonomously?
4. Can agents delegate to sub-agents? Under what conditions?
5. What's the equivalent of "business judgment rule" - when do we defer to agent decisions?

## Related Directories

- [Management](../management/) - Principal-Agent theory (economic version)
- [Mechanism Design](../mechanism-design/) - Incentive structures
- [Safety Engineering](../safety-engineering/) - Liability and failure
