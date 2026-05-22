from pathlib import Path
from typing import Any

from google.adk.tools import ToolContext


def read_file(path: str, ctx: ToolContext | None = None) -> dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        return {"error": f"File not found: {path}", "content": None}
    content = file_path.read_text()
    return {"path": path, "content": content}


def write_file(path: str, content: str, ctx: ToolContext | None = None) -> dict[str, Any]:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)
    return {"path": path, "status": "written"}
