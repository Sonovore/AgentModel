# Metrics Instrumentation Research

**Research Date:** 2026-01-21
**Purpose:** Determine how to instrument agent systems for reliable, comparable measurements

---

## Executive Summary

**Key findings:**
- **Existing frameworks:** LangSmith (LangGraph) uses distributed tracing + OpenTelemetry (2025)
- **Industry standard:** OpenTelemetry reached full maturity (metrics, traces, logs GA in 2025)
- **Lightweight option:** Prometheus + structlog sufficient for our experiments
- **Token counting:** Must estimate (tiktoken) or track via API responses
- **Latency measurement:** Use `time.perf_counter()` for high precision

**Recommendation:** Start with **lightweight custom collector** (structlog + JSON Lines storage), not full OpenTelemetry (overkill for experiments).

---

## Part 1: Framework Instrumentation Review

### LangSmith (LangGraph's Observability System)

**Architecture:**
- **LangSmith** - Centralized observability platform (SaaS)
- **OpenTelemetry** - Standard instrumentation (2025 integration)
- **Distributed tracing** - Tracks multi-agent execution flow
- **Component-level metrics** - Execution flow, latency, intermediate state, failures

**Key capabilities:**
- Automatically tracks inputs, outputs, intermediate steps
- Tool usage tracking
- Memory chain tracking
- Integration with existing observability tools (Datadog, Grafana, Jaeger)

**Instrumentation approach:**
```python
# LangSmith automatically instruments via SDK
from langsmith import Client

client = Client()
# All LangChain/LangGraph calls automatically traced
```

**What we can learn:**
- Component-level tracking is critical (which agent did what)
- Trace IDs link related operations
- Async/distributed tracing patterns
- Integration with standard tools (OTel)

