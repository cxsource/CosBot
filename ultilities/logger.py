"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] logger.py                                         """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 27/04/2022 13:31:46                                     """
"""   Updated: 13/07/2022 14:40:48                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

from datetime import datetime
from questionary import Style
import ctypes
import time
import os
os.system("")

class colors:

    RED = "\033[91m" # for errors
    BLUE = "\033[94m" # normal entries
    RESET = "\033[0m"
    GREEN = "\033[92m" # for success
    PURPLE = "\033[35m" # for date time 
    BLACK  = '\033[30m'
    YELLOW = '\033[33m'
    BEIGE  = '\033[36m'
    WHITE  = '\033[37m'
    BEIGE  = '\33[36m'
    GREY   = '\33[90m'
    CYAN    = '\033[36m'
    DARK_GREY = "\033[1;30m"
    BROWN = "\033[38;5;215m" #214
    CBLUE = "\033[38;5;81m" #117
    CGREY = "\033[1;38;5;246m"
    CGREEN = "\033[38;5;70m"
       

def getTime():
    return datetime.now().strftime("%H:%M:%S:%f")[:-3]

def clear_line():
    clear = '\x1b[2K'
    return clear

def logger(message, taskname, status="", tasknumber=""):

    taskname = f"{colors.BROWN}{taskname}"
    tasknumber = f"{colors.BROWN}{tasknumber}"

    if status == "success":
        message = f"{colors.CGREEN}{message}"
    elif status == "error":
        message = f"{colors.RED}{message}"
    elif status == "info":
        message = f"{colors.YELLOW}{message}"
    else:
        message = f"{colors.DARK_GREY}{message}"

    formatedMessage = f"[{colors.CBLUE}{getTime()}{colors.RESET}][{taskname}{colors.RESET}][{tasknumber}{colors.RESET}] {message}{colors.RESET}"
    print(formatedMessage)
    # print(f'\r{formatedMessage}', end=clear_line())
    # time.sleep(2)

    # message
    

def auth_logger(message, status=""):
    if status == "success":
        message = f"{colors.CGREEN}{message}"
    elif status == "error":
        message = f"{colors.RED}{message}"
    elif status == "info":
        message = f"{colors.YELLOW}{message}"
    else:
        message = f"{colors.DARK_GREY}{message}"

    formatedMessage = f"{message}{colors.RESET}"
    print(formatedMessage)
    
def setTitle(title):
	if (os.name == "nt"):
		ctypes.windll.kernel32.SetConsoleTitleW(title)
	else:
		print(f"\33]0;{title}\a", end='', flush=True)


def qstyle():
    
    custom_style_fancy = Style([
		('qmark', 'fg:#45d0eb bold'),       # token in front of the question
		('question', 'fg:#45d0eb bold'),    # question text
		('answer', 'fg:#d6862b bold'),      # submitted answer text behind the question
		('pointer', 'fg:#45d0eb bold'),     # pointer used in select and checkbox prompts
		('highlighted', 'fg:#45d0eb bold'), # pointed-at choice in select and checkbox prompts
		('selected', 'fg:#45d0eb'),         # style for a selected item of a checkbox
		('separator', 'fg:#45d0eb'),        # separator in lists
		('instruction', 'fg:#92a4af'),      # user instructions for select, rawselect, checkbox
		('text', ''),                       # plain text
		('disabled', 'fg:#858585 italic')   # disabled choices for select and checkbox prompts
	])

    return custom_style_fancy


# logger("Success Submitting Raffle Entry..", "AFEW")