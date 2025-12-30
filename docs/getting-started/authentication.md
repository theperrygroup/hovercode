## Authentication

Hovercode uses token authentication. Every API request includes:

```
Authorization: Token YOUR-TOKEN
```

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
