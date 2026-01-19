# Manager Tools: One-on-Ones

Exploring how the One-on-One concept applies to agent supervision.

## Human Practice

| Aspect | Description |
|--------|-------------|
| **Purpose** | Know your people exceptionally well |
| **Format** | 30 min weekly, 10/10/10 (their agenda / your agenda / future) |
| **Outcome** | Manager understands concerns, blockers, career aspirations, work style |

## Initial Translation: State Management

The obvious mapping is context/state preservation across sessions:
- `context.md` for session continuity
- `state.md` for agent working memory
- Handoff protocols

But this only captures the "your agenda" portion - checking in on task status.

## Deeper Translation: Capability Calibration

**"Know your agent exceptionally well"** means understanding:

| Aspect | Human Version | Agent Equivalent |
|--------|---------------|------------------|
| Strengths | "Sarah is great at debugging" | Success rates by task type |
| Weaknesses | "John struggles with estimates" | Failure patterns by condition |
| Work style | "Prefers detailed specs" | Context requirements for success |
| Growth | "Ready for more responsibility" | Model improvements over time |

### Key Insight: Model Capability Drift

Agent capabilities are **not static**. They change when:
- Model updates (Claude 3.5 → Claude 4)
- Different model tiers (Haiku → Sonnet → Opus)
- Prompt refinements (CLAUDE.md changes)

**Implication:** Must periodically re-assess what agents can do. Assumptions from last month may be wrong.

### Capability Calibration System

```
Capability Dimensions:
├── Task Complexity
│   ├── Single-file changes
│   ├── Multi-file coordinated changes
│   ├── Architectural reasoning
│   └── Edge case handling
├── Context Requirements
│   ├── Minimum context for success
│   ├── Noise tolerance (irrelevant context)
│   └── Context window efficiency
├── Accuracy
│   ├── Syntactic correctness (builds)
│   ├── Semantic correctness (does what's asked)
│   └── Completeness (nothing missing)
├── Judgment Quality
│   ├── Knows when to ask vs. proceed
│   ├── Boundary respect
│   └── Scope discipline
└── Domain-Specific
    └── (Project-specific capabilities)
```

### Calibration Workflow

```
Model Update Detected (or periodic trigger)
    ↓
Run Capability Test Suite
    ↓
Compare to Previous Baseline
    ↓
┌─────────────┬─────────────┬─────────────┐
│ Regression  │ No Change   │ Improvement │
│ Detected    │             │ Detected    │
└─────────────┴─────────────┴─────────────┘
    ↓               ↓               ↓
Demote trust    Log only      Probe further
Alert human                   Consider promotion
```

## Deeper Translation: Observation Surfacing

**"Their agenda"** in human 1:1s = what's on the employee's mind.

Agent equivalent: **Observations outside task scope that matter.**

### Types of Agent "Concerns"

| Type | Example |
|------|---------|
| **Code Quality** | "This module has no error handling" |
| **Inconsistency** | "Two functions do the same thing differently" |
| **Security** | "Saw hardcoded credentials in config.c" |
| **Performance** | "This loop allocates memory every frame" |
| **Documentation** | "Comment says X but code does Y" |
| **Architecture** | "Circular dependency between three modules" |
| **Scope Risk** | "This task touches more files than expected" |

### Observation Surfacing System

**In task output:**
```markdown
## Task Output
(The actual deliverable)

## Observations (Non-blocking)
- [ ] `Core/Src/audio.c:247` - Hardcoded buffer size, should be constant
- [ ] `Core/Src/display/` - Three different screen clear methods
- [ ] General - No null checks in SPI functions
```

**Or separate file:** `.claude/observations.md`

**CLAUDE.md instruction:**
```markdown
## Observation Reporting

While working, note anything that seems off even if not in scope:
- Code quality issues
- Inconsistencies
- Potential bugs unrelated to your task
- Documentation drift
- Architecture concerns

Add to "Observations" section of task output. Don't fix - just report.
```

## Summary: One-on-One → Agent Equivalent

| Human 1:1 Element | Agent System |
|-------------------|--------------|
| "What's on your mind?" | Observation surfacing |
| "How's the project going?" | State files, task status |
| "What do you need from me?" | Blocker reporting |
| Understanding strengths/weaknesses | Capability calibration |
| Career development | N/A (no agent careers) |
| Relationship building | N/A (no relationships) |

## Open Questions

1. **Calibration frequency:** After every model update? Weekly? Only when issues arise?

2. **Calibration scope:**
   - Per agent-type (Implementer vs Reviewer)?
   - Per domain (display code vs audio code)?
   - Per project?

3. **Observation noise:** How to prevent over-reporting? Severity thresholds?

4. **Who runs calibration?** Monitor agent? Human-triggered? Automatic?

## Systems to Build

- [ ] Capability test suite (standardized tasks with known-good outputs)
- [ ] Calibration results tracking (per model, per project)
- [ ] Observation aggregation and triage workflow
- [ ] Model version detection and calibration triggers

## Status

**Phase:** Exploration complete, ready for system design.
