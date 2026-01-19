# Satisficing and Bounded Rationality

Exploring Herbert Simon's theory of bounded rationality and satisficing as an alternative to optimization, with applications to AI agent design and supervision.

## Background

| Aspect | Description |
|--------|-------------|
| **Creator** | Herbert A. Simon (1916-2001) |
| **Core Insight** | Rationality is bounded by information, cognitive capacity, and time - optimization is often impossible |
| **Key Concept** | Satisficing: choosing options that are "good enough" rather than optimal |
| **Nobel Prize** | 1978 Economics Prize "for his pioneering research into the decision-making process within economic organizations" |
| **Foundational Works** | *Administrative Behavior* (1947), "A Behavioral Model of Rational Choice" (1955) |

## The Critique of Classical Rationality

### The Homo Economicus Model

Classical economics assumes a hypothetical agent - "homo economicus" or "economic man" - who:

| Assumption | Reality |
|------------|---------|
| **Complete information** | Decision makers rarely have full information about options |
| **Perfect foresight** | Consequences of choices are uncertain and unpredictable |
| **Unlimited computational capacity** | Human minds have severe processing limits |
| **Utility maximization** | People often don't know what they're optimizing for |
| **Stable preferences** | Preferences shift based on context and framing |

John Stuart Mill (1844) described this self-interested agent who maximizes personal utility. William Jevons (1871) formalized marginal utility. Frank Knight (1921) extended this to "slot-machine man" with perfect foresight and clearly defined risks.

### Simon's Challenge

Simon rejected this model as descriptively false and normatively misleading:

> "The capacity of the human mind for formulating and solving complex problems is very small compared with the size of the problems whose solution is required for objectively rational behavior in the real world."

**His key arguments:**

1. **Alternatives and consequences are partly unknown** - We can't evaluate what we can't see
2. **Means and ends are imperfectly differentiated** - Often unclear what we're optimizing for
3. **Computational limits are real** - Many problems are intractable even in principle
4. **Information is costly** - Acquiring more information has diminishing returns
5. **Time constraints bind** - Most decisions must be made under time pressure

Simon proposed replacing "economic man" (who maximizes) with "administrative man" (who satisfices).

## Bounded Rationality: The Three Constraints

Simon's 1955 paper proposed that human rationality is bounded by three critical limitations:

### 1. Limited Information

```
Perfect Rationality:    All options known → All consequences known → Choose best
                              ↓                    ↓                    ↓
Bounded Reality:        Options discovered   Consequences uncertain  Choose satisfactory
                        through search       and partially known
```

- Decision makers rarely have complete information about all possibilities
- Information must be searched for, at a cost
- The search process itself consumes resources and time
- Information arrives sequentially, not all at once

### 2. Limited Cognitive Capacity

| Capacity Limit | Impact on Decision Making |
|----------------|---------------------------|
| **Working memory** | Can only hold ~4 items simultaneously |
| **Attention** | Can focus on limited aspects of complex situations |
| **Computation** | Cannot process all combinations of variables |
| **Comparison** | Cannot simultaneously evaluate all tradeoffs |

The human mind has limited computational capacity for processing available information. Even with full information, we couldn't process it optimally.

### 3. Limited Time

- Most real-world decisions must be made under time constraints
- Time spent deciding is time not spent acting
- Deliberation has opportunity costs
- The environment changes while you're thinking

**The core insight:** These aren't failures to be corrected - they're fundamental features of being an agent in a complex world. Optimization isn't just difficult; it's often impossible in principle.

## Satisficing Defined

Simon coined "satisficing" (a portmanteau of "satisfy" and "suffice") to describe how bounded rational agents actually decide:

### The Basic Model

```
Step 1: Set an aspiration level α (threshold for "good enough")
Step 2: Search through available options
Step 3: Choose the first option that meets or exceeds α
Step 4: If no option satisfies α after time β, adjust α and continue
```

**Key characteristics:**

| Feature | Description |
|---------|-------------|
| **Sequential search** | Options evaluated one at a time, not simultaneously |
| **First satisfactory** | Stop at first acceptable option, don't compare all |
| **Threshold-based** | Success defined by meeting aspiration, not maximizing |
| **Adaptive** | Aspiration level adjusts based on experience |

### Satisficing vs. Optimizing

