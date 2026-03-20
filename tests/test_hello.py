"""Tests for hello function."""

import pytest
from hello_world.hello import hello


class TestHello:
    """Test cases for hello function."""

    def test_hello_default(self) -> None:
        """Test default greeting."""
        assert hello() == "Hello, World!"

    def test_hello_custom_name(self) -> None:
        """Test greeting with custom name."""
        assert hello("Alice") == "Hello, Alice!"

    def test_hello_empty_string(self) -> None:
        """Test greeting with empty string."""
        assert hello("") == "Hello, !"
