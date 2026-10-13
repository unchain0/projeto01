# projeto01

Budget PDF generator for project estimates (Python, Jupyter).

[![CI](https://github.com/unchain0/projeto01/actions/workflows/ci.yml/badge.svg)](https://github.com/unchain0/projeto01/actions)

Real execution captured in `docs/assets/test-output.txt` (import verification in clean environment).

## Quick start

```bash
pip install -r requirements.txt
python main.py
```

## Quality

- Strict ruff (E/F/W/I/N/D/UP/B/C4/SIM/C90), max complexity 10
- Warnings as errors
- UUIDv7 / CSPRNG required for any randomness
