# Contributing to TradeScope

Thank you for your interest in contributing to TradeScope! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

Please read and understand our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/tradescope.git
   cd tradescope
   ```
3. Add the upstream remote:
   ```bash
   git remote add upstream https://github.com/mrningzeoutlook-pixel/tradescope.git
   ```

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov pytest-mock
   ```

3. Install in development mode:
   ```bash
   pip install -e .
   ```

## Making Changes

1. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. Make your changes following the guidelines below.

3. Run tests to ensure nothing is broken:
   ```bash
   pytest tests/ -v
   ```

4. Commit your changes with a clear message:
   ```bash
   git commit -m "Add feature: your feature description"
   ```

## Testing

### Running Tests

Run all tests:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ -v --cov=src --cov-report=html
```

Run specific test file:
```bash
pytest tests/test_pipeline.py -v
```

Run specific test:
```bash
pytest tests/test_pipeline.py::TestTradeScopePipeline::test_analyze_returns_string -v
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_<module_name>.py`
- Use descriptive test names: `test_<function>_<scenario>_<expected_result>`
- Include docstrings explaining what each test does
- Aim for >80% code coverage

Example:
```python
def test_analyze_returns_dict(analysis_agent, sample_data):
    """Test that analyze returns a dictionary with expected fields."""
    result = analysis_agent.analyze(sample_data)
    assert isinstance(result, dict)
    assert "market_attractiveness_score" in result
```

## Code Style

### Python Style Guide

We follow PEP 8 with some modifications:

- Line length: 88 characters (Black default)
- Use type hints where possible
- Docstrings for all public functions and classes

### Formatting

We use Black for code formatting:
```bash
black src/ tests/
```

### Import Sorting

We use isort for import sorting:
```bash
isort src/ tests/
```

### Linting

Run flake8:
```bash
flake8 src/ tests/
```

## Submitting Changes

1. Update your fork with the latest changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Open a Pull Request on GitHub:
   - Use a clear, descriptive title
   - Reference any related issues
   - Explain your changes in the description

4. Your PR will be reviewed and merged once approved.

## Reporting Issues

When reporting issues, please include:

- Python version
- TradeScope version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages or logs

## Types of Contributions

We welcome the following types of contributions:

- Bug fixes
- New features
- Documentation improvements
- Test coverage improvements
- Performance optimizations
- Code refactoring

## Questions?

Feel free to open an issue for any questions about contributing.

---

Thank you for contributing to TradeScope!
