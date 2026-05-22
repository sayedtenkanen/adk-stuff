import tempfile
from pathlib import Path

from delivery_team.tools.file_tools import read_file, write_file


class TestReadFile:
    def test_read_existing_file(self) -> None:
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
            f.write("hello world")
            tmp_path = f.name
        try:
            result = read_file(tmp_path)
            assert result["path"] == tmp_path
            assert result["content"] == "hello world"
            assert "error" not in result
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    def test_read_nonexistent_file(self) -> None:
        result = read_file("/nonexistent/path/file.txt")
        assert "error" in result
        assert result["content"] is None


class TestWriteFile:
    def test_write_creates_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "subdir" / "test.txt"
            result = write_file(str(path), "file content")
            assert result["status"] == "written"
            assert result["path"] == str(path)
            assert path.read_text() == "file content"

    def test_write_overwrites_existing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "existing.txt"
            path.write_text("old")
            write_file(str(path), "new content")
            assert path.read_text() == "new content"
