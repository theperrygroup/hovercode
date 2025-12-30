## Quickstart

This quickstart assumes you have set `HOVERCODE_API_TOKEN` in your environment.

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

!!! tip
    If you want hosted PNG/SVG URLs in the create response, pass `generate_png=True`.

### List QR codes in a workspace

```python
payload = client.hovercodes.list_for_workspace("YOUR-WORKSPACE-ID", q="twitter")
print(payload["count"])
print(payload["results"][:2])
```

### Get a single QR code

```python
qr_id = qr["id"]
qr_full = client.hovercodes.get_hovercode(qr_id)
print(qr_full.get("svg_file"))
print(qr_full.get("png"))
```

### Add tags

```python
from hovercode.models import TagInput

client.hovercodes.add_tags(
    qr_id,
    [
        TagInput(title="marketing"),
        {"title": "campaign-2025"},
    ],
)
```

### Get tracking activity (dynamic codes)

```python
activity = client.hovercodes.get_activity(qr_id, page_size=50)
print(activity["count"])
print(activity["results"][:3])
```

### Update a QR code

```python
updated = client.hovercodes.update(
    qr_id,
    display_name="QR code for Twitter",
    # qr_data="https://twitter.com/hovercodeHQ",  # supported for dynamic Link codes
)
print(updated["display_name"])
```

### Delete a QR code

The delete endpoint returns HTTP 204, so the SDK returns `{}` on success.

```python
client.hovercodes.delete_hovercode(qr_id)
```

### Handle errors

```python
from hovercode import ApiError

try:
    client.hovercodes.get_hovercode("not-a-real-id")
except ApiError as exc:
    print(exc.status_code)
    print(exc.response_data)
```

