"""List QR codes in a Hovercode workspace.

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

    parser = argparse.ArgumentParser(description="List workspace hovercodes.")
    parser.add_argument("--api-token", default=None, help="Hovercode API token.")
    parser.add_argument(
        "--workspace-id", required=True, help="Hovercode workspace ID (UUID)."
    )
    parser.add_argument(
        "--q",
        default=None,
        help="Optional search query (searches link, display name, tags, shortlink).",
    )
    parser.add_argument("--page", type=int, default=None, help="Optional page number.")
    return parser.parse_args()


def main() -> None:
    """Run the example."""

    args = _parse_args()
    api_token: Optional[str] = args.api_token
    client = HovercodeClient(api_token=api_token)

    payload = client.hovercodes.list_for_workspace(
        args.workspace_id, q=args.q, page=args.page
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
