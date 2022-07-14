"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] svd_new.py                                        """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 19/06/2022 16:57:51                                     """
"""   Updated: 12/07/2022 02:50:12                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import json
import random
import requests
import urllib
import base64
import time
from bs4 import BeautifulSoup
from ultilities.ThreadManager import *
from ultilities.DelayManager import *
from ultilities.createsession import *
from ultilities.CSVManager import getCsvInfo
from ultilities.ProxyManager import *
from ultilities.logger import *
from ultilities.WebhookManager import *
from ultilities.DiscordRPC import updateRPC
from ultilities.CaptchaManager import RecaptchasolverV2
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed

# session = requests.session()

def get_region_id(session, country, state):
        
    payload={}
    
    headers = {
        'Host': 'ms-api.sivasdescalzo.com',
        'pragma': 'no-cache',
        'accept': 'application/json',
        'device-os': 'I-iOS 14.4',
        'authorization': 'Bearer k600kh7poedpfgoddu9vknwe6w56jt0v',
        'app-version': '2.2.1',
        'device-id': '71E0D1E5-8498-470A-82C1-7A1A68034866',
        'accept-language': 'de-de',
        'cache-control': 'no-cache',
        'store-code': 'en',
        'user-agent': 'SVD/2002252234 CFNetwork/1220.1 Darwin/20.3.0',
        'bundle-version': '39',
        # 'Cookie': 'country=PK'
    }
    
    try:
        response = session.get(f'https://ms-api.sivasdescalzo.com/api/regions/{country}', headers=headers, data=payload)
    except Exception as RegionError:
        logger(f"Error while getting regions: Check if you are using correct country code or region", "SVD", "error", tasknumber="REGION ERROR")
        return -1
        
    # print(response.text)
    try:
        json_response=json.loads(response.text)
        for i in json_response:
            if i["name"].encode('utf-8').decode('unicode-escape').lower() == state.lower():
                return i["id"]
    except Exception as e:
        logger(f"Error while getting regions: {e}", "SVD", "error", tasknumber="REGION ERROR")
        return -1

