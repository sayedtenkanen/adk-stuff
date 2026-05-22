from delivery_team.tools.search_tools import web_search


class TestWebSearch:
    def test_returns_dict_with_keys(self) -> None:
        result = web_search("Python programming", max_results=2)
        assert isinstance(result, dict)
        assert "query" in result
        assert "results" in result
        assert result["query"] == "Python programming"

    def test_default_max_results(self) -> None:
        result = web_search("test")
        assert len(result["results"]) <= 5

    def test_empty_query_returns_empty_results(self) -> None:
        result = web_search("")
        assert result["results"] == []
