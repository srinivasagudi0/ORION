print("Welcome to ORION!")
print("This is pre v1.0")

while True:
    user_input = input("> ")
    
    if user_input.lower() == 'exit':
        print("Exiting ORION. Goodbye!")
        break
    else:
        print(f"You entered: {user_input}")