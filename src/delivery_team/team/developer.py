import os

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from delivery_team.schemas import CodeOutput
from delivery_team.tools.exec_tools import run_code
from delivery_team.tools.file_tools import read_file, write_file

model = os.getenv("ZEN_MODEL", "openai/deepseek-v4-flash-free")

developer_agent = Agent(
    name="developer",
    model=LiteLlm(model=model),
    mode="task",
    output_schema=CodeOutput,
    tools=[read_file, write_file, run_code],
    instruction=(
        "You are a Software Developer. "
        "Given a task from the sprint backlog, "
        "write the code to implement it. "
        "Use the write_file tool to save your code. "
        "Use the run_code tool to execute your code and check for errors. "
        "Iterate on any errors you encounter. "
        "When the code runs successfully, return a CodeOutput "
        "with the files you created and the execution result."
    ),
)
