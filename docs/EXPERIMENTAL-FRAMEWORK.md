# Experimental Framework: Testing Agent Mental Models

**Purpose:** Empirically determine which mental models work best for which types of agent tasks.

**Related Documents:**
- `docs/TASK-SELECTION-RESEARCH.md` - 2025-2026 research on what agents can/cannot do, sources task recommendations
- `docs/AGENT-MODEL-PRIORITIZATION.md` - Theoretical prioritization (pre-empirical testing)
- `docs/IMPLEMENTATION-GUIDE.md` - Implementation guide (deferred pending experimental validation)

## The Orient Problem

We have completed **Observe** (research phase - 31 mental models documented). We are now in **Orient** - we must understand the terrain before deciding on implementation.

**Current state:** We have theory from 14 disciplines. We do NOT yet know:
- Which models work best in practice for AI agents
- Which task types benefit from which coordination patterns
- Where the models break or conflict
- What the actual bottlenecks are at scale

**Boyd's insight:** Jumping from Observe → Decide → Act without Orient leads to "incestuous amplification" - confirming our assumptions rather than testing reality.

## Experimental Philosophy

1. **Progressive Complexity** - Start with simplest possible tests, add variables incrementally
2. **Competing Variations** - Test alternatives head-to-head, measure differences
3. **Real Tasks** - Use actual agent work, not toy problems
4. **Objective Metrics** - Measure what matters, ignore vanity metrics
5. **Document Failures** - Failed experiments teach us as much as successful ones

## Key Questions to Answer

### Model Selection Questions

**Q1: When does coordination overhead exceed coordination benefit?**
- Test: Same task with 1, 3, 5, 10, 20 agents
- Measure: Total completion time, message count, error rate
- Hypothesis: Coordination overhead grows non-linearly

**Q2: Which error handling model prevents cascade failures best?**
- Test: Jidoka (stop immediately) vs Circuit Breaker (degrade gracefully) vs Retry (push through)
- Measure: Error propagation depth, recovery time, data consistency
- Hypothesis: Jidoka prevents propagation but increases recovery time

**Q3: Does station-based specialization beat dynamic task assignment?**
- Test: Fixed specialist agents vs generalist pool with dynamic assignment
- Measure: Task completion time, context switching overhead, error rate
- Hypothesis: Specialization wins for deep expertise, loses for load balancing

**Q4: When does hub-and-spoke communication become the bottleneck?**
- Test: Hub-and-spoke vs peer-to-peer vs hybrid
- Measure: Hub queue depth, message latency, throughput
- Hypothesis: Hub becomes bottleneck at ~50-100 agents

**Q5: Does explicit cue-based coordination (WARNING/STANDBY/GO) reduce race conditions?**
- Test: Cue-based vs event-driven vs polling
- Measure: Race condition frequency, synchronization overhead, latency
- Hypothesis: Cue-based eliminates races but increases latency

**Q6: Which tasks benefit from shared mental models vs explicit coordination?**
- Test: Convention-based (implicit) vs message-based (explicit) coordination
- Measure: Message count, error rate due to misalignment
- Hypothesis: Routine tasks → conventions, novel tasks → explicit messages

**Q7: How much does temporal synchronization cost?**
- Test: Tightly synchronized (all agents act together) vs loosely coupled (dependencies only)
- Measure: Idle time, throughput, latency
- Hypothesis: Tight sync reduces throughput 30-50%

**Q8: When do hierarchical structures emerge as necessary?**
- Test: Flat coordination vs 2-tier vs 3-tier hierarchy
- Measure: Decision latency, span of control, coordination overhead
- Hypothesis: Flat works to ~8-10 agents, hierarchy required beyond

### Task Type Questions

**Q9: Which mental models work for which task types?**

Task types to test:
- **Parallel Independent** - Tasks with no dependencies (embarrassingly parallel)
- **Sequential Pipeline** - Tasks in strict order (A → B → C)
- **DAG Dependencies** - Complex dependency graph
- **Real-Time Coordination** - Time-critical synchronized actions
- **Exploratory** - Unknown solution space, requires backtracking
- **Iterative Refinement** - Multiple passes to improve quality

For each task type, test:
- Which coordination model works best?
- Which error handling strategy works best?
- Which communication pattern works best?

