"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] bstn.py                                           """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 22/05/2022 22:38:22                                     """
"""   Updated: 13/07/2022 15:09:29                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import time
from bs4 import BeautifulSoup
from collections import OrderedDict
from ultilities.ThreadManager import *
from ultilities.DelayManager import *
from ultilities.createsession import *
from ultilities.logger import *
from ultilities.CSVManager import getCsvInfo
from ultilities.ProxyManager import *
from ultilities.WebhookManager import *
from ultilities.DiscordRPC import updateRPC
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed


def BSTNEntry(profiles, proxy, tasknumber):
    
    session = CFsession3(proxy)

    ## get main raffle page

    session.headers = OrderedDict([
        ('authority', 'raffle.bstn.com'),
        ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
        ('accept-language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7'),
        ('cache-control', 'max-age=0'),
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga_9FC6HBPLQ6=GS1.1.1653349229.1.0.1653349229.0; _ga=GA1.1.586683679.1653349229; cf_clearance=7G.Q0t9IU1uNEKU4mxY.2JSYMg4pSzuE4p9mtdcXkKU-1653349230-0-150; __cf_bm=l.YGzvseYsvAY4_gcOvOwBbuQxF6vPY2om5QSbK59Ok-1653349230-0-Ac0UT3IPJYJwoCOPK+n0GJbD67sdBMduRGRO+PGsg8vv1Trl3ghrFv17De/4+jVv8SKYnuFpVdz4bCjA98MT62k=',
        ('dnt', '1'),
        # ('referer', 'https://raffle.bstn.com/?__cf_chl_tk=m8RDzeLlSkWZVTCIDlrDt7fVCYGDn_GkBpkNv5V9gMs-1653349228-0-gaNycGzNB_0'),
        # ('sec-ch-ua', '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"'),
        ('sec-ch-ua-mobile', '?0'),
        ('sec-ch-ua-platform', '"macOS"'),
        ('sec-fetch-dest', 'document'),
        ('sec-fetch-mode', 'navigate'),
        ('sec-fetch-site', 'same-origin'),
        ('upgrade-insecure-requests', '1'),
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'),
    ])

    logger(f"Starting Entry.. {profiles['email']}", "BSTN", tasknumber=tasknumber)
    
    try:
        response = session.get('https://raffle.bstn.com/')
    except Exception as e:
        logger("Exception happened: {}".format(str(e)), "BSTN", "error", tasknumber=tasknumber)
        return -1

    try:
        response = session.get(profiles['link'])
    except Exception as e:
        logger("Error while getting raffle url: {}".format(str(e)), "BSTN", "error", tasknumber=tasknumber)
        return -1

    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            raffle_details = json.loads(soup.find("script", {"id":"__NEXT_DATA__"}).text)
            # print(raffle_details)
            variants = raffle_details.get("props").get("pageProps").get("raffleProduct").get("variants")
            #.get("attributes")
            # print(variants)

            size = profiles['size']

            for a in variants:
                # print(a.get("attributes")[0].get("label"))
                if a.get("attributes")[0].get("label") == size: ## bekomme alle sizes
                    # print(a.get("product").get("id"))
                    product_id = a.get("product").get("id")
                    print(product_id)
    except:
        print("problem")

    ###-------------------------------------
    ###      Log in into account            |
    ###-------------------------------------

    logger(f"Logging in.. {profiles['email']}", "BSTN", tasknumber=tasknumber)
    
    json_data = {
        'operationName': 'loginAndRetrieveCustomerData',
        'variables': {
            'email': profiles['email'], # 'sneakercd3@gmail.com',
            'password': profiles['password']# 'Password007!',
        },
        'query': 'mutation loginAndRetrieveCustomerData($email: String!, $password: String!) {\n  loginAndRetrieveCustomerData(email: $email, password: $password) {\n    firstname\n    lastname\n    email\n    instagram_name\n    registered_raffles\n    addresses {\n      id\n      firstname\n      lastname\n      street\n      city\n      region {\n        region_id\n        region_code\n        region\n        __typename\n      }\n      postcode\n      country_code\n      country_name\n      telephone\n      __typename\n    }\n    __typename\n  }\n}',
    }

    try:
        response = session.post('https://raffle.bstn.com/graphql', json=json_data)
    except Exception as e: 
        logger("Error while log in into the account: {}".format(str(e)), "BSTN", "error", tasknumber=tasknumber)
        return -1
        
    if "The account sign-in was incorrect or your account is disabled temporarily." in response.text:
        logger(f"Account is probaly shadow banned or needs to be verified: {response.text}", "BSTN", "error", tasknumber=tasknumber)
        return -1
    else:
        logger(f"Successfully logged in: {profiles['email']}", "BSTN", "success", tasknumber=tasknumber)

    # print(response.text)
    # customer_id = response["data"]["loginAndRetrieveCustomerData"]["addresses"][0]["id"]
    # print(customer_id)

    ###-------------------------------------
    ###   submitting raffle infos           |
    ###-------------------------------------

    
    logger(f"Submitting raffle information.. {profiles['email']}", "BSTN", tasknumber=tasknumber)
    
    json_data = {
        'operationName': 'CreateCustomerAddress',
        'variables': {
            'firstname': profiles['first_name'], # 'Moritz',
            'lastname': profiles['last_name'], # 'Lehmann',
            'street': [
                profiles['address'], # 'Dahlgruenring',
                profiles['housenumber'], # '2',
            ],
            'postcode': profiles['zip'], # '21109',
            'city': profiles['city'], # 'Hamburg',
            'country_code': profiles['country_code'] # 'DE',
        },
        'query': 'mutation CreateCustomerAddress($country_code: CountryCodeEnum!, $street: [String]!, $telephone: String, $postcode: String!, $city: String!, $firstname: String!, $lastname: String!, $company: String, $default_shipping: Boolean, $default_billing: Boolean, $region_id: Int) {\n  createCustomerAddress(\n    input: {country_code: $country_code, street: $street, telephone: $telephone, postcode: $postcode, city: $city, firstname: $firstname, lastname: $lastname, company: $company, default_shipping: $default_shipping, default_billing: $default_billing, region: {region_id: $region_id}}\n  ) {\n    id\n    region {\n      region\n      region_id\n      __typename\n    }\n    firstname\n    lastname\n    country_code\n    country_name\n    company\n    street\n    telephone\n    postcode\n    city\n    __typename\n  }\n}',
    }

    try:
        response = session.post('https://raffle.bstn.com/graphql', json=json_data)
    except Exception as e: 
        logger("Error while submitting raffle information {}".format(str(e)), "BSTN", "error", tasknumber=tasknumber)
        return -1

    # print(response.text)

    try:
        customer_id = json.loads(response.text)["data"]["createCustomerAddress"]["id"]
    except Exception as e: 
        logger("Error while getting contact id {}".format(str(e)), "BSTN", "error", tasknumber=tasknumber)
        return -1
    # print(customer_id)

    # print(response.text)

    ###-------------------------------------
    ###      instagram                      |
    ###-------------------------------------

    ### logger("Submitting instagram information", "BSTN", tasknumber="")

    json_data = {
        'operationName': 'UpdateCustomer',
        'variables': {
            'firstname': profiles['first_name'], # 'Max',
            'email': profiles['email'], # 'sneakercd3@gmail.com',
            'instagram_name': profiles['instagram'] # '@maxmorizt', ## have to be with @ before
        },
        'query': 'mutation UpdateCustomer($firstname: String!, $email: String!, $instagram_name: String!) {\n  updateCustomer(\n    input: {firstname: $firstname, email: $email, instagram_name: $instagram_name}\n  ) {\n    customer {\n      firstname\n      email\n      instagram_name\n      __typename\n    }\n    __typename\n  }\n}',
    }

    try:
        response = session.post('https://raffle.bstn.com/graphql', json=json_data)
    except Exception as e: 
        logger("Error while submitting instagram account{}".format(str(e)), "BSTN", "error", tasknumber=tasknumber)
        return -1
        
    # print(response.text)

    logger(f"Complete the raffle.. {profiles['email']}", "BSTN", tasknumber=tasknumber)
    
    json_data = {
        'operationName': 'RegisterCustomerForProductRaffle',
        'variables': {
            'customer_address_id': customer_id,
            'product_id': product_id, 
        },
        'query': 'mutation RegisterCustomerForProductRaffle($customer_address_id: Int!, $product_id: Int!) {\n  registerCustomerForProductRaffle(\n    customer_address_id: $customer_address_id\n    product_id: $product_id\n  )\n}',
    }
    
    try:
        response = session.post('https://raffle.bstn.com/graphql', json=json_data)
        # print(response.text)
    except Exception as e:
        logger("Exception happened: {}".format(str(e)), "BSTN", "error", tasknumber=tasknumber)
        return -1

    if "Customer is already registered for selected product raffle" in response.text:
        logger(f"Error while submitting the raffle entry: {profiles['email']}, {response.text}", "BSTN", "error", tasknumber=tasknumber)
        # failed_webhook("BSTN", profiles['size'], "Product", profiles['email'], proxy, profiles['link'], "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
        return -1
    else:
        logger(f"SUCCESS - Your Raffle Entry is in: {profiles['email']}", "BSTN", "success", tasknumber=tasknumber)
        # success_webhook("BSTN", profiles['size'], "Product", profiles['email'], proxy, profiles['link'], "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
        return 0

    # if response.status_code == 200:
    #     logger(f"SUCCESS —— Your Raffle Entry is in:", "BSTN", "success", tasknumber="")
    #     return 0 
    # else:
    #     logger(f"Error while submitting the raffle entry: {response.status_code}", "AFEW", "error", tasknumber="")
    #     # return -1


