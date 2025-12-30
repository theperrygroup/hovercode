## Hovercode Python SDK

Typed Python client for the Hovercode API (dynamic and static QR codes).

### Installation

```bash
python -m pip install hovercode
```

### Authentication

Hovercode uses token authentication. Provide your token either:

- Via environment variable `HOVERCODE_API_TOKEN`, or
- By passing `api_token=` to `HovercodeClient`.

### Quickstart

```python
from hovercode import HovercodeClient

client = HovercodeClient()  # reads HOVERCODE_API_TOKEN

qr = client.hovercodes.create(
    workspace="YOUR-WORKSPACE-ID",
    qr_data="https://twitter.com/hovercodeHQ",
    primary_color="#1DA1F2",
)

print(qr["id"])
print(qr["svg"][:80])
```

### Notes

- Do not call the Hovercode API from a browser client (it would expose your token).

