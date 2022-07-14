"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] CaptchaManager.py                                 """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 13/05/2022 09:03:54                                     """
"""   Updated: 23/05/2022 18:36:45                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import json
import time


with open("config.json", "r") as file:
    data = json.load(file)

key = data["CaptchaServices"]["2Captcha"]


"""2 Captcha Support"""

## make sure to change method and version
## version on hcaptcha needs to be empty 

def Recaptchasolver(sitekey, version, pageurl, action="verify", score="0.4", api_key=key):

    try:
        params = {
            "key": api_key,
            "method": "userrecaptcha", ## userrecaptcha
            "version": version,
            "googlekey": sitekey, ## can be also named googlekey or k parameter 
            "pageurl": pageurl,
            "invisible": 0,
            "action": action,
            "min_score": score,
            "json": 1
        }

        api_url = requests.get("http://2captcha.com/in.php", params=params, timeout=600).json()
       
        if api_url["request"] == "ERROR_WRONG_USER_KEY":
            print("Please make sure to use your correct key.")
        elif api_url["request"] == "ERROR_ZERO_BALANCE":
            print("Please top up your 2captcha balance!")
        elif api_url["request"] == "IP_BANNED":
            print("Your IP address is banned due to many frequent attempts to access the server using wrong authorization keys.")

        captcha_id = api_url["request"]

        while True:
            params = {
                "key": api_key,
                "action": "get",
                "id": captcha_id,
                "json": "1"
            }

            api_url = requests.get("http://2captcha.com/res.php", params=params).json()
            
            if api_url["request"] == "CAPCHA_NOT_READY":
                print("Solving captcha ..") ## kann ich im script ändern
                time.sleep(3)
            elif api_url["request"] == "ERROR_ZERO_BALANCE":
                print("Please top up your 2captcha balance!")
            elif api_url["request"] == "ERROR_CAPTCHA_UNSOLVABLE":
                print("error")
            elif api_url["status"] == 1:
                print("Captcha solved!")
                return api_url["request"]
    except Exception as CaptchaERROR:
        print(CaptchaERROR)

def Hcaptchasolver(sitekey, pageurl, api_key=key):

    try:
        params = {
            "key": api_key,
            "method": "hcaptcha", ## hcaptcha
            "sitekey": sitekey, ## can be also named googlekey or k parameter 
            "pageurl": pageurl,
            "invisible": 0,
            "json": 1
        }

        api_url = requests.get("http://2captcha.com/in.php", params=params, timeout=600).json()
       
        if api_url["request"] == "ERROR_WRONG_USER_KEY":
            print("Please make sure to use your correct key.")
        elif api_url["request"] == "ERROR_ZERO_BALANCE":
            print("Please top up your 2captcha balance!")
        elif api_url["request"] == "IP_BANNED":
            print("Your IP address is banned due to many frequent attempts to access the server using wrong authorization keys.")

        captcha_id = api_url["request"]

        while True:
            params = {
                "key": api_key,
                "action": "get",
                "id": captcha_id,
                "json": "1"
            }

            api_url = requests.get("http://2captcha.com/res.php", params=params).json()
            
            # if api_url["request"] == "CAPCHA_NOT_READY":
            #     print("Solving captcha ..") ## kann ich im script ändern
            # time.sleep(2)
            if api_url["request"] == "ERROR_ZERO_BALANCE":
                print("Please top up your 2captcha balance!")
            elif api_url["request"] == "ERROR_CAPTCHA_UNSOLVABLE":
                print("error")
            elif api_url["status"] == 1:
                # print("Captcha solved!")
                return api_url["request"]
    except Exception as CaptchaERROR:
        print(CaptchaERROR)
    
def RecaptchasolverV2(sitekey, pageurl, invisible="0", api_key=key):

    try:
        params = {
            "key": api_key,
            "method": "userrecaptcha", ## userrecaptcha
            "googlekey": sitekey, ## can be also named googlekey or k parameter 
            "pageurl": pageurl,
            "invisible": invisible,
            "json": 1
        }

        api_url = requests.get("http://2captcha.com/in.php", params=params).json()
       
        if api_url["request"] == "ERROR_WRONG_USER_KEY":
            print("Please make sure to use your correct key.")
        elif api_url["request"] == "ERROR_ZERO_BALANCE":
            print("Please top up your 2captcha balance!")
        elif api_url["request"] == "IP_BANNED":
            print("Your IP address is banned due to many frequent attempts to access the server using wrong authorization keys.")

        captcha_id = api_url["request"]

        while True:
            params = {
                "key": api_key,
                "action": "get",
                "id": captcha_id,
                "json": "1"
            }

            api_url = requests.get("http://2captcha.com/res.php", params=params).json()
            
            # if api_url["request"] == "CAPCHA_NOT_READY":
            #     print("Solving captcha ..") ## kann ich im script ändern
            # time.sleep(2)
            if api_url["request"] == "ERROR_ZERO_BALANCE":
                print("Please top up your 2captcha balance!")
            elif api_url["request"] == "ERROR_CAPTCHA_UNSOLVABLE":
                print("error")
            elif api_url["status"] == 1:
                # print("Captcha solved!")
                return api_url["request"]
    except Exception as CaptchaERROR:
        print(CaptchaERROR)
    
# Recaptchasolver(
#     api_key=key,
#     sitekey="6LcCR2cUAAAAANS1Gpq_mDIJ2pQuJphsSQaUEuc9",
#     version="v3",
#     pageurl="https://www.patta.nl/de/account/login"
#     )

# Hcaptchasolver(
#     sitekey="46f5b790-b7e7-401c-98f3-aa19179aed7e",
#     pageurl="https://www.nakedcph.com/en/search/bysearchdefinition/1282"
# )
    


    

    
    
