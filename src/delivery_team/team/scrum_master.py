import os

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from delivery_team.schemas import SprintBacklog

model = os.getenv("ZEN_MODEL", "openai/deepseek-v4-flash-free")

scrum_master_agent = Agent(
    name="scrum_master",
    model=LiteLlm(model=model),
    mode="task",
    output_schema=SprintBacklog,
    instruction=(
        "You are a Scrum Master. "
        "Given the architecture plan, break the work into a sprint backlog. "
        "Create TaskItems with: id, description, assignee, and effort_hours. "
        "Return a SprintBacklog containing all the tasks. "
        "If you need clarification, ask the coordinator."
    ),
)
