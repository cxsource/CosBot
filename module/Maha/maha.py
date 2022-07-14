"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] maha.py                                           """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 23/06/2022 00:37:56                                     """
"""   Updated: 23/06/2022 01:06:48                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import json
from bs4 import BeautifulSoup

from ultilities.createsession import getsession

session = requests.session()

def MahaEntry():

    # cookies = {
    #     'secure_customer_sig': '',
    #     'cookieconsent_preferences_disabled': '',
    #     '_y': 'd95fbb03-07a2-4b32-88c5-d0d233b75d3c',
    #     '_shopify_y': 'd95fbb03-07a2-4b32-88c5-d0d233b75d3c',
    #     'cookieconsent_status': 'allow',
    #     '_shopify_m': 'persistent',
    #     '_tracking_consent': '%7B%22con%22%3A%7B%22GDPR%22%3A%221%22%7D%2C%22v%22%3A%222.0%22%2C%22reg%22%3A%22GDPR%22%2C%22lim%22%3A%5B%22GDPR%22%5D%7D',
    #     '_ga': 'GA1.2.231430613.1640694331',
    #     'localization': 'NL',
    #     'cart_currency': 'EUR',
    #     '_orig_referrer': '',
    #     '_landing_page': '%2Fcollections%2Flaunches%2Fproducts%2Fyeezy-350-v2-blue-tint',
    #     '_s': 'e8d5903f-7957-4ea3-83e7-00128111d14c',
    #     '_shopify_s': 'e8d5903f-7957-4ea3-83e7-00128111d14c',
    #     '_shopify_tm': '',
    #     '_shopify_tw': '',
    #     'shopify_pay_redirect': 'pending',
    #     '_shopify_sa_p': '',
    #     '_gid': 'GA1.2.1845281184.1655937423',
    #     'cart': '5f0aafb6875285c98525cf1f2ce7c169',
    #     'cart_sig': '2fb4c85065ab1a4a7f9c2240a14df93e',
    #     'dynamic_checkout_shown_on_cart': '1',
    #     '_shopify_sa_t': '2022-06-22T22%3A40%3A30.380Z',
    #     '__kla_id': 'eyIkcmVmZXJyZXIiOnsidHMiOjE2Mzc3OTY4MzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1haGEtYW1zdGVyZGFtLmNvbS9jb2xsZWN0aW9ucy9sYXVuY2hlcy9wcm9kdWN0cy95ZWV6eS1ib29zdC03MDAtZmFkZS1henVyZSJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY1NTkzNzYzMSwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubWFoYS1hbXN0ZXJkYW0uY29tL2NvbGxlY3Rpb25zL2xhdW5jaGVzL3Byb2R1Y3RzL3llZXp5LTM1MC12Mi1ibHVlLXRpbnQifSwiJHNvdXJjZSI6Ik5pa2UgVyBEdW5rIEhpZ2ggQmxhY2sgV2hpdGUgJ1BhbmRhJyIsIlNpemUiOiI0MC41IiwiJGZpcnN0X25hbWUiOiJDaGFyYWYiLCIkbGFzdF9uYW1lIjoiRGlzc291IiwiJGFkZHJlc3MxIjoiRGFobGdydWVucmluZyAyIiwiJGNpdHkiOiJIYW1idXJnIiwiJGNvdW50cnkiOiJEZXV0c2NobGFuZCIsIkRlbGl2ZXJ5IjoiU2hpcHBpbmciLCIkZXhjaGFuZ2VfaWQiOiJOOHctb1IyQTdxNk5maEN4LWdUVnRBdWhtUXRnRnc2bjFmRVl3WnhDeHc0PS5USHhTZXcifQ==',
    #     'cart_ts': '1655937630',
    #     'cart_ver': 'gcp-us-central1%3A3',
    #     '_dd_s': 'logs=1&id=7ca19404-7ad5-41bd-ba03-7ff66080336c&created=1655937422768&expire=1655938599808',
    # }


    print("Getting Raffle Site")
    
    headers = {
        'authority': 'www.maha-amsterdam.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'secure_customer_sig=; cookieconsent_preferences_disabled=; _y=d95fbb03-07a2-4b32-88c5-d0d233b75d3c; _shopify_y=d95fbb03-07a2-4b32-88c5-d0d233b75d3c; cookieconsent_status=allow; _shopify_m=persistent; _tracking_consent=%7B%22con%22%3A%7B%22GDPR%22%3A%221%22%7D%2C%22v%22%3A%222.0%22%2C%22reg%22%3A%22GDPR%22%2C%22lim%22%3A%5B%22GDPR%22%5D%7D; _ga=GA1.2.231430613.1640694331; localization=NL; cart_currency=EUR; _orig_referrer=; _landing_page=%2Fcollections%2Flaunches%2Fproducts%2Fyeezy-350-v2-blue-tint; _s=e8d5903f-7957-4ea3-83e7-00128111d14c; _shopify_s=e8d5903f-7957-4ea3-83e7-00128111d14c; _shopify_tm=; _shopify_tw=; shopify_pay_redirect=pending; _shopify_sa_p=; _gid=GA1.2.1845281184.1655937423; cart=5f0aafb6875285c98525cf1f2ce7c169; cart_sig=2fb4c85065ab1a4a7f9c2240a14df93e; dynamic_checkout_shown_on_cart=1; _shopify_sa_t=2022-06-22T22%3A40%3A30.380Z; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2Mzc3OTY4MzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1haGEtYW1zdGVyZGFtLmNvbS9jb2xsZWN0aW9ucy9sYXVuY2hlcy9wcm9kdWN0cy95ZWV6eS1ib29zdC03MDAtZmFkZS1henVyZSJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY1NTkzNzYzMSwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubWFoYS1hbXN0ZXJkYW0uY29tL2NvbGxlY3Rpb25zL2xhdW5jaGVzL3Byb2R1Y3RzL3llZXp5LTM1MC12Mi1ibHVlLXRpbnQifSwiJHNvdXJjZSI6Ik5pa2UgVyBEdW5rIEhpZ2ggQmxhY2sgV2hpdGUgJ1BhbmRhJyIsIlNpemUiOiI0MC41IiwiJGZpcnN0X25hbWUiOiJDaGFyYWYiLCIkbGFzdF9uYW1lIjoiRGlzc291IiwiJGFkZHJlc3MxIjoiRGFobGdydWVucmluZyAyIiwiJGNpdHkiOiJIYW1idXJnIiwiJGNvdW50cnkiOiJEZXV0c2NobGFuZCIsIkRlbGl2ZXJ5IjoiU2hpcHBpbmciLCIkZXhjaGFuZ2VfaWQiOiJOOHctb1IyQTdxNk5maEN4LWdUVnRBdWhtUXRnRnc2bjFmRVl3WnhDeHc0PS5USHhTZXcifQ==; cart_ts=1655937630; cart_ver=gcp-us-central1%3A3; _dd_s=logs=1&id=7ca19404-7ad5-41bd-ba03-7ff66080336c&created=1655937422768&expire=1655938599808',
        'dnt': '1',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    response = session.get('https://www.maha-amsterdam.com/collections/launches/products/yeezy-350-v2-blue-tint', headers=headers) ## have to change the shoe name

    print(response.text) 
    print(response.status_code)

    with open("response/first_response.html", "w") as f:
        f.write(response.text)
    
    #########################
    print("Doing Entry 1")
    
    headers = {
        'authority': 'a.klaviyo.com',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'dnt': '1',
        'origin': 'https://www.maha-amsterdam.com',
        'referer': 'https://www.maha-amsterdam.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    params = {
        'c': 'THxSew',
    }

    data = '{"$exchange_id":"N8w-oR2A7q6NfhCx-gTVtAuhmQtgFw6n1fEYwZxCxw4=.THxSew","token":"THxSew","properties":{"$referrer":{"ts":1637796838,"value":"","first_page":"https://www.maha-amsterdam.com/collections/launches/products/yeezy-boost-700-fade-azure"},"$last_referrer":{"ts":1655937707,"value":"","first_page":"https://www.maha-amsterdam.com/collections/launches/products/yeezy-350-v2-blue-tint"},"$source":"Yeezy 350 V2 Blue Tint","Size":"39 1/3","$first_name":"Charaf","$last_name":"Dissou","$address1":"Dahlgruenring","$city":"Hamburg","$country":"Germany","Delivery":"Shipping","$exchange_id":"N8w-oR2A7q6NfhCx-gTVtAuhmQtgFw6n1fEYwZxCxw4=.THxSew","Shipping":"Shipping","$email":"charafdissou@gmail.com","number":"2","$zip":"21109","Instagram Handle":"@charafdissou"}}'

    response = session.post('https://a.klaviyo.com/api/onsite/identify', params=params, headers=headers, data=data)
    print(response.text) 
    print(response.status_code)

    with open("response/second_response.html", "w") as f:
        f.write(response.text)


    ####################

    print("Doing Entry 2")

    headers = {
        'authority': 'a.klaviyo.com',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-headers': '*',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://www.maha-amsterdam.com',
        'referer': 'https://www.maha-amsterdam.com/',
        'revision': '2022-02-16.pre',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    params = {
        'company_id': 'THxSew',
    }

    json_data = {
        'data': {
            'type': 'subscription',
            'attributes': {
                'list_id': 'SXR59R',
                'custom_source': 'Yeezy 350 V2 Blue Tint',
                'email': 'charafdissou@gmail.com',
                'properties': {
                    'Size': '39 1/3',
                    'Shipping': 'Shipping',
                    '$first_name': 'Charaf',
                    '$last_name': 'Dissou',
                    '$address1': 'Dahlgruenring',
                    'number': '2',
                    '$zip': '21109',
                    '$city': 'Hamburg',
                    '$country': 'Germany',
                    'Instagram Handle': '@charafdissou',
                    '$consent_method': 'Klaviyo Form',
                    '$consent_form_id': 'X34C92',
                    '$consent_form_version': 6006239,
                    'services': '{"shopify":{"source":"form"}}',
                    '$timezone_offset': 2,
                    '$exchange_id': 'N8w-oR2A7q6NfhCx-gTVtAuhmQtgFw6n1fEYwZxCxw4=.THxSew',
                },
            },
        },
    }

    response = session.post('https://a.klaviyo.com/onsite/v1/subscriptions/', params=params, headers=headers, json=json_data)
    print(response.text) 
    print(response.status_code)

    with open("response/third_response.html", "w") as f:
        f.write(response.text)

    print("Finish Entry 1")