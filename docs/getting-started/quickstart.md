## Quickstart

```python
from hovercode import HovercodeClient

client = HovercodeClient()

qr = client.hovercodes.create(
    workspace="YOUR-WORKSPACE-ID",
    qr_data="https://twitter.com/hovercodeHQ",
    primary_color="#1DA1F2",
)

print(qr["id"])
```

