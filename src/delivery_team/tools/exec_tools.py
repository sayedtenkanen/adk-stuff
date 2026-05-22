import subprocess
import tempfile
from pathlib import Path
from typing import Any


def run_code(code: str, filename: str = "script.py") -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / filename
        file_path.write_text(code)
        result = subprocess.run(
            ["python", str(file_path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
        }


def run_code_from_files(files: dict[str, str], entry_point: str) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        for path, content in files.items():
            full_path = base / path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content)
        entry_path = base / entry_point
        if not entry_path.exists():
            return {
                "stdout": "",
                "stderr": f"Entry point not found: {entry_point}",
                "exit_code": -1,
            }
        result = subprocess.run(
            ["python", str(entry_path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
        }
