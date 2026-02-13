# Baseline Agent Frameworks for Comparison Testing

**Purpose:** Identify existing agent control systems we can test against to validate our mental model implementations.

**Research Date:** 2026-01-21

---

## Executive Summary

Three major frameworks dominate the 2025-2026 multi-agent landscape, each with different coordination philosophies:

1. **LangGraph** (graph-based workflows) - Highest performance, most flexible, steepest learning curve
2. **CrewAI** (role-based teams) - Fastest development time, production-ready patterns, less flexible
3. **OpenAI Agents SDK** (handoff-based) - Minimalist primitives, production-ready, OpenAI-native

**Performance baseline:** LangGraph achieves lowest latency and token usage across benchmarks. CrewAI trades runtime performance for 8x faster development time (2 weeks vs 2 months to production).

**Market adoption:** 72% of enterprise AI projects now involve multi-agent architectures (up from 23% in 2024). CrewAI powers agents for 60% of Fortune 500 companies.

---

## Framework 1: LangGraph (Performance Leader)

### Coordination Approach

**Graph-based workflows:** Treats agent interactions as nodes in a directed graph with conditional logic, branching, and cycles.

**Architecture components:**
- **Nodes:** Agents or tools
- **Edges:** Connections with conditional logic
- **State:** Shared graph state accessible to all nodes
- **Checkpointing:** Durable execution with automatic state persistence

### Key Patterns

1. **Multi-Agent Network:** Divide-and-conquer with specialized experts for each domain
2. **Supervisor Pattern:** Supervisor agent coordinates multiple specialized agents, each with own scratchpad
3. **Reflection Pattern:** Agents collaborate in structured feedback loops for iterative improvement

### Performance Characteristics

**Benchmarked performance:**
- Lowest latency across all tasks
- Lowest token usage among frameworks
- Streaming support: 200-500ms latency reduction via token-by-token output
- Best for production-scale deployments requiring control and observability

**Tradeoffs:**
- Development time: ~2 months to production (longer than CrewAI)
- Learning curve: Steeper (graph-based thinking required)
- Flexibility: Highest (supports any workflow pattern)

### Implementation Resources

