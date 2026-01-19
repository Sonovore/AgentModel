# Two-Phase Commit (2PC) and Three-Phase Commit for Agent Coordination

Exploring how distributed transaction protocols apply to multi-agent AI coordination when actions must be atomic.

## Background

| Aspect | Description |
|--------|-------------|
| **Origin** | Jim Gray, "Notes on Data Base Operating Systems" (1978) |
| **Domain** | Distributed databases, transaction processing |
| **Core Problem** | How do multiple independent nodes agree to commit or abort a transaction atomically? |
| **Key Insight** | Consensus requires phases: first get agreement, then execute. You cannot do both simultaneously. |
| **Why It's Hard** | Nodes can fail at any point, messages can be lost, and there's no global clock |

The distributed transaction problem is deceptively simple to state: multiple nodes must either all commit a change or all abort it. No partial commits. If a bank transfer moves money from Account A (on Node 1) to Account B (on Node 2), both changes must happen or neither must happen. If Node 1 debits and Node 2 crashes before crediting, money vanishes.

This is the **atomicity** guarantee - the "A" in ACID. Achieving atomicity on a single machine is straightforward (write-ahead logging). Achieving atomicity across multiple machines that can fail independently requires a protocol. That protocol is Two-Phase Commit.

## Why "Just Retry" Doesn't Work

Before understanding 2PC, understand why naive approaches fail.

### The Naive Approach

```
Coordinator:
  1. Tell Node A: "Debit $100"
  2. Tell Node B: "Credit $100"
  3. Done!

What could go wrong:
  - Node A succeeds, Node B is unreachable → money debited but not credited
  - Node A succeeds, message to Node B lost → same problem
  - Node B fails mid-operation → partial state
  - Coordinator crashes between steps 1 and 2 → unknown state
```

**Why retrying doesn't help:**
- If Node B is down, retrying won't bring it up
- If Node A already committed, you can't uncommit
- If you don't know whether a message was received, retrying might double-execute

**The fundamental issue:** Once you tell a node to commit, you can't take it back. But you don't know if the other node will commit until you ask. And asking takes time, during which failures can happen.

### The Two Generals Problem

This is the theoretical foundation. Two generals on opposite sides of a valley need to coordinate an attack. Messages sent through the valley might be intercepted.

```
General A → "Attack at dawn" → General B
         ← "Acknowledged"    ←
         → "Confirmed ack"   →
         ← "Confirmed conf"  ←
         → ...ad infinitum...
```

**The problem:** Neither general can ever be *certain* the other received the message. Any finite number of acknowledgments still leaves uncertainty. If General A attacks alone, their army is destroyed. If both attack, they win.

**Theorem:** There is no protocol that guarantees agreement with unreliable communication.

**What this means for 2PC:** We cannot guarantee perfect atomicity in the presence of arbitrary failures. We can only make trade-offs about which failure modes we handle and which we accept.

## Two-Phase Commit Protocol

### The Core Mechanism

