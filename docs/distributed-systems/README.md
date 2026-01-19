# Distributed Systems

Mental models from distributed computing applied to multi-agent AI coordination.

## Purpose

Distributed systems research has formalized the fundamental tradeoffs in coordinating multiple independent processes. Multi-agent AI systems face identical challenges: consensus, consistency, failure handling, and coordination under uncertainty.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Fundamental Theorems

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| CAP Theorem | Eric Brewer | Consistency, Availability, Partition tolerance - pick two |
| PACELC | Daniel Abadi | Extends CAP: latency vs consistency tradeoff |
| FLP Impossibility | Fischer, Lynch, Paterson | Consensus impossible with one faulty process |
| Two Generals Problem | Classical | Coordinated action with unreliable communication |
| Byzantine Generals | Lamport et al. | Consensus with malicious actors |

### Consistency Models

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Strong Consistency | Distributed DBs | All see same state simultaneously |
| Eventual Consistency | Dynamo, etc. | Converges over time |
| Causal Consistency | Vector clocks | Respects cause-effect ordering |
| Read-Your-Writes | Session guarantees | See your own changes |
| Monotonic Reads | Session guarantees | Never see older state |

### Consensus Protocols

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Paxos | Lamport | Classic consensus algorithm |
| Raft | Ongaro & Ousterhout | Understandable consensus |
| Two-Phase Commit | Distributed transactions | Coordinated commit/abort |
| Three-Phase Commit | Non-blocking variant | Better failure handling |
| PBFT | Castro & Liskov | Byzantine fault tolerant consensus |

### Failure Handling

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Fail-Stop vs Fail-Silent | Fault models | How failures manifest |
| Crash-Recovery | Fault models | Processes that restart |
| Byzantine Failure | Fault models | Arbitrary/malicious behavior |
| Failure Detectors | Chandra & Toueg | Unreliable vs perfect detection |
| Heartbeats & Timeouts | Practical systems | Detecting liveness |

### Coordination Patterns

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Leader Election | Consensus | Choosing a coordinator |
| Quorum Systems | Replicated data | Majorities for consistency |
| Vector Clocks | Distributed ordering | Tracking causality |
| Logical Clocks | Lamport | Ordering without synchronized time |
| Saga Pattern | Microservices | Long-running distributed transactions |

### Scalability Patterns

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Sharding/Partitioning | Databases | Dividing work by key |
| Replication | Databases | Copies for availability |
| Load Balancing | Web services | Distributing requests |
| Backpressure | Reactive systems | Slowing producers when consumers overwhelmed |
| Bulkheads | Release It! | Isolation to prevent cascade |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| CAP Theorem | Very High | Medium | 1 |
| Eventual Consistency | Very High | Medium | 1 |
| Leader Election | High | Medium | 1 |
| Two Generals Problem | High | Low | 1 |
| Failure Detectors | High | Medium | 2 |
| Saga Pattern | High | Medium | 2 |
| Vector Clocks | Medium | High | 2 |
| Byzantine Generals | Medium | High | 3 |

## Key Questions

1. What's the CAP tradeoff for multi-agent systems? (Consensus vs responsiveness vs network partition?)
2. Is "eventual consistency" acceptable for agent coordination? When?
3. How do we handle the Two Generals Problem when agents need to coordinate irreversible actions?
4. What's the equivalent of "leader election" - choosing which agent coordinates?
5. How do we detect agent failures? What's the timeout?

## Related Directories

- [Control Theory](../control-theory/) - Feedback and coordination
- [Safety Engineering](../safety-engineering/) - Failure handling
- [Management](../management/) - Incident Command System (coordination)
