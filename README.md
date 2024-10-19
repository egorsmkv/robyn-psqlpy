# Robyn + PSQLPy

This is a test repo to see how these two tools work together.

- https://github.com/sparckles/Robyn
- https://github.com/psqlpy-python/psqlpy

## Install

```bash
uv venv --python 3.12

source .venv/bin/activate

just sync
```

## Run

```bash
# Run PostgreSQL
just up

# Run API
just api
```

## Check performance

```bash
oha -n 50000 http://127.0.0.1:8000/
```