2PC separates the decision to commit from the act of committing.

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PHASE 1: VOTING/PREPARE                       │
│                                                                      │
│   Coordinator → "Can you commit?" → Participant A                    │
│               → "Can you commit?" → Participant B                    │
│               → "Can you commit?" → Participant C                    │
│                                                                      │
│   Participants do all the work EXCEPT final commit:                  │
│   - Acquire locks                                                    │
│   - Write to temporary storage                                       │
│   - Validate constraints                                             │
│   - Write to log: "PREPARED for transaction X"                       │
│                                                                      │
│   Participant A → "YES" (vote to commit)                             │
│   Participant B → "YES"                                              │
│   Participant C → "YES"                                              │
│                                                                      │
│   OR any participant → "NO" (vote to abort)                          │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        PHASE 2: COMMIT/ABORT                         │
│                                                                      │
│   IF all voted YES:                                                  │
│     Coordinator logs: "COMMIT transaction X"                         │
│     Coordinator → "COMMIT" → All participants                        │
│     Participants make changes permanent, release locks               │
│                                                                      │
│   IF any voted NO (or timeout):                                      │
│     Coordinator logs: "ABORT transaction X"                          │
│     Coordinator → "ABORT" → All participants                         │
│     Participants discard changes, release locks                      │
└─────────────────────────────────────────────────────────────────────┘
```

### The "Promise" Semantics of a YES Vote

This is crucial and often glossed over. When a participant votes YES:

| What YES Means | Implication |
|----------------|-------------|
| "I am ABLE to commit" | All preconditions satisfied |
| "I WILL commit if told" | This is a binding promise |
| "I have logged PREPARED" | Crash recovery can honor the promise |
| "I am holding locks" | No one else can interfere |
| "I await your decision" | Control transfers to coordinator |

**A YES vote is irrevocable.** Once a participant votes YES, it must wait for the coordinator's decision. It cannot unilaterally abort. It has surrendered its autonomy on this transaction.

**Why this is necessary:** If participants could change their vote, the coordinator's decision could become invalid between making it and delivering it.

### The Coordinator's Role

The coordinator is the single decision point:

| Responsibility | Why It Matters |
|----------------|----------------|
| Collect all votes | Must hear from everyone |
| Make THE decision | Only one entity decides |
| Log the decision | Crash recovery depends on this |
| Distribute the decision | Participants need to know |
| Handle timeouts | Decide what "no response" means |

**The coordinator IS the transaction.** Without the coordinator, participants don't know the outcome. This creates the central vulnerability of 2PC.

## Failure Modes and Recovery

This is where 2PC reveals its complexity. Different failures require different handling.

### Failure Mode 1: Participant Fails Before Voting

```
Timeline:
  1. Coordinator sends PREPARE to A, B, C
  2. A responds YES
  3. B crashes (no response)
  4. C responds YES
  5. Coordinator times out waiting for B
  6. Decision: ABORT (safety first)
```

**Handling:** Coordinator aborts the transaction. No harm done - nobody committed.

**Recovery:** When B restarts, it has no record of this transaction. Coordinator can tell it "ABORT" or just let it time out.

### Failure Mode 2: Participant Fails After Voting YES

```
Timeline:
  1. Coordinator sends PREPARE to A, B, C
  2. A responds YES
  3. B responds YES
  4. C responds YES
  5. Coordinator decides COMMIT
  6. Coordinator sends COMMIT to A, B, C
  7. A commits
  8. B crashes before receiving COMMIT
  9. C commits
```

**The critical insight:** B voted YES, which means B logged "PREPARED for transaction X" before voting. When B restarts:

```
B's Recovery:
  1. Read log, find "PREPARED for X"
  2. I voted YES but don't see a decision
  3. Ask coordinator: "What happened to X?"
  4. Coordinator: "COMMIT"
  5. B commits
```

**This is why the PREPARED log entry exists.** It survives crashes. A participant that voted YES must be able to honor that vote after restart.

### Failure Mode 3: Coordinator Fails During Phase 1

```
Timeline:
  1. Coordinator sends PREPARE to A, B
  2. Coordinator crashes before sending PREPARE to C
  3. A responded YES (waiting)
  4. B responded YES (waiting)
  5. C never heard of this transaction
```

**The problem:** A and B are stuck. They voted YES. They're holding locks. They cannot unilaterally abort (they promised). They cannot commit (no decision received).

**Recovery options:**

1. **Wait for coordinator recovery:** Coordinator restarts, sees incomplete transaction, sends ABORT to everyone.

2. **Cooperative termination protocol:** Participants talk to each other:
   - A asks B: "Did you vote? What did you vote?"
   - B says: "I voted YES"
   - A asks C: "Did you vote?"
   - C says: "What transaction?"
   - A and B conclude: "C never got PREPARE, so coordinator couldn't have decided COMMIT. Safe to abort."

### Failure Mode 4: Coordinator Fails During Phase 2 (THE BLOCKING PROBLEM)

```
Timeline:
  1. Coordinator sends PREPARE to A, B, C
  2. All vote YES
  3. Coordinator decides COMMIT
  4. Coordinator logs COMMIT
  5. Coordinator sends COMMIT to A
  6. Coordinator crashes before sending to B, C
  7. A commits
  8. B is waiting (voted YES)
  9. C is waiting (voted YES)
