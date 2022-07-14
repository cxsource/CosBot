"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] email_confirmer.py                                """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 11/05/2022 11:33:17                                     """
"""   Updated: 04/07/2022 23:17:46                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

from selenium import webdriver
from ultilities.CSVManager import get_confirmer_info
from ultilities.logger import logger
from ultilities.WebhookManager import *
from ultilities.DiscordRPC import updateRPC
from ultilities.createsession import CFsession
from ultilities.ProxyManager import *
import requests
import random
import platform
import os
import csv
import time

def setup_paypal_login():

    tasknumber = "Attention Needed!"
    try:
        if platform.system() == "Windows":
            driver_path = os.getcwd() + "\\chromedriver.exe"
        elif platform.system() == "Linux":
            driver_path = os.getcwd() + "/chromedriver"
        elif platform.system() == "Darwin":
            driver_path = os.getcwd() + "/chromedriver"
        else:
            logger("Unsupported OS", "Chromedriver", "error", tasknumber=tasknumber)
            return False
        
        #driver_path = r'/Users/charafdissou/Desktop/SourceRaffles_v2/chromedriver'
        
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(driver_path)
        driver.get("https://www.paypal.com/login")
    except Exception as e:
        logger("Download the latest driver in https://chromedriver.chromium.org : {}".format(str(e)), "Email Confirmer", "error", tasknumber=tasknumber)
    logger("Log into your paypal account manually then click enter on the bot..", "Email Confirmer", "info", tasknumber=tasknumber)
    input()
    return driver 


def paypal_confirmer():
    
    ## getting the confirmer csv
    row_list = get_confirmer_info("Afew")
    ## open paypal login
    driver = setup_paypal_login()

    task_total = len(row_list)
    counter = 1 
    
    ## now open the links 
    
    for task in row_list:

        updateRPC("Working for the win ...")

        tasknumber = f"{counter}/{task_total}"
        
        link = task['links']
        try:
            driver.get(link)
            time.sleep(3)
            submit_payment = driver.find_element_by_id("payment-submit-btn")
        except Exception as TimeOut:
            logger("Option 1: The link is probably outdated - Afew links are only 3 hours availabe.", "Email Confirmer", "error", tasknumber) 
            logger("Option 2: Your paypal account cant afford more payments - Use another account.", "Email Confirmer", "error", tasknumber)
            pass
        time.sleep(1)
        try:
            submit_payment.click()
            logger("SUCCESS - Entry is confirmed!", "Afew - Email Confirmer", "success", tasknumber)
            success_confirmer_webhook(link, "https://media.discordapp.net/attachments/812303141114478593/812303561253060658/Bildschirmfoto_2021-01-10_um_02.png")
        except Exception as e:
            logger("FAILED - Couldn't confirm your entry!", "Afew - Email Confirmer", "error", tasknumber)
            failed_confirmer_webhook(link, "https://media.discordapp.net/attachments/812303141114478593/812303561253060658/Bildschirmfoto_2021-01-10_um_02.png")
            pass
        time.sleep(2)
        counter +=1
    logger("Finished Tasks", "Afew - Email Confirmer", "success", tasknumber)

        
