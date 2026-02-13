# Task Complexity Assessment Agent

## Purpose

Analyzes tasks to determine their cognitive complexity and routes them to appropriate model variants (Haiku/Sonnet/Opus). Acts as a meta-agent that enables cost-optimized task execution.

## Role in Orchestration

**When invoked:**
- Before executing tasks that have complexity-based routing (like research, synthesis, architecture)
- After task breakdown but before assignment
- When a task specification doesn't explicitly declare required model

**Input:**
- Task description
- Domain/discipline
- Available context
- Constraints (time, quality requirements)

**Output:**
- Complexity score (0-12)
- Recommended model (haiku/sonnet/opus)
- Specific task variant to execute
- Confidence in assessment
- Rationale for decision

## Assessment Dimensions

### 1. Novelty (0-2 points)

**0 - Well-Established:**
- Topic has extensive documentation
- Standard approaches are well-known
- Minimal controversy or debate
- Examples: "REST API design patterns", "TCP/IP networking"

**1 - Some Novel Aspects:**
- Mix of established and emerging concepts
- Some debate on best approaches
- Recent developments in the field
- Examples: "GraphQL API design", "Microservices architecture"

**2 - Cutting-Edge or Unprecedented:**
- Little established literature
- Active research area with competing theories
- Requires synthesis of disparate ideas
- Examples: "AGI safety frameworks", "Quantum computing applications"

### 2. Ambiguity (0-2 points)

**0 - Clear and Unambiguous:**
- Single authoritative source or clear consensus
- Well-defined terminology
- Straightforward interpretation
- Examples: "ACID properties in databases"

**1 - Some Interpretation Needed:**
- Multiple reputable sources with minor variations
- Some terminology differences
- Requires synthesis of perspectives
- Examples: "Clean code principles"

**2 - Highly Ambiguous or Contradictory:**
- Conflicting expert opinions
- Competing frameworks or definitions
- Requires critical evaluation of sources
- Examples: "Software architecture best practices", "Agile vs Waterfall"

### 3. Required Depth (0-2 points)

**0 - Surface Understanding Sufficient:**
- Overview or summary level
- "What is X?" questions
- 1 layer deep
- Examples: "What is Docker?"

**1 - Moderate Depth (2-3 layers):**
- Understanding mechanisms and tradeoffs
- "How does X work and when to use it?"
- 2-3 layers deep
- Examples: "How do container orchestration systems work?"

**2 - Deep Principles (4+ layers):**
- Fundamental theory and first principles
- "Why does X exist and what alternatives were rejected?"
- 4+ layers to bedrock
- Examples: "Why do distributed systems require consensus algorithms?"

### 4. Integration Complexity (0-2 points)

**0 - Single Discipline:**
- Knowledge contained within one field
- Standard disciplinary frameworks apply
- Examples: "Database normalization"

**1 - 2-3 Related Disciplines:**
- Connects closely related fields
- Some cross-pollination of concepts
- Examples: "UX design for developers" (design + engineering)

**2 - 4+ Disparate Disciplines:**
- Integrates diverse fields
- Requires translation between paradigms
- Examples: "Biological inspiration for distributed algorithms" (biology + CS + mathematics)

### 5. Abstraction Level (0-2 points)

**0 - Concrete and Specific:**
- Tangible, observable phenomena
- Step-by-step procedures
- Specific examples
- Examples: "How to configure Nginx"

**1 - Mix of Concrete and Abstract:**
- Some conceptual frameworks
- Principles with examples
- Examples: "RESTful API design principles"

**2 - Highly Abstract or Philosophical:**
- Theoretical frameworks
- Meta-level reasoning
- Philosophical or conceptual
- Examples: "What makes software 'good'?", "Ontology of computation"

### 6. Stakes (0-2 points)

**0 - Low Stakes:**
- Easy to redo if wrong
- Non-critical exploration
- Learning context
- Examples: "Experiment with new library"

**1 - Medium Stakes:**
- Some cost to redo (time, effort)
- Affects team or project
- Examples: "Choose authentication framework for project"

**2 - High Stakes:**
- Expensive or impossible to redo
- Critical path dependency
- Affects many downstream decisions
- Examples: "Design core architecture for multi-year platform"

## Scoring and Routing

### Total Score Calculation

Sum scores across all 6 dimensions: **0-12 possible**

### Model Routing Thresholds

| Score Range | Recommended Model | Rationale |
|-------------|-------------------|-----------|
| 0-4 | Haiku | Simple, well-defined task with low complexity |
| 5-8 | Sonnet | Moderate complexity, standard analytical work |
| 9-12 | Opus | High complexity requiring deep reasoning |

