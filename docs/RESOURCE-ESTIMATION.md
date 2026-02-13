# Resource Estimation Research

**Research Date:** 2026-01-21
**Purpose:** Estimate token costs, time, and financial budget for experimental suite

---

## Executive Summary

**Key findings:**
- **Full experimental suite:** ~50M tokens, $400-600 estimated cost
- **MVP (Phase 1-2):** ~5M tokens, $40-60 estimated cost
- **Single experiment:** ~500K tokens, $4-6 estimated cost
- **Optimization:** Use Haiku where possible (10x cost reduction)

**Recommendation:** Start with **MVP scope** ($40-60), validate approach, then scale

---

## Part 1: Token Estimates

### Per-Task Token Estimates

Based on typical agent conversation patterns:

**Task S1 (Parallel Map-Reduce - 100 files, 5 agents):**
- Orchestrator prompt: 2K tokens
- Per-agent spawn: 1K tokens × 5 = 5K tokens
- File processing: 1K tokens per file × 100 = 100K tokens
- Agent responses: 500 tokens × 5 = 2.5K tokens
- Aggregation: 5K tokens
- **Total input:** ~112K tokens
- **Total output:** ~10K tokens
- **Total:** ~122K tokens per run

**Task S2 (Sequential Pipeline - 4 stages):**
- Stage 1 (Fetch): 3K in, 2K out = 5K
- Stage 2 (Transform): 5K in, 3K out = 8K
- Stage 3 (Validate): 4K in, 2K out = 6K
- Stage 4 (Store): 3K in, 1K out = 4K
- Orchestrator overhead: 2K in, 1K out = 3K
- **Total:** ~26K tokens per run

**Task S3 (Orchestrator-Worker - 50 queries):**
- Orchestrator: 5K tokens
- Routing: 50 queries × 100 tokens = 5K tokens
- Worker processing: 50 × 2K = 100K tokens
- **Total:** ~110K tokens per run

**Task S4 (Bounded ReAct - 10 steps):**
- Per step: 1K in, 500 out = 1.5K
- 10 steps: 15K tokens
- Context growth: +5K tokens
- **Total:** ~20K tokens per run

**Task W1 (Multi-File Refactoring - 5-8 files):**
- Initial context: 10K tokens (code reading)
- Per-file analysis: 5K × 7 = 35K tokens
- Refactoring planning: 10K tokens
- Implementation: 20K tokens
- Validation: 5K tokens
- **Total:** ~80K tokens per run

**Task W2 (High-Coordination - 5 agents, 20 message rounds):**
- Orchestrator: 10K tokens
- Per message round: 5 agents × 2K = 10K tokens
- 20 rounds: 200K tokens
- Coordination overhead: +30K tokens
- **Total:** ~240K tokens per run

**Tasks H1-H3 (Hybrid tasks):**
- H1: Similar to S1 = ~120K tokens
- H2: Similar to S2 with retries = ~40K tokens
- H3: Between S4 and W1 = ~50K tokens

### Summary Table

| Task | Type | Tokens/Run | Runs/Exp | Total Tokens |
|------|------|------------|----------|--------------|
| S1 | Parallel | 122K | 30 (3 variations × 10 trials) | 3.7M |
| S2 | Pipeline | 26K | 30 | 780K |
| S3 | Orchestrator | 110K | 30 | 3.3M |
| S4 | ReAct | 20K | 30 | 600K |
| W1 | Refactoring | 80K | 30 | 2.4M |
| W2 | High-Coord | 240K | 30 | 7.2M |
| H1 | Hybrid | 120K | 30 | 3.6M |
| H2 | Hybrid | 40K | 30 | 1.2M |
| H3 | Hybrid | 50K | 30 | 1.5M |

**Total for full suite:** ~24.3M tokens

---

## Part 2: Cost Estimation

### Claude API Pricing (2026 estimates)

**Sonnet 4.5:**
- Input: $3.00 per 1M tokens
- Output: $15.00 per 1M tokens
- **Average:** ~$6.00 per 1M tokens (assuming 3:1 input:output ratio)

