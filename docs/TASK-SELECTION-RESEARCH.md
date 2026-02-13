# Task Selection Research: What AI Agents Can and Cannot Do (2025-2026)

**Purpose:** Identify realistic test tasks covering both agent strengths and weaknesses based on empirical research.

**Research Date:** 2026-01-21

---

## Executive Summary

Based on extensive 2025-2026 research, AI agents show a stark divide:

- **What works:** Bounded, well-defined workflows with clear tool usage (e.g., customer service, claims processing, sequential pipelines)
- **What struggles:** Long-horizon tasks requiring cross-file reasoning, deep context integration, and sustained multi-step problem-solving

The performance gap is striking: top models score 70%+ on simple benchmarks but drop to 21-23% on realistic long-horizon tasks. Multi-agent coordination overhead often causes systems to underperform single-agent baselines.

---

## Key Findings from Benchmarks

### Performance Reality Check

**SWE-Bench vs. SWE-Bench Pro:**
- SWE-Bench Verified: 70%+ scores from top models
- SWE-Bench Pro: Only 23% from GPT-5 and Claude Opus 4.1
- **Why the gap?** SWE-Bench Pro features long-horizon tasks (hours to days for humans), average 107 lines across 4+ files, requiring deep contextual understanding

**Real-world impact study:** Experienced open-source developers using AI tools take **19% longer** than without AI in early 2025.

### Multi-Agent Coordination Failures

Research analyzing **1,642 execution traces** identified 14 fine-grained failure modes:

**Common failures:**
- Unexpected conversation resets (2.20%)
- Proceeding with wrong assumptions instead of seeking clarification (6.80%)
- Task derailment (7.40%)
- Ignoring other agents' input (1.90%)
- Mismatch between reasoning and action (13.2%)

**Critical insight:** Unclear agent-to-agent transfers drastically increase failure rates, especially in dynamic reasoning tasks (GAIA benchmark).

**Coordination overhead:** Many multi-agent systems struggle to outperform strong single-agent baselines, with performance often degrading as coordination complexity increases.

---

## What AI Agents Do Well

### 1. Sequential Workflows with Clear Boundaries

**Evidence:** Sequential/prompt chaining is one of the most successful patterns in 2025, where each step's output becomes input for the next.

**Examples that work:**
- Document processing pipelines (fetch → transform → validate → store)
- Customer onboarding flows
- Data ETL processes
- Claims processing (policy rules → damage assessment → payout)

**Success factors:**
- Clear task boundaries
- Well-defined input/output contracts
- Limited need for backtracking
- Structured data formats

### 2. Parallel Independent Tasks (I/O-Bound)

**Evidence:** Parallel execution patterns work best for I/O-bound operations like API calls or database queries.

**Examples that work:**
- Processing multiple independent files
- Parallel API calls
- Concurrent database queries
- Batch data processing

**Success factors:**
- No inter-task dependencies
- Clear success criteria per task
- Minimal coordination required
- Stateless operations

### 3. Structured Tool Use (Orchestrator-Worker Pattern)

**Evidence:** Orchestrator-worker patterns succeed when a primary model coordinates specialized workers, each optimizing for specific subtasks.

**Examples that work:**
- Customer service routing (intent classification → specialist → response)
- Sales prospecting (lead qualification → engagement → followup)
- Supply chain monitoring (data collection → analysis → action recommendation)

**Success factors:**
- Clear division of labor
- Well-defined specialist capabilities
- Simple handoff protocols
- Central context management

### 4. Bounded Reasoning Tasks (ReAct Pattern)

**Evidence:** ReAct (Reason + Act) loops work well for tasks that interleave reasoning with tool calls, using observations to decide next steps.

**Examples that work:**
- Search and summarize tasks
- Data analysis with tool support
- Single-file code modifications
- Question answering with retrieval

**Success factors:**
- Limited reasoning horizon (5-10 steps)
- Clear tool interfaces
- Observable results after each action
- Well-defined termination conditions

---

## What AI Agents Struggle With

### 1. Long-Horizon Tasks Requiring Deep Context

