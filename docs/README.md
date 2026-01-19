# Mental Models for Agent Governance

A multi-disciplinary collection of frameworks for understanding and designing AI agent supervision systems.

## Philosophy

**Surface-level understanding is dangerous.** Many of these models have popular interpretations that miss the actual insight. OODA Loop is not "observe then orient then decide then act" - it's about implicit guidance and control, Einheit (shared mental models), and tempo as weapon. The surface description is actively misleading.

For each model, we aim for 2-3 layers of depth beyond the Wikipedia summary.

## Directories

| Directory | Focus | Status |
|-----------|-------|--------|
| [management/](management/) | Org behavior, decision science, supervision | Active |
| [control-theory/](control-theory/) | Feedback, stability, observability | Identified |
| [safety-engineering/](safety-engineering/) | Failure, resilience, human factors | Identified |
| [legal-agency/](legal-agency/) | Authority, liability, fiduciary duty | Identified |
| [distributed-systems/](distributed-systems/) | Consensus, consistency, coordination | Identified |
| [mechanism-design/](mechanism-design/) | Incentives, information asymmetry | Identified |
| [biology-cas/](biology-cas/) | Emergence, swarms, adaptation | Identified |
| [cognitive-science/](cognitive-science/) | Bounded rationality, attention, expertise | Identified |

## Models Requiring Deep Dives

These models are "icebergs" - the popular understanding is the tip, and the real value is below the surface.

### Critical (Get These Wrong = Misapply Everything)

| Model | Directory | Surface Understanding | What's Actually Important |
|-------|-----------|----------------------|---------------------------|
| **OODA Loop** | management | Linear cycle: O→O→D→A | Implicit guidance, Einheit, Orient as bottleneck, tempo, multiple feedback shortcuts |
| **Principal-Agent Theory** | management | Information asymmetry | Hidden action vs hidden information, incentive design impossibility, monitoring costs |
| **CAP Theorem** | distributed-systems | "Pick two of three" | The tradeoff is during partitions; PACELC extends to latency; most systems are CA until they're not |
| **Feedback Loops** | control-theory | "Feedback is good" | Gain, bandwidth, phase margin, when feedback causes oscillation, derivative kick |
| **Normal Accident Theory** | safety-engineering | "Accidents are normal" | Tight coupling + interactive complexity = system accidents; linear vs complex interactions |
| **Mechanism Design** | mechanism-design | "Design good incentives" | Revelation principle, why incentive compatibility is hard, impossibility theorems |

### Important (Surface Works Sometimes, But Fails in Edge Cases)

| Model | Directory | Surface Understanding | Depth Required |
|-------|-----------|----------------------|----------------|
| **Cynefin** | management | Four quadrants of problems | Boundary dynamics, how to probe, the disorder space, ritual dissent |
| **Situational Leadership** | management | Match style to readiness | The "selling" style doesn't translate to agents; development isn't linear |
| **PID Control** | control-theory | P + I + D | Tuning methods (Ziegler-Nichols), integral windup, derivative noise, cascade PID |
| **Swiss Cheese Model** | safety-engineering | Holes must align | The holes are dynamic, drift, organizational factors, active vs latent failures |
| **Vicarious Liability** | legal-agency | Boss liable for employee | Scope of employment, independent contractor exception, borrowed servant doctrine |
| **Eventual Consistency** | distributed-systems | "Eventually converges" | Conflict resolution strategies, CRDTs, vector clocks for causality |
| **Dual Process Theory** | cognitive-science | Fast intuition vs slow reasoning | When System 1 overrides System 2, attribute substitution, cognitive ease |

### Moderate (Surface Is Useful, Depth Adds Nuance)

| Model | Directory | Why Depth Matters |
|-------|-----------|-------------------|
| **ICS** | management | Scaling rules, transfer of command, unified command for multi-jurisdictional |
| **Trust Development** | management | Time dynamics, domain specificity, violation asymmetry |
| **Circuit Breaker** | management | Half-open testing, exponential backoff, dependency-aware breakers |
| **Stability** | control-theory | Lyapunov methods, Bode plots, gain/phase margins |
| **STAMP/STPA** | safety-engineering | Control structure analysis, loss scenarios, constraints |
| **Two-Phase Commit** | distributed-systems | Blocking problem, coordinator failure, three-phase as solution |
| **Satisficing** | cognitive-science | How organisms set aspiration levels, adaptive search |

## Models That Are Simpler Than They Seem

Some models are actually straightforward once you understand them. Don't over-complicate.

| Model | Directory | It's Just... |
|-------|-----------|--------------|
| **RACI** | management | Make one person accountable. That's it. |
| **Ashby's Law** | management | Variety must match variety. Controllers need as many states as controlled. |
| **Heartbeats/Timeouts** | distributed-systems | Ping and wait. The tradeoffs are in timeout values. |
| **Chunking** | cognitive-science | Group related things. 7±2 chunks, or 4 for working memory. |

## Models Requiring Careful Translation

These don't map directly. The metaphor is useful but the mechanism doesn't transfer.

| Model | Directory | Why Translation Is Hard |
|-------|-----------|------------------------|
| **Stigmergy** | biology-cas | Agents don't leave persistent environment traces the same way |
| **Immune System** | biology-cas | No "self" to recognize; no clonal expansion |
| **Evolution** | biology-cas | Agents don't reproduce, mutate, or die |
| **Deliberate Practice** | cognitive-science | Agents don't learn from practice within session |
| **Commitment Devices** | mechanism-design | Agents can't constrain their future behavior |

## Research Strategy

1. **Start with highest-leverage icebergs**: OODA, Principal-Agent, CAP, Feedback Loops, Normal Accidents
2. **Build vocabulary**: Each field has precise terms that prevent confusion
3. **Find the primary sources**: Wikipedia summaries are insufficient
4. **Look for failed applications**: Where did the model fail? That reveals limits.
5. **Cross-reference**: When two fields describe the same thing differently, that's signal

## Related Documents

- [Agent Management Framework](agent-management-framework.md) - Synthesized guidance
- [Agent Types](agent-types.md) - Agent specializations
- [Agent Task System](agent-task-system.md) - Coordination patterns
