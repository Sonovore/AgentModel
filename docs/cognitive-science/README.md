# Cognitive Science

Mental models from cognitive psychology, decision science, and human factors applied to AI agent supervision.

## Purpose

Cognitive science studies how minds process information, make decisions, and manage limited resources like attention. Both humans and agents operate under constraints - bounded context, limited attention, cognitive load. Understanding these constraints informs both agent design and human-agent interaction.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Bounded Rationality

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Satisficing | Herbert Simon | "Good enough" decisions under constraints |
| Bounded Rationality | Herbert Simon | Rationality limited by information, time, cognitive capacity |
| Ecological Rationality | Gigerenzer | Heuristics matched to environment |
| Recognition Heuristic | Gigerenzer | Using recognition as decision cue |
| Fast & Frugal Heuristics | Gigerenzer | Simple rules that work |

### Attention & Cognitive Load

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Cognitive Load Theory | Sweller | Intrinsic, extraneous, germane load |
| Working Memory Limits | Miller, Cowan | 7±2 chunks, or 4 items |
| Attention as Resource | Kahneman | Limited pool, must be allocated |
| Selective Attention | Broadbent | Filtering what gets processed |
| Inattentional Blindness | Simons & Chabris | Missing what you're not looking for |

### Decision Making

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Dual Process Theory | Kahneman | System 1 (fast/intuitive) vs System 2 (slow/deliberate) |
| Prospect Theory | Kahneman & Tversky | Loss aversion, reference points |
| Anchoring | Tversky & Kahneman | First information biases subsequent judgment |
| Availability Heuristic | Tversky & Kahneman | Judging by ease of recall |
| Confirmation Bias | Wason | Seeking confirming evidence |

### Mental Models & Representation

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Mental Models | Johnson-Laird | Internal representations of external reality |
| Schemas | Bartlett | Organized knowledge structures |
| Scripts | Schank & Abelson | Expected sequences of events |
| Chunking | Miller | Grouping information for processing |
| Levels of Abstraction | Various | Representing at appropriate detail |

### Expertise & Skill

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Dreyfus Model | Dreyfus brothers | Novice → Advanced Beginner → Competent → Proficient → Expert |
| Deliberate Practice | Ericsson | Structured practice for improvement |
| Automaticity | Psychology | Skills becoming automatic |
| Transfer of Learning | Educational psych | Applying learning to new contexts |
| Expertise Reversal | Kalyuga | What helps novices hurts experts |

### Metacognition

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Metacognition | Flavell | Thinking about thinking |
| Calibration | Judgment research | Confidence matching accuracy |
| Dunning-Kruger Effect | Dunning & Kruger | Unskilled unaware of incompetence |
| Illusion of Explanatory Depth | Rozenblit & Keil | Overestimating understanding |
| Feeling of Knowing | Metacognition | Subjective sense of retrievability |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| Satisficing | Very High | Low | 1 |
| Cognitive Load Theory | Very High | Medium | 1 |
| Dual Process Theory | High | Medium | 1 |
| Working Memory Limits | High | Low | 1 |
| Calibration | Very High | Medium | 2 |
| Mental Models | High | Medium | 2 |
| Dreyfus Model | Medium | Low | 2 |
| Ecological Rationality | Medium | High | 3 |

## Key Questions

1. What's "cognitive load" for an agent? (Context window limits, but also complexity of the problem)
2. Do agents "satisfice"? (Yes - they produce plausible outputs, not optimal ones)
3. What's the agent equivalent of System 1 vs System 2? (Pattern matching vs deliberate reasoning?)
4. How do we measure agent "calibration"? (Confidence vs actual correctness)
5. How does the Dreyfus model apply to agent capability? (Do agents have "expertise levels"?)

## Related Directories

- [Management](../management/) - Recognition-Primed Decision (Klein's work bridges both)
- [Control Theory](../control-theory/) - Information processing limits
- [Safety Engineering](../safety-engineering/) - Human factors
