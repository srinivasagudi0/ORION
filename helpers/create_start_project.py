import time
from helpers.app_control import open_app
from helpers.typing_controls import press_hotkey, write_text, press_key
from helpers.mouse_controls import click_mouse
import os


def startProject():
    logged_in = input("Are you logged in to GitHub on Safari? (y/n): ").strip().lower()
    if logged_in != "y":
        print("Please log in to GitHub before starting a new project.")
        return
    
    # Step 1: Collect project details
    project_name = input("Project name: ").strip()
    project_description = input("Description: ").strip()
    visibility = input("Visibility (public/private): ").strip().lower()
    location = input(
        "Location parent folder (use pwd for full path): "
    ).strip()

    #Check project details properly
    if not project_name or not project_description or not location:
        print("Please provide all project details.")
        return

    if visibility not in ("public", "private"):
        print("Visibility must be public or private.")
        return

    if not os.path.isdir(location):
        print("Parent folder does not exist.")
        return
    #confirm 
    print("\n--- ORION Project Setup ---")
    print(f"Project Name: {project_name}")
    print(f"Description: {project_description}")
    print(f"Visibility: {visibility}")
    print(f"Parent Folder: {os.path.abspath(location)}")

    print("\nProject details validated successfully!")

    print("STAY BACK AND WATCH THE STAY BACK AND WATCH THE MAGIC HAPPEN...")

    ## Step 2: Open github and do the form filling
    open_app("Safari")
    click_mouse()  # Click to ensure Safari is active
    time.sleep(1)
    press_hotkey(["command", "t"])  # Open a new tab
    press_hotkey(["command", "l"])  # Focus the address bar
    write_text("https://github.com/new")
    press_key("enter")  # Navigate to the new repository page
    time.sleep(2)
    for i in range(5):
        press_hotkey(["tab"])  # Navigate through the form fields
    write_text(project_name)
    press_hotkey(["tab"])
    write_text(project_description)
    press_hotkey(["tab"])
    if visibility == "private":
        press_hotkey(['space'])  # Confirm selection
        press_hotkey(["down"])  # Select private visibility
        press_hotkey(['enter'])  # Confirm selection
        
    for i in range(2):
        press_hotkey(["alt", "tab"])  #go to add readme checkbox
    press_key('space')  # Check the box to add a README file
    for i in range(9):
        press_hotkey(["tab"])  # Navigate to the "Create repository" button
    press_key('enter')  # prss enter in the name box
    time.sleep(3)  # Wait for the repository to be created
    print("Repository created successfully!")
    print("Press 'Continue' to open the repository in VS Code.")
    a = input("Press anything to continue...")
    print("Continuing...")
    time.sleep(1)
    open_app("Safari")
    time.sleep(2)
    click_mouse()  # Click to ensure Safari is active
    time.sleep(1)
    press_hotkey(["command", "l"])  # Focus the address bar
    press_hotkey(["command", "c"])  # Copy the URL
    open_app("Visual Studio Code")
    time.sleep(2)
    click_mouse()  # Click to ensure VS Code is active
    press_hotkey(["command", "shift", "n"])  # Open a new window in VS Code
    time.sleep(1)  # Wait for the new window to open
    click_mouse()  # Click to ensure the new window is active
    time.sleep(1)  # Wait for the new window to be ready
    press_hotkey(["command", "shift", "p"])  # Open the command palette
    write_text("Git: Clone")
    press_key("enter")  # Select the "Git: Clone" command
    time.sleep(1)  # Wait for the input box to appear
    press_hotkey(["command", "v"])  # Paste the repository URL
    press_key("enter")  # Confirm the URL
    time.sleep(1)  # Wait for it to clone
    # choose the location to clone the repository
    press_hotkey(["command", "shift", "g"])  # Open the "Go to Folder" dialog
    write_text(location)  # Type the location path
    press_key("enter")  # Confirm the location
    time.sleep(1)  # Wait for the folder to be selected
    press_key("enter")  # Confirm the clone operation
    time.sleep(3)  # Wait for the cloning process to complete
    print("Repository cloned successfully!")
    # open it now
    press_key("enter")  # Open the cloned repository in VS Code
    time.sleep(2)  # Wait for the repository to open
    press_key("enter")  # trust the authorship of the repository thing
    

if __name__ == "__main__":
    startProject()
