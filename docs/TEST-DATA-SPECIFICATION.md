# Test Data Requirements Research

**Research Date:** 2026-01-21
**Purpose:** Specify data requirements for all test tasks and identify existing datasets

---

## Executive Summary

**Key findings:**
- **SWE-Bench:** Available with 2,294 tasks (full), 500 tasks (verified), 300 tasks (lite)
- **Existing datasets:** Sufficient for Task W1 (multi-file refactoring)
- **Synthetic generation:** Needed for Tasks S1, S2, H1-H3
- **Quick generation:** Python + Faker library (~2 hours implementation)

**Recommendation:** Use **SWE-Bench Lite for W1**, generate synthetic data for all other tasks

---

## Part 1: Existing Dataset Review

### SWE-Bench (Multi-File Code Tasks)

**Available via Hugging Face:**
```python
from datasets import load_dataset
swebench = load_dataset('princeton-nlp/SWE-bench', split='test')
```

**Variants:**
- **SWE-bench Full:** 2,294 tasks from 12 Python repositories
- **SWE-bench Lite:** 300 carefully selected tasks
- **SWE-bench Verified:** 500 human-verified samples
- **SWE-bench Pro:** 1,865 tasks across 41 professional repos

**Task characteristics:**
- Real GitHub issues
- Multi-file modifications (average 107 lines across 4+ files)
- Ground truth patches
- Test suites for validation

**Perfect for Task W1 (Multi-File Refactoring)**

**Licensing:** Research use (check specific terms)

