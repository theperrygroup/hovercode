## Hovercode SDK Style Guide

### Docstrings

- Use **Google-style** docstrings for all public classes, functions, and methods.
- Always include:
  - `Args:` for parameters
  - `Returns:` for return values
  - `Raises:` for exceptions

### Typing

- All public APIs must be fully typed.
- Prefer precise types (`dict[str, Any]`, `Sequence[str]`, `UUID`) over `Any` when feasible.
- Keep response payload types as `dict[str, Any]` unless the API shape is stable and well-defined.

### Formatting & linting

- Format with `black` and `isort`.
- Lint with `flake8`.
- Type-check with `mypy --strict`.

### Testing

- Unit tests use `pytest` + `responses`.
- Coverage target is **100%** for the `hovercode` package.

