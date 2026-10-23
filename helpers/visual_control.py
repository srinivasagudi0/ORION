from pydantic import BaseModel, ConfigDict
from typing import Literal
from helpers.screen_controls import capture_screen
from helpers.mouse_controls import move_mouse, click_mouse, double_click_mouse, scroll_mouse
from helpers.typing_controls import type_text, write_text, press_key, press_hotkey
from helpers.vision_prompt import VISION_PROMPT

class ScreenStep(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    action: Literal[
        "open_app", "move_mouse", "click", "double_click", "scroll", "write_text", "press_key", "hotkey", "wait", "ask", "handoff", "done"
    ]
    messages: str
    text: str
    x: int
    y: int
    keys: list[str]
    amount: int
    seconds: float
