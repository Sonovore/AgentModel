# Experiment Management System Research

**Research Date:** 2026-01-21
**Purpose:** Determine systematic approach for configuring, running, storing, and comparing agent experiments

---

## Executive Summary

**Key findings:**
- **Industry tools:** MLflow (full platform), Weights & Biases (managed service), Sacred (lightweight)
- **Our needs:** Simple experiments, not ML model training
- **Recommendation:** **Custom lightweight system** with YAML config + JSON Lines results
- **Why:** ML experiment tracking is overkill, adds complexity, learning curve
- **Decision:** Build minimal system (~4 hours) vs learn/integrate heavy tools (~2+ days)

**Verdict:** Use **YAML for config**, **JSON Lines for results**, **pandas for analysis**, **git for versioning**

---

## Part 1: ML Experiment Tracking Tools Survey

### MLflow (Full MLOps Platform)

**What it is:**
- Open-source developer platform for building AI/LLM applications
- End-to-end experiment tracking, observability, evaluations
- Organized around "runs" (executions of data science code)

**Key capabilities:**
- **Tracking:** Logs parameters, metrics, start/end times, artifacts
- **Auto-logging:** Integrates with Scikit-learn, TensorFlow, PyTorch, XGBoost, LightGBM
- **Model registry:** Version and deploy models
- **Projects:** Package and reproduce runs
- **GenAI/LLM support:** (2025 updates: MLflow 3)

**Usage pattern:**
```python
import mlflow

mlflow.start_run()
mlflow.log_param("coordination_model", "cue-based")
mlflow.log_param("agent_count", 5)

# Execute experiment
result = run_experiment()

mlflow.log_metric("latency_ms", result.latency)
mlflow.log_metric("success_rate", result.success_rate)
mlflow.end_run()
```

**Pros:**
- Comprehensive (covers entire ML workflow)
- Auto-logging (minimal code changes)
- UI for visualization
- Model registry and deployment
- Mature ecosystem

