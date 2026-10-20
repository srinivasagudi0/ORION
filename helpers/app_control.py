def open_app(app_name):
    # Open the application using the appropriate method for the Mac (for now)
    import subprocess
    try:
        subprocess.run(["open", "-a", app_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to open {app_name}: {e}")
