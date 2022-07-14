"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] AutoUpdater.py                                    """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 14/07/2022 21:31:34                                     """
"""   Updated: 15/07/2022 00:09:31                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import base64
import os, sys, subprocess
from termcolor import *
from colorama import *
from ultilities.logger import logger
from CLI.main_cli import getVersion
os.system("")

name = f"CosphixBot-{getVersion()}.exe"

def updater():

    with open('version.txt') as file:
        current_version = file.read()

    ghg = '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' # "API KEY"
    username = 'cxsource' # 'USERNAME OF THE OWNER OF THE REPO'
    repo = 'rbot' # 'NAME OF THE REPO'

    def check_version():
        headers = {
            "Authorization": "token " + ghg
        }
        r  = requests.get(f"https://api.github.com/repos/{username}/{repo}/contents/version.txt", headers=headers)
        data = r.json()
        # print(data)
        # print(r.status_code)
        file_content = data['content']
        file_content_encoding = data.get('encoding')
        if file_content_encoding == 'base64':
            file_content = base64.b64decode(file_content).decode("utf-8", "ignore").strip()
        return file_content

    newest_version = check_version()

    def comparison():
        if newest_version == current_version:
            return True
        else:
            return False
        
    def update():

        download_executable = 'CosphixBot.exe' # 'NAME OF EXE IN GITHUB REPO'

        headers = {
            "Authorization": "token " + ghg
        }
        try:
            r = requests.get(f"https://api.github.com/repos/{username}/{repo}/contents", headers=headers)
        except Exception as e:
            print("\033[91m[UPDATE FAILED] There was an error to get the latest update...")
            input()
            exit()
        data = r.json()
        # print(data)
        for i in data:
            if i['name'] == download_executable:
                URL = i['download_url']
                # print(URL)
        if URL:
            try:
                response = requests.get(URL, headers=headers)
                # print(response.content)
            except Exception as e:
                print("\033[91m[UPDATE FAILED] There was an error to get the latest update...")
                exit()

            with open(name, 'wb') as f: # 'NAME OF NEW EXE (ONE DOWNLOADING)'
                f.write(response.content) # writes the new version to the new exe
            with open("version.txt", "w") as f:
                f.write(newest_version) # adds new version number to version.txt
            print("\033[92m[SOFTWARE UPDATE] Successfully downloaded the latest update! Launching now...")

            if sys.platform == "win32":
                os.startfile(name)
            else:
                try:
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    subprocess.call([opener, "CosphixBot.exe"])
                except Exception as e:
                    print("\033[91m[UPDATE FAILED] File doesn't exists")
            # os.startfile(f'THEBOTMacOS') # starts the new exe ## NAME OF NEW EXE (ONE DOWNLOADING -- SAME AS LINE 59 ONE)

        else:
            print("\033[91m[UPDATE FAILED] There was an error to get the latest update...")
            exit()

    def main():
        get_comparison = comparison()
        if get_comparison == False:
            print("\033[33m[SOFTWARE UPDATE] New update is available.. ")
            print("\033[1;30m[SOFTWARE UPDATE] Downloading the latest update.. ")
            update()
            exit()
        else:
            print("\033[92m[UPDATE] Cosphix is already up to date!", end="\r")
            
    main()

updater()



