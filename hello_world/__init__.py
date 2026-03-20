"""Hello World package - Hello and waving cat animations."""

__version__ = "0.2.0"

from hello_world.hello import hello
from hello_world.cat_animation import wave_cat, wave_cat_static, wave_cat_frame

__all__ = ["hello", "wave_cat", "wave_cat_static", "wave_cat_frame"]
