# Delivery Team

Multi-agent software delivery team built with Google ADK 2.0.

## Agents

| Agent | Mode | Role |
|---|---|---|
| Product Owner | chat | Clarifies requirements |
| Architect | single_turn | Produces architecture plan |
| Scrum Master | task | Breaks plan into sprint backlog |
| Developer | task | Writes and runs code |
| QA Engineer | task | Writes and runs tests |

## Setup

```bash
uv venv && uv sync
uv run pre-commit install
cp .env.example .env  # or edit .env with your provider
```

## Provider Setup

### GitHub Copilot (recommended)
```env
ZEN_MODEL="github_copilot/gpt-4o"
```
No API key needed. On first LLM call, LiteLLM will open a browser for GitHub OAuth device flow authentication. Supported models include `github_copilot/gpt-4o`, `github_copilot/claude-sonnet-4.5`, etc.

### OpenCode Zen (fallback)
```env
OPENAI_API_KEY="your-key"
OPENAI_BASE_URL="https://opencode.ai/zen/v1"
ZEN_MODEL="openai/deepseek-v4-flash-free"
```

## Run

```bash
PYTHONPATH=src uv run adk web src
```

Open http://127.0.0.1:8000. The app will appear as **`delivery_team`** in the UI.

> **Note:** If you get a `RateLimitError` / `FreeUsageLimitError`, the API key's rate limit has been exceeded. Wait a moment and retry, or use a different provider.

## Test

```bash
uv run pytest --cov --cov-report=term-missing
```

## Pre-commit

- `ruff` lint + auto-fix
- `ruff-format`
- `ty` type checking
- `pytest --cov --cov-fail-under=100`
- `secrets` — scans staged files for API keys, tokens, private keys
- `bandit` — static security analysis for Python code
- `pip-audit` — scans dependencies for known CVEs
