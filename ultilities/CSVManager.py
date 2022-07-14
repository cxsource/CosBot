"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] csvManager.py                                     """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 17/04/2022 15:45:27                                     """
"""   Updated: 12/07/2022 02:37:18                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import csv
import os
import questionary
from ultilities.logger import *


"""FOR STORES FOLDER - CSV MANAGER"""

def getCsvInfo(moduleName):
    rowList = []
    csv_name = choosecsv(moduleName)
    with open(f'stores/{moduleName}/{csv_name}', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rowList.append(row)
    return rowList



def getcsv(moduleName):
    files = os.listdir(f"stores/{moduleName}/")
    list_csv = []

    for file in files:
        if ".csv" in file:
            list_csv.append(file)
    return list_csv

def choosecsv(moduleName):
    list = getcsv(moduleName)

    answer = questionary.select(
            "Which csv do you want to use?", style=qstyle(),
            choices=list,
        ).ask()
    return answer

    
"""FOR EMAIL SCRAPER FOLDER - CSV MANAGER-SCR"""

## list of the files in this direction

def get_toolscsv(moduleName):
    list_files = []
    files = os.listdir(f"tools/Email_Scraper/{moduleName}/")
    for file in files:
        if ".csv" in file:
            list_files.append(file)
            # print(list_files)
    return list_files
    
def choose_toolscsv(moduleName):
    list = get_toolscsv(moduleName)
    
    answer = questionary.select(
        "Which csv do you want to use?", style=qstyle(),
        choices=list,
    ).ask()
    return answer

def toolscsv_info(moduleName):
    rowList = []
    csv_name = choose_toolscsv(moduleName)
    with open(f'tools/Email_Scraper/{moduleName}/{csv_name}', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rowList.append(row)
    return rowList

"""FOR CONFIRMER FOLDER - CSV MANAGER"""

def get_confirmer_csv(moduleName):
    list_files = []
    files = os.listdir(f"tools/Confirmer/{moduleName}/")
    for file in files:
        if ".csv" in file:
            list_files.append(file)
            # print(list_files)
    return list_files
    
def choose_confirmer_csv(moduleName):
    list = get_confirmer_csv(moduleName)
    
    answer = questionary.select(
        "Which csv do you want to use?", style=qstyle(),
        choices=list,
    ).ask()
    return answer

def get_confirmer_info(moduleName):
    rowList = []
    csv_name = choose_confirmer_csv(moduleName)
    with open(f'tools/Confirmer/{moduleName}/{csv_name}', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rowList.append(row)
    return rowList