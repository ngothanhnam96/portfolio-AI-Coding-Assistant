# Architecture

This project uses Clean Architecture to keep business logic independent from frameworks and external providers.

## Layers

```text
API -> Application -> Domain
             |
             v
      Infrastructure
```

## Responsibilities

| Layer | Responsibility |
| --- | --- |
| Domain | Core models, task types, analyzer interface |
| Application | Use cases and orchestration |
| Infrastructure | Static analyzer and future LLM provider adapters |
| API | FastAPI routing, validation, HTTP responses |

## Dependency Rule

Outer layers depend on inner layers. Inner layers do not import FastAPI, databases, SDK clients, or other delivery concerns.

## Extension Points

- Add a new task in `app/domain/models.py`.
- Implement analyzer behavior in `app/infrastructure/static_code_analyzer.py`.
- Register dependencies in `app/api/dependencies.py`.
- Add tests under `tests/unit` and `tests/integration`.

## Future Improvements

- Add OpenAI/Gemini provider behind the `CodeAnalyzer` protocol.
- Add repository upload and multi-file context.
- Add authentication and request history.
- Add frontend editor with Monaco.