## Experimental Variables

### Independent Variables (What We Control)

**Coordination Model:**
- Cue-Based (WARNING/STANDBY/GO)
- Event-Driven (publish/subscribe)
- Polling (agents check for work)
- Direct Assignment (orchestrator assigns tasks)

**Communication Pattern:**
- Hub-and-Spoke (centralized)
- Peer-to-Peer (decentralized)
- Hierarchical (multi-tier)
- Hybrid (hub for control, P2P for data)

**Error Handling:**
- Jidoka (stop on error)
- Circuit Breaker (degrade gracefully)
- Retry with Backoff (push through)
- Escalation Tiers (progressive recovery)

**Agent Organization:**
- Station-Based Specialization (fixed roles)
- Dynamic Assignment (generalist pool)
- Tournant Model (generalist + specialists)
- Hierarchical (managers + workers)

**Scale:**
- Small (3-5 agents)
- Medium (10-20 agents)
- Large (50-100 agents)
- Very Large (100+ agents)

### Dependent Variables (What We Measure)

**Effectiveness Metrics:**
- **Task Completion Rate** - % of tasks successfully completed
- **Completion Time** - Wall clock time from start to finish
- **Error Rate** - % of tasks that encountered errors
- **Recovery Time** - Time to recover from errors
- **Throughput** - Tasks completed per unit time

**Efficiency Metrics:**
- **Message Count** - Total messages exchanged
- **Message Size** - Total bytes transmitted
- **Idle Time** - % of time agents waiting for work
- **Context Switches** - How often agents change tasks
- **Resource Utilization** - % of available capacity used

**Coordination Overhead:**
- **Synchronization Time** - Time spent waiting for coordination
- **Communication Latency** - Message round-trip time
- **Queue Depth** - How many messages waiting
- **Decision Latency** - Time to make routing decisions

**Failure Modes:**
- **Error Propagation Depth** - How far errors cascade
- **Deadlock Frequency** - Rate of stuck states
- **Livelock Frequency** - Rate of spinning without progress
- **Cascade Failure Rate** - % of single failures that cascade

**Scalability:**
- **Span of Control** - How many agents per coordinator
- **Coordination Overhead Growth** - How overhead scales with N
- **Bottleneck Identification** - Where does it break?

## Baseline Tasks

**UPDATED BASED ON 2025-2026 RESEARCH** - See `docs/TASK-SELECTION-RESEARCH.md` for full analysis.

We need standard tasks covering both agent **strengths** (should succeed) and **weaknesses** (should reveal bottlenecks). Research shows:
- Top models: 70%+ on simple benchmarks, 21-23% on long-horizon tasks
- Multi-agent coordination overhead often causes underperformance vs. single-agent
- Key struggle areas: cross-file reasoning, sustained multi-step, high communication overhead

### Strength Category Tasks (Expected: 75-90% Success)

**Task S1: Parallel File Processing (Map-Reduce)**
- Description: Process 100 text files, extract keywords, aggregate results
- Dependencies: None between files, aggregation depends on all extractions
- Coordination: Minimal (aggregation only)
- Expected Success: 90%+
- Optimal Time: O(N/agents + aggregation)
- **Tests:** Load balancing, basic coordination, clear boundaries
- **Research basis:** Parallel execution works best for I/O-bound operations

**Task S2: Sequential ETL Pipeline**
- Description: Fetch data → Clean → Transform → Validate → Store (strict order)
- Dependencies: Linear chain with clear contracts
- Coordination: Sequential handoffs
- Expected Success: 85%+
- Optimal Time: O(sum of stage times)
- **Tests:** Handoff protocols, state passing, error propagation
- **Research basis:** Sequential/prompt chaining is proven successful pattern

**Task S3: Orchestrator-Worker Dispatch**
- Description: Route 50 customer queries to specialized agents (support, sales, tech)
- Dependencies: None (parallel after routing)
- Coordination: Central orchestrator, parallel workers
- Expected Success: 80%+
- Optimal Time: O(max specialist time)
- **Tests:** Routing logic, specialist capabilities, response aggregation
- **Research basis:** Orchestrator-worker pattern succeeds for bounded specialization

