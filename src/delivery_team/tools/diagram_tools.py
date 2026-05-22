import base64
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
        "png_path": None,
        "display": None,
        "rendered": False,
    }
    try:
        png_path = file_path.with_suffix(".png")
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
            png_path.write_bytes(png_bytes)
        result["png_path"] = str(png_path)
        data_uri = "data:image/png;base64," + base64.b64encode(png_bytes).decode()
        result["display"] = f"![diagram]({data_uri})"
        result["rendered"] = True
    except Exception:  # nosec  # pragma: no cover
        pass
    return result
