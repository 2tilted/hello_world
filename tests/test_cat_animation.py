"""Tests for cat animation module."""

import pytest
from hello_world.cat_animation import (
    wave_cat_static,
    wave_cat_frame,
    CAT_FRAMES,
)


class TestCatAnimation:
    """Test cases for cat animation functions."""

    def test_cat_frames_not_empty(self) -> None:
        """Test that CAT_FRAMES has content."""
        assert len(CAT_FRAMES) > 0

    def test_cat_frames_count(self) -> None:
        """Test the expected number of frames."""
        assert len(CAT_FRAMES) == 4

    def test_wave_cat_static_returns_string(self) -> None:
        """Test that wave_cat_static returns a non-empty string."""
        result = wave_cat_static()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_wave_cat_static_contains_cat(self) -> None:
        """Test that static version contains cat features."""
        result = wave_cat_static()
        assert "/\\" in result  # Cat ears

    def test_wave_cat_frame_valid_index(self) -> None:
        """Test getting a frame with valid index."""
        for i in range(len(CAT_FRAMES)):
            result = wave_cat_frame(i)
            assert result == CAT_FRAMES[i]

    def test_wave_cat_frame_wraps_index(self) -> None:
        """Test that frame index wraps around."""
        result = wave_cat_frame(10)
        assert result == CAT_FRAMES[10 % len(CAT_FRAMES)]

    def test_wave_cat_frame_negative_index(self) -> None:
        """Test that negative indices work correctly."""
        result = wave_cat_frame(-1)
        assert result == CAT_FRAMES[-1 % len(CAT_FRAMES)]
