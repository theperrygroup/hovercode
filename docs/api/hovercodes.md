## HovercodesClient

`HovercodesClient` is the main domain client for QR code operations.

It maps closely to the Hovercode API endpoints:

- `create()` → `POST /hovercode/create/`
- `list_for_workspace()` → `GET /workspace/{workspace_id}/hovercodes/`
- `get_hovercode()` → `GET /hovercode/{qr_code_id}/`
- `get_activity()` → `GET /hovercode/{qr_code_id}/activity/`
- `update()` → `PUT /hovercode/{qr_code_id}/update/`
- `add_tags()` → `POST /hovercode/{qr_code_id}/tags/add/`
- `delete_hovercode()` → `DELETE /hovercode/{qr_code_id}/delete/`

!!! note
    The SDK returns API responses as JSON-like dictionaries/lists. For most endpoints
    you should expect a `dict` with fields described below.

---

## create()

Create a QR code (static by default). This is the main endpoint of the Hovercode API.

### Minimal example

```python
from hovercode import HovercodeClient

client = HovercodeClient()

qr = client.hovercodes.create(
    workspace="YOUR-WORKSPACE-ID",
    qr_data="https://example.com",
)
print(qr["id"])
print(qr["svg"][:80])
```

### Important behavior

- **Static vs dynamic**: QR codes are **static** by default. Pass `dynamic=True` for a dynamic code.
- **Link vs Text**: `qr_type` defaults to `"Link"`. `"Text"` codes are plain text and
  (per the upstream docs) are **static only**.
- **PNG generation**: `generate_png=True` can slow down the create response, but it
  includes `.png`/`.svg` file URLs in the response.

### Parameter reference

The SDK passes parameters through to Hovercode’s API. Some parameters are only meaningful
for certain QR types or dynamic codes.

| Parameter | Type | Required | Default (API) | Notes |
| --- | --- | --- | --- | --- |
| `workspace` | `str` | Yes | — | Workspace ID (UUID) from your Hovercode settings. |
| `qr_data` | `str` | Yes | — | Destination/content. For `qr_type="Link"`, should be a URL. |
| `qr_type` | `QrType | str` | No | `"Link"` | `"Text"` is documented as static-only. |
| `dynamic` | `bool` | No | `false` | Set `true` for dynamic codes. |
| `display_name` | `str` | No | `null` | Internal label for your dashboard. |
| `domain` | `str` | No | workspace default | Dynamic only. Select a custom domain if you have multiple. |
| `generate_png` | `bool` | No | `false` | Slower response; includes `png`/`svg_file` URLs. |
| `gps_tracking` | `bool` | No | `false` | Dynamic only. |
| `error_correction` | `ErrorCorrection | str` | No | `Q`/`H` | Docs: defaults to `Q` without logo, `H` with logo. |
| `size` | `int` | No | `220` | Width in pixels (height derived). |
| `logo_url` | `str` | No | `null` | URL to a logo image file. |
| `logo_round` | `bool` | No | `false` | Force logo into a circle shape. |
| `primary_color` | `str` | No | `#111111` | Hex color including `#`. |
| `background_color` | `str` | No | transparent | Hex color including `#`. |
| `pattern` | `Pattern | str` | No | `"Original"` | Pattern style. |
| `eye_style` | `EyeStyle | str` | No | `"Square"` | Eye style for corners. |
| `frame` | `Frame | str` | No | `null` | Frame name. |
| `has_border` | `bool` | No | `false` | Only applies to frames with a border option. |
| `text` | `str` | No | `""` | Only applies to frames with a text option. |

!!! tip
    Prefer enums (`hovercode.enums.QrType`, `Frame`, `Pattern`, etc.) to avoid typos.

### Common styling options

Most styling is controlled via `primary_color`, `background_color`, `pattern`, `eye_style`, and `frame`.

Valid values documented by Hovercode (you can also use the enums in `hovercode.enums`):

- `pattern`: `Original`, `Circles`, `Squares`, `Diamonds`, `Triangles`
- `eye_style`: `Square`, `Rounded`, `Drop`, `Leaf`
- `frame`: `border`, `border-small`, `border-large`, `square`, `speech-bubble`,
  `speech-bubble-above`, `card`, `card-above`, `text-frame`, `round-frame`,
  `circle-viewfinder`, `solid-spin`, `burst`, `scattered-lines`, `polkadot`, `swirl`

!!! note
    The upstream docs state `error_correction` defaults to **Q** without a logo and **H**
    with a logo.

### Styled dynamic example (enums)

