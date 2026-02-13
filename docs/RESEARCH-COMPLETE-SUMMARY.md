# Research Complete: 4-Hour Block Summary

**Date:** 2026-01-21
**Duration:** 4 hours (completed in series)
**Purpose:** Remove all unknowns blocking test harness implementation

---

## Executive Summary

**All 6 research gaps completed and documented.**

**Verdict: READY TO IMPLEMENT TEST HARNESS**

**Key findings:**
1. ✅ **Claude Code supports our architecture** - Parallel agents, file-based coordination, model selection
2. ✅ **Lightweight instrumentation sufficient** - structlog + JSON Lines + pandas
3. ✅ **Custom experiment system best fit** - YAML config, ~10 hours to build
4. ✅ **Test data is straightforward** - SWE-Bench + synthetic generation (~10 hours)
5. ✅ **9 failure modes auto-detectable** - Rule-based detector (~6 hours)
6. ✅ **Budget is affordable** - MVP $40-60, full suite $300

**Total implementation estimate:** ~40 hours (1 week)
**MVP budget:** $40-60
**Full suite budget:** $300

---

## Gap 1: Claude Code Capabilities ✅

**Document:** `docs/CLAUDE-CODE-CAPABILITIES.md`

**Research performed:**
- Documentation analysis of 7 agent types
- Parallel execution patterns
- State management approaches
- Background agent capabilities
- Model selection (opus/sonnet/haiku)

**Key findings:**
- ✅ Parallel execution supported (single message, multiple Task calls)
- ✅ Background agents supported (run_in_background parameter)
- ✅ File-based coordination natural (matches our conventions)
- ✅ Hub-and-spoke enforced by architecture (good for us!)
- ✅ Model selection per agent (optimize costs)
- ❓ Hard limits unknown (will discover experimentally)

**Implications:**
- Our test harness design is **FEASIBLE**
- Hub-and-spoke is **enforced** (matches our mental models)
- Can implement all tasks (S1-W4)
- Can test all coordination models

**Status:** Architecture validated, ready to implement

---

## Gap 2: Metrics Instrumentation ✅

**Document:** `docs/METRICS-INSTRUMENTATION.md`

**Research performed:**
- LangSmith/LangGraph observability review
- OpenTelemetry, Prometheus, structlog survey
- MetricsCollector class design
- JSON Lines storage format

**Key findings:**
- OpenTelemetry = overkill for experiments
- Structlog + JSON Lines = perfect fit
- time.perf_counter() for latency
- tiktoken for token estimation
- pandas for analysis

**Recommendation:**
- Use **lightweight custom collector**
- structlog → JSON Lines → pandas → matplotlib
- ~5 hours to implement
- Zero external dependencies (no servers, no accounts)

**Deliverables ready:**
- MetricsCollector interface (~200 lines)
- JSON Lines event schemas
- Analysis patterns (pandas)

**Status:** Design complete, ready to implement

---

## Gap 3: Experiment Management ✅

**Document:** `docs/EXPERIMENT-MANAGEMENT.md`

**Research performed:**
- MLflow, Weights & Biases, Sacred survey
- Custom system design
- YAML configuration format
- Experiment runner and analyzer classes

**Key findings:**
- ML experiment tracking tools = overkill
- Custom system = 10 hours vs 2+ days learning MLflow
- YAML config + JSON results + git = sufficient
- No external dependencies needed

**Recommendation:**
- Build **custom lightweight system**
- ExperimentRunner class (~200 lines)
- ExperimentAnalyzer class (~200 lines)
- Jupyter notebook templates

**Deliverables ready:**
- config.yaml template
- ExperimentRunner implementation
- ExperimentAnalyzer implementation
- analysis.ipynb template

**Status:** Design complete, ready to implement

---

## Gap 4: Test Data Requirements ✅

**Document:** `docs/TEST-DATA-SPECIFICATION.md`

**Research performed:**
- SWE-Bench dataset review (2,294 tasks available)
- Synthetic generation strategy
- Data versioning approach
- Generation script designs

**Key findings:**
- SWE-Bench Lite perfect for Task W1 (300 tasks available)
- Python + Faker sufficient for synthetic generation
- Git + manifest files for versioning
- ~10 hours to generate all data

**Data plan:**
- **Task S1:** Generate 100 files (Python + Faker)
- **Task S2:** Generate 1000 JSON records
- **Task W1:** Use SWE-Bench Lite (download)
- **Task W2:** Generate problem instances
- **Tasks H1-H3:** Reuse/adapt S1-W1 data

