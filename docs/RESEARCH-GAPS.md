# Research Gaps: 4-Hour Priority Block

**Purpose:** Identify critical research needed before implementing test harness and running experiments.

**Current status:** We have theoretical framework and know what exists externally. Need to understand:
1. What Claude Code can actually do (our implementation environment)
2. How to measure what we need to measure (instrumentation)
3. How to manage experiments systematically (reproducibility)
4. What data/resources we need (preparation)

---

## Gap 1: Claude Code Capabilities (CRITICAL - 60 minutes)

**Why critical:** Everything we build must work within Claude Code's constraints. We're designing multi-agent experiments but don't deeply understand the Task tool.

### Research Questions

1. **Task tool behavior:**
   - What subagent types are available? (We know: Bash, general-purpose, Explore, Plan, claude-code-guide)
   - How do agents communicate back? (We see: agent returns single message)
   - Can agents spawn sub-agents? (Nested Task calls?)
   - What's the context window for spawned agents?

2. **Parallel execution:**
   - Can we spawn multiple Task agents in one message? (Docs say yes)
   - How are results returned? (All at once? Streaming?)
   - What's the limit on parallel agents?
   - Do parallel agents share context?

3. **State management:**
   - How do agents persist state between invocations?
   - Can we pass structured data to agents? (Yes via prompt)
   - Can agents resume from previous runs? (Yes via resume parameter)
   - File-based state vs memory-based?

4. **Limitations and constraints:**
   - Maximum agent execution time?
   - Token limits per agent?
   - Model selection (Opus, Sonnet, Haiku)?
   - Cost considerations?

5. **Background agents:**
   - run_in_background parameter - how does it work?
   - Checking on background agent progress
   - Multiple background agents concurrently?

### Research Approach

**Method 1: Documentation deep-dive** (20 min)
- Read Claude Code tool descriptions thoroughly
- Note every parameter, constraint, capability
- Document examples from tool descriptions

**Method 2: Experimental testing** (30 min)
- Create test script spawning different agent types
- Test parallel execution (2, 5, 10 agents)
- Test state passing (file-based, parameter-based)
- Test background execution
- Measure actual behavior vs documentation

**Method 3: Review codebase for examples** (10 min)
- Search `.claude/` and project for Task tool usage
- Find real-world patterns already working
- Document what's proven vs theoretical

### Deliverable

**Document:** `docs/CLAUDE-CODE-CAPABILITIES.md`

**Contents:**
- Available agent types and their capabilities
- Parallel execution limits and patterns
- State management approaches
- Constraints and limitations
- Cost model (tokens per agent type)
- Best practices from testing
- Anti-patterns to avoid

**Impact:** Determines whether our test harness design is feasible or needs revision.

---

## Gap 2: Metrics Instrumentation Patterns (45 minutes)

**Why important:** We know WHAT to measure (latency, tokens, messages, errors) but not HOW to instrument it reliably.

### Research Questions

1. **Latency measurement:**
   - Where to start/stop timers? (Message send? Agent spawn? Task start?)
   - Clock drift in distributed systems?
   - Python timing best practices (`time.perf_counter` vs `time.time`)?

2. **Token counting:**
   - Can we access actual token counts from Claude Code?
   - Count input vs output tokens separately?
   - Count tokens in spawned agents?
   - Use tiktoken library for estimation?

3. **Message counting:**
   - What counts as a "message"? (Task spawn? Hub route? Agent-to-agent?)
   - How to track message flow through system?
   - Structured logging format?

4. **Error tracking:**
   - Exception types to catch?
   - Error categorization (validation, timeout, resource, etc.)
   - Stack trace capture and storage?
   - Error recovery attempts vs failures?

5. **Existing frameworks' approaches:**
   - How does LangGraph instrument metrics?
   - How does CrewAI track performance?
   - OpenAI SDK observability features?

### Research Approach

**Method 1: Framework instrumentation review** (20 min)
- Search LangGraph docs/code for metrics/observability
- Search CrewAI docs/code for performance tracking
- Check OpenAI SDK for built-in monitoring
- Note patterns, libraries, approaches

