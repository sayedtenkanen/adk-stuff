import json
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen


def render_mermaid(
    code: str,
    output_path: str,
) -> dict[str, Any]:
    file_path = Path(output_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(code)
    result = {
        "mmd_path": str(file_path),
        "svg_path": None,
        "rendered": False,
    }
    try:
        svg_path = file_path.with_suffix(".svg")
        body = json.dumps({"diagram_source": code}).encode()
        req = Request(
            "https://kroki.io/mermaid/svg",
            data=body,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "delivery-team/1.0",
            },
        )
        with urlopen(req, timeout=30) as resp:  # nosec
            svg_path.write_bytes(resp.read())
        result["svg_path"] = str(svg_path)
        result["rendered"] = True
    except Exception:  # nosec  # pragma: no cover
        pass
    return result
