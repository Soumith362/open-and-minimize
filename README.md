DATE(15-06-24 To 26-06-24):   OPEN AND MINIMIZIATION OF NVIDIA APPLICATION:
	Opening and minimizing the app using python script
   By replacing the path of the application we want to  perform the task
>this includes some steps they are:
      1.creating a bat file
      2.finding the correct path that we want to replace  the application in a code.
3.running and performing the task ,whenever you are turning on your pc it should be automayically  open and minimize.

Create a bat file , it will be helpful to start the application whenever when we turn on pc
*Notes*:
- Replace "notepad.exe" with the full path to the application you want to open if it is not in your system PATH.
- Ensure pygetwindow is installed (pip install pygetwindow) and might need pywin32 (pip install pywin32) on Windows.

### Step 2: Setting Up Automatic Startup

#### Windows

1. *Create a Batch File*:
   - Save your Python script as open_and_minimize.py.
   - Create a batch file to run your script: open_and_minimize.bat
     batch
     @echo off
     pythonw "C:\path\to\open_and_minimize.py"
     

2. *Add to Startup*:
   - Press Win + R, type shell:startup, and press Enter. This opens the Startup folder.
   - Place the batch file (open_and_minimize.bat) in this folder.

#### macOS

1. *Create a Shell Script*:
   - Save your Python script as open_and_minimize.py.
   - Create a shell script to run your script:
     sh
     #!/bin/sh
     python3 /path/to/open_and_minimize.py
     

2. *Add to Startup*:
   - Use the launchd service to create a plist file (~/Library/LaunchAgents/com.user.startup.plist):
     xml
     <?xml version="1.0" encoding="UTF-8"?>
     <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
     <plist version="1.0">
     <dict>
         <key>Label</key>
         <string>com.user.startup</string>
         <key>ProgramArguments</key>
         <array>
             <string>/usr/bin/python3</string>
             <string>/path/to/open_and_minimize.py</string>
         </array>
         <key>RunAtLoad</key>
         <true/>
     </dict>
     </plist>
     
   - Load the plist file with:
     sh
     launchctl load ~/Library/LaunchAgents/com.user.startup.plist
     

#### Linux

1. *Create a Shell Script*:
   - Save your Python script as open_and_minimize.py.
   - Create a shell script to run your script:
     sh
     #!/bin/sh
     python3 /path/to/open_and_minimize.py
     

2. *Add to Startup*:
   - Create a .desktop file in ~/.config/autostart:
     ini
     [Desktop Entry]
     Type=Application
     Exec=/path/to/your_script.sh
     Hidden=false
     NoDisplay=false
     X-GNOME-Autostart-enabled=true
     Name[en_US]=OpenAndMinimize
     Name=OpenAndMinimize
     Comment=Open and minimize an application on startup
     

This setup will ensure that your Python script runs and the application is minimized each time the system starts.










PRE REQUESTS BEFORE RUNNING THE CODE:
  1.pip install pygetwindow
  2.pip install pywin32
