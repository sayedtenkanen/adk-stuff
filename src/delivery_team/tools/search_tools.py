from typing import Any

from ddgs import DDGS


def web_search(query: str, max_results: int = 5) -> dict[str, Any]:
    if not query.strip():
        return {"query": query, "results": []}
    results = list(DDGS().text(query, max_results=max_results))
    return {
        "query": query,
        "results": [
            {"title": r.get("title"), "url": r.get("href"), "snippet": r.get("body")}
            for r in results
        ],
    }
