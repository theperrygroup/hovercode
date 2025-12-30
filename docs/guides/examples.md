## Examples

This repository includes runnable scripts under `examples/`:

- `examples/create_hovercode.py`
- `examples/list_workspace_hovercodes.py`
- `examples/update_hovercode.py`
- `examples/verify_webhook_signature.py`

### Run the scripts

```bash
export HOVERCODE_API_TOKEN="YOUR-TOKEN"

python examples/create_hovercode.py --workspace "YOUR-WORKSPACE-ID" --qr-data "https://example.com"
python examples/list_workspace_hovercodes.py --workspace-id "YOUR-WORKSPACE-ID" --q twitter
python examples/update_hovercode.py --qr-code-id "QR-CODE-ID" --display-name "New name"
```

### Create a QR code (Python)

```python
from hovercode import HovercodeClient

client = HovercodeClient()

qr = client.hovercodes.create(
    workspace="YOUR-WORKSPACE-ID",
    qr_data="https://example.com",
    primary_color="#111111",
)
print(qr["id"])
```

### Create a dynamic QR code with enums

```python
from hovercode import HovercodeClient
from hovercode.enums import ErrorCorrection, EyeStyle, Frame, Pattern, QrType

client = HovercodeClient()

qr = client.hovercodes.create(
    workspace="YOUR-WORKSPACE-ID",
    qr_data="https://example.com",
    qr_type=QrType.LINK,
    dynamic=True,
    generate_png=True,
    error_correction=ErrorCorrection.H,
    pattern=Pattern.DIAMONDS,
    eye_style=EyeStyle.ROUNDED,
    frame=Frame.CIRCLE_VIEWFINDER,
    has_border=True,
)
print(qr.get("shortlink_url"))
print(qr.get("png"))
```

### Add tags

```python
from hovercode import HovercodeClient
from hovercode.models import TagInput

client = HovercodeClient()

client.hovercodes.add_tags(
    "QR-CODE-ID",
    [
        TagInput(title="marketing"),
        {"title": "campaign-2025"},  # raw dicts are also supported
    ],
)
```

### Get tracking activity

```python
from hovercode import HovercodeClient

client = HovercodeClient()

activity = client.hovercodes.get_activity("QR-CODE-ID", page_size=50)
print(activity["count"])
print(activity["results"][:3])
```

### Verify a webhook signature

```python
import json

from hovercode.webhooks import verify_signature_or_raise

secret = "YOUR_WEBHOOK_SECRET"
received_signature = "X-SIGNATURE-HEADER-VALUE"
raw_payload = json.dumps({"example": "payload"}).encode("utf-8")

verify_signature_or_raise(
    secret=secret,
    raw_payload=raw_payload,
    received_signature=received_signature,
)
```

