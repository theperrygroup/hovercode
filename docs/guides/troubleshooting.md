## Troubleshooting

### Authentication errors

- Ensure you are using the correct token.
- Ensure `HOVERCODE_API_TOKEN` is set in your environment if you are not passing `api_token=`.

If you want to use a `.env` file, install the optional extra and enable it:

```bash
python -m pip install "hovercode[dotenv]"
```

```python
from hovercode import HovercodeClient

client = HovercodeClient(load_dotenv=True)
```

### Timeouts / transient errors

The client supports configurable timeouts and retries via:

- `HOVERCODE_TIMEOUT_SECONDS`
- `HOVERCODE_MAX_RETRIES`
- `HOVERCODE_RETRY_BACKOFF_SECONDS`

Example:

```bash
export HOVERCODE_TIMEOUT_SECONDS="20"
export HOVERCODE_MAX_RETRIES="5"
export HOVERCODE_RETRY_BACKOFF_SECONDS="0.5"
```

!!! note
    Retries are applied to transient server failures (500/502/503/504) and network
    exceptions. Rate limits (429) are **not** retried automatically.

### Understanding errors

All API errors inherit from `hovercode.exceptions.ApiError` and include:

- `status_code`: HTTP status code when applicable
- `response_data`: decoded JSON (or raw text) from the API

Common exception types:

- `AuthenticationError` (401)
- `ValidationError` (400)
- `NotFoundError` (404)
- `RateLimitError` (429)
- `ServerError` (5xx)
- `NetworkError` (connection/timeouts)

```python
from hovercode import ApiError, HovercodeClient

client = HovercodeClient()

try:
    client.hovercodes.get_hovercode("not-a-real-id")
except ApiError as exc:
    print(exc.status_code)
    print(exc.response_data)
```

### Common HTTP status codes

- **400 (ValidationError)**: invalid request body/params (e.g., missing required fields)
- **401 (AuthenticationError)**: missing/invalid token
- **404 (NotFoundError)**: wrong ID or resource doesn’t exist
- **429 (RateLimitError)**: too many requests; slow down and retry later
- **5xx (ServerError)**: transient Hovercode server issue; retries may succeed

### Debugging tips

- Print `exc.response_data` to see the upstream error payload.
- Confirm the workspace ID and QR code ID are correct (UUIDs).
- If `generate_png=True` feels slow, that’s expected (the API documents it as slower).
