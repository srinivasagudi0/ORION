from openai import OpenAI
import subprocess
import time
import pyperclip
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
    message: str
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

def paste_text(text):
    # pastes text into the current focused window using the clipboard and command+v
    if not text or len(text) > 12000:
        raise ValueError("Text is empty or too long.")
    previous = pyperclip.paste()
    try:
        pyperclip.copy(text)
        press_hotkey(["command", "v"])
        time.sleep(0.5)
    finally:
        pyperclip.copy(previous)

def execute_screen_step(step, frame):
    action = step.action

    if action == "open_app":
        if not step.text.strip() or "/" in step.text:
            raise ValueError("Use an application name, not a path.")

        subprocess.run(
            ["open", "-a", step.text],
            check=True,
            capture_output=True,
            text=True,
            timeout=15,
        )

    elif action in ("move_mouse", "click", "double_click", "scroll"):
        x, y = screen_point(step, frame)

        if action == "scroll" and not -10 <= step.amount <= 10:
            raise ValueError("Scroll amount must be between -10 and 10.")

        move_mouse(x, y)

        if action == "click":
            click_mouse()
        elif action == "double_click":
            double_click_mouse()
        elif action == "scroll":
            scroll_mouse(step.amount)
    elif action == "write_text":
        paste_text(step.text)

    elif action in ("press_key", "hotkey"):
        keys = step.keys
        if (
            not 1 <= len(keys) <= 5
            or any(key not in pyautogui.KEYBOARD_KEYS for key in keys)
            or (action == "press_key" and len(keys) != 1)
        ):
            raise ValueError("Invalid keys for action.")

        if action == "press_key":
            press_key(keys[0])
        else:
            press_hotkey(keys)

    elif action == "wait":
        if not 0 <= step.seconds <= 5:
            raise ValueError("Wait time must be between 0 and 5 seconds.")
        time.sleep(step.seconds)

    else:
        raise ValueError(f"Unknown action: {action}")
    return f"Action sent: {action}. Check the next screenshot."

def run_visual_task(goal, max_steps=40):
    if not goal.strip():
        print("ORION: Please give me a task.")
        return False

    if not os.getenv("OPENAI_API_KEY"):
        print("ORION: OPENAI_API_KEY is missing.")
        return False

    print("ORION: Starting screen control.")
    print("Move the pointer to the top-left corner to stop.")
    print("Questions and results will appear in this terminal.")

    history = []
    last_signature = None
    repeats = 0

    try:
        client = OpenAI(timeout=30.0, max_retries=0)

        for number in range(1, max_steps + 1):
            pyautogui.failSafeCheck()

            frame = read_screen()
            print(f"ORION: Reading screen ({number}/{max_steps})...")

            step = choose_step(client, goal, history, frame)
            pyautogui.failSafeCheck()

            print(f"ORION: {step.message}")

            if step.action == "done":
                return True

            if step.action in ("ask", "handoff"):
                print(
                    "ORION: Complete/clarify that, "
                    "then run the full task again."
                )
                return False

            signature = step.model_dump_json(exclude={"message"})
            repeats = repeats + 1 if signature == last_signature else 1
            last_signature = signature

            if repeats >= 4 and step.action != "wait":
                raise RuntimeError("Repeated the same action; stopping.")

            result = execute_screen_step(step, frame)

            history.append({
                "step": step.model_dump(),
                "execution": result,
            })

            time.sleep(0.7)

        print("ORION: Step limit reached. Task is not confirmed complete.")
        return False

    except (KeyboardInterrupt, pyautogui.FailSafeException):
        print("\nORION: Stopped.")
        return False

    except Exception as error:
        print(f"ORION: Stopped because: {error}")
        return False