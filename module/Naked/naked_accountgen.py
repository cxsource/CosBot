"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] naked_accountgen.py                               """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 20/05/2022 22:07:15                                     """
"""   Updated: 12/07/2022 02:49:06                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import re
from bs4 import BeautifulSoup
from ultilities.ThreadManager import *
from ultilities.DelayManager import *
from ultilities.logger import *
from ultilities.createsession import*
from ultilities.CaptchaManager import *
from ultilities.CSVManager import getCsvInfo
from ultilities.ProxyManager import *
from ultilities.DiscordRPC import updateRPC
from ultilities.WebhookManager import *
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed

"""
1. Get main page for registration
2. creating account
3. verifying account by scraping remember token
4. update profiles by adding last name 

"""

sitekey = "6LeNqBUUAAAAAFbhC-CS22rwzkZjr_g4vMmqD_qo"

def naked_account_gen(profiles, proxy, tasknumber):

    session = CFsession(proxy)
    
    ## get the login page of naked

    logger(f"Solving Cloudflare.. {profiles['email']}", "Naked Account Gen", tasknumber=tasknumber)

    headers = {
        'authority': 'www.nakedcph.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'nakedcph.state=en-DE-0-0; png.state=FD939RyYvasYCvJdWlqbP+fNB8fO3yjVlB0tU1/oHqxwvZHZ1Osk3EWev93kA007JzlyfcPTY+8Dzw0kVi45yG3cLjyhPK8MekZ8E1PyC9noU2HIhNU+y0442ruKjqhDcXx9gQ==; CookieInformationConsent=%7B%22website_uuid%22%3A%22f9bd9a9d-e73a-46db-96d4-b498c1ae8dd7%22%2C%22timestamp%22%3A%222022-03-05T08%3A25%3A11.173Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.nakedcph.com%2Fen%2Fsearch%2Fbysearchdefinition%2F1184%22%2C%22consent_website%22%3A%22nakedcph.com%22%2C%22consent_domain%22%3A%22www.nakedcph.com%22%2C%22user_uid%22%3A%227397e51c-6e7c-417f-9e03-24f8fd79a9ad%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F97.0.4692.99%20Safari%2F537.36%22%7D; _gcl_au=1.1.1747032226.1646468711; _fbp=fb.1.1646468711317.42364426; cf_clearance=ANX0Im8W4uLRa6FG3JfNShaoXyGqFiQ58i.ucMX9SZM-1652953930-0-1-f1ee6d70.4bfa505a.ff7fb45b-150; AntiCsrfToken=b6cf500bbfc742aebf738549ee5ca19b; __cf_bm=h1.LguRy9ZMfluTiqf2t5ZCLJA5wykbH.8zzXciYnNQ-1653078001-0-AVfRtlKGYlQPz1JyNVgMKtfFUwzn6vq7w2C4AyjSxS8bWoD/KvUuB0dHqniru3nyToAm3yAEnVhA+mvbQ9RwxV0=; _gid=GA1.2.711023216.1653078002; _gat_gtag_UA_36099866_1=1; _ga_JZ8QLBHSKW=GS1.1.1653078001.16.1.1653078205.0; _ga=GA1.2.1720994024.1646468710',
        'referer': 'https://www.nakedcph.com/en/auth/view',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }
    try:
        response = session.get('https://www.nakedcph.com/en/auth/view?type=register', headers=headers)
    except Exception as e:
        logger("Failed to bypass Cloudflare...", "Naked Account Gen", "error", tasknumber=tasknumber)
        return -1

    # if response.status_code == 200:
    #     csrfToken = session.cookies.get_dict().get("AntiCsrfToken")
    #     print(csrfToken)

    ## get the registerpage 

    logger(f"Creating Account.. {profiles['email']}", "Naked Account Gen", tasknumber=tasknumber)

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        CsrfToken = soup.find("input", {"name": '_AntiCsrfToken'})["value"]
        # print(CsrfToken)
    except Exception as CsrfTokenError:
        logger("Error while getting AntiCsrfToken: {}".format(str(CsrfTokenError)), "Naked Account Gen", "error", tasknumber=tasknumber)
        return -1
        

    headers = {
        'X-AntiCsrfToken': CsrfToken,
        'x-requested-with': 'XMLHttpRequest'
    }

    data = {
        'AntiCsrfToken': CsrfToken,
        'action': 'Register',
        'firstName': profiles['first_name'],
        'email': profiles['email'],
        'password': profiles['password'],
        'subscribe': '3', ## do value 3 for subscribe or empty string for nothing
        'termsAccepted': 'true',
        'g-recaptcha-response': RecaptchasolverV2(sitekey, pageurl="https://www.nakedcph.com/en/auth/view?type=register", invisible="1")
    }

    try:
        response = session.post('https://www.nakedcph.com/en/auth/submit', headers=headers, data=data)
    except Exception as e:
        logger("Exception happened: {}".format(str(e)), "Naked Account Gen", "error", tasknumber=tasknumber)
        return -1

    if response.status_code == 200:
        
        if '"Success":false,' in response.text:
            logger(f"Account already exist: {profiles['email']}", "Naked Account Gen", "error", tasknumber=tasknumber)
            # failed_accountgen_webhook("Naked Account Gen", profiles['email'], profiles['password'], proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
            return -1
        else:
            logger(f"Account have been generated: {profiles['email']}", "Naked Account Gen", "info", tasknumber=tasknumber)
    else:
        logger(f"Error while generating the account: {response.status_code}, {profiles['email']}", "Naked Account Gen", "success", tasknumber=tasknumber)
        return -1


    logger(f"Verifying Account.. {profiles['email']}", "Naked Account Gen", tasknumber=tasknumber)

    headers = {
        'Host': 'www.nakedcph.com',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'CookieInformationConsent=%7B%22website_uuid%22%3A%22f9bd9a9d-e73a-46db-96d4-b498c1ae8dd7%22%2C%22timestamp%22%3A%222022-03-21T18%3A44%3A40.491Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.nakedcph.com%2F%22%2C%22consent_website%22%3A%22nakedcph.com%22%2C%22consent_domain%22%3A%22www.nakedcph.com%22%2C%22user_uid%22%3A%229774c4bf-be93-40b1-abad-3ff4ad90ec22%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F99.0.4844.74%20Safari%2F537.36%22%7D; _gcl_au=1.1.2130633205.1647888280; _fbp=fb.1.1647888280626.490796781; cf_clearance=jRtW9JTp5WVwLwGUvTk05iiMfrgSj02XgVuGTi713K4-1647888283-0-1-ca49cfd5.ed7da09f.3d434917-150; _gid=GA1.2.1419068776.1653306384; __cf_bm=dKD.UnV.bc2SZcfsRRnk_tKc1.j93Vc1_IwMi9vZJXg-1653307289-0-ARyN6BQn/vMusFfX4GLupD2P0dHdzou6ecJBX/VObLf218mpPEdYd+xPS94AuB68RyihLAzXF5tnTMNrrxawf/o=; nakedcph.state=en-DE-0-1; AntiCsrfToken=082b8dcab4714923ac8806924aa26065; _gat_gtag_UA_36099866_1=1; _ga_JZ8QLBHSKW=GS1.1.1653306383.3.1.1653307506.0; _ga=GA1.2.999371159.1647888280; __kla_id=eyIkZXhjaGFuZ2VfaWQiOiJ1OURzS1FwTVRxNjR0Y2RlMDBOMVpYdEE5YS1GS3dqUU9XU2ZiT1VlRUFkU3Z2dlg3VmtaN2Y1UEdDSzktdnYzLlhKc1U0ZCJ9; png.state=Ygn7zEVna+dT76ytuoSJCRuJO3FzljhIWjrpmRtmj3hmMnIdvw0Re5TFRYr9tz3OrMRSzY/x9fL/1ukE54ieN0KKmIDowsRJIIamJF1kLPsK3TGTZk7ZjtTWfMDt+2cXU/3LOfK6YFXeY86e/nzsZdAmVQsz7vS/DiI6fp0e8wdRjbxEOmEKnS4Er1KwPqlw6MLjDjibWQpOYpfoU4dOGQSPm0U=',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'dnt': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.nakedcph.com/en/auth/view',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    try:
        response = session.get('https://www.nakedcph.com/en/customer/viewprofile', headers=headers)
    except Exception as CustomePageError:
        logger("Exception happenend on customer page: {}".format(str(CustomePageError)), "Naked Account Gen", "error", tasknumber=tasknumber)
        return -1

    ## get remember me token 
    
    try:
        rememberToken = re.search('<a href="/en/customer/rememberme/(.+?)"', response.text).group(1)
    except Exception as Ttoken:
        logger("Exception happenend while scraping remember token: {}".format(str(Ttoken)), "Naked Account Gen", "error", tasknumber=tasknumber)
        return -1

    headers = {
        'Host': 'www.nakedcph.com',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'CookieInformationConsent=%7B%22website_uuid%22%3A%22f9bd9a9d-e73a-46db-96d4-b498c1ae8dd7%22%2C%22timestamp%22%3A%222022-03-21T18%3A44%3A40.491Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.nakedcph.com%2F%22%2C%22consent_website%22%3A%22nakedcph.com%22%2C%22consent_domain%22%3A%22www.nakedcph.com%22%2C%22user_uid%22%3A%229774c4bf-be93-40b1-abad-3ff4ad90ec22%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F99.0.4844.74%20Safari%2F537.36%22%7D; _gcl_au=1.1.2130633205.1647888280; _fbp=fb.1.1647888280626.490796781; cf_clearance=jRtW9JTp5WVwLwGUvTk05iiMfrgSj02XgVuGTi713K4-1647888283-0-1-ca49cfd5.ed7da09f.3d434917-150; _gid=GA1.2.1419068776.1653306384; nakedcph.state=en-DE-0-1; AntiCsrfToken=082b8dcab4714923ac8806924aa26065; png.state=Ygn7zEVna+dT76ytuoSJCRuJO3FzljhIWjrpmRtmj3hmMnIdvw0Re5TFRYr9tz3OrMRSzY/x9fL/1ukE54ieN0KKmIDowsRJIIamJF1kLPsK3TGTZk7ZjtTWfMDt+2cXU/3LOfK6YFXeY86e/nzsZdAmVQsz7vS/DiI6fp0e8wdRjbxEOmEKnS4Er1KwPqlw6MLjDjibWQpOYpfoU4dOGQSPm0U=; _ga_JZ8QLBHSKW=GS1.1.1653306383.3.1.1653307525.0; _ga=GA1.2.999371159.1647888280; __kla_id=eyIkZmlyc3RfbmFtZSI6Ik1heCIsIiRleGNoYW5nZV9pZCI6IjVESV9ueHZ2V0h5bGRyNHVVcFNEQm1SR2NFbUtvVlZfekhYUXF4TFJNelhVc1ZGMktnYmZjRzQ4RmhXQTdsQUQuWEpzVTRkIn0=',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'dnt': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.nakedcph.com/en/customer/viewprofile',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response = session.get('https://www.nakedcph.com/en/customer/rememberme/' + rememberToken, headers=headers)

    if response.status_code == 200:
        logger(f"Account have been Verified: {profiles['email']}", "Naked Account Gen", "info", tasknumber=tasknumber)

    print(response.status_code)

    ## updating profile 

    # logger(f"Finishing Account.. {profiles['email']}", "Naked Account Gen", tasknumber=tasknumber)

    headers = {
        'authority': 'www.nakedcph.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'CookieInformationConsent=%7B%22website_uuid%22%3A%22f9bd9a9d-e73a-46db-96d4-b498c1ae8dd7%22%2C%22timestamp%22%3A%222022-05-15T15%3A15%3A58.160Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.nakedcph.com%2Fen%2Fsearch%2Fbysearchdefinition%2F1283%22%2C%22consent_website%22%3A%22nakedcph.com%22%2C%22consent_domain%22%3A%22www.nakedcph.com%22%2C%22user_uid%22%3A%2251ba2868-734a-4095-99fb-20bd6aa70feb%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F101.0.4951.64%20Safari%2F537.36%22%7D; _gcl_au=1.1.1557339622.1652627758; _fbp=fb.1.1652627758505.1498415471; cf_clearance=BpGRw2sccJ.W.IwCzyXBnp7eqmvVCzAG5D.WdEPjIDk-1652628365-0-1-f8c6d719.7f9da11c.6508fe67-150; _gid=GA1.2.1451575736.1653220050; __cf_bm=W._oC4I2XRS_8oFD9EN6ghaVh2You7oJ4FZy9la88NU-1653317121-0-AQvSUz22NihwU7mx3n/7URUNnTD0uudQL3kE5gbUA+lL8wbG9UDnunBf5vpYVN1aMX/63H8JH2abjMRPqBPPUvk=; AntiCsrfToken=8526b83673874ccbb83bef95aaa0ce4a; nakedcph.state=en-DE-0-1; png.state=lQjAim7gwOusLyJsmX6p+vYEySyCiUDFQNKgf0EnICuf/iWoQrkDbRoZRND34wbGo9tsGRvA3fGSzvjs7/kJlrFu6cPTLki1+9LBZgqPakiuKewio0HyZoEFLWQhGM/kxE9PhS/8RyaYyef66lxVH6Rd6/0VFTa8HlPZcSOFGnB3qsLm; _ga_JZ8QLBHSKW=GS1.1.1653317121.9.1.1653317265.0; _ga=GA1.2.1014446234.1652627743; __kla_id=eyIkZmlyc3RfbmFtZSI6Ik1heCIsIiRleGNoYW5nZV9pZCI6IkNxUFZoZHY1SklhdGJCZVVYMVNBZTBoZjRUVWFibkcybVFYdG1taDRvMlRVc1ZGMktnYmZjRzQ4RmhXQTdsQUQuWEpzVTRkIn0=',
        'origin': 'https://www.nakedcph.com',
        'referer': 'https://www.nakedcph.com/en/customer/viewprofile',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }

    data = {
        '_AntiCsrfToken': CsrfToken,
        'firstName': profiles['first_name'],
        'lastName': profiles['last_name'],
        'country': profiles['country_code'], ## country code
        'region': [
            '-1',
            '-1',
        ],
        'subscribe': '3',
    }

    try: 
        response = session.post('https://www.nakedcph.com/en/customer/update', headers=headers, data=data)
    except Exception as e:
        logger("Error while updating the account: {}".format(str(CustomePageError)), "Naked Account Gen", "error", tasknumber=tasknumber)
        return -1

    if response.status_code == 200:
        logger(f"SUCCESS - ACCOUNT GENERATED: {profiles['email']}", "Naked Account Gen", "success", tasknumber=tasknumber)
        # success_accountgen_webhook("Naked Account Gen", profiles['email'], profiles['password'], proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
        return 0
    else:
        logger(f"Error while creating account on Naked: {response.text}", "Naked Account Gen", "error", tasknumber=tasknumber)
        # failed_accountgen_webhook("Naked Account Gen", profiles['email'], profiles['password'], proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
        return -1


def naked_gen_main():

    setTitle("Running Naked Account Generator")
    
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
            
            result = naked_account_gen(row, chosen_proxy, tasknumber)
            # print(row)
            
            if result == 0:
                success_accountgen_webhook("Naked Account Gen", row['email'], row['password'], threads, maxDelay, chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                logger("Webhook sent!", "Naked Account Gen", "success", tasknumber=tasknumber)
                successTasks +=1
                               
            else:
                if row in rows_list:
                    tasksFailed.append(row)
                    # print(tasksFailed)
                failed_accountgen_webhook("Naked Account Gen", row['email'], row['password'], threads, maxDelay, chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                logger("Webhook Error sent!", "Naked Account Gen", "error", tasknumber=tasknumber)
                failedTasks +=1

            resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
            setTitle(f"Running Naked Account Generator - {resultTracker}")
                
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
                
                result = naked_account_gen(newrow, chosen_proxy, tasknumber)
                # print(row)
                
                if result == 0:
                    success_accountgen_webhook("Naked Account Gen", newrow['email'], newrow['password'], threads, maxDelay, chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                    logger("Webhook sent!", "Naked Account Gen", "success", tasknumber=tasknumber)
                    successTasks +=1
                                
                else:
                    failed_accountgen_webhook("Naked Account Gen", newrow['email'], newrow['password'], threads, maxDelay, chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                    logger("Webhook Error sent!", "Naked Account Gen", "error", tasknumber=tasknumber)
                    failedTasks +=1

                resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
                setTitle(f"Running Naked Account Generator - {resultTracker}")
                    
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
                        naked_account_gen, 
                        row, 
                        chosen_proxy, 
                        tasknumber
                        )
                    tasksResult.append(tasks)
                    index +=1

                for task in as_completed(tasksResult):

                    results = task.result()
                    
                    if results == 0:
                        success_accountgen_webhook("Naked Account Gen", row['email'], row['password'], threads, "ND", chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                        logger("Webhook sent!", "Naked Account Gen", "success", tasknumber=tasknumber)
                        successTasks +=1
                    else:
                        failed_accountgen_webhook("Naked Account Gen", row['email'], row['password'], threads, "ND", chosen_proxy, "https://media.discordapp.net/attachments/812303141114478593/812303408857612338/Bildschirmfoto_2020-11-28_um_01.png")
                        logger("Webhook Error sent!", "Naked Account Gen", "error", tasknumber=tasknumber)
                        failedTasks +=1
                        
                    resultTracker = f"success: {successTasks} / failed: {failedTasks}"
                    setTitle(f"Running Naked Account Generator - {resultTracker}")
                    
    logger("Finished Tasks", "Naked Account Gen", "info", tasknumber="DONE")
