import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
jobs = []
for path in sorted((root / "data/jobs").glob("*.json")):
    job = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(job, dict) or not job.get("id") or not job.get("title"):
        raise ValueError(f"Invalid job: {path}")
    jobs.append(job)
(root / "data/jobs-index.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Indexed {len(jobs)} jobs")
