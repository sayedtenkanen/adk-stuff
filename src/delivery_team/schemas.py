from pydantic import BaseModel


class RequirementInput(BaseModel):
    feature: str
    description: str
    acceptance_criteria: list[str]


class ArchitecturePlan(BaseModel):
    components: list[dict[str, str]]
    tech_stack: list[str]
    data_flow: str


class TaskItem(BaseModel):
    id: str
    description: str
    assignee: str
    effort_hours: int


class SprintBacklog(BaseModel):
    tasks: list[TaskItem]


class CodeOutput(BaseModel):
    files: dict[str, str]
    execution_result: str | None
    exit_code: int | None


class TestResult(BaseModel):
    passed: int
    failed: int
    log: str