def SVDEntry(profiles, proxy, tasknumber):
    
    session = getsession(proxy)

    ###-------------------------------------
    ###      Login in into the account      |
    ###-------------------------------------

    logger(f"Logging into the account.. {profiles['email']}", "SVD", "info", tasknumber=tasknumber)
    
    try:
        headers = {
            'Host': 'ms-api.sivasdescalzo.com',
            'Pragma': 'no-cache',
            'Accept': 'application/json',
            'device-os': 'I-iOS 15.4.1',
            'app-version': '2.2.1',
            'device-id': '71E0D1E5-8498-470A-82C1-7A1A68034866',
            'Accept-Language': 'de-DE,de;q=0.9',
            'Cache-Control': 'no-cache',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'store-code': 'en',
            'User-Agent': 'SVD/2002252234 CFNetwork/1331.0.7 Darwin/21.4.0',
            'bundle-version': '38',
            # 'Cookie': 'country=DE',
        }

        json_data = {
            'username': profiles['email'], # ChristianaEnglade011@outlook.com',
            'password': profiles['password'], # 'Facing678',
            'customer_agree': 'true',
        }

        response = session.post('https://ms-api.sivasdescalzo.com/api/login', headers=headers, json=json_data)
    except Exception as LoginError:
        logger(f"Proxy Error {LoginError}", "SVD", "error", tasknumber=tasknumber)
        return -1

    if response.status_code == 200:
        logger(f"Successfully logged in {profiles['email']}", "SVD", "success", tasknumber=tasknumber)
    else:
        logger(f"Error while logging into the account: {response.status_code}", "SVD", "error", tasknumber=tasknumber)
        return -1
        
    

    # print(response.text)
    # print(response.status_code)
    
    try:
        token = json.loads(response.text)["customer_data"]["token"]
    except Exception as TokenError:
        logger(f"Error while getting user token... {TokenError}", "SVD", "error", tasknumber=tasknumber)
        return -1
    # print(token)
    

    ###-------------------------------------
    ###      Getting the raffle shoe        |
    ###-------------------------------------

    logger(f"Getting the raffle.. {profiles['email']}", "SVD", tasknumber=tasknumber)

    headers = {
        'Host': 'ms-api.sivasdescalzo.com',
        # 'Cookie': 'country=DE; country=PK',
        'pragma': 'no-cache',
        'accept': 'application/json',
        'device-os': 'I-iOS 14.4',
        'authorization': f'Bearer {token}',
        'app-version': '2.2.1',
        'device-id': '71E0D1E5-8498-470A-82C1-7A1A68034866',
        'accept-language': 'de-de',
        'cache-control': 'no-cache',
        'store-code': 'en',
        'user-agent': 'SVD/2002252234 CFNetwork/1220.1 Darwin/20.3.0',
        'bundle-version': '39'
    }
    
    try:
        response = session.get("https://ms-api.sivasdescalzo.com/api/raffles/items?filter=all&limit=150&offset=0", headers=headers)
    except Exception as RaffleError:
        logger(f"Error while getting the raffle... {response.text}", "SVD", "error", tasknumber=tasknumber)
        return -1
    # sprint(response.text)
    # print(response.status_code)
    
    try:
        product_id = None
        products = json.loads(response.text)["items"]
        for p in products:
            # print(p.get("general_data").get("sku")) ### er sucht alle skus in general_data
            if p.get("general_data").get("sku") == profiles['SKU']:
                raffle_id = p.get("general_data").get("id")
                # print(raffle_id)
                # print(p.get("product_data").get("options"))
                for i in p.get("product_data").get("options"):
                    for sizes in i.get("sizes"):
                        # print(sizes)
                        for size in sizes["size"]:
                            if size["value"] == profiles['size']:
                                product_id = sizes["product_id"]
                                option_value_id = sizes["option_value_id"]
                                size_group = size["size_group"].split('size_')[1]
                                # print(product_id)
    except Exception as SizeError:
        logger(f"Error while getting raffleid and size... {SizeError}", "SVD", "error", tasknumber=tasknumber)
        return -1

    logger(f"Solving Captcha.. {profiles['email']}", "SVD", tasknumber=tasknumber)
    time.sleep(2)

    headers = {
        'Host': 'ms-api.sivasdescalzo.com',
        # 'Cookie': 'country=DE',
        'pragma': 'no-cache',
        'accept': 'application/json',
        'device-os': 'I-iOS 14.4',
        'authorization': f'Bearer {token}',
        'app-version': '2.2.1',
        'device-id': '71E0D1E5-8498-470A-82C1-7A1A68034866',
        'x-recaptcha': RecaptchasolverV2("6LcuURUTAAAAAK_b8wWvbNLY0awdFT27EJYcx-M1", "https://ms-api.sivasdescalzo.com/api/carts/payments/token"),
        'accept-language': 'de-de',
        'cache-control': 'no-cache',
        'store-code': 'en',
        'user-agent': 'SVD/2002252234 CFNetwork/1220.1 Darwin/20.3.0',
        'bundle-version': '39',
    }
    
    try:
        response = session.get('https://ms-api.sivasdescalzo.com/api/carts/payments/token', headers=headers)
    except:
        logger(f"Error while solving Captcha...", "SVD", "error", tasknumber=tasknumber)
        return -1

    # print(response.text)
    # print(response.status_code)
    try:
        json_data = json.loads(base64.b64decode(json.loads(response.text)["token"]))
    except Exception as e:
        logger(f"Error while getting payment tokens... {e}", "SVD", "error", tasknumber=tasknumber)
    # print(json_data)

    ###------------------------------
    ###    Get payment details       |
    ###------------------------------

    logger(f"Getting Payment details.. {profiles['email']}", "SVD", tasknumber=tasknumber)
    
    try:
        authorizationFingerprint = json_data['authorizationFingerprint']
        id = json_data['configUrl'].split('merchants/')[1].split('/')[0]
        url = f"{json_data['configUrl'].replace(':443','')}?configVersion=3&authorization_fingerprint={authorizationFingerprint}"
    except Exception as ValueError:
        logger(f"Error while getting payment values... {e}", "SVD", "error", tasknumber=tasknumber)
        return -1
        # print(id)

    payload = {}
    
    headers = {
        'Host': 'api.braintreegateway.com:443',
        'Accept': 'application/json',
        'Accept-Language': 'en-DE',
        'User-Agent': 'Braintree/iOS/4.38.0'
    }

    response = session.get(url, headers=headers, data=payload)

    # print(response.text)
    # print(response.status_code)

    ###------------------------------
    ###    Get tokenize card         |
    ###------------------------------
    
    try:
        # print("Get tokenize card")
        # logger(f"Adding card.. {profiles['email']}", "SVD", tasknumber=tasknumber)

        headers = {
            'Host': 'payments.braintree-api.com',
            'Content-Type': 'application/json; charset=utf-8',
            'Braintree-Version': '2018-03-06',
            'Accept': 'application/json',
            'User-Agent': 'Braintree/iOS/4.38.0',
            'Authorization': f'Bearer {authorizationFingerprint}',
            'Accept-Language': 'en-DE',
        }

        json_data = {
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {  tokenizeCreditCard(input: $input) {    token    creditCard {      brand      expirationMonth      expirationYear      cardholderName      last4      bin      binData {        prepaid        healthcare        debit        durbinRegulated        commercial        payroll        issuingBank        countryOfIssuance        productId      }    }  }}',
            'clientSdkMetadata': {
                'sessionId': 'BF394A1539314C0A805640BD6CF6922F',
                'integration': 'dropin2',
                'source': 'unknown',
            },
            'operationName': 'TokenizeCreditCard',
            'variables': {
                'input': {
                    'options': {
                        'validate': True,
                    },
                    'creditCard': {
                        'number': profiles['cc_number'], # '4633840011222011',
                        'expirationYear': profiles['cc_year'], #'2026', # XXXX
                        'expirationMonth': profiles['cc_month'], # XX
                        'cvv': profiles['cc_cvv'],
                        'cardholderName': f"{profiles['first_name']} {profiles['last_name']}",
                    },
                },
            },
        }
        
        response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        # print(response.text)
        # print(response.status_code)
        # print("cool")
    except Exception as e:
        # print(response.text)
        # print(e)
        logger(f"Error while tokenize card... {e}", "SVD", "error", tasknumber=tasknumber)
        return -1


    ###------------------------------
    ###    Get Payment Method        |
    ###------------------------------
    
    try:
        headers = {
            'Host': 'api.braintreegateway.com:443',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json',
            'User-Agent': 'Braintree/iOS/4.38.0',
            'Accept-Language': 'en-DE'
        }

        params = {
            'default_first': 'true',
            'authorization_fingerprint': authorizationFingerprint,
            'session_id': 'BF394A1539314C0A805640BD6CF6922F',
        }

        response = session.get(f'https://api.braintreegateway.com/merchants/{id}/client_api/v1/payment_methods', params=params, headers=headers)
    except Exception as e:
        logger(f"Error while getting payment method... {PaymentMethodError}", "SVD", "error", tasknumber=tasknumber)
        return -1
    
    try:
        card_token = json.loads(response.text)["paymentMethods"][0]["nonce"]
        # print(card_token)
    except Exception as PaymentMethodError:
        logger(f"Error while scraping first payment method token... {PaymentMethodError}", "SVD", "error", tasknumber=tasknumber)
        print(response.text)
        pass

    ###------------------------------
    ###    Fingerprint Payment       |
    ###------------------------------

    # print("fingerprint payment")
    # logger(f"Getting Fingerprint payment.. {profiles['email']}", "SVD", tasknumber=tasknumber)

    headers = {
        'Host': 'api.braintreegateway.com:443',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json',
        'User-Agent': 'Braintree/iOS/4.38.0',
        'Accept-Language': 'en-DE',
    }

    json_data = {
        'amount': 0,
        'authorization_fingerprint': authorizationFingerprint,
        '_meta': {
            'iosIdentifierForVendor': '71E0D1E5-8498-470A-82C1-7A1A68034866',
            'source': 'unknown',
            'iosDeviceName': 'iPhone von Source',
            'merchantAppName': 'SVD',
            'integration': 'dropin2',
            'deviceAppGeneratedPersistentUuid': '742388C7-1ED9-42F1-BC4F-AC556E8195B4',
            'merchantAppVersion': '2002252234',
            'iosIsCocoapods': True,
            'sessionId': 'BF394A1539314C0A805640BD6CF6922F',
            'iosSystemName': 'iOS',
            'merchantAppId': 'com.sivasdescalzo.svd-app',
            'platform': 'iOS',
            'isSimulator': False,
            'iosDeploymentTarget': '130000',
            'sdkVersion': '4.38.0',
            'deviceManufacturer': 'Apple',
            'deviceModel': 'iPhone10,4',
            'deviceScreenOrientation': 'Portrait',
            'venmoInstalled': False,
            'dropinVersion': '8.2.0',
            'iosBaseSDK': '150200',
            'platformVersion': '14.4',
        },
        'customer': {},
    }

    try:
        response = session.post(f'https://api.braintreegateway.com/merchants/{id}/client_api/v1/payment_methods/{card_token}/three_d_secure/lookup', headers=headers, json=json_data)
    except Exception as FingerprintError:
        logger(f"Error while getting fingerprint... {FingerprintError}", "SVD", "error", tasknumber=tasknumber)
        return -1
    
    # print(response.url)
    # print(response.text)
    # print(response.status_code)

    try:
        card_token1 = json.loads(response.text)["paymentMethod"]["nonce"]
        # print(f"new token of card : {card_token1}")
    except Exception as e:
        logger(f"Error while scraping second payment method token... {response.text}", "SVD", "error", tasknumber=tasknumber)
        pass

    
    try:
        pareq =  json.loads(response.text)["lookup"]["pareq"]
        termUrl = json.loads(response.text)["lookup"]["termUrl"]
        md = json.loads(response.text)["lookup"]["md"]
    except Exception as e:
        logger(f"Error while scraping values... {e}", "SVD", "error", tasknumber=tasknumber)
        return -1
        

    ###-------------------------------------
    ###    Fingerprint Submit Payment       |
    ###-------------------------------------

    # print("fingerprint submit")

    headers = {
        'Host': '1eaf.cardinalcommerce.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://assets.braintreegateway.com',
        'accept-language': 'de-de',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'referer': 'https://assets.braintreegateway.com/',
    }

    data = f'PaReq={pareq}&MD={md}&TermUrl={termUrl}'

    try:
        response = session.post('https://1eaf.cardinalcommerce.com/EAFService/jsp/v1/redirect', headers=headers, data=data)
    except Exception as e:
        logger(f"Error while submitting fingerprint... {e}", "SVD", "error", tasknumber=tasknumber)
        return -1
        
    # print(response.text)
    # print(response.text)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    if 'name="PaRes"' in response.text:
        PaRes = soup.find("input", {"name":"PaRes"})["value"]
        url = response.text.split('form action="')[1].split('"')[0]

        url = url.replace(":443","")

        ###----------------------
        ###    Submit PaRes      |
        ###----------------------

        try:
            message = authorizationFingerprint # json_data['authorizationFingerprint']
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            # https://api.braintreegateway.com/merchants/7rgb8j8vb5f4hdwg/client_api/v1/payment_methods/93ac331f-16de-155a-f716-c1bf5b1c1467/three_d_secure/authenticate?authorization_fingerprint=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2NTQ5Njk5NzQsImp0aSI6IjY5MDA3ZjQzLWYyYjQtNGEzYy1iMDE5LTI0ZDJjMDM4NmI4OCIsInN1YiI6IjdyZ2I4ajh2YjVmNGhkd2ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjdyZ2I4ajh2YjVmNGhkd2ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJjdXN0b21lcl9pZCI6IjI2OTUzOTMiLCJtZXJjaGFudF9hY2NvdW50X2lkIjoic3Zkc2l2YXNkZXNjYWx6b0VVUiJ9fQ.r4y7_cpnNF_s4jyXuACxs4TISCArNG9ql81xJIPYqYpwHX-hmxGbh4hF3HWr8z78mmDrKOlXgtvmX25sY_kXJg?customer_id=

            url = f"{url.split('?customer_id=')[0]}&authorization_fingerprint={authorizationFingerprint}&authorization_fingerprint_64={base64_message}&authentication_complete_base_url=https://assets.braintreegateway.com/mobile/three-d-secure-redirect/0.2.0/redirect.html?redirect_url%3Dcom.sivasdescalzo.svd-app.payments%253A%252F%252Fx-callback-url%252Fbraintree%252Fthreedsecure%253F"
            # print(url)
        except Exception as e:
            logger(f"Error while getting values... {PaymentMethodError}", "SVD", "error", tasknumber=tasknumber)
            return -1
        
        payload={
            "PaRes": PaRes,
            "MD": md
        }
        
        # payload = urllib.parse.urlencode(payload)
        # print(payload)
        
        headers = {
            'Host': 'api.braintreegateway.com',
            'Origin': 'https://1eaf.cardinalcommerce.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'Referer': 'https://1eaf.cardinalcommerce.com/EAFService/jsp/v1/term',
            'Accept-Language': 'de-de',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        try:
            response = session.post(url, headers=headers, data=payload,allow_redirects=False)
            url=response.text.split('<a href="')[1].split('"')[0]
            payload={}
            headers = {
                'Host': 'assets.braintreegateway.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
                'accept-language': 'de-de',
                'referer': 'https://0eaf.cardinalcommerce.com/'
            }

            response = session.get( url, headers=headers, data=payload)

            # print(response.text)
            # return 0
        except Exception as ProxyError:
            logger(f"Proxy Error, try a bit later again... {PaymentMethodError}", "SVD", "error", tasknumber=tasknumber)
            return -1
            
        # print(response.text)

    ###########################
        
    try: 
        PaReq = soup.find("input", {"name":"PaReq"})["value"]
        md = soup.find("input", {"name":"MD"})["value"]
    except Exception as e:
        logger(f"Error while getting pareq value... {response.text}", "SVD", "error", tasknumber=tasknumber)
        return -1
    
    # print(PaReq)
    # print(md)

    # payload=f'PaReq={urllib.parse.urlencode(self.PaReq)}&TermUrl={urllib.parse.urlencode("https://1eaf.cardinalcommerce.com/EAFService/jsp/v1/term")}&MD={urllib.parse.urlencode(self.MD)}'
    
    payload= {
        "PaReq": PaReq,
        "TermUrl": "https://1eaf.cardinalcommerce.com/EAFService/jsp/v1/term",
        "MD": md,
    }
    
    # payload = urllib.parse.urlencode(payload)
    # print(payload)
    
    headers = {
        'Host': 'idcheck.acs.touchtechpayments.com',
        'Origin': 'https://1eaf.cardinalcommerce.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1',
        'Accept-Language': 'de-de',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = session.post('https://idcheck.acs.touchtechpayments.com/v1/payerAuthentication', headers=headers, data=payload)
    except Exception as e:
        logger(f"Error while posting values... {e}", "SVD", "error", tasknumber=tasknumber)
        return -1
    # print(response.text)

    card = "Mastercard"

    if not "Mastercard SecureCode" in response.text:
        card = "Visa"
        transactionToken = response.text.split('token: "')[1].split('"')[0]

        ###-------------------------------------
        ###    Waiting For 3DS Approval         |
        ###-------------------------------------

        status= "pending"
        
        logger(f"Please confirm your 3Ds.. {profiles['email']}", "SVD", "info", tasknumber=tasknumber)
        
        while status == "pending":
            
            time.sleep(2)

            headers = {
                'Host': 'poll.touchtechpayments.com',
                'accept': '*/*',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                'origin': 'https://idcheck.acs.touchtechpayments.com',
                'accept-language': 'de-de',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
                'referer': 'https://idcheck.acs.touchtechpayments.com/',
            }

            json_data = {
                'transToken': transactionToken,
            }

            response = session.post('https://poll.touchtechpayments.com/poll', headers=headers, json=json_data)
            
            # print(response.text)
            
            status=json.loads(response.text)["status"]

        if status == "success":
            authToken = json.loads(response.text)["authToken"]
        else:
            logger(f"You couldn't confirm 3Ds in time...", "SVD", "error", tasknumber=tasknumber)
            return -1

            
        ###-------------------------------------
        ###    Confirm Transaction              |
        ###-------------------------------------
            
        # print("Confirm Transaction")
        logger(f"3Ds have been confirmed! {profiles['email']}", "SVD", "success", tasknumber=tasknumber)

        headers = {
            'Host': 'macs.touchtechpayments.com',
            'accept': '*/*',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            'origin': 'https://idcheck.acs.touchtechpayments.com',
            'accept-language': 'de-de',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'referer': 'https://idcheck.acs.touchtechpayments.com/',
        }

        json_data = {
            'transToken': transactionToken,
            'authToken': authToken
        }

        try:
            response = session.post('https://macs.touchtechpayments.com/v1/confirmTransaction', headers=headers, json=json_data)
        except Exception as e:
            logger(f"Exception happenend while 3Ds confirmation... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1
        # print(response.text)
        
        try:
            PaRes = json.loads(response.text)["Response"]
        except Exception as PaResError:
            logger(f"Error while scraping PaRes value... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1

        ###-------------------------------------
        ###    Processing Transaction           |
        ###-------------------------------------
        
        headers = {
            'Host': '1eaf.cardinalcommerce.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://idcheck.acs.touchtechpayments.com',
            'accept-language': 'de-de',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'referer': 'https://idcheck.acs.touchtechpayments.com/',
            # 'Cookie': '__cfruid=0da8f08e22e09ea3b5f37375ec12d810f5fef6c2-1654884054; BIGipServerCentinel-Prod-Web-EnhancedAltFlow.app~Centinel-Prod-Web-EnhancedAltFlow_pool=!uYUtCZsGtRtRqfJKkcbbaZHdYVkLmWPTx24GkhX9iFpR8vHEQFoLd+mIlS2kZd18Pw2X7EkJs3iZUKk=; TS0163941c=01d4b443a9593f34172c1242adc0b76466ca9db4855c2f129b0443650f6bc527a4252082be44494c3a063f8ed74d07205d7e010c18719d001a9d9beb95d2970c4bdf99611f'
        }
        
        payload= {
            "PaRes": PaRes,
            "MD": pareq
        }
        
        # payload = urllib.parse.urlencode(payload)
        # print(payload)

        try:
            response = session.post('https://1eaf.cardinalcommerce.com/EAFService/jsp/v1/term', headers=headers, data=payload)
        except Exception as e:
            logger(f"Exception happenend processing transaktion... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1
        # print(response.text)
        
        try:
            url = response.text.split("form action='")[1].split("'")[0]

            url = url.replace(":443","")
            # self.card_token=self.url.split("payment_methods/")[1].split("/")[0]
            soup = BeautifulSoup(response.text, "lxml")
            PaRes = soup.find("input", {"name":"PaRes"})["value"]
            md = soup.find("input", {"name":"MD"})["value"]
        except Exception as e:
            logger(f"Error while scraping values... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1
            
        ###-------------------------------------
        ###    Submit PaRes                     |
        ###-------------------------------------

        # print("Submit")
        try:
            message = authorizationFingerprint # json_data['authorizationFingerprint'] authorizationFingerprint
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            # https://api.braintreegateway.com/merchants/7rgb8j8vb5f4hdwg/client_api/v1/payment_methods/93ac331f-16de-155a-f716-c1bf5b1c1467/three_d_secure/authenticate?authorization_fingerprint=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2NTQ5Njk5NzQsImp0aSI6IjY5MDA3ZjQzLWYyYjQtNGEzYy1iMDE5LTI0ZDJjMDM4NmI4OCIsInN1YiI6IjdyZ2I4ajh2YjVmNGhkd2ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjdyZ2I4ajh2YjVmNGhkd2ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJjdXN0b21lcl9pZCI6IjI2OTUzOTMiLCJtZXJjaGFudF9hY2NvdW50X2lkIjoic3Zkc2l2YXNkZXNjYWx6b0VVUiJ9fQ.r4y7_cpnNF_s4jyXuACxs4TISCArNG9ql81xJIPYqYpwHX-hmxGbh4hF3HWr8z78mmDrKOlXgtvmX25sY_kXJg?customer_id=
    
            url = f"{url.split('?customer_id=')[0]}&authorization_fingerprint={authorizationFingerprint}&authorization_fingerprint_64={base64_message}&authentication_complete_base_url=https://assets.braintreegateway.com/mobile/three-d-secure-redirect/0.2.0/redirect.html?redirect_url%3Dcom.sivasdescalzo.svd-app.payments%253A%252F%252Fx-callback-url%252Fbraintree%252Fthreedsecure%253F"
        except Exception as e:
            logger(f"Error while scraping values... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1
        
        # print(url)
        
        payload={
            "PaRes": PaRes,
            "MD": md
        }
        
        # payload = urllib.parse.urlencode(payload)
        # print(payload)
        
        headers = {
            'Host': 'api.braintreegateway.com',
            'Origin': 'https://1eaf.cardinalcommerce.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'Referer': 'https://1eaf.cardinalcommerce.com/EAFService/jsp/v1/term',
            'Accept-Language': 'de-de',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
#### ab hier geändert
        try:
            response = session.post(url, headers=headers, data=payload,allow_redirects=False)
            url=response.text.split('<a href="')[1].split('"')[0]
            payload={}
            headers = {
            'Host': 'assets.braintreegateway.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'accept-language': 'de-de',
            'referer': 'https://0eaf.cardinalcommerce.com/'
            }

            response = session.get( url, headers=headers, data=payload)

            # print(response.text)
        except Exception as e:
            logger(f"Proxy Error, try a bit later again... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1
    else:
        PaRes = response.text.split('pares = "')[1].split('"')[0]

        ###-------------------------------------
        ###    Processing Transaction           |
        ###-------------------------------------

        # print("Processing Transaction")
        
        headers = {
            'Host': '1eaf.cardinalcommerce.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://idcheck.acs.touchtechpayments.com',
            'accept-language': 'de-de',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'referer': 'https://idcheck.acs.touchtechpayments.com/',
            # 'Cookie': '__cfruid=0da8f08e22e09ea3b5f37375ec12d810f5fef6c2-1654884054; BIGipServerCentinel-Prod-Web-EnhancedAltFlow.app~Centinel-Prod-Web-EnhancedAltFlow_pool=!uYUtCZsGtRtRqfJKkcbbaZHdYVkLmWPTx24GkhX9iFpR8vHEQFoLd+mIlS2kZd18Pw2X7EkJs3iZUKk=; TS0163941c=01d4b443a9593f34172c1242adc0b76466ca9db4855c2f129b0443650f6bc527a4252082be44494c3a063f8ed74d07205d7e010c18719d001a9d9beb95d2970c4bdf99611f'
        }
        
        payload= {
            "PaRes": PaRes,
            "MD": pareq
        }
        
        # payload = urllib.parse.urlencode(payload)
        # print(payload)

        try:
            response = session.post('https://1eaf.cardinalcommerce.com/EAFService/jsp/v1/term', headers=headers, data=payload)
        except Exception as e:
            logger(f"Exception happenend processing transaktion... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1
        # print(response.text)
        
        try:
            url = response.text.split("form action='")[1].split("'")[0]

            url = url.replace(":443","")
            # self.card_token=self.url.split("payment_methods/")[1].split("/")[0]
            soup = BeautifulSoup(response.text,"lxml")
            PaRes = soup.find("input", {"name":"PaRes"})["value"]
            md = soup.find("input", {"name":"MD"})["value"]
        except Exception as e:
            logger(f"Error while scraping values... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1

        ###-------------------------------------
        ###    Submit PaRes                     |
        ###-------------------------------------

        # print("Submit")
        try:
            message = authorizationFingerprint # json_data['authorizationFingerprint'] authorizationFingerprint
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            # https://api.braintreegateway.com/merchants/7rgb8j8vb5f4hdwg/client_api/v1/payment_methods/93ac331f-16de-155a-f716-c1bf5b1c1467/three_d_secure/authenticate?authorization_fingerprint=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2NTQ5Njk5NzQsImp0aSI6IjY5MDA3ZjQzLWYyYjQtNGEzYy1iMDE5LTI0ZDJjMDM4NmI4OCIsInN1YiI6IjdyZ2I4ajh2YjVmNGhkd2ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjdyZ2I4ajh2YjVmNGhkd2ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJjdXN0b21lcl9pZCI6IjI2OTUzOTMiLCJtZXJjaGFudF9hY2NvdW50X2lkIjoic3Zkc2l2YXNkZXNjYWx6b0VVUiJ9fQ.r4y7_cpnNF_s4jyXuACxs4TISCArNG9ql81xJIPYqYpwHX-hmxGbh4hF3HWr8z78mmDrKOlXgtvmX25sY_kXJg?customer_id=

            url = f"{url.split('?customer_id=')[0]}&authorization_fingerprint={authorizationFingerprint}&authorization_fingerprint_64={base64_message}&authentication_complete_base_url=https://assets.braintreegateway.com/mobile/three-d-secure-redirect/0.2.0/redirect.html?redirect_url%3Dcom.sivasdescalzo.svd-app.payments%253A%252F%252Fx-callback-url%252Fbraintree%252Fthreedsecure%253F"
        except Exception as e:
            logger(f"Error while scraping values... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1
        # print(url)
        
        payload={
            "PaRes": PaRes,
            "MD": md
        }
        
        # payload = urllib.parse.urlencode(payload)
        # print(payload)
        
        headers = {
            'Host': 'api.braintreegateway.com',
            'Origin': 'https://1eaf.cardinalcommerce.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'Referer': 'https://1eaf.cardinalcommerce.com/EAFService/jsp/v1/term',
            'Accept-Language': 'de-de',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        try:
            response = session.post(url, headers=headers, data=payload)
        except Exception as e:
            logger(f"Proxy Error, try a bit later again... {e}", "SVD", "error", tasknumber=tasknumber)
            return -1


    logger(f"Finishing Raffle Entry.. {profiles['email']}", "SVD", "info", tasknumber=tasknumber)

    ###-----------------------------------------
    ###    Submitting raffle information        |
    ###-----------------------------------------

    # print("Getting shipping infos")
    

    headers = {
        'Host': 'ms-api.sivasdescalzo.com',
        # 'Cookie': 'country=DE',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'pragma': 'no-cache',
        'accept': 'application/json',
        'device-os': 'I-iOS 14.4',
        'authorization': f'Bearer {token}',
        'app-version': '2.2.1',
        'device-id': '71E0D1E5-8498-470A-82C1-7A1A68034866',
        'accept-language': 'de-de',
        'cache-control': 'no-cache',
        'store-code': 'en',
        'user-agent': 'SVD/2002252234 CFNetwork/1220.1 Darwin/20.3.0',
        'bundle-version': '39',
    }

    json_data = {
        'address': {
            'city': profiles['city'],
            'country_id': profiles['country'],
            'firstname': profiles['first_name'],
            'lastname': profiles['last_name'],
            'postcode': profiles['zip'],
            'region': profiles['region'],
            'region_id': get_region_id(session, profiles['country'], profiles['region']),
            'street': [
                profiles['address'],
            ],
            'telephone': profiles['phone'],
            'custom_attributes': {},
        },
    }
    # print(json_data)

    try:
        response = session.post(f'https://ms-api.sivasdescalzo.com/api/raffles/{raffle_id}/estimate-shipping', headers=headers, json=json_data) ## add raffle product_id
    except Exception as ShippingError:
        logger(f"Error while submitting shipping inormation: {response.text}", "SVD", "error", tasknumber=tasknumber)
        return -1
        
    # print(response.status_code)
    # print(response.text)
    
    try:
        shipping_method_code = json.loads(response.text)[0]["method_code"]
    except Exception as methode_codeError:
        logger(f"Error while getting method_code inormation: {response.text}", "SVD", "error", tasknumber=tasknumber)
        return -1

    
    # print("Getting raffle informaion infos")
    
    headers = {
        'Host': 'ms-api.sivasdescalzo.com',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'pragma': 'no-cache',
        'accept': 'application/json',
        'device-os': 'I-iOS 14.4',
        'authorization': f'Bearer {token}',
        'app-version': '2.2.1',
        'device-id': '71E0D1E5-8498-470A-82C1-7A1A68034866',
        'accept-language': 'de-de',
        'cache-control': 'no-cache',
        'store-code': 'en',
        'user-agent': 'SVD/2002252234 CFNetwork/1220.1 Darwin/20.3.0',
        'bundle-version': '39',
    }

    json_data = {
        'participation': {
            'product_id': product_id,
            'size_group': size_group,
            'store_group_id': 1,
            'product_option_id': option_value_id,
            'shipping_method': shipping_method_code,
            'payment_data': card_token1,
            'shipping_firstname': profiles['first_name'],
            'shipping_lastname': profiles['last_name'],
            'shipping_street': profiles['address'],
            'shipping_postcode': profiles['zip'],
            'shipping_country_id': profiles['country'],
            'shipping_region_id': get_region_id(session, profiles['country'], profiles['region']),
            'shipping_region': profiles['region'],
            'shipping_city': profiles['city'],
            'shipping_telephone': profiles['phone'],
            'billing_firstname': profiles['first_name'],
            'billing_lastname': profiles['last_name'],
            'billing_street': profiles['address'],
            'billing_postcode': profiles['zip'],
            'billing_country_id': profiles['country'],
            'billing_region_id': get_region_id(session, profiles['country'], profiles['region']),
            'billing_region': profiles['region'],
            'billing_city': profiles['city'],
            'billing_telephone': profiles['phone'],
        },
    }

    try:
        response = session.post(f'https://ms-api.sivasdescalzo.com/api/raffles/{raffle_id}', headers=headers, json=json_data)
    except Exception as e:
        logger(f"Error while submitting raffle inormation: {response.text}", "SVD", "error", tasknumber=tasknumber)
        return -1

    if response.status_code == 200:
        logger(f"SUCCESS - Your Raffle Entry is in: {profiles['email']}", "SVD", "success", tasknumber=tasknumber)
        # success_webhook("SVD", profiles['size'], "Product", profiles['email'], proxy, profiles['SKU'], "https://media.discordapp.net/attachments/812303141114478593/856232226428551209/Bildschirmfoto_2021-06-20_um_20.00.57.png")
        return 0
    else:
        logger(f"Error while submitting the raffle entry... {profiles['email']}: {response.text} ", "SVD", "error", tasknumber=tasknumber)
        # failed_webhook("SVD", profiles['size'], "Product", profiles['email'], proxy, profiles['SKU'], "https://media.discordapp.net/attachments/812303141114478593/856232226428551209/Bildschirmfoto_2021-06-20_um_20.00.57.png")
        return -1
        
    # print(url)
    # print(response.status_code)
    # print(response.text)


def svd_main():

    setTitle("Running SVD")
    
    rows_list = getCsvInfo("SVD")
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
            
            result = SVDEntry(row, chosen_proxy, tasknumber)
            # print(row)
            
            if result == 0:
                success_webhook("SVD", row['size'], row['SKU'], row['email'], threads, maxDelay, chosen_proxy, "", "https://media.discordapp.net/attachments/708741400333779015/936118442250100746/svd.jpg?width=898&height=898")
                logger("Webhook sent!", "SVD", "success", tasknumber=tasknumber)
                successTasks +=1
                               
            else:
                if row in rows_list:
                    tasksFailed.append(row)
                    # print(tasksFailed)
                failed_webhook("SVD", row['size'], row['SKU'], row['email'], threads, maxDelay, chosen_proxy, "", "https://media.discordapp.net/attachments/708741400333779015/936118442250100746/svd.jpg?width=898&height=898")
                logger("Webhook Error sent!", "SVD", "error", tasknumber=tasknumber)
                failedTasks +=1

            resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
            setTitle(f"Running SVD - {resultTracker}")
                
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
                
                result = SVDEntry(newrow, chosen_proxy, tasknumber)
                # print(row)
                
                if result == 0:
                    success_webhook("SVD", newrow['size'], newrow['SKU'], newrow['email'], threads, maxDelay, chosen_proxy, "", "https://media.discordapp.net/attachments/708741400333779015/936118442250100746/svd.jpg?width=898&height=898")
                    logger("Webhook sent!", "SVD", "success", tasknumber=tasknumber)
                    successTasks +=1
                                
                else:
                    failed_webhook("SVD", newrow['size'], newrow['SKU'], newrow['email'], threads, maxDelay, chosen_proxy, "", "https://media.discordapp.net/attachments/708741400333779015/936118442250100746/svd.jpg?width=898&height=898")
                    logger("Webhook Error sent!", "SVD", "error", tasknumber=tasknumber)
                    failedTasks +=1

                resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
                setTitle(f"Running SVD - {resultTracker}")
                    
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
                        SVDEntry, 
                        row, 
                        chosen_proxy, 
                        tasknumber
                        )
                    tasksResult.append(tasks)
                    index +=1

                for task in as_completed(tasksResult):

                    results = task.result()
                    
                    if results == 0:
                        success_webhook("SVD", row['size'], row['SKU'], row['email'], threads, "ND", chosen_proxy, "", "https://media.discordapp.net/attachments/708741400333779015/936118442250100746/svd.jpg?width=898&height=898")
                        logger("Webhook sent!", "SVD", "success", tasknumber=tasknumber)
                        successTasks +=1
                    else:
                        failed_webhook("SVD", row['size'], row['SKU'], row['email'], threads, "ND", chosen_proxy, "", "https://media.discordapp.net/attachments/708741400333779015/936118442250100746/svd.jpg?width=898&height=898")
                        logger("Webhook Error sent!", "SVD", "error", tasknumber=tasknumber)
                        failedTasks +=1
                        
                    resultTracker = f"success: {successTasks} / failed: {failedTasks}"
                    setTitle(f"Running SVD - {resultTracker}")
                    
    logger("Finished Tasks", "SVD", "info", tasknumber="DONE")

