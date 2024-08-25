import subprocess
import pygetwindow as gw
import time

def open_and_minimize(app_path):
    # Open the application
    process = subprocess.Popen([app_path])

    # Wait for the application window to appear
    time.sleep(2)

    # Find the application window
    windows = gw.getWindowsWithTitle('Untitled - Notepad')
    if windows:
        window = windows[0]
        window.minimize()
    else:
        print("Window not found.")

if __name__ == "__main__":
    # Path to the application, e.g., Notepad
    app_path = "notepad.exe"  # Replace with the path to your application

    open_and_minimize(app_path)
