# Trust Development Framework

**Source:** Mayer, Davis, and Schoorman (1995) - "An Integrative Model of Organizational Trust"

## Framework Summary

An integrative model of organizational trust that distinguishes between:
- **Trustworthiness** - characteristics of the trustee (the three factors)
- **Trust** - the trustor's willingness to be vulnerable
- **Risk-taking** - actually becoming vulnerable

## Key Concepts

### The Three Factors of Trustworthiness

1. **Ability** - Skills, competencies, and characteristics that enable influence within a specific domain. Answers "Can they do this?"

2. **Benevolence** - The extent to which the trustee wants to do good for the trustor. Answers "Do they care about my interests?"

3. **Integrity** - Adherence to principles the trustor finds acceptable. Answers "Will they do what they say?"

### How Trust Develops Over Time

Trust develops through a feedback loop: assessment leads to trust decision, which leads to risk-taking, which produces outcomes that update perceptions.

- **Early stage**: Ability dominates (must demonstrate competence first)
- **Developing stage**: Integrity becomes important (consistency and follow-through)
- **Mature stage**: Benevolence becomes most important (genuine care for interests)

Trust violations are asymmetric: easy to destroy, hard to rebuild.

## Agent Application

| Factor | Human Context | Agent Context |
|--------|---------------|---------------|
| Ability | Skills, experience | Model capabilities, domain performance |
| Integrity | Keeps commitments, honest | Follows instructions, reports honestly, acknowledges uncertainty |
| Benevolence | Wants good for trustor | Optimizes for actual goals, not just metrics |

### Trust Development Stages for Agents

1. **Ability testing** - Can the agent perform the task correctly?
2. **Integrity confirmation** - Does the agent follow instructions and report honestly?
3. **Benevolence evaluation** - Does the agent optimize for actual goals, not just surface metrics?

## Practical Implications

1. **Trust must be domain-specific** - High trust for formatting code does not transfer to architecture decisions

2. **Trust must be externally tracked** - Agents don't remember; the system must maintain trust state

3. **Trust development is incremental** - Start with ability tests, then integrity confirmation, then benevolence evaluation

4. **Trust drives autonomy** - Trust level should determine verification rates and scope of delegation

### Trust Violations

- Ability failures: "Agent couldn't do X" → Reduce scope, increase verification
- Integrity failures: "Agent didn't follow instructions" → Reset to high oversight
- Benevolence failures: "Agent optimized for wrong goal" → Fundamental reassessment

## Key Insight

Trust in agents is not binary ("trust or don't trust"). It's multi-dimensional (A, B, I), domain-specific, and should develop systematically through evidence. The framework provides a structured way to think about when to increase autonomy (demonstrated ability + integrity + benevolence) and when to pull back (violations of specific factors).