**Task S4: Bounded ReAct Loop**
- Description: Answer complex question using search + calculator (5-10 steps max)
- Dependencies: Sequential within loop
- Coordination: Single agent with tool access
- Expected Success: 75%+
- Optimal Time: O(reasoning steps)
- **Tests:** Tool selection, observation integration, termination
- **Research basis:** ReAct loops work well for bounded reasoning horizons

### Struggle Category Tasks (Expected: 20-40% Success)

**Task W1: Multi-File Code Refactoring**
- Description: Refactor authentication system across 5-8 Python files (~100+ lines)
- Dependencies: Deep cross-file reasoning
- Coordination: Context integration
- Expected Success: 20-30%
- Optimal Time: Unknown (human: hours to days)
- **Tests:** Context management, cross-file dependencies, sustained reasoning
- **Research basis:** SWE-Bench Pro shows 23% performance on multi-file tasks

**Task W2: High-Coordination Multi-Agent**
- Description: 5 agents collaboratively solve resource allocation problem (20+ message rounds)
- Dependencies: Shared state, frequent communication
- Coordination: Peer-to-peer with high message passing
- Expected Success: 30-40%
- Optimal Time: Unknown (coordination overhead dominant)
- **Tests:** Communication overhead, message efficiency, coordination protocol
- **Research basis:** Multi-agent often underperforms single-agent due to overhead

**Task W3: Exploratory Problem Solving with Backtracking**
- Description: Find optimal solution in search space requiring exploration + hypothesis revision
- Dependencies: Results inform strategy changes
- Coordination: Single agent, complex reasoning (30+ steps)
- Expected Success: 25-35%
- Optimal Time: Unknown (heuristic-dependent)
- **Tests:** Reasoning chain maintenance, backtracking, hypothesis revision
- **Research basis:** Sustained multi-step reasoning remains challenging

**Task W4: Dynamic Multi-Agent Handoff**
- Description: Multi-stage research task where findings change the approach mid-execution
- Dependencies: Unclear handoffs, evolving strategy
- Coordination: Agent-to-agent with context compression
- Expected Success: 20-30%
- Optimal Time: Unknown (human: hours)
- **Tests:** Context transfer, adaptation, protocol robustness under uncertainty
- **Research basis:** GAIA shows unclear handoffs drastically increase failures

### Hybrid Tasks (Expected: 40-70% Success)

**Task H1: Parallel with Coordination Bottleneck**
- Description: Deploy to 10 servers (parallel) with verification gate (sync)
- Dependencies: All must synchronize for verification
- Coordination: Mostly parallel, tight sync point
- Expected Success: 60-70%
- Optimal Time: O(deploy time + sync overhead)
- **Tests:** Synchronization overhead, coordination benefit vs. cost
- **Research basis:** Tests boundary between parallel and synchronized

**Task H2: Error Recovery in Pipeline**
- Description: ETL pipeline (Task S2) with 20% random failure injection
- Dependencies: Linear chain with recovery
- Coordination: Sequential + error handling
- Expected Success: 50-60%
- Optimal Time: O(stages + recovery)
- **Tests:** Error detection, recovery strategies, graceful degradation
- **Research basis:** Tests error handling under realistic failure rates

**Task H3: Incremental Context Building**
- Description: Analyze codebase → Design change → Implement → Test (15-20 steps)
- Dependencies: Each stage builds on previous understanding
- Coordination: Sequential with growing context
- Expected Success: 40-50%
- Optimal Time: Unknown (human: hours)
- **Tests:** Context accumulation, mental model transfer, long-term memory
- **Research basis:** Tests medium-horizon sustained reasoning

## Test Harness Design

### Requirements

1. **Reproducible** - Same inputs → same results
2. **Isolated** - Tests don't interfere with each other
3. **Instrumented** - Capture all relevant metrics automatically
4. **Configurable** - Easy to swap coordination models
5. **Comparable** - Results in standardized format

### Architecture

