import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
jobs = []

def first_added(path):
    """Read the first commit that added this vacancy, not its latest edit."""
    relative = path.relative_to(root).as_posix()
    result = subprocess.run(
        ["git", "log", "--follow", "--diff-filter=A", "--format=%aI", "--", relative],
        cwd=root, capture_output=True, text=True, check=True
    )
    dates = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return min(dates) if dates else ""

for path in (root / "data/jobs").glob("*.json"):
    job = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(job, dict) or not job.get("id") or not job.get("title"):
        raise ValueError(f"Invalid job: {path}")
    job["postedAt"] = first_added(path)
    jobs.append(job)

jobs.sort(key=lambda job: (job["postedAt"], job["id"]), reverse=True)
(root / "data/jobs-index.json").write_text(
    json.dumps(jobs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(f"Indexed {len(jobs)} jobs, newest first")
