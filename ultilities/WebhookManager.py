"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] WebhookManager.py                                 """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 04/05/2022 00:01:23                                     """
"""   Updated: 06/07/2022 12:00:11                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

from discord_webhook import DiscordWebhook, DiscordEmbed
from ultilities.logger import logger
import requests
import json


with open("config.json", "r") as file:
    data = json.load(file)

"""ENTRY WEBHOOK"""
    
def success_webhook(sitename, size, product, email, threads, delay, proxy, link, sitelogo):
    try:
        webhookURL = data["WebhookURL"]
        # create embed object for webhook
        swebhook = DiscordWebhook(
            url=webhookURL,
            username="Cosphix Bot",
            avatar_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
        )
        # create embed object for webhook
        embed = DiscordEmbed(
            title="SUCCESS - YOUR RAFFLE ENTRY IS IN ! ✅",
            url=link,
            color=6017433 ##5bd199
        )
        # set thumbnail
        embed.set_thumbnail(
            url=sitelogo
        )
        # set footer
        embed.set_footer(
            text="Cosphix Raffles", 
            icon_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
        )
        # set timestamp (default is now)
        embed.set_timestamp()
        # add fields to embed
        embed.add_embed_field(name='Productname:', value=product, inline=True)
        embed.add_embed_field(name='Store:', value=sitename, inline=True)
        embed.add_embed_field(name='Sizes:', value=size, inline=True)
        embed.add_embed_field(name='Email:', value=f"||{email}||", inline=True)
        embed.add_embed_field(name='Threads / Delay:', value=f"{threads} / {delay}", inline=True)
        embed.add_embed_field(name='Proxy:', value=f"||{proxy}||", inline=True)

        swebhook.add_embed(embed)
        response = swebhook.execute()
    except Exception as WebhookError:
            logger("Error sending webhook...", "WEBHOOK", "error")


