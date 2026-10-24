import pyautogui
import os
import io
import json
from pydantic import BaseModel, ConfigDict
import base64
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

def read_screen():
    # simply take a screenshot and and then encode it using base64 and send the full link back
    frame = capture_screen()
    buffer = io.BytesIO()
    frame["image"].save(buffer, format="PNG")

    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    frame["image_url"]= f"data:image/png;base64,{encoded}"
    return frame


def choose_step(client, goal, history, frame):
    # simply again use the taken screenshot and send it to the model with the goal and history, and get back the next step
    state = {
        "goal": goal,
        "history": history,
        "image_width": frame["image_width"],
        "image_height": frame["image_height"],
    }
    response = client.responses.parse(
        model="gpt-5.6-luna",
        instructions=VISION_PROMPT,
        reasoning={"effort": "low"},
        max_output_tokens=2048,
        store=False,
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": json.dumps(state)},
                {
                    "type": "input_image",
                    "image_url": frame["image_url"],
                    "detail": "original",
                },
            ],
        }],
        text_format=ScreenStep,
    )

    if response.status != "completed" or response.output_parsed is None:
        raise RuntimeError("The model did not return a complete action.")

    return response.output_parsed

def screen_point(step, frame):
    # macs screen can have more pixels so adding a way to fix it (found this on reddit)
    if not (0 <= step.x < frame["image_width"] and 0 <= step.y < frame["image_height"]):        
        raise ValueError("Target is outside the screenshot.")    
    width = frame["screen_width"]    
    height = frame["screen_height"]    
    if tuple(pyautogui.size()) != (width, height):  
        raise ValueError("Display dimensions changed. Start the task again.")    
        x = min(width - 1, int(step.x * width / frame["image_width"]))    
        y = min(height - 1, int(step.y * height / frame["image_height"]))    
        if not pyautogui.onScreen(x, y):        
            raise ValueError("Target is outside the controllable screen.")    
        return x, y
