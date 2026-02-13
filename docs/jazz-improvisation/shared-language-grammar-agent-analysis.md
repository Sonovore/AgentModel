# Shared Language/Grammar: Architectural Analysis for AI Agent Systems

## Executive Summary

Shared grammar in jazz provides the foundation for all coordination - without common language, musicians cannot predict, respond to, or support each other. For AI agent systems, the parallel is exact: **shared conventions (documented in CLAUDE.md, schemas, protocols) are the infrastructure that makes coordination possible**.

The key insight is that grammar is not just documentation - it's **operational infrastructure**. Incomplete grammar means incomplete coordination capability. Inconsistent grammar means coordination conflicts. Grammar that exists only in documentation (not internalized by agents) is unusable in real-time.

| Jazz Grammar Layer | Agent Equivalent | Implementation |
|-------------------|------------------|----------------|
| **Harmonic grammar** | Data schemas and types | JSON Schema, Protocol Buffers |
| **Rhythmic grammar** | Timing and sync conventions | Polling intervals, timeouts |
| **Formal grammar** | Process and workflow patterns | State machines, workflows |
| **Role grammar** | Agent responsibilities | Service boundaries, ownership |
| **Genre grammar** | Domain-specific conventions | Industry standards, domain models |
| **Timbral grammar** | Quality and style conventions | Coding standards, logging formats |

The central architectural claim: **investment in grammar (conventions, documentation, schemas) pays off exponentially in reduced coordination overhead. Systems with rich, consistent grammar coordinate implicitly; systems with sparse grammar require explicit orchestration for everything.**

---

## Part I: The Grammar-Coordination Relationship

### Grammar Quality Determines Coordination Capacity

The quality of shared grammar directly determines what coordination is achievable:

| Grammar Quality | Coordination Achievable |
|-----------------|------------------------|
| No shared grammar | No coordination possible |
| Basic schema agreement | Request-reply works |
| Comprehensive conventions | Implicit coordination possible |
| Deep, consistent grammar | Emergent coordination possible |

This is not metaphorical - it's architectural. Without grammar:
- Agents cannot predict each other's behavior
- Messages cannot be interpreted consistently
- State cannot be shared meaningfully
- Errors cannot be distinguished from intent

### The Bandwidth Argument

Grammar enables bandwidth efficiency through prediction.

**Without shared grammar**:
```
Agent A: "I am now processing order 12345. The order contains 3 items.
         I will validate each item against inventory. If all items are
         available, I will calculate the total including tax at 8.5%.
         I will then create a shipment record..."

Agent B: "I understand. I will wait for your completion signal which
         should indicate success or failure along with..."
```

**With shared grammar**:
```
Agent A: { "type": "order.processing", "order_id": "12345" }

Agent B: [Knows exactly what this means, what will happen, what response to expect]
```

The compression ratio can be 100:1 or more. All the implicit knowledge - what "order.processing" means, what steps it involves, what responses follow - is encoded in shared grammar, not explicit messages.

### Grammar Must Be Operational

Jazz grammar is not intellectual knowledge - it's embodied, automatic, real-time accessible. Agent grammar must similarly be **operational**:

| Grammar Type | Characteristic | Usability |
|--------------|----------------|-----------|
| **Documentation-only** | Written down, must be looked up | Slow, error-prone |
| **Schema-enforced** | Built into tooling, automatically checked | Better, catches violations |
| **Internalized** | Part of agent's baseline behavior | Real-time coordination possible |

The goal: grammar so pervasive that agents don't "follow conventions" - they simply cannot violate them because the conventions are built into their operating context.

---

## Part II: Grammar Layer Analysis for Agents

### Layer 1: Schema Grammar (Harmonic)

**Jazz parallel**: Harmonic grammar constrains which notes fit at each moment.

**Agent equivalent**: Data schemas constrain what messages and state look like.

**Implementation**:
```json
// JSON Schema example
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "type": { "type": "string", "pattern": "^order\\." },
    "order_id": { "type": "string" },
    "items": {
      "type": "array",
      "items": { "$ref": "#/$defs/OrderItem" }
    }
  },
  "required": ["type", "order_id"]
}
```

**Coordination enabled**:
- All agents interpret messages identically
- Invalid messages rejected before processing
- Downstream agents can depend on structure

