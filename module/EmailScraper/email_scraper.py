"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] email_scraper.py                                  """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 10/05/2022 11:14:45                                     """
"""   Updated: 07/07/2022 19:16:55                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""
import csv
from datetime import date
from datetime import datetime
from imap_tools import MailBox, A
from bs4 import BeautifulSoup
from ultilities.CSVManager import toolscsv_info
from ultilities.logger import logger
from ultilities.DiscordRPC import updateRPC
from ultilities.WebhookManager import success_email_scraper

def afew_scraper():

    updateRPC("Working for the win ...")

    profiles = toolscsv_info("Afew")
    
    task_total = len(profiles)
    counter = 1 
    
    for task in profiles:

        try:         
            tasknumber = f"{counter}/{task_total}"
            
            email = task["email"]
            password = task["password"]
            sender = "noreply@afew-store.com"
            links_to_find = "https://www.paypal.com/cgi-bin"

            if "gmail.com" in email:
                imap_server = "imap.gmail.com"
                logger(f"Connection to {email} ..", "Email Scraper", tasknumber=tasknumber)
            elif "outlook" in email:
                imap_server = "outlook.office365.com"
                logger(f"Connection to {email} ..", "Email Scraper", tasknumber=tasknumber)
            else:
                logger(f"{email} - We don't support other providers yet. Please open a ticket and ask for it.", "Email Scraper", "error", tasknumber=tasknumber)

            with MailBox(imap_server).login(email, password, 'INBOX') as mailbox:
                logger(f"Successfully connected into {email} ..", "Email Scraper", "success", tasknumber=tasknumber)
                list_links = []
                for msg in mailbox.fetch(A(from_=sender, seen=False), mark_seen=False):
                    body = msg.html ## wandelt die nachrichten es in html um 
                    soup = BeautifulSoup(body, 'html.parser')
                    urls = soup.find_all('a')
                    for url in urls:
                        links = url.attrs['href']
                        if links_to_find in links:
                            logger("Scraping Afew Links ..", "Email Scraper", "success", tasknumber=tasknumber)
                            list_links.append(links)
            savetocsv(list_links, "Afew")
            if len(list_links) == 0:
                logger("No new links have been found!", "Email Scraper", "info", tasknumber=tasknumber)
            else:
                logger(f"{len(list_links)} links have been found!", "Email Scraper", "info", tasknumber=tasknumber)
                success_email_scraper("Afew", f"{len(list_links)} have been found with Cosphix", "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
            counter +=1
        except Exception as e:
            logger("Error while scraping mails: {}".format(str(e)), "Email Scraper", "error", tasknumber=tasknumber)
    print()
    logger("Finished Tasks", "Email Scraper", "info", tasknumber="DONE")


def bstn_scraper():
    
    updateRPC("Working for the win ...")

    profiles = toolscsv_info("BSTN")
    
    task_total = len(profiles)
    counter = 1 
    
    for task in profiles:

        try:         
            tasknumber = f"{counter}/{task_total}"
            
            email = task["email"]
            password = task["password"]
            sender = "no-reply@store.bstn.com"
            links_to_find = "https://www.bstn.com/eu_de/customer/account/confirm/?back_url"
            en_links_to_find = "https://www.bstn.com/uk_en/customer/account/confirm/?back_url"
            eu_links_to_find = "https://www.bstn.com/eu_en/customer/account/confirm/?back_url"

            if "gmail.com" in email:
                imap_server = "imap.gmail.com"
                logger(f"Connection to {email} ..", "Email Scraper", tasknumber=tasknumber)
            elif "outlook" in email:
                imap_server = "outlook.office365.com"
                logger(f"Connection to {email} ..", "Email Scraper", tasknumber=tasknumber)
            else:
                logger(f"{email} - We don't support other providers yet. Please open a ticket and ask for it.", "Email Scraper", "error", tasknumber=tasknumber)

            with MailBox(imap_server).login(email, password, 'INBOX') as mailbox:
                logger(f"Successfully connected into {email} ..", "Email Scraper", "success", tasknumber=tasknumber)
                list_links = []
                for msg in mailbox.fetch(A(from_=sender, seen=False), mark_seen=False):
                    body = msg.html ## wandelt die nachrichten es in html um 
                    soup = BeautifulSoup(body, 'html.parser')
                    urls = soup.find_all('a')
                    for url in urls:
                        links = url.attrs['href']
                        if links_to_find in links:
                            logger("Scraping BSTN Links ..", "Email Scraper", "success", tasknumber=tasknumber)
                            list_links.append(links)
                        if en_links_to_find in links:
                            logger("Scraping BSTN Links ..", "Email Scraper", "success", tasknumber=tasknumber)
                            list_links.append(links)
                        if eu_links_to_find in links:
                            logger("Scraping BSTN Links ..", "Email Scraper", "success", tasknumber=tasknumber)
                            list_links.append(links)
            savetocsv(list_links, "BSTN")
            if len(list_links) == 0:
                logger("No new links have been found!", "Email Scraper", "info", tasknumber=tasknumber)
            else:
                logger(f"{len(list_links)} links have been found!", "Email Scraper", "info", tasknumber=tasknumber)
                success_email_scraper("BSTN", f"{len(list_links)} have been found with Cosphix", "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
            counter +=1
        except Exception as e:
            logger("Error while scraping mails: {}".format(str(e)), "Email Scraper", "error", tasknumber=tasknumber)
    print()
    logger("Finished Tasks", "Email Scraper", "info", tasknumber="DONE")


def woodwood_scraper():
    
    updateRPC("Working for the win ...")

    profiles = toolscsv_info("Woodwood")
    
    task_total = len(profiles)
    counter = 1 
    
    for task in profiles:

        try:         
            tasknumber = f"{counter}/{task_total}"
            
            email = task["email"]
            password = task["password"]
            sender = "raffle@woodwood.com"
            links_to_find = "https://app.rule.io/subscriber/optIn?"

            if "gmail.com" in email:
                imap_server = "imap.gmail.com"
                logger(f"Connection to {email} ..", "Email Scraper", tasknumber=tasknumber)
            elif "outlook" in email:
                imap_server = "outlook.office365.com"
                logger(f"Connection to {email} ..", "Email Scraper", tasknumber=tasknumber)
            else:
                logger(f"{email} - We don't support other providers yet. Please open a ticket and ask for it.", "Email Scraper", "error", tasknumber=tasknumber)

            with MailBox(imap_server).login(email, password, 'INBOX') as mailbox:
                logger(f"Successfully connected into {email} ..", "Email Scraper", "success", tasknumber=tasknumber)
                list_links = []
                for msg in mailbox.fetch(A(from_=sender, seen=False), mark_seen=True):
                    body = msg.html ## wandelt die nachrichten es in html um 
                    soup = BeautifulSoup(body, 'html.parser')
                    urls = soup.find_all('a')
                    for url in urls:
                        links = url.attrs['href']
                        if links_to_find in links:
                            logger("Scraping Woodwood Links ..", "Email Scraper", "success", tasknumber=tasknumber)
                            list_links.append(links)
            savetocsv(list_links, "Woodwood")
            if len(list_links) == 0:
                logger("No new links have been found!", "Email Scraper", "info", tasknumber=tasknumber)
            else:
                logger(f"{len(list_links)} links have been found!", "Email Scraper", "info", tasknumber=tasknumber)
                success_email_scraper("Woodwood", f"{len(list_links)} have been found with Cosphix", "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
            counter +=1
        except Exception as e:
            logger("Error while scraping mails: {}".format(str(e)), "Email Scraper", "error", tasknumber=tasknumber)
    print()
    logger("Finished Tasks", "Email Scraper", "info", tasknumber="DONE")

    
                              
def savetocsv(links, moduleName):
    
    t = datetime.now().strftime("%H:%M")
    d = date.today()
    filename = f"{moduleName}-link-{d}-{t}"
    with open(f'tools/Confirmer/{moduleName}/{filename}.csv', 'a', newline='') as f: ##tools/link_scrapper/Afew/
        writer = csv.writer(f, delimiter=',')
        headers = ['links']
        writer.writerow(headers)
        for link in links:
            writer.writerow([link])