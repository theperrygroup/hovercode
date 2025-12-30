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

::: hovercode.exceptions

