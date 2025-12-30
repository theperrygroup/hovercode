## Installation

The Hovercode SDK supports Python **3.9+**.

```bash
python -m pip install hovercode
```

### Optional extras

If you want `.env` file support via `python-dotenv`:

```bash
python -m pip install "hovercode[dotenv]"
```

### Development install

For development (tests, linting, typing, security, docs):

```bash
python -m pip install -e ".[dev,docs]"
```

### Verify installation

```bash
python -c "from hovercode import HovercodeClient; print(HovercodeClient)"
```

