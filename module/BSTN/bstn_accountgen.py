"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] bstn_accountgen.py                                """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 17/05/2022 11:08:20                                     """
"""   Updated: 12/07/2022 02:48:39                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import random
import time
from ultilities.ThreadManager import *
from ultilities.DelayManager import *
from ultilities.createsession import CFsession
from ultilities.logger import *
from ultilities.CSVManager import getCsvInfo
from ultilities.ProxyManager import *
from ultilities.DiscordRPC import updateRPC
from ultilities.WebhookManager import *
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed


def bstn_accountgen(profiles, proxy, tasknumber):

    session = CFsession(proxy)

    logger(f"Solving Cloudflare.. {profiles['email']}", "BSTN Account Gen", tasknumber=tasknumber)

    headers = {
        'authority': 'www.bstn.com',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'cf_clearance=bqT5WFvxMyxGHNadTfwynA9zDfxz2xRcLzHDkZ_DaEQ-1652777857-0-150; __cf_bm=PhPWJ2q75mTQCNr5ZKHP3wt4t7qLT5fNi8mf0WjdDOE-1652777857-0-ASGt29oPgL3R40JzX54Va9/95HDjoLQK4SnIgRFfuEBu1HEDAT4wIbxOQz4eIgK8QuoR5LsyJVotzFJKXLbrV1U=; gender=men; _ga_9FC6HBPLQ6=GS1.1.1652777856.1.0.1652777858.0; _ALGOLIA=anonymous-f76e196e-712d-478c-8d12-a3f03a53bb34; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; form_key=33wIDfH8eJgtWZSy; cjConsent=MHxZfDB8Tnww; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; scarab.visitor=%227622DAE98BE4DEC8%22; form_key=33wIDfH8eJgtWZSy; PHPSESSID=mb2ndealgu585eds4b4ts3v213; section_data_ids=%7B%22emrssection%22%3A1652777858%2C%22cart%22%3A1652777858%2C%22customer%22%3A1652777858%2C%22wishlist%22%3A1652777858%2C%22rafflesection%22%3A1652777858%7D; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1652777861%2C%22type%22%3A%22category%22%2C%22version%22%3A%227ff7db62-4f82-4346-af4a-421f8a8bf045%22%7D; _gcl_au=1.1.1388763952.1652777861; __gtm_referrer=https%3A%2F%2Fraffle.bstn.com%2F; _gid=GA1.2.229697031.1652777861; _ga=GA1.1.872180635.1652777857; _uetsid=68c057d0d5bf11ec8a99b9c8313837a2; _uetvid=68c037e0d5bf11ec9da13350e14564fa; _fbp=fb.1.1652777861469.1569413978; ABTasty=uid=myzdmqd01k04pzg7&fst=1652777861444&pst=-1&cst=1652777861444&ns=1&pvt=1&pvis=1&th=822959.0.1.1.1.1.1652777861534.1652777861534.1; ABTastySession=mrasn=&sen=1&lp=https%253A%252F%252Fwww.bstn.com%252Feu_de%252Fmen%252Fupcoming.html%253Fcategories%253DMen~Upcoming; cebs=1; _tt_enable_cookie=1; _ttp=49965965-3fdc-40a4-a7af-708e1144a199; cto_bundle=SNvvil9xNFV5OWdSbTVGN0N6a2ZjeUhGWSUyQmpSUVBwVjAxMDVzS1FzRXBHMEc2RFBmNXBNMEpjSjVwMzB6N3l5YTVqa0ZYTWI5Y2ZvUGNtaWsxRXVHM0xicyUyQnlVa2RrbCUyQkR4ZWc4VFd6MjliVGdMbGNiRXdqTE5oa0wlMkZRbXJNbzE4bVV0Qjk2aCUyQmU5cEVmUmJtSWhMUXg0TE5OMTR6SWlrTGFMOGtueG40WHJrVlpzJTNE; _ce.s=v~80738519b3dd3ed5ebf0a583398cfdc4152a0f58~vpv~0~v11.rlc~1652777861877; _ga_NCXNW87L01=GS1.1.1652777861.1.1.1652777896.0; _ga_3480EPZ6W5=GS1.1.1652777861.1.1.1652777897.24',
        'origin': 'https://www.bstn.com',
        'referer': 'https://www.bstn.com/eu_de/men/upcoming.html?categories=Men~Upcoming',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'success_url': '',
        'error_url': '',
        'gender': '1',
        'firstname': profiles['first_name'],
        'lastname': profiles['last_name'],
        'email': profiles["email"],
        'password': profiles['password'],
        'is_subscribed': '1'
        }

    try:
        logger(f"Creating Account.. {profiles['email']}", "BSTN Account Gen", tasknumber=tasknumber)
        time.sleep(2)
        response = session.post('https://www.bstn.com/eu_de/sociallogin/popup/create/', headers=headers, data=data)
    except Exception as e:
        logger("Exception happened: {}".format(str(e)), "BSTN Account Gen", "error", tasknumber=tasknumber)
        return -1
    
    if response.status_code == 200:
        
        if '"error":true' in response.text:
            logger(f"Account already exist: {response.text}", "BSTN Account Gen", "error", tasknumber=tasknumber)
            return -1
        else:
            logger(f"SUCCESS - ACCOUNT GENERATED: {profiles['email']}", "BSTN Account Gen", "success", tasknumber=tasknumber)
            return 0
    else:
        logger(f"Error while creating account on BSTN: {response.status_code}", "BSTN Account Gen", "error", tasknumber=tasknumber)
        return -1


