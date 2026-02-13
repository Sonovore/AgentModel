# Model Selection Strategy for Agent Tasks

## Purpose

Different tasks require different levels of cognitive capability. Using the right model for each task optimizes cost, latency, and quality. This document defines how to select models for agent tasks and when to use complexity assessment.

## Model Capabilities and Cost

| Model | Speed | Cost (relative) | Best For |
|-------|-------|-----------------|----------|
| **Haiku** | Fastest | 1x | Simple, well-defined tasks with clear patterns |
| **Sonnet** | Fast | ~20x | Most research, analysis, and writing tasks |
| **Opus** | Slower | ~60x | Complex reasoning, novel synthesis, high-stakes decisions |

## Task Classification Framework

### Haiku Tasks (Simple, Pattern-Based)

**Characteristics:**
- Clear instructions with established patterns
- Minimal ambiguity or interpretation needed
- Straightforward input/output transformations
- Low risk of failure

**Examples:**
- File operations (create, copy, move, rename)
- Template filling with provided data
- Format conversions (JSON to CSV, etc.)
- Directory structure creation
- Status checks and progress monitoring
- Simple text transformations
- README generation from established templates

**When to use:**
- Task has been done many times before with consistent results
- Instructions can be expressed in <200 words
- No novel problem-solving required
- Failure is easily detectable and correctable

### Sonnet Tasks (Balanced Analysis and Creation)

**Characteristics:**
- Requires analysis and synthesis
- Moderate complexity with some ambiguity
- Domain knowledge application
- Quality matters but not mission-critical

**Examples:**
- Research on established topics
- Technical documentation writing
- Code generation for known patterns
- Data analysis and visualization
- Mental model documentation (most cases)
- Helper agent specifications
- Cross-referencing and relationship mapping

**When to use:**
- Task requires understanding and applying concepts
- Multiple valid approaches exist
- Quality/accuracy is important
- Domain expertise is needed but not cutting-edge

### Opus Tasks (Complex Reasoning and Novel Synthesis)

**Characteristics:**
- Novel problems without clear precedents
- Requires deep reasoning or creative synthesis
- Cross-disciplinary integration
- High-stakes architectural decisions
- Abstract or philosophical questions

**Examples:**
- Designing new frameworks or architectures
- Cross-disciplinary synthesis (connecting 5+ disciplines)
- Resolving fundamental trade-offs
- Novel mental model identification
- Complex ontology design
- Strategic decision-making with high consequences
- Tasks where Sonnet has failed or produced poor results

**When to use:**
- No established pattern or precedent
- Requires genuine insight or creativity
- Multiple competing frameworks must be reconciled
- Failure would be costly (time, resources, trust)
- Task involves fundamental uncertainty

## Complexity Assessment Protocol

For tasks that could use multiple models (like research), use a **Complexity Assessment Agent** to route to the appropriate variant.

### Assessment Criteria

Rate each criterion 0-2:

| Criterion | 0 (Simple) | 1 (Moderate) | 2 (Complex) |
|-----------|------------|--------------|-------------|
| **Novelty** | Well-established topic | Some novel aspects | Cutting-edge or unprecedented |
| **Ambiguity** | Clear, unambiguous | Some interpretation needed | Highly ambiguous or contradictory sources |
| **Depth** | Surface/overview sufficient | 2-3 layers deep | 4+ layers, fundamental principles |
| **Integration** | Single discipline | 2-3 related disciplines | 4+ disparate disciplines |
| **Abstraction** | Concrete, specific | Mix of concrete and abstract | Highly abstract or philosophical |
| **Stakes** | Low (redo is cheap) | Medium (some cost to redo) | High (expensive to redo or critical path) |

**Scoring:**
- **0-4 points:** Use Haiku (if task is also pattern-based)
- **5-8 points:** Use Sonnet
- **9-12 points:** Use Opus

### Example: Deep Research Task Routing

**Original task:** "Deep research on [topic]"

**Complexity assessment evaluates:**
1. Is this topic well-documented or novel?
2. Are there clear authoritative sources or conflicting views?
3. Does it require 2-3 layers or 4+ layers of depth?
4. Single discipline or cross-disciplinary?
5. Concrete or abstract?
6. What's the cost of poor-quality research?