def bstn_main():

    setTitle("Running BSTN")
    
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
            
            result = BSTNEntry(row, chosen_proxy, tasknumber)
            # print(row)
            
            if result == 0:
                success_webhook("BSTN", row['size'], "Product", row['email'], chosen_proxy, threads, maxDelay, row['link'], "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                logger("Webhook sent!", "BSTN", "success", tasknumber=tasknumber)
                successTasks +=1
                               
            else:
                if row in rows_list:
                    tasksFailed.append(row)
                    # print(tasksFailed)
                failed_webhook("BSTN", row['size'], "Product", row['email'], chosen_proxy, threads, maxDelay, row['link'], "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                logger("Webhook Error sent!", "BSTN", "error", tasknumber=tasknumber)
                failedTasks +=1

            resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
            setTitle(f"BSTN - {resultTracker}")
                
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
                
                result = BSTNEntry(newrow, chosen_proxy, tasknumber)
                # print(row)
                
                if result == 0:
                    success_webhook("BSTN", newrow['size'], "Product", newrow['email'], threads, maxDelay, chosen_proxy, newrow['link'], "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                    logger("Webhook sent!", "BSTN", "success", tasknumber=tasknumber)
                    successTasks +=1
                                
                else:
                    failed_webhook("BSTN", newrow['size'], "Product", newrow['email'], threads, maxDelay, chosen_proxy, newrow['link'], "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                    logger("Webhook Error sent!", "BSTN", "error", tasknumber=tasknumber)
                    failedTasks +=1

                resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
                setTitle(f"BSTN - {resultTracker}")
                    
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
                        BSTNEntry, 
                        row, 
                        chosen_proxy, 
                        tasknumber
                        )
                    tasksResult.append(tasks)
                    index +=1

                for task in as_completed(tasksResult):

                    results = task.result()
                    
                    if results == 0:
                        success_webhook("BSTN", row['size'], "Product", row['email'], threads, "ND", chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                        logger("Webhook sent!", "BSTN", "success", tasknumber=tasknumber)
                        successTasks +=1
                    else:
                        failed_webhook("BSTN", row['size'], "Product", row['email'], threads, "ND", chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
                        logger("Webhook Error sent!", "BSTN", "error", tasknumber=tasknumber)
                        failedTasks +=1
                        
                    resultTracker = f"success: {successTasks} / failed: {failedTasks}"
                    setTitle(f"BSTN - {resultTracker}")
                    
    logger("Finished Tasks", "BSTN", "info", tasknumber="DONE")


    