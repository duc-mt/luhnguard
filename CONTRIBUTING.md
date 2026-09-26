# Contributing to Luhnguard

Thank you for your interest in contributing to Luhnguard! 

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Set up the development environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   pre-commit install
   ```

## Development Workflow

- We use `pytest` for testing. Ensure your tests have 100% coverage:
  ```bash
  pytest --cov=luhnguard tests/
  ```
- We use `ruff` for linting and formatting:
  ```bash
  ruff check luhnguard tests
  ```
- We use `mypy` for static type checking:
  ```bash
  mypy luhnguard
  ```

## Submitting Changes

1. Create a feature branch.
2. Commit your changes (we recommend following [Conventional Commits](https://www.conventionalcommits.org/)).
3. Push to your fork and submit a Pull Request.
4. Ensure all CI checks pass.
