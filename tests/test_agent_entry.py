from delivery_team import agent


class TestAgentEntry:
    def test_root_agent_exported(self) -> None:
        assert hasattr(agent, "root_agent")

    def test_root_agent_name(self) -> None:
        assert agent.root_agent.name == "delivery_coordinator"

    def test_all_exported(self) -> None:
        assert "root_agent" in agent.__all__
        assert len(agent.__all__) == 1