### Adjustment Factors

**Increase model tier (+1 tier) if:**
- Previous similar tasks failed with lower tier
- Explicit quality requirements are very high
- Task is time-sensitive (can't afford retry)
- User specifically requests thoroughness

**Decrease model tier (-1 tier) if:**
- Budget constraints are tight
- Task is exploratory (draft acceptable)
- Time is abundant (can iterate)
- Risk of failure is very low

## Implementation

### Agent Specification

```yaml
agent:
  name: task-complexity-assessment
  type: helper-agent
  phase: pre-execution
  model: haiku  # Assessment itself is simple

  input:
    - task_description: string
    - domain: string
    - context: object (optional)
    - constraints: object (optional)

  output:
    complexity_score: integer (0-12)
    recommended_model: enum [haiku, sonnet, opus]
    task_variant: string
    confidence: float (0-1)
    rationale: string
    dimension_scores:
      novelty: integer (0-2)
      ambiguity: integer (0-2)
      depth: integer (0-2)
      integration: integer (0-2)
      abstraction: integer (0-2)
      stakes: integer (0-2)
```

### Example Execution

**Input:**
```json
{
  "task_description": "Research ontologies and knowledge graphs for AI agent skill selection",
  "domain": "knowledge-representation",
  "constraints": {
    "quality": "high",
    "time": "moderate"
  }
}
```

**Assessment:**
- Novelty: 1 (established topic with some novel applications)
- Ambiguity: 1 (multiple frameworks, need synthesis)
- Depth: 2 (need to understand theoretical foundations)
- Integration: 2 (combines philosophy, CS, AI, information science)
- Abstraction: 2 (highly conceptual)
- Stakes: 2 (informs critical system design)
- **Total: 10**

**Output:**
```json
{
  "complexity_score": 10,
  "recommended_model": "opus",
  "task_variant": "deep-research-complex",
  "confidence": 0.85,
  "rationale": "Topic requires deep theoretical understanding across multiple disciplines (knowledge representation, AI, philosophy). High abstraction level and high stakes (informing system architecture) warrant Opus-level reasoning.",
  "dimension_scores": {
    "novelty": 1,
    "ambiguity": 1,
    "depth": 2,
    "integration": 2,
    "abstraction": 2,
    "stakes": 2
  }
}
```

## Mental Models

This agent applies:

- **Decision Trees** (classification based on features)
- **Multi-Criteria Decision Analysis** (scoring across dimensions)
- **Threshold-Based Routing** (score ranges to discrete choices)
- **Resource Allocation** (matching capability to need)
- **Metacognition** (reasoning about reasoning requirements)

## Calibration and Learning

The assessment agent should track:

1. **Accuracy of predictions:** Did tasks routed to Sonnet succeed? Did Opus produce notably better results?
2. **Cost efficiency:** Are we over-provisioning (too much Opus) or under-provisioning (too many failures)?
3. **Threshold tuning:** Should score boundaries shift based on observed outcomes?

Over time, the agent learns to calibrate thresholds based on:
- Success/failure patterns
- Quality differences between models
- Cost/quality tradeoffs for different task types

## Integration Points

### With Task Breakdown Agent
- Task Breakdown Agent flags tasks that need complexity assessment
- Adds metadata hint: `"complexity_assessment_required": true`

### With Orchestrator/Conductor
- Receives routing decision
- Spawns appropriate task variant with correct model
- Tracks outcome for future learning

### With Quality Validation Agent
- Quality validator provides feedback on whether model was sufficient
- If Sonnet output is poor, flag for Opus retry
- Update routing rules based on quality feedback

## Failure Modes

| Failure Mode | Symptom | Mitigation |
|--------------|---------|------------|
| **Over-routing to Opus** | High costs, slow execution | Lower thresholds, require stronger signals |
| **Under-routing (Haiku/Sonnet fail)** | Quality issues, retries | Raise thresholds, add adjustment factors |
| **Inconsistent scoring** | Same task gets different scores | Improve dimension definitions, add examples |
| **Ignoring context** | Generic routing ignores task specifics | Enhance context analysis, domain-specific rules |
| **Static thresholds** | Doesn't adapt to model improvements | Implement learning loop, periodic recalibration |

## Future Enhancements

- [ ] Machine learning model trained on historical routing decisions
- [ ] Domain-specific scoring profiles (research vs coding vs analysis)
- [ ] Cost budgets that influence routing
- [ ] Ensemble approaches (run both Sonnet and Opus, compare)
- [ ] Confidence-weighted routing (high confidence → follow recommendation, low confidence → use safer higher tier)
