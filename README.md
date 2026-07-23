# AI Coding Assistant

Portfolio project for an AI-powered coding assistant API. The assistant can explain code, suggest refactors, detect bugs, generate unit-test ideas, create UML text, and summarize source files.

## Features

- Explain Code: describe purpose, inputs, outputs, and execution flow.
- Refactor: suggest clean-code improvements without changing behavior.
- Bug Detection: identify risky patterns and likely defects.
- Unit Test: propose practical test cases for the submitted code.
- UML: generate Mermaid class or flow diagrams from code.
- Code Summary: produce concise technical summaries.

## Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- Pytest
- Clean Architecture

## Project Structure

```text
portfolio-AI-Coding-Assistant/
├── app/
│   ├── api/                 # HTTP routes and request/response schemas
│   ├── application/         # Use cases and service orchestration
│   ├── domain/              # Entities, value objects, interfaces
│   ├── infrastructure/      # Analyzer implementations and adapters
│   ├── config.py            # App settings
│   └── main.py              # FastAPI app factory
├── docs/
│   ├── ARCHITECTURE.md
│   └── API.md
├── tests/
│   ├── unit/
│   └── integration/
├── requirements.txt
├── requirements-dev.txt
└── pytest.ini
```

## Getting Started

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open:

- API health: `http://127.0.0.1:8000/health`
- Swagger UI: `http://127.0.0.1:8000/docs`

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d "{\"task\":\"bug_detection\",\"language\":\"python\",\"code\":\"def divide(a,b): return a / b\"}"
```

## Supported Tasks

| Task | Value |
| --- | --- |
| Explain Code | `explain_code` |
| Refactor | `refactor` |
| Bug Detection | `bug_detection` |
| Unit Test | `unit_test` |
| UML | `uml` |
| Code Summary | `code_summary` |

## Run Tests

```bash
pytest
ruff check .
```

## Architecture

The code follows Clean Architecture:

- Domain has no FastAPI dependency.
- Application coordinates use cases.
- Infrastructure implements analyzers.
- API translates HTTP payloads into use-case calls.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for details.