| Optimizing | Satisficing |
|------------|-------------|
| Evaluate all options | Evaluate until satisfactory found |
| Compare and rank | Accept or reject against threshold |
| Select the best | Select first good-enough |
| Requires complete information | Works with incomplete information |
| Computationally expensive | Computationally cheap |
| May never terminate | Guaranteed to terminate (with aspiration adjustment) |

## Aspiration Levels: The Dynamics of "Good Enough"

The aspiration level - what counts as "good enough" - is not fixed. It adapts to experience:

### Simon's Principle of Aspiration Adaptation

> "As the individual, in his exploration of alternatives, finds it easy to discover satisfactory alternatives, his aspiration level rises; as he finds it difficult to discover satisfactory alternatives, his aspiration level falls."

```
Easy success → Aspiration rises → Higher standards
Repeated failure → Aspiration falls → Lower standards
```

### The Adaptive Mechanism

| Search Outcome | Aspiration Adjustment | Effect |
|----------------|----------------------|--------|
| Quick success | Raise aspiration | Next time, demand more |
| Slow success | Maintain aspiration | Current level is appropriate |
| Prolonged failure | Lower aspiration | Make "good enough" easier to achieve |
| Continued failure | Lower further | Eventually, something becomes acceptable |

This adaptive process has important properties:

1. **Near-uniqueness**: Adjustments tend toward a "near-uniqueness" of satisfactory solutions
2. **Existence guarantee**: Failure depresses aspiration, which brings satisfactory solutions into existence
3. **Environmental fit**: Aspiration calibrates to what's actually achievable

### Empirical Example: Used Car Dealers

An analysis of 628 used car dealers showed that 97% relied on satisficing:

- Set initial price α in the middle of comparable cars' price range
- Lower price if car not sold after 24 days (β)
- Reduce by about 3% (γ) at each adjustment
- Dealers adapted parameters to their environment (decreased wait time by ~3% for each additional local competitor)

## When Satisficing is Optimal: The Computational Argument

Simon argued that satisficing isn't a failure mode - it's often the optimal strategy given constraints:

### The Nobel Prize Insight

From Simon's Nobel lecture:

> "Decision makers can satisfice either by finding optimum solutions for a simplified world, or by finding satisfactory solutions for a more realistic world. Neither approach, in general, dominates the other, and both have continued to co-exist in the world of management science."

### Why Optimization Can Be Worse

| Factor | Why Optimization Fails |
|--------|----------------------|
| **Computational intractability** | Many real problems are NP-hard or worse |
| **Model uncertainty** | The optimization model may not match reality |
| **Overfitting** | Optimizing for known data misses future patterns |
| **Brittleness** | Optimal solutions are sensitive to small changes |
| **Opportunity cost** | Time optimizing could be spent acting |

### The Meta-Optimization

There's a meta-level question: what's the optimal amount of optimization?

```
Total Cost = Decision Cost + Opportunity Cost of Delay + Suboptimality Cost

Optimizing:     High decision cost + High delay cost + Low suboptimality cost
Satisficing:    Low decision cost + Low delay cost + Moderate suboptimality cost
```

Often, satisficing minimizes total cost. The effort to find the "best" answer exceeds the value gained over a "good enough" answer.

## Satisficers vs. Maximizers: The Happiness Research

Barry Schwartz's research (*The Paradox of Choice*, 2004) extended Simon's framework to psychology:

### Two Decision-Making Styles

| Satisficer | Maximizer |
|------------|-----------|
| Seeks option meeting criteria | Seeks absolute best option |
| Stops when satisfied | Continues searching exhaustively |
| "Good enough" is enough | Only best is acceptable |
| Focuses on own standards | Compares to all alternatives |

### The Paradox: Maximizers Are Less Happy

Schwartz's research found:

| Finding | Explanation |
|---------|-------------|
| Maximizers score higher on depression scales | Constant comparison creates dissatisfaction |
| Maximizers experience more regret | Always wondering about unchosen options |
| Maximizers are more vulnerable to social comparison | Others' choices threaten their own |
| Satisficers are happier with decisions | Not haunted by "what if" |

> "Schwartz's studies show that people who are oriented toward maximizing are borderline clinically depressed."

### The Key Insight

Maximizers might get objectively better outcomes but experience subjectively worse ones:

```
Maximizer:   Better objective choice + Worse subjective experience = Net negative
Satisficer:  Good enough choice + Peace of mind = Net positive
```

**Schwartz's conclusion:** "Satisficing is, in fact, the maximizing strategy" - if what you're maximizing is well-being.

## Ecological Rationality: Gigerenzer's Extension

Gerd Gigerenzer and colleagues at the Max Planck Institute extended bounded rationality into "ecological rationality" - the study of how simple heuristics are matched to environments.

### The Adaptive Toolbox

Gigerenzer conceptualizes rational decisions in terms of:

1. **The adaptive toolbox** - the repertoire of heuristics an individual or institution has
2. **Ecological rationality** - the ability to choose a good heuristic for the task at hand

> "A heuristic is called ecologically rational to the degree that it is adapted to the structure of an environment."

### Fast-and-Frugal Heuristics

These are simple rules that work well despite (or because of) their simplicity:

| Heuristic | How It Works | Why It Works |
|-----------|--------------|--------------|
| **Recognition** | Choose what you recognize | Recognition correlates with quality in many domains |
| **Take-the-best** | Use the single best predictor | Avoids overfitting, robust to noise |
| **Satisficing** | Accept first option meeting threshold | Saves search cost, terminates quickly |
| **Fast-and-frugal trees** | Sequential yes/no decisions | Matches decision structure, prevents overthinking |

### The "Less is More" Effect

Gigerenzer's key finding: in many situations, simpler heuristics outperform complex optimization:

```
Traditional view:     More information → More computation → Better decisions
Gigerenzer's finding: Less information → Simpler heuristics → Sometimes better decisions
```

**When "less is more" occurs:**

| Condition | Why Heuristics Win |
|-----------|-------------------|
| **High uncertainty** | Complex models overfit to noise |
| **Small samples** | Not enough data to estimate parameters |
| **Unpredictable environments** | Future differs from past |
| **Time pressure** | Can't afford exhaustive analysis |

> "In situations of risk you can calculate the best answer - you can optimize. In situations of uncertainty, you can't."

### Empirical Evidence

Studies have shown heuristics outperform complex models in:

- Personnel selection (predicting job performance)
- Medical diagnosis (predicting heart attacks)
- Financial prediction (forecasting returns)
- Sports outcomes (predicting winners)

## Satisficing in Organizations

Cyert and March's *A Behavioral Theory of the Firm* (1963) applied Simon's framework to organizations:

### Key Concepts

#### 1. Sequential Attention to Goals

Organizations don't optimize across all goals simultaneously. They attend to goals sequentially:

```
Time 1: Focus on production efficiency
Time 2: Focus on market share
Time 3: Focus on employee satisfaction
Time 4: Return to production efficiency
```

This is organizational satisficing - meeting "good enough" thresholds on each goal, cycling through them, rather than simultaneously optimizing all.

#### 2. Problemistic Search

Search is:
- **Motivated by problems** - Not proactive, but reactive to performance gaps
- **Simple-minded** - Looks near the problem, not across the whole organization
- **Biased** - By goals, training, and experience of the searchers

> "Search is assumed to be motivated by problems, simple-minded in its causal models, and biased by goals and experiences."

#### 3. Organizational Slack

Organizational slack is the difference between total resources and necessary payments to maintain the organization:

| Form of Slack | Example |
|---------------|---------|
| **Excess payments** | Wages above market, high dividends |
| **Excess capacity** | Unused production capability |
| **Time buffers** | Schedule margins, deadline padding |
| **Inventory** | Stockpiled materials beyond immediate need |

**Functions of slack:**

- **Stabilization**: Absorbs environmental shocks
- **Conflict resolution**: Provides resources for competing coalitions
- **Innovation cushion**: Allows experimentation without immediate ROI pressure
- **Adaptation buffer**: Time to adjust when conditions change

> "Slack plays both a stabilising and an adaptive role."

---

## Application to AI Agents

### Do Agents Satisfice?

Yes - current AI agents exhibit clear satisficing behavior:

| Agent Behavior | Satisficing Equivalent |
|----------------|----------------------|
| **Produces plausible output** | Meets quality threshold |
| **Stops when response is "good enough"** | First satisfactory option |
| **Doesn't exhaustively evaluate alternatives** | Sequential, not parallel search |
| **Quality varies with prompt quality** | Aspiration influenced by context |

