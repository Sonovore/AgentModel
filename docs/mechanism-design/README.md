# Mechanism Design

Mental models from economics, game theory, and incentive design applied to AI agent systems.

## Purpose

Mechanism design asks: how do you design systems where self-interested agents produce desired outcomes? While AI agents don't have "interests" in the human sense, the frameworks for analyzing incentives, information asymmetry, and strategic behavior still apply.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Foundational Concepts

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Incentive Compatibility | Hurwicz | Designing systems where truth-telling is optimal |
| Revelation Principle | Myerson | Any outcome achievable through direct mechanism |
| Individual Rationality | Participation constraints | Why would agents participate? |
| Mechanism Design Basics | Maskin | The "inverse game theory" approach |

### Information Problems

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Adverse Selection | Akerlof | Hidden information before contracting |
| Moral Hazard | Arrow | Hidden action after contracting |
| Signaling | Spence | Costly signals of private information |
| Screening | Rothschild-Stiglitz | Designing choices that reveal types |
| Principal-Agent Problem | Economics | Information asymmetry in delegation |

### Auction Theory

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| First-Price Auction | Auction theory | Highest bid wins, pays bid |
| Second-Price Auction | Vickrey | Highest bid wins, pays second-highest |
| Revenue Equivalence | Myerson | Different formats, same expected revenue |
| Combinatorial Auctions | Multi-item | Bidding on bundles |
| Matching Markets | Roth & Shapley | Two-sided matching (stable marriage) |

### Game Theory Foundations

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Nash Equilibrium | Nash | Mutual best response |
| Pareto Efficiency | Welfare economics | No one can improve without harming another |
| Prisoner's Dilemma | Game theory | Individual vs collective rationality |
| Coordination Games | Game theory | Multiple equilibria, need to coordinate |
| Repeated Games | Folk theorem | Cooperation through repetition |

### Contract Theory

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Complete vs Incomplete Contracts | Hart & Moore | What can be specified in advance? |
| Renegotiation | Contract theory | Changing terms as information revealed |
| Commitment Devices | Behavioral economics | Making future actions credible |
| Option Contracts | Finance | Rights without obligations |

### Social Choice

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Arrow's Impossibility | Arrow | No perfect voting system |
| Condorcet Paradox | Social choice | Cyclic preferences |
| Median Voter Theorem | Political economy | Converging to middle |
| Strategyproof Mechanisms | Gibbard-Satterthwaite | Preventing manipulation |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| Moral Hazard | Very High | Medium | 1 |
| Adverse Selection | High | Medium | 1 |
| Incentive Compatibility | High | High | 1 |
| Commitment Devices | High | Low | 2 |
| Screening | Medium | Medium | 2 |
| Repeated Games | Medium | Medium | 2 |
| Incomplete Contracts | Medium | High | 3 |
| Auction Theory | Low | High | 3 |

## Key Questions

1. Do AI agents have "incentives"? (Not really, but they optimize for objectives that function like incentives)
2. What's "moral hazard" for agents? (Agent taking shortcuts when not observed)
3. How do we design "incentive compatible" prompts? (Where the obvious interpretation is the intended one)
4. What's the equivalent of "screening" - designing tasks that reveal agent capability?
5. Can we use "commitment devices" - ways agents can credibly commit to behaviors?

## Related Directories

- [Management](../management/) - Principal-Agent theory
- [Legal Agency](../legal-agency/) - Duty structures
- [Cognitive Science](../cognitive-science/) - Decision making under constraints
