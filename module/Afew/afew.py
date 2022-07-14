"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] afeww.py                                          """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 14/04/2022 13:21:39                                     """
"""   Updated: 13/07/2022 15:01:27                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import random
from bs4 import BeautifulSoup
from requests.exceptions import ProxyError
from ultilities.ThreadManager import *
from ultilities.DelayManager import *
from ultilities.createsession import getsession
from ultilities.CSVManager import getCsvInfo
from ultilities.ProxyManager import *
from ultilities.logger import *
from ultilities.WebhookManager import *
from ultilities.DiscordRPC import updateRPC
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed


def AfewEntry(profile, proxy, tasknumber):

    # res = requests.get(profile["link"])
    # soup = BeautifulSoup(res.text, 'html.parser')
    # name = soup.find_all('title')[0]
    # title = name.text
    # split_title = title.split('|')
    # product_name = split_title[0]
    
    ##
    ## first we create the session for the entries by importing our extern function "createsession"
    
    session = getsession(proxy)
    # session = requests.session()
    
    ## we send a "get" requests to the link of the raffle and to get the information of the raffle
    ## i still need to learn how to scrape the raffle link this part after /cart/ e.g. "39638248325206"


    logger(f"Getting Size.. {profile['email']}", "AFEW", tasknumber=tasknumber)
    try:
        url = profile["link"]

        url_link = url.replace("https://de.afew-store.com", "https://raffles.afew-store.com") \
            .replace("https://en.afew-store.com", "https://raffles.afew-store.com")

        json_link = url_link + ".json"
        
        r = session.get(json_link)
        variants = r.json()["product"]["variants"]

        variant_wanted = "not found"

        if profile["size"] == "random":
            size_info = random.choice(variants)
            variant_wanted = size_info["id"]
            
        for size in variants:
            if size["title"] == profile["size"]:
                variant_wanted = size["id"]
        if variant_wanted == "not found":
            logger("We couldn't find the size.. We will choose a random size for you!", "AFEW", "error", tasknumber=tasknumber)
            size_info = random.choice(variants)
            variant_wanted = size_info["id"]
    except Exception as SizeError:
        logger("There's a problem to scrape the correct sizes...", "AFEW", "error", tasknumber=tasknumber)
        return -1
        

    errorCounter = 0
    
    while True:
        try:
            r = session.get(f"https://raffles.afew-store.com/cart/{variant_wanted}:1")
            break
        except Exception as e:
            errorCounter += 1
            if errorCounter == 3:
                logger("Exception happened, too much retries, stopping task {}".format(str(e)), "AFEW", "error", tasknumber=tasknumber)
                return -1
            else:
                logger("Exception happened, retrying task...", "AFEW", "error", tasknumber=tasknumber)
                continue

    ## getting the "authenticity token" by scraping with Beautifulsoup
    ## getting "action" token for the things after the link

    try:
        soup = BeautifulSoup(r.text, 'html.parser')
        authenticity_token = soup.find("input", {"name": 'authenticity_token'})["value"]
        action = soup.find("form", {"class": 'edit_checkout'})["action"]
    except Exception as AuthenticityError:
        logger("Error while scraping authenticity token : {}".format(str(AuthenticityError)), "AFEW", "error", tasknumber=tasknumber)
        return -1 

    ##
    ## posting the contact information / data for the raffle that we want to enter
    
    headers = {
        'authority': 'raffles.afew-store.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'origin': 'https://raffles.afew-store.com',
        'referer': 'https://raffles.afew-store.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    data = [
        ('_method', 'patch'),
        ('authenticity_token', authenticity_token),
        ('previous_step', 'contact_information'),
        ('step', 'shipping_method'),
        ('checkout[email]', profile['email']),
        ('checkout[attributes][locale]', 'de'),
        ('checkout[attributes][instagram]', profile['instagram']),
        ('checkout[shipping_address][first_name]', profile['first_name']),
        ('checkout[shipping_address][last_name]', profile['last_name']),
        ('checkout[shipping_address][company]', ''),
        ('checkout[shipping_address][address1]', profile['address']),
        ('checkout[shipping_address][address2]', profile['address_2']),
        ('checkout[shipping_address][city]', profile['city']),
        ('checkout[shipping_address][country]', profile['country']),
        ('checkout[shipping_address][province]', profile['region']),
        ('checkout[shipping_address][zip]', profile['zip']),
        ('checkout[shipping_address][phone]', profile['phone']),
        ('checkout[shipping_address][country]', profile['country']), #Germany
        ('checkout[shipping_address][first_name]', profile['first_name']),
        ('checkout[shipping_address][last_name]', profile['last_name']),
        ('checkout[shipping_address][company]', ''),
        ('checkout[shipping_address][address1]', profile['address']),
        ('checkout[shipping_address][address2]', profile['address_2']),
        ('checkout[shipping_address][zip]', profile['zip']),
        ('checkout[shipping_address][city]', profile['city']),
        ('checkout[remember_me]', ''),
        ('checkout[remember_me]', '0'),
        ('checkout[client_details][browser_width]', '702'),
        ('checkout[client_details][browser_height]', '673'),
        ('checkout[client_details][javascript_enabled]', '1'),
        ('checkout[client_details][color_depth]', '30'),
        ('checkout[client_details][java_enabled]', 'false'),
        ('checkout[client_details][browser_tz]', '-120'),
    ]

    try:
        response = session.post('https://raffles.afew-store.com' + action, headers=headers, data=data)
    except ProxyError:
        logger("Proxy Error Happend...", "AFEW", "error", tasknumber=tasknumber)
        return -1 

    if response.status_code != 200: 
        logger("Error while submitting raffle information...", "AFEW", "error", tasknumber=tasknumber)
        return -1
    else:
        logger(f"Submitting Raffle Information.. {profile['email']}" , "AFEW", tasknumber=tasknumber)

    ##
    ## scraping the shipping method for the raffle with BeautifulSoup 

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        shipping_method = soup.find("div", {"class": 'radio-wrapper'})["data-shipping-method"]
    except Exception as ShippingError:
        logger("Error while scraping shipping method: {}".format(str(ShippingError)), "AFEW", "error", tasknumber=tasknumber)
        return -1 

    ##
    ## posting the shipping information for the raffle

    headers = {
        'authority': 'raffles.afew-store.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9',
        'cache-control': 'max-age=0',
        'origin': 'https://raffles.afew-store.com',
        'referer': 'https://raffles.afew-store.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    data = {
        '_method': 'patch',
        'authenticity_token': authenticity_token,
        'previous_step': 'shipping_method',
        'step': 'payment_method',
        'checkout[shipping_rate][id]': shipping_method,
        'checkout[client_details][browser_width]': '603',
        'checkout[client_details][browser_height]': '673',
        'checkout[client_details][javascript_enabled]': '1',
        'checkout[client_details][color_depth]': '30',
        'checkout[client_details][java_enabled]': 'false',
        'checkout[client_details][browser_tz]': '-120',
    }

    try:
        response = session.post('https://raffles.afew-store.com' + action, headers=headers, data=data)
    except ProxyError:
        logger("Proxy Error Happend...", "AFEW", "error", tasknumber=tasknumber)
        return -1 

    if response.status_code != 200:
        logger("Error while submitting shipping information...", "AFEW", "error", tasknumber=tasknumber)
        return -1
    else:
        logger(f"Submitting Shipping Information.. {profile['email']}", "AFEW", tasknumber=tasknumber)

    ##
    ## scraping id for payment gateway

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        payment_gateway = soup.find("div", {"class": 'radio-wrapper content-box__row'})["data-select-gateway"]
    except Exception as PaymentError:
        logger("Error while scraping payment method: {}".format(str(PaymentError)), "AFEW", "error", tasknumber=tasknumber)
        return -1

    ##
    ## the request for reviewing the data and posting the payment method

    headers = {
        'authority': 'raffles.afew-store.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9',
        'cache-control': 'max-age=0',
        'origin': 'https://raffles.afew-store.com',
        'referer': 'https://raffles.afew-store.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    data = {
        '_method': 'patch',
        'authenticity_token': authenticity_token,
        'previous_step': 'payment_method',
        'step': 'review',
        's': '',
        'checkout[payment_gateway]': payment_gateway,
        'checkout[different_billing_address]': 'false',
        'checkout[client_details][browser_width]': '428',
        'checkout[client_details][browser_height]': '673',
        'checkout[client_details][javascript_enabled]': '1',
        'checkout[client_details][color_depth]': '30',
        'checkout[client_details][java_enabled]': 'false',
        'checkout[client_details][browser_tz]': '-120',
    }

    try:
        response = session.post('https://raffles.afew-store.com' + action, headers=headers, data=data)
    except ProxyError:
        logger("Proxy Error Happend...", "AFEw", "error", tasknumber=tasknumber)
        return -1 

    if response.status_code != 200:
        logger("Error while submitting payment information...", "AFEW", "error", tasknumber=tasknumber)
        return -1
    else: 
        logger(f"Submitting Payment Information.. {profile['email']}", "AFEW", tasknumber=tasknumber)
    
    ##
    ## scraping the total price with beautifulsoup

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        total_price = soup.find("input", {"name": 'checkout[total_price]'})["value"]
    except Exception as TotalPriceError:
        logger("Error while scraping total price... ", "AFEW", "error", tasknumber=tasknumber)
        return -1

    ##
    ## getting the total price and finalise the raffle entry 

    headers = {
        'authority': 'raffles.afew-store.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9',
        'cache-control': 'max-age=0',
        'origin': 'https://raffles.afew-store.com',
        'referer': 'https://raffles.afew-store.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    }

    data = {
        '_method': 'patch',
        'authenticity_token': authenticity_token,
        'checkout[total_price]': total_price,
        'complete': '1',
        'checkout[client_details][browser_width]': '330',
        'checkout[client_details][browser_height]': '673',
        'checkout[client_details][javascript_enabled]': '1',
        'checkout[client_details][color_depth]': '30',
        'checkout[client_details][java_enabled]': 'false',
        'checkout[client_details][browser_tz]': '-120',
    }

    try:
        response = session.post('https://raffles.afew-store.com' + action, headers=headers, data=data)
    except ProxyError:
        logger("Proxy Error Happend...", "AFEW", "error", tasknumber=tasknumber)
        return -1 

    if response.status_code == 200:
        logger(f"SUCCESS - Your Raffle Entry is in: {profile['email']}", "AFEW", "success", tasknumber=tasknumber)
        # success_webhook("Afew", profile["size"], product_name, profile["email"], threads, maxDelay, proxy, profile["link"], "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
        return 0
    else:
        logger(f"Error while submitting the raffle entry: {response.status_code}, {profile['email']}", "AFEW", "error", tasknumber=tasknumber)
        # failed_webhook("Afew", profile["size"], product_name, profile["email"], proxy, profile["link"], "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
        return -1

##
## End Task


def afew_main():

    setTitle("Running Afew")
    
    rows_list = getCsvInfo("Afew")
    proxyList = getProxies()

    taskTotal = len(rows_list) ## show me the whole lenght of the list 
    index = 1
    
    failedTasks = 0
    successTasks = 0

    threads = EnterThread() # int(input("How many threads do you want to start: ")

    if threads == 1:
        
        maxDelay = EnterDelay()

        tasksFailed = []

        # res = requests.get(row["link"])
        # soup = BeautifulSoup(res.text, 'html.parser')
        # name = soup.find_all('title')[0]
        # title = name.text
        # split_title = title.split('|')
        # product_name = split_title[0]

        for row in rows_list:

            res = requests.get(row["link"])
            soup = BeautifulSoup(res.text, 'html.parser')
            name = soup.find_all('title')[0]
            title = name.text
            split_title = title.split('|')
            product_name = split_title[0]


            tasknumber = f"{index}/{taskTotal}"
            
            # resultTracker = f"success: {successTasks} / failed: {failedTasks}" # start ist 0 / 0
            # print(resultTracker)

            updateRPC()
            
            chosen_proxy = random.choice(proxyList)
            proxyList.remove(chosen_proxy)
            
            result = AfewEntry(row, chosen_proxy, tasknumber)
            # print(row)
            
            if result == 0:
                success_webhook("Afew", row["size"], product_name, row["email"], threads, maxDelay, chosen_proxy, row["link"], "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
                logger("Webhook sent!", "AFEW", "success", tasknumber=tasknumber)
                successTasks +=1
                # print(resultTracker)
                               
            else:
                if row in rows_list:
                    tasksFailed.append(row)
                    # print(tasksFailed)
                failed_webhook("Afew", row["size"], product_name, row["email"], threads, maxDelay, chosen_proxy, row["link"], "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
                logger("Webhook Error sent!", "AFEW", "error", tasknumber=tasknumber)
                failedTasks +=1

            resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
            setTitle(f"Running Afew - {resultTracker}")
                
            index +=1
            
            sleeping_delay(maxDelay)

        answer = questionary.confirm(
					"Do you want to restart failed tasks?", style=qstyle()
				).ask()
                
        if answer == True:

            taskTotal2 = len(tasksFailed)
            index2 = 1
            
            for newrow in tasksFailed:

                res = requests.get(newrow["link"])
                soup = BeautifulSoup(res.text, 'html.parser')
                name = soup.find_all('title')[0]
                title = name.text
                split_title = title.split('|')
                product_name = split_title[0]

                tasknumber = f"{index2}/{taskTotal2}"
                
                # resultTracker = f"success: {successTasks} / failed: {failedTasks}" # start ist 0 / 0
                # print(resultTracker)

                updateRPC()
                
                chosen_proxy = random.choice(proxyList)
                proxyList.remove(chosen_proxy)
                
                result = AfewEntry(newrow, chosen_proxy, tasknumber)
                # print(row)
                
                if result == 0:
                    success_webhook("Afew", newrow["size"], product_name, newrow["email"], threads, maxDelay, chosen_proxy, newrow["link"], "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
                    logger("Webhook sent!", "AFEW", "success", tasknumber=tasknumber)
                    successTasks +=1
                    # print(resultTracker)
                                
                else:
                    failed_webhook("Afew", newrow["size"], product_name, newrow["email"], threads, maxDelay, chosen_proxy, newrow["link"], "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
                    logger("Webhook Error sent!", "AFEW", "error", tasknumber=tasknumber)
                    failedTasks +=1

                resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
                setTitle(f"Running Afew - {resultTracker}")
                    
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
                        AfewEntry, 
                        row, 
                        chosen_proxy, 
                        tasknumber
                        )
                    tasksResult.append(tasks)
                    index +=1

                for task in as_completed(tasksResult):

                    results = task.result()
                    
                    if results == 0:
                        success_webhook("Afew", row["size"], product_name, row["email"], threads, "ND", chosen_proxy, row["link"], "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
                        logger("Webhook sent!", "AFEW", "success", tasknumber=tasknumber)
                        successTasks +=1
                    else:
                        failed_webhook("Afew", row["size"], product_name, row["email"], threads, "ND", chosen_proxy, row["link"], "https://media.discordapp.net/attachments/812303141114478593/853957258736173096/Bildschirmfoto_2021-06-14_um_13.21.03.png")
                        logger("Webhook Error sent!", "AFEW", "error", tasknumber=tasknumber)
                        failedTasks +=1
                        
                    resultTracker = f"success: {successTasks} / failed: {failedTasks}"
                    setTitle(f"Running Afew - {resultTracker}")
                    
    logger("Finished Tasks", "AFEW", "info", tasknumber="DONE")