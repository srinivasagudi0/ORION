import pyautogui

pyautogui.FAILSAFE = True

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
    pyautogui.scroll(amount)
    return f"Scrolled {amount}."