.PHONY = \
    build-dist \
    default \
    check-all \
    check-lint \
    check-lock \
    check-types \
    clean \
    fix-all \
    fix-format \
    fix-lint \
    fix-lint-unsafe \
    help \
    install \
    install-pre-commit \
    lock \
    run-tests \
    sync

## Run all checks and tests
default: check-all run-tests

## Build source distribution
build-dist: sync
	uv build --verbose --sdist

## Run all checks (lock, lint, types)
check-all: check-lock check-lint check-types

## Run ruff linter
check-lint: check-lock
	uv run ruff check

## Verify uv.lock is up to date
check-lock:
	uv lock --locked

## Run ty type checker
check-types: check-lock
	uv tool run ty check

## Remove build artifacts and caches
clean:
	rm -rf .ruff_cache .venv build .cache *.egg-info dist $(TARGET) $(TMPTARGET) $(TARGET_DECB) $(TMPTARGET_DECB) $(EXAMPLES_OUTPUTS)

## Auto-fix formatting and lint issues, then update lock
fix-all: fix-format fix-lint lock

## Auto-format code with ruff
fix-format: check-lock
	uv run ruff format

## Auto-fix lint issues with ruff
fix-lint: check-lock
	uv run ruff check --fix

## Auto-fix lint issues including unsafe fixes
fix-lint-unsafe: check-lock
	uv run ruff check --fix --unsafe-fixes

## Show this help
help:
	@grep -B1 -E '^[a-zA-Z_-]+:' $(MAKEFILE_LIST) | grep -E '^##|^[a-zA-Z_-]+:' | sed 'N;s/\n/ /' | sed 's/## \(.*\) \([a-zA-Z_-]*\):.*/\2\t\1/' | sort | awk -F'\t' '{ printf "  \033[36m%-24s\033[0m %s\n", $$1, $$2 }'

## Install package
install: check-lock build-dist
	uv run pip install .

## Install pre-commit hooks
install-pre-commit:
	uv run pre-commit install

## Update uv.lock
lock:
	uv lock

## Run tests with coverage
run-tests: check-lock
	uv run coverage run -m pytest
	uv run coverage report --show-missing

## Sync dependencies
sync: check-lock
	uv sync --no-install-workspace