```

**This is the worst case.** B and C are blocked:

- They cannot abort (they promised to commit if told)
- They cannot commit (they haven't been told)
- They cannot ask each other (neither knows the decision)
- They cannot ask A (A might have committed or not - they don't know)
- They MUST wait for coordinator recovery

**The blocking problem is fundamental to 2PC.** There exists a failure window where participants have voted YES but the decision hasn't propagated, and they cannot make progress without the coordinator.

### The BLOCKING Problem Visualized

```
                            Participant State Space

                 UNCERTAIN                    CERTAIN
              (can abort or commit)      (committed to one path)
                    │                            │
                    │                            │
    Before vote:    │ ────────────────────────── │
    Can abort       │                            │
                    │                            │
                    │         VOTED YES          │
    After vote:     │ ──────────────────────▶    │
    Must wait       │                            │
                    │                            │
                    │                            │ COMMITTED
    After decision: │ ──────────────────────────▶│ or ABORTED
                    │                            │ (resolved)
                    │                            │

    THE BLOCKING WINDOW: Between "VOTED YES" and "RECEIVED DECISION"

    In this window, the participant:
    - Cannot abort (promised not to)
    - Cannot commit (hasn't been told)
    - Cannot make progress alone
    - MUST wait for coordinator
```

### Recovery Mechanisms

#### Write-Ahead Logging (WAL)

Every critical state change is logged BEFORE the action:

| Action | Log Entry First |
|--------|-----------------|
| Vote YES | Log "PREPARED X" then send vote |
| Decide COMMIT | Log "COMMIT X" then send decision |
| Decide ABORT | Log "ABORT X" then send decision |

**Recovery algorithm:**
1. Read log
2. For each transaction:
   - If COMMIT logged: ensure committed
   - If ABORT logged: ensure aborted
   - If PREPARED logged but no decision: ask coordinator
   - If nothing logged: abort (safe because didn't vote)

#### Presumed Abort

An optimization: if no decision is logged, presume ABORT.

**Rationale:** Aborts are more common than commits. If we presume abort when uncertain, we:
- Don't need to log ABORT decisions
- Don't need to acknowledge ABORT messages
- Save disk writes and messages

**Trade-off:** Must always log COMMIT. Can never lose a COMMIT decision.

#### Timeout and Heartbeat

Participants use timeouts to detect coordinator failure:

```
Participant:
  - Set timeout when voting YES
  - If timeout expires and no decision:
    - Try to contact coordinator
    - Try cooperative termination with other participants
    - If still stuck: human intervention
```

## Three-Phase Commit (3PC)

3PC attempts to solve the blocking problem by adding a phase.

### The Additional Phase

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PHASE 1: VOTING/PREPARE                       │
│                                                                      │
│   Same as 2PC:                                                        │
│   Coordinator → "Can you commit?" → Participants                      │
│   Participants → YES/NO → Coordinator                                 │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PHASE 2: PRE-COMMIT (NEW!)                        │
│                                                                      │
│   IF all voted YES:                                                  │
│     Coordinator → "PRE-COMMIT" → All participants                    │
│     Participants → "ACK" → Coordinator                               │
│                                                                      │
│   Now everyone KNOWS the decision is COMMIT                          │
│   (Coordinator wouldn't send PRE-COMMIT unless all voted YES)        │
│                                                                      │
│   IF any voted NO:                                                   │
│     Coordinator → "ABORT" → All participants                         │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        PHASE 3: COMMIT                               │
│                                                                      │
│   IF all ACKed PRE-COMMIT:                                           │
│     Coordinator → "COMMIT" → All participants                        │
│     Participants commit and release locks                            │
└─────────────────────────────────────────────────────────────────────┘
```

### How 3PC Addresses Blocking

The key insight: in 3PC, if a participant times out, it can make a safe decision based on its state.

| Participant State at Timeout | Safe Action | Reasoning |
|------------------------------|-------------|-----------|
| UNCERTAIN (not voted) | ABORT | Normal 2PC behavior |
| PREPARED (voted YES) | ABORT | Haven't received PRE-COMMIT, so coordinator either crashed or aborted |
| PRE-COMMITTED | COMMIT | Know coordinator decided commit (else wouldn't have sent PRE-COMMIT) |

**The difference:** In 2PC, a participant in PREPARED state cannot safely abort (coordinator might have decided COMMIT). In 3PC, the PRE-COMMIT phase ensures that if you're still in PREPARED when you timeout, the decision was definitely not COMMIT.

### Why 3PC Is Rarely Used

Despite solving blocking, 3PC has problems:

#### 1. Network Partitions

```
Scenario:
  Participants: A, B, C, D, E
  All vote YES
  Coordinator sends PRE-COMMIT to A, B, C
  Network partition: {A, B, C} | {D, E}
  Coordinator is in partition with D, E

  Partition 1 (A, B, C):
    - A, B, C received PRE-COMMIT
    - They timeout waiting for COMMIT
    - Per 3PC rules: they COMMIT

  Partition 2 (D, E):
    - D, E never got PRE-COMMIT
    - They timeout waiting for PRE-COMMIT
    - Per 3PC rules: they ABORT

  Result: A, B, C committed; D, E aborted
  INCONSISTENCY!
```

**3PC assumes fail-stop failures, not network partitions.** If nodes can be isolated rather than crashed, 3PC breaks.

#### 2. More Messages

| Protocol | Messages (n participants) |
|----------|--------------------------|
| 2PC | 4n (prepare, vote, decision, ack) |
| 3PC | 6n (prepare, vote, pre-commit, ack, commit, ack) |

50% more messages means higher latency and more failure opportunities.

#### 3. Longer Lock Duration

More phases means locks are held longer, reducing throughput.

#### 4. Complexity

More states to manage, more edge cases, harder to implement correctly.

### When 3PC Might Apply

| Scenario | 2PC or 3PC? |
|----------|-------------|
| Network partitions possible | 2PC (3PC doesn't help) |
| Need non-blocking recovery | 3PC (if no partitions) |
| High availability required | Neither - use alternatives |
| Latency critical | 2PC (fewer round trips) |
| Node crashes likely but network reliable | 3PC |

**In practice:** Most systems use 2PC and accept the blocking window, or avoid distributed transactions entirely.

## Alternatives to 2PC

Given 2PC's limitations, what else?

### Saga Pattern

Break a transaction into a sequence of local transactions with compensating actions.

```
2PC Approach:
  All-or-nothing: Debit A AND Credit B atomically

Saga Approach:
  1. Debit A (local commit)
  2. Credit B (local commit)

  If step 2 fails:
  3. Compensate: Credit A (undo step 1)
```

| Aspect | 2PC | Saga |
|--------|-----|------|
| Atomicity | All-or-nothing | Eventually consistent |
| Isolation | Full (locks held) | None (intermediate states visible) |
| Latency | Higher (phases) | Lower (no coordination) |
| Availability | Lower (coordinator required) | Higher (no single point) |
| Complexity | Protocol complexity | Compensation logic complexity |

**Saga trade-off:** You see intermediate states. After step 1, the money is debited but not credited. Compensation fixes it eventually, but the inconsistent state was visible.

### Eventual Consistency

Don't require immediate consistency across nodes.

```
Eventually Consistent:
  1. Write to Node A
  2. Asynchronously replicate to Node B
  3. Eventually (seconds? minutes?) B has the data

  During the window: A and B disagree
```

| When Acceptable | When Not Acceptable |
|-----------------|---------------------|
| Social media posts | Bank transfers |
| Shopping cart | Inventory reservation |
| Read replicas | Primary data modification |
| Analytics data | Billing records |

### Compensating Transactions

Like Saga, but more general. Every forward action has a defined backward action.

| Forward Action | Compensating Action |
|----------------|---------------------|
| Debit account | Credit account |
| Reserve inventory | Release reservation |
| Create order | Cancel order |
| Send email | Send "please disregard" email |
| Deploy code | Rollback deployment |

**Some actions are not compensable:**
- Sending a text message (can't unsend)
- Physical manufacturing (can't unmake a widget)
- Time-sensitive actions (concert already happened)

## Mapping to AI Agent Systems

Now the application to the actual problem domain: multi-agent AI coordination.

### When Do Agents Need Atomic Coordination?

| Scenario | Why Atomicity Matters |
|----------|----------------------|
| Multi-file code changes | All files must be consistent |
| Cross-system API calls | Both systems need consistent state |
| Multi-agent task handoff | Can't have task in limbo or duplicated |
| Coordinated external actions | Can't email customer twice or zero times |
| State machine transitions | System state must be valid |

**Example:** Three agents are modifying an API - one changes the server, one changes the client, one updates documentation. Either all changes happen or none do.

### What's the "Prepare" Phase for Agents?

In 2PC, PREPARE means "do everything except final commit." For agents:

| 2PC Prepare | Agent Equivalent |
|-------------|------------------|
| Acquire locks | Reserve resources, claim tasks |
| Write to temp storage | Stage changes, create drafts |
| Validate constraints | Verify feasibility, check dependencies |
| Log PREPARED | Record commitment to complete |

**Agent PREPARE phase:**
1. Agent receives task
2. Agent analyzes feasibility
3. Agent prepares (but doesn't execute) the solution
4. Agent reports: "I CAN do this, and I WILL if told to proceed"

### What's "Voting YES" for Agents?

A YES vote in 2PC is a binding promise. For agents:

| 2PC YES Vote | Agent Equivalent |
|--------------|------------------|
| "I can commit" | "I can complete this task" |
| "I will commit if told" | "I commit to completing if you say GO" |
| "I've logged PREPARED" | "I've recorded my plan/preparation" |
| "I'm holding locks" | "I've reserved what I need" |

**The binding nature:** When an agent votes YES, it's saying: "I have everything I need, I've verified I can do this, and I will do it if you tell me to proceed." It cannot later say "actually, I can't."

**This is stronger than typical agent behavior.** Agents usually operate opportunistically - try, and if it fails, report failure. Voting YES requires upfront verification.

### What If an Agent Fails After Voting YES?

This is the blocking problem for agents.

```
Scenario:
  Coordinator: "Agent A, Agent B, Agent C - can you each make your changes?"
  Agent A: "YES" (prepared, holding locks)
  Agent B: "YES" (prepared, holding locks)
  Agent C: "YES" (prepared, holding locks)
  Coordinator: "COMMIT"
  Agent A: *commits*
  Agent B: *crashes/hangs/context overflow*
  Agent C: *commits*

  Result: A and C committed, B didn't
  System in inconsistent state
```

**Recovery options for agents:**

| Option | Mechanism | Trade-off |
|--------|-----------|-----------|
| Agent restart | B restarts, reads its log, completes | Requires durable agent state |
| Compensating actions | Undo A and C's changes | Must be possible to undo |
| Human intervention | Human completes B's task | Defeats automation |
| Timeout and abort | If B doesn't complete, abort all | Requires A and C to be undoable |

### What's the "Coordinator" in Multi-Agent Systems?

| Coordinator Role | Agent System Equivalent |
|------------------|------------------------|
| Collect votes | Ask all agents "can you do your part?" |
| Make THE decision | Single point decides GO/NO-GO |
| Distribute decision | Tell all agents the decision |
| Handle failures | Decide what to do when an agent fails |
| Log decision | Record for recovery |

**Options for coordinator:**
1. **Orchestrator agent:** A special agent whose job is coordination
2. **Human supervisor:** Human makes GO/NO-GO decision
3. **Consensus among agents:** Agents vote and agree (more complex)
4. **First agent in chain:** Initiating agent coordinates

**The coordinator is a single point of failure.** If using 2PC semantics, coordinator failure blocks the entire transaction.

### Should Agent Systems Use 2PC?

| Consider 2PC When | Consider Alternatives When |
|-------------------|---------------------------|
| Actions are truly irreversible | Actions can be compensated |
| Inconsistency is catastrophic | Eventual consistency is acceptable |
| Few agents involved | Many agents (scaling issues) |
| Reliable agent execution | Agents frequently fail |
| Low latency not critical | Speed matters |

**The honest answer:** Most agent systems should NOT use 2PC. The overhead is high, the blocking problem is real, and most agent actions can be compensated or retried.

### Saga Pattern for Agent Coordination

This is often more appropriate:

```
Multi-Agent Saga:

Agent A: Execute step 1 → Success → Notify coordinator
  │
  ▼
Agent B: Execute step 2 → Success → Notify coordinator
  │
  ▼
Agent C: Execute step 3 → FAILURE → Notify coordinator
  │
  ▼
Coordinator: Initiate compensation
  │
  ├── Agent B: Execute compensation for step 2
  │
  └── Agent A: Execute compensation for step 1

Result: System back to initial state (eventually)
```

**Agent Saga requirements:**
1. Each agent's action must be compensable
2. Compensation must be defined upfront
3. Intermediate states are visible
4. Coordinator tracks progress

### Eventual Consistency for Agent Coordination

Some agent coordination doesn't need atomicity:

| Example | Why Eventual Consistency Works |
|---------|-------------------------------|
| Multiple agents writing documentation | Sections can be inconsistent temporarily |
| Parallel research tasks | Results merge at end |
| Independent code modules | Integration happens later |
| Distributed data collection | Aggregation reconciles |

**When eventual consistency fails:**
- Single document that must be internally consistent
- API changes that must be deployed together
- State transitions with invariants

## Practical Agent Coordination Patterns

### Pattern 1: Two-Phase Task Execution

```
Phase 1: Verification
  Coordinator → "Can you complete this task?" → Agent A
  Coordinator → "Can you complete this task?" → Agent B

  Agent A: [Analyzes task, checks resources, verifies feasibility]
  Agent A → "YES, I can do: [specific description]" → Coordinator

  Agent B: [Analyzes task, checks resources, verifies feasibility]
  Agent B → "YES, I can do: [specific description]" → Coordinator

Phase 2: Execution (only if all YES)
  Coordinator → "PROCEED" → Agent A, Agent B

  Agents execute their tasks
```

**Key differences from database 2PC:**
- No lock holding between phases (impractical for agents)
- YES vote is best-effort commitment, not guaranteed
- Failure during Phase 2 requires compensation, not blocking

### Pattern 2: Checkpoint and Compensate

```
Execution with checkpoints:

Agent A: Execute → Checkpoint (save state) → Continue → Checkpoint → Done
            │                                    │
            └── On failure, restore checkpoint ◀─┘

Cross-agent:
  Agent A: Checkpoint → Execute
  Agent B: Checkpoint → Execute

  If either fails:
    Both restore to checkpoint
```

**Requires:** Agents that can checkpoint and restore state. For code changes, this is git. For other actions, requires explicit design.

### Pattern 3: Soft Locks with Timeout

```
Instead of hard locks:

Agent A: "I intend to modify file X" (soft lock, 5 min timeout)
Agent B: "I intend to modify file Y" (soft lock, 5 min timeout)

Coordinator: Sees no conflicts → "PROCEED"

If Agent A doesn't complete within 5 min:
  Lock expires
  Changes can be overwritten
  Agent A must re-acquire if still working
```

**Trade-off:** Reduces blocking at cost of potential conflicts.

### Pattern 4: Optimistic Execution with Validation

```
Skip the prepare phase for speed:

Agent A: Execute changes to file X
Agent B: Execute changes to file Y
Agent C: Execute changes to file Z

Validation Agent:
  - Check all changes are consistent
  - Check no conflicts
  - If valid: Accept all
  - If invalid: Rollback all

This is like optimistic concurrency control in databases.
```

**When to use:** When conflicts are rare and rollback is cheap.

## What 2PC Reveals About Agent Coordination

### 1. Consensus Is Harder Than It Looks

The Two Generals Problem proves that perfect agreement is impossible with unreliable communication. 2PC is a practical compromise:

- We accept the blocking window
- We accept that coordinator failure halts progress
- We get atomicity in exchange

**For agents:** Don't expect perfect coordination. Design for graceful degradation when coordination fails.

### 2. The Promise Phase Is Critical

2PC works because participants make a binding promise before the final decision. This changes everything:

| Without Promise Phase | With Promise Phase |
|----------------------|-------------------|
| Agents might fail mid-execution | Agents verify before committing |
| Coordinator decides blind | Coordinator decides with confirmation |
| Failure = unknown state | Failure = known recovery path |

**For agents:** The "can you do this?" query should trigger real verification, not optimistic agreement.

### 3. The Coordinator Is the Bottleneck

2PC has a single coordinator by design. This creates:
- Single point of failure
- Ordering (only one transaction at a time with same participants)
- Scalability limits

**For agents:** If you need coordination, accept the coordinator bottleneck or use patterns that don't need it (Saga, eventual consistency).

### 4. Blocking vs. Availability Trade-off

| 2PC Behavior | Consequence |
|--------------|-------------|
| Block when uncertain | Always consistent, but sometimes stuck |
| Proceed when uncertain | Available, but might be inconsistent |

2PC chooses consistency over availability. This is appropriate when inconsistency is catastrophic.

**For agents:** Is inconsistency catastrophic? Often no. Two agents making overlapping documentation changes is annoying, not catastrophic. Pick the right trade-off.

### 5. Compensation Is Often Better Than Prevention

2PC prevents inconsistency. Saga accepts it and fixes it.

| Approach | Cost |
|----------|------|
| Prevention (2PC) | Coordination overhead, blocking |
| Compensation (Saga) | Undo logic, temporary inconsistency |

**For agents:** Many agent actions are naturally compensable (undo code changes, resend corrected emails, update documentation again). Compensation is often cheaper than coordination.

## Open Questions

1. **What's the agent equivalent of "holding locks"?** In 2PC, participants hold locks between PREPARE and COMMIT. Can agents "lock" resources in a meaningful way?

2. **How long can agents maintain a commitment?** If an agent votes YES, how long can it reliably wait before executing? Context window limits may force a timeout.

3. **Can agents checkpoint reliably?** Saga compensation requires the ability to undo. Can agents reliably capture and restore state?

4. **What's the right timeout for agent voting?** Too short and you abort valid transactions. Too long and you block indefinitely.

5. **Should the human be the coordinator?** Human-in-the-loop naturally creates a coordinator. Is this the right model?

6. **Multi-agent consensus without coordinator?** Can agents reach agreement without a single coordinator? (See Paxos, Raft - but these are complex.)

7. **What actions are truly non-compensable for agents?** Sending external communications? Triggering physical systems? Where must we use prevention vs. compensation?

## Systems to Build

- [ ] **Verification query system:** Ask agents "can you complete this?" and get meaningful YES/NO
- [ ] **Commitment tracker:** Track which agents have committed to what
- [ ] **Compensation registry:** For each agent action, define the compensation action
- [ ] **Checkpoint mechanism:** Allow agents to save/restore state at boundaries
- [ ] **Coordinator service:** Central coordination point for multi-agent transactions
- [ ] **Timeout manager:** Handle agents that don't respond to coordination requests
- [ ] **Conflict detector:** Identify when agent actions would conflict

## Summary

Two-Phase Commit solves the distributed transaction problem by separating voting from execution. It guarantees atomicity at the cost of potential blocking when the coordinator fails.

**The protocol:**
1. **Phase 1 (Prepare):** Coordinator asks, participants verify and vote
2. **Phase 2 (Commit/Abort):** Coordinator decides, participants execute

**The key insight:** A YES vote is a binding promise. Participants surrender autonomy once they vote YES.

**The limitation:** The blocking problem. If the coordinator fails after participants vote YES but before the decision propagates, participants are stuck.

**Three-Phase Commit** adds a pre-commit phase to enable non-blocking recovery, but fails under network partitions.

**For agent systems:**
- Most agent coordination should NOT use 2PC - the overhead isn't worth it
- The Saga pattern (execute and compensate) is usually more appropriate
- Eventual consistency is acceptable for many agent tasks
- When atomicity truly matters, 2PC provides a framework but requires:
  - A reliable coordinator (often the human)
  - Agents that can make and honor commitments
  - Clear compensation strategies for failure

**The deeper insight:** Distributed consensus is fundamentally hard. There is no protocol that gives you atomicity, availability, and partition tolerance simultaneously (CAP theorem). 2PC trades availability (blocking) for consistency. Agent systems must make the same trade-off consciously.

The question isn't "should we use 2PC?" but "what's our tolerance for inconsistency, and what mechanisms do we have for recovery when things go wrong?"

## Status

**Phase:** Initial research complete. Core protocols mapped to agent coordination context. Key insight is that most agent systems should use Saga/compensation patterns rather than 2PC, because agent actions are usually compensable and the blocking problem is severe for agents that may have transient failures. 2PC semantics are valuable for understanding what "atomic coordination" requires, even if the full protocol is rarely implemented.

**Next:** Explore Saga pattern in depth, as it appears more applicable to typical agent coordination scenarios.