**Cons:**
- Heavy (requires MLflow server or cloud)
- ML-focused (not designed for agent experiments)
- Learning curve (concepts: runs, experiments, projects)
- Overhead (logging infrastructure, UI complexity)
- Overkill (we don't need model registry, deployment)

**Verdict for our use case:**
- ❌ **Not recommended** - Too heavy for simple experiments
- ❌ Designed for ML training loops, not agent coordination
- ❌ Would spend more time learning MLflow than running experiments

### Weights & Biases (Managed Service)

**What it is:**
- Cloud-based ML experiment tracking platform
- Serves 200,000+ ML practitioners (OpenAI, Toyota, Samsung)
- "5 lines of code" integration

**Key capabilities:**
- **Experiment tracking:** Logs parameters, metrics, artifacts
- **Hyperparameter optimization:** Auto-tuning
- **Model registry:** Version control
- **Team collaboration:** Shared dashboards
- **Framework integration:** PyTorch, TensorFlow, Hugging Face
- **Self-hosted option:** On-premises deployment

**Usage pattern:**
```python
import wandb

wandb.init(project="agent-experiments", name="exp-001")
wandb.config.coordination_model = "cue-based"
wandb.config.agent_count = 5

# Execute experiment
result = run_experiment()

wandb.log({"latency_ms": result.latency})
wandb.log({"success_rate": result.success_rate})
wandb.finish()
```

**Pros:**
- Easy integration (5 lines of code)
- Beautiful dashboards
- Team collaboration features
- Managed service (no infrastructure)
- Strong community support

**Cons:**
- Cloud dependency (sends data to W&B servers)
- Pricing (free tier limited, paid for teams)
- ML-focused (agent experiments are not standard use case)
- Privacy concerns (experiment data leaves our machine)
- Overkill (we don't need hyperparameter tuning, team dashboards)

**Verdict for our use case:**
- ❌ **Not recommended** - Unnecessary cloud dependency
- ❌ Data privacy (experiment details to external service)
- ❌ Overkill (designed for enterprise ML teams)

### Sacred (Lightweight Open Source)

**What it is:**
- Lightweight Python experiment tracking library
- Focused solely on logging (no UI, no platform)
- MIT licensed, open source

**Key capabilities:**
- **Configuration management:** Track all parameters
- **Experiment logging:** Metrics, artifacts, dependencies
- **Observers:** Send data to MongoDB, SQL, file system
- **Randomness control:** Reproducible experiments
- **External UI:** Omniboard or Sacredboard (separate projects)

**Usage pattern:**
```python
from sacred import Experiment

ex = Experiment('agent-experiment')

@ex.config
def cfg():
    coordination_model = "cue-based"
    agent_count = 5

@ex.automain
def run(coordination_model, agent_count):
    result = run_experiment(coordination_model, agent_count)
    ex.log_scalar("latency_ms", result.latency)
    ex.log_scalar("success_rate", result.success_rate)
    return result
```

**Pros:**
- Lightweight (no server, no cloud)
- Open source (no vendor lock-in)
- Flexible (custom observers)
- Python-focused
- No pricing

**Cons:**
- No built-in UI (need Omniboard/Sacredboard)
- MongoDB typically required (or file-based observer)
- More code than plain Python (decorators, framework)
- Designed for ML experiments (not perfect fit)
- Moderate learning curve

**Verdict for our use case:**
- ⚠️ **Possible but not ideal** - Lightweight but still framework overhead
- ⚠️ Requires decorators/framework thinking
- ⚠️ Need separate UI tool for visualization

---

## Part 2: Custom Lightweight System Design

### Why Custom > Tools

**Our requirements are simpler than ML experiments:**
1. Run experiment with config (coordination model, agent count, task type)
2. Record metrics (latency, tokens, messages, errors)
3. Store results (structured format)
4. Compare results (across variations)
5. Visualize trends (simple plots)

**We don't need:**
- Hyperparameter optimization
- Model registry
- Team collaboration dashboards
- Cloud integration
- Auto-logging for ML frameworks
- Distributed training support

**Benefit of custom:**
- Zero learning curve (YAML + JSON + pandas we already know)
- Zero external dependencies (no servers, no accounts)
- Full control (modify as needed)
- Minimal code (~200 lines total)
- Git-friendly (text files, not databases)

### Architecture

```
experiments/
├── exp-001-coordination-comparison/
│   ├── config.yaml              # Experiment configuration
│   ├── run-001/                 # Trial 1
│   │   ├── metrics.jsonl        # Timestamped metrics
│   │   └── summary.json         # Aggregated results
│   ├── run-002/                 # Trial 2
│   │   └── ...
│   └── analysis.ipynb           # Experiment analysis notebook
├── exp-002-scale-test/
│   └── ...
├── templates/
│   ├── config.yaml.template     # Config template
│   └── analysis.ipynb.template  # Analysis template
└── lib/
    ├── experiment_runner.py     # Run experiments from config
    └── experiment_analyzer.py   # Analyze and compare results
```

### Experiment Configuration Format

**File:** `experiments/exp-001-coordination-comparison/config.yaml`

```yaml
# Experiment metadata
experiment:
  id: "EXP-001"
  name: "Coordination Model Comparison"
  description: "Compare cue-based vs event-driven vs polling for Task S1"
  author: "researcher"
  created: "2026-01-21"

# Task to run
task:
  type: "task_s1_map_reduce"  # References tasks/ directory
  description: "Process 100 files in parallel"
  data_path: "test-harness/data/task-s1/"

# Variations to test (each gets N trials)
variations:
  - name: "Cue-Based Coordination"
    params:
      coordination_model: "cue_based"
      communication_pattern: "hub_and_spoke"
      error_handling: "jidoka"
      agent_count: 5
      agent_model: "sonnet"

  - name: "Event-Driven"
    params:
      coordination_model: "event_driven"
      communication_pattern: "hub_and_spoke"
      error_handling: "jidoka"
      agent_count: 5
      agent_model: "sonnet"

  - name: "Polling"
    params:
      coordination_model: "polling"
      communication_pattern: "hub_and_spoke"
      error_handling: "jidoka"
      agent_count: 5
      agent_model: "sonnet"

# Number of trials per variation (for statistical significance)
trials: 10

# Metrics to collect
metrics:
  - "completion_time_ms"
  - "message_count"
  - "error_rate"
  - "idle_time_percent"
  - "total_tokens"

# Success criteria (optional validation)
success_criteria:
  - metric: "error_rate"
    condition: "< 0.05"
  - metric: "completion_time_ms"
    condition: "< 60000"  # 60 seconds

# Environment
environment:
  python_version: "3.13"
  claude_code_version: "1.x"
  git_commit: "ad3f49a"  # Auto-populated by runner
```

### Result Storage Format

**File:** `experiments/exp-001-coordination-comparison/run-001/summary.json`

```json
{
  "experiment_id": "EXP-001",
  "variation": "Cue-Based Coordination",
  "trial": 1,
  "params": {
    "coordination_model": "cue_based",
    "agent_count": 5,
    "agent_model": "sonnet"
  },
  "metrics": {
    "completion_time_ms": 12345,
    "message_count": 47,
    "error_rate": 0.02,
    "idle_time_percent": 15.3,
    "total_tokens": 5678,
    "input_tokens": 3456,
    "output_tokens": 2222
  },
  "status": "success",
  "error": null,
  "started_at": "2026-01-21T10:00:00.000Z",
  "ended_at": "2026-01-21T10:00:12.345Z",
  "duration_ms": 12345
}
```

### Experiment Runner

**File:** `test-harness/lib/experiment_runner.py`

```python
import yaml
import json
from pathlib import Path
from datetime import datetime
import subprocess

class ExperimentRunner:
    """Run experiments from YAML configuration"""

    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        self.experiment_dir = self.config_path.parent
        self.runs_dir = self.experiment_dir / "runs"
        self.runs_dir.mkdir(exist_ok=True)

    def run_all(self):
        """Run all variations × trials"""
        for variation in self.config["variations"]:
            for trial in range(1, self.config["trials"] + 1):
                self.run_single(variation, trial)

    def run_single(self, variation: dict, trial: int):
        """Run single trial of a variation"""
        print(f"Running {variation['name']} trial {trial}...")

        # Create run directory
        run_id = f"run-{len(list(self.runs_dir.glob('run-*'))) + 1:03d}"
        run_dir = self.runs_dir / run_id
        run_dir.mkdir()

        # Prepare task execution
        task_module = self.load_task(self.config["task"]["type"])
        metrics_file = run_dir / "metrics.jsonl"

        # Execute task with parameters
        start_time = datetime.utcnow()
        try:
            result = task_module.execute(
                params=variation["params"],
                data_path=self.config["task"]["data_path"],
                metrics_file=metrics_file
            )
            status = "success"
            error = None
        except Exception as e:
            status = "failed"
            error = str(e)
            result = {}

        end_time = datetime.utcnow()
        duration_ms = (end_time - start_time).total_seconds() * 1000

        # Write summary
        summary = {
            "experiment_id": self.config["experiment"]["id"],
            "variation": variation["name"],
            "trial": trial,
            "params": variation["params"],
            "metrics": result.get("metrics", {}),
            "status": status,
            "error": error,
            "started_at": start_time.isoformat() + "Z",
            "ended_at": end_time.isoformat() + "Z",
            "duration_ms": duration_ms
        }

        with open(run_dir / "summary.json", "w") as f:
            json.dump(summary, f, indent=2)

        print(f"  ✓ Completed in {duration_ms:.0f}ms")

    def load_task(self, task_type: str):
        """Dynamically load task module"""
        # Import from tasks/ directory
        module_name = f"tasks.{task_type}"
        return __import__(module_name, fromlist=["execute"])
```

### Experiment Analyzer

**File:** `test-harness/lib/experiment_analyzer.py`

```python
import json
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

class ExperimentAnalyzer:
    """Analyze and compare experiment results"""

    def __init__(self, experiment_dir: str):
        self.experiment_dir = Path(experiment_dir)
        self.runs_dir = self.experiment_dir / "runs"
        self.results = self.load_results()

    def load_results(self) -> pd.DataFrame:
        """Load all run summaries into DataFrame"""
        summaries = []
        for run_dir in sorted(self.runs_dir.glob("run-*")):
            summary_file = run_dir / "summary.json"
            if summary_file.exists():
                with open(summary_file) as f:
                    summary = json.load(f)
                summaries.append(summary)

        return pd.DataFrame(summaries)

    def aggregate_by_variation(self) -> pd.DataFrame:
        """Aggregate metrics by variation"""
        # Expand nested metrics dict
        metrics_df = pd.json_normalize(self.results["metrics"])
        results_with_metrics = pd.concat([
            self.results.drop(columns=["metrics"]),
            metrics_df
        ], axis=1)

        # Group by variation, calculate statistics
        agg_funcs = ["mean", "std", "min", "max", "median"]
        grouped = results_with_metrics.groupby("variation").agg(agg_funcs)

        return grouped

    def plot_comparison(self, metric: str):
        """Plot metric comparison across variations"""
        # Extract metric from nested dict
        metric_data = []
        for _, row in self.results.iterrows():
            if metric in row["metrics"]:
                metric_data.append({
                    "variation": row["variation"],
                    "value": row["metrics"][metric]
                })

        df = pd.DataFrame(metric_data)

        # Box plot
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x="variation", y="value")
        plt.title(f"{metric} by Variation")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def statistical_test(self, metric: str, variation_a: str, variation_b: str):
        """Compare two variations statistically"""
        from scipy import stats

        # Extract data
        data_a = [row["metrics"][metric]
                  for _, row in self.results.iterrows()
                  if row["variation"] == variation_a and metric in row["metrics"]]
        data_b = [row["metrics"][metric]
                  for _, row in self.results.iterrows()
                  if row["variation"] == variation_b and metric in row["metrics"]]

        # T-test
        t_stat, p_value = stats.ttest_ind(data_a, data_b)

        print(f"Comparing {variation_a} vs {variation_b} on {metric}:")
        print(f"  Mean A: {sum(data_a)/len(data_a):.2f}")
        print(f"  Mean B: {sum(data_b)/len(data_b):.2f}")
        print(f"  T-statistic: {t_stat:.2f}")
        print(f"  P-value: {p_value:.4f}")
        print(f"  Significant (p<0.05): {'Yes' if p_value < 0.05 else 'No'}")

    def generate_report(self, output_file: str = "report.md"):
        """Generate markdown report"""
        aggregated = self.aggregate_by_variation()

        report = [
            f"# Experiment Report: {self.experiment_dir.name}",
            "",
            "## Summary Statistics",
            "",
            aggregated.to_markdown(),
            "",
            "## Success Rates",
            "",
            self.results.groupby("variation")["status"].value_counts().to_markdown(),
            "",
        ]

        with open(self.experiment_dir / output_file, "w") as f:
            f.write("\n".join(report))

        print(f"Report generated: {output_file}")
```

### Analysis Notebook Template

**File:** `experiments/templates/analysis.ipynb.template`

```python
# Cell 1: Setup
import sys
sys.path.append("../../test-harness/lib")

from experiment_analyzer import ExperimentAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Cell 2: Load results
analyzer = ExperimentAnalyzer(".")
results = analyzer.results

print(f"Loaded {len(results)} trial results")
print(f"Variations: {results['variation'].unique()}")

# Cell 3: Aggregate statistics
aggregated = analyzer.aggregate_by_variation()
print(aggregated)

# Cell 4: Plot latency comparison
analyzer.plot_comparison("completion_time_ms")

# Cell 5: Plot message count comparison
analyzer.plot_comparison("message_count")

# Cell 6: Statistical test
analyzer.statistical_test(
    "completion_time_ms",
    "Cue-Based Coordination",
    "Event-Driven"
)

# Cell 7: Success rate analysis
success_rates = results.groupby("variation")["status"].value_counts(normalize=True)
print(success_rates)

# Cell 8: Generate report
analyzer.generate_report()
```

---

## Part 3: Reproducibility Checklist

### Configuration Capture

**Auto-capture in experiment runner:**
```python
def capture_environment():
    """Capture reproducibility metadata"""
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "git_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"]
        ).decode().strip(),
        "git_dirty": subprocess.call(["git", "diff-index", "--quiet", "HEAD"]) != 0,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "working_directory": os.getcwd(),
    }
```

**Stored in summary.json:**
```json
{
  "experiment_id": "EXP-001",
  "environment": {
    "python_version": "3.13.0",
    "platform": "Darwin-24.6.0-arm64",
    "git_commit": "ad3f49a",
    "git_dirty": false,
    "timestamp": "2026-01-21T10:00:00.000Z",
    "working_directory": "/Users/user/AgentModel"
  }
}
```

### Random Seed Management

**In config.yaml:**
```yaml
# Random seed for reproducibility
random_seed: 42

# Or null for non-deterministic
random_seed: null
```

**In experiment runner:**
```python
import random
import numpy as np

def set_seed(seed):
    """Set all random seeds"""
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
        # Add other libraries as needed

# In run_single()
set_seed(self.config.get("random_seed"))
```

### Data Versioning

**Approach 1: Git LFS for large files**
```bash
# Track test data with Git LFS
git lfs track "test-harness/data/**/*.json"
git add .gitattributes
git add test-harness/data/
git commit -m "Add test data v1"
git tag data-v1
```

**Approach 2: Data manifest**
```yaml
# experiments/exp-001/data-manifest.yaml
data_sources:
  - path: "test-harness/data/task-s1/"
    checksum: "sha256:abc123..."
    created: "2026-01-21"
    description: "100 text files for map-reduce task"
```

---

## Part 4: Comparison Workflow

### Step-by-Step Process

**1. Run experiment:**
```bash
cd experiments/exp-001-coordination-comparison/
python ../../test-harness/lib/experiment_runner.py config.yaml
```

**2. Analyze results:**
```bash
jupyter notebook analysis.ipynb
```

**3. Generate report:**
```python
# In notebook or script
analyzer = ExperimentAnalyzer(".")
analyzer.generate_report()
```

**4. Compare experiments:**
```python
# Cross-experiment comparison
from experiment_analyzer import compare_experiments

compare_experiments([
    "experiments/exp-001-coordination-comparison/",
    "experiments/exp-002-scale-test/"
], metric="completion_time_ms")
```

### Visualization Examples

**Box plot comparison:**
```python
df = analyzer.results
metric_data = pd.json_normalize(df["metrics"])
df_with_metrics = pd.concat([df[["variation"]], metric_data], axis=1)

sns.boxplot(data=df_with_metrics, x="variation", y="completion_time_ms")
plt.title("Latency Comparison")
plt.show()
```

**Scatter plot (2 metrics):**
```python
sns.scatterplot(
    data=df_with_metrics,
    x="completion_time_ms",
    y="message_count",
    hue="variation",
    style="variation"
)
plt.title("Latency vs Message Count")
plt.show()
```

**Heatmap (variation × metric):**
```python
pivot = df_with_metrics.groupby("variation").mean()
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd")
plt.title("Mean Metrics by Variation")
plt.show()
```

---

## Part 5: Key Recommendations

### Use Custom System Because:

1. **Simplicity:** ~200 lines of Python vs learning MLflow/W&B
2. **Speed:** Implement in 4 hours vs 2+ days integration
3. **Control:** Full customization, no framework constraints
4. **Privacy:** All data local, no cloud dependencies
5. **Git-friendly:** Text files (YAML, JSON, notebooks), not databases

### Don't Use ML Tools Because:

1. **Overkill:** We don't need model registry, hyperparameter optimization, team dashboards
2. **Learning curve:** Time better spent running experiments
3. **Dependencies:** Adds complexity (servers, accounts, databases)
4. **Misfit:** Designed for ML training loops, not agent coordination
5. **Cost:** Managed services have pricing, we don't need them

### Implementation Priority

**Week 1:**
1. YAML config schema (1 hour)
2. ExperimentRunner class (2 hours)
3. ExperimentAnalyzer class (2 hours)
4. Analysis notebook template (1 hour)

**Week 2:**
1. Run first experiment (EXP-001)
2. Iterate on analysis tools as needed
3. Add visualization functions
4. Document patterns

**Total effort:** ~10 hours to fully working system

---

## Conclusion

**Custom lightweight system is best fit for our needs.**

**Core components:**
- YAML config (experiment specification)
- JSON Lines metrics (timestamped events)
- JSON summary (aggregated results)
- pandas DataFrames (analysis)
- Jupyter notebooks (visualization)
- Git (versioning)

**Why this works:**
- Minimal learning curve (tools we know)
- Quick implementation (~10 hours total)
- Full control (modify as needed)
- Reproducible (config + git commits)
- Analyzable (pandas, matplotlib)
- Shareable (notebooks, reports)

**Status: READY TO IMPLEMENT**

---

## Sources

- [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/)
- [MLflow GitHub Repository](https://github.com/mlflow/mlflow)
- [MLflow Tracing for LLM Observability](https://mlflow.org/docs/latest/genai/tracing/)
- [Experiment Tracking with MLflow](https://mlflow.org/classical-ml/experiment-tracking)
- [Weights & Biases Experiment Tracking](https://wandb.ai/site/experiment-tracking/)
- [Weights & Biases Documentation](https://docs.wandb.ai/models/track)
- [ML Experiment Tracking Tools Comparison](https://dagshub.com/blog/best-8-experiment-tracking-tools-for-machine-learning-2023/)
- [Sacred vs Weights & Biases Alternatives](https://www.zenml.io/blog/weights-and-biases-alternatives)
