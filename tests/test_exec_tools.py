from delivery_team.tools.exec_tools import run_code, run_code_from_files


class TestRunCode:
    def test_successful_execution(self) -> None:
        result = run_code("print('hello')")
        assert result["stdout"] == "hello\n"
        assert result["exit_code"] == 0

    def test_runtime_error(self) -> None:
        result = run_code("raise RuntimeError('fail')")
        assert result["exit_code"] == 1
        assert "RuntimeError" in result["stderr"]

    def test_default_filename(self) -> None:
        result = run_code("print('ok')")
        assert result["exit_code"] == 0

    def test_custom_filename(self) -> None:
        result = run_code("print('custom')", filename="custom_script.py")
        assert result["stdout"] == "custom\n"


class TestRunCodeFromFiles:
    def test_single_file_success(self) -> None:
        result = run_code_from_files(
            files={"app.py": "print('from file')"},
            entry_point="app.py",
        )
        assert result["stdout"] == "from file\n"
        assert result["exit_code"] == 0

    def test_multi_file_with_import(self) -> None:
        result = run_code_from_files(
            files={
                "lib.py": "def greet(): return 'hello'",
                "main.py": "from lib import greet; print(greet())",
            },
            entry_point="main.py",
        )
        assert result["stdout"] == "hello\n"
        assert result["exit_code"] == 0

    def test_entry_point_not_found(self) -> None:
        result = run_code_from_files(
            files={"app.py": "print('ok')"},
            entry_point="missing.py",
        )
        assert result["exit_code"] == -1
        assert "not found" in result["stderr"]

    def test_nested_directory_structure(self) -> None:
        result = run_code_from_files(
            files={
                "package/__init__.py": "",
                "package/module.py": "VALUE = 42",
                "main.py": "from package.module import VALUE; print(VALUE)",
            },
            entry_point="main.py",
        )
        assert result["stdout"] == "42\n"
        assert result["exit_code"] == 0

    def test_runtime_error_in_entry(self) -> None:
        result = run_code_from_files(
            files={"fail.py": "1/0"},
            entry_point="fail.py",
        )
        assert result["exit_code"] == 1
        assert "ZeroDivisionError" in result["stderr"]
