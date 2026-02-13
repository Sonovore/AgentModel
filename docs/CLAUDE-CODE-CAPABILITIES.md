# Claude Code Capabilities Research

**Research Date:** 2026-01-21
**Purpose:** Understand Claude Code's Task tool capabilities, constraints, and patterns for multi-agent experiments

---

## Executive Summary

**Critical findings:**
- **Parallel execution:** Supported - can launch multiple agents in single message
- **Agent types:** 7 specialized agents with different tool access
- **Model selection:** Can specify sonnet/opus/haiku per agent
- **Background execution:** Supported with output file monitoring
- **Resume capability:** Agents can be resumed with full context preserved
- **State management:** File-based (agents can read/write), context passed via prompt
- **Limitations:** No explicit token/time limits documented, agents return single message

**Verdict:** Our test harness design is **FEASIBLE** within Claude Code constraints.

---

## Part 1: Documentation Analysis

### Available Agent Types

From tool descriptions, Claude Code provides 7 specialized agent types:

#### 1. Bash Agent
**Purpose:** Command execution specialist
**Tools:** Bash only
**Use case:** Git operations, command execution, terminal tasks
**Model options:** sonnet (default), opus, haiku

**Characteristics:**
- Single tool (Bash command execution)
- Ideal for file operations, git, system commands
- Can run in background
- Fast iteration (single tool, focused purpose)

#### 2. General-Purpose Agent
**Purpose:** Complex, multi-step tasks requiring multiple tools
**Tools:** All tools available (*)
**Use case:** Research, complex questions, multi-step tasks
**Model options:** sonnet (default), opus, haiku

**Characteristics:**
- Full tool access (Read, Write, Edit, Glob, Grep, Bash, WebFetch, WebSearch, Task)
- Can spawn sub-agents (nested Task calls)
- Most flexible but potentially highest overhead
- Recommended when uncertain which tools needed

#### 3. Statusline-Setup Agent
**Purpose:** Configure Claude Code status line
**Tools:** Read, Edit
**Use case:** Settings configuration
**Model options:** sonnet (default), opus, haiku

**Characteristics:**
- Specialized configuration agent
- Limited tool set (Read, Edit)
- Not relevant for our experiments

#### 4. Explore Agent
**Purpose:** Fast codebase exploration
**Tools:** All except Task, ExitPlanMode, Edit, Write, NotebookEdit
**Use case:** File pattern search, code keyword search, codebase questions
**Model options:** sonnet (default), opus, haiku

**Thoroughness levels:**
- "quick" - Basic searches
- "medium" - Moderate exploration
- "very thorough" - Comprehensive analysis

**Characteristics:**
- Read-only operations (no editing)
- Optimized for search and discovery
- Can't spawn sub-agents (no Task tool)
- Faster than general-purpose for search tasks

#### 5. Plan Agent
**Purpose:** Software architect for implementation planning
**Tools:** All except Task, ExitPlanMode, Edit, Write, NotebookEdit
**Use case:** Design implementation plans, identify critical files
**Model options:** sonnet (default), opus, haiku

**Characteristics:**
- Read-only (no editing/writing)
- Architecture and planning focus
- Can't spawn sub-agents
- Returns step-by-step plans

#### 6. Claude-Code-Guide Agent
**Purpose:** Answer questions about Claude Code, SDK, API
**Tools:** Glob, Grep, Read, WebFetch, WebSearch
**Use case:** Documentation lookup, Claude Code features
**Model options:** sonnet (default), opus, haiku

**Characteristics:**
- Can be resumed (check if already running)
- Documentation-focused
- Limited tool set (search and read)
- Not relevant for our experiments

#### 7. Custom Skill Agents
**Purpose:** User-defined skills from .claude/skills/
**Tools:** Defined per skill
**Use case:** Domain-specific workflows
**Model options:** Defined per skill

**Note:** We can create custom agent types via skills, but not necessary for initial experiments.

### Model Selection

**Available models:**
- **sonnet** (default) - Claude Sonnet 4.5, balanced performance/cost
- **opus** - Claude Opus 4.5, highest capability, most expensive
- **haiku** - Claude Haiku (version not specified), fastest/cheapest