**Why we won't use it:**
- Requires LangChain/LangGraph (we're building from scratch)
- SaaS platform (we want local experiments)
- Overkill for simple experiments

### CrewAI Metrics

**No specific documentation found for CrewAI's internal metrics.**

Likely uses:
- Execution logs
- Task completion tracking
- Simple timing measurements

**Why limited info:**
- Higher-level abstraction (hides instrumentation)
- Focus on developer productivity over observability
- Built-in tracking may be minimal

### OpenAI SDK Observability

**No specific documentation found for OpenAI Agents SDK metrics.**

Likely relies on:
- OpenAI API response metadata (token counts, latency)
- Application-level logging
- External monitoring tools

**Pattern:**
- Minimalist framework = minimalist instrumentation
- Rely on underlying API metrics
- Application adds custom tracking

---

## Part 2: Python Observability Libraries

### OpenTelemetry (Industry Standard)

**Status in 2025:**
- **Full maturity** - GA status for metrics, traces, logs
- **Auto-instrumentation** - 20+ languages and frameworks
- **Python support** - Python 3.9+ fully supported

**What it provides:**
- **Traces** - Distributed execution tracking
- **Metrics** - Counter, UpDownCounter, Gauge, Histogram
- **Logs** - Structured logging with trace correlation
- **Context propagation** - Links related operations
- **Exporters** - Send to Prometheus, Jaeger, Grafana, etc.

**Architecture:**
```python
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider

# Setup
tracer_provider = TracerProvider()
meter_provider = MeterProvider()

tracer = tracer_provider.get_tracer(__name__)
meter = meter_provider.get_meter(__name__)

# Instrument
with tracer.start_as_current_span("agent_execution"):
    counter = meter.create_counter("agent_tasks")
    counter.add(1, {"agent": "worker-1", "status": "success"})
```

**Pros:**
- Industry standard (vendor-neutral)
- Mature ecosystem
- Integrates with everything
- Automatic HTTP/gRPC instrumentation

**Cons:**
- Complex setup for simple use cases
- Requires external backend (Prometheus, Jaeger)
- Overhead (tracing isn't free)
- Learning curve

**Verdict:**
- **Not recommended for MVP** - Too heavy for experiments
- **Consider for production** - If scaling beyond experiments
- **Use if integrating** - With existing observability stack

### Prometheus (Metrics Collection)

**What it is:**
- Time-series metrics database
- Pull-based model (scrapes endpoints)
- Simple metric types (counter, gauge, histogram, summary)

**Python client:**
```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define metrics
task_counter = Counter('agent_tasks_total', 'Total tasks', ['agent', 'status'])
task_duration = Histogram('agent_task_duration_seconds', 'Task duration', ['agent'])
active_agents = Gauge('active_agents', 'Currently active agents')

# Instrument
task_counter.labels(agent='worker-1', status='success').inc()
with task_duration.labels(agent='worker-1').time():
    execute_task()
active_agents.inc()

# Expose metrics
start_http_server(8000)  # Prometheus scrapes http://localhost:8000/metrics
```

**Pros:**
- Lightweight
- Standard metric types
- Easy to expose
- Grafana integration

**Cons:**
- Requires scraping infrastructure
- Pull model (need HTTP server)
- No tracing (metrics only)
- Separate from logs

**Verdict:**
- **Good for production monitoring**
- **Overkill for experiments** - Don't need persistent metrics DB
- **Use if scaling** - Deploy Prometheus + Grafana stack

### Structlog (Structured Logging)

**What it is:**
- Structured logging library
- JSON output by default
- Context binding
- Integration with observability platforms

**Usage:**
```python
import structlog

# Configure
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)

log = structlog.get_logger()

# Log with structure
log.info("agent_started",
    agent_id="worker-1",
    agent_type="general-purpose",
    model="sonnet"
)

log.info("task_completed",
    agent_id="worker-1",
    task_id="TASK-001",
    duration_ms=1234,
    tokens_used=567
)
```

**Output:**
```json
{"event": "agent_started", "agent_id": "worker-1", "agent_type": "general-purpose", "model": "sonnet", "timestamp": "2026-01-21T10:30:00Z"}
{"event": "task_completed", "agent_id": "worker-1", "task_id": "TASK-001", "duration_ms": 1234, "tokens_used": 567, "timestamp": "2026-01-21T10:30:01Z"}
```

**Pros:**
- Lightweight (logging only)
- Structured output (easy parsing)
- Context binding (attach metadata)
- No external dependencies
- JSON = easy analysis (pandas, jq)

**Cons:**
- Logging only (no metrics/traces built-in)
- No aggregation (need post-processing)
- No visualization (need separate tool)

**Verdict:**
- **Perfect for experiments** - Simple, effective, analyzable
- **Recommended for MVP** - Log to JSON Lines, analyze with pandas
- **Upgrade path** - Can feed into OTel later

### JSON Lines (Storage Format)

**What it is:**
- One JSON object per line
- Easy to append (no array closing bracket)
- Easy to stream (process line-by-line)
- Standard format (`.jsonl` extension)

**Example:**
```jsonl
{"event": "experiment_start", "exp_id": "EXP-001", "timestamp": "2026-01-21T10:00:00Z"}
{"event": "agent_spawn", "agent_id": "worker-1", "timestamp": "2026-01-21T10:00:01Z"}
{"event": "task_complete", "agent_id": "worker-1", "duration_ms": 1234, "timestamp": "2026-01-21T10:00:02Z"}
{"event": "experiment_end", "exp_id": "EXP-001", "timestamp": "2026-01-21T10:00:03Z"}
```

**Pros:**
- Append-friendly (no file rewriting)
- Stream-friendly (process incrementally)
- Pandas-friendly (`pd.read_json(lines=True)`)
- Human-readable (can read directly)
- Git-friendly (line-based diffs)

**Cons:**
- No schema enforcement (need validation)
- No indexing (sequential scan)
- No querying (need to load into tool)

**Verdict:**
- **Perfect for experiments** - Simple, flexible, analyzable
- **Recommended** - Primary storage format for metrics

---

## Part 3: Metric Types and Measurement Points

### Latency Measurement

**Use Python's `time.perf_counter()` for high precision:**

```python
import time

start = time.perf_counter()
execute_agent_task()
end = time.perf_counter()
duration_ms = (end - start) * 1000  # Convert to milliseconds
```

**Why `perf_counter()`:**
- High resolution (nanosecond precision)
- Monotonic (unaffected by system clock changes)
- Best for performance measurement

**Why NOT `time.time()`:**
- Lower resolution
- Affected by clock adjustments
- Not monotonic

**Measurement points:**
```python
# Agent execution (full lifecycle)
start_agent = time.perf_counter()
result = spawn_agent(task)
end_agent = time.perf_counter()
agent_latency_ms = (end_agent - start_agent) * 1000

# Task processing (within agent)
start_task = time.perf_counter()
process_task(input)
end_task = time.perf_counter()
task_latency_ms = (end_task - start_task) * 1000

# Message routing (hub operations)
start_route = time.perf_counter()
route_message(message)
end_route = time.perf_counter()
route_latency_ms = (end_route - start_route) * 1000
```

### Token Counting

**Challenge:** Claude Code doesn't expose token counts directly

**Option 1: Estimate with tiktoken**
```python
import tiktoken

encoding = tiktoken.encoding_for_model("claude-3-5-sonnet-20241022")
tokens = encoding.encode(text)
token_count = len(tokens)
```

**Pros:**
- Fast estimation
- No API dependency
- Works offline

**Cons:**
- Approximate (Claude uses different tokenizer)
- Input tokens only (unless we capture output)
- May undercount

**Option 2: Track via API responses**
```python
# If Claude Code returns token usage in agent result
result = spawn_agent(task)
if "usage" in result:
    input_tokens = result["usage"]["input_tokens"]
    output_tokens = result["usage"]["output_tokens"]
    total_tokens = input_tokens + output_tokens
```

**Pros:**
- Accurate (actual usage)
- Input + output
- Billing-aligned

**Cons:**
- Requires API response parsing
- May not be available in Claude Code
- Depends on return format

**Recommendation:**
- Use **tiktoken for estimates** during development
- Track **actual counts if available** in results
- Log both for comparison

### Message Counting

**What counts as a message:**
- `task.assignment` - Orchestrator → Agent
- `task.handoff` - Agent → Agent (via orchestrator)
- `status.*` - Agent → Orchestrator
- `coord.*` - Orchestrator → Agents
- `escalation.*` - Agent → Orchestrator
- `ack.*` - Agent → Orchestrator

**Tracking approach:**
```python
message_counter = {
    "task.assignment": 0,
    "task.handoff": 0,
    "status.ready": 0,
    "status.busy": 0,
    # ... etc
}

def send_message(message):
    message_type = message["message_type"]
    message_counter[message_type] += 1
    log.info("message_sent",
        message_type=message_type,
        sender=message["sender"],
        recipient=message["recipient"]
    )
```

**Alternative: File-based tracking**
```python
# Each message written to messages.jsonl
with open("messages.jsonl", "a") as f:
    f.write(json.dumps(message) + "\n")

# Count in post-processing
df = pd.read_json("messages.jsonl", lines=True)
message_counts = df.groupby("message_type").size()
```

### Error Tracking

**Error categorization:**
```python
ERROR_CATEGORIES = [
    "validation",  # Schema validation failed
    "resource",    # File not found, API unavailable
    "timeout",     # Operation exceeded time limit
    "conflict",    # Resource conflict, race condition
    "invariant",   # System invariant violated
    "external"     # External system error
]

def log_error(error, context):
    log.error("agent_error",
        error_type=type(error).__name__,
        error_category=categorize_error(error),
        error_message=str(error),
        stack_trace=traceback.format_exc(),
        **context
    )
```

**Recovery tracking:**
```python
recovery_attempts = []

def attempt_recovery(error, strategy):
    attempt = {
        "error_id": error.id,
        "strategy": strategy,  # "retry", "fallback", "escalate"
        "timestamp": datetime.utcnow().isoformat(),
        "success": None  # Set after attempt
    }
    recovery_attempts.append(attempt)

    try:
        result = execute_recovery(strategy)
        attempt["success"] = True
        return result
    except Exception as e:
        attempt["success"] = False
        attempt["failure_reason"] = str(e)
        raise
```

---

## Part 4: Metrics Collector Design

### Interface Specification

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any
import json
import time

@dataclass
class TaskMetrics:
    """Metrics for a single task execution"""
    task_id: str
    agent_id: str
    agent_type: str
    model: str
    start_time: float
    end_time: Optional[float] = None
    duration_ms: Optional[float] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    status: str = "running"  # "running", "success", "failed"
    error: Optional[str] = None

class MetricsCollector:
    """Lightweight metrics collector for agent experiments"""

    def __init__(self, output_file: str = "metrics.jsonl"):
        self.output_file = output_file
        self.active_tasks: Dict[str, TaskMetrics] = {}

    def start_task(self, task_id: str, agent_id: str,
                   agent_type: str, model: str) -> None:
        """Record task start"""
        metrics = TaskMetrics(
            task_id=task_id,
            agent_id=agent_id,
            agent_type=agent_type,
            model=model,
            start_time=time.perf_counter()
        )
        self.active_tasks[task_id] = metrics
        self._log_event("task_start", metrics.__dict__)

    def end_task(self, task_id: str, status: str = "success",
                 input_tokens: Optional[int] = None,
                 output_tokens: Optional[int] = None,
                 error: Optional[str] = None) -> None:
        """Record task completion"""
        if task_id not in self.active_tasks:
            raise ValueError(f"Unknown task: {task_id}")

        metrics = self.active_tasks[task_id]
        metrics.end_time = time.perf_counter()
        metrics.duration_ms = (metrics.end_time - metrics.start_time) * 1000
        metrics.status = status
        metrics.input_tokens = input_tokens
        metrics.output_tokens = output_tokens
        metrics.error = error

        self._log_event("task_end", metrics.__dict__)
        del self.active_tasks[task_id]

    def log_message(self, message: Dict[str, Any]) -> None:
        """Record message sent"""
        self._log_event("message_sent", {
            "message_type": message["message_type"],
            "sender": message["sender"],
            "recipient": message["recipient"],
            "message_id": message["message_id"]
        })

    def log_error(self, error: Exception, context: Dict[str, Any]) -> None:
        """Record error"""
        self._log_event("error", {
            "error_type": type(error).__name__,
            "error_message": str(error),
            **context
        })

    def _log_event(self, event_type: str, data: Dict[str, Any]) -> None:
        """Write event to JSON Lines file"""
        event = {
            "event": event_type,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            **data
        }
        with open(self.output_file, "a") as f:
            f.write(json.dumps(event) + "\n")
```

### Usage Pattern

```python
# Initialize collector
metrics = MetricsCollector("experiments/exp-001/metrics.jsonl")

# Start task
metrics.start_task(
    task_id="TASK-001",
    agent_id="worker-1",
    agent_type="general-purpose",
    model="sonnet"
)

# Execute task
try:
    result = execute_agent_task()

    # End task successfully
    metrics.end_task(
        task_id="TASK-001",
        status="success",
        input_tokens=result.get("input_tokens"),
        output_tokens=result.get("output_tokens")
    )
except Exception as e:
    # End task with error
    metrics.end_task(
        task_id="TASK-001",
        status="failed",
        error=str(e)
    )
    metrics.log_error(e, {"task_id": "TASK-001"})

# Log messages
message = create_message(...)
metrics.log_message(message)
```

### Analysis Pattern

```python
import pandas as pd

# Load metrics
df = pd.read_json("experiments/exp-001/metrics.jsonl", lines=True)

# Filter to task events
task_starts = df[df["event"] == "task_start"]
task_ends = df[df["event"] == "task_end"]

# Aggregate statistics
print("Task Duration Statistics:")
print(task_ends["duration_ms"].describe())

print("\nTask Success Rate:")
print(task_ends["status"].value_counts(normalize=True))

print("\nToken Usage:")
print(f"Total input tokens: {task_ends['input_tokens'].sum()}")
print(f"Total output tokens: {task_ends['output_tokens'].sum()}")

# Message counts
message_events = df[df["event"] == "message_sent"]
print("\nMessage Counts by Type:")
print(message_events["message_type"].value_counts())
```

---

## Part 5: Storage Format Specification

### JSON Lines Schema

**Event types:**

**1. experiment_start**
```json
{
  "event": "experiment_start",
  "experiment_id": "EXP-001",
  "experiment_name": "Coordination Model Comparison",
  "variation": "cue-based",
  "timestamp": "2026-01-21T10:00:00.000Z"
}
```

**2. task_start**
```json
{
  "event": "task_start",
  "task_id": "TASK-001",
  "agent_id": "worker-1",
  "agent_type": "general-purpose",
  "model": "sonnet",
  "start_time": 1234567.89,
  "timestamp": "2026-01-21T10:00:01.000Z"
}
```

**3. task_end**
```json
{
  "event": "task_end",
  "task_id": "TASK-001",
  "agent_id": "worker-1",
  "agent_type": "general-purpose",
  "model": "sonnet",
  "start_time": 1234567.89,
  "end_time": 1234569.12,
  "duration_ms": 1230,
  "input_tokens": 450,
  "output_tokens": 120,
  "status": "success",
  "error": null,
  "timestamp": "2026-01-21T10:00:02.230Z"
}
```

**4. message_sent**
```json
{
  "event": "message_sent",
  "message_type": "task.assignment",
  "message_id": "550e8400-e29b-41d4-a716-446655440000",
  "sender": "orchestrator-main",
  "recipient": "worker-1",
  "timestamp": "2026-01-21T10:00:01.100Z"
}
```

**5. error**
```json
{
  "event": "error",
  "error_type": "ValidationError",
  "error_message": "Message does not match schema",
  "error_category": "validation",
  "task_id": "TASK-001",
  "agent_id": "worker-1",
  "timestamp": "2026-01-21T10:00:02.500Z"
}
```

**6. experiment_end**
```json
{
  "event": "experiment_end",
  "experiment_id": "EXP-001",
  "total_tasks": 100,
  "successful_tasks": 95,
  "failed_tasks": 5,
  "total_duration_ms": 12345,
  "timestamp": "2026-01-21T10:02:15.345Z"
}
```

### Directory Structure

```
experiments/
├── exp-001-coordination-comparison/
│   ├── config.yaml              # Experiment configuration
│   ├── metrics.jsonl            # All metrics (timestamped events)
│   ├── messages.jsonl           # All messages sent (optional)
│   ├── errors.jsonl             # All errors (optional, or in metrics)
│   └── results.json             # Aggregated results summary
├── exp-002-scale-test/
│   └── ...
└── analysis/
    └── comparison.ipynb         # Cross-experiment analysis
```

---

## Part 6: Key Recommendations

### For MVP (Next 2 weeks)

**Use:**
1. **Structlog** - Structured logging to JSON Lines
2. **Custom MetricsCollector** - Lightweight wrapper
3. **JSON Lines files** - Storage format
4. **Pandas** - Analysis and aggregation
5. **time.perf_counter()** - High-precision timing
6. **tiktoken** - Token estimation

**Don't use (yet):**
- OpenTelemetry (too heavy)
- Prometheus (overkill)
- LangSmith (framework-specific)
- Complex tracing (not needed)

### For Production (Future)

**Consider upgrading to:**
1. **OpenTelemetry** - If integrating with existing stack
2. **Prometheus + Grafana** - If need real-time dashboards
3. **Distributed tracing** - If debugging complex multi-agent flows
4. **Custom backend** - If scaling beyond experiments

### Measurement Strategy

**Always measure:**
- Task start/end times (wall clock)
- Task duration (high precision)
- Task success/failure status
- Message counts by type
- Error counts by category

**Measure when available:**
- Token counts (input + output)
- Agent utilization (idle time)
- Queue depths (message backlog)
- Recovery attempts

**Calculate in post-processing:**
- Throughput (tasks per second)
- Success rate (%)
- P50/P95/P99 latency
- Coordination overhead (% of total time)
- Cost estimates (tokens × price)

---

## Conclusion

**Lightweight instrumentation is sufficient for experiments.**

**Recommended stack:**
- structlog → JSON Lines → pandas → matplotlib
- Simple, effective, analyzable, no external dependencies

**Implementation priority:**
1. MetricsCollector class (2 hours)
2. JSON Lines storage (30 min)
3. Analysis notebook template (1 hour)
4. Integration with test harness (1 hour)

**Total effort:** ~5 hours to working instrumentation

**Status: READY TO IMPLEMENT**

---

## Sources

- [LangSmith Observability](https://www.langchain.com/langsmith/observability)
- [LangSmith Observability Documentation](https://docs.langchain.com/langsmith/observability)
- [Building Observable AI Agents Using LangGraph and LangSmith](https://ubiai.tools/building-observable-and-reliable-ai-agents-using-langgraph-langsmith-and-ubiai/)
- [End-to-End OpenTelemetry Support in LangSmith](https://www.blog.langchain.com/end-to-end-opentelemetry-langsmith/)
- [OpenTelemetry Python Documentation](https://opentelemetry.io/docs/languages/python/)
- [Python Logging with Structlog](https://last9.io/blog/python-logging-with-structlog/)
- [Implementing OpenTelemetry Metrics in Python Apps](https://betterstack.com/community/guides/observability/otel-metrics-python/)
- [2025 Observability Guide: OpenTelemetry + Grafana 11](https://markaicode.com/2025-observability-opentelemetry-grafana-11-full-stack-monitoring/)
