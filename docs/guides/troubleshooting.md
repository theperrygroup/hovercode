## Troubleshooting

### Authentication errors

- Ensure you are using the correct token.
- Ensure `HOVERCODE_API_TOKEN` is set in your environment if you are not passing `api_token=`.

### Timeouts / transient errors

The client supports configurable timeouts and retries via:

- `HOVERCODE_TIMEOUT_SECONDS`
- `HOVERCODE_MAX_RETRIES`
- `HOVERCODE_RETRY_BACKOFF_SECONDS`