**Method 2: Python observability libraries** (15 min)
- Research OpenTelemetry for Python
- Research Prometheus client for metrics
- Research structlog for structured logging
- Identify lightweight options for experiments

**Method 3: Design metrics collector** (10 min)
- Sketch Python class: `MetricsCollector`
- Methods: `start_task()`, `end_task()`, `log_message()`, `log_error()`
- Storage: JSON Lines format for easy analysis?
- Aggregation: pandas for post-processing?

### Deliverable

**Document:** `docs/METRICS-INSTRUMENTATION.md`

**Contents:**
- Measurement points and timing approaches
- Token counting strategy
- Message tracking schema
- Error categorization taxonomy
- Metrics collector interface design
- Storage format specification
- Analysis tooling recommendations

**Code:** `coordination/metrics_collector.py` (skeleton)

**Impact:** Enables reliable, comparable measurements across experiments.

---

## Gap 3: Experiment Management System (45 minutes)

**Why important:** We'll run dozens of experiments. Need systematic way to configure, run, store results, and compare.

### Research Questions

1. **Experiment configuration:**
   - YAML format for experiment specs? (Like EXPERIMENTAL-FRAMEWORK.md shows)
   - How to specify variations (coordination model, agent count, etc.)?
   - Parameter grids for systematic exploration?

2. **Result storage:**
   - One file per experiment run? Directory structure?
   - JSON for structured data? CSV for tabular? Both?
   - Metadata: timestamp, git commit, model versions?

3. **Result comparison:**
   - How to aggregate across trials (mean, median, stddev)?
   - Statistical significance testing?
   - Visualization (matplotlib? seaborn?)?

4. **Reproducibility:**
   - Random seed management?
   - Environment capture (Python version, dependencies)?
   - Git commit hash for code version?
   - Input data versioning?

5. **Existing tools:**
   - MLflow for experiment tracking?
   - Weights & Biases?
   - Sacred?
   - Or custom lightweight system?

### Research Approach

**Method 1: ML experiment tracking tools** (20 min)
- Survey MLflow, W&B, Sacred
- Assess fit for our use case
- Identify overkill vs useful features
- Lightweight alternatives?

**Method 2: Design experiment schema** (15 min)
- YAML spec for experiment definition
- JSON spec for result storage
- Directory structure for runs
- Naming conventions

**Method 3: Comparison workflow** (10 min)
- Sketch analysis notebook structure
- Data loading and aggregation approach
- Comparison visualizations needed
- Report generation format

### Deliverable

**Document:** `docs/EXPERIMENT-MANAGEMENT.md`

**Contents:**
- Experiment configuration format
- Result storage schema and structure
- Reproducibility checklist
- Comparison and analysis workflow
- Tool recommendations (MLflow vs custom)
- Example experiment YAML
- Example analysis notebook outline

**Templates:**
- `test-harness/experiments/template.yaml`
- `test-harness/notebooks/analysis_template.ipynb`

**Impact:** Enables systematic, reproducible experiments with clear comparison.

---

## Gap 4: Test Data Requirements (30 minutes)

**Why important:** Our tasks need actual data. Task S1 needs 100 text files, Task W1 needs a codebase to refactor, etc.

### Research Questions

1. **Task S1 (Parallel Map-Reduce):**
   - 100 text files: real or synthetic?
   - File size range (1KB, 10KB, 100KB)?
   - Content type (code, prose, structured data)?
   - Keyword extraction: what's expected output?

2. **Task S2 (Sequential Pipeline):**
   - Data source (API, file, database)?
   - Data format (JSON, CSV, XML)?
   - Transform logic (what operations)?
   - Validation rules?

3. **Task W1 (Multi-File Refactoring):**
   - Codebase to refactor: which language?
   - How many files (research says 5-8)?
   - Lines of code (~100+)?
   - Refactoring task specifics?
   - Ground truth for correctness?

