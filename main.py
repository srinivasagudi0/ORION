from helpers.visual_control import run_visual_task
from helpers.app_control import open_app, delete_files_or_folders
from helpers.typing_controls import type_text
from helpers.mouse_controls import move_mouse, click_mouse, double_click_mouse, scroll_mouse
from helpers.create_start_project import startProject as setup_project
from helpers.typing_controls import press_key, write_text, press_hotkey
from helpers.screen_controls import capture_screen
from ai_control import handle_ai_request

print("Welcome to ORION!")
print("This is pre v1.0")
print("Type 'help' to see available commands.")

def show_help():
    print("""
ORION commands:

  open Safari          Open an application, file, or folder
  type Hello           Open TextEdit and type text
  write Hello          Type into the currently focused field
  press enter          Press one key
  hotkey command s     Press a keyboard shortcut

  move 500 300         Move the mouse to X, Y
  click                Click at the current mouse position
  double click         Double-click at the current position
  scroll -3            Scroll down; positive numbers scroll up

  capture              Save a screenshot
  delete <path>        Move a file or folder to Trash after confirmation
  setup                Start the GitHub project setup routine

  do <task>            Ask AI to control the computer
  help                 Show these commands
  exit                 Close ORION

You can also ask a question in plain English.

AI computer control:
  Requires an OpenAI API key and uses paid requests.
  Screenshots are sent to OpenAI.
  Keep the keyboard and mouse still while a task runs.
  Move the mouse to the top-left corner to stop automation.
""")

while True:
    user_input = input("> ")
    
    if user_input.lower() == 'exit':
        print("Exiting ORION. Goodbye!")
        break

    elif user_input.lower().startswith('open '):
        app_name = user_input[5:].strip()
        if app_name:
            result = open_app(app_name)
            if result is False:
                handle_ai_request(user_input)
        else:
            print("Please specify an application name to open.")

    elif user_input.lower().startswith('type '):
        text_to_type = user_input[5:].strip()
        if text_to_type:
            type_text(text_to_type)
        else:
            print("Please specify the text to type.")

    elif user_input.lower().startswith('move '):
        try:
            move, x, y = user_input.split()
            x, y = int(x), int(y)
            print(move_mouse(x, y))
        except ValueError:
            print("Please provide valid coordinates in the format: move x y")

    elif user_input.lower().startswith('click'):
        print(click_mouse())

    elif user_input.strip().lower() == "help":
        show_help()

    elif user_input.lower().startswith('double click'):
        print(double_click_mouse())

    elif user_input.lower().startswith('scroll '):
        try:
            scroll, amount = user_input.split()
            amount = int(amount)
            print(scroll_mouse(amount))
        except ValueError:
            print("Use the format: scroll amount (e.g., scroll 10 or scroll -10)")

    elif user_input.lower().startswith("press "):  # press key NOT CLICK
        key_to_press = user_input[6:].strip()
        if key_to_press:
            print(press_key(key_to_press))
        else:
            print("Please specify a key to press.")

    elif user_input.lower().startswith("write "):
        text_to_write = user_input[6:].strip()
        if text_to_write:
            print(write_text(text_to_write))
        else:
            print("Please specify the text to write.")

    elif user_input.lower().startswith("hotkey "):
        keys = user_input[7:].strip().split()
        if keys:
            print(press_hotkey(keys))
        else:
            print("Please specify the keys for the hotkey.")

    elif user_input.lower().startswith("capture"):
        screen_info = capture_screen()
        print(f"Screen captured. Width: {screen_info['screen_width']}, Height: {screen_info['screen_height']}.")
        print("Taking pic in 2 seconds...")
        import time
        time.sleep(1)
        print("Taking pic in 1 second...")
        time.sleep(1)
        # Optionally, you can save the screenshot to a file
        screen_info['image'].save("screenshot.png")
        print("Screenshot saved as 'screenshot.png'.")

    elif user_input.lower().startswith('delete '):
        path_to_delete = user_input[7:].strip()
        if path_to_delete:
            delete_files_or_folders(path_to_delete)
        else:
            print("Please specify the file or folder path to delete.")
    elif user_input.lower() == 'setup':
        setup_project()
    elif user_input.lower().startswith("do "):
        run_visual_task(user_input[3:].strip())
    else:
        handle_ai_request(user_input)
