"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] nakedv2.py                                        """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 23/05/2022 21:55:09                                     """
"""   Updated: 24/05/2022 00:55:12                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import random
from threading import Thread
from bs4 import BeautifulSoup
from ultilities.logger import logger
from ultilities.createsession import CFsession, CFsession1
from ultilities.CaptchaManager import *

sitekey = "6LeNqBUUAAAAAFbhC-CS22rwzkZjr_g4vMmqD_qo"

def nakedv2():
    
    session = CFsession1()

    headers = {
        'Host': 'www.nakedcph.com',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'CookieInformationConsent=%7B%22website_uuid%22%3A%22f9bd9a9d-e73a-46db-96d4-b498c1ae8dd7%22%2C%22timestamp%22%3A%222021-11-01T12%3A03%3A40.123Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.nakedcph.com%2F%22%2C%22consent_website%22%3A%22nakedcph.com%22%2C%22consent_domain%22%3A%22www.nakedcph.com%22%2C%22user_uid%22%3A%22ab26cf11-cff4-40ac-96cd-9d3eb5676b76%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F95.0.4638.54%20Safari%2F537.36%22%7D; _gcl_au=1.1.61116221.1651566141; _gid=GA1.2.1699209968.1653215477; cf_clearance=zKEKeKvBdxJpwRODEcSBS4HRb_ZbjguE5PYBTEDgIVE-1653311619-0-1-71c8f8d8.3daf5fa5.26c9a738-150; nakedcph.state=en-DE-0-1; png.state=QePOeIE8iiOvKzKrn3qorw3CaEFRWgk15urfN0xPTDavwKEbRzPKcMAvOh6Pp8ilRwfE4Rn+B2DJmmTkAGqwchB+T9KgKV8yDO1qJRvVm3GEog88L+Y3BB+pyRqa2cP2TipsNf/fkmLtF390V16j1+0LR5U=; __cf_bm=BcY9pWASerLXW_13GJsQvQvaSjXalCda06ipgRGaDt0-1653337996-0-ARowkIjuCgAwAOwqfsaoUu2f6YMBXbiFO7YukPyQSjSONtRJiurgT390OSYEvtlo2cBvkKtWmelmV2k5fEh50HI=; AntiCsrfToken=dfeacffe76eb42719f7d4ef2fbf8f61c; _gat_gtag_UA_36099866_1=1; _ga_JZ8QLBHSKW=GS1.1.1653335308.51.1.1653337999.0; _ga=GA1.2.48066875.1635768219; __kla_id=eyIkZXhjaGFuZ2VfaWQiOiJfZ2dGVWtmMzU5cWpVODUtYjNpakNYRzd5ZW1nbTQzSnVScE5mRzQ1ZnQ0PS5YSnNVNGQiLCIkZmlyc3RfbmFtZSI6IkNoYXJhZiIsIiRsYXN0X25hbWUiOiJEaXNzb3UifQ==',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'dnt': '1',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response = session.get('https://www.nakedcph.com/en/auth/view', headers=headers)


    soup = BeautifulSoup(response.text, 'html.parser')
    CsrfToken = soup.find("input", {"name": '_AntiCsrfToken'})["value"]
    print(CsrfToken)  

    headers = {
        'X-AntiCsrfToken': CsrfToken,
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '_AntiCsrfToken': CsrfToken,
        'action': 'Login',
        'email': 'victria@cosphixbot.com',
        'password': 'Password007!',
        'g-recaptcha-response': RecaptchasolverV2(sitekey, pageurl="https://www.nakedcph.com/en/auth/view?type=register")  
    }

    response = session.post('https://www.nakedcph.com/en/auth/submit', headers=headers, data=data)
    print(response.text)

    headers = {
        'Host': 'www.nakedcph.com',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'CookieInformationConsent=%7B%22website_uuid%22%3A%22f9bd9a9d-e73a-46db-96d4-b498c1ae8dd7%22%2C%22timestamp%22%3A%222021-11-01T12%3A03%3A40.123Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.nakedcph.com%2F%22%2C%22consent_website%22%3A%22nakedcph.com%22%2C%22consent_domain%22%3A%22www.nakedcph.com%22%2C%22user_uid%22%3A%22ab26cf11-cff4-40ac-96cd-9d3eb5676b76%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F95.0.4638.54%20Safari%2F537.36%22%7D; _gcl_au=1.1.61116221.1651566141; _gid=GA1.2.1699209968.1653215477; cf_clearance=zKEKeKvBdxJpwRODEcSBS4HRb_ZbjguE5PYBTEDgIVE-1653311619-0-1-71c8f8d8.3daf5fa5.26c9a738-150; nakedcph.state=en-DE-0-1; png.state=QePOeIE8iiOvKzKrn3qorw3CaEFRWgk15urfN0xPTDavwKEbRzPKcMAvOh6Pp8ilRwfE4Rn+B2DJmmTkAGqwchB+T9KgKV8yDO1qJRvVm3GEog88L+Y3BB+pyRqa2cP2TipsNf/fkmLtF390V16j1+0LR5U=; __cf_bm=BcY9pWASerLXW_13GJsQvQvaSjXalCda06ipgRGaDt0-1653337996-0-ARowkIjuCgAwAOwqfsaoUu2f6YMBXbiFO7YukPyQSjSONtRJiurgT390OSYEvtlo2cBvkKtWmelmV2k5fEh50HI=; AntiCsrfToken=dfeacffe76eb42719f7d4ef2fbf8f61c; _ga_JZ8QLBHSKW=GS1.1.1653335308.51.1.1653338039.0; _ga=GA1.2.48066875.1635768219; __kla_id=eyIkZXhjaGFuZ2VfaWQiOiJfZ2dGVWtmMzU5cWpVODUtYjNpakNYRzd5ZW1nbTQzSnVScE5mRzQ1ZnQ0PS5YSnNVNGQiLCIkZmlyc3RfbmFtZSI6IkNoYXJhZiIsIiRsYXN0X25hbWUiOiJEaXNzb3UifQ==',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'dnt': '1',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    getProductsRequest = session.get('https://www.nakedcph.com/en/2/sneakers', headers=headers)

    print(response.status_code)

    urlList = []

    if getProductsRequest.status_code == 200:
        soup = BeautifulSoup(getProductsRequest.text, 'html.parser')
        products = soup.find("div", {"id": "products"})
        print(products)
        for a in soup.find_all('a', href=True):
            url = a['href']
            list_brand = ["new-balance", "reebok", "nike", "jordan", "adidas"]
            for brand in list_brand:
                if brand in url and "product" in url:
                    urlList.append("https://www.nakedcph.com" + url)
                    print(urlList)
    else:
        logger("Error while getting the release page ...", "NakedV2", "error", tasknumber="tasknumber")
    

    # productUrl = random.choice(urlList)
    # logger(f"We are using this URL: {productUrl}", "NakedV2", "info", tasknumber="tasknumber")
    # urlList.remove(productUrl)
    # logger(f"We'll remove the link from the list: {productUrl}", "NakedV2", "info", tasknumber="tasknumber")

    productUrl = "https://www.nakedcph.com/en/product/12687/nike-air-max-97-nh-dr0157-001"
    
    productInformationRequest = session.get(productUrl)
    
    if productInformationRequest.status_code == 200:
        logger("Getting the product page..", "NakedV2", tasknumber="tasknumber")
        soup = BeautifulSoup(productInformationRequest.text, 'html.parser')
        options = [option for option in soup.find_all('option') if option.get("value") != "-1"]
        optionId = random.choice(options).get('value')
        did = productUrl.split("https://www.nakedcph.com/en/product/")[1].split("/")[0]
    else:
        logger("Error to access product page...", "NakedV2", "error", tasknumber="tasknumber")

    
    logger("Checking out product..", "NakedV2", tasknumber="tasknumber")

    cookies = {
        'AntiCsrfToken': session.cookies.get("AntiCsrfToken"),
        'nakedcph.state': session.cookies.get("nakedcph.state"),
        'cartRevisionCookie': '2',
        'png.state': session.cookies.get("png.state"),
        'cart-state': 'check-email',
        '__cf_bm': session.cookies.get("__cf_bm"),
    }

    headers = {
        'authority': 'www.nakedcph.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'x-anticsrftoken': session.cookies.get("AntiCsrfToken"),
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-gpc': '1',
        'origin': 'https://www.nakedcph.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': productUrl,
    }

    data = {
        '_AntiCsrfToken': session.cookies.get("AntiCsrfToken"),
        'did': 12687, # did
        'id': 80260, # id
        'partial': 'ajax-cart'
    }

    response = session.post('https://www.nakedcph.com/en/cart/add', headers=headers, cookies=cookies, json=data)
    logger(f"Checkout status code : {response.status_code}", "NakedV2", "info", tasknumber="tasknumber")
    logger(f"Checkout response : {response.text}", "NakedV2", "info", tasknumber="tasknumber")
    
    if response.status_code != 200:
        logger("Product is out of stock!", "NakedV2", "error", tasknumber="tasknumber")
        return -1

    cookies = {
            'AntiCsrfToken': session.cookies.get("AntiCsrfToken"),
            'nakedcph.state': session.cookies.get("nakedcph.state"),
            'cartRevisionCookie': '2',
            'png.state': session.cookies.get("png.state"),
            '__cf_bm': session.cookies.get("__cf_bm"),
        }

    headers = {
        'authority': 'www.nakedcph.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-gpc': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.nakedcph.com/en/product/12242/vans-og-authentic-lx-vn0a4bv90rd1',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response = session.get('https://www.nakedcph.com/en/cart/view', headers=headers, cookies=cookies)
    logger(f"View cart status code : {response.status_code}", "NakedV2", "info", tasknumber="tasknumber")