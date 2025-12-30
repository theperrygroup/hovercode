## Authentication

Hovercode uses token authentication. Every API request includes:

```
Authorization: Token YOUR-TOKEN
```

### Where to find your token and workspace ID

You can find your **API token** (and your **workspace ID**) in your Hovercode settings area
while logged in.

Treat this token like a password:

- Do not commit it to git
- Do not expose it in a browser/front-end app
- Prefer environment variables or a secrets manager

### Provide your token to the SDK

In this SDK, you can provide a token either:

- via `HOVERCODE_API_TOKEN`, or
- by passing `api_token=` to `HovercodeClient`.

### Environment variable (recommended)

```bash
export HOVERCODE_API_TOKEN="YOUR-TOKEN"
```

```python
from hovercode import HovercodeClient

client = HovercodeClient()
```

### Constructor argument

```python
from hovercode import HovercodeClient

client = HovercodeClient(api_token="YOUR-TOKEN")
```

### `.env` support (optional)

If you prefer using a `.env` file, install the optional extra:

```bash
python -m pip install "hovercode[dotenv]"
```

Then:

```python
from hovercode import HovercodeClient

client = HovercodeClient(load_dotenv=True)
```

### Timeouts and retries

The HTTP client supports configurable timeouts and retries. You can set these via
environment variables (recommended for production deployments):

- `HOVERCODE_TIMEOUT_SECONDS` (default: `10.0`)
- `HOVERCODE_MAX_RETRIES` (default: `3`)
- `HOVERCODE_RETRY_BACKOFF_SECONDS` (default: `0.5`)

```bash
export HOVERCODE_TIMEOUT_SECONDS="20"
export HOVERCODE_MAX_RETRIES="5"
export HOVERCODE_RETRY_BACKOFF_SECONDS="0.5"
```

Or pass them in code:

```python
from hovercode import HovercodeClient

client = HovercodeClient(timeout_seconds=20.0, max_retries=5, retry_backoff_seconds=0.5)
```
