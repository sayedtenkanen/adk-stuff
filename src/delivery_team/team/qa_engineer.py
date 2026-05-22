import os

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from delivery_team.schemas import TestResult
from delivery_team.tools.exec_tools import run_code, run_code_from_files
from delivery_team.tools.file_tools import read_file, write_file

model = os.getenv("ZEN_MODEL", "openai/deepseek-v4-flash-free")

qa_engineer_agent = Agent(
    name="qa_engineer",
    model=LiteLlm(model=model),
    mode="task",
    output_schema=TestResult,
    tools=[read_file, write_file, run_code, run_code_from_files],
    instruction=(
        "You are a QA Engineer. "
        "Given the code from the Developer, "
        "write and run tests to verify correctness. "
        "Use the write_file tool to save your tests. "
        "Use the run_code tool to execute them. "
        "Iterate on any test failures. "
        "Return a TestResult with pass/fail counts and the test log."
    ),
)