4. **Task W2 (High-Coordination):**
   - Resource allocation problem specifics?
   - Input format?
   - Optimal solution (for comparison)?

5. **Existing datasets:**
   - SWE-Bench Pro: can we use their tasks?
   - WebArena: can we adapt their scenarios?
   - AgentBench: reusable task data?
   - Synthetic generation vs real data?

### Research Approach

**Method 1: Benchmark dataset review** (15 min)
- Check SWE-Bench Pro for downloadable tasks
- Check WebArena for task templates
- Check AgentBench for reusable data
- Licensing and usage constraints?

**Method 2: Synthetic generation** (10 min)
- Script to generate 100 text files (Python + Faker?)
- Script to generate sample codebase
- Script to generate problem instances
- Deterministic generation (seeded random)

**Method 3: Data specification** (5 min)
- Document required data per task
- File formats and schemas
- Storage location in test-harness
- Version control considerations

### Deliverable

**Document:** `docs/TEST-DATA-SPECIFICATION.md`

**Contents:**
- Data requirements per task (S1-S4, W1-W4, H1-H3)
- Synthetic generation scripts
- Dataset sources and licenses
- Storage structure
- Ground truth / expected outputs
- Data versioning approach

**Scripts:**
- `test-harness/data/generate_task_s1_data.py`
- `test-harness/data/generate_task_w1_codebase.py`
- etc.

**Impact:** Enables running experiments immediately with ready test data.

---

## Gap 5: Failure Mode Detection (30 minutes)

**Why important:** Research identified 14 failure modes in multi-agent systems. We need to detect them programmatically.

### Research Questions

1. **From research (1,642 traces):**
   - Conversation resets (2.20%): How to detect?
   - Wrong assumptions (6.80%): Pattern recognition?
   - Task derailment (7.40%): Drift detection?
   - Ignoring input (1.90%): Message acknowledgment tracking?
   - Reasoning/action mismatch (13.2%): How to identify?

2. **Detection strategies:**
   - Log analysis patterns?
   - State machine invariants?
   - Expected message sequences?
   - Timeout thresholds?
   - Semantic drift detection?

3. **Categorization:**
   - Map 14 modes to our message types?
   - Which are detectable automatically?
   - Which require human annotation?

4. **Prevention vs detection:**
   - Which failures do our conventions prevent?
   - Which require runtime detection?
   - Which require post-hoc analysis?

### Research Approach

**Method 1: Map failure modes to our system** (15 min)
- Review 14 failure modes from research
- Map to our message schema (task, status, coord, escalation, ack)
- Identify detectable signatures
- Design detection rules

**Method 2: Design failure detector** (10 min)
- Sketch Python class: `FailureDetector`
- Rule-based detection for each mode
- Statistical anomaly detection?
- Output: categorized failure log

**Method 3: Integration with metrics** (5 min)
- How failure detection feeds metrics
- Failure rate calculations
- Cascade depth tracking
- Recovery success tracking

### Deliverable

**Document:** `docs/FAILURE-MODE-DETECTION.md`

**Contents:**
- 14 failure modes mapped to our system
- Detection strategies per mode
- Detectable automatically vs manual review
- Prevention via conventions
- Detector interface design

**Code:** `coordination/failure_detector.py` (skeleton)

**Impact:** Enables measuring cascade failures, coordination breakdowns, and other key failure modes.

---

## Gap 6: Resource Estimation (30 minutes)

**Why important:** Need to understand costs (tokens, time, money) before running experiments.

### Research Questions

1. **Token costs:**
   - Average tokens per task type?
   - Opus vs Sonnet vs Haiku costs?
   - Coordination overhead in tokens?
   - Budget for full test suite?

2. **Time estimates:**
   - How long does Task S1 take? (baseline)
   - Scaling with agent count (linear, superlinear)?
   - Total time for Phase 1 experiments?
   - Parallelization opportunities?

3. **Infrastructure:**
   - Can we run on local machine?
   - Cloud requirements?
   - Storage needs for results?
   - Computational bottlenecks?

