from .app_control import open_app
import time
import pyautogui

def type_text(text):
    # type text into TextEdit for now (later we can add more apps)
    open_app("TextEdit")
    time.sleep(1.5)  # Wait for TextEdit to open
    pyautogui.press('escape')
    time.sleep(0.5)
    pyautogui.hotkey('command', 'n')  # Create a new document
    time.sleep(0.5)  # Wait for the new document to be ready
    cursor_position = pyautogui.position()  # Get the current cursor position
    pyautogui.typewrite(text, interval=0.05)  # Type the text with a slight delay between keystrokes
    return "Text typed successfully in TextEdit."

def press_key(key):
    if key not in pyautogui.KEYBOARD_KEYS:
        return f"'{key}' is not a valid key."
    time.sleep(1) # idk why but thiis mkaes the thing work better
    pyautogui.press(key)
    return f"Pressed '{key}'."

def press_hotkey(keys):
    if not keys or any(kets not in pyautogui.KEYBOARD_KEYS for kets in keys):
        return "Unknown or missing keys."

    time.sleep(3) # you got to wait a bit for the hotkey to work
    pyautogui.hotkey(*keys)
    return "Shortcut pressed successfully."

def write_text(text):
    time.sleep(1)  # Wait for the application to be ready
    pyautogui.typewrite(text, interval=0.05)
    return "Text written successfully."