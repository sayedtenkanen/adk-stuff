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
cp .env.example .env  # or edit .env with your API key
```

## Run

```bash
PYTHONPATH=src uv run adk web src/delivery_team
```

Open http://127.0.0.1:8000.

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
