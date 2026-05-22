import os

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

model = os.getenv("ZEN_MODEL", "openai/deepseek-v4-flash-free")

product_owner_agent = Agent(
    name="product_owner",
    model=LiteLlm(model=model),
    mode="chat",
    instruction=(
        "You are a Product Owner in a software delivery team. "
        "Your job is to elicit feature requirements from the user. "
        "Ask clarifying questions to understand what they want to build. "
        "Write user stories with clear acceptance criteria. "
        "After you have a clear understanding, summarize the requirements "
        "including: feature name, description, and acceptance criteria. "
        "Hand off to the Architect agent when requirements are clear."
    ),
)