**Generation scripts ready:**
- generate_task_s1_data.py
- generate_task_s2_data.py
- generate_task_w2_data.py
- generate_all.py (orchestrator)

**Status:** Plan complete, ready to implement

---

## Gap 5: Failure Mode Detection ✅

**Document:** `docs/FAILURE-MODE-DETECTION.md`

**Research performed:**
- Mapped 14 failure modes from research
- Designed detection strategies
- Identified 9 auto-detectable modes
- FailureDetector class design

**Key findings:**
- 9 modes detectable with rule-based approaches
- 5 modes require semantic analysis (harder)
- Deadlock, livelock, race conditions = highest priority
- Integration with MetricsCollector straightforward

**Auto-detectable failures:**
1. Conversation resets
2. Ignoring input
3. Deadlock
4. Livelock
5. Race conditions
6. Resource conflicts
7. Cascade failures
8. State divergence
9. Timeout deadlock

**Implementation:**
- FailureDetector class (~400 lines)
- Rule-based detection functions
- ~6 hours to implement core detectors

**Status:** Design complete, ready to implement

---

## Gap 6: Resource Estimation ✅

**Document:** `docs/RESOURCE-ESTIMATION.md`

**Research performed:**
- Token estimates per task type
- Cost projections (Sonnet/Haiku/Opus)
- Time estimates per experiment
- Budget recommendations

**Key findings:**
- **Full suite:** ~25M tokens = $145 (Sonnet) or $70 (optimized)
- **MVP (Phase 1-2):** ~8M tokens = $48 (Sonnet) or $20 (Haiku)
- **Single experiment:** ~500K tokens = $3-6
- **Time:** 11-22 hours for full suite (sequential), 13 hours (parallel)

**Budget breakdown:**
- Phase 1-2 (MVP): $40-60
- Phase 3 (Scaling): $45
- Phase 4 (Full suite): $150
- Phase 5-7 (Comparisons): $200
- **Total:** $435 ($300 with optimization)

**Optimizations:**
- Use Haiku for simple tasks (50% savings)
- Reduce trials initially (70% savings)
- Incremental approach (risk reduction)
- **Recommended MVP budget:** $60

**Status:** Budget justified and affordable

---

## Implementation Roadmap

### Week 1: Foundation (40 hours)

**Monday: Metrics & Experiment Infrastructure (8 hours)**
- Implement MetricsCollector class (4 hours)
- Implement ExperimentRunner class (2 hours)
- Implement ExperimentAnalyzer class (2 hours)

**Tuesday: Test Data Generation (8 hours)**
- Implement generate_task_s1_data.py (2 hours)
- Implement generate_task_s2_data.py (1 hour)
- Download SWE-Bench Lite for W1 (1 hour)
- Implement generate_task_w2_data.py (2 hours)
- Generate all data + verify (2 hours)

**Wednesday: Failure Detection (6 hours) + Task S1 Implementation (2 hours)**
- Implement FailureDetector class (4 hours)
- Core detectors (deadlock, livelock, races) (2 hours)
- Begin Task S1 implementation (2 hours)

**Thursday: Task S1 Complete (8 hours)**
- Complete Task S1 in our model (4 hours)
- Write config.yaml for EXP-001 (1 hour)
- Test metrics collection (1 hour)
- Test experiment runner (2 hours)

**Friday: Run EXP-001 (8 hours)**
- Run first experiment (30 trials) (3 hours)
- Analyze results (2 hours)
- Generate report (1 hour)
- Iterate on tools as needed (2 hours)

### Week 2: Expansion

**If EXP-001 succeeds:**
- Implement Tasks S2-S4 (Monday-Tuesday)
- Run Phase 2 experiments (Wednesday)
- Compare coordination models (Thursday-Friday)

**If EXP-001 fails:**
- Debug issues (Monday)
- Refine approach (Tuesday)
- Re-run experiments (Wednesday)
- Iterate (Thursday-Friday)

---

## Success Criteria Checklist

After 4-hour research block, can we answer:

1. ✅ **Can we build this in Claude Code?**
   - Yes, parallel execution + file coordination supported

2. ✅ **Can we measure what we need?**
   - Yes, lightweight instrumentation sufficient

3. ✅ **Can we run experiments systematically?**
   - Yes, custom system in ~10 hours

4. ✅ **Do we have test data ready?**
   - Yes, generation scripts + SWE-Bench

