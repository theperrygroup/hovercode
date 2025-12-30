## Data types

This SDK uses strong typing for request inputs and helpers. API responses are JSON and are
returned as JSON-like dictionaries/lists.

### JSON typing

The SDK defines JSON type aliases used across the codebase:

::: hovercode.types

### Enums

Enums help you avoid typos when passing common “choice” parameters (like `qr_type` or
`pattern`). All enum values are sent to the API as their `.value` string.

::: hovercode.enums

### Models

Models are small dataclasses that help structure request inputs and common response
patterns. For example, `TagInput` helps build payloads for adding tags.

::: hovercode.models