**CLAUDE.md Template**:
```markdown
# Data Schemas

## Message Formats
All inter-agent messages follow schemas in `/schemas/*.json`.

## Validation
- All outgoing messages must validate against schema
- All incoming messages must be validated before processing
- Invalid messages: Log, reject, respond with error

## Schema Evolution
- Minor changes (additive): Backward compatible
- Major changes: Version negotiation required
- Never: Remove required fields without major version
```

### Layer 2: Timing Grammar (Rhythmic)

**Jazz parallel**: Rhythmic grammar synchronizes temporal structure.

**Agent equivalent**: Timing conventions synchronize agent activities.

**Implementation**:
```markdown
# Timing Conventions

## Polling Intervals
- Status checks: Every 5 seconds
- Health checks: Every 10 seconds
- Batch processing: Every 60 seconds

## Timeouts
- Fast operations: 1 second
- Normal operations: 5 seconds
- Heavy operations: 30 seconds

## Retry Timing
- First retry: 100ms
- Second retry: 500ms
- Third retry: 2000ms
- After third: Escalate

## Synchronization Points
- Workflow boundaries: Explicit wait
- Transaction commits: Sequential
- Event ordering: Within partition only
```

**Coordination enabled**:
- Agents know when to expect responses
- Timeouts don't fire prematurely
- Retries don't overwhelm

### Layer 3: Process Grammar (Formal)

**Jazz parallel**: Form structures provide macro-level organization.

**Agent equivalent**: Process patterns define workflow organization.

**Implementation**:
```markdown
# Process Patterns

## Standard Workflow Form
1. **Initiation**: Task received, validated, acknowledged
2. **Processing**: Core work, progress signals
3. **Completion**: Results produced, success/failure signaled
4. **Cleanup**: Resources released, state finalized

## Checkpoint Protocol
- Checkpoint at: Each process phase boundary
- Checkpoint contains: Current state, progress, recoverable context
- Recovery from checkpoint: Resume from last successful phase

## Multi-Step Patterns
- Sequential: Each step waits for previous
- Parallel: Steps run concurrently, join at barrier
- Pipeline: Steps overlap, streaming handoff
```

**Coordination enabled**:
- Agents know where they are in process
- Recovery from any checkpoint possible
- Handoffs occur at defined boundaries

### Layer 4: Role Grammar (Responsibility)

**Jazz parallel**: Role conventions define instrument responsibilities.

**Agent equivalent**: Service boundaries define agent responsibilities.

**Implementation**:
```markdown
# Service Responsibilities

## Agent Roles
| Role | Responsibility | Does NOT Do |
|------|----------------|-------------|
| Orchestrator | Task assignment, monitoring | Data processing |
| Worker | Data processing, transformation | Task assignment |
| Validator | Schema validation, business rules | Data modification |
| Storage | Persistence, retrieval | Business logic |

## Ownership Boundaries
- Orders: OrderService owns order state
- Customers: CustomerService owns customer state
- Inventory: InventoryService owns inventory state

## Cross-Boundary Protocol
- To read owned state: Query owning service
- To modify owned state: Request to owning service
- Never: Direct modification of state you don't own
```

**Coordination enabled**:
- Clear accountability
- No conflicting modifications
- Predictable who handles what

### Layer 5: Domain Grammar (Genre)

**Jazz parallel**: Genre conventions set style-specific expectations.

**Agent equivalent**: Domain conventions set context-specific expectations.

**Implementation**:
```markdown
# Domain Conventions: E-Commerce

## Order Lifecycle
CREATED -> VALIDATED -> PAID -> FULFILLED -> COMPLETED
          -> CANCELLED (from any state before FULFILLED)

## Pricing Conventions
- All prices in cents (integer)
- Currency always explicit
- Tax calculated at checkout, not per-item

## Inventory Conventions
- Soft reserve on cart add
- Hard reserve on payment
- Release on cancellation

## Domain Vocabulary
| Term | Definition |
|------|------------|
| SKU | Unique product identifier |
| Cart | Temporary order before checkout |
| Order | Confirmed purchase |
```

**Coordination enabled**:
- All agents share domain understanding
- Business logic consistent across services
- Domain terms have precise meanings

### Layer 6: Quality Grammar (Timbral)

**Jazz parallel**: Timbral conventions set sound quality expectations.

**Agent equivalent**: Quality conventions set code/output standards.

**Implementation**:
```markdown
# Quality Conventions

## Logging Format
```json
{
  "timestamp": "ISO8601",
  "level": "info|warn|error",
  "service": "service_name",
  "trace_id": "correlation_id",
  "message": "Human readable",
  "context": { "structured": "data" }
}
```

## Error Response Format
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable",
    "details": { "structured": "context" }
  }
}
```

## Code Style
- Language: [language conventions]
- Naming: [naming conventions]
- Structure: [structural conventions]
```

**Coordination enabled**:
- Logs are parseable across services
- Errors are handleable consistently
- Code is readable by any agent/human

---

## Part III: Where Agents Struggle with Grammar

### Challenge 1: Grammar Must Be Specified, Not Learned

Jazz musicians learn grammar through years of immersion. Agents must have grammar explicitly specified.

**The Problem**: Agents cannot infer conventions from examples. They must be told.

**Manifestation**:
- Agent handles documented cases correctly
- Agent fails on undocumented cases
- Agent cannot generalize from examples

**Mitigation**: Exhaustive documentation. Every convention must be written.

**CLAUDE.md Template**:
```markdown
# Convention Coverage Checklist

## For Every Agent Operation
- [ ] Input format documented
- [ ] Output format documented
- [ ] Error cases enumerated
- [ ] Edge cases addressed
- [ ] Timing expectations stated
- [ ] Dependencies listed

## For Every Cross-Agent Interaction
- [ ] Protocol documented
- [ ] Message formats schema'd
- [ ] Success criteria defined
- [ ] Failure handling specified
- [ ] Recovery protocol defined
```

### Challenge 2: Grammar Drift Over Time

As systems evolve, grammar can drift - different parts of the system develop different conventions.

**The Problem**: Agents in the same system may follow incompatible grammars.

**Manifestation**:
- New services use different conventions than old
- Refactored code follows different patterns
- Different teams develop different standards

**Mitigation**: Grammar governance and enforcement.

**CLAUDE.md Template**:
```markdown
# Grammar Governance

## Single Source of Truth
All conventions documented in: `/docs/conventions/`

## Change Protocol
1. Propose change via PR to conventions doc
2. Review by architecture team
3. Approve or reject with rationale
4. If approved: Update all affected documentation
5. Communicate change to all agents/teams

## Enforcement
- CI checks for schema compliance
- Linting for code conventions
- Runtime validation for message formats
- Audit logging for protocol compliance
```

### Challenge 3: Grammar Depth - Automatic vs. Lookup

Even well-documented grammar may not be "internalized" by agents.

**The Problem**: Agents may need to "look up" conventions rather than having them built-in.

**Manifestation**:
- Agent consults documentation during operation
- Latency increases when conventions needed
- Edge cases fall back to defaults

**Mitigation**: Build grammar into agent operating context.

**CLAUDE.md Template**:
```markdown
# Grammar Internalization

## Always-Loaded Context
The following conventions are ALWAYS loaded in context:
- Data schemas for this domain
- Core process patterns
- Error handling protocol
- Role boundaries

## On-Demand Reference
The following may be looked up when needed:
- Edge case handling
- Rarely-used protocols
- Historical compatibility rules

## Grammar Embedding
- Schemas compiled into code
- Conventions enforced by tooling
- Patterns provided as libraries/templates
```

### Challenge 4: Grammar Conflicts

Different grammar layers may conflict, requiring resolution.

**The Problem**: What happens when timing grammar says "respond in 1 second" but process grammar says "complete all validation steps"?

**Manifestation**:
- Agents follow one convention, violate another
- Different agents resolve conflicts differently
- Coordination breaks when resolution varies

**Mitigation**: Explicit priority and resolution rules.

**CLAUDE.md Template**:
```markdown
# Grammar Conflict Resolution

## Priority Hierarchy
1. Safety constraints (never violated)
2. Data integrity (never compromised)
3. Security requirements (always met)
4. Domain grammar (business rules)
5. Process grammar (workflow patterns)
6. Timing grammar (performance targets)
7. Quality grammar (style preferences)

## Conflict Resolution Protocol
When conventions conflict:
1. Identify which layer each belongs to
2. Higher priority layer wins
3. Document the resolution and rationale
4. If unclear, escalate to human

## Example Resolutions
- Timing vs Process: If validation cannot complete in timeout, extend timeout (process > timing)
- Quality vs Domain: If domain requires non-standard format, follow domain (domain > quality)
```

---

## Part IV: Grammar as Coordination Infrastructure

### The Grammar Investment Argument

Grammar is infrastructure. Investment pays off across all coordination:

| Grammar Investment | Coordination Return |
|--------------------|---------------------|
| Document one schema | All agents can exchange that message type |
| Document one process | All agents can participate in that workflow |
| Document role boundaries | All agents know their responsibilities |
| Document conventions consistently | Agents coordinate without explicit messaging |

The return compounds:
- Each new agent immediately benefits from all documented grammar
- Each convention enables implicit coordination across all agents that know it
- Grammar scales without proportional coordination overhead

### Grammar Completeness Determines Coordination Ceiling

The maximum coordination capability is bounded by grammar completeness:

```
Max Coordination = f(Grammar Completeness, Grammar Consistency, Grammar Depth)
```

Where:
- **Completeness**: What % of needed conventions are documented
- **Consistency**: What % of documentation is internally consistent
- **Depth**: What % of grammar is operationally internalized

To increase coordination capability, invest in grammar, not orchestration.

### Grammar vs. Orchestration Trade-off

Systems can coordinate through two mechanisms:

| Mechanism | When Works | Cost |
|-----------|------------|------|
| **Grammar** (conventions) | When behavior is predictable from rules | Documentation upfront, minimal runtime |
| **Orchestration** (explicit messages) | When behavior varies by situation | Little upfront, significant runtime |

**Jazz insight**: The more grammar is shared, the less orchestration is needed.

**Design implication**: Before adding orchestration, ask "could this be a convention?"

**CLAUDE.md Template**:
```markdown
# Grammar vs. Orchestration Decision

## Default: Grammar
If a coordination need can be addressed by convention, do so.

## When Orchestration
Explicit orchestration for:
- Genuinely dynamic situations
- One-time or rare scenarios
- Contexts where conventions don't apply
- High-stakes decisions requiring validation

## Converting Orchestration to Grammar
If orchestration is repeated:
1. Identify the pattern
2. Document as convention
3. Implement as default behavior
4. Remove explicit orchestration
```

---

## Part V: Optimization Patterns

### Pattern 1: Schema-First Development

**Problem**: Data formats defined ad-hoc lead to integration pain.

**Solution**: Define schemas before implementation.

**Implementation**:
```markdown
# Schema-First Protocol

## Before Any New Message Type
1. Define JSON Schema in `/schemas/`
2. Review with affected agents/teams
3. Generate code from schema
4. Implement against generated types

## Schema Requirements
- All required fields marked
- All optional fields documented with defaults
- Enums for constrained values
- Patterns for formatted strings
- References for shared definitions

## Benefits
- Type safety across language boundaries
- Documentation from schema
- Validation generated automatically
```

### Pattern 2: Convention-as-Code

**Problem**: Documentation drifts from implementation.

**Solution**: Encode conventions in code/tooling.

**Implementation**:
```markdown
# Convention Enforcement

## Linting
- Naming conventions → Linter rules
- Format conventions → Formatter config
- Import conventions → Import sorter

## Validation
- Schema conventions → Runtime validators
- Protocol conventions → Contract tests
- Timing conventions → Timeout configuration

## Generation
- Code templates embody conventions
- Scaffolding generates conventional structure
- Examples are executable and tested
```

### Pattern 3: Convention Audit

**Problem**: Unknown convention violations accumulate.

**Solution**: Regular audits of convention compliance.

**Implementation**:
```markdown
# Convention Audit Protocol

## Automated Checks (CI/CD)
- Schema validation
- Lint checks
- Contract tests
- Timing verification

## Manual Review (Monthly)
- Sample agent outputs for convention compliance
- Review error logs for convention-related failures
- Check new code against conventions
- Update conventions if patterns changed

## Metrics
- Convention violation rate
- Undocumented pattern rate
- Grammar coverage %
```

### Pattern 4: Grammar Versioning

**Problem**: Grammar must evolve but changes break coordination.

**Solution**: Versioned grammar with migration support.

**Implementation**:
```markdown
# Grammar Version Management

## Version Format
grammar-v{major}.{minor}.{patch}

## Compatibility Rules
- Patch: Bug fixes, clarifications (always compatible)
- Minor: Additions (backward compatible)
- Major: Breaking changes (requires migration)

## Version in Messages
All messages include:
{
  "grammar_version": "v2.1.0",
  ...
}

## Migration Protocol
Major version upgrade:
1. Announce deprecation of old version
2. Support both versions during transition
3. Provide migration tools
4. Set deadline for old version removal
5. Remove old version support
```

### Pattern 5: Grammar Observatory

**Problem**: Can't improve what you can't see.

**Solution**: Monitor grammar usage and violations.

**Implementation**:
```markdown
# Grammar Observability

## Metrics to Track
- Messages by schema type
- Schema validation failures by type
- Convention violations by category
- Grammar coverage gaps

## Alerts
- Spike in validation failures
- New undocumented message type
- Convention compliance drop

## Dashboard
- Grammar coverage over time
- Top violation types
- Grammar usage distribution
```

---

## Part VI: Measurement Framework

### Grammar Quality Metrics

| Metric | Definition | Target | Measurement |
|--------|------------|--------|-------------|
| Convention coverage | % of agent behaviors with documented conventions | >95% | Audit behaviors vs. docs |
| Schema coverage | % of message types with schemas | 100% | Compare types to schemas |
| Grammar consistency | % of docs without internal contradictions | 100% | Automated cross-reference |
| Grammar depth | % of conventions enforced by tooling | >80% | Audit enforcement mechanisms |

### Coordination Effectiveness Metrics

| Metric | Definition | Target | Measurement |
|--------|------------|--------|-------------|
| Implicit coordination % | Coordinated actions without explicit messages | >80% | Compare coordination to messages |
| Grammar-based prediction success | Predictions that prove correct | >95% | Track prediction accuracy |
| Convention violation rate | Actions that violate conventions | <2% | Track violations |
| Schema validation success | Messages that pass validation | >99% | Track validation results |

### Grammar Investment ROI Metrics

| Metric | Definition | Target | Measurement |
|--------|------------|--------|-------------|
| Coordination overhead | Messages per coordinated action | Decreasing | Track over time |
| Onboarding time | Time for new agent to coordinate | Decreasing | Track by agent |
| Integration time | Time to integrate new service | Decreasing | Track by integration |

---

## Part VII: Failure Mode Taxonomy

### Documentation Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| Missing convention | Agents handle same case differently | Convention not documented | Document it |
| Stale convention | Agents follow outdated rules | Documentation not updated | Update and version |
| Ambiguous convention | Agents interpret differently | Documentation unclear | Clarify with examples |
| Conflicting conventions | Agents follow contradictory rules | Documentation inconsistent | Reconcile |

### Enforcement Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| Schema bypass | Invalid messages accepted | Validation not enforced | Add enforcement |
| Convention drift | Different agents follow different standards | No governance | Implement governance |
| Silent violation | Convention broken without error | No detection | Add monitoring |

### Depth Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| Lookup latency | Slow coordination when conventions needed | Grammar not internalized | Embed in operating context |
| Edge case gaps | Unusual cases handled incorrectly | Only common cases internalized | Expand internalized coverage |

### Evolution Failures

| Failure | Symptom | Root Cause | Fix |
|---------|---------|------------|-----|
| Breaking change | Agents fail after grammar update | Backward compatibility broken | Follow versioning protocol |
| Compatibility fog | Unclear what versions are compatible | No version documentation | Document compatibility matrix |
| Zombie grammar | Old conventions persist | No deprecation process | Implement deprecation protocol |

---

## Part VIII: Multi-Agent Grammar Architecture

### Grammar Layering for Scale

Large systems need hierarchical grammar:

```
System Grammar (all agents)
├── Domain Grammar (domain agents)
│   ├── Service Grammar (specific service)
│   └── Service Grammar (specific service)
└── Domain Grammar (other domain)
    ├── Service Grammar (specific service)
    └── Service Grammar (specific service)
```

**Layer Rules**:
- System grammar: Universal, stable, minimal
- Domain grammar: Domain-specific, moderately stable
- Service grammar: Service-specific, may evolve faster

**Conflict Resolution**:
- Higher layer wins
- Service grammar cannot contradict domain
- Domain grammar cannot contradict system

### Grammar Governance at Scale

| Scale | Governance Model |
|-------|------------------|
| <10 agents | Single owner, informal review |
| 10-50 agents | Architecture team, PR review |
| 50-200 agents | Federated governance, domain owners |
| 200+ agents | Formal standards body, versioned releases |

### Grammar Distribution

How do agents get grammar?

| Method | Appropriate When |
|--------|------------------|
| **Compiled in** | Core, stable grammar |
| **Configuration** | Environment-specific grammar |
| **Fetched at startup** | Grammar that changes periodically |
| **Real-time updates** | Grammar that changes during operation |

**CLAUDE.md Template**:
```markdown
# Grammar Distribution

## Core Grammar (compiled)
- Fundamental schemas
- Universal conventions
- Never changes during operation

## Configuration Grammar (startup)
- Environment-specific values
- Feature flags
- Current version numbers

## Dynamic Grammar (fetched)
- Latest schema versions
- Current domain rules
- May update during operation

## Update Protocol
1. Grammar service publishes updates
2. Agents subscribe to updates
3. Graceful transition to new grammar
4. Old grammar deprecated after transition period
```

---

## Part IX: Cross-Model Integration

### Related Models

Shared Language/Grammar connects to other models:

**Emergent Coordination**: Grammar is the foundation that enables emergence. Without shared grammar, emergent coordination is impossible.

**Call and Response**: Grammar defines what calls and responses mean. The response patterns (imitation, variation, contrast, extension) are only interpretable given shared grammar.

**OODA Loop**: Grammar accelerates orientation. An agent with complete grammar knowledge orients faster because patterns are immediately recognizable.

### Integration Points

| Model | Grammar's Role |
|-------|---------------|
| Emergent Coordination | Provides the constraint system that enables prediction |
| Call and Response | Defines the semantics of messages |
| OODA Loop | Accelerates orientation through pattern recognition |
| Separation Assurance | Defines boundaries that grammar respects |
| Jidoka | Defines error types and recovery protocols |

### Synthesis

Grammar is **foundational infrastructure** for all other coordination models:

- Without grammar, emergence cannot occur (no prediction basis)
- Without grammar, call-response is noise (no shared semantics)
- Without grammar, OODA is slow (no pattern library)

Investment in grammar is investment in all coordination capabilities.

---

## Part X: Implementation Roadmap

### Phase 1: Grammar Audit (Week 1-2)

- [ ] Inventory all current conventions
- [ ] Identify documented vs. undocumented
- [ ] Identify consistent vs. inconsistent
- [ ] Measure current grammar coverage

### Phase 2: Grammar Foundation (Week 3-4)

- [ ] Document core schemas
- [ ] Document timing conventions
- [ ] Document process patterns
- [ ] Document role boundaries

### Phase 3: Grammar Enforcement (Week 5-6)

- [ ] Implement schema validation
- [ ] Add convention linting
- [ ] Create contract tests
- [ ] Set up violation monitoring

### Phase 4: Grammar Depth (Week 7-8)

- [ ] Embed core grammar in agent context
- [ ] Generate code from schemas
- [ ] Create convention-compliant templates
- [ ] Build tooling that enforces conventions

### Phase 5: Grammar Governance (Ongoing)

- [ ] Establish change review process
- [ ] Implement version management
- [ ] Create audit schedule
- [ ] Monitor and improve continuously

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Agent architecture analysis for shared language/grammar mental model
**Status:** Complete

---

## Sources

### Primary Research Document

- Shared Language/Grammar research document: `/docs/jazz-improvisation/shared-language-grammar.md`

### Related Agent Analysis Documents

- OODA Loop Agent Analysis: `/docs/management/ooda-loop-agent-analysis.md`
- Emergent Coordination Agent Analysis: `/docs/jazz-improvisation/emergent-coordination-agent-analysis.md`
- Call and Response Agent Analysis: `/docs/jazz-improvisation/call-and-response-agent-analysis.md`

### Jazz Grammar Research

- Chord-Scale Theory. *Open Music Theory*.
- Learning Jazz Language by Aural Imitation. *Project MUSE*.
- Minimal Structures: From Jazz Improvisation to Product Innovation. *Sage Journals*.

### Schema and Protocol Standards

- JSON Schema: https://json-schema.org/
- Protocol Buffers: https://protobuf.dev/
- OpenAPI: https://www.openapis.org/