Agents don't search for optimal responses. They generate responses that meet implicit quality thresholds, influenced by training data, prompts, and context.

### What's the Agent's Aspiration Level?

The agent's aspiration level - what counts as "good enough" - is set by:

| Factor | How It Affects Aspiration |
|--------|---------------------------|
| **Training data** | Implicit standards from examples |
| **System prompt** | Explicit quality expectations |
| **User prompt specificity** | Detailed prompts raise expectations |
| **Few-shot examples** | Concrete standards for "good enough" |
| **Feedback within session** | Adjusts based on user response |

**The problem:** Unlike human satisficers, agents don't naturally adjust aspiration based on difficulty. They don't say "this is hard, so I'll accept lower quality." They try to meet the same implicit threshold regardless of problem tractability.

### How Should We Set Aspiration Levels for Agents?

This is a critical design question:

| Aspiration Level | Effect | When Appropriate |
|------------------|--------|------------------|
| **High** | More search, better output, slower, may fail to terminate | High-stakes decisions, ample time |
| **Medium** | Balanced search, adequate output, reasonable speed | Most tasks |
| **Low** | Quick response, "good enough" output, fast | Time pressure, low stakes |

**Practical levers:**

```markdown
# High aspiration
"Find the best solution. Consider multiple approaches. Explain tradeoffs."

# Medium aspiration
"Solve this problem. A working solution is fine."

# Low aspiration
"Quick answer needed. Don't overthink it."
```

### When Should Agents Search More vs. Accept Current Solution?

Map to decision importance and uncertainty:

| Situation | Recommended Strategy |
|-----------|---------------------|
| **High stakes, low uncertainty** | Optimize - search exhaustively |
| **High stakes, high uncertainty** | Satisfice with high aspiration - limit search time but maintain standards |
| **Low stakes, low uncertainty** | Satisfice with low aspiration - quick and done |
| **Low stakes, high uncertainty** | Satisfice with medium aspiration - reasonable effort, accept uncertainty |

### Organizational Slack for Agent Systems

What's the equivalent of organizational slack for agent systems?

| Human Organization Slack | Agent System Equivalent |
|-------------------------|------------------------|
| **Excess budget** | Token budget buffers |
| **Time padding** | Timeout margins |
| **Excess capacity** | Compute headroom |
| **Inventory buffers** | Cached results, pre-computed data |
| **Redundant capabilities** | Fallback models, parallel agents |

**Functions in agent systems:**

- **Error absorption**: Retry capacity when first attempt fails
- **Quality improvement**: Extra tokens for refinement
- **Adaptation room**: Capacity to handle unexpected complexity
- **Experimentation**: Resources for trying alternative approaches

### When Should We WANT Agents to Satisfice vs. Optimize?

| Want Satisficing | Want Optimizing |
|------------------|-----------------|
| Speed matters | Quality matters more than speed |
| Cost is constrained | Resources are abundant |
| "Good enough" is actually good enough | Marginal improvement has high value |
| High uncertainty (optimization overfits) | Low uncertainty (optimization achievable) |
| Reversible decisions | Irreversible decisions |
| Learning/exploration phase | Exploitation phase |

**The key question:** What's the cost of a suboptimal solution vs. the cost of searching for a better one?

---

## Practical Implications

### For Agent Prompting

1. **Make aspiration levels explicit**

   Instead of: "Solve this problem"

   Try: "Find a working solution. It doesn't need to be perfect, just functional and maintainable."

2. **Specify stopping criteria**

   Instead of: "Make it faster"

   Try: "Make it at least 2x faster. Stop when you achieve that."

3. **Distinguish satisficing from optimizing tasks**

   "Find the best approach" (optimizing) vs. "Find a good approach" (satisficing)

### For Agent System Design

1. **Build in aspiration adaptation**

   If agent struggles, lower expectations. If agent succeeds easily, raise them.

2. **Implement organizational slack**

   Budget extra tokens, time, and compute for unexpected complexity.

3. **Use sequential attention**

   Focus on one objective at a time rather than trying to optimize all simultaneously.

4. **Enable problemistic search**

   Start search at the problem location, expand outward only if needed.