4. **Financial costs:**
   - API costs per experiment run?
   - Cost per trial (10 trials per variation)?
   - Budget for full experimental suite?
   - Cost optimization strategies?

### Research Approach

**Method 1: Back-of-envelope calculations** (15 min)
- Estimate tokens per task
- Count experiments in full suite
- Calculate total token budget
- Convert to dollars
- Identify expensive experiments

**Method 2: Optimization strategies** (10 min)
- Use Haiku for simple coordination?
- Cache embeddings/prompts?
- Parallel execution to save wall time?
- Incremental approach (MVP first)?

**Method 3: Create budget document** (5 min)
- Cost per experiment type
- Total budget estimate
- Phased approach to stay within budget
- Optimization recommendations

### Deliverable

**Document:** `docs/RESOURCE-ESTIMATION.md`

**Contents:**
- Token estimates per task type
- Time estimates per experiment
- Financial cost projections
- Budget for experimental phases
- Optimization strategies
- Phased implementation plan

**Impact:** Ensures experiments are feasible within budget, prioritizes high-value tests.

---

## 4-Hour Research Block Schedule

**Hour 1: Claude Code Capabilities (CRITICAL)**
- 20 min: Documentation deep-dive
- 30 min: Experimental testing
- 10 min: Codebase examples review
- **Deliverable:** `CLAUDE-CODE-CAPABILITIES.md`

**Hour 2: Metrics + Experiment Management**
- 45 min: Metrics instrumentation patterns
  - 20 min: Framework review
  - 15 min: Python observability libraries
  - 10 min: Design collector
  - **Deliverable:** `METRICS-INSTRUMENTATION.md` + skeleton code
- 15 min: Break

**Hour 3: Experiment Management (continued) + Test Data**
- 45 min: Experiment management system
  - 20 min: ML experiment tracking tools
  - 15 min: Design experiment schema
  - 10 min: Comparison workflow
  - **Deliverable:** `EXPERIMENT-MANAGEMENT.md` + templates
- 15 min: Break

**Hour 4: Test Data + Failure Detection + Resources**
- 30 min: Test data requirements
  - 15 min: Benchmark dataset review
  - 10 min: Synthetic generation
  - 5 min: Data specification
  - **Deliverable:** `TEST-DATA-SPECIFICATION.md` + scripts
- 30 min: Failure detection + Resource estimation
  - 15 min: Failure mode detection design
  - 15 min: Resource estimation
  - **Deliverables:** `FAILURE-MODE-DETECTION.md`, `RESOURCE-ESTIMATION.md`

---

## Success Criteria

After 4-hour block, we can answer:

1. **Can we build this in Claude Code?** (Gap 1)
2. **Can we measure what we need?** (Gap 2)
3. **Can we run experiments systematically?** (Gap 3)
4. **Do we have test data ready?** (Gap 4)
5. **Can we detect key failures?** (Gap 5)
6. **Is this affordable?** (Gap 6)

If all yes: **Ready to implement test harness**

If any no: **Adjust approach based on constraints**

---

## Priority Ordering (If Limited Time)

**Must have (blocker):**
1. Gap 1: Claude Code Capabilities (can't proceed without knowing environment)

**Should have (high value):**
2. Gap 2: Metrics Instrumentation (needed for meaningful results)
3. Gap 3: Experiment Management (needed for reproducibility)

**Nice to have (important but can defer):**
4. Gap 4: Test Data (can mock initially)
5. Gap 5: Failure Detection (can add incrementally)
6. Gap 6: Resource Estimation (helps prioritize but not blocking)

---

## Post-Research Next Steps

After completing this research:

**Week 1:**
- Implement metrics collector
- Implement experiment runner
- Generate test data
- Build test harness MVP

**Week 2:**
- Implement Task S1 in our model
- Implement Task S1 in LangGraph (baseline)
- Run first experiment (EXP-001)
- Analyze results

**Week 3:**
- Iterate based on learnings
- Expand to more tasks
- Compare coordination models
- Document findings

This research block removes all major unknowns blocking implementation.
