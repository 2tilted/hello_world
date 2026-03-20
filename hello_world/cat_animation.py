"""ASCII cat waving animation."""

import time
import sys
from typing import Optional


# Cat frames for waving animation
CAT_FRAMES = [
    """
      |\\__/,|   (`\\
    _.|o o  |_   ) )
   -(((---(((--------
    """,
    """
      |\\__/,|   (`\\
    _.|o o  |_   ) )
   -(((---(((--------
    /
    """,
    """
      |\\__/,|   (`\\
    _.|o o  |_   ) )
   -(((---(((--------
    / \\
    """,
    """
      |\\__/,|   (`\\
    _.|o o  |_   ) )
   -(((---(((--------
    \\ /
    """,
    """
      |\\__/,|   (`\\
    _.|o o  |_   ) )
   -(((---(((--------
     \\
    """,
    """
      |\\__/,|   (`\\
    _.|o o  |_   ) )
   -(((---(((--------
    """,
]


def wave_cat(
    speed: float = 0.3,
    duration: Optional[float] = None,
    repeat: int = 3,
    clear_screen: bool = True,
) -> None:
    """Display an ASCII animation of a cat waving.

    Args:
        speed: Delay between frames in seconds (default: 0.3)
        duration: Total animation duration in seconds (None = use repeat)
        repeat: Number of times to repeat the animation
        clear_screen: Whether to clear screen between frames

    Example:
        >>> wave_cat()  # Default: 3 seconds, 3 repeats
        >>> wave_cat(speed=0.1, duration=5)  # Fast, 5 seconds
    """
    total_duration = duration or repeat * len(CAT_FRAMES) * speed

    start_time = time.time()
    frame_count = 0

    while time.time() - start_time < total_duration:
        for frame in CAT_FRAMES:
            # Check if we should stop
            if duration and time.time() - start_time >= duration:
                return

            if clear_screen:
                print("\033[2J\033[H", end="")  # Clear screen
            else:
                print()  # New line without clearing

            print(frame)
            print(f"Time elapsed: {time.time() - start_time:.1f}s")
            print()

            time.sleep(speed)
            frame_count += 1

        repeat -= 1
        if repeat <= 0:
            break


def wave_cat_static() -> str:
    """Return a static ASCII cat waving (no animation).

    Returns:
        ASCII art string of a waving cat.
    """
    return CAT_FRAMES[2]


def wave_cat_frame(index: int = 0) -> str:
    """Return a specific frame of the cat animation.

    Args:
        index: Frame index (0-5)

    Returns:
        ASCII art string for the specified frame.
    """
    return CAT_FRAMES[index % len(CAT_FRAMES)]


if __name__ == "__main__":
    print("Waving Cat Animation Demo!")
    print("=" * 40)
    wave_cat(speed=0.2, repeat=2, clear_screen=False)
    print()
    print("Static version:")
    print(wave_cat_static())
