.DEFAULT_GOAL := help

.PHONY: install-requirements
install-requirements: ## Install requirements in local venv
	uv sync --frozen


.PHONY: test-unit
test-unit: ## Launch unit-tests
	@printf "🧪🧪 Starting unit-tests"
	@uv run pytest -vv -s tests/unit --cov money
	@uv run coverage html
	@uv run coverage xml -o coverage.xml
	@mkdir -p /tmp/test-reports/


# Picks up all comments that start with a ## and are at the end of a target definition line.
.PHONY: help
help:  ## Display command usage
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
