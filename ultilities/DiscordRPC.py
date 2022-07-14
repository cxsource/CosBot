"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] DiscordRPC.py                                     """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 09/05/2022 22:38:46                                     """
"""   Updated: 06/07/2022 23:20:47                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

from ultilities.logger import logger
from pypresence import Presence
import time


client_id = "994349416158871683"
RPC = Presence(client_id)
try:
    RPC.connect()
except Exception as e:
    pass

def updateRPC(details='Destroying Raffles'):
    try:
        RPC.update(
            buttons=[{"label": "Twitter", "url": "https://twitter.com/cosphix"}],
            details=details, 
            state="Version 0.0.1",
            large_image='cosphixbot', 
            large_text="The beast is here to stay!",
            start=int(time.time())
        )
    except Exception as RPCerror:
        # logger("Error while activating the RPCS", "DiscordRPC" "error")
        pass