**Evidence:** SWE-Bench Pro reveals "substantial gaps" in handling real-world software engineering scenarios requiring deep contextual understanding and cross-file reasoning.

**Examples that fail:**
- Multi-file code refactoring (107+ line patches across 4+ files)
- Architectural design changes
- Large-scale system integration
- Tasks requiring hours/days of sustained reasoning

**Why they fail:**
- Context window limitations despite large sizes
- Attention degradation over long sequences
- Inability to maintain working memory across sessions
- Difficulty building accurate mental models of complex systems

### 2. Multi-Agent Coordination with High Communication Overhead

**Evidence:** The primary bottleneck in LLM-based multi-agent systems lies in planning and communication processes. Input tokens predominantly originate from inter-agent dialogues.

**Examples that fail:**
- Complex multi-agent negotiations
- Dynamic task allocation with frequent reassignments
- Real-time collaborative problem solving
- Shared state management across agents

**Why they fail:**
- Token consumption grows substantially with communication rounds
- Network architectures create communication overhead
- Misalignment in goal understanding
- Memory management failures across agents
- Coordination protocol violations

### 3. Tasks Requiring Sustained Multi-Step Reasoning

**Evidence:** Even advanced reasoning models (OpenAI o1, DeepSeek R1) find automated failure attribution challenging - a task demanding higher reasoning than conventional tasks.

**Examples that fail:**
- Complex debugging (finding root causes across multiple systems)
- Multi-constraint optimization
- Exploratory problem solving with backtracking
- Synthesizing insights from diverse sources

**Why they fail:**
- Reasoning chains degrade over multiple steps
- Difficulty tracking assumptions across branches
- Weak counterfactual reasoning
- Cannot effectively backtrack and revise earlier decisions

### 4. Dynamic Reasoning Tasks with Unclear Handoffs

**Evidence:** GAIA benchmark shows unclear agent-to-agent transfers drastically increase failure rates, especially in dynamic reasoning tasks.

**Examples that fail:**
- Adaptive workflows where next step depends on complex prior results
- Creative problem solving requiring iteration
- Research tasks with evolving understanding
- Tasks where intermediate results change the strategy

**Why they fail:**
- Difficulty compressing context for handoffs
- Loss of nuance in agent-to-agent communication
- Inability to transfer "working understanding" vs. just data
- Protocol violations during state transitions

---

## Recommended Test Task Suite

Based on research findings, we propose testing tasks in both "strength" and "struggle" categories:

### Strength Category Tasks (Should Succeed)

**Task S1: Parallel File Processing (Map-Reduce)**
- Type: Embarrassingly parallel
- Description: Process 100 text files, extract keywords, aggregate results
- Coordination: Minimal (aggregation only)
- Expected success: 90%+
- **Tests:** Load balancing, basic coordination, clear boundaries

**Task S2: Sequential ETL Pipeline**
- Type: Linear dependency chain
- Description: Fetch data → Clean → Transform → Validate → Store
- Coordination: Sequential handoffs with clear contracts
- Expected success: 85%+
- **Tests:** Handoff protocols, state passing, error propagation

**Task S3: Orchestrator-Worker Dispatch**
- Type: Hub-and-spoke pattern
- Description: Route customer queries to specialized agents
- Coordination: Central orchestrator, parallel workers
- Expected success: 80%+
- **Tests:** Routing logic, specialist capabilities, response aggregation

**Task S4: Bounded ReAct Loop**
- Type: Iterative reasoning with tools (5-10 steps)
- Description: Answer complex question using search + calculator
- Coordination: Single agent with tool access
- Expected success: 75%+
- **Tests:** Tool selection, observation integration, termination

### Struggle Category Tasks (Should Reveal Weaknesses)

**Task W1: Multi-File Code Refactoring**
- Type: Long-horizon, cross-file reasoning
- Description: Refactor authentication system across 5-8 files
- Coordination: Deep context integration
- Expected success: 20-30%
- **Tests:** Context management, cross-file dependencies, sustained reasoning