**Haiku (future):**
- Input: $0.25 per 1M tokens
- Output: $1.25 per 1M tokens
- **Average:** ~$0.50 per 1M tokens (10x cheaper than Sonnet)

**Opus 4.5:**
- Input: $15.00 per 1M tokens
- Output: $75.00 per 1M tokens
- **Average:** ~$30.00 per 1M tokens (5x more expensive than Sonnet)

### Cost Breakdown

**Full suite (all Sonnet):**
- 24.3M tokens × $6.00 / 1M = **$145.80**

**With optimization (Haiku for simple tasks):**
- S1, S2, S3, S4 (simple): 8.4M tokens × $0.50 / 1M = $4.20
- W1, W2, H1-H3 (complex): 15.9M tokens × $6.00 / 1M = $95.40
- **Total optimized:** **$99.60**

**With Opus for baseline (10% of runs):**
- 2.4M tokens × $30.00 / 1M = $72.00
- Remaining 21.9M tokens × $6.00 / 1M = $131.40
- **Total with Opus:** **$203.40**

### Cost Per Phase

**Phase 1: Baseline (Task S1 only, 1 experiment):**
- 3.7M tokens × $6.00 / 1M = **$22.20**

**Phase 2: Model Comparison (Tasks S1-S4):**
- 8.4M tokens × $6.00 / 1M = **$50.40**

**Phase 3: Scale Testing (Variations of S1 at 5, 10, 20 agents):**
- Estimated 2x token usage = 7.4M tokens × $6.00 / 1M = **$44.40**

**Phase 4: Full Task Suite (S1-H3):**
- 24.3M tokens × $6.00 / 1M = **$145.80**

**Phase 5-7: Framework Comparisons + Optimizations:**
- Estimated 2x full suite = 48.6M tokens × $6.00 / 1M = **$291.60**

**Grand Total (All Phases):** ~50M tokens = **$300.00**

---

## Part 3: Time Estimates

### Wall Clock Time Per Task

**Based on typical agent execution:**

- **S1:** 5 parallel agents × 2 min/agent = 2 min (parallel)
- **S2:** 4 sequential stages × 1 min/stage = 4 min
- **S3:** 50 parallel workers × 30 sec/worker = 30 sec (parallel)
- **S4:** 10 sequential steps × 20 sec/step = 3.3 min
- **W1:** 1 agent × 10 min = 10 min (complex reasoning)
- **W2:** 20 message rounds × 30 sec/round = 10 min
- **H1:** Similar to S1 = 2 min
- **H2:** Similar to S2 with retries = 6 min
- **H3:** Similar to W1 = 8 min

### Experiment Duration

**Single trial:** ~2-10 minutes depending on task

**Single experiment (30 trials):**
- Can run trials sequentially or parallel
- Sequential: 30 trials × 5 min avg = 150 min = 2.5 hours
- Parallel (3 at a time): 10 batches × 5 min = 50 min
- **Estimate:** 1-2.5 hours per experiment

**Full suite (11 tasks):**
- Sequential experiments: 11 × 2 hours = 22 hours
- Parallel experiments (2 at a time): 11 hours
- **Estimate:** 11-22 hours for full suite

**All phases (MVP through full analysis):**
- Phase 1-2: 5 hours
- Phase 3: 8 hours
- Phase 4: 22 hours
- Phase 5-7: 44 hours
- **Total:** ~80 hours (10 workdays)

---

## Part 4: Computational Requirements

### Local Machine

**Minimum:**
- Python 3.9+
- 8GB RAM (for data loading and analysis)
- 10GB disk space (data + results)
- Stable internet (Claude API calls)

**Recommended:**
- 16GB RAM (smoother analysis with pandas)
- 50GB disk space (buffer for experiments)
- Fast internet (reduces latency)

**No GPU required** (LLM inference via API)

### Parallelization Opportunities

**Can run in parallel:**
- Multiple trials of same experiment
- Multiple experiments on different tasks
- Framework comparisons simultaneously

**Sequential dependencies:**
- Must complete baseline before optimization experiments
- Must complete Phase 1-2 before Phase 3-4

