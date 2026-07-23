# API

Base URL: `http://127.0.0.1:8000`

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok",
  "service": "AI Coding Assistant"
}
```

## Analyze Code

```http
POST /api/v1/analyze
```

Request:

```json
{
  "task": "explain_code",
  "language": "python",
  "code": "def add(a, b): return a + b",
  "file_name": "math_utils.py"
}
```

Response:

```json
{
  "task": "explain_code",
  "language": "python",
  "result": "...",
  "findings": [],
  "suggestions": []
}
```
