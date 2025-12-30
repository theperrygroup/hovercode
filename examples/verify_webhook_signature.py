"""Verify a Hovercode webhook signature for a payload file.

Hovercode webhooks include an `X-Signature` header that is an HMAC-SHA256
signature of the raw request body.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from hovercode.webhooks import verify_signature_or_raise


def _parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the example script."""

    parser = argparse.ArgumentParser(
        description="Verify a Hovercode webhook signature."
    )
    parser.add_argument("--secret", required=True, help="Webhook secret.")
    parser.add_argument(
        "--payload-path",
        required=True,
        help="Path to a file containing raw payload bytes.",
    )
    parser.add_argument(
        "--signature",
        required=True,
        help="Signature received in the X-Signature header (hex).",
    )
    return parser.parse_args()


def main() -> None:
    """Run the example."""

    args = _parse_args()
    payload = Path(args.payload_path).read_bytes()

    verify_signature_or_raise(
        secret=args.secret, raw_payload=payload, received_signature=args.signature
    )
    print("Signature OK")


if __name__ == "__main__":
    main()
