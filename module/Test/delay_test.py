"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] DelayManager.py                                   """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 29/06/2022 17:52:11                                     """
"""   Updated: 29/06/2022 20:22:35                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import questionary
from questionary import Validator, ValidationError, prompt
from questionary import Style
import random
import os
import ctypes
import time

from itertools import islice
from datetime import datetime

"""
	Colors Class
		permit to use Colors everywhere.
"""

class Colors:

	RED = "\033[91m"
	BLUE = "\033[94m"
	RESET = "\033[0m"
	GREEN = "\033[92m"
	PURPLE = "\033[35m"
	BLACK  = '\033[30m'
	YELLOW = '\033[33m'
	BEIGE  = '\033[36m'
	WHITE  = '\033[37m'

class DelayValidator(Validator):
    
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Please enter a delay",
                cursor_position=len(document.text),
            )

        values = document.text.split(",")

        if (len(values) != 2):
            raise ValidationError(
                message='Enter a delay in seconds like : 5, 45 (Must be an Number separated by comma)',
                cursor_position=len(document.text))  # Move cursor to end

        try:
            min = int(values[0])
            max = int(values[1])
        except ValueError:
            raise ValidationError(
                message='Enter a delay in seconds like : 5, 45 (Must be an Number separated by comma)',
                cursor_position=len(document.text))  # Move cursor to end

def EnterDelay(default=""):
    answer = questionary.text("Enter delay in seconds here (Separated by comma like 1,5)", validate=DelayValidator, default=default).ask()

    if (answer is None):
        return None, None

    values = answer.split(",")

    try:
        min = int(values[0])
        max = int(values[1])
    except ValueError:
        return EnterDelay()

    return (min, max)


def sleeping_delay(delay):

    print(f"Sleeping for {delay} s...")
    time.sleep(delay)
    return



# def waitUntil(delay, threads=False):
	
# 	if (threads is True):
# 		print(f"[{Colors.PURPLE}{getCurrentTime()}{Colors.RESET}] {Colors.BEIGE}Sleeping for {delay} s...{Colors.RESET}")
# 		time.sleep(delay)
# 		print(f"[{Colors.PURPLE}{getCurrentTime()}{Colors.RESET}] {Colors.BEIGE}Sleeped for {delay} s. Continuing..{Colors.RESET}")
# 		return 

# 	while delay > -1:
# 		time.sleep(1)
# 		print("\r               {}s left before continuing..".format(delay), end="")
# 		delay = delay - 1

# 	print("\r               Continuing...                 ")

def getCurrentTime():
	return datetime.now().strftime("%H:%M:%S:%f")[:-3]




def test():

    minDelay, maxDelay = EnterDelay("5, 10")
    
    sleeping_delay(random.randint(minDelay, maxDelay))

    print("Hello")

    sleeping_delay(random.randint(minDelay, maxDelay))

    print("Wie gehts")
    print("")

    