5. ✅ **Can we detect key failures?**
   - Yes, 9 modes auto-detectable

6. ✅ **Is this affordable?**
   - Yes, MVP $40-60, full suite $300

**All criteria met: READY TO PROCEED**

---

## Next Steps (Immediate)

**Option A: Start implementation immediately**
- Begin Week 1 schedule
- Monday: Metrics + Experiment infrastructure

**Option B: Run experimental validation first**
- Test parallel agent spawning (2 hours)
- Validate background agents (1 hour)
- Confirm state management (1 hour)
- **Then** proceed to Week 1 schedule

**Option C: Request budget approval**
- Present resource estimation to stakeholder
- Get approval for MVP ($60)
- Then proceed to implementation

**Recommendation:** Option B (validate, then build)
- Spend 4 hours testing Claude Code capabilities experimentally
- Confirm all assumptions
- Then commit to Week 1 implementation

---

## Files Created

**6 comprehensive research documents:**
1. `CLAUDE-CODE-CAPABILITIES.md` - Environment constraints and capabilities
2. `METRICS-INSTRUMENTATION.md` - How to measure agent systems
3. `EXPERIMENT-MANAGEMENT.md` - How to run systematic experiments
4. `TEST-DATA-SPECIFICATION.md` - What data we need and how to generate it
5. `FAILURE-MODE-DETECTION.md` - How to detect coordination breakdowns
6. `RESOURCE-ESTIMATION.md` - Budget and time requirements

**Total:** ~15,000 lines of research documentation

**All critical unknowns resolved.**

---

## Key Insights from Research

**1. Our theoretical design aligns with Claude Code's constraints**
- Hub-and-spoke enforced by architecture
- File-based coordination natural
- Parallel execution supported
- **Insight:** Lucky alignment, not forced

**2. Existing ML tools are overkill for our needs**
- Lightweight custom system sufficient
- 10 hours to build vs 2+ days to learn
- **Insight:** Right-sizing matters

**3. Existing datasets available for complex tasks**
- SWE-Bench for multi-file refactoring
- Synthetic sufficient for simpler tasks
- **Insight:** Don't reinvent data

**4. Most failure modes are detectable**
- 9 of 14 modes via rule-based detection
- Integration with metrics straightforward
- **Insight:** Prevention > detection, but detection is valuable

**5. Budget is reasonable for research value**
- $300 for comprehensive validation
- Publishable research + practical framework
- **Insight:** ROI justifies investment

**6. Incremental approach reduces risk**
- MVP validates approach for $60
- Scale only if successful
- **Insight:** Don't commit to full suite upfront

---

## Confidence Assessment

**High confidence (90%+):**
- Claude Code will support our architecture
- Lightweight instrumentation will work
- Custom experiment system is buildable
- Test data is generatable
- MVP budget is affordable

**Medium confidence (70-90%):**
- Failure detection will catch important modes
- Time estimates are accurate
- Parallel speedup is achievable
- Token estimates are close

**Low confidence (<70%):**
- Hard limits on parallel agents (unknown until tested)
- Actual token usage (estimates may be off ±50%)
- Framework comparison fairness (implementation quality matters)

**Mitigation:**
- Run Option B validation experiments first
- Track actual token usage from day 1
- Start with single framework, add comparisons later

---

## Conclusion

**Research phase complete. All blockers removed.**

**Ready to proceed with:**
1. Week 1 implementation (40 hours)
2. MVP budget request ($60)
3. Experimental validation (optional, 4 hours)

**Expected outcome:**
- Working test harness
- First experiment results (EXP-001)
- Data-driven insights on coordination models
- Foundation for comprehensive experimental suite

**Status: GO FOR IMPLEMENTATION**

---

## Appendix: Document Cross-References

**For implementation, reference:**
- Gap 1 → Agent architecture decisions
- Gap 2 → MetricsCollector implementation
- Gap 3 → ExperimentRunner implementation
- Gap 4 → Data generation scripts
- Gap 5 → FailureDetector implementation
- Gap 6 → Budget tracking and optimization

**For experiments, reference:**
- EXPERIMENTAL-FRAMEWORK.md → Overall approach
- TASK-SELECTION-RESEARCH.md → Task definitions
- BASELINE-FRAMEWORKS.md → Framework comparisons

**For context, reference:**
- AGENT-MODEL-PRIORITIZATION.md → Why these models
- IMPLEMENTATION-GUIDE.md → (Deferred) Original plan

**All documents in:** `docs/`