### For Supervision

1. **Match supervision to stakes**

   High-stakes tasks deserve more scrutiny; let low-stakes satisficing pass.

2. **Set appropriate quality thresholds**

   Define what "good enough" means for each task type.

3. **Monitor aspiration drift**

   Watch for agents accepting lower quality over time or demanding unnecessary perfection.

---

## Key Insight

**Satisficing isn't a failure mode - it's often the OPTIMAL strategy given constraints.**

Simon's profound insight was that when you account for:
- The cost of search
- The limits of computation
- The uncertainty of the environment
- The time pressure of decisions

...then "good enough" is often the rational choice. Trying to optimize under bounded rationality can produce worse outcomes than satisficing, because:

1. You waste resources searching for improvements that don't exist
2. You may never reach a decision at all
3. The "optimal" solution may be based on a model that doesn't match reality
4. By the time you find the optimum, the world has changed

For AI agents, this means:
- Design systems that satisfice appropriately rather than optimizing everything
- Make aspiration levels explicit and adaptive
- Build in organizational slack for error absorption and adaptation
- Know when "good enough" truly is good enough

> "As Simon observed in his Nobel Prize in Economics speech: 'decision makers can satisfice either by finding optimum solutions for a simplified world, or by finding satisfactory solutions for a more realistic world. Neither approach, in general, dominates the other.'"

---

## Open Questions

1. **Aspiration calibration for agents**: How do we calibrate what "good enough" means for agents across different task types?

2. **Adaptive aspiration**: Can agents learn to adjust their aspiration levels based on task difficulty?

3. **Organizational slack sizing**: How much slack should agent systems carry? Too much is waste; too little is fragile.

4. **Maximizer tendency in agents**: Do agents trained on human feedback develop maximizer tendencies (always seeking "best" responses)?

5. **Meta-satisficing**: When should an agent satisfice about whether to satisfice?

6. **Quality vs. confidence**: How does aspiration level relate to agent confidence/certainty expressions?

7. **Multi-agent satisficing**: How do aspiration levels interact when multiple agents collaborate?

---

## Related Frameworks

- **Recognition-Primed Decision Making** (Klein): Experts satisfice by recognizing patterns and retrieving typical responses
- **Cynefin Framework** (Snowden): Clear domain allows satisficing; Complex domain may require exploration before satisficing is possible
- **OODA Loop** (Boyd): Fast OODA cycles are a form of satisficing - act on partial information, adjust
- **Dual Process Theory** (Kahneman): System 1 satisfices quickly; System 2 optimizes slowly

---

## Sources

### Primary Sources
- Simon, Herbert A. "A Behavioral Model of Rational Choice." *Quarterly Journal of Economics* 69, no. 1 (1955): 99-118.
- Simon, Herbert A. *Administrative Behavior*. 1947.
- Simon, Herbert A. *Models of Bounded Rationality*. MIT Press, 1982.
- Simon, Herbert A. Nobel Prize Lecture: "Rational Decision-Making in Business Organizations." 1978.

### Extensions and Applications
- Cyert, Richard M., and James G. March. *A Behavioral Theory of the Firm*. 1963.
- Gigerenzer, Gerd, and Peter M. Todd. *Simple Heuristics That Make Us Smart*. Oxford University Press, 1999.
- Schwartz, Barry. *The Paradox of Choice: Why More Is Less*. Harper Perennial, 2004.

### Web Resources
- [Bounded Rationality - Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/bounded-rationality/)
- [Satisficing - Wikipedia](https://en.wikipedia.org/wiki/Satisficing)
- [Herbert A. Simon - Nobel Prize Lecture](https://www.nobelprize.org/prizes/economic-sciences/1978/simon/lecture/)
- [Gerd Gigerenzer - Wikipedia](https://en.wikipedia.org/wiki/Gerd_Gigerenzer)
- [A Behavioral Theory of the Firm - Wikipedia](https://en.wikipedia.org/wiki/A_Behavioral_Theory_of_the_Firm)

---

## Status

**Phase:** Research complete. Simon's satisficing framework provides a rigorous alternative to optimization-based thinking. Key insight: bounded rationality makes satisficing not just practical but often optimal. Direct applications to agent design include explicit aspiration levels, organizational slack, and adaptive quality thresholds.