```
test-harness/
├── tasks/                  # Baseline task definitions
│   ├── task_001_map_reduce.yaml
│   ├── task_002_pipeline.yaml
│   └── ...
├── models/                 # Mental model implementations
│   ├── coordination/
│   │   ├── cue_based.py
│   │   ├── event_driven.py
│   │   └── polling.py
│   ├── communication/
│   │   ├── hub_and_spoke.py
│   │   ├── peer_to_peer.py
│   │   └── hierarchical.py
│   └── error_handling/
│       ├── jidoka.py
│       ├── circuit_breaker.py
│       └── retry.py
├── agents/                 # Test agent implementations
│   ├── base_agent.py      # Common interface
│   ├── specialist_agent.py
│   └── generalist_agent.py
├── metrics/                # Measurement infrastructure
│   ├── collector.py       # Gather metrics during execution
│   ├── analyzer.py        # Analyze results
│   └── visualizer.py      # Generate comparison charts
├── experiments/            # Experiment definitions
│   ├── exp_001_coordination_comparison.yaml
│   ├── exp_002_scale_test.yaml
│   └── ...
└── runner.py               # Main test execution
```

### Experiment Definition Format

```yaml
experiment:
  id: "EXP-001"
  name: "Coordination Model Comparison"
  description: "Compare cue-based vs event-driven vs polling for Task 1"

  task: "task_001_map_reduce"

  variations:
    - name: "Cue-Based Coordination"
      coordination: "cue_based"
      communication: "hub_and_spoke"
      error_handling: "jidoka"
      agents: 5

    - name: "Event-Driven"
      coordination: "event_driven"
      communication: "hub_and_spoke"
      error_handling: "jidoka"
      agents: 5

    - name: "Polling"
      coordination: "polling"
      communication: "hub_and_spoke"
      error_handling: "jidoka"
      agents: 5

  metrics:
    - "completion_time"
    - "message_count"
    - "error_rate"
    - "idle_time"

  trials: 10  # Run each variation 10 times

  success_criteria:
    - "error_rate < 0.05"
    - "completion_time < 60s"
```

## Progressive Testing Strategy

### Phase 1: Baseline (Week 1)
- Implement test harness
- Implement Task 1 (simplest: parallel map-reduce)
- Test with 3 agents, single coordination model
- Verify metrics collection works
- **Goal:** Working test infrastructure

### Phase 2: Model Comparison (Week 2)
- Implement 3 coordination models (cue-based, event-driven, polling)
- Run Task 1 with each model
- Compare results
- **Goal:** Understand coordination model tradeoffs

### Phase 3: Scale (Week 3)
- Test Task 1 at 3, 5, 10, 20 agents
- Identify where coordination breaks
- Measure overhead growth rate
- **Goal:** Understand scaling characteristics

### Phase 4: Task Diversity (Week 4)
- Implement Tasks 2-4
- Test best coordination model from Phase 2 on each task
- Identify which tasks need different models
- **Goal:** Understand task-model fit

### Phase 5: Error Handling (Week 5)
- Implement error injection for Task 6
- Test Jidoka vs Circuit Breaker vs Retry
- Measure recovery characteristics
- **Goal:** Understand error handling tradeoffs

### Phase 6: Communication Patterns (Week 6)
- Implement hub-and-spoke vs peer-to-peer
- Test at medium scale (20 agents)
- Identify bottlenecks
- **Goal:** Understand communication pattern tradeoffs

### Phase 7: Full Combinations (Week 7-8)
- Test full matrix of models × tasks × scales
- Identify optimal combinations
- Document anti-patterns
- **Goal:** Comprehensive model-task-scale mapping

## Success Criteria for Orient Phase

We will know we've successfully oriented when we can answer:

1. **Model Selection:** For any task type, we can recommend which mental model(s) to use
2. **Scale Thresholds:** We know at what scale each model breaks and what replaces it
3. **Tradeoff Clarity:** We understand the costs and benefits of each choice
4. **Anti-Patterns:** We know what NOT to do and why
5. **Empirical Validation:** We have data supporting each recommendation

## Rationale

This experimental approach:
- **Prevents premature optimization** - Test before implementing
- **Reveals hidden assumptions** - Find where theory diverges from practice
- **Builds confidence** - Data-driven decisions
- **Enables the book** - The experimental journey IS the story
- **Follows Boyd** - Orient thoroughly before deciding

## Next Steps

1. Design test harness architecture (detailed)
2. Implement baseline task (Task 1)
3. Implement simplest coordination model
4. Verify metrics collection
5. Run first experiment (EXP-001)
6. Iterate based on learnings
