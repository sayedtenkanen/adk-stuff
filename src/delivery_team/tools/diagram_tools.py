import base64
import json
import webbrowser
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
        "html_path": None,
        "rendered": False,
    }
    try:
        body = json.dumps({"diagram_source": code}).encode()
        req = Request(
            "https://kroki.io/mermaid/png",
            data=body,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "delivery-team/1.0",
            },
        )
        with urlopen(req, timeout=30) as resp:  # nosec
            png_bytes = resp.read()
        html_path = file_path.with_suffix(".html")
        html_path.write_text(
            f"<html><body><img src='data:image/png;base64,"
            f"{base64.b64encode(png_bytes).decode()}'/></body></html>"
        )
        result["html_path"] = str(html_path)
        result["rendered"] = True
        webbrowser.open(f"file://{html_path.resolve()}")
    except Exception:  # nosec  # pragma: no cover
        pass
    return result
