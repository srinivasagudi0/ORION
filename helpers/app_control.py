import os
from send2trash import send2trash as st

def path_to_app(app_name):
    # basically makes the shortcut of the app name to the actual name of the app (later we can do files and folders too)
    #check if this is a an application name or a file/folder path
    import os
    root = os.path.expanduser("~")
    current_path = os.path.join(os.getcwd(), app_name)
    if os.path.exists(current_path):
        return (current_path, "file_or_folder")
    home_path = os.path.join(root, app_name)
    if os.path.exists(home_path):
        return (home_path, "file_or_folder")
    # If it's not a file or folder, assume it's an application name
        # Search Spotlight for matching file and folder names
    import subprocess

    try:
        result = subprocess.run(
            ["mdfind", "-0", "-name", app_name],
            capture_output=True,
            text=True,
            check=True,
            timeout=10
        )
    except (subprocess.SubprocessError, OSError) as e:
        print(f"Search failed: {e}")
        return None

    # Keep existing items whose full name matches, ignoring capitals
    matches = sorted({
        path
        for path in result.stdout.split("\0")
        if path
        and os.path.exists(path)
        and os.path.basename(path).casefold() == app_name.casefold()
    })

    if len(matches) == 1:
        print(f"Found: {matches[0]}")
        return (matches[0], "file_or_folder")

    if len(matches) > 1:
        print("Several matches found:")
        for number, path in enumerate(matches, start=1):
            print(f"{number}. {path}")

        choice = input("Choose a number, or Enter to cancel: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            return (matches[int(choice) - 1], "file_or_folder")

        print("Canceled.")
        return None

    app_paths = {
        # Browsers
        "chrome": "Google Chrome",
        "firefox": "Firefox",
        "edge": "Microsoft Edge",
        "opera": "Opera",
        "brave": "Brave",
        "vivaldi": "Vivaldi",
        # Coding / Development
        "vscode": "Visual Studio Code",
        "vs": "Visual Studio",
        "pycharm": "PyCharm",
        "intellij": "IntelliJ IDEA",
        "sublime": "Sublime Text",
        "notepad++": "Notepad++",
        "git": "Git Bash",
        "python": "Python",
        "idle": "IDLE",
        "android studio": "Android Studio",
        # Communication
        "discord": "Discord",
        "telegram": "Telegram Desktop",
        "whatsapp": "WhatsApp",
        "slack": "Slack",
        "teams": "Microsoft Teams",
        "zoom": "Zoom",
        "skype": "Skype",
        # Games / Launchers
        "steam": "Steam",
        "epic": "Epic Games Launcher",
        "minecraft": "Minecraft Launcher",
        "roblox": "Roblox",
        "valorant": "VALORANT",
        "riot": "Riot Client",
        "ea": "EA app",
        "ubisoft": "Ubisoft Connect",
        "battle.net": "Battle.net",
        "gog": "GOG Galaxy",
        # Media / Entertainment
        "spotify": "Spotify",
        "vlc": "VLC media player",
        "obs": "OBS Studio",
        "audacity": "Audacity",
        "itunes": "iTunes",
        "plex": "Plex",
        "apple music": "Apple Music",
        # Creative / Design
        "photoshop": "Adobe Photoshop",
        "illustrator": "Adobe Illustrator",
        "premiere": "Adobe Premiere Pro",
        "after effects": "Adobe After Effects",
        "blender": "Blender",
        "gimp": "GIMP",
        "krita": "Krita",
        "figma": "Figma",
        "canva": "Canva",
        # Microsoft Office
        "word": "Microsoft Word",
        "excel": "Microsoft Excel",
        "powerpoint": "Microsoft PowerPoint",
        "outlook": "Microsoft Outlook",
        "onenote": "OneNote",
        "access": "Microsoft Access",
        # Windows Utilities
        "cmd": "Command Prompt",
        "powershell": "Windows PowerShell",
        "terminal": "Windows Terminal",
        "explorer": "File Explorer",
        "taskmgr": "Task Manager",
        "control": "Control Panel",
        "settings": "Settings",
        "notepad": "Notepad",
        "paint": "Paint",
        "calculator": "Calculator",
        "calc": "Calculator",
        "snipping": "Snipping Tool",
        "regedit": "Registry Editor",
        "device manager": "Device Manager",
        "disk management": "Disk Management",
        # Cloud / Storage
        "onedrive": "OneDrive",
        "dropbox": "Dropbox",
        "google drive": "Google Drive",
        # Other
        "7zip": "7-Zip File Manager",
        "winrar": "WinRAR",
        "acrobat": "Adobe Acrobat",
        "virtualbox": "Oracle VirtualBox",
        "vmware": "VMware Workstation",
        "docker": "Docker Desktop",
        "postman": "Postman",
        "putty": "PuTTY",
    }
    return app_paths.get(app_name.lower(), app_name)

def open_app(app_name):
    # Open the application using the appropriate method for the Mac (for now)
    import subprocess
    name_type = path_to_app(app_name)
    if name_type is None:
        return
    if isinstance(name_type, tuple) and name_type[1] == "file_or_folder":
        # It's a file or folder path, open it directly
        try:
            subprocess.run(["open", name_type[0]], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to open {name_type[0]}: {e}")
            return False
    else:
        try:
            subprocess.run(["open", "-a", name_type], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to open {app_name}: {e}")
            return False
        
def delete_files_or_folders(path):
    import shutil
    # check if path is allowed to be deleted including their contents, if not, retur
    disallowed_paths = [
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~/Pictures"),
        os.path.expanduser("~/Music"),
        os.path.expanduser("~/Movies"),
        os.path.expanduser("~/.Trash"),
        "/System",
        "/Library",
        "/Applications",
    ]
    if path in disallowed_paths:
            print("Cannot delete the specified path. Don't delete system or important directories.")
            return
    disallowed_paths = [os.path.abspath(p) for p in disallowed_paths]
    if path in disallowed_paths:
            print("Cannot delete the specified path. Don't delete system or important directories.")
            return
    result = path_to_app(path)
    if result is None:
        return
    if not isinstance(result, tuple):
        print("File or folder not found.")
        return

    actual_path = result[0]

    confirm = input(f"Move this {path} to the Trash? (y/N): ")
    if confirm.lower() != "y":
        print("Deletion canceled.")
        return

    try:
        if os.path.isfile(actual_path):
            st(actual_path)
        elif os.path.isdir(actual_path):
            st(actual_path)
        else:
            print("File or folder not found.")
            return

        print(f"Deleted: {actual_path}")
    except OSError as e:
        print(f"Could not delete: {e}")