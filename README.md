# Hello World

A simple Python Hello World project demonstrating project structure, testing, and CI/CD.

## Installation

```bash
pip install -e .
```

## Usage

```python
from hello_world.hello import hello

print(hello())  # Hello, World!
print(hello("Alice"))  # Hello, Alice!
```

## Running Tests

```bash
pip install -e ".[dev]"
pytest
```

## Project Structure

```
hello_world/
├── hello_world/
│   ├── __init__.py
│   └── hello.py
├── tests/
│   └── test_hello.py
├── pyproject.toml
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## License

MIT
