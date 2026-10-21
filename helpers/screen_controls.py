import pyautogui

def capture_screen():
    screenshot = pyautogui.screenshot()
    screen_width, screen_height = pyautogui.size()
    return {
        "image": screenshot,
        "screen_width": screen_width,
        "screen_height": screen_height,
        "image_width": screenshot.width,
        "image_height": screenshot.height
    }

