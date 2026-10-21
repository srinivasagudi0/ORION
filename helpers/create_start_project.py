
import os


def startProject():
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

if __name__ == "__main__":
    startProject()
