"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] test.py                                           """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 16/05/2022 01:23:34                                     """
"""   Updated: 16/05/2022 01:25:45                                     """
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


def Recaptchasolver(api_key, sitekey, version, pageurl, action="verify", score="0.4"):

    try:
        params = {
            "key": api_key,
            "method": "usercaptcha", ## usercaptcha or hcaptcha
            "version": version,
            "googlekey": sitekey, ## can be also named googlekey or k parameter 
            "pageurl": pageurl,
            "invisible": 0,
            "action": action,
            "min_score": score,
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

Recaptchasolver(
    api_key=key,
    sitekey="6LcCR2cUAAAAANS1Gpq_mDIJ2pQuJphsSQaUEuc9",
    version="v3",
    pageurl="https://www.patta.nl/de/account/login"
)