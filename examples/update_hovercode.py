"""Update an existing Hovercode QR code.

This example reads the API token from `HOVERCODE_API_TOKEN` (or you can pass
`--api-token` explicitly).
"""

from __future__ import annotations

import argparse
import json
from typing import Optional

from hovercode import HovercodeClient


def _parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the example script."""

    parser = argparse.ArgumentParser(description="Update a Hovercode QR code.")
    parser.add_argument("--api-token", default=None, help="Hovercode API token.")
    parser.add_argument("--qr-code-id", required=True, help="QR code ID (UUID).")
    parser.add_argument(
        "--qr-data",
        default=None,
        help="New destination URL/text (only supported for dynamic Link codes).",
    )
    parser.add_argument("--display-name", default=None, help="New display name.")
    parser.add_argument(
        "--gps-tracking",
        choices=["true", "false"],
        default=None,
        help="Enable/disable GPS tracking (true/false).",
    )
    return parser.parse_args()


def _parse_bool(value: Optional[str]) -> Optional[bool]:
    """Parse a tri-state boolean from a string."""

    if value is None:
        return None
    return value.lower() == "true"


def main() -> None:
    """Run the example."""

    args = _parse_args()
    api_token: Optional[str] = args.api_token
    client = HovercodeClient(api_token=api_token)

    updated = client.hovercodes.update(
        args.qr_code_id,
        qr_data=args.qr_data,
        display_name=args.display_name,
        gps_tracking=_parse_bool(args.gps_tracking),
    )
    print(json.dumps(updated, indent=2))


if __name__ == "__main__":
    main()
