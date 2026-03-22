"""Sitting ASCII cat with tail and ear movement."""

import time
import sys

# Vertical sitting cat frames
CAT_FRAMES = [
    # Frame 0: Ears up, tail left
    """      /\\___/\\
     (  o o  )  (  /
     (  =^=  )  ) )
     (        ) / /
     (         |_/
     / /----\\ \\
    (_/      \\_)""",
    # Frame 1: Ears twitch, tail mid
    """      vv___vv
     (  o o  )  ( |
     (  =^=  )  ) )
     (        ) / /
     (         |_/
     / /----\\ \\
    (_/      \\_)""",
    # Frame 2: Eyes blink, tail right
    """      /\\___/\\
     (  - -  )  (  \\
     (  =^=  )  ) )
     (        ) / /
     (         |_/
     / /----\\ \\
    (_/      \\_)""",
    # Frame 3: Ears up, tail right
    """      /\\___/\\
     (  o o  )  (  \\
     (  =^=  )  ) )
     (        ) / /
     (         |_/
     / /----\\ \\
    (_/      \\_)"""
]

def wave_cat_static() -> str:
    """Return a static cat ASCII art."""
    return CAT_FRAMES[0]


def wave_cat_frame(index: int) -> str:
    """Return a specific frame with index wrapping."""
    return CAT_FRAMES[index % len(CAT_FRAMES)]


def wave_cat(speed: float = 0.2, repeat: int = 4):
    sys.stdout.write("\033[?25l") # Hide cursor
    try:
        for _ in range(repeat):
            for frame in CAT_FRAMES:
                sys.stdout.write("\033[2J\033[H")
                sys.stdout.write(frame + "\n")
                sys.stdout.flush()
                time.sleep(speed)
    finally:
        sys.stdout.write("\033[?25h") # Show cursor