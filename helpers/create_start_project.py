from app_control import open_app
from typing_controls import press_hotkey, write_text
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
    press_hotkey(["command", "t"])  # Open a new tab
    press_hotkey(["command", "l"])  # Focus the address bar
    write_text("https://github.com/new")

if __name__ == "__main__":
    startProject()
