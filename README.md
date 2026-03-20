# Hello World 🌍

> A simple Python Hello World project demonstrating modern project structure, testing, and CI/CD pipelines.

![Python](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/2tilted/hello_world/actions/workflows/ci.yml/badge.svg)

---

## 🎯 About

This project is a classic "Hello World" application written in Python, designed to showcase:

- ✅ **Modern Python packaging** with `pyproject.toml`
- ✅ **Clean project structure** following best practices
- ✅ **Comprehensive testing** with pytest
- ✅ **Automated CI/CD** with GitHub Actions
- ✅ **Professional documentation**

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/2tilted/hello_world.git
   cd hello_world
   ```

2. **Install the package in editable mode**

   ```bash
   pip install -e .
   ```

3. **(Optional) Install development dependencies**

   ```bash
   pip install -e ".[dev]"
   ```

---

## 💻 Usage

### Basic Usage

```python
from hello_world.hello import hello

# Default greeting
print(hello())              # Output: Hello, World!

# Custom greeting
print(hello("Alice"))       # Output: Hello, Alice!
print(hello("Bob"))         # Output: Hello, Bob!
```

### Command Line

The package also provides a command-line interface:

```bash
hello --help
```

---

## 🧪 Running Tests

This project includes comprehensive tests to ensure everything works correctly.

### Run all tests

```bash
pytest
```

### Run with coverage

```bash
pytest --cov=hello_world --cov-report=html
```

Then open `htmlcov/index.html` in your browser to view the coverage report.

### Run specific test file

```bash
pytest tests/test_hello.py -v
```

---

## 📁 Project Structure

```
hello_world/
├── .github/                    # GitHub-specific files
│   └── workflows/
│       └── ci.yml              # CI/CD pipeline configuration
├── .gitignore                  # Git ignore rules
├── hello_world/                # Main package
│   ├── __init__.py             # Package initialization
│   └── hello.py                # Core hello function
├── tests/                      # Test suite
│   ├── run_tests.py            # Simple test runner (no dependencies)
│   └── test_hello.py           # Pytest-style tests
├── pyproject.toml              # Project configuration & metadata
├── README.md                   # This file
└── LICENSE                     # MIT License
```

### Directory Descriptions

| Directory/File | Purpose |
|----------------|---------|
| `hello_world/` | Main Python package containing the core functionality |
| `tests/` | Test suite with both pytest and standalone test runners |
| `.github/workflows/` | GitHub Actions CI configuration |
| `pyproject.toml` | Modern Python packaging configuration (PEP 517/518) |

---

## 🤖 CI/CD Pipeline

This project includes an automated CI pipeline that runs on every push and pull request:

- **Test Matrix**: Tests run against Python 3.8, 3.9, 3.10, 3.11, and 3.12
- **Coverage**: Code coverage reporting
- **Quality**: Python syntax validation

The pipeline status is shown in the badge at the top of this README.

---

## 📋 Requirements

- **Python**: 3.8+
- **Development Dependencies** (optional):
  - `pytest` >= 7.0 - Testing framework
  - `pytest-cov` >= 4.0 - Coverage reporting

---

## 🛠️ Development

### Setting up a local development environment

1. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install development dependencies**

   ```bash
   pip install -e ".[dev]"
   ```

3. **Run tests**

   ```bash
   pytest -v
   ```

---

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Built with ❤️ using Python
- Testing powered by [pytest](https://pytest.org)
- CI/CD powered by [GitHub Actions](https://github.com/features/actions)

---

<div align="center">

**Made with 🐍 and ☕**

</div>
