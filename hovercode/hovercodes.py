"""Domain client for Hovercode QR code operations."""

from __future__ import annotations

from enum import Enum
from typing import Mapping, Optional, Sequence, Union, cast

from hovercode.base_client import BaseClient, QueryParamValue
from hovercode.enums import ErrorCorrection, EyeStyle, Frame, Pattern, QrType
from hovercode.exceptions import ValidationError
from hovercode.models import TagInput
from hovercode.types import JsonObject, JsonValue


class HovercodesClient(BaseClient):
    """Client for creating and managing Hovercode QR codes.

    This client implements the endpoints documented in `documentation.md`.

    Args:
        api_token: Hovercode API token. If not provided, `HOVERCODE_API_TOKEN`
            is used.
        base_url: Hovercode API base URL. Defaults to `https://hovercode.com/api/v2`.
        timeout_seconds: Per-request timeout in seconds.
        max_retries: Maximum number of retries for transient failures.
        retry_backoff_seconds: Base backoff duration (seconds) used for exponential
            backoff between retries.

    Raises:
        hovercode.exceptions.AuthenticationError: If the API token is missing.
        hovercode.exceptions.ValidationError: If `base_url` is empty.
    """

    _DEFAULT_BASE_URL = "https://hovercode.com/api/v2"

    def __init__(
        self,
        *,
        api_token: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout_seconds: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_backoff_seconds: Optional[float] = None,
    ) -> None:
        super().__init__(
            api_token=api_token,
            base_url=base_url or self._DEFAULT_BASE_URL,
            timeout_seconds=timeout_seconds,
            max_retries=max_retries,
            retry_backoff_seconds=retry_backoff_seconds,
        )

    def create(
        self,
        *,
        workspace: str,
        qr_data: str,
        qr_type: Optional[Union[QrType, str]] = None,
        dynamic: Optional[bool] = None,
        display_name: Optional[str] = None,
        domain: Optional[str] = None,
        generate_png: Optional[bool] = None,
        gps_tracking: Optional[bool] = None,
        error_correction: Optional[Union[ErrorCorrection, str]] = None,
        size: Optional[int] = None,
        logo_url: Optional[str] = None,
        logo_round: Optional[bool] = None,
        primary_color: Optional[str] = None,
        background_color: Optional[str] = None,
        pattern: Optional[Union[Pattern, str]] = None,
        eye_style: Optional[Union[EyeStyle, str]] = None,
        frame: Optional[Union[Frame, str]] = None,
        has_border: Optional[bool] = None,
        text: Optional[str] = None,
    ) -> JsonObject:
        """Create a QR code.

        Endpoint: `POST /hovercode/create/`

        Args:
            workspace: Workspace ID from your Hovercode settings.
            qr_data: QR payload. For `qr_type="Link"` it must be a valid URL.
            qr_type: QR type. Currently documented values are `"Link"` (default)
                and `"Text"`.
            dynamic: Whether to create a dynamic QR code. Defaults to `False`.
            display_name: Optional internal name for organization in Hovercode.
            domain: Optional custom domain to use for dynamic QR shortlinks.
            generate_png: If `True`, include PNG/SVG file URLs in the response.
            gps_tracking: Whether to enable GPS tracking (dynamic codes only).
            error_correction: Error correction level: `"L"`, `"M"`, `"Q"`, `"H"`.
            size: Size in pixels (width).
            logo_url: Optional logo image URL to embed in the QR code.
            logo_round: If `True`, force the logo into a circle.
            primary_color: Primary HEX color (including `#`).
            background_color: Background HEX color (including `#`).
            pattern: Pattern style (e.g. `"Original"`, `"Diamonds"`).
            eye_style: Eye style (e.g. `"Square"`, `"Rounded"`).
            frame: Frame name (e.g. `"circle-viewfinder"`).
            has_border: Whether to enable frame border option.
            text: Optional frame text (only applies to some frames).

        Returns:
            The created QR code object as returned by the API.
        """

        payload: JsonObject = {
            "workspace": workspace,
            "qr_data": qr_data,
        }
        if qr_type is not None:
            payload["qr_type"] = _normalize_str_enum(qr_type)
        if dynamic is not None:
            payload["dynamic"] = dynamic
        if display_name is not None:
            payload["display_name"] = display_name
        if domain is not None:
            payload["domain"] = domain
        if generate_png is not None:
            payload["generate_png"] = generate_png
        if gps_tracking is not None:
            payload["gps_tracking"] = gps_tracking
        if error_correction is not None:
            payload["error_correction"] = _normalize_str_enum(error_correction)
        if size is not None:
            payload["size"] = size
        if logo_url is not None:
            payload["logo_url"] = logo_url
        if logo_round is not None:
            payload["logo_round"] = logo_round
        if primary_color is not None:
            payload["primary_color"] = primary_color
        if background_color is not None:
            payload["background_color"] = background_color
        if pattern is not None:
            payload["pattern"] = _normalize_str_enum(pattern)
        if eye_style is not None:
            payload["eye_style"] = _normalize_str_enum(eye_style)
        if frame is not None:
            payload["frame"] = _normalize_str_enum(frame)
        if has_border is not None:
            payload["has_border"] = has_border
        if text is not None:
            payload["text"] = text

        result = self.post("hovercode/create/", json_data=payload)
        if not isinstance(result, dict):
            raise ValidationError(
                message="Unexpected response type from create().",
                status_code=None,
                response_data=result,
            )
        return cast(JsonObject, result)

    def list_for_workspace(
        self,
        workspace_id: str,
        *,
        q: Optional[str] = None,
        page: Optional[int] = None,
    ) -> JsonObject:
        """List QR codes for a workspace.

        Endpoint: `GET /workspace/{workspace_id}/hovercodes/`

        Args:
            workspace_id: Hovercode workspace ID.
            q: Optional search query (searches links, display names, shortlinks,
                and tag names).
            page: Optional page number.

        Returns:
            A paginated response object containing `count`, `next`, `previous`,
            and `results`.
        """

        params: dict[str, QueryParamValue] = {}
        if q is not None:
            params["q"] = q
        if page is not None:
            params["page"] = page

        endpoint = f"workspace/{workspace_id}/hovercodes/"
        result = super().get(endpoint, params=params or None)
        if not isinstance(result, dict):
            raise ValidationError(
                message="Unexpected response type from list_for_workspace().",
                status_code=None,
                response_data=result,
            )
        return cast(JsonObject, result)

    def get_hovercode(self, qr_code_id: str) -> JsonObject:
        """Retrieve a previously created QR code.

        Endpoint: `GET /hovercode/{qr_code_id}/`

        Args:
            qr_code_id: QR code ID (UUID).

        Returns:
            The QR code object as returned by the API.
        """

        result = super().get(f"hovercode/{qr_code_id}/")
        if not isinstance(result, dict):
            raise ValidationError(
                message="Unexpected response type from get_hovercode().",
                status_code=None,
                response_data=result,
            )
        return cast(JsonObject, result)

    def get_activity(
        self,
        qr_code_id: str,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> JsonObject:
        """Get tracking activity for a QR code.

        Endpoint: `GET /hovercode/{qr_code_id}/activity/`

        Args:
            qr_code_id: QR code ID (UUID).
            page: Optional page number.
            page_size: Optional page size (maximum 200 per the documentation).

        Returns:
            A paginated response with `results` containing activity items.

        Raises:
            ValidationError: If `page_size` is greater than 200.
        """

        if page_size is not None and page_size > 200:
            raise ValidationError(
                message="page_size must be <= 200.",
                status_code=None,
                response_data={"page_size": page_size},
            )

        params: dict[str, QueryParamValue] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size

        result = super().get(f"hovercode/{qr_code_id}/activity/", params=params or None)
        if not isinstance(result, dict):
            raise ValidationError(
                message="Unexpected response type from get_activity().",
                status_code=None,
                response_data=result,
            )
        return cast(JsonObject, result)

    def update(
        self,
        qr_code_id: str,
        *,
        qr_data: Optional[str] = None,
        display_name: Optional[str] = None,
        gps_tracking: Optional[bool] = None,
    ) -> JsonObject:
        """Update a QR code.

        Endpoint: `PUT /hovercode/{qr_code_id}/update/`

        Args:
            qr_code_id: QR code ID (UUID).
            qr_data: Updated QR destination. Documented as only updateable for
                dynamic `"Link"` QR codes.
            display_name: Updated display name.
            gps_tracking: Enable/disable GPS tracking for the QR code.

        Returns:
            The updated QR code object as returned by the API.

        Raises:
            ValidationError: If none of `qr_data`, `display_name`, or `gps_tracking`
                are provided.
        """

        if qr_data is None and display_name is None and gps_tracking is None:
            raise ValidationError(
                message="update() requires at least one field to update.",
                status_code=None,
                response_data=None,
            )

        payload: JsonObject = {}
        if qr_data is not None:
            payload["qr_data"] = qr_data
        if display_name is not None:
            payload["display_name"] = display_name
        if gps_tracking is not None:
            payload["gps_tracking"] = gps_tracking

        result = self.put(f"hovercode/{qr_code_id}/update/", json_data=payload)
        if not isinstance(result, dict):
            raise ValidationError(
                message="Unexpected response type from update().",
                status_code=None,
                response_data=result,
            )
        return cast(JsonObject, result)

    def add_tags(
        self,
        qr_code_id: str,
        tags: Sequence[Union[TagInput, Mapping[str, JsonValue]]],
    ) -> JsonObject:
        """Add tags to a QR code.

        Endpoint: `POST /hovercode/{qr_code_id}/tags/add/`

        Args:
            qr_code_id: QR code ID (UUID).
            tags: List of tag objects, e.g. `[{\"title\": \"my tag\"}]`. The API
                documentation describes adding tags by title or ID.

        Returns:
            The QR code object as returned by the API.

        Raises:
            ValidationError: If `tags` is empty.
        """

        if not tags:
            raise ValidationError(
                message="add_tags() requires a non-empty tags list.",
                status_code=None,
                response_data=None,
            )

        tag_payload: list[JsonValue] = []
        for tag in tags:
            if isinstance(tag, TagInput):
                tag_payload.append(tag.to_request_dict())
            else:
                tag_payload.append(dict(tag))

        result = self.post(f"hovercode/{qr_code_id}/tags/add/", json_data=tag_payload)
        if not isinstance(result, dict):
            raise ValidationError(
                message="Unexpected response type from add_tags().",
                status_code=None,
                response_data=result,
            )
        return cast(JsonObject, result)

    def delete_hovercode(self, qr_code_id: str) -> JsonObject:
        """Delete a QR code permanently.

        Endpoint: `DELETE /hovercode/{qr_code_id}/delete/`

        Args:
            qr_code_id: QR code ID (UUID).

        Returns:
            Empty dict for a successful delete (API returns HTTP 204).
        """

        result = super().delete(f"hovercode/{qr_code_id}/delete/")
        if not isinstance(result, dict):
            raise ValidationError(
                message="Unexpected response type from delete_hovercode().",
                status_code=None,
                response_data=result,
            )
        return cast(JsonObject, result)


def _normalize_str_enum(value: Union[str, Enum]) -> str:
    """Normalize a string or Enum value to a string.

    Args:
        value: Either a string, or an Enum whose `.value` is a string.

    Returns:
        A string suitable for sending to the Hovercode API.
    """

    if isinstance(value, Enum):
        raw = value.value
        if not isinstance(raw, str):
            raise ValidationError(
                message="Enum value must be a string.",
                status_code=None,
                response_data={"value": raw},
            )
        return raw
    return value
