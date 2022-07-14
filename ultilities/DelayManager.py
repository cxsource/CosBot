"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] DelayManager.py                                   """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 29/06/2022 17:52:11                                     """
"""   Updated: 12/07/2022 02:39:13                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import time
import questionary
from ultilities.logger import *
from questionary import Validator, ValidationError, prompt
from questionary import Style


class DelayValidator(Validator):
    
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Make sure to enter a delay.",
                cursor_position=len(document.text),
            )

        values = document.text

        try:
            max = int(values)
        except ValueError:
            raise ValidationError(
                message='Do not use weird strings. Enter a number for a delay! (Example: 5)',
                cursor_position=len(document.text))  # Move cursor to end

def EnterDelay(default=""):
    answer = questionary.text("Enter delay in second (Enter 0 for no delay):", style=qstyle(), validate=DelayValidator, default=default).ask()

    if (answer is None):
        return None, None

    values = answer

    try:
       #  min = int(values[0])
        max = int(values)
    except ValueError:
        return EnterDelay()
    return max


def sleeping_delay(delay):
    
    while delay > -1: # 5 größer als -1
        time.sleep(1)
        print("\r            Sleeping for {}s ..".format(delay), end="")
        delay = delay - 1
    print("\r               Continuing...                 ")
    return 



# def waitUntil(delay, threads=False):
	
# 	if (threads is True):
# 		print(f"[{Colors.PURPLE}{getCurrentTime()}{Colors.RESET}] {Colors.BEIGE}Sleeping for {delay} s...{Colors.RESET}")
# 		time.sleep(delay)
# 		print(f"[{Colors.PURPLE}{getCurrentTime()}{Colors.RESET}] {Colors.BEIGE}Sleeped for {delay} s. Continuing..{Colors.RESET}")
# 		return 

	# while delay > -1:
	# 	time.sleep(1)
	# 	print("\r               {}s left before continuing..".format(delay), end="")
	# 	delay = delay - 1

	# print("\r               Continuing...                 ")

# def getCurrentTime():
# 	return datetime.now().strftime("%H:%M:%S:%f")[:-3]


# class DelayValidator(Validator):
    
#     def validate(self, document):
#         if len(document.text) == 0:
#             raise ValidationError(
#                 message="Please enter a delay",
#                 cursor_position=len(document.text),
#             )

#         values = document.text.split(",")

#         if (len(values) != 2):
#             raise ValidationError(
#                 message='Enter a delay in seconds like : 5, 45 (Must be an Number separated by comma)',
#                 cursor_position=len(document.text))  # Move cursor to end

#         try:
#             min = int(values[0])
#             max = int(values[1])
#         except ValueError:
#             raise ValidationError(
#                 message='Enter a delay in seconds like : 5, 45 (Must be an Number separated by comma)',
#                 cursor_position=len(document.text))  # Move cursor to end


