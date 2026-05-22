# Delivery Team

Multi-agent software delivery team built with Google ADK 2.0.

## Agents

| Agent | Mode | Role | Tools |
|---|---|---|---|
| **Coordinator** | multi-agent | Orchestrates the delivery pipeline | `web_search`, `render_mermaid` |
| Product Owner | chat | Clarifies requirements | — |
| Architect | single_turn | Produces architecture plan | — |
| Scrum Master | task | Breaks plan into sprint backlog | — |
| Developer | task | Writes and runs code | `read_file`, `write_file`, `run_code` |
| QA Engineer | task | Writes and runs tests | `read_file`, `write_file`, `run_code`, `run_code_from_files` |

### Tool Details

| Tool | Description |
|---|---|
| `web_search(query, max_results=5)` | Web search via DuckDuckGo (no API key). Returns title, URL, snippet. |
| `render_mermaid(code, output_path)` | Generates a diagram from Mermaid syntax. Renders to PNG via Kroki.io, saves an HTML file, and opens it in the browser. |
| `read_file(path)` | Reads a file from disk. |
| `write_file(path, content)` | Writes a file to disk (creates parent directories). |
| `run_code(code, filename)` | Executes Python code in an isolated temp directory (30s timeout). |
| `run_code_from_files(files, entry_point)` | Executes a multi-file Python project in a temp directory. |

## Setup

```bash
uv venv && uv sync
uv run pre-commit install
cp .env.example .env   # then edit .env with your provider
```

## Provider Setup

### GitHub Copilot (recommended)
```env
ZEN_MODEL="github_copilot/gpt-4"
```
No API key needed. On first LLM call, LiteLLM will open a browser for GitHub OAuth device flow authentication. Models include `github_copilot/gpt-4`, `github_copilot/claude-sonnet-4.5`, `github_copilot/gpt-5.4-mini`, etc.

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

100% branch coverage is enforced.

```bash
uv run pytest --cov --cov-report=term-missing
```

## Pre-commit

- `ruff` lint + auto-fix
- `ruff-format`
- `ty` strict type checking
- `pytest --cov --cov-fail-under=100` — 100% branch coverage required
- `secrets` — scans staged files for API keys, tokens, private keys
- `bandit` — static security analysis for Python code (skips subprocess/assert rules — intentional for code execution tools)
- `pip-audit` — scans dependencies for known CVEs. Suppressed: `PYSEC-2026-161` (starlette pinned by google-adk, unfixable without breaking compatibility)

## CI

GitHub Actions workflow in `.github/workflows/ci.yml` runs all checks on push/PR to `main`.
