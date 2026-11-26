# CHECK

[group('check')]
check: audit lint format types test

[group('check')]
audit:
    uv audit --preview-features audit

[group('check')]
lint:
    uv run ruff check --fix

[group('check')]
format:
    uv run ruff format

[group('check')]
types:
    uv run ty check

[group('check')]
test *ARGS:
    uv run pytest {{ if ARGS == "" { "." } else { ARGS } }}


# Recreate the virtualenv, install deps + pre-commit hooks
[group('setup')]
init-env:
    rm -rf .venv
    uv venv
    uv sync
    uv run pre-commit install
