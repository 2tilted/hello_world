#!/usr/bin/env python3
"""Simple test runner without external dependencies."""

import sys
sys.path.insert(0, '.')

from hello_world.hello import hello
from hello_world.cat_animation import wave_cat_static, wave_cat_frame, CAT_FRAMES


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


def test_cat_frames_not_empty():
    """Test that CAT_FRAMES has content."""
    assert len(CAT_FRAMES) > 0, "CAT_FRAMES should not be empty"
    print("✓ test_cat_frames_not_empty passed")


def test_cat_frames_count():
    """Test the expected number of frames."""
    assert len(CAT_FRAMES) == 6, f"Expected 6 frames, got {len(CAT_FRAMES)}"
    print("✓ test_cat_frames_count passed")


def test_wave_cat_static_returns_string():
    """Test that wave_cat_static returns a non-empty string."""
    result = wave_cat_static()
    assert isinstance(result, str), "wave_cat_static should return a string"
    assert len(result) > 0, "wave_cat_static should return non-empty string"
    print("✓ test_wave_cat_static_returns_string passed")


def test_wave_cat_static_contains_cat():
    """Test that static version contains cat features."""
    result = wave_cat_static()
    assert "\\__/" in result, "Static cat should contain cat ears"
    print("✓ test_wave_cat_static_contains_cat passed")


def test_wave_cat_frame_valid_index():
    """Test getting a frame with valid index."""
    for i in range(len(CAT_FRAMES)):
        result = wave_cat_frame(i)
        assert result == CAT_FRAMES[i], f"Frame {i} mismatch"
    print("✓ test_wave_cat_frame_valid_index passed")


def test_wave_cat_frame_wraps_index():
    """Test that frame index wraps around."""
    result = wave_cat_frame(10)
    expected = CAT_FRAMES[10 % len(CAT_FRAMES)]
    assert result == expected, "Frame index should wrap around"
    print("✓ test_wave_cat_frame_wraps_index passed")


if __name__ == "__main__":
    print("Running Hello World tests...\n")
    try:
        test_hello_default()
        test_hello_custom_name()
        test_hello_empty_string()
        test_cat_frames_not_empty()
        test_cat_frames_count()
        test_wave_cat_static_returns_string()
        test_wave_cat_static_contains_cat()
        test_wave_cat_frame_valid_index()
        test_wave_cat_frame_wraps_index()
        print("\n✓ All tests passed!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