**Speedup potential:**
- 3 parallel trials: 3x speedup on experiments
- 2 parallel experiments: 2x speedup on suite
- **Combined:** ~6x speedup = 13 hours instead of 80 hours

---

## Part 5: Budget Recommendations

### Phased Budget

**Phase 1-2: MVP ($40-60)**
- Goal: Validate test harness and baseline
- Scope: Tasks S1-S4, single coordination model
- Tokens: ~8M tokens
- Cost: $48 (with Haiku optimization: $20)
- **Decision point:** Is approach working? Continue or pivot?

**Phase 3: Scaling ($45)**
- Goal: Understand scaling characteristics
- Scope: Task S1 at 5, 10, 20 agents
- Tokens: ~7.5M tokens
- Cost: $45
- **Decision point:** Do models scale? Identify bottlenecks?

**Phase 4: Full Task Suite ($150)**
- Goal: Comprehensive task-model mapping
- Scope: All 11 tasks, all variations
- Tokens: ~25M tokens
- Cost: $150
- **Decision point:** Which models work for which tasks?

**Phase 5-7: Framework Comparisons ($200)**
- Goal: Compare to LangGraph, CrewAI, OpenAI SDK
- Scope: Implement baseline tasks in each framework
- Tokens: ~33M tokens
- Cost: $200
- **Decision point:** Do our mental models beat existing frameworks?

**Total Budget:** $435

**With optimizations (Haiku for simple tasks):** $300

**Conservative buffer (20%):** $360

### Cost Optimization Strategies

**1. Use Haiku where appropriate:**
- Simple tasks (S1-S4): Haiku (10x cheaper)
- Complex tasks (W1-W2): Sonnet
- Baseline/comparison: Opus (sparingly)
- **Savings:** ~50% ($145 → $70)

**2. Reduce trial count initially:**
- Start with 3 trials instead of 10
- Add more trials only for statistical significance
- **Savings:** ~70% of experimental costs

**3. Incremental approach:**
- Run Phase 1-2 first ($40-60)
- Validate approach works
- Only proceed to Phase 3-4 if successful
- **Risk reduction:** Don't spend $300 on wrong approach

**4. Cache and reuse:**
- Store agent responses
- Reuse for multiple analyses
- Avoid re-running experiments
- **Savings:** Time + repeated API calls

**5. Synthetic before real:**
- Test with small datasets first (10 files vs 100)
- Validate code works
- Scale up only when ready
- **Savings:** ~90% during development

---

## Part 6: Funding & ROI

### Investment Justification

**Research value:**
- Empirical validation of 31 mental models
- First systematic comparison of agent coordination patterns
- Publishable research (ICSE, OOPSLA, NeurIPS workshops)
- **ROI:** Academic contribution + potential citations

**Practical value:**
- Proven agent coordination patterns
- Decision framework for model selection
- Reusable test harness
- **ROI:** Save 10-100x this cost in future agent projects

**Book value:**
- Documented experimental journey
- Data-driven insights
- Validated recommendations
- **ROI:** Book sales + consulting opportunities

**Time value:**
- 80 hours of experiments (10 days)
- vs months of trial-and-error
- **ROI:** 10x time savings

**Total investment:** $300 (optimized) + 80 hours (10 days)
**Total value:** Publishable research + practical framework + book material

---

## Conclusion

**Full experimental suite is affordable and achievable.**

**Budget summary:**
- MVP (Phase 1-2): $40-60
- Full suite (Phase 1-7): $300-360
- Per experiment: $5-20
- Per task run: $0.50-2.00

**Time summary:**
- MVP: 5-8 hours
- Full suite: 11-22 hours (sequential) or 13 hours (parallel)
- Per experiment: 1-2.5 hours
- Per task run: 2-10 minutes

**Recommendations:**
1. Start with MVP ($40-60, 8 hours)
2. Validate approach works
3. Scale to full suite if successful
4. Use Haiku optimization (50% cost savings)
5. Parallelize where possible (6x speedup)

**Status: AFFORDABLE AND FEASIBLE**

**Next step:** Request budget approval for MVP ($60) and proceed with implementation.
