#!/usr/bin/env python3
"""Simple test runner without external dependencies."""

import sys
sys.path.insert(0, '.')

from hello_world.hello import hello


def test_hello_default():
    """Test default greeting."""
    result = hello()
    assert result == "Hello, World!", f"Expected 'Hello, World!' but got '{result}'"
    print("✓ test_hello_default passed")


def test_hello_custom_name():
    """Test greeting with custom name."""
    result = hello("Alice")
    assert result == "Hello, Alice!", f"Expected 'Hello, Alice!' but got '{result}'"
    print("✓ test_hello_custom_name passed")


def test_hello_empty_string():
    """Test greeting with empty string."""
    result = hello("")
    assert result == "Hello, !", f"Expected 'Hello, !' but got '{result}'"
    print("✓ test_hello_empty_string passed")


if __name__ == "__main__":
    print("Running Hello World tests...\n")
    try:
        test_hello_default()
        test_hello_custom_name()
        test_hello_empty_string()
        print("\n✓ All tests passed!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