**Task W2: High-Coordination Multi-Agent**
- Type: Dynamic task allocation
- Description: 5 agents collaboratively solve resource allocation problem
- Coordination: High message passing, shared state
- Expected success: 30-40%
- **Tests:** Communication overhead, message passing efficiency, coordination protocol

**Task W3: Exploratory Problem Solving**
- Type: Multi-step reasoning with backtracking
- Description: Find optimal solution in search space (requires exploration + revision)
- Coordination: Single agent, complex reasoning
- Expected success: 25-35%
- **Tests:** Reasoning chain maintenance, backtracking, hypothesis revision

**Task W4: Dynamic Multi-Agent Handoff**
- Type: Unclear handoffs, evolving strategy
- Description: Multi-stage research task where findings change the approach
- Coordination: Agent-to-agent transfers with context compression
- Expected success: 20-30%
- **Tests:** Context transfer, adaptation to new information, protocol robustness

### Hybrid Tasks (Interesting Cases)

**Task H1: Parallel with Coordination Bottleneck**
- Type: Mostly parallel but with synchronization points
- Description: Deploy to 10 servers (parallel) with verification gate (sync)
- Expected success: 60-70%
- **Tests:** Synchronization overhead, coordination benefit vs. cost

**Task H2: Error Recovery in Pipeline**
- Type: Sequential with high failure injection
- Description: ETL pipeline with 20% random failures
- Expected success: 50-60%
- **Tests:** Error detection, recovery strategies, graceful degradation

**Task H3: Incremental Context Building**
- Type: Sequential tasks that build shared understanding
- Description: Analyze codebase → Design change → Implement → Test
- Expected success: 40-50%
- **Tests:** Context accumulation, mental model transfer, long-term memory

---

## Task Characteristics Matrix

| Task | Horizon | Coord Overhead | Context Depth | File/System Scope | Expected Success |
|------|---------|----------------|---------------|-------------------|------------------|
| S1: Map-Reduce | Short | Minimal | Shallow | Single file × N | 90%+ |
| S2: ETL Pipeline | Short-Medium | Low | Medium | 3-5 components | 85%+ |
| S3: Dispatcher | Short | Low | Shallow | Well-bounded | 80%+ |
| S4: ReAct | Short | None | Medium | Limited tools | 75%+ |
| W1: Multi-File Refactor | Long | Medium | Deep | 5-8 files | 20-30% |
| W2: High-Coord | Medium | High | Medium | 5 agents | 30-40% |
| W3: Exploratory | Medium-Long | None | Deep | Conceptual | 25-35% |
| W4: Dynamic Handoff | Medium | High | Deep | Evolving | 20-30% |
| H1: Parallel+Sync | Short | Medium | Shallow | 10 targets | 60-70% |
| H2: Error Recovery | Medium | Medium | Medium | 5 stages | 50-60% |
| H3: Context Build | Long | Low | Deep | Evolving | 40-50% |

---

## Key Dimensions to Test

Based on research, our test suite should cover:

### 1. Coordination Overhead Spectrum
- **Minimal:** Map-reduce (aggregation only)
- **Low:** Sequential pipeline (clear handoffs)
- **Medium:** Parallel with sync points
- **High:** Dynamic multi-agent with frequent communication

**Research question:** At what coordination overhead do benefits turn negative?

### 2. Task Horizon Spectrum
- **Short:** 5-10 agent actions
- **Medium:** 20-50 actions
- **Long:** 50+ actions spanning multiple sessions

**Research question:** When does performance degrade with horizon length?

### 3. Context Depth Spectrum
- **Shallow:** Single file, clear inputs/outputs
- **Medium:** 3-5 related files/components
- **Deep:** 5-8+ files with complex interdependencies

**Research question:** How does context depth affect reasoning quality?

### 4. Coordination Pattern Types
- **Embarrassingly Parallel:** Independent tasks
- **Sequential/Pipeline:** Linear dependencies
- **Hub-and-Spoke:** Central coordinator
- **Peer-to-Peer:** Direct agent communication
- **Hierarchical:** Multi-tier delegation

**Research question:** Which patterns scale best with agent count?

### 5. Failure Modes
- **Error Propagation:** How failures cascade
- **Communication Breakdown:** Agent misalignment
- **Context Loss:** Information degradation in transfers
- **Coordination Overhead:** Performance degradation