**Sources:**
- [SWE-Bench GitHub](https://github.com/SWE-bench/SWE-bench)
- [Hugging Face Dataset](https://huggingface.co/datasets/princeton-nlp/SWE-bench)
- [Official Website](https://www.swebench.com/)

### Other Benchmarks (Not Immediately Useful)

**WebArena:** Web agent tasks (e-commerce, forums) - not file-based
**AgentBench:** Operating systems, databases - different domain
**GAIA:** General AI assistants - question answering focus

**Verdict:** SWE-Bench is sufficient, others don't match our task types

---

## Part 2: Synthetic Data Generation

### Task S1: Parallel File Processing (Map-Reduce)

**Requirements:**
- 100 text files (varying sizes: 1KB - 100KB)
- Content: Mixed (code, prose, structured data)
- Expected output: Keyword extraction, word counts

**Generation script:**
```python
# test-harness/data/generate_task_s1_data.py
from faker import Faker
import random
import json
from pathlib import Path

fake = Faker()
Faker.seed(42)  # Reproducible

output_dir = Path("test-harness/data/task-s1/")
output_dir.mkdir(parents=True, exist_ok=True)

for i in range(100):
    # Vary content type
    content_type = random.choice(["code", "prose", "data"])

    if content_type == "code":
        # Generate Python-like code
        content = "\\n".join([
            f"def function_{j}({', '.join(fake.words(3))}):",
            f"    {fake.sentence()}",
            f"    return {fake.word()}"
            for j in range(random.randint(10, 50))
        ])
    elif content_type == "prose":
        # Generate paragraphs
        content = "\\n\\n".join([
            fake.paragraph(nb_sentences=random.randint(3, 10))
            for _ in range(random.randint(5, 20))
        ])
    else:  # data
        # Generate JSON data
        content = json.dumps([
            {
                "id": fake.uuid4(),
                "name": fake.name(),
                "email": fake.email(),
                "text": fake.sentence()
            }
            for _ in range(random.randint(10, 100))
        ], indent=2)

    # Write file
    filename = f"file_{i:03d}_{content_type}.txt"
    (output_dir / filename).write_text(content)

print(f"Generated 100 files in {output_dir}")
```

**Ground truth:** Generate expected keyword counts separately

**Time estimate:** 1 hour implementation, <1 minute generation

### Task S2: Sequential ETL Pipeline

**Requirements:**
- Source data: JSON records (1000 records)
- Transform: Clean, normalize, enrich
- Validation: Schema compliance
- Output: Validated JSON

**Generation script:**
```python
# test-harness/data/generate_task_s2_data.py
import json
from faker import Faker

fake = Faker()
Faker.seed(42)

# Generate source data with intentional issues
data = []
for i in range(1000):
    record = {
        "id": i,
        "name": fake.name() if random.random() > 0.05 else None,  # 5% missing
        "email": fake.email() if random.random() > 0.03 else "invalid",  # 3% invalid
        "age": random.randint(18, 80) if random.random() > 0.02 else -1,  # 2% invalid
        "created_at": fake.iso8601()
    }
    data.append(record)

output_file = Path("test-harness/data/task-s2/source_data.json")
output_file.parent.mkdir(parents=True, exist_ok=True)
output_file.write_text(json.dumps(data, indent=2))

print(f"Generated {len(data)} records")
```

**Ground truth:** Clean version with known transformations

**Time estimate:** 30 minutes implementation

### Task W2: High-Coordination Multi-Agent

**Requirements:**
- Resource allocation problem: 20 tasks, 5 shared resources
- Constraints: Task durations, resource requirements, deadlines
- Optimal solution: Known (computed separately)

**Generation script:**
```python
# test-harness/data/generate_task_w2_data.py
import json
import random

random.seed(42)

# Generate problem instance
tasks = []
for i in range(20):
    tasks.append({
        "id": f"TASK-{i:03d}",
        "duration_min": random.randint(5, 30),
        "resources_required": random.sample(["R1", "R2", "R3", "R4", "R5"], k=random.randint(1, 3)),
        "priority": random.choice(["high", "medium", "low"]),
        "deadline_min": random.randint(60, 180)
    })

problem = {
    "tasks": tasks,
    "resources": ["R1", "R2", "R3", "R4", "R5"],
    "constraints": {
        "exclusive_access": True,  # Resources can't be shared simultaneously
        "total_time_limit": 180  # 3 hours
    }
}

output_file = Path("test-harness/data/task-w2/problem_instance.json")
output_file.parent.mkdir(parents=True, exist_ok=True)
output_file.write_text(json.dumps(problem, indent=2))

# Compute optimal solution (greedy approximation)
optimal_schedule = compute_optimal(problem)  # Implement scheduler
output_file.parent.joinpath("optimal_solution.json").write_text(
    json.dumps(optimal_schedule, indent=2)
)
```

**Time estimate:** 2 hours (includes scheduler implementation)

### Tasks H1-H3

**H1 (Parallel + Sync):** Reuse S1 data, add verification step
**H2 (Error Recovery):** Reuse S2 data, inject failures programmatically
**H3 (Context Building):** Reuse SWE-Bench sample, track context growth

**Time estimate:** 1 hour (mostly configuration, not generation)

---

## Part 3: Data Storage Structure

```
test-harness/data/
├── task-s1-map-reduce/
│   ├── files/
│   │   ├── file_000_code.txt
│   │   ├── file_001_prose.txt
│   │   └── ...
│   ├── expected_output.json
│   └── README.md
├── task-s2-pipeline/
│   ├── source_data.json
│   ├── expected_clean.json
│   └── schema.json
├── task-w1-refactoring/
│   ├── swebench_lite/  # Symlink or download
│   └── selected_tasks.json  # 10 tasks we'll use
├── task-w2-coordination/
│   ├── problem_instance.json
│   ├── optimal_solution.json
│   └── README.md
└── generators/
    ├── generate_all.py  # Run all generators
    ├── generate_task_s1_data.py
    ├── generate_task_s2_data.py
    └── generate_task_w2_data.py
```

---

## Part 4: Data Versioning

**Approach:** Git + manifest files

```yaml
# test-harness/data/DATA-MANIFEST.yaml
version: "1.0"
created: "2026-01-21"
generator_commit: "ad3f49a"

datasets:
  - name: "task-s1-map-reduce"
    path: "task-s1-map-reduce/"
    checksum: "sha256:abc123..."
    file_count: 100
    total_size_mb: 5.2
    description: "100 text files for parallel processing"

  - name: "task-s2-pipeline"
    path: "task-s2-pipeline/"
    checksum: "sha256:def456..."
    record_count: 1000
    description: "JSON records for ETL pipeline"

  - name: "task-w1-refactoring"
    path: "task-w1-refactoring/"
    source: "SWE-bench Lite"
    version: "2025-01"
    task_count: 10
    description: "Selected SWE-bench tasks"
```

**Update manifest after generation:**
```bash
cd test-harness/data
python update_manifest.py  # Computes checksums, counts, sizes
git add DATA-MANIFEST.yaml
git commit -m "Update data manifest v1.0"
```

---

## Part 5: Implementation Plan

**Week 1 (Data Generation):**

**Day 1: Task S1**
- Implement `generate_task_s1_data.py` (1 hour)
- Generate 100 files (<1 minute)
- Create expected output (30 min)
- Test: Can we process the files? (30 min)

**Day 2: Task S2**
- Implement `generate_task_s2_data.py` (30 min)
- Generate source data (<1 minute)
- Create expected output (30 min)
- Define schema (30 min)

**Day 3: Task W1**
- Download SWE-bench Lite (10 min)
- Select 10 representative tasks (1 hour)
- Document selection criteria (30 min)

**Day 4: Task W2**
- Implement problem generator (1 hour)
- Implement optimal scheduler (1 hour)
- Generate instances (5 min)

**Day 5: Verification**
- Run all generators with `generate_all.py` (30 min)
- Update manifest (30 min)
- Document usage in READMEs (1 hour)
- Commit to git (10 min)

**Total effort:** ~10 hours

---

## Conclusion

**Data requirements are straightforward and achievable.**

**Summary:**
- **Existing:** SWE-Bench Lite for Task W1 (multi-file refactoring)
- **Generated:** Python + Faker for Tasks S1, S2, W2, H1-H3
- **Storage:** Git-friendly text files with manifest
- **Versioning:** Git commits + checksums
- **Time:** ~10 hours to generate all data

**Status: READY TO IMPLEMENT**

---

## Sources

- [SWE-Bench GitHub Repository](https://github.com/SWE-bench/SWE-bench)
- [SWE-Bench Datasets Documentation](https://www.swebench.com/SWE-bench/guides/datasets/)
- [SWE-Bench on Hugging Face](https://huggingface.co/datasets/princeton-nlp/SWE-bench)
- [SWE-Bench Lite](https://www.swebench.com/lite.html)
- [SWE-Bench Pro Public Dataset](https://scale.com/leaderboard/swe_bench_pro_public)
