"""Hello World synced with sitting cat animation."""

import sys
import time
from .cat_animation import CAT_FRAMES

# Styles for the 4-frame cycle
# 0: Bold, 1: Italic/Dim, 2: Hidden/Normal, 3: Cyan
MOOD_STYLES = [
    "\033[1m",      # Frame 0: Bold (Ears Up)
    "\033[2m",      # Frame 1: Dim (Ears Down)
    "\033[3m",      # Frame 2: Italic (Blink)
    "\033[1;36m"    # Frame 3: Cyan (Tail Right)
]

def hello(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def hello_sitting(name: str = "World", repeat: int = 5):
    sys.stdout.write("\033[?25l")
    try:
        for r in range(repeat):
            for i, frame in enumerate(CAT_FRAMES):
                sys.stdout.write("\033[2J\033[H")

                # Print the sitting cat
                print(frame)

                # Apply mood style
                style = MOOD_STYLES[i % len(MOOD_STYLES)]
                print(f"\n{style}Hello, {name}!\033[0m")

                sys.stdout.flush()
                time.sleep(0.2)
    finally:
        sys.stdout.write("\033[?25h")

if __name__ == "__main__":
    # If running in WSL, make sure your terminal window is tall enough!
    hello_sitting()