import pytest
from pydantic import ValidationError

from delivery_team.schemas import (
    ArchitecturePlan,
    CodeOutput,
    RequirementInput,
    SprintBacklog,
    TaskItem,
    TestResult,
)


class TestRequirementInput:
    def test_valid(self) -> None:
        data = RequirementInput(
            feature="login",
            description="User login feature",
            acceptance_criteria=["must support email", "must validate password"],
        )
        assert data.feature == "login"
        assert data.description == "User login feature"
        assert len(data.acceptance_criteria) == 2

    def test_missing_field(self) -> None:
        with pytest.raises(ValidationError):
            RequirementInput()


class TestArchitecturePlan:
    def test_valid(self) -> None:
        data = ArchitecturePlan(
            components=[{"name": "api", "resp": "handle requests"}],
            tech_stack=["python", "fastapi"],
            data_flow="request -> api -> db",
        )
        assert len(data.components) == 1
        assert "python" in data.tech_stack
        assert data.data_flow == "request -> api -> db"


class TestTaskItem:
    def test_valid(self) -> None:
        item = TaskItem(id="T1", description="Build API", assignee="dev", effort_hours=5)
        assert item.id == "T1"
        assert item.effort_hours == 5


class TestSprintBacklog:
    def test_valid(self) -> None:
        backlog = SprintBacklog(
            tasks=[
                TaskItem(id="T1", description="Task 1", assignee="dev1", effort_hours=3),
                TaskItem(id="T2", description="Task 2", assignee="dev2", effort_hours=5),
            ]
        )
        assert len(backlog.tasks) == 2

    def test_empty_tasks(self) -> None:
        backlog = SprintBacklog(tasks=[])
        assert backlog.tasks == []


class TestCodeOutput:
    def test_valid_with_all_fields(self) -> None:
        output = CodeOutput(
            files={"main.py": "print('hello')"},
            execution_result="hello\n",
            exit_code=0,
        )
        assert "main.py" in output.files
        assert output.execution_result == "hello\n"
        assert output.exit_code == 0

    def test_valid_with_nullable_fields(self) -> None:
        output = CodeOutput(files={}, execution_result=None, exit_code=None)
        assert output.files == {}
        assert output.execution_result is None
        assert output.exit_code is None


class TestTestResult:
    def test_valid(self) -> None:
        result = TestResult(passed=5, failed=0, log="all tests passed")
        assert result.passed == 5
        assert result.failed == 0
        assert result.log == "all tests passed"

    def test_all_failed(self) -> None:
        result = TestResult(passed=0, failed=3, log="3 failures")
        assert result.passed == 0
        assert result.failed == 3
