from helpers.app_control import open_app, delete_files_or_folders
from helpers.typing_controls import type_text
from helpers.mouse_controls import move_mouse, click_mouse, double_click_mouse, scroll_mouse
from helpers.typing_controls import press_key, write_text, press_hotkey

print("Welcome to ORION!")
print("This is pre v1.0")

while True:
    user_input = input("> ")
    
    if user_input.lower() == 'exit':
        print("Exiting ORION. Goodbye!")
        break

    elif user_input.lower().startswith('open '):
        app_name = user_input[5:].strip()
        if app_name:
            open_app(app_name)
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
            
    elif user_input.lower().startswith('delete '):
        path_to_delete = user_input[7:].strip()
        if path_to_delete:
            delete_files_or_folders(path_to_delete)
        else:
            print("Please specify the file or folder path to delete.")
    
    else:
        print(f"You entered: {user_input}")
