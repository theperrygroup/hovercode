## API reference

This section is generated from the library’s docstrings using `mkdocstrings`.

### Key classes

- `hovercode.client.HovercodeClient`: the main facade client
- `hovercode.hovercodes.HovercodesClient`: QR code operations

### Naming note

`HovercodesClient` also provides high-level methods like:

- `get_hovercode(qr_code_id)`
- `delete_hovercode(qr_code_id)`

These names intentionally avoid clashing with the lower-level HTTP helper
methods on the shared transport client.

