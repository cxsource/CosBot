"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] ThreadDelay.py                                    """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 30/06/2022 01:39:50                                     """
"""   Updated: 12/07/2022 02:38:20                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import time
import questionary
from ultilities.logger import *
from questionary import Validator, ValidationError, prompt
from questionary import Style

class ThreadValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(
                message="Make sure to enter a thread.",
                cursor_position=len(document.text),
            )
        try:
            min = int(document.text)
        except ValueError:
            raise ValidationError(
                message='Do not use weird strings. Enter a number for a delay! (Example: 1)',
                cursor_position=len(document.text))  # Move cursor to end

def EnterThread(default=""):
    answer = questionary.text("Enter a thread number:", style=qstyle(), validate=ThreadValidator, default=default).ask()

    if (answer is None):
        return (1)

    try:
        threadsNumber = int(answer)
    except ValueError:
        return EnterThread()

    return (threadsNumber)


