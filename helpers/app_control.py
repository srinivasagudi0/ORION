import os

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
    if isinstance(name_type, tuple) and name_type[1] == "file_or_folder":
        # It's a file or folder path, open it directly
        try:
            subprocess.run(["open", name_type[0]], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to open {name_type[0]}: {e}")
    else:
        try:
            subprocess.run(["open", "-a", name_type], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to open {app_name}: {e}")

def delete_files_or_folders(path):
    import os
    import shutil
    if os.path.isfile(path):
        print(f"Should I delete file: {path}")
        confirm = input("Are you sure? (Y/n): ")
        if confirm.lower() == 'y':
            os.remove(path)
        else:
            print("File deletion canceled.")
        print(f"Deleted file: {path}")
    elif os.path.isdir(path):
        print(f"Should I delete folder: {path}")
        confirm = input("Are you sure? (Y/n): ")
        if confirm.lower() == 'y':
            print(f"Deleting folder: {path}")
        else:
            print("Folder deletion canceled.")
