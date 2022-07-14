"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] woodwood.py                                       """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 26/05/2022 13:54:35                                     """
"""   Updated: 12/07/2022 02:50:27                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import random
from threading import Thread
from ultilities.ThreadManager import *
from ultilities.DelayManager import *
from ultilities.createsession import CFsession
from ultilities.CaptchaManager import *
from ultilities.logger import *
from ultilities.CSVManager import getCsvInfo
from ultilities.ProxyManager import *
from ultilities.DiscordRPC import updateRPC
from ultilities.WebhookManager import *
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed

sitekey = "6LfbPnAUAAAAACqfb_YCtJi7RY0WkK-1T4b9cUO8"

def WoodwoodEntry(profiles, proxy, tasknumber):

    """Create Cloudflare Session & Raffle Page"""
    
    session = CFsession(proxy)

    link = profiles['link']

    errorCounter = 0
    while True:
        try:
            logger(f"Solving Cloudflare.. {profiles['email']}", "Woodwood", tasknumber=tasknumber)
            response = session.get(link)
            break

            print(response.status_code)

            if response.status_code == 200:
                csrfToken = session.cookies.get_dict().get("AntiCsrfToken")
                logger(f"Successfully solved Cloudflare.. {profiles['email']}", "Woodwood", "info", tasknumber=tasknumber)
                # break          
        except Exception as e: 
            logger("Failed to bypass Cloudflare...", "Woodwood", "error", tasknumber=tasknumber)
            errorCounter += 1
            if errorCounter == 3:
                logger("Too much retries, I am stopping the current task: {}".format(str(e)), "Woodwood", "error", tasknumber=tasknumber)
                failed_webhook("Woodwood", "None", "Product", profiles['email'], proxy, profiles['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                return -1
            else:
                logger("Retrying task...", "Woodwood", "info", tasknumber=tasknumber)
                continue

    ## """Posting the raffle data"""

    logger(f"Submitting Raffle Information.. {profiles['email']}", "Woodwood", tasknumber=tasknumber)

    headers = {
        'authority': 'app.rule.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'origin': 'https://www.woodwood.com',
        'referer': 'https://www.woodwood.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }

    data = {
        'tags[]': profiles['tags'], ## 101770
        'token': profiles['token'], ## 4471020e-81f0638-c2d1963-04b2c92-15e0283-a85'
        'rule_email': profiles['email'],
        'fields[Raffle.Phone Number]': profiles['phone'],
        'fields[Raffle.First Name]': profiles['first_name'],
        'fields[Raffle.Last Name]': profiles['last_name'],
        'fields[Raffle.Shipping Address]': profiles['address'],
        'fields[Raffle.Postal Code]': profiles['zip'],
        'fields[Raffle.City]': profiles['city'],
        'fields[Raffle.Country]': profiles['country_code'],
        'fields[SignupSource.ip]': '149.224.227.135',
        'fields[SignupSource.useragent]': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'language': 'sv',
        'g-recaptcha-response': RecaptchasolverV2(sitekey, link, invisible="1")
    }

    try:
        response = session.post('https://app.rule.io/subscriber-form/subscriber', headers=headers, data=data, allow_redirects=False)
    except Exception as e:
        logger("Exception happened: {}".format(str(e)), "Woodwood", "error", tasknumber=tasknumber) 
        return -1

    if response.status_code == 302 and response.headers['Location'] == "https://www.woodwood.com/en/raffle-confirm-email":
        logger(f"SUCCESS - Your Raffle Entry is in: {profiles['email']}", "Woodwood", "success", tasknumber=tasknumber)
        # success_webhook("Woodwood", "None", "Product", profiles['email'], proxy, profiles['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
        return 0
    else:
        logger(f"Error while submitting the raffle entry... {profiles['email']}: {response.status_code} ", "Naked", tasknumber=tasknumber)
        # failed_webhook("Woodwood", "None", "Product", profiles['email'], proxy, profiles['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
        return -1


def woodwood_main():

    setTitle("Running Woodwood")
    
    rows_list = getCsvInfo("Woodwood")
    proxyList = getProxies()

    taskTotal = len(rows_list) ## show me the whole lenght of the list 
    index = 1
    
    failedTasks = 0
    successTasks = 0

    threads = EnterThread() # int(input("How many threads do you want to start: "))

    if threads == 1:
        
        maxDelay = EnterDelay()

        tasksFailed = []

        for row in rows_list:

            tasknumber = f"{index}/{taskTotal}"

            updateRPC()
            
            chosen_proxy = random.choice(proxyList)
            proxyList.remove(chosen_proxy)
            
            result = WoodwoodEntry(row, chosen_proxy, tasknumber)
            # print(row)
            
            if result == 0:
                success_webhook("Woodwood", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                logger("Webhook sent!", "Woodwood", "success", tasknumber=tasknumber)
                successTasks +=1
                               
            else:
                if row in rows_list:
                    tasksFailed.append(row)
                    # print(tasksFailed)
                failed_webhook("Woodwood", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                logger("Webhook Error sent!", "Woodwood", "error", tasknumber=tasknumber)
                failedTasks +=1

            resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
            setTitle(f"Running Woodwood - {resultTracker}")
                
            index +=1
            
            sleeping_delay(maxDelay)

        answer = questionary.confirm(
					"Do you want to restart failed tasks?", style=qstyle()
				).ask()
                
        if answer == True:

            taskTotal2 = len(tasksFailed)
            index2 = 1
            
            for newrow in tasksFailed:

                tasknumber = f"{index2}/{taskTotal2}"
                
                updateRPC()
                
                chosen_proxy = random.choice(proxyList)
                proxyList.remove(chosen_proxy)
                
                result = WoodwoodEntry(newrow, chosen_proxy, tasknumber)
                # print(row)
                
                if result == 0:
                    success_webhook("Woodwood", "None", "Product", newrow['email'], threads, maxDelay, chosen_proxy, newrow['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                    logger("Webhook sent!", "Woodwood", "success", tasknumber=tasknumber)
                    successTasks +=1
                                
                else:
                    failed_webhook("Woodwood", "None", "Product", newrow['email'], threads, maxDelay, chosen_proxy, newrow['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                    logger("Webhook Error sent!", "Woodwood", "error", tasknumber=tasknumber)
                    failedTasks +=1

                resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
                setTitle(f"Running Woodwood - {resultTracker}")
                    
                index2 +=1
                
                sleeping_delay(maxDelay)

    else: 
        
        if threads > 1:
            
            tasksResult = []
            
            with ThreadPoolExecutor(max_workers=threads) as executor:
                    
                for row in rows_list:

                    tasknumber = f"{index}/{taskTotal}"
                    
                    updateRPC()

                    chosen_proxy = random.choice(proxyList)
                    proxyList.remove(chosen_proxy)
                    
                    tasks = executor.submit(
                        WoodwoodEntry, 
                        row, 
                        chosen_proxy, 
                        tasknumber
                        )
                    tasksResult.append(tasks)
                    index +=1

                for task in as_completed(tasksResult):

                    results = task.result()
                    
                    if results == 0:
                        success_webhook("Woodwood", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                        logger("Webhook sent!", "Woodwood", "success", tasknumber=tasknumber)
                        successTasks +=1
                    else:
                        failed_webhook("Woodwood", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                        logger("Webhook Error sent!", "Woodwood", "error", tasknumber=tasknumber)
                        failedTasks +=1
                        
                    resultTracker = f"success: {successTasks} / failed: {failedTasks}"
                    setTitle(f"Running Woodwood - {resultTracker}")
                    
    logger("Finished Tasks", "Woodwood", "info", tasknumber="DONE")