```python
from hovercode import HovercodeClient
from hovercode.enums import ErrorCorrection, EyeStyle, Frame, Pattern, QrType

client = HovercodeClient()

qr = client.hovercodes.create(
    workspace="YOUR-WORKSPACE-ID",
    qr_data="https://example.com",
    qr_type=QrType.LINK,
    dynamic=True,
    display_name="Example QR",
    generate_png=True,
    error_correction=ErrorCorrection.H,
    primary_color="#3b81f6",
    background_color="#FFFFFF",
    pattern=Pattern.DIAMONDS,
    eye_style=EyeStyle.ROUNDED,
    frame=Frame.CIRCLE_VIEWFINDER,
    has_border=True,
    logo_url="https://example.com/logo.png",
    logo_round=True,
)
print(qr.get("shortlink_url"))
print(qr.get("png"))
```

### Typical response fields

The API response commonly includes fields like:

- `id` (UUID string)
- `qr_data` (string)
- `qr_type` (string)
- `display_name` (string or null)
- `shortlink_url` (string or null)
- `dynamic` (bool)
- `svg` (SVG string)
- `svg_file` (string URL or null)
- `png` (string URL or null)
- `created` (ISO datetime string)

---

## list_for_workspace()

List all QR codes in a workspace. The API is paginated (50 per page by default).

```python
from hovercode import HovercodeClient

client = HovercodeClient()

page_1 = client.hovercodes.list_for_workspace("YOUR-WORKSPACE-ID")
print(page_1["count"])
print(len(page_1["results"]))
```

The response includes:

- `count`: total number of hovercodes
- `next`: URL for the next page, or `null`
- `previous`: URL for the previous page, or `null`
- `results`: list of hovercode objects

### Pagination

The SDK keeps the API close to the wire format. To get additional pages, pass `page=2`,
`page=3`, etc:

```python
page_2 = client.hovercodes.list_for_workspace("YOUR-WORKSPACE-ID", page=2)
```

### Searching

Use `q=` to search across:

- QR code links (`qr_data`)
- Display names
- Shortlink URLs
- Tag names

```python
page_1 = client.hovercodes.list_for_workspace("YOUR-WORKSPACE-ID", q="twitter")
```

---

## get_hovercode()

Retrieve a previously created QR code by ID.

```python
qr = client.hovercodes.get_hovercode("QR-CODE-ID")
print(qr.get("svg_file"))
print(qr.get("png"))
```

!!! note
    Even if you did not set `generate_png=True` during creation, the API may still
    return `svg_file` / `png` URLs when retrieving the QR code later.

---

## get_activity()

Get tracking activity for a QR code (dynamic codes). This endpoint is paginated.

- Default page size is 50
- `page_size` can be set up to **200**

```python
activity = client.hovercodes.get_activity("QR-CODE-ID", page_size=100)
print(activity["count"])
print(activity["results"][:3])
```

Each activity item commonly includes fields like:

- `qr_code_id`
- `time_utc`
- `time_timezone_aware`
- `location`
- `device`
- `scanner_id`
- `id`

---

## update()

Update a QR code. The API supports updating:

- `display_name` (for static or dynamic codes)
- `qr_data` (for **dynamic Link** codes only, per upstream documentation)
- `gps_tracking` (enable/disable GPS tracking for dynamic codes)

```python
updated = client.hovercodes.update(
    "QR-CODE-ID",
    display_name="New name",
)
print(updated["display_name"])
```

!!! important
    `update()` requires at least one of: `qr_data`, `display_name`, `gps_tracking`.

---

## add_tags()

Add tags to a QR code. The API accepts a list of tag objects.

You can provide:

- `TagInput(title=...)` / `TagInput(id=...)` (recommended)
- raw dictionaries like `{"title": "my tag"}` or `{"id": "TAG-ID"}`

```python
from hovercode.models import TagInput

client.hovercodes.add_tags(
    "QR-CODE-ID",
    [
        TagInput(title="marketing"),
        {"title": "campaign-2025"},  # raw dicts are also supported
    ],
)
```

---

## delete_hovercode()

Delete a QR code permanently.

The API returns HTTP 204 on success, so the SDK returns an empty dict (`{}`).

```python
client.hovercodes.delete_hovercode("QR-CODE-ID")
```

---

## Error handling

All API exceptions inherit from `hovercode.exceptions.ApiError`.

```python
from hovercode import ApiError

try:
    client.hovercodes.get_hovercode("not-a-real-id")
except ApiError as exc:
    print(exc.status_code)
    print(exc.response_data)
```

---

::: hovercode.hovercodes.HovercodesClient