**Official repositories:**
- Main: [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) - Python implementation
- JavaScript: [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs) - TypeScript/JS implementation
- Examples: [von-development/awesome-LangGraph](https://github.com/von-development/awesome-LangGraph) - Ecosystem index

**Documentation:**
- [Multi-agent network tutorial](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)
- [LangGraph official docs](https://www.langchain.com/langgraph)

**Integration examples:**
- [Elasticsearch + LangGraph multi-agent](https://www.elastic.co/search-labs/blog/multi-agent-system-llm-agents-elasticsearch-langgraph)
- [Amazon Bedrock + LangGraph](https://aws.amazon.com/blogs/machine-learning/build-multi-agent-systems-with-langgraph-and-amazon-bedrock/)

### Testing Strategy

**What to test:**
1. Supervisor pattern vs our orchestrator-worker model
2. Graph-based coordination vs cue-based (WARNING/STANDBY/GO)
3. State management approach (shared graph state vs message passing)
4. Checkpointing overhead vs our error handling (Jidoka)
5. Performance baseline: measure their latency/token usage on our tasks

**Expected insights:**
- How much does graph flexibility cost in overhead?
- When does checkpointing become bottleneck?
- How does shared state scale vs message passing?

---

## Framework 2: CrewAI (Development Speed Leader)

### Coordination Approach

**Role-based teams:** Models crews of specialized agents that cooperate through roles, tasks, and collaboration protocols.

**Architecture components:**
- **Agents:** Defined by role, goal, backstory, and tools
- **Tasks:** Assigned to agents with context and expected output
- **Crews:** Collections of agents working together
- **Flows:** Event-driven pipelines managing execution paths and branching logic (2025 addition)
- **Process:** Sequential or hierarchical execution modes

### Key Patterns

1. **Sequential Process:** Tasks execute in order, output of one becomes context for next
2. **Hierarchical Process:** Manager agent coordinates planning, delegates tasks, validates results
3. **Asynchronous Collaboration:** Agents cooperate in rounds to accomplish goals

### Performance Characteristics

**Development speed:**
- 2 weeks to production (vs 2 months for LangGraph)
- Higher-level abstractions accelerate prototyping
- Ideal for content generation, analysis, role-based workflows

**Runtime performance:**
- Similar latency and token usage to OpenAI Swarm
- Higher than LangGraph but acceptable for most use cases
- Optimized for developer productivity over raw speed

**Tradeoffs:**
- Less flexible than LangGraph (shoehorning complex workflows harder)
- Better for multi-role problems (vs single agent with tools)
- Production-ready patterns out of the box

### Implementation Resources

**Official repositories:**
- Main: [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) - Official framework
- Tutorials: [bhancockio/crewai-updated-tutorial-hierarchical](https://github.com/bhancockio/crewai-updated-tutorial-hierarchical)
- Multi-agent examples: [akj2018/Multi-AI-Agent-Systems-with-crewAI](https://github.com/akj2018/Multi-AI-Agent-Systems-with-crewAI)

**Documentation:**
- [CrewAI Tasks documentation](https://docs.crewai.com/en/concepts/tasks)
- [Hierarchical mode discussion](https://github.com/crewAIInc/crewAI/discussions/1220)

**Market presence:**
- $18M funding (2025)
- Powers agents for 60% of Fortune 500 companies
- Active community and rapid iteration

### Testing Strategy

**What to test:**
1. Sequential process vs our pipeline coordination
2. Hierarchical process vs our hub-and-spoke with orchestrator
3. Role-based specialization vs our station-based specialization (kitchen brigade)
4. Task delegation patterns vs our task assignment protocols
5. Development time: How quickly can we replicate our tasks in CrewAI?

**Expected insights:**
- How much coordination overhead does hierarchical manager add?
- When does role-based abstraction become limitation?
- What's the productivity vs. performance tradeoff?

---

## Framework 3: OpenAI Agents SDK (Minimalist Approach)

### Coordination Approach

**Handoff-based:** Minimalist framework with four core primitives for production-ready agent systems.

**Architecture components:**
- **Agents:** Instruction-driven entities with model and tool access
- **Tools/Functions:** Any Python/TypeScript function with automatic schema generation
- **Handoffs:** Native delegation between agents (appears as tool to LLM: `transfer_to_refund_agent`)
- **Guardrails:** Input/output validation to constrain behavior

### Key Patterns

**Handoff pattern:**
```python
billing_agent = Agent(name="Billing agent")
refund_agent = Agent(name="Refund agent")
triage_agent = Agent(
    name="Triage agent",
    handoffs=[billing_agent, handoff(refund_agent)]
)
```

### Performance Characteristics

**Design philosophy:**
- Minimalist (4 primitives vs dozens in other frameworks)
- Production-ready from day one (replaces experimental Swarm)
- Dual-language support (Python and TypeScript/JavaScript equally supported)

**Integration:**
- Native OpenAI integration (optimized for OpenAI models)
- Automatic schema generation and validation
- Built-in handoff mechanics (no manual state wiring)

### Implementation Resources

**Official repositories:**
- Main: [openai/openai-agents-python](https://github.com/openai/openai-agents-python) - Python version
- Legacy: [openai/swarm](https://github.com/openai/swarm) - Educational framework (deprecated)
- Realtime: [openai/openai-realtime-agents](https://github.com/openai/openai-realtime-agents) - Realtime API patterns

**Documentation:**
- [OpenAI Agents SDK docs](https://openai.github.io/openai-agents-python/)
- [Handoffs documentation](https://openai.github.io/openai-agents-python/handoffs/)
- [Deep dive analysis](https://www.siddharthbharath.com/openai-agents-sdk/)

**Timeline:**
- Swarm released: ~2024 (experimental)
- Agents SDK released: March 2025 (production)
- Active maintenance by OpenAI team

### Testing Strategy

**What to test:**
1. Handoff pattern vs our task.handoff message protocol
2. Minimalist primitives vs our convention-based coordination
3. OpenAI-native performance vs framework-agnostic approaches
4. Guardrails vs our Jidoka error handling
5. Development simplicity vs flexibility

**Expected insights:**
- How much overhead do richer frameworks add?
- When is minimalism sufficient vs limiting?
- How do native integrations affect performance?

---

## Framework 4: Microsoft Multi-Agent Reference Architecture

### Overview

**Enterprise-focused reference implementation** designed for adaptive, scalable, and secure multi-agent systems based on real-world enterprise experience.

### Key Components

**Agent Registry:**
- Information repository about available agents
- Facilitates agent-to-agent communication
- Enables dynamic agent discovery

**Architecture principles:**
- Adaptive: Responds to changing requirements
- Scalable: Grows with system demands
- Secure: Enterprise-grade security patterns

### Implementation Resources

**Official repository:**
- [microsoft/multi-agent-reference-architecture](https://github.com/microsoft/multi-agent-reference-architecture)

**Documentation:**
- [Introduction](https://microsoft.github.io/multi-agent-reference-architecture/docs/Introduction.html)
- [Agent Registry details](https://microsoft.github.io/multi-agent-reference-architecture/docs/agent-registry/Agent-Registry.html)

**Integration:**
- Merges AutoGen + Semantic Kernel (October 2025)
- Enterprise deployment focus
- Active Microsoft maintenance

### Testing Strategy

**What to test:**
1. Agent registry pattern vs our hub routing
2. Enterprise patterns vs lean startup approach
3. Security model vs our convention-based trust
4. Scalability claims vs our measured scaling thresholds

**Expected insights:**
- What enterprise requirements add to architecture?
- When do registry patterns beat direct coordination?
- What security overhead is necessary vs optional?

---

## Additional Reference Implementations

### Educational: PicoAgents (Victor Dibia)

**Repository:** [victordibia/designing-multiagent-systems](https://github.com/victordibia/designing-multiagent-systems)

**Value:**
- Built from scratch for teaching (not production framework)
- Every component implemented with clarity and transparency
- Shows internal mechanics other frameworks hide
- Agent reasoning loops and orchestration patterns exposed

**Testing use:**
- Understand implementation details frameworks abstract
- Compare our low-level mechanics to proven patterns
- Validate our design decisions against educational best practices

### Workshop: Azure Multi-Agent Workshop

**Repository:** [Azure-Samples/multi-agent-workshop](https://github.com/Azure-Samples/multi-agent-workshop)

**Value:**
- Progressive exercises from simple to sophisticated
- Hands-on AutoGen and Semantic Kernel examples
- Real-world collaborative scenarios

**Testing use:**
- Standard tutorial tasks we can replicate
- Documented expected behaviors for comparison
- Baseline complexity ramp for our test suite

### Production: MetaGPT

**Repository:** [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)

**Value:**
- "First AI Software Company" concept
- One-line requirement → full specification (user stories, APIs, docs)
- Demonstrates ambitious multi-agent coordination

**Testing use:**
- Stress test our coordination at high complexity
- Compare output quality on software generation tasks
- Learn from production multi-agent system at scale

---

## Performance Benchmarks (2025 Data)

### Latency Comparison

**Ranking (fastest to slowest):**
1. **LangGraph** - Lowest latency across all tasks
2. **OpenAI Swarm** - Similar to CrewAI
3. **CrewAI** - Similar to Swarm
4. **LangChain** - Highest latency

**Token Usage:**
- **LangGraph** - Lowest token consumption
- **CrewAI/Swarm** - Similar (moderate)
- **LangChain** - Highest token usage

**Production considerations:**
- LangGraph streaming reduces perceived latency 200-500ms
- Token efficiency directly impacts API costs at scale
- Development speed vs execution speed tradeoff

### Development Time Comparison

**Time to production:**
- **CrewAI:** 2 weeks (simplicity and high-level abstractions)
- **LangGraph:** 2 months (flexibility requires more setup)

**Productivity factors:**
- CrewAI sparks creativity and accelerates prototyping
- LangGraph provides control and observability for enterprise scale
- OpenAI SDK minimalist approach (fastest learning curve)

---

## Recommended Testing Approach

### Phase 1: Baseline Performance (Week 1)

**Test all frameworks on Task S1 (parallel map-reduce):**

1. **LangGraph implementation**
   - Clone [langgraph tutorial](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)
   - Adapt to our Task S1 specification
   - Measure: latency, token usage, message count, code complexity

2. **CrewAI implementation**
   - Clone [sequential example](https://github.com/crewAIInc/crewAI)
   - Use sequential process for pipeline
   - Measure: same metrics + development time

3. **OpenAI Agents SDK implementation**
   - Clone [handoffs example](https://openai.github.io/openai-agents-python/handoffs/)
   - Implement with minimal primitives
   - Measure: same metrics

4. **Our mental model implementation**
   - Implement using our conventions + schemas
   - Apply hub-and-spoke + exception-based reporting
   - Measure: same metrics

**Comparison dimensions:**
- Performance: Which is fastest?
- Simplicity: Which has least code?
- Flexibility: Which adapts easiest to task variations?
- Observability: Which provides best debugging?

### Phase 2: Coordination Patterns (Week 2-3)

**Test coordination models on Task W2 (high-coordination multi-agent):**

1. **LangGraph supervisor pattern**
   - Central supervisor coordinating 5 agents
   - Shared graph state
   - Measure coordination overhead

2. **CrewAI hierarchical process**
   - Manager agent with 5 specialized workers
   - Task delegation and validation
   - Measure coordination overhead

3. **OpenAI handoff chains**
   - Agents handing off via transfer functions
   - Minimal state management
   - Measure coordination overhead

4. **Our cue-based coordination**
   - WARNING/STANDBY/GO protocol
   - Hub-and-spoke message routing
   - Measure coordination overhead

**Key questions:**
- At what agent count does each model break?
- Which has lowest communication overhead?
- Which handles failures most gracefully?

### Phase 3: Scaling Analysis (Week 4-5)

**Test all models at 3, 5, 10, 20 agents:**

- Use Tasks S1 (parallel) and S2 (sequential)
- Measure overhead growth rate
- Identify bottlenecks for each framework
- Map scaling characteristics

**Expected findings:**
- LangGraph: Best raw performance, scales well with overhead
- CrewAI: Good mid-scale, hierarchical manager may bottleneck
- OpenAI: Minimal overhead, but limited coordination features
- Our model: TBD (this is what we're learning!)

### Phase 4: Task-Model Fit (Week 6-7)

**Test all models across task suite (S1-S4, W1-W4, H1-H3):**

- Create performance matrix: framework × task type
- Identify which frameworks excel at which tasks
- Document anti-patterns (what fails badly)
- Build decision framework for model selection

**Deliverable:**
Comprehensive guide: "For task type X, use coordination model Y because..."

---

## Success Criteria for Baseline Testing

We'll know baseline testing succeeded when we can answer:

1. **Performance:** How does our implementation compare to LangGraph (performance leader)?
2. **Development speed:** How does our implementation compare to CrewAI (productivity leader)?
3. **Simplicity:** How does our implementation compare to OpenAI SDK (minimalism leader)?
4. **Task fit:** For each task type, which framework performs best and why?
5. **Scaling:** At what agent count does each framework break?
6. **Validation:** Do our mental models (Magnificent Seven) beat existing frameworks?

If our mental models don't outperform existing frameworks, we learn:
- Which of our models should be replaced with proven patterns
- Where theory diverged from practice
- What the actual bottlenecks are (not what we thought they'd be)

**This is Orient phase success:** Empirical understanding before implementation commitment.

---

## Implementation Recommendation

**Start with LangGraph + CrewAI comparison:**

1. **Week 1:** Implement Task S1 in both frameworks + our model
2. **Week 2:** Analyze differences, measure performance
3. **Week 3:** Add OpenAI SDK for minimalist comparison
4. **Week 4:** Scale to remaining tasks

**Why this order:**
- LangGraph: Performance baseline (what's possible)
- CrewAI: Productivity baseline (what's practical)
- OpenAI SDK: Simplicity baseline (what's minimal)
- Our model: Mental model validation (does theory work?)

**Deliverable:**
Performance matrix showing which approach wins for which task type, with measured data backing every claim.

---

## Sources

### Framework Comparisons
- [CrewAI vs LangGraph vs AutoGen: Choosing the Right Multi-Agent AI Framework](https://www.datacamp.com/tutorial/crewai-vs-langgraph-vs-autogen)
- [Best AI Agent Frameworks 2025: LangGraph, CrewAI, OpenAI, LlamaIndex, AutoGen](https://www.getmaxim.ai/articles/top-5-ai-agent-frameworks-in-2025-a-practical-guide-for-ai-builders/)
- [LangGraph vs AutoGen vs CrewAI: Complete Comparison + Architecture Analysis 2025](https://latenode.com/blog/platform-comparisons-alternatives/automation-platform-comparisons/langgraph-vs-autogen-vs-crewai-complete-ai-agent-framework-comparison-architecture-analysis-2025)
- [Comparing AI agent frameworks: CrewAI, LangGraph, and BeeAI](https://developer.ibm.com/articles/awb-comparing-ai-agent-frameworks-crewai-langgraph-and-beeai/)

### LangGraph Resources
- [LangGraph Official Documentation](https://www.langchain.com/langgraph)
- [LangGraph GitHub Repository](https://github.com/langchain-ai/langgraph)
- [Multi-agent network tutorial](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)
- [LangGraph Multi-Agent Orchestration Guide 2025](https://latenode.com/blog/ai-frameworks-technical-infrastructure/langgraph-multi-agent-orchestration/langgraph-multi-agent-orchestration-complete-framework-guide-architecture-analysis-2025)
- [Awesome-LangGraph Ecosystem Index](https://github.com/von-development/awesome-LangGraph)

### CrewAI Resources
- [CrewAI GitHub Repository](https://github.com/crewAIInc/crewAI)
- [CrewAI Tasks Documentation](https://docs.crewai.com/en/concepts/tasks)
- [CrewAI Framework 2025 Complete Review](https://latenode.com/blog/ai-frameworks-technical-infrastructure/crewai-framework/crewai-framework-2025-complete-review-of-the-open-source-multi-agent-ai-platform)
- [Multi-AI-Agent Systems with crewAI Examples](https://github.com/akj2018/Multi-AI-Agent-Systems-with-crewAI)

### OpenAI Agents SDK Resources
- [OpenAI Agents SDK Official Documentation](https://openai.github.io/openai-agents-python/)
- [OpenAI Agents Python GitHub](https://github.com/openai/openai-agents-python)
- [OpenAI Swarm (Educational Framework)](https://github.com/openai/swarm)
- [OpenAI Agents SDK Review (December 2025)](https://mem0.ai/blog/openai-agents-sdk-review)
- [A Deep Dive Into The OpenAI Agents SDK](https://www.siddharthbharath.com/openai-agents-sdk/)
- [Handoffs Documentation](https://openai.github.io/openai-agents-python/handoffs/)

### Reference Implementations
- [Microsoft Multi-Agent Reference Architecture](https://microsoft.github.io/multi-agent-reference-architecture/)
- [PicoAgents: Designing Multi-Agent Systems](https://github.com/victordibia/designing-multiagent-systems)
- [Azure Multi-Agent Workshop](https://github.com/Azure-Samples/multi-agent-workshop)
- [MetaGPT: Multi-Agent Framework](https://github.com/FoundationAgents/MetaGPT)

### Performance Benchmarks
- [Best AI Agent Frameworks in 2025: Performance Comparison](https://langwatch.ai/blog/best-ai-agent-frameworks-in-2025-comparing-langgraph-dspy-crewai-agno-and-more)
- [LangGraph vs CrewAI: Comparison Guide for Production Agents](https://xcelore.com/blog/langgraph-vs-crewai/)
- [Top 5 Open-Source Agentic Frameworks in 2026](https://research.aimultiple.com/agentic-frameworks/)
- [14 AI Agent Frameworks Compared](https://softcery.com/lab/top-14-ai-agent-frameworks-of-2025-a-founders-guide-to-building-smarter-systems)
