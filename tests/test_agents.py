from google.adk.agents.llm_agent import Agent as LlmAgent

from delivery_team.team.architect import architect_agent
from delivery_team.team.coordinator import root_agent
from delivery_team.team.developer import developer_agent
from delivery_team.team.product_owner import product_owner_agent
from delivery_team.team.qa_engineer import qa_engineer_agent
from delivery_team.team.scrum_master import scrum_master_agent


class TestProductOwnerAgent:
    def test_name(self) -> None:
        assert product_owner_agent.name == "product_owner"

    def test_mode(self) -> None:
        assert product_owner_agent.mode == "chat"

    def test_has_instruction(self) -> None:
        assert len(product_owner_agent.instruction) > 0


class TestArchitectAgent:
    def test_name(self) -> None:
        assert architect_agent.name == "architect"

    def test_mode(self) -> None:
        assert architect_agent.mode == "single_turn"

    def test_has_output_schema(self) -> None:
        from delivery_team.schemas import ArchitecturePlan

        assert architect_agent.output_schema is ArchitecturePlan

    def test_has_instruction(self) -> None:
        assert len(architect_agent.instruction) > 0


class TestScrumMasterAgent:
    def test_name(self) -> None:
        assert scrum_master_agent.name == "scrum_master"

    def test_mode(self) -> None:
        assert scrum_master_agent.mode == "task"

    def test_has_output_schema(self) -> None:
        from delivery_team.schemas import SprintBacklog

        assert scrum_master_agent.output_schema is SprintBacklog

    def test_has_instruction(self) -> None:
        assert len(scrum_master_agent.instruction) > 0


class TestDeveloperAgent:
    def test_name(self) -> None:
        assert developer_agent.name == "developer"

    def test_mode(self) -> None:
        assert developer_agent.mode == "task"

    def test_has_output_schema(self) -> None:
        from delivery_team.schemas import CodeOutput

        assert developer_agent.output_schema is CodeOutput

    def test_has_tools(self) -> None:
        user_tools = [
            t for t in developer_agent.tools if not t.__class__.__name__.endswith("FinishTaskTool")
        ]
        assert len(user_tools) == 3

    def test_has_instruction(self) -> None:
        assert len(developer_agent.instruction) > 0


class TestQAEngineerAgent:
    def test_name(self) -> None:
        assert qa_engineer_agent.name == "qa_engineer"

    def test_mode(self) -> None:
        assert qa_engineer_agent.mode == "task"

    def test_has_output_schema(self) -> None:
        from delivery_team.schemas import TestResult

        assert qa_engineer_agent.output_schema is TestResult

    def test_has_tools(self) -> None:
        user_tools = [
            t
            for t in qa_engineer_agent.tools
            if not t.__class__.__name__.endswith("FinishTaskTool")
        ]
        assert len(user_tools) == 4

    def test_has_instruction(self) -> None:
        assert len(qa_engineer_agent.instruction) > 0


class TestCoordinator:
    def test_name(self) -> None:
        assert root_agent.name == "delivery_coordinator"

    def test_is_llm_agent(self) -> None:
        assert isinstance(root_agent, LlmAgent)

    def test_has_instruction(self) -> None:
        assert len(root_agent.instruction) > 0

    def test_has_all_sub_agents(self) -> None:
        names = [a.name for a in root_agent.sub_agents]
        assert "product_owner" in names
        assert "architect" in names
        assert "scrum_master" in names
        assert "developer" in names
        assert "qa_engineer" in names

    def test_sub_agent_count(self) -> None:
        assert len(root_agent.sub_agents) == 5

    def test_has_web_search_tool(self) -> None:
        assert any(t.__name__ == "web_search" for t in root_agent.tools)

    def test_has_render_mermaid_tool(self) -> None:
        assert any(t.__name__ == "render_mermaid" for t in root_agent.tools)
