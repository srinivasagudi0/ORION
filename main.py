from helpers.app_control import open_app

print("Welcome to ORION!")
print("This is pre v1.0")

while True:
    user_input = input("> ")
    
    if user_input.lower() == 'exit':
        print("Exiting ORION. Goodbye!")
        break
    if user_input.lower().startswith('open '):
        app_name = user_input[5:].strip()
        if app_name:
            open_app(app_name)
        else:
            print("Please specify an application name to open.")
    else:
        print(f"You entered: {user_input}")
