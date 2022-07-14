"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] naked.py                                          """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 14/05/2022 12:45:20                                     """
"""   Updated: 12/07/2022 02:49:27                                     """
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

# Twocaptchasolver key, method, sitekey, version, pageurl

sitekey = "46f5b790-b7e7-401c-98f3-aa19179aed7e"

def NakedEntry(profiles, proxy, tasknumber):

    link = profiles['link']

    ## this is the first requests that will solve CF and access to the first site
    ## i will probably need to check if a token com
    
    session = CFsession(proxy)

    errorCounter = 0
    while True:
        try:
            logger(f"Solving Cloudflare.. {profiles['email']}", "Naked", tasknumber=tasknumber)
            response = session.get(link)
            break

            print(response.status_code)

            if response.status_code == 200:
                csrfToken = session.cookies.get_dict().get("AntiCsrfToken")
                logger(f"Successfully solved Cloudflare.. {profiles['email']}", "Naked", "info", tasknumber=tasknumber)
                # break          
        except Exception as e: 
            logger("Failed to bypass Cloudflare...", "Naked", "error", tasknumber=tasknumber)
            errorCounter += 1
            if errorCounter == 3:
                logger("Too much retries, I am stopping the current task: {}".format(str(e)), "Naked", "error", tasknumber=tasknumber)
                failed_webhook("Naked", "None", "Product", profiles['email'], proxy, profiles['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                return -1
            else:
                logger("Retrying task...", "Naked", "info", tasknumber=tasknumber)
                continue

    ## second requests, where i put all data and post the request to the following 

    logger(f"Submitting Raffle Information.. {profiles['email']}", "Naked", tasknumber=tasknumber)
    
    headers = {
        'authority': 'helpers.rule.se',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9',
        'cache-control': 'max-age=0',
        'origin': 'https://www.nakedcph.com',
        'referer': 'https://www.nakedcph.com/',
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
        'tags[]': profiles['tags'], ## 100755
        'token': profiles['token'], ## c812c1ff-2a5a0fe-efad139-d754416-71e1e60-2ce
        'rule_email': profiles['email'],
        'fields[Raffle.Instagram Handle]': profiles['instagram'],
        'fields[Raffle.Phone Number]': profiles['phone'],
        'fields[Raffle.First Name]': profiles['first_name'],
        'fields[Raffle.Last Name]': profiles['last_name'],
        'fields[Raffle.Shipping Address]': profiles['address'],
        'fields[Raffle.Postal Code]': profiles['zip'],
        'fields[Raffle.City]': profiles['city'],
        'fields[Raffle.Country]': profiles['country_code'], ## DE .. country code
        'fields[SignupSource.ip]': '192.0.0.1',
        'fields[SignupSource.useragent]': 'Mozilla',
        'language': 'sv',
        'g-recaptcha-response': Hcaptchasolver(sitekey=sitekey, pageurl=link),
        'h-captcha-response': Hcaptchasolver(sitekey=sitekey, pageurl=link)
    }

    try:
        response = session.post('https://helpers.rule.se/raffle/naked.php', headers=headers, data=data, allow_redirects=False)
    except Exception as e:
        logger("Exception happened: {}".format(str(e)), "Naked", "error", tasknumber=tasknumber) 
        return -1
        

    if response.status_code == 302 and response.headers['Location'] == "https://www.nakedcph.com/en/775/you-are-now-registered-for-our-fcfs-raffle":
        logger(f"SUCCESS - Your Raffle Entry is in: {profiles['email']}", "Naked", "success", tasknumber=tasknumber)
        # success_webhook("Naked", "None", "Product", profiles['email'], proxy, profiles['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
        return 0
    else:
        logger(f"Error while submitting the raffle entry... {profiles['email']}: {response.status_code} ", "Naked", "error", tasknumber=tasknumber)
        # failed_webhook("Naked", "None", "Product", profiles['email'], proxy, profiles['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
        return -1

def naked_main():

    setTitle("Running Naked")
    
    rows_list = getCsvInfo("Naked")
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
            
            result = NakedEntry(row, chosen_proxy, tasknumber)
            # print(row)
            
            if result == 0:
                success_webhook("Naked", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                logger("Webhook sent!", "Naked", "success", tasknumber=tasknumber)
                successTasks +=1
                               
            else:
                if row in rows_list:
                    tasksFailed.append(row)
                    # print(tasksFailed)
                failed_webhook("Naked", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                logger("Webhook Error sent!", "Naked", "error", tasknumber=tasknumber)
                failedTasks +=1

            resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
            setTitle(f"Running Naked - {resultTracker}")
                
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
                
                result = NakedEntry(newrow, chosen_proxy, tasknumber)
                # print(row)
                
                if result == 0:
                    success_webhook("Naked", "None", "Product", newrow['email'], threads, maxDelay, chosen_proxy, newrow['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                    logger("Webhook sent!", "Naked", "success", tasknumber=tasknumber)
                    successTasks +=1
                                
                else:
                    failed_webhook("Naked", "None", "Product", newrow['email'], threads, maxDelay, chosen_proxy, newrow['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                    logger("Webhook Error sent!", "Naked", "error", tasknumber=tasknumber)
                    failedTasks +=1

                resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
                setTitle(f"Running Naked - {resultTracker}")
                    
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
                        NakedEntry, 
                        row, 
                        chosen_proxy, 
                        tasknumber
                        )
                    tasksResult.append(tasks)
                    index +=1

                for task in as_completed(tasksResult):

                    results = task.result()
                    
                    if results == 0:
                        success_webhook("Naked", "None", "Product", row['email'], threads, "ND", chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                        logger("Webhook sent!", "Naked", "success", tasknumber=tasknumber)
                        successTasks +=1
                    else:
                        failed_webhook("Naked", "None", "Product", row['email'], threads, "ND", chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                        logger("Webhook Error sent!", "Naked", "error", tasknumber=tasknumber)
                        failedTasks +=1
                        
                    resultTracker = f"success: {successTasks} / failed: {failedTasks}"
                    setTitle(f"Running Naked - {resultTracker}")
                    
    logger("Finished Tasks", "Naked", "info", tasknumber="DONE")

