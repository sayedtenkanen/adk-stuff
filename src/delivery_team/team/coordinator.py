import os

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from delivery_team.team.architect import architect_agent
from delivery_team.team.developer import developer_agent
from delivery_team.team.product_owner import product_owner_agent
from delivery_team.team.qa_engineer import qa_engineer_agent
from delivery_team.team.scrum_master import scrum_master_agent
from delivery_team.tools.diagram_tools import render_mermaid
from delivery_team.tools.search_tools import web_search

model = os.getenv("ZEN_MODEL", "openai/deepseek-v4-flash-free")

root_agent = Agent(
    name="delivery_coordinator",
    model=LiteLlm(model=model),
    instruction=(
        "You are the Delivery Coordinator for a software development team. "
        "Your team includes:\n"
        "- Product Owner: clarifies requirements with the user\n"
        "- Architect: designs the system architecture\n"
        "- Scrum Master: breaks work into tasks\n"
        "- Developer: writes the code\n"
        "- QA Engineer: tests the code\n\n"
        "When a user requests a feature:\n"
        "1. First delegate to the Product Owner to clarify requirements\n"
        "2. Pass the requirements to the Architect for design\n"
        "3. Pass the architecture to the Scrum Master for task breakdown\n"
        "4. Pass each task to the Developer for implementation\n"
        "5. Pass the code to the QA Engineer for testing\n"
        "6. Report the results back to the user\n\n"
        "You have the web_search tool to look up documentation, APIs, "
        "or best practices when needed.\n"
        "You have the render_mermaid tool to generate architecture diagrams "
        "and flowcharts as PNG images. "
        "After calling render_mermaid, copy the 'display' value from the result "
        "onto its own line in your response. Do not modify it.\n\n"
        "Keep the user updated on progress throughout."
    ),
    sub_agents=[
        product_owner_agent,
        architect_agent,
        scrum_master_agent,
        developer_agent,
        qa_engineer_agent,
    ],
    tools=[web_search, render_mermaid],
)
