## HovercodesClient

This client maps closely to the Hovercode API endpoints:

- `create()` → `POST /hovercode/create/`
- `list_for_workspace()` → `GET /workspace/{workspace_id}/hovercodes/`
- `get_hovercode()` → `GET /hovercode/{qr_code_id}/`
- `get_activity()` → `GET /hovercode/{qr_code_id}/activity/`
- `update()` → `PUT /hovercode/{qr_code_id}/update/`
- `add_tags()` → `POST /hovercode/{qr_code_id}/tags/add/`
- `delete_hovercode()` → `DELETE /hovercode/{qr_code_id}/delete/`

::: hovercode.hovercodes.HovercodesClient

