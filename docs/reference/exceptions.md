## Exceptions

All API-related errors inherit from `ApiError` and typically include:

- `status_code`: HTTP status code (if the error came from an HTTP response)
- `response_data`: parsed JSON (or raw text) returned by the API

For example:

```python
from hovercode import ApiError, HovercodeClient

client = HovercodeClient()

try:
    client.hovercodes.get_hovercode("not-a-real-id")
except ApiError as exc:
    print(exc.status_code)
    print(exc.response_data)
```

### Error mapping

The SDK maps HTTP status codes to exception types:

- 400 → `ValidationError`
- 401 → `AuthenticationError`
- 404 → `NotFoundError`
- 429 → `RateLimitError`
- 5xx → `ServerError`

Network/transport issues (DNS, timeouts, connection errors) raise `NetworkError`.

### Recommended handling patterns

- Catch **specific** errors when you want to branch logic (e.g., auth vs not found).
- Catch `ApiError` for a broad “any Hovercode failure” handler.

```python
from hovercode import AuthenticationError, HovercodeClient, NotFoundError

client = HovercodeClient()

try:
    client.hovercodes.get_hovercode("QR-CODE-ID")
except AuthenticationError:
    # Token missing/invalid
    raise
except NotFoundError:
    # Wrong QR code ID or it was deleted
    raise
```

::: hovercode.exceptions