**Routes to:**
- `deep-research-simple` (Sonnet): Well-established topic, clear sources, 2-3 layers
- `deep-research-complex` (Opus): Novel synthesis, conflicting sources, 4+ layers, cross-disciplinary

## Task Naming Convention

When a task type has model variants, use this naming pattern:

```
<task-type>-<complexity-level>
```

Examples:
- `deep-research-simple` (Sonnet)
- `deep-research-complex` (Opus)
- `synthesis-routine` (Sonnet)
- `synthesis-novel` (Opus)
- `code-generation-standard` (Sonnet)
- `code-generation-novel-architecture` (Opus)

## Task Metadata Schema

Every task definition should include:

```yaml
task:
  name: "task-name"
  recommended_model: "haiku|sonnet|opus"
  model_rationale: "Why this model is appropriate"
  complexity_assessment_required: true|false
  fallback_model: "model to use if recommended fails"

  # If complexity_assessment_required: true
  complexity_routing:
    simple_variant: "task-name-simple"
    simple_model: "sonnet"
    complex_variant: "task-name-complex"
    complex_model: "opus"
    threshold: 8  # Complexity score threshold
```

## Implementation Patterns

### Pattern 1: Direct Assignment (No Routing)

For tasks with clear model requirements:

```python
task = {
    "name": "create-directory-structure",
    "model": "haiku",
    "rationale": "Simple file operations with clear template"
}
```

### Pattern 2: Complexity-Based Routing

For tasks where complexity varies:

```python
# Step 1: Assess complexity
assessment_task = {
    "name": "assess-research-complexity",
    "model": "haiku",  # Assessment itself is simple
    "input": {"topic": "Knowledge Graphs", "domain": "computer-science"},
    "output": "complexity_score"
}

# Step 2: Route based on assessment
if complexity_score >= 9:
    research_task = {
        "name": "deep-research-complex",
        "model": "opus",
        "topic": "Knowledge Graphs"
    }
else:
    research_task = {
        "name": "deep-research-simple",
        "model": "sonnet",
        "topic": "Knowledge Graphs"
    }
```

### Pattern 3: Fallback on Failure

If a cheaper model fails, escalate:

```python
try:
    result = execute_task(task, model="sonnet")
    if not meets_quality_threshold(result):
        raise QualityError()
except (QualityError, ExecutionError):
    result = execute_task(task, model="opus")
```

## Cost Optimization Strategies

### 1. Batch Similar Tasks
- Process all Haiku tasks together
- Group Sonnet research tasks
- Reserve Opus for true complexity

### 2. Progressive Enhancement
- Start with Haiku/Sonnet
- Human review flags quality issues
- Retry with higher model only when needed

### 3. Model Mixing in Pipelines
- Use Haiku for data gathering
- Use Sonnet for analysis
- Use Opus for final synthesis

### 4. Learning from History
- Track which tasks needed model escalation
- Adjust initial routing based on patterns
- Update complexity thresholds over time

## Mental Models Informing This Strategy

| Mental Model | Source | Application |
|--------------|--------|-------------|
| **Resource Allocation** | Economics | Match resource cost to task value |
| **Progressive Enhancement** | Web Development | Start cheap, enhance where needed |
| **Fast-Cheap-Good Triangle** | Project Management | Can't have all three; optimize per task |
| **Theory of Constraints** | Lean Manufacturing | Don't over-provision for non-bottleneck tasks |
| **Decision Trees** | ML/Statistics | Route tasks based on observable features |
| **Pareto Principle** | Management | 80% of tasks need 20% of the capability |

## Integration with Agent System

The orchestrator/conductor must:

1. **Receive task with complexity hints** from task breakdown
2. **Run complexity assessment** if task type supports routing
3. **Select appropriate model variant**
4. **Monitor quality** of outputs
5. **Learn from failures** to improve routing over time

## Future Enhancements

- [ ] Automatic complexity assessment using historical data
- [ ] Cost budgets that adapt model selection
- [ ] A/B testing to validate model routing decisions
- [ ] Multi-model ensembles for critical tasks
- [ ] Real-time model selection based on current queue depth
