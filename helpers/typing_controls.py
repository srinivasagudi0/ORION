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