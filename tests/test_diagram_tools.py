from pathlib import Path

from delivery_team.tools.diagram_tools import render_mermaid


class TestRenderMermaid:
    def test_writes_mmd_file(self, tmp_path: Path) -> None:
        code = "graph TD; A-->B;"
        output = tmp_path / "test.mmd"
        result = render_mermaid(code, str(output))
        assert result["mmd_path"] == str(output)
        assert output.exists()
        assert output.read_text() == code

    def test_returns_png_path_on_render(self, tmp_path: Path) -> None:
        code = "graph TD; A-->B;"
        output = tmp_path / "diagram.mmd"
        result = render_mermaid(code, str(output))
        assert "png_path" in result
        assert "rendered" in result

    def test_creates_parent_directories(self, tmp_path: Path) -> None:
        code = "graph TD; A-->B;"
        output = tmp_path / "nested" / "sub" / "test.mmd"
        result = render_mermaid(code, str(output))
        assert Path(result["mmd_path"]).exists()
