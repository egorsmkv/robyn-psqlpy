set dotenv-filename := '.env.dev'

bin := ".venv/bin"

api:
    {{bin}}/python api.py

fmt:
    {{bin}}/ruff check --select I --fix
    {{bin}}/ruff format

up:
    docker compose -f dev.yml up

down:
    docker compose -f dev.yml down

db:
    @echo "Connecting to database... $POSTGRES_DB"
    docker exec -it robyn_pgsql_dev psql -U $POSTGRES_USER -d $POSTGRES_DB

sync:
    uv sync --extra dev

pdm-outdated:
    {{bin}}/pdm update --dry-run