def bstn_gen_main():

    setTitle("Running BSTN Account Generator")
    
    rows_list = getCsvInfo("BSTN")
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
            
            result = bstn_accountgen(row, chosen_proxy, tasknumber)
            # print(row)
            
            if result == 0:
                success_accountgen_webhook("BSTN Account Gen", row['email'], row['password'], threads, maxDelay, chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                logger("Webhook sent!", "BSTN Account Gen", "success", tasknumber=tasknumber)
                successTasks +=1
                               
            else:
                if row in rows_list:
                    tasksFailed.append(row)
                    # print(tasksFailed)
                failed_accountgen_webhook("BSTN Account Gen", row['email'], row['password'], threads, maxDelay, chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                logger("Webhook Error sent!", "BSTN Account Gen", "error", tasknumber=tasknumber)
                failedTasks +=1

            resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
            setTitle(f"BSTN Account Generator - {resultTracker}")
                
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
                
                # resultTracker = f"success: {successTasks} / failed: {failedTasks}" # start ist 0 / 0
                # print(resultTracker)

                updateRPC()
                
                chosen_proxy = random.choice(proxyList)
                proxyList.remove(chosen_proxy)
                
                result = bstn_accountgen(newrow, chosen_proxy, tasknumber)
                # print(row)
                
                if result == 0:
                    success_accountgen_webhook("BSTN Account Gen", newrow['email'], newrow['password'], threads, maxDelay, chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                    logger("Webhook sent!", "BSTN Account Gen", "success", tasknumber=tasknumber)
                    successTasks +=1
                                
                else:
                    failed_accountgen_webhook("BSTN Account Gen", newrow['email'], newrow['password'], threads, maxDelay, chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                    logger("Webhook Error sent!", "BSTN Account Gen", "error", tasknumber=tasknumber)
                    failedTasks +=1

                resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
                setTitle(f"BSTN Account Generator - {resultTracker}")
                    
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
                        bstn_accountgen, 
                        row, 
                        chosen_proxy, 
                        tasknumber
                        )
                    tasksResult.append(tasks)
                    index +=1

                for task in as_completed(tasksResult):

                    results = task.result()
                    
                    if results == 0:
                        success_accountgen_webhook("BSTN Account Gen", row['email'], row['password'], threads, "ND", chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                        logger("Webhook sent!", "BSTN Account Gen", "success", tasknumber=tasknumber)
                        successTasks +=1
                    else:
                        failed_accountgen_webhook("BSTN Account Gen", row['email'], row['password'], threads, "ND", chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                        logger("Webhook Error sent!", "BSTN Account Gen", "error", tasknumber=tasknumber)
                        failedTasks +=1
                        
                    resultTracker = f"success: {successTasks} / failed: {failedTasks}"
                    setTitle(f"BSTN Account Generator - {resultTracker}")
                    
    logger("Finished Tasks", "BSTN Account Gen", "info", tasknumber="DONE")