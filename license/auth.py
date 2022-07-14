"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] auth.py                                           """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 03/05/2022 10:31:53                                     """
"""   Updated: 06/07/2022 18:46:49                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import sys
import time
import json
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
# from ultilities.logger import logger
# from ultilities.logger import auth_logger

def check_license():
    api_key = "pk_cJEH7TYwtp7stUmrgwM3RrdKR7cAhh8R"

    with open("config.json", "r") as file:
        data = json.load(file)
    license_key = data["License"]
    
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    check_key = requests.get(f'https://api.hyper.co/v6/licenses/{license_key}', headers=headers)
    # print(check_key.status_code)
    return check_key

def getusername():
    
    user = check_license()

    if user.status_code == 200:
                userData = user.json()
                username = userData["integrations"]["discord"]["username"]
                discriminator = userData["integrations"]["discord"]["discriminator"]
                discordname = username + "#" + discriminator
                return discordname

def get_license():
    
    user = check_license()
    if user.status_code == 200:
        userData = user.json()
        license = userData["key"]
        return license


def auth(version):
    
    print("\033[33m[License Key] Checking your license... ", end="\r")
    time.sleep(1)

    key = check_license()
    
    if key.status_code == 200:
        print("\033[92m[License Key] Successfully authenticated your license key!", end="\r")
        auth_webhook(version)
        time.sleep(2)
    else: 
        print("\033[91m[License Key] There was an error to authentify your license key.", end="\r")
        time.sleep(2)
        input("")
        sys.exit()
    

def auth_webhook(version):
    
    try:
        webhookURL = "https://discord.com/api/webhooks/993478666300436560/35eGUEd1KyOGyVsuP2913S6x40NLly5xwsGbUahLXSRPLpklaR776yt3u_GywcXdBVMg"
        # create embed object for webhook
        swebhook = DiscordWebhook(
            url=webhookURL,
            username="Cosphix Bot",
            avatar_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
        )
        # create embed object for webhook
        embed = DiscordEmbed(
            title=" Cosphix Authentification Tracker",
            url="",
            color=9795785 # #9578c9
        )
        # set thumbnail
        # embed.set_thumbnail(
        #     url=sitelogo
        # )
        # set footer
        embed.set_footer(
            text="Cosphix Raffles", 
            icon_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
        )
        # set timestamp (default is now)
        embed.set_timestamp()
        # add fields to embed
        embed.add_embed_field(name='Version:', value=version, inline=False)
        embed.add_embed_field(name='License Key:', value=f'{get_license()}', inline=False)
        embed.add_embed_field(name='Information:', value=f'{getusername()} successfully logged in bot', inline=True)


        swebhook.add_embed(embed)
        response = swebhook.execute()
    except Exception as WebhookError:
            pass
        
    