**Research question:** Which coordination models prevent cascade failures?

---

## Implementation Recommendations

### Phase 1: Validate Strengths (Weeks 1-2)
Start with tasks S1-S4 to establish baseline and verify test harness:
- Should see 75-90% success rates
- Low coordination overhead
- Fast iteration cycles
- Build confidence in measurement

### Phase 2: Probe Weaknesses (Weeks 3-4)
Implement tasks W1-W4 to identify failure modes:
- Expect 20-40% success rates
- High coordination overhead or deep context
- Slow iteration (complex tasks)
- Identify specific bottlenecks

### Phase 3: Explore Hybrids (Weeks 5-6)
Test tasks H1-H3 to find boundaries:
- Expect 40-70% success rates
- Mixed characteristics
- Identify tipping points
- Map task-model fit

### Phase 4: Systematic Variation (Weeks 7-8)
Vary coordination models across all tasks:
- Test cue-based vs. event-driven vs. polling
- Test hub-and-spoke vs. peer-to-peer
- Test Jidoka vs. circuit breaker
- Build comprehensive performance matrix

---

## Success Criteria for Orient Phase

We'll know we've successfully oriented when we can answer:

1. **For each task type (S1-W4):** Which coordination model performs best?
2. **For each coordination model:** What task characteristics favor it?
3. **For scaling:** At what agent count does each model break?
4. **For failures:** Which error handling prevents cascades in each task?
5. **For handoffs:** When does compression/transfer degrade performance?

This data will directly inform implementation decisions in Phase 4 (Decide) and Phase 5 (Act).

---

## Sources

### Benchmarks and Evaluations
- [10 AI Agent Benchmarks](https://www.evidentlyai.com/blog/ai-agent-benchmarks)
- [Best AI Agent Evaluation Benchmarks: 2025 Complete Guide](https://o-mega.ai/articles/the-best-ai-agent-evals-and-benchmarks-full-2025-guide)
- [TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://openreview.net/forum?id=LZnKNApvhG)
- [SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?](https://arxiv.org/html/2509.16941)
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://webarena.dev/)

### Multi-Agent Failures and Coordination
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/html/2503.13657v1)
- [Why Multi-Agent LLM Systems Fail: Key Issues Explained](https://orq.ai/blog/why-do-multi-agent-llm-systems-fail)
- [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/pdf/2402.03578)
- [Towards a Science of Scaling Agent Systems](https://arxiv.org/html/2512.08296v1)
- [Coordinated LLM multi-agent systems for collaborative question-answer generation](https://www.sciencedirect.com/science/article/pii/S0950705125016661)

### Workflow Patterns and Success Cases
- [20 Agentic AI Workflow Patterns That Actually Work in 2025](https://skywork.ai/blog/agentic-ai-examples-workflow-patterns-2025/)
- [Top AI Agentic Workflow Patterns](https://blog.bytebytego.com/p/top-ai-agentic-workflow-patterns)
- [AI Agent Workflows: Everything You Need to Know](https://www.gooddata.com/blog/ai-agent-workflows-everything-you-need-to-know/)
- [10 Agentic AI Examples & Use Cases In 2026](https://www.warmly.ai/p/blog/agentic-ai-examples)
- [AI Agents in 2025: Top 8 Use Cases & Real-World Applications](https://tkxel.com/blog/ai-agents-use-cases-2025/)
- [The state of AI in 2025: Agents, innovation, and transformation](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)

### State of LLMs and Agent Systems
- [The State Of LLMs 2025: Progress, Progress, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)
- [Rethinking LLM Benchmarks for 2025: Why Agentic AI Needs a New Evaluation Standard](https://www.fluid.ai/blog/rethinking-llm-benchmarks-for-2025)
- [Evaluating LLM Agents in Multi-Step Workflows (2026 Guide)](https://www.codeant.ai/blogs/evaluate-llm-agentic-workflows)
- [Multi-agent LLMs in 2025 [+frameworks]](https://www.superannotate.com/blog/multi-agent-llms)