def failed_webhook(sitename, size, product, email, threads, delay, proxy, link, sitelogo):
    webhookURL = data["WebhookURL"]
    # create embed object for webhook
    fwebhook = DiscordWebhook(
        url=webhookURL,
        username="Cosphix Bot",
        avatar_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # create embed object for webhook
    embed = DiscordEmbed(
        title="FAILED - RAFFLE ENTRY IS NOT IN ! ❌",
        url=link,
        color=13720411 ##d15b5b
    )
    # set thumbnail
    embed.set_thumbnail(
        url=sitelogo
    )
    # set footer
    embed.set_footer(
        text="Cosphix Raffles", 
        icon_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # set timestamp (default is now)
    embed.set_timestamp()
    # add fields to embed
    embed.add_embed_field(name='Productname:', value=product, inline=True)
    embed.add_embed_field(name='Store:', value=sitename, inline=True)
    embed.add_embed_field(name='Sizes:', value=size, inline=True)
    embed.add_embed_field(name='Email:', value=f"||{email}||", inline=True)
    embed.add_embed_field(name='Threads / Delay:', value=f"{threads} / {delay}", inline=True)
    embed.add_embed_field(name='Proxy:', value=f"||{proxy}||", inline=True)

    fwebhook.add_embed(embed)
    response = fwebhook.execute()

    
"""ACCOUNT GEN WEBHOOK"""

def success_accountgen_webhook(sitename, email, password, threads, delay, proxy, logo):
    webhookURL = data["WebhookURL"]
    # create embed object for webhook
    swebhook = DiscordWebhook(
        url=webhookURL,
        username="Cosphix Bot",
        avatar_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # create embed object for webhook
    embed = DiscordEmbed(
        title="SUCCESS - ACCOUNT GENERATED ! ✅",
        url= None,
        color=13422939 ##ccd15b
    )
    # set thumbnail
    embed.set_thumbnail(
        url=logo
    )
    # set footer
    embed.set_footer(
        text="Cosphix Raffles", 
        icon_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # set timestamp (default is now)
    embed.set_timestamp()
    # add fields to embed
    embed.add_embed_field(name='Email:', value=email, inline=True)
    embed.add_embed_field(name='Password:', value=f"||{password}||", inline=True)
    embed.add_embed_field(name='Store:', value=sitename, inline=True)
    embed.add_embed_field(name='Threads / Delay:', value=f"{threads} / {delay}", inline=True)
    embed.add_embed_field(name='Proxy:', value=f"||{proxy}||", inline=True)

    swebhook.add_embed(embed)
    response = swebhook.execute()


def failed_accountgen_webhook(sitename, email, password, threads, delay, proxy, logo):
    webhookURL = data["WebhookURL"]
    # create embed object for webhook
    fwebhook = DiscordWebhook(
        url=webhookURL,
        username="Cosphix Bot",
        avatar_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # create embed object for webhook
    embed = DiscordEmbed(
        title="FAILED - ACCOUNT ALREADY EXSIST! ❌",
        url= None,
        color=13720411 ##d15b5b
    )
    # set thumbnail
    embed.set_thumbnail(
        url=logo
    )
    # set footer
    embed.set_footer(
        text="Cosphix Raffles", 
        icon_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # set timestamp (default is now)
    embed.set_timestamp()
    # add fields to embed
    embed.add_embed_field(name='Email:', value=email, inline=True)
    embed.add_embed_field(name='Password:', value=f"||{password}||", inline=True)
    embed.add_embed_field(name='Store:', value=sitename, inline=True)
    embed.add_embed_field(name='Threads / Delay:', value=f"{threads} / {delay}", inline=True)
    embed.add_embed_field(name='Proxy:', value=f"||{proxy}||", inline=True)

    fwebhook.add_embed(embed)
    response = fwebhook.execute()


"""TEST WEBHOOK"""

def test():
    webhookURL = data["WebhookURL"]
    webhook = DiscordWebhook(
        url= webhookURL, 
        content='Webhook Message'
    )
    response = webhook.execute()


"""CONFIRMER MODE"""

def success_confirmer_webhook(link, logo):
    webhookURL = data["WebhookURL"]
    # create embed object for webhook
    swebhook = DiscordWebhook(
        url=webhookURL,
        username="Cosphix Bot",
        avatar_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # create embed object for webhook
    embed = DiscordEmbed(
        title="SUCCESS - ENTRY IS CONFIRMED ! ✅",
        url= None,
        color=6017433 ##5bd199
    )
    # set thumbnail
    embed.set_thumbnail(
        url=logo
    )
    # set footer
    embed.set_footer(
        text="Cosphix Raffles", 
        icon_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # set timestamp (default is now)
    embed.set_timestamp()
    # add fields to embed
    embed.add_embed_field(name='LINK:', value=link, inline=True)

    swebhook.add_embed(embed)
    response = swebhook.execute()


def failed_confirmer_webhook(link, logo):
    webhookURL = data["WebhookURL"]
    # create embed object for webhook
    cwebhook = DiscordWebhook(
        url=webhookURL,
        username="Cosphix Bot",
        avatar_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # create embed object for webhook
    embed = DiscordEmbed(
        title="FAILED - ENTRY IS CONFIRMED ! ❌",
        url= None,
        color=13720411 ##d15b5b
    )
    # set thumbnail
    embed.set_thumbnail(
        url=logo
    )
    # set footer
    embed.set_footer(
        text="Cosphix Raffles", 
        icon_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # set timestamp (default is now)
    embed.set_timestamp()
    # add fields to embed
    embed.add_embed_field(name='LINK:', value=link, inline=True)

    cwebhook.add_embed(embed)
    response = cwebhook.execute()


"""EMAIL SCRAPER"""

def success_email_scraper(sitename, link, sitelogo):
    webhookURL = data["WebhookURL"]
    # create embed object for webhook
    swebhook = DiscordWebhook(
        url=webhookURL,
        username="Cosphix Bot",
        avatar_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # create embed object for webhook
    embed = DiscordEmbed(
        title="LINK SCRAPER ! 🔗",
        url= None,
        color=13422939 ##ccd15b
    )
    # set thumbnail
    embed.set_thumbnail(
        url=sitelogo
    )
    # set footer
    embed.set_footer(
        text="Cosphix Raffles", 
        icon_url="https://media.discordapp.net/attachments/971320786398896128/971321736761069579/background2_cosphix.png"
    )
    # set timestamp (default is now)
    embed.set_timestamp()
    # add fields to embed
    embed.add_embed_field(name='Store:', value=sitename, inline=False)
    embed.add_embed_field(name='Link:', value=link, inline=False)

    swebhook.add_embed(embed)
    response = swebhook.execute()



# failed_webhook("Afew", "Nike Dunk Low", "test@webhook.com", "proxiesurl")
# entry_webhook("Afew", "Nike Dunk Low", "test@webhook.com", "proxiesurl")
# accountgen_webhook("Afew", "test@webhook.com", "HDEdcjcnd", "proxyused@dhdjene:djedjle")
