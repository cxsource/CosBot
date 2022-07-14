"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] ProxyManager.py                                   """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 01/05/2022 20:43:18                                     """
"""   Updated: 12/07/2022 02:37:54                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import csv
import json
import os
import questionary
from ultilities.logger import *
# from createsession import getsession


def getProxies():
    proxyList = []
    proxyFilename = chooseProxyfile()
    with open(f'proxies/{proxyFilename}', 'r') as file:
        for row in file:
            proxyList.append(row.strip())
    return proxyList


def getProxyFiles():
    proxyFileList = []
    folder = os.listdir("proxies/")

    for file in folder:
        if ".txt" in file:
            proxyFileList.append(file)
    return proxyFileList


def chooseProxyfile():
    list = getProxyFiles()

    answer = questionary.select(
            "Which proxy list do you want to use?", style=qstyle(),
            choices=list,
        ).ask()
    return answer


# def ProxyMode():
    
#     with open("config.json", "r") as file:
#         data = json.load(file)
    
#     if data["Proxyless"] == True:
#         getProxies()
#     else:
#         getsession(None)


# getProxies()
        

# def loadingProxies():
    
#     proxies_number = len(getProxies())
#     print(proxies_number)