**Recommendation from tool description:**
"Prefer haiku for quick, straightforward tasks to minimize cost and latency."

**Cost implications:**
- Haiku: Lowest cost, fastest
- Sonnet: Medium cost, balanced
- Opus: Highest cost, best for complex reasoning

### Parallel Execution

**From tool description:**
"Launch multiple agents concurrently whenever possible, to maximize performance; to do that, use a single message with multiple tool uses"

**Example pattern:**
```
Send a single message with multiple Task tool calls:
- Task 1: analyze file A
- Task 2: analyze file B
- Task 3: analyze file C
All execute in parallel
```

**Benefits:**
- Maximize parallelism
- Reduce wall-clock time
- Efficient resource utilization

**Constraints:**
- Must be independent tasks (no dependencies between parallel agents)
- All launched in single message (can't add more mid-execution)

### Background Execution

**From tool description:**
"You can optionally run agents in the background using the run_in_background parameter. When an agent runs in the background, the tool result will include an output_file path. To check on the agent's progress or retrieve its results, use the Read tool to read the output file, or use Bash with `tail` to see recent output. You can continue working while background agents run."

**Key capabilities:**
- Non-blocking execution
- Output written to file
- Can monitor progress via Read or tail
- Continue working while agent runs

**Use case for experiments:**
- Long-running agents (exploratory search, large file processing)
- Want to monitor multiple agents simultaneously
- Non-critical path operations

### Resume Capability

**From tool description:**
"Agents can be resumed using the `resume` parameter by passing the agent ID from a previous invocation. When resumed, the agent continues with its full previous context preserved."

**Key capabilities:**
- Full context preserved
- Agent ID from previous run
- Continue where left off
- No need to repeat work

**Use case for experiments:**
- Iterative refinement tasks
- Error recovery (resume after fixing issue)
- Incremental progress on long tasks

### State Management

**Context passing:**
"Agents with 'access to current context' can see the full conversation history before the tool call. When using these agents, you can write concise prompts that reference earlier context (e.g., 'investigate the error discussed above') instead of repeating information. The agent will receive all prior messages and understand the context."

**File-based state:**
- Agents can Read files to get state
- Agents can Write/Edit files to persist state
- Shared file system across agents
- Git-friendly coordination

**Message-based state:**
- Agent returns single message
- Can include structured data in message
- Parent agent receives result
- Can pass to next agent

### Agent Communication Patterns

**Parent-Child (Task spawning):**
- Parent launches child via Task tool
- Child executes and returns single message
- Parent receives result, continues
- Hierarchical structure

**Sibling (Parallel agents):**
- Parent launches multiple children in parallel
- Each executes independently
- All return to parent
- No direct sibling communication

**Sequential (Pipeline):**
- Agent 1 executes, returns result
- Parent processes result
- Parent launches Agent 2 with context from Agent 1
- Chain continues

**File-based coordination:**
- Agent 1 writes to file
- Agent 2 reads from file
- Asynchronous, decoupled
- Enables complex coordination patterns

### Constraints and Limitations

**From documentation analysis:**

1. **No explicit token limits documented**
   - Tool description mentions agents can be "complex" and "multi-step"
   - No hard limit specified
   - Likely inherits Claude API limits (200K tokens for Claude 4.5)

2. **No explicit time limits documented**
   - Background agents can run while parent continues
   - No timeout mentioned
   - Likely system-level limits exist

3. **Single message return**
   - "When the agent is done, it will return a single message back to you"
   - No streaming from child agents
   - Must batch results

4. **No explicit parallel agent limit**
   - Documentation says "launch multiple agents concurrently"
   - No maximum number specified
   - Practical limit likely exists (system resources)

5. **Agent isolation**
   - Agents don't share memory/state directly
   - Must coordinate via files or parent mediation
   - Can't directly message each other

---

## Part 2: Experimental Testing

### Experiment 1: Parallel Agent Spawning

**Goal:** Test launching 2, 5, 10 agents in parallel and measure behavior

**Test code pattern:**
```python
# Single message with N Task tool calls
# Each agent: simple task (analyze a file, compute sum, etc.)
# Measure: completion time, success rate
```

**Expected behavior:**
- All agents launch simultaneously
- Parent waits for all to complete
- Results returned together

**Actual results:** (TO BE RUN)

### Experiment 2: Background Agent Monitoring

**Goal:** Test background agent with progress monitoring

**Test code pattern:**
```python
# Launch background agent with run_in_background=True
# Receive output_file path
# Poll file with Read or tail
# Continue working while agent runs
```

**Expected behavior:**
- Agent launches in background
- Output file path provided immediately
- Can monitor progress incrementally
- Parent continues execution

**Actual results:** (TO BE RUN)

### Experiment 3: State Passing Patterns

**Goal:** Test different state management approaches

**Test patterns:**
1. **File-based:** Agent writes JSON, next agent reads
2. **Parameter-based:** Pass data in prompt to next agent
3. **Mixed:** Some via file, some via prompt

**Expected behavior:**
- File-based: Most flexible, persistent
- Parameter-based: Simpler, ephemeral
- Mixed: Best of both

**Actual results:** (TO BE RUN)

### Experiment 4: Agent Resume

**Goal:** Test resuming agents from previous runs

**Test code pattern:**
```python
# Launch agent, save agent_id
# Agent performs partial work
# Resume with same agent_id
# Verify context preserved
```

**Expected behavior:**
- Full context preserved
- Continues from previous state
- No repeated work

**Actual results:** (TO BE RUN)

### Experiment 5: Model Selection Impact

**Goal:** Compare opus/sonnet/haiku for same task

**Test code pattern:**
```python
# Same task with model="opus"
# Same task with model="sonnet"
# Same task with model="haiku"
# Measure: quality, latency, cost (estimated)
```

**Expected behavior:**
- Haiku: Fastest, lowest quality
- Sonnet: Balanced
- Opus: Slowest, highest quality

**Actual results:** (TO BE RUN)

---

## Part 3: Codebase Examples Review

### Example 1: Current Session Usage

**Search for Task tool usage in this session:**

From conversation history, we see Task tool has been mentioned but not yet used in this session. Previous sessions likely have examples.

### Example 2: Skills Directory

**Check .claude-shared/skills/ for agent patterns:**

We know skills exist (deep-research-mm, agents:*, etc.) but need to examine their implementation for Task tool usage patterns.

### Example 3: Startup Scripts

**Check .claude/scripts/startup.sh for agent orchestration:**

Startup script may spawn agents for initialization tasks.

---

## Part 4: Practical Recommendations for Test Harness

Based on documentation analysis (experimental results pending):

### Agent Type Selection for Tasks

**Task S1 (Parallel Map-Reduce):**
- Use: **General-purpose agents** (need flexibility)
- Model: **Haiku** (simple file processing)
- Pattern: Launch 5-10 agents in parallel
- Coordination: Parent aggregates results

**Task S2 (Sequential Pipeline):**
- Use: **General-purpose agents** (need Read/Write/Bash)
- Model: **Sonnet** (moderate complexity)
- Pattern: Sequential task spawning
- Coordination: File-based state passing

**Task S3 (Orchestrator-Worker):**
- Use: **General-purpose** for orchestrator, **specialized** for workers
- Model: **Sonnet** for orchestrator, **Haiku** for workers
- Pattern: Hub-and-spoke via parent mediation
- Coordination: Parent routes messages

**Task W1 (Multi-File Refactoring):**
- Use: **General-purpose agents** (need Edit capabilities)
- Model: **Opus** (complex reasoning required)
- Pattern: Single agent or sequential coordination
- Coordination: Context via prompts + file reads

**Task W2 (High-Coordination Multi-Agent):**
- Use: **General-purpose agents** (flexible tool needs)
- Model: **Sonnet** (balanced)
- Pattern: Multiple agents with parent mediation
- Coordination: File-based + parent message routing

### Coordination Pattern Recommendations

**Pattern 1: Hub-and-Spoke (Parent Mediation)**
```
Parent Agent
├─> Child Agent 1 (execute task A)
├─> Child Agent 2 (execute task B)
└─> Child Agent 3 (execute task C)
Parent aggregates results
```

**Implementation:**
- Parent launches children in parallel
- Children return results to parent
- Parent mediates all communication
- No direct child-to-child communication

**Best for:** Tasks requiring coordination, aggregation, decision-making

**Pattern 2: Sequential Pipeline**
```
Parent
├─> Agent 1 (fetch data) → write to file1.json
├─> Agent 2 (transform) → read file1.json, write file2.json
├─> Agent 3 (validate) → read file2.json, write file3.json
└─> Agent 4 (store) → read file3.json, write to DB
```

**Implementation:**
- Sequential Task calls
- State passed via files
- Each agent reads previous output
- Parent orchestrates sequence

**Best for:** Clear dependencies, ETL workflows, pipelines

**Pattern 3: Parallel-Then-Aggregate**
```
Parent
├─> [Agent 1, Agent 2, Agent 3, Agent 4, Agent 5] parallel
└─> Aggregate results
```

**Implementation:**
- Single message with N Task calls
- All execute in parallel
- Parent waits for all
- Parent processes all results

**Best for:** Embarrassingly parallel tasks, map-reduce

**Pattern 4: Background + Monitor**
```
Parent
├─> Background Agent (long task) → output_file
└─> Monitor loop (Read output_file periodically)
```

**Implementation:**
- Launch with run_in_background=True
- Receive output_file path
- Poll file for progress
- Continue other work

**Best for:** Long-running tasks, exploratory search, monitoring

### Model Selection Strategy

**Use Haiku when:**
- Simple, well-defined tasks
- High volume (cost matters)
- Speed critical (map-reduce workers)
- Minimal reasoning required

**Use Sonnet when:**
- Moderate complexity
- Balanced cost/performance needed
- Most coordination/orchestration
- Default choice

**Use Opus when:**
- Complex reasoning required
- Quality critical (refactoring, design)
- Low volume (few calls)
- Benchmark/baseline establishment

### State Management Strategy

**File-based state (prefer for):**
- Persistent state across agents
- Complex data structures
- Asynchronous coordination
- Debugging (can inspect files)

**Parameter-based state (prefer for):**
- Simple scalar values
- Synchronous pipelines
- Ephemeral state
- Quick prototypes

**Mixed approach (prefer for):**
- Large data in files (JSON results)
- Metadata in prompts (task instructions)
- Best of both worlds

### Error Handling Recommendations

**Detect errors via:**
- Return message analysis (agent reports errors)
- File system checks (expected files missing)
- Schema validation (output malformed)
- Timeout detection (background agent stalled)

**Recover from errors via:**
- Retry with same agent (transient failures)
- Resume agent (continue from checkpoint)
- Reassign to different agent (capability mismatch)
- Escalate to parent (unrecoverable)

---

## Part 5: Test Harness Architecture Implications

### Feasibility Assessment

**✓ Parallel execution:** Claude Code supports it natively
**✓ Background agents:** Can run long tasks without blocking
**✓ State management:** File-based works for our conventions
**✓ Model selection:** Can optimize cost with haiku/sonnet/opus
**✓ Error recovery:** Resume capability enables retry patterns
**✓ Scalability:** Can test 2, 5, 10, 20 agents (practical limits TBD)

**Verdict: Test harness design is FEASIBLE**

### Architecture Refinements

Based on capabilities, our test harness should:

1. **Use parent agent as orchestrator**
   - Parent launches worker agents via Task tool
   - Workers return results via single message
   - Parent mediates all coordination

2. **State management via files**
   - Write messages to JSON files
   - Agents read/write shared file system
   - Matches our convention-based coordination

3. **Model selection per role**
   - Haiku for simple workers
   - Sonnet for orchestrator
   - Opus for complex reasoning tasks

4. **Background for long tasks**
   - Use run_in_background for exploratory tasks
   - Monitor via output files
   - Don't block main thread

5. **Metrics via instrumentation**
   - Log Task calls (parent knows all spawns)
   - Log file operations (track messages)
   - Aggregate timing data
   - Count tokens via return messages

### Constraints to Design Around

1. **No direct agent-to-agent communication**
   - Must route through parent (hub-and-spoke enforced)
   - Matches our coordination model!

2. **Single message return per agent**
   - Can't stream progress
   - Must batch results
   - Implies agents should complete atomic tasks

3. **File-based coordination only**
   - No shared memory
   - No message queues
   - Files are coordination medium

4. **Unknown hard limits**
   - Will discover via experiments
   - Start conservative (5 agents)
   - Scale up carefully
   - Monitor for failures

---

## Part 6: Experimental Test Plan

### Test Suite to Run

**Test 1: Basic parallel (5 agents)**
- Task: Each agent analyzes one file
- Measure: Wall time, success rate
- Expected: ~same as single agent (parallelism works)

**Test 2: Scaling parallel (10, 20 agents)**
- Task: Same as Test 1, more agents
- Measure: Wall time, success rate, degradation
- Expected: Diminishing returns, find practical limit

**Test 3: Background execution**
- Task: Long-running search (background)
- Monitor: Read output file every 5 seconds
- Measure: Progress visibility, completion detection

**Test 4: Sequential pipeline (4 agents)**
- Task: Fetch → Transform → Validate → Store
- State: Files passed between agents
- Measure: Total time, coordination overhead

**Test 5: Model comparison (same task × 3 models)**
- Task: Analyze complex file
- Models: Haiku, Sonnet, Opus
- Measure: Quality, latency, estimated cost

**Test 6: Error recovery (resume)**
- Task: Agent fails mid-execution
- Recovery: Resume with agent ID
- Measure: Context preservation, recovery success

### Success Criteria

**After experimental tests, we can answer:**
1. Maximum practical parallel agents? (Target: 10+)
2. Background monitoring lag? (Target: <10s)
3. File-based coordination overhead? (Target: <10% overhead)
4. Model performance differences? (Validate haiku for simple tasks)
5. Error recovery success rate? (Target: >80%)
6. Overall: Is architecture viable? (Yes/No)

---

## Part 7: Key Findings Summary

### What We Learned from Documentation

1. **7 agent types available** - most relevant: general-purpose, bash, explore
2. **Model selection supported** - opus/sonnet/haiku per agent
3. **Parallel execution native** - single message, multiple Task calls
4. **Background execution supported** - run_in_background parameter
5. **Resume capability exists** - full context preserved
6. **File-based state natural** - matches our conventions
7. **Hub-and-spoke enforced** - no direct agent communication (good!)
8. **Single message return** - atomic task completion

### Critical Constraints

1. **Parent mediates all coordination** (enforced by architecture)
2. **File-based state only** (no shared memory)
3. **Single message return** (no streaming)
4. **Unknown hard limits** (must discover experimentally)

### Design Implications

1. **Our hub-and-spoke model maps perfectly to Claude Code**
2. **File-based conventions work natively**
3. **Can implement all task types (S1-W4)**
4. **Can test all coordination models**
5. **Cost can be optimized via model selection**

### Experimental Validation Needed

1. ✓ Parallel agent limits (how many?)
2. ✓ Background monitoring patterns (how responsive?)
3. ✓ State passing overhead (how expensive?)
4. ✓ Model performance differences (haiku vs sonnet vs opus)
5. ✓ Error recovery robustness (resume reliability)

---

## Conclusion

**Claude Code provides sufficient capabilities for our test harness.**

**Key enablers:**
- Native parallel execution
- File-based coordination
- Model flexibility
- Background execution
- Resume capability

**Key constraints:**
- Hub-and-spoke enforced (this is actually good!)
- File-based only (matches our design)
- Single message return (design for atomic tasks)
- Unknown limits (discover experimentally)

**Next steps:**
1. Run experimental test suite (6 tests above)
2. Document actual performance characteristics
3. Refine architecture based on constraints
4. Proceed with test harness implementation

**Status: READY TO PROCEED** (pending experimental validation)
