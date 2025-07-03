# Contributing to  Bambara TTS Inference SDK
Thank you for your interest in contributing to the Bamabara TTS Inference SDK! We welcome contributions from the community to enhance this SDK.

## Table of Contents

- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Coding Standards](#coding-standards)
- [Running Tests](#running-tests)
- [Submitting Pull Requests](#submitting-pull-requests)

## Setting Up the Development Environment

### Clone the Repository

```bash
git clone https://github.com/naboopay/naboopay-python-sdk.git
cd naboopay-python-sdk
```

### Install Dependencies

Install development dependencies listed in `dev-requirements.txt`:

```bash
pip install -r dev-requirements.txt
```

### Set Up Pre-Commit Hooks

Ensure code quality with pre-commit hooks:

```bash
pre-commit install
```

## Coding Standards

- Adhere to **PEP 8** for Python code style
- Use descriptive variable and function names
- Include docstrings for all public classes and methods
- Format code with `black` and sort imports with `isort`

## Running Tests

Run a test suite to verify your changes

All tests must pass before submitting a pull request.

## Submitting Pull Requests

1. Fork the repository and create a feature or bug-fix branch
2. Make changes following the [Coding Standards](#coding-standards)
3. Add tests for new features or fixes
4. Run tests and ensure they pass
5. Commit with a clear message 
6. Push your branch and submit a pull request to the main repository
7. Follow the template when submitting your pull request