def bstn_confirmer():

    rows_list = get_confirmer_info("BSTN")
    proxyList = getProxies()

    task_total = len(rows_list) ## show me the whole lenght of the list 
    counter = 1
    
    for task in rows_list:

        updateRPC("Working for the win ...")

        tasknumber = f"{counter}/{task_total}"

        link = task['links']

        chosen_proxy = random.choice(proxyList)
        # print(chosen_Proxy)
        proxyList.remove(chosen_proxy)

        session = CFsession(chosen_proxy)

        logger("Confirming..", "BSTN - Email Confirmer", tasknumber=tasknumber)

        headers = {
            'authority': 'www.bstn.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'cjConsent=MHxZfDB8Tnww; scarab.visitor=%22608E3E0CAE9A99E8%22; _gcl_au=1.1.907912704.1648038676; _fbp=fb.1.1648038675691.1367979066; _clck=10lrhro|1|f00|0; scarab.profile=%22167574%7C1648038677%22; cf_clearance=yBMQFReX.FyPmhIKSxF6C.KHJKyiDz93kXJNxr26xk0-1652742983-0-150; _ALGOLIA=anonymous-6f49662f-edf5-4cc4-b32c-9fdfe1a8ea04; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1648038675%2C%22type%22%3A%22category%22%2C%22version%22%3A%227ff7db62-4f82-4346-af4a-421f8a8bf045%22%7D; _gid=GA1.2.249330487.1652743251; _tt_enable_cookie=1; _ttp=fec5d3b7-46f0-4d07-a6ba-cf59552c6456; _ga_9FC6HBPLQ6=GS1.1.1652777673.2.0.1652777673.0; cebs=1; section_data_clean=; cto_bundle=oslpbl9VNHo0Zm93RyUyQmh6N1ZHM1p3cDNFQU1STEFHVHVIQlcxS0UlMkJ5ZWlmSWRDTVFoOVZ6JTJCVW9tTzVMYWh1V1QzV0x4ZkIzdkk0d2ZFOXZLTmRRdHVnVjdZaThUR1NjOEhNcmxEc2FXVDUxMCUyRkZIYXhTc2h3JTJGemlvcnlNck85NjJIUGpIS1Z6ekl2SHl5OVlESUhGVTd4Y1h2NVlOam8lMkJpaGRyeHEwQm8wam1tYUZ6d01vbDJmUnhMSmslMkJmZVRPb05Caw; private_content_version=a94959e2292f7e7e5070c6704ca3c2de; PHPSESSID=eeo8dps16h731l64ed9v3j81ll; aa-search=aa-Y3VzdG9tZXItbWFya0Bzb3VyY2VyYWZmbGVzLmNvbS0xNDI3NzEy; __cf_bm=iMi7PCJHG7Lyr6O4Am_EFDg4mT0S53oD1Xmg7fJEDJE-1652796262-0-AccwVuiLe0N75QTLxN9T5TYlECwZRY6zG0VGoI/jNAY/qra/3H7dvMtB/VKP8jO9mZsSRApbnxbbHo21/FX4ytw=; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; form_key=648pa2y5kTeUe7Ri; mage-cache-sessid=true; mage-messages=; form_key=648pa2y5kTeUe7Ri; _ce.s=v~e2ea041e1c498e4d2f8154ece217d0cf0950c240~vpv~2~v11.rlc~1652796264384; _ga_3480EPZ6W5=GS1.1.1652796263.5.1.1652796281.42; _ga_NCXNW87L01=GS1.1.1652796263.4.1.1652796281.0; _ga=GA1.2.1667164530.1648038676; _uetsid=d33f4ae0d56e11ecadf6757711b068f6; _uetvid=21e8a8b0aaa511ecba9599f922c6fbaa; ABTasty=uid=ys1enm9xn53g57e6&fst=1648038675665&pst=1652793201753&cst=1652796264200&ns=4&pvt=9&pvis=2&th=799342.992899.1.1.1.1.1648038678190.1648038678190.1_808212.1004175.1.1.1.1.1648038685591.1648038685591.1_808220.0.3.3.1.1.1648038675706.1648038685593.1_822959.0.9.2.4.1.1648038675730.1652796281390.1; ABTastySession=mrasn=&sen=3&lp=https%253A%252F%252Fwww.bstn.com%252Fuk_en%252Fcustomer%252Faccount%252Findex%252F; section_data_ids=%7B%22cart%22%3A1652796265%2C%22customer%22%3A1652796265%2C%22wishlist%22%3A1652796265%2C%22emrssection%22%3A1652796281%2C%22rafflesection%22%3A1652796282%2C%22compare-products%22%3A1652796265%2C%22last-ordered-items%22%3A1652796265%2C%22directory-data%22%3A1652796265%2C%22instant-purchase%22%3A1652796265%2C%22captcha%22%3A1652796265%2C%22sociallogin%22%3A1652796265%2C%22recently_viewed_product%22%3A1652796265%2C%22recently_compared_product%22%3A1652796265%2C%22product_data_storage%22%3A1652796265%2C%22paypal-billing-agreement%22%3A1652796265%7D',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        }

        try:    
            response = session.get(link, headers=headers, allow_redirects=False)
        except Exception as err:
            logger("Exception happened: {}".format(str(err)), "BSTN - Email Confirmer", "error", tasknumber)
            pass

        if response.status_code == 302:
            logger("SUCCESS - Entry is confirmed!", "BSTN - Email Confirmer", "success", tasknumber)
            success_confirmer_webhook(link, "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
        else:
            logger("FAILED - Couldn't confirm your entry!", "BSTN - Email Confirmer", "error", tasknumber)
            failed_confirmer_webhook(link, "https://media.discordapp.net/attachments/812303141114478593/978354250751025202/Bildschirmfoto_2022-05-23_um_19.50.28.png")
            
        counter +=1
            
    logger("Finished Tasks", "BSTN - Email Confirmer", "info", tasknumber)
            
        # print(response.text)
        # print(response.status_code)


def woodwood_confirmer():

    rows_list = get_confirmer_info("Woodwood")
    proxyList = getProxies()

    task_total = len(rows_list) ## show me the whole lenght of the list 
    counter = 1
    
    for task in rows_list:

        updateRPC("Working for the win ...")

        tasknumber = f"{counter}/{task_total}"

        link = task['links']

        chosen_proxy = random.choice(proxyList)
        # print(chosen_Proxy)
        proxyList.remove(chosen_proxy)

        session = CFsession(chosen_proxy)

        logger("Confirming..", "Woodwood - Email Confirmer", tasknumber=tasknumber)

        headers = {
            'Host': 'app.rule.io',
            # 'Cookie': 'laravel_session=eyJpdiI6Ing4aExRbUZkKy9vQmNYMm41ZC9iRWc9PSIsInZhbHVlIjoiNysvMldkY0JlMXZ0QlJDb3JWOGhlK1Y3ekF2N1hZbFlNODkzQlFqdjhmc2ZuZFV0Z1FsZVFoNnVNeXZWS3RBcjVTdlFDVGpDbzBlY1BORmYrNGxVQWU4ejJQbmdjcEpnT3FkbU1MZG1HclZ5bjlpVUQ4OUd5ZG5UMVhObWtWRlQiLCJtYWMiOiIwOTQ5YWU0NTk0ZGRlNWRiNjZmOWM5MGQ4ZjFmNTg4OTkzNjNmZDBiOTUyZTM5OWQzNTc5MzE0NTE5YTAyZjBhIiwidGFnIjoiIn0%3D',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        try:    
            response = session.get(link, headers=headers, allow_redirects=False)
        except Exception as err:
            logger("Exception happened: {}".format(str(err)), "Woodwood - Email Confirmer", "error", tasknumber)
            pass

        if response.status_code == 302:
            logger("SUCCESS - Entry is confirmed!", "Woodwood - Email Confirmer", "success", tasknumber)
            success_confirmer_webhook(link, "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
        else:
            logger("FAILED - Couldn't confirm your entry!", "Woodwood - Email Confirmer", "error", tasknumber)
            failed_confirmer_webhook(link, "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                
        counter +=1
                
    logger("Finished Tasks", "Woodwood - Email Confirmer", "info", tasknumber)