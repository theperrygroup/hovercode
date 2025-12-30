## Authentication

Hovercode uses token authentication. Every request sends:

```
Authorization: Token YOUR-TOKEN
```

In this library, you can provide a token:

- via `HOVERCODE_API_TOKEN`, or
- by passing `api_token=` to `HovercodeClient`.

