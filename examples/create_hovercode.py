"""Create a QR code with the Hovercode API.

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

    parser = argparse.ArgumentParser(description="Create a Hovercode QR code.")
    parser.add_argument("--api-token", default=None, help="Hovercode API token.")
    parser.add_argument(
        "--workspace", required=True, help="Hovercode workspace ID (UUID)."
    )
    parser.add_argument("--qr-data", required=True, help="URL or text payload.")
    parser.add_argument(
        "--qr-type",
        default=None,
        help='QR type: "Link" or "Text" (defaults to API default).',
    )
    parser.add_argument(
        "--dynamic",
        action="store_true",
        help="Create a dynamic QR code (default is static).",
    )
    parser.add_argument("--display-name", default=None, help="Optional display name.")
    parser.add_argument("--primary-color", default=None, help="HEX color like #111111.")
    parser.add_argument(
        "--generate-png",
        action="store_true",
        help="Include PNG/SVG file URLs in the response.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the example."""

    args = _parse_args()

    api_token: Optional[str] = args.api_token
    client = HovercodeClient(api_token=api_token)

    qr = client.hovercodes.create(
        workspace=args.workspace,
        qr_data=args.qr_data,
        qr_type=args.qr_type,
        dynamic=True if args.dynamic else None,
        display_name=args.display_name,
        primary_color=args.primary_color,
        generate_png=True if args.generate_png else None,
    )

    print(json.dumps(qr, indent=2))


if __name__ == "__main__":
    main()
