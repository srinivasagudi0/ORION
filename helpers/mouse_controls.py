import pyautogui

pyautogui.FAILSAFE = True

def current_mouse_position():
    x, y = pyautogui.position()
    return f"Current mouse position: ({x}, {y})"

def move_mouse(x, y):
    if not pyautogui.onScreen(x, y):
        return "That position is outside the screen."

    pyautogui.moveTo(x, y, duration=0.5)
    return f"Moved to {x}, {y}."

def click_mouse():
    pyautogui.click()
    return "Clicked."

def double_click_mouse():
    pyautogui.doubleClick(interval=0.10)
    return "Double-clicked."

def scroll_mouse(amount):
    current = 0
    while current < amount:
        pyautogui.scroll(1)
        current += 1
    return f"Scrolled {amount}."