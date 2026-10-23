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
    # =========================================================================
    # 1. macOS BUILT-IN SYSTEM APPLICATIONS & CORE UTILITIES
    # =========================================================================

    # Finder & System Control
    "finder": "Finder",
    "macintosh hd": "Finder",
    "desktop": "Finder",
    "file manager": "Finder",
    "file explorer": "Finder",
    "airdrop": "Finder",
    "icloud": "Finder",
    "icloud drive": "Finder",

    "system settings": "System Settings",
    "system preferences": "System Settings",
    "sys preferences": "System Settings",
    "sys settings": "System Settings",
    "preferences": "System Settings",
    "settings": "System Settings",
    "mac settings": "System Settings",
    "control panel": "System Settings",

    # Activity & Task Management
    "activity monitor": "Activity Monitor",
    "activity": "Activity Monitor",
    "task manager": "Activity Monitor",
    "taskmgr": "Activity Monitor",
    "process monitor": "Activity Monitor",
    "system monitor": "Activity Monitor",

    # Disk & Storage Management
    "disk utility": "Disk Utility",
    "disk": "Disk Utility",
    "disk management": "Disk Utility",
    "disk manager": "Disk Utility",
    "formatter": "Disk Utility",

    # Terminal & Command Line
    "terminal": "Terminal",
    "terminal app": "Terminal",
    "mac terminal": "Terminal",
    "bash": "Terminal",
    "zsh": "Terminal",
    "cmd": "Terminal",
    "command prompt": "Terminal",
    "console terminal": "Terminal",

    # Console & Logging
    "console": "Console",
    "system console": "Console",
    "log viewer": "Console",
    "logs": "Console",

    # Security & Credentials
    "keychain access": "Keychain Access",
    "keychain": "Keychain Access",
    "keychains": "Keychain Access",
    "passwords": "Passwords",
    "password manager": "Passwords",
    "mac passwords": "Passwords",

    # Automation & Scripting
    "shortcuts": "Shortcuts",
    "shortcut": "Shortcuts",
    "apple shortcuts": "Shortcuts",
    "mac shortcuts": "Shortcuts",
    "siri shortcuts": "Shortcuts",

    "automator": "Automator",
    "mac automator": "Automator",

    "script editor": "Script Editor",
    "applescript": "Script Editor",
    "applescript editor": "Script Editor",

    # System Migration & Setup
    "migration assistant": "Migration Assistant",
    "migration": "Migration Assistant",
    "mac migration": "Migration Assistant",

    "boot camp assistant": "Boot Camp Assistant",
    "boot camp": "Boot Camp Assistant",
    "bootcamp": "Boot Camp Assistant",

    "bluetooth file exchange": "Bluetooth File Exchange",
    "bluetooth exchange": "Bluetooth File Exchange",

    "dirutility": "Directory Utility",
    "directory utility": "Directory Utility",

    "netutility": "Network Utility",
    "network utility": "Network Utility",

    # Audio & Display Hardware Utilities
    "audio midi setup": "Audio MIDI Setup",
    "audio midi": "Audio MIDI Setup",
    "midi setup": "Audio MIDI Setup",
    "audio setup": "Audio MIDI Setup",

    "colorsync utility": "ColorSync Utility",
    "colorsync": "ColorSync Utility",
    "color profile": "ColorSync Utility",

    # Fonts & Typography
    "font book": "Font Book",
    "fontbook": "Font Book",
    "fonts": "Font Book",
    "font manager": "Font Book",

    # System Recovery & Diagnostics
    "system information": "System Information",
    "system info": "System Information",
    "sysinfo": "System Information",
    "about this mac": "System Information",

    # Time Machine / Backup
    "time machine": "Time Machine",
    "timemachine": "Time Machine",
    "mac backup": "Time Machine",


    # =========================================================================
    # 2. APPLE NATIVE / STOCK APPLICATIONS
    # =========================================================================

    # Productivity & Knowledge
    "notes": "Notes",
    "note": "Notes",
    "apple notes": "Notes",
    "mac notes": "Notes",
    "memo": "Notes",
    "memos": "Notes",
    "notepad": "Notes",

    "reminders": "Reminders",
    "reminder": "Reminders",
    "apple reminders": "Reminders",
    "mac reminders": "Reminders",
    "todo": "Reminders",
    "to-do": "Reminders",
    "tasks": "Reminders",
    "task list": "Reminders",

    "calendar": "Calendar",
    "apple calendar": "Calendar",
    "mac calendar": "Calendar",
    "ical": "Calendar",
    "icalendar": "Calendar",

    "contacts": "Contacts",
    "contact": "Contacts",
    "address book": "Contacts",
    "apple contacts": "Contacts",
    "mac contacts": "Contacts",
    "people": "Contacts",

    "calculator": "Calculator",
    "calc": "Calculator",
    "apple calculator": "Calculator",

    "textedit": "TextEdit",
    "text edit": "TextEdit",
    "texteditor": "TextEdit",
    "txt": "TextEdit",
    "mac notepad": "TextEdit",

    "preview": "Preview",
    "pdf viewer": "Preview",
    "image viewer": "Preview",
    "apple preview": "Preview",

    "dictionary": "Dictionary",
    "thesaurus": "Dictionary",
    "apple dictionary": "Dictionary",

    "freeform": "Freeform",
    "apple freeform": "Freeform",
    "whiteboard": "Freeform",

    "journal": "Journal",
    "apple journal": "Journal",

    # Communication & Social
    "mail": "Mail",
    "apple mail": "Mail",
    "mac mail": "Mail",
    "email": "Mail",
    "e-mail": "Mail",

    "messages": "Messages",
    "message": "Messages",
    "imessage": "Messages",
    "apple messages": "Messages",
    "mac messages": "Messages",
    "sms": "Messages",
    "i-message": "Messages",

    "facetime": "FaceTime",
    "face time": "FaceTime",
    "apple facetime": "FaceTime",
    "video call": "FaceTime",

    # Media, Audio & Entertainment
    "music": "Music",
    "apple music": "Music",
    "itunes": "Music",
    "i-tunes": "Music",

    "tv": "TV",
    "apple tv": "TV",
    "apple tv+": "TV",
    "appletv": "TV",
    "apple tv plus": "TV",

    "podcasts": "Podcasts",
    "podcast": "Podcasts",
    "apple podcasts": "Podcasts",

    "books": "Books",
    "apple books": "Books",
    "ibooks": "Books",
    "i-books": "Books",
    "ebooks": "Books",

    "photos": "Photos",
    "photo": "Photos",
    "apple photos": "Photos",
    "iphoto": "Photos",
    "photo library": "Photos",

    "photo booth": "Photo Booth",
    "photobooth": "Photo Booth",
    "webcam": "Photo Booth",
    "camera": "Photo Booth",

    "voice memos": "Voice Memos",
    "voice memo": "Voice Memos",
    "voicememos": "Voice Memos",
    "voice recorder": "Voice Memos",
    "dictaphone": "Voice Memos",
    "audio recorder": "Voice Memos",

    "quicktime player": "QuickTime Player",
    "quicktime": "QuickTime Player",
    "quick time": "QuickTime Player",
    "video player": "QuickTime Player",

    # Information & Utility
    "maps": "Maps",
    "map": "Maps",
    "apple maps": "Maps",

    "weather": "Weather",
    "apple weather": "Weather",
    "forecast": "Weather",

    "stocks": "Stocks",
    "stock": "Stocks",
    "apple stocks": "Stocks",
    "finance": "Stocks",
    "market": "Stocks",

    "news": "News",
    "apple news": "News",

    "home": "Home",
    "apple home": "Home",
    "homekit": "Home",

    "find my": "Find My",
    "findmy": "Find My",
    "find my mac": "Find My",
    "find my iphone": "Find My",
    "find my device": "Find My",

    # Games & Gaming Utilities
    "chess": "Chess",
    "apple chess": "Chess",

    "game center": "Game Center",
    "gamecenter": "Game Center",

    # Apple iWork Suite
    "pages": "Pages",
    "apple pages": "Pages",
    "word processor": "Pages",

    "numbers": "Numbers",
    "apple numbers": "Numbers",
    "spreadsheet": "Numbers",

    "keynote": "Keynote",
    "apple keynote": "Keynote",
    "presentation": "Keynote",
    "slides": "Keynote",

    # Apple Professional Creative Apps
    "final cut pro": "Final Cut Pro",
    "final cut": "Final Cut Pro",
    "fcp": "Final Cut Pro",
    "fcpx": "Final Cut Pro",

    "logic pro": "Logic Pro",
    "logic": "Logic Pro",
    "logic pro x": "Logic Pro",
    "daw": "Logic Pro",

    "garageband": "GarageBand",
    "garage band": "GarageBand",

    "motion": "Motion",
    "apple motion": "Motion",

    "compressor": "Compressor",
    "apple compressor": "Compressor",

    "mainstage": "MainStage",
    "main stage": "MainStage",


    # =========================================================================
    # 3. WEB BROWSERS
    # =========================================================================

    "safari": "Safari",
    "apple safari": "Safari",
    "safari browser": "Safari",

    "chrome": "Google Chrome",
    "google chrome": "Google Chrome",
    "gchrome": "Google Chrome",

    "firefox": "Firefox",
    "mozilla firefox": "Firefox",
    "mozilla": "Firefox",
    "ff": "Firefox",

    "edge": "Microsoft Edge",
    "microsoft edge": "Microsoft Edge",
    "ms edge": "Microsoft Edge",
    "msedge": "Microsoft Edge",

    "opera": "Opera",
    "opera browser": "Opera",
    "opera gx": "Opera GX",
    "operagx": "Opera GX",

    "brave": "Brave Browser",
    "brave browser": "Brave Browser",

    "vivaldi": "Vivaldi",
    "vivaldi browser": "Vivaldi",

    "arc": "Arc",
    "arc browser": "Arc",

    "orion": "Orion",
    "orion browser": "Orion",

    "tor": "Tor Browser",
    "tor browser": "Tor Browser",
    "onion browser": "Tor Browser",

    "duckduckgo": "DuckDuckGo",
    "duck duck go": "DuckDuckGo",
    "ddg": "DuckDuckGo",

    "waterfox": "Waterfox",
    "pale moon": "Pale Moon",
    "sea monkey": "SeaMonkey",
    "maxthon": "Maxthon",
    "mullvad browser": "Mullvad Browser",
    "mullvad": "Mullvad Browser",


    # =========================================================================
    # 4. CODING, DEVELOPMENT & TERMINALS
    # =========================================================================

    # Editors & IDEs
    "vscode": "Visual Studio Code",
    "vs code": "Visual Studio Code",
    "visual studio code": "Visual Studio Code",
    "code": "Visual Studio Code",

    "vscodium": "VSCodium",
    "codium": "VSCodium",

    "cursor": "Cursor",
    "cursor ai": "Cursor",
    "cursor editor": "Cursor",

    "zed": "Zed",
    "zed editor": "Zed",

    "sublime": "Sublime Text",
    "sublime text": "Sublime Text",
    "sublimetext": "Sublime Text",
    "subl": "Sublime Text",

    "notepad++": "Notepad++",
    "npp": "Notepad++",

    "bbedit": "BBEdit",
    "bb edit": "BBEdit",

    "nova": "Nova",
    "panic nova": "Nova",

    "coda": "Coda",
    "espresso": "Espresso",

    "xcode": "Xcode",
    "apple xcode": "Xcode",

    "android studio": "Android Studio",
    "androidstudio": "Android Studio",
    "adb": "Android Studio",

    # JetBrains Suite
    "pycharm": "PyCharm",
    "pycharm professional": "PyCharm",
    "pycharm community": "PyCharm",

    "intellij": "IntelliJ IDEA",
    "intellij idea": "IntelliJ IDEA",
    "idea": "IntelliJ IDEA",

    "webstorm": "WebStorm",
    "web storm": "WebStorm",

    "phpstorm": "PhpStorm",
    "php storm": "PhpStorm",

    "clion": "CLion",

    "rider": "Rider",
    "jetbrains rider": "Rider",

    "datagrip": "DataGrip",
    "data grip": "DataGrip",

    "goland": "GoLand",
    "go land": "GoLand",

    "rubymine": "RubyMine",
    "ruby mine": "RubyMine",

    "appcode": "AppCode",
    "fleet": "Fleet",
    "jetbrains fleet": "Fleet",

    "rustrover": "RustRover",

    # Advanced Terminals
    "iterm": "iTerm",
    "iterm2": "iTerm",
    "i-term": "iTerm",

    "warp": "Warp",
    "warp terminal": "Warp",

    "alacritty": "Alacritty",
    "kitty": "kitty",
    "hyper": "Hyper",
    "wezterm": "WezTerm",
    "tabby": "Tabby",
    "rio": "Rio",

    # API & Database Tools
    "postman": "Postman",
    "insomnia": "Insomnia",
    "paw": "RapidAPI Client",
    "rapidapi": "RapidAPI Client",
    "rapidapi client": "RapidAPI Client",
    "bruno": "Bruno",
    "yaak": "Yaak",

    "tableplus": "TablePlus",
    "table plus": "TablePlus",

    "sequel ace": "Sequel Ace",
    "sequel pro": "Sequel Pro",

    "pgadmin": "pgAdmin 4",
    "pgadmin4": "pgAdmin 4",
    "postgres app": "Postgres",
    "postgresql": "Postgres",

    "dbeaver": "DBeaver",
    "dbeaver community": "DBeaver",

    "mongodb compass": "MongoDB Compass",
    "compass": "MongoDB Compass",

    "redis insight": "Redis Insight",
    "redisinsight": "Redis Insight",

    # Version Control & DevOps
    "git": "GitHub Desktop",
    "github": "GitHub Desktop",
    "github desktop": "GitHub Desktop",

    "gitkraken": "GitKraken",
    "git kraken": "GitKraken",

    "sourcetree": "SourceTree",
    "source tree": "SourceTree",

    "tower": "Tower",
    "git tower": "Tower",

    "fork": "Fork",
    "git fork": "Fork",

    "docker": "Docker",
    "docker desktop": "Docker",
    "container": "Docker",

    "orbstack": "OrbStack",
    "orb stack": "OrbStack",

    "rancher": "Rancher Desktop",
    "podman": "Podman Desktop",

    # Web & File Transfer
    "transmit": "Transmit",
    "panic transmit": "Transmit",

    "cyberduck": "Cyberduck",
    "duck": "Cyberduck",

    "filezilla": "FileZilla",
    "file zilla": "FileZilla",

    "forklift": "ForkLift",
    "fork lift": "ForkLift",

    # Environment Managers
    "python": "IDLE",
    "idle": "IDLE",
    "anaconda": "Anaconda-Navigator",
    "anaconda navigator": "Anaconda-Navigator",
    "conda": "Anaconda-Navigator",
    "jupyter": "JupyterLab",
    "jupyterlab": "JupyterLab",
    "jupyter notebook": "JupyterLab",


    # =========================================================================
    # 5. COMMUNICATION & COLLABORATION
    # =========================================================================

    "discord": "Discord",
    "discord app": "Discord",

    "telegram": "Telegram",
    "telegram desktop": "Telegram",
    "tg": "Telegram",

    "whatsapp": "WhatsApp",
    "whats app": "WhatsApp",
    "whatsapp desktop": "WhatsApp",

    "slack": "Slack",
    "slack app": "Slack",

    "teams": "Microsoft Teams",
    "microsoft teams": "Microsoft Teams",
    "ms teams": "Microsoft Teams",
    "msteams": "Microsoft Teams",

    "zoom": "zoom.us",
    "zoom.us": "zoom.us",
    "zoom cloud meetings": "zoom.us",

    "skype": "Skype",
    "skype for mac": "Skype",

    "signal": "Signal",
    "signal messenger": "Signal",

    "element": "Element",
    "matrix": "Element",

    "viber": "Viber",
    "viber messenger": "Viber",

    "messenger": "Messenger",
    "facebook messenger": "Messenger",
    "fb messenger": "Messenger",

    "wechat": "WeChat",
    "we chat": "WeChat",

    "line": "LINE",
    "line messenger": "LINE",

    "qq": "QQ",
    "qqmusic": "QQ",

    "dingtalk": "DingTalk",
    "lark": "Lark",
    "feishu": "Feishu",

    # Third-Party Email Clients
    "spark": "Spark",
    "spark mail": "Spark",
    "spark desktop": "Spark",

    "airmail": "Airmail",
    "air mail": "Airmail",

    "thunderbird": "Mozilla Thunderbird",
    "mozilla thunderbird": "Mozilla Thunderbird",

    "superhuman": "Superhuman",

    "canary": "Canary Mail",
    "canary mail": "Canary Mail",

    "mimestream": "Mimestream",

    "postbox": "Postbox",

    "boxysuite": "Boxy for Gmail",


    # =========================================================================
    # 6. PRODUCTIVITY, NOTES, PLANNING & LAUNCHERS
    # =========================================================================

    # Knowledge & PKM
    "notion": "Notion",
    "notion app": "Notion",

    "obsidian": "Obsidian",
    "obsidian md": "Obsidian",

    "roam": "Roam Research",
    "roam research": "Roam Research",

    "logseq": "Logseq",

    "evernote": "Evernote",

    "bear": "Bear",
    "bear notes": "Bear",

    "ulysses": "Ulysses",

    "craft": "Craft",
    "craft docs": "Craft",

    "reflect": "Reflect",
    "reflect notes": "Reflect",

    "amplenote": "Amplenote",

    "capacities": "Capacities",

    "anytype": "Anytype",

    "scrivener": "Scrivener",

    "ia writer": "iA Writer",
    "iawriter": "iA Writer",

    "marked": "Marked 2",
    "marked 2": "Marked 2",

    # Task & Project Management
    "todoist": "Todoist",

    "things": "Things",
    "things 3": "Things3",
    "things3": "Things3",

    "omnifocus": "OmniFocus",
    "omni focus": "OmniFocus",
    "omnifocus 3": "OmniFocus",
    "omnifocus 4": "OmniFocus",

    "ticktick": "TickTick",
    "tick tick": "TickTick",

    "trello": "Trello",

    "asana": "Asana",

    "monday": "Monday",
    "monday.com": "Monday",

    "clickup": "ClickUp",
    "click up": "ClickUp",

    "linear": "Linear",

    "height": "Height",

    "joplin": "Joplin",

    # Document & Mind Mapping
    "xmind": "XMind",
    "xmind pro": "XMind",

    "mindnode": "MindNode",
    "mind node": "MindNode",

    "omnigraffle": "OmniGraffle",
    "omni graffle": "OmniGraffle",

    "omniplan": "OmniPlan",

    "omnoutliner": "OmniOutliner",

    # Launchers & Command Bars
    "raycast": "Raycast",

    "alfred": "Alfred",
    "alfred 5": "Alfred 5",
    "alfred 4": "Alfred 4",

    "launcher": "Raycast",
    "spotlight": "Spotlight",


    # =========================================================================
    # 7. CREATIVE, DESIGN, 3D & AUDIO/VIDEO EDITING
    # =========================================================================

    # Adobe Creative Cloud
    "photoshop": "Adobe Photoshop",
    "adobe photoshop": "Adobe Photoshop",
    "ps": "Adobe Photoshop",

    "illustrator": "Adobe Illustrator",
    "adobe illustrator": "Adobe Illustrator",
    "ai": "Adobe Illustrator",

    "premiere": "Adobe Premiere Pro",
    "premiere pro": "Adobe Premiere Pro",
    "adobe premiere": "Adobe Premiere Pro",
    "pr": "Adobe Premiere Pro",

    "after effects": "Adobe After Effects",
    "aftereffects": "Adobe After Effects",
    "adobe after effects": "Adobe After Effects",
    "ae": "Adobe After Effects",

    "indesign": "Adobe InDesign",
    "adobe indesign": "Adobe InDesign",
    "id": "Adobe InDesign",

    "lightroom": "Adobe Lightroom",
    "adobe lightroom": "Adobe Lightroom",
    "lr": "Adobe Lightroom",
    "lightroom classic": "Adobe Lightroom Classic",

    "audition": "Adobe Audition",
    "adobe audition": "Adobe Audition",
    "au": "Adobe Audition",

    "animate": "Adobe Animate",
    "adobe animate": "Adobe Animate",
    "flash": "Adobe Animate",

    "bridge": "Adobe Bridge",
    "adobe bridge": "Adobe Bridge",

    "character animator": "Adobe Character Animator",

    "substance 3d": "Adobe Substance 3D Painter",
    "substance painter": "Adobe Substance 3D Painter",

    "creative cloud": "Adobe Creative Cloud",
    "acc": "Adobe Creative Cloud",

    # Affinity Suite
    "affinity designer": "Affinity Designer",
    "affinity designer 2": "Affinity Designer 2",

    "affinity photo": "Affinity Photo",
    "affinity photo 2": "Affinity Photo 2",

    "affinity publisher": "Affinity Publisher",
    "affinity publisher 2": "Affinity Publisher 2",

    # UI/UX & Vector Design
    "figma": "Figma",
    "figma desktop": "Figma",

    "sketch": "Sketch",
    "sketch app": "Sketch",

    "canva": "Canva",

    "balsamiq": "Balsamiq Wireframes",
    "balsamiq wireframes": "Balsamiq Wireframes",

    "principle": "Principle",

    "framer": "Framer",

    "procreate dreams": "Procreate Dreams",

    # Open Source / Raster Creative
    "blender": "Blender",
    "blender 3d": "Blender",

    "gimp": "GIMP",
    "gimp app": "GIMP",

    "krita": "Krita",

    "inkscape": "Inkscape",

    "pixelmator": "Pixelmator Pro",
    "pixelmator pro": "Pixelmator Pro",

    "photomator": "Photomator",

    # 3D, CAD & Animation
    "cinema 4d": "Maxon Cinema 4D",
    "c4d": "Maxon Cinema 4D",
    "cinema4d": "Maxon Cinema 4D",

    "maya": "Autodesk Maya",
    "autodesk maya": "Autodesk Maya",

    "3ds max": "Autodesk 3ds Max",

    "houdini": "Houdini",
    "sidefx houdini": "Houdini",

    "zbrush": "ZBrush",
    "pixologic zbrush": "ZBrush",

    "sketchup": "SketchUp",
    "sketchup pro": "SketchUp",

    "shapr3d": "Shapr3D",
    "shapr 3d": "Shapr3D",

    "fusion 360": "Autodesk Fusion 360",
    "fusion360": "Autodesk Fusion 360",
    "autodesk fusion": "Autodesk Fusion 360",

    "rhino": "Rhinoceros",
    "rhinoceros": "Rhinoceros",
    "rhino 3d": "Rhinoceros",

    # Professional Video & Color Grading
    "davinci resolve": "DaVinci Resolve",
    "davinci": "DaVinci Resolve",
    "resolve": "DaVinci Resolve",
    "davinci resolve studio": "DaVinci Resolve Studio",

    "capcut": "CapCut",

    "handbrake": "HandBrake",
    "hand brake": "HandBrake",

    "screenflow": "ScreenFlow",
    "screen flow": "ScreenFlow",

    "camtasia": "Camtasia",

    # Professional Audio & DAWs
    "ableton": "Ableton Live",
    "ableton live": "Ableton Live",
    "ableton live suite": "Ableton Live Suite",

    "pro tools": "Pro Tools",
    "protools": "Pro Tools",
    "avid pro tools": "Pro Tools",

    "fl studio": "FL Studio",
    "flstudio": "FL Studio",
    "fruity loops": "FL Studio",

    "reaper": "REAPER",

    "cubase": "Cubase",
    "steinberg cubase": "Cubase",

    "studio one": "Studio One",
    "presonus studio one": "Studio One",

    "bitwig": "Bitwig Studio",
    "bitwig studio": "Bitwig Studio",

    "audacity": "Audacity",

    "izotope rx": "iZotope RX",
    "rx": "iZotope RX",


    # =========================================================================
    # 8. MICROSOFT OFFICE & ENTERPRISE
    # =========================================================================

    "word": "Microsoft Word",
    "microsoft word": "Microsoft Word",
    "ms word": "Microsoft Word",
    "msword": "Microsoft Word",

    "excel": "Microsoft Excel",
    "microsoft excel": "Microsoft Excel",
    "ms excel": "Microsoft Excel",
    "msexcel": "Microsoft Excel",

    "powerpoint": "Microsoft PowerPoint",
    "microsoft powerpoint": "Microsoft PowerPoint",
    "ms powerpoint": "Microsoft PowerPoint",
    "mspowerpoint": "Microsoft PowerPoint",
    "ppt": "Microsoft PowerPoint",

    "outlook": "Microsoft Outlook",
    "microsoft outlook": "Microsoft Outlook",
    "ms outlook": "Microsoft Outlook",

    "onenote": "Microsoft OneNote",
    "microsoft onenote": "Microsoft OneNote",
    "ms onenote": "Microsoft OneNote",

    "one drive": "OneDrive",
    "onedrive": "OneDrive",
    "microsoft onedrive": "OneDrive",

    "to do": "Microsoft To Do",
    "microsoft to do": "Microsoft To Do",
    "ms to do": "Microsoft To Do",

    "defender": "Microsoft Defender",
    "microsoft defender": "Microsoft Defender",

    "company portal": "Company Portal",
    "intune": "Company Portal",


    # =========================================================================
    # 9. GAMING, LAUNCHERS & EMULATION
    # =========================================================================

    # Digital Stores & Launchers
    "steam": "Steam",
    "steam app": "Steam",

    "epic": "Epic Games Launcher",
    "epic games": "Epic Games Launcher",
    "epic games launcher": "Epic Games Launcher",

    "heroic": "Heroic Games Launcher",
    "heroic launcher": "Heroic Games Launcher",

    "gog": "GOG Galaxy",
    "gog galaxy": "GOG Galaxy",

    "battle.net": "Battle.net",
    "battlenet": "Battle.net",
    "blizzard": "Battle.net",

    "riot": "Riot Client",
    "riot client": "Riot Client",
    "league of legends": "League of Legends",
    "lol": "League of Legends",

    "minecraft": "Minecraft",
    "minecraft launcher": "Minecraft Launcher",

    "roblox": "Roblox",
    "roblox player": "Roblox",
    "roblox studio": "Roblox Studio",

    "itch": "itch",
    "itch.io": "itch",

    # Compatibility Layers & Emulators
    "crossover": "CrossOver",
    "codeweavers crossover": "CrossOver",

    "whisky": "Whisky",

    "porting kit": "Porting Kit",

    "openemu": "OpenEmu",
    "open emu": "OpenEmu",

    "dolphin": "Dolphin",
    "dolphin emulator": "Dolphin",

    "pcsx2": "PCSX2",

    "ppsspp": "PPSSPP",

    "rpcs3": "RPCS3",

    "ryujinx": "Ryujinx",

    "suyu": "suyu",

    "retroarch": "RetroArch",

    "aetherxs2": "AetherSX2",


    # =========================================================================
    # 10. MEDIA PLAYERS, UTILITIES & STREAMING
    # =========================================================================

    "spotify": "Spotify",
    "spotify music": "Spotify",

    "vlc": "VLC",
    "vlc media player": "VLC",
    "vlc player": "VLC",

    "iina": "IINA",
    "iina player": "IINA",

    "elmedia": "Elmedia Player",
    "elmedia player": "Elmedia Player",

    "obs": "OBS Studio",
    "obs studio": "OBS Studio",
    "open broadcaster software": "OBS Studio",

    "streamlabs": "Streamlabs Desktop",
    "streamlabs obs": "Streamlabs Desktop",

    "plex": "Plex",
    "plex media player": "Plex",
    "plex desktop": "Plex",

    "jellyfin": "Jellyfin Media Player",

    "kodi": "Kodi",

    "tidal": "TIDAL",

    "deezer": "Deezer",

    "amazon music": "Amazon Music",

    "xld": "X Lossless Decoder",
    "x lossless decoder": "X Lossless Decoder",

    "makemkv": "MakeMKV",

    "mkvtoolnix": "MKVToolNix",


    # =========================================================================
    # 11. CLOUD STORAGE, SYNC & NETWORKING
    # =========================================================================

    "dropbox": "Dropbox",

    "google drive": "Google Drive",
    "gdrive": "Google Drive",
    "google drive stream": "Google Drive",

    "box": "Box Drive",
    "box drive": "Box Drive",

    "pcloud": "pCloud Drive",

    "mega": "MEGAsync",
    "megasync": "MEGAsync",

    "synology drive": "Synology Drive Client",

    "nextcloud": "Nextcloud",

    "owncloud": "ownCloud",

    # VPN & Networking
    "tailscale": "Tailscale",

    "zero tier": "ZeroTier One",
    "zerotier": "ZeroTier One",

    "nordvpn": "NordVPN",
    "nord vpn": "NordVPN",

    "expressvpn": "ExpressVPN",
    "express vpn": "ExpressVPN",

    "proton vpn": "Proton VPN",
    "protonvpn": "Proton VPN",

    "surfshark": "Surfshark",

    "mullvad vpn": "Mullvad VPN",

    "pia": "Private Internet Access",
    "private internet access": "Private Internet Access",

    "wireguard": "WireGuard",

    "openvpn": "OpenVPN Connect",
    "viscosity": "Viscosity",

    "tunnelblick": "Tunnelblick",

    "wireshark": "Wireshark",

    "charles": "Charles",
    "charles proxy": "Charles",

    "proxyman": "Proxyman",


    # =========================================================================
    # 12. VIRTUALIZATION & EMULATION (OS LEVEL)
    # =========================================================================

    "parallels": "Parallels Desktop",
    "parallels desktop": "Parallels Desktop",

    "vmware": "VMware Fusion",
    "vmware fusion": "VMware Fusion",

    "virtualbox": "VirtualBox",
    "oracle virtualbox": "VirtualBox",

    "utm": "UTM",
    "utm virtual machine": "UTM",

    "qemu": "QEMU",


    # =========================================================================
    # 13. SYSTEM UTILITIES, WINDOW MANAGEMENT & ENHANCEMENTS
    # =========================================================================

    # Archivers & Compression
    "the unarchiver": "The Unarchiver",
    "unarchiver": "The Unarchiver",

    "keka": "Keka",

    "7zip": "Keka",
    "7-zip": "Keka",
    "winrar": "Keka",
    "rar": "Keka",

    "archive utility": "Archive Utility",
    "zip": "Archive Utility",

    "peazip": "PeaZip",

    "bandizip": "Bandizip",

    # System Maintenance & Cleaners
    "cleanmymac": "CleanMyMac X",
    "cleanmymac x": "CleanMyMac X",

    "appcleaner": "AppCleaner",
    "app cleaner": "AppCleaner",

    "daisydisk": "DaisyDisk",
    "daisy disk": "DaisyDisk",

    "grandperspective": "GrandPerspective",

    "onyx": "OnyX",

    "stats": "Stats",

    "istat menus": "iStat Menus",
    "istat": "iStat Menus",

    # Window Management & Productivity Tweaks
    "rectangle": "Rectangle",
    "rectangle pro": "Rectangle Pro",

    "magnet": "Magnet",

    "spectacle": "Spectacle",

    "yabai": "yabai",

    "amethyst": "Amethyst",

    "bettertouchtool": "BetterTouchTool",
    "btt": "BetterTouchTool",

    "bartender": "Bartender",
    "bartender 5": "Bartender 5",

    "hidden bar": "Hidden Bar",

    "ice": "Ice",

    "itsycal": "Itsycal",

    "amphetamine": "Amphetamine",
    "caffeine": "Caffeine",

    "flux": "f.lux",
    "f.lux": "f.lux",

    "shottr": "Shottr",

    "cleanshot": "CleanShot X",
    "cleanshot x": "CleanShot X",

    "snagit": "Snagit",

    "popclip": "PopClip",

    "dropzone": "Dropzone 4",
    "dropzone 4": "Dropzone 4",

    "yoink": "Yoink",

    "paste": "Paste",

    "maccy": "Maccy",

    "copyclip": "CopyClip",

    "alt-tab": "AltTab",
    "alttab": "AltTab",

    # PDF & Reader Tools
    "acrobat": "Adobe Acrobat",
    "adobe acrobat": "Adobe Acrobat",
    "acrobat reader": "Adobe Acrobat Reader",
    "pdf reader": "Adobe Acrobat Reader",

    "pdf expert": "PDF Expert",

    "skim": "Skim",

    "zotero": "Zotero",

    "mendeley": "Mendeley Reference Manager",

    "calibre": "calibre",


    # =========================================================================
    # 14. SECURITY, PRIVACY & PASSWORD MANAGERS
    # =========================================================================

    "1password": "1Password",
    "onepassword": "1Password",
    "1password 8": "1Password",

    "bitwarden": "Bitwarden",

    "dashlane": "Dashlane",

    "lastpass": "LastPass",

    "keepassxc": "KeePassXC",

    "enpass": "Enpass",

    "malwarebytes": "Malwarebytes",
    "malware bytes": "Malwarebytes",

    "lulu": "LuLu",

    "little snitch": "Little Snitch",

    "knockknock": "KnockKnock",

    "blockblock": "BlockBlock",


    # =========================================================================
    # 15. AI, HEURISTIC & ASSISTANT TOOLS
    # =========================================================================

    "chatgpt": "ChatGPT",
    "chat gpt": "ChatGPT",
    "openai chatgpt": "ChatGPT",

    "claude": "Claude",
    "anthropic claude": "Claude",

    "macgpt": "MacGPT",

    "ollama": "Ollama",

    "lm studio": "LM Studio",
    "lmstudio": "LM Studio",

    "jan": "Jan",

    "diffusionbee": "DiffusionBee",

    "whisper": "Whisper",

    "perplexica": "Perplexica",
}
    return app_paths.get(app_name.lower(), app_name)

def open_app(app_name):
    # Open the application using the appropriate method for the Mac (for now)
    import subprocess
    if "/" not in app_name:
        try:
            result = subprocess.run(
                ["mdfind", "0", "-name", app_name],
                capture_output=True,
                text=True,
                check=True
                timeout=10
            )

            wanted = app_name.casefold()
            app_matches = sorted(
                path
                for path in result.stdout.split("\0")
                if path # just in case there are empty strings
                and os.path.isdir(path)
                and path.casefold().endswith(".app")
                and os.path.basename(path)[:-4]:casefold() == wanted
            )

            if app_matches:
                selected = app_matches[0]

                if len(app_matches) > 1:
                    for  number, path in enumerate(app_matches,1):
                        print(f"{number}. {path}")
                    choice = input("Choose an app or enter to cancel: ")

                    if not choice.isdigit():
                        return None
                    





        except FileNotFoundError:
            print(f"Application '{app_name}' not found.")
            return False
    name_type = path_to_app(app_name)

    if name_type is None:
        return False
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
        return False
    if not isinstance(result, tuple):
        print("File or folder not found.")
        return False

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