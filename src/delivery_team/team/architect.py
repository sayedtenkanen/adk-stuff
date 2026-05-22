import os

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from delivery_team.schemas import ArchitecturePlan

model = os.getenv("ZEN_MODEL", "openai/deepseek-v4-flash-free")

architect_agent = Agent(
    name="architect",
    model=LiteLlm(model=model),
    mode="single_turn",
    output_schema=ArchitecturePlan,
    instruction=(
        "You are a Software Architect. "
        "Given the requirements from the Product Owner, "
        "design a system architecture. "
        "Return an ArchitecturePlan with: "
        "- components: list of components and their responsibilities "
        "- tech_stack: recommended technologies "
        "- data_flow: how data flows through the system "
        "Be specific and practical."
    ),
)
