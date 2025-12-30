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

Example: building tag payloads

```python
from hovercode.models import TagInput

tag_1 = TagInput(title="marketing").to_request_dict()
tag_2 = TagInput(id="TAG-ID").to_request_dict()

print(tag_1)  # {"title": "marketing"}
print(tag_2)  # {"id": "TAG-ID"}
```

Example: parsing paginated responses

```python
from hovercode.models import PaginatedResponse

payload = {
    "count": 2,
    "next": None,
    "previous": None,
    "results": [{"id": "1"}, {"id": "2"}],
}

parsed = PaginatedResponse.from_dict(payload)
print(parsed.count)
print(parsed.results)
```

::: hovercode.models

