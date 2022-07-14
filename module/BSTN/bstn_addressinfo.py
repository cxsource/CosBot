"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] bstn_addressinfo.py                               """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 18/05/2022 00:45:18                                     """
"""   Updated: 26/05/2022 12:09:15                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""


"""STILL NEED AN UPDATE"""

from questionary import form
import requests
import random
import time
from bs4 import BeautifulSoup
from ultilities.createsession import *

def bstn_addressinfo():
    
    session = CFsession1()

## start to log into the account

    headers = {
        'authority': 'www.bstn.com',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'gender=men; _ALGOLIA=anonymous-f76e196e-712d-478c-8d12-a3f03a53bb34; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; form_key=33wIDfH8eJgtWZSy; cjConsent=MHxZfDB8Tnww; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; scarab.visitor=%227622DAE98BE4DEC8%22; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1652777861%2C%22type%22%3A%22category%22%2C%22version%22%3A%227ff7db62-4f82-4346-af4a-421f8a8bf045%22%7D; _gcl_au=1.1.1388763952.1652777861; __gtm_referrer=https%3A%2F%2Fraffle.bstn.com%2F; _gid=GA1.2.229697031.1652777861; _fbp=fb.1.1652777861469.1569413978; cebs=1; _tt_enable_cookie=1; _ttp=49965965-3fdc-40a4-a7af-708e1144a199; __cf_bm=dOJZB6rJgb4GLZDF4CI70he3W59jv06qd2w9SPeT2f0-1652827538-0-AS4vZC9BgJ8JBvPg/kxvOj19IvLO8viYFO7i9VAHMH/XAfZjFbpqjOsF4RkBe6MCBo3T4dQBrENnutfkGVnxXuA=; cf_clearance=HGEsLFrn_AmbAcjTlpEQO4uer8VMLUALSFGBuyd_9WU-1652827558-0-150; _ga_9FC6HBPLQ6=GS1.1.1652827557.2.0.1652827558.0; aa-search=aa-Y3VzdG9tZXItc25lYWtlcmNkOUBnbWFpbC5jb20tMTQyNzAzMA; private_content_version=33970ecff3cee538b47de3dd29b648f4; _gat_UA-38846488-10=1; _gat_UA-38846488-11=1; PHPSESSID=g65ouo453i3dl5mr34cbo3ofll; mage-cache-sessid=true; _ga_3480EPZ6W5=GS1.1.1652827549.2.1.1652827674.47; _ga_NCXNW87L01=GS1.1.1652827549.2.1.1652827674.0; _ga=GA1.1.872180635.1652777857; _uetsid=68c057d0d5bf11ec8a99b9c8313837a2; _uetvid=68c037e0d5bf11ec9da13350e14564fa; ABTasty=uid=myzdmqd01k04pzg7&fst=1652777861444&pst=1652777861444&cst=1652827548476&ns=2&pvt=7&pvis=6&th=822959.0.7.6.2.1.1652777861534.1652827675988.1; ABTastySession=mrasn=&sen=11&lp=https%253A%252F%252Fwww.bstn.com%252Feu_de%252Fmen%252Fupcoming.html; form_key=33wIDfH8eJgtWZSy; cto_bundle=ax8zFF9xNFV5OWdSbTVGN0N6a2ZjeUhGWSUyQnFTSmRSamJSTjlUTHZwOXElMkZ6NjlUQkpNbWZDWUpiYUdueG9YR3hVJTJCWmRxVlQ3cmUlMkYxNkFZYkpLa1ZVclZBaXhka0lsS21iUDNFNjVmSE1JJTJGNDBoS043YWl2dFclMkJoWnZMQzQ1T0g4dDczMmZ4N0slMkZIR3pxa1FHTXVHeUNPY2tqbjBMWU9wTmRGekU1ckNZOVlkSGVXYyUzRA; section_data_ids=%7B%22emrssection%22%3A1652827676%2C%22cart%22%3A1652827676%2C%22customer%22%3A1652827676%2C%22wishlist%22%3A1652827676%2C%22rafflesection%22%3A1652827676%2C%22compare-products%22%3A1652827606%2C%22last-ordered-items%22%3A1652827606%2C%22directory-data%22%3A1652827606%2C%22instant-purchase%22%3A1652827606%2C%22captcha%22%3A1652827606%2C%22sociallogin%22%3A1652827606%2C%22recently_viewed_product%22%3A1652827606%2C%22recently_compared_product%22%3A1652827606%2C%22product_data_storage%22%3A1652827606%2C%22paypal-billing-agreement%22%3A1652827606%7D; _ce.s=v~80738519b3dd3ed5ebf0a583398cfdc4152a0f58~vpv~0~v11.rlc~1652827549279~ir~1~gtrk.la~l3aqxz6k',
        'origin': 'https://www.bstn.com',
        'referer': 'https://www.bstn.com/eu_de/men.html',
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
        'username':'mark@sourceraffles.com',
        'password': 'Password007!'
        }

    response = session.post('https://www.bstn.com/eu_de/sociallogin/popup/login/', headers=headers, data=data)

    print(response.text)
    print(response.status_code)


    # headers = {
    #     'authority': 'www.bstn.com',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    #     # Requests sorts cookies= alphabetically
    #     # 'cookie': 'cjConsent=MHxZfDB8Tnww; scarab.visitor=%22608E3E0CAE9A99E8%22; _gcl_au=1.1.907912704.1648038676; _fbp=fb.1.1648038675691.1367979066; _clck=10lrhro|1|f00|0; scarab.profile=%22167574%7C1648038677%22; cf_clearance=yBMQFReX.FyPmhIKSxF6C.KHJKyiDz93kXJNxr26xk0-1652742983-0-150; _ALGOLIA=anonymous-6f49662f-edf5-4cc4-b32c-9fdfe1a8ea04; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1648038675%2C%22type%22%3A%22category%22%2C%22version%22%3A%227ff7db62-4f82-4346-af4a-421f8a8bf045%22%7D; _tt_enable_cookie=1; _ttp=fec5d3b7-46f0-4d07-a6ba-cf59552c6456; _ga_9FC6HBPLQ6=GS1.1.1652777673.2.0.1652777673.0; cebs=1; private_content_version=a94959e2292f7e7e5070c6704ca3c2de; PHPSESSID=eeo8dps16h731l64ed9v3j81ll; aa-search=aa-Y3VzdG9tZXItbWFya0Bzb3VyY2VyYWZmbGVzLmNvbS0xNDI3NzEy; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; form_key=648pa2y5kTeUe7Ri; form_key=648pa2y5kTeUe7Ri; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gid=GA1.2.1194596649.1652900730; cto_bundle=bmGEXl9VNHo0Zm93RyUyQmh6N1ZHM1p3cDNFQUpIRzV3YWphTjYwZlhJVWVKWnpUQ0NsMTlUZHgxR2clMkY5YyUyRkVwWFYlMkZ6Q3pRTVc5SjFQRkJUTHg2ZlA4U1BzMno0V2JtU3VGdlpXakdSYTBDSEljcXhIN1l4Qjh1cTQ5QzYzOEplM2IlMkZOenJTYnBtMSUyQjFnVWdzaW51JTJCbXNqJTJGOUcyRFJXWFB1eVBCM1R1akJnaHJzbmUlMkZvQXpqQWs3U0pWS1ZEdnp5a1pPTWE; __cf_bm=QKMUw8yFUWCT.iptJR5XPU1zB2vAK.Q1gKzdffeI3gs-1652953800-0-AabL7NDNqaMWp0Ay4sAxhTchwOUflLQpB0g169VexxIkUyoXf/ZmrjbHMYtnfm/1CBikCGa6IThB7LMgFCtlISg=; _ce.s=v~e2ea041e1c498e4d2f8154ece217d0cf0950c240~vpv~2~v11.rlc~1652953802408; _ga_3480EPZ6W5=GS1.1.1652953800.8.1.1652954560.59; _ga_NCXNW87L01=GS1.1.1652953800.7.1.1652954560.0; _ga=GA1.2.1667164530.1648038676; _gat_UA-38846488-10=1; _gat_UA-38846488-11=1; _uetsid=7be94cf0d6dd11ec91fe37f222d36328; _uetvid=21e8a8b0aaa511ecba9599f922c6fbaa; ABTasty=uid=ys1enm9xn53g57e6&fst=1648038675665&pst=1652913203045&cst=1652953801777&ns=7&pvt=39&pvis=8&th=799342.992899.1.1.1.1.1648038678190.1648038678190.1_808212.1004175.1.1.1.1.1648038685591.1648038685591.1_808220.0.3.3.1.1.1648038675706.1648038685593.1_822959.0.39.8.7.1.1648038675730.1652954560756.1; ABTastySession=mrasn=&sen=15&lp=https%253A%252F%252Fwww.bstn.com%252Feu_de%252Fcustomer%252Faddress%252F; section_data_ids=%7B%22emrssection%22%3A1652954560%2C%22cart%22%3A1652953801%2C%22customer%22%3A1652954561%2C%22wishlist%22%3A1652900730%2C%22rafflesection%22%3A1652954560%7D',
    #     'referer': 'https://www.bstn.com/eu_de/customer/account/',
    #     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"macOS"',
    #     'sec-fetch-dest': 'document',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-user': '?1',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    # }

    # response = session.get('https://www.bstn.com/eu_de/customer/account/edit/', headers=headers)

    


    headers = {
        'authority': 'www.bstn.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'cjConsent=MHxZfDB8Tnww; scarab.visitor=%22608E3E0CAE9A99E8%22; _gcl_au=1.1.907912704.1648038676; _fbp=fb.1.1648038675691.1367979066; _clck=10lrhro|1|f00|0; scarab.profile=%22167574%7C1648038677%22; cf_clearance=yBMQFReX.FyPmhIKSxF6C.KHJKyiDz93kXJNxr26xk0-1652742983-0-150; _ALGOLIA=anonymous-6f49662f-edf5-4cc4-b32c-9fdfe1a8ea04; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1648038675%2C%22type%22%3A%22category%22%2C%22version%22%3A%227ff7db62-4f82-4346-af4a-421f8a8bf045%22%7D; _tt_enable_cookie=1; _ttp=fec5d3b7-46f0-4d07-a6ba-cf59552c6456; _ga_9FC6HBPLQ6=GS1.1.1652777673.2.0.1652777673.0; cebs=1; private_content_version=a94959e2292f7e7e5070c6704ca3c2de; PHPSESSID=eeo8dps16h731l64ed9v3j81ll; aa-search=aa-Y3VzdG9tZXItbWFya0Bzb3VyY2VyYWZmbGVzLmNvbS0xNDI3NzEy; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; form_key=648pa2y5kTeUe7Ri; form_key=648pa2y5kTeUe7Ri; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gid=GA1.2.1194596649.1652900730; cto_bundle=bmGEXl9VNHo0Zm93RyUyQmh6N1ZHM1p3cDNFQUpIRzV3YWphTjYwZlhJVWVKWnpUQ0NsMTlUZHgxR2clMkY5YyUyRkVwWFYlMkZ6Q3pRTVc5SjFQRkJUTHg2ZlA4U1BzMno0V2JtU3VGdlpXakdSYTBDSEljcXhIN1l4Qjh1cTQ5QzYzOEplM2IlMkZOenJTYnBtMSUyQjFnVWdzaW51JTJCbXNqJTJGOUcyRFJXWFB1eVBCM1R1akJnaHJzbmUlMkZvQXpqQWs3U0pWS1ZEdnp5a1pPTWE; __cf_bm=QKMUw8yFUWCT.iptJR5XPU1zB2vAK.Q1gKzdffeI3gs-1652953800-0-AabL7NDNqaMWp0Ay4sAxhTchwOUflLQpB0g169VexxIkUyoXf/ZmrjbHMYtnfm/1CBikCGa6IThB7LMgFCtlISg=; _ce.s=v~e2ea041e1c498e4d2f8154ece217d0cf0950c240~vpv~2~v11.rlc~1652953802408; _gat_UA-38846488-10=1; _gat_UA-38846488-11=1; _ga_3480EPZ6W5=GS1.1.1652953800.8.1.1652954174.47; _ga=GA1.1.1667164530.1648038676; _ga_NCXNW87L01=GS1.1.1652953800.7.1.1652954174.0; _uetsid=7be94cf0d6dd11ec91fe37f222d36328; _uetvid=21e8a8b0aaa511ecba9599f922c6fbaa; ABTasty=uid=ys1enm9xn53g57e6&fst=1648038675665&pst=1652913203045&cst=1652953801777&ns=7&pvt=37&pvis=6&th=799342.992899.1.1.1.1.1648038678190.1648038678190.1_808212.1004175.1.1.1.1.1648038685591.1648038685591.1_808220.0.3.3.1.1.1648038675706.1648038685593.1_822959.0.37.6.7.1.1648038675730.1652954174347.1; ABTastySession=mrasn=&sen=11&lp=https%253A%252F%252Fwww.bstn.com%252Feu_de%252Fcustomer%252Faddress%252F; section_data_ids=%7B%22emrssection%22%3A1652954174%2C%22cart%22%3A1652953801%2C%22customer%22%3A1652954175%2C%22wishlist%22%3A1652900730%2C%22rafflesection%22%3A1652954174%7D',
        'referer': 'https://www.bstn.com/eu_de/customer/account/',
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

    response = session.get('https://www.bstn.com/eu_de/customer/address/', headers=headers)

    print(response.text)
    print(response.status_code)
    

    soup = BeautifulSoup(response.text, 'html.parser')
    formkey = soup.find("input", {"name": 'form_key'})["value"]
    print(formkey)

    headers = {
        'authority': 'www.bstn.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'de-DE,de;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryA4NBYK3p21Ko4Asc',
        # Requests sorts cookies= alphabetically
        'cookie': f'gender=men; _ALGOLIA=anonymous-f76e196e-712d-478c-8d12-a3f03a53bb34; form_key={formkey}; cjConsent=MHxZfDB8Tnww; scarab.visitor=%227622DAE98BE4DEC8%22; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1652777861%2C%22type%22%3A%22category%22%2C%22version%22%3A%227ff7db62-4f82-4346-af4a-421f8a8bf045%22%7D; _gcl_au=1.1.1388763952.1652777861; __gtm_referrer=https%3A%2F%2Fraffle.bstn.com%2F; _gid=GA1.2.229697031.1652777861; _fbp=fb.1.1652777861469.1569413978; cebs=1; _tt_enable_cookie=1; _ttp=49965965-3fdc-40a4-a7af-708e1144a199; aa-search=aa-Y3VzdG9tZXItc25lYWtlcmNkOUBnbWFpbC5jb20tMTQyNzAzMA; cf_clearance=gerssf0jzSBpu.bxQoS3uRdSpEAZZpw8B6R.PjKWOoA-1652828842-0-150; _ga_9FC6HBPLQ6=GS1.1.1652827557.2.1.1652828843.0; form_key=33wIDfH8eJgtWZSy; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; cto_bundle=ESqexV9xNFV5OWdSbTVGN0N6a2ZjeUhGWSUyQnVLd3I1V2FrYXFtWmdsdCUyRmpMQ0lkUEROaExXNEg1empFUDdLUnd4T2VaSVdYR0Y1TWVEWHFKYmxRWTRYMEE2TTl2Q3ZVWXVxYzRKVFVVdllqdTczTGdqRFNrbmtrNXhjelNuZ2p3eDhuMXlENVc2czJ1dFY0eFRTTkVQT1JjemhLMlh2MWxGV2h6NXdSNzIxZFJjMlhnJTNE; PHPSESSID=g7j0nvmfb32v662d6ksk36jbph; private_content_version=ce351d361821e8ffa530c2804288a2d4; mage-cache-sessid=true; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; _ce.s=v~80738519b3dd3ed5ebf0a583398cfdc4152a0f58~vpv~0~v11.rlc~1652907764321~ir~1~gtrk.la~l3arqm69; _ga_3480EPZ6W5=GS1.1.1652907763.4.1.1652907776.47; _ga=GA1.1.872180635.1652777857; _ga_NCXNW87L01=GS1.1.1652907763.4.1.1652907776.0; _uetsid=68c057d0d5bf11ec8a99b9c8313837a2; _uetvid=68c037e0d5bf11ec9da13350e14564fa; ABTasty=uid=myzdmqd01k04pzg7&fst=1652777861444&pst=1652901051938&cst=1652907764264&ns=4&pvt=40&pvis=2&th=822959.0.38.2.4.1.1652777861534.1652907776512.1; section_data_ids=%7B%22emrssection%22%3A1652907776%2C%22cart%22%3A1652907763%2C%22customer%22%3A1652829424%2C%22wishlist%22%3A1652829424%2C%22rafflesection%22%3A1652907776%2C%22compare-products%22%3A1652829424%2C%22last-ordered-items%22%3A1652829424%2C%22directory-data%22%3A1652829424%2C%22instant-purchase%22%3A1652829424%2C%22captcha%22%3A1652829424%2C%22sociallogin%22%3A1652829424%2C%22recently_viewed_product%22%3A1652829424%2C%22recently_compared_product%22%3A1652829424%2C%22product_data_storage%22%3A1652829424%2C%22paypal-billing-agreement%22%3A1652829424%7D',
        'origin': 'https://www.bstn.com',
        'referer': 'https://www.bstn.com/eu_de/customer/address/new/',
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
        'form_key': formkey,
        'success_url': '',
        'error_url': '',
        'firstname': 'Max',
        'lastname': 'Moritz',
        'street[0]': 'Eichwischen',
        'street[1]': '17',
        'street[2]': '',
        'country_id': 'DE',
        'postcode': '22143',
        'city': 'Hamburg',
        'telephone': '017612345678'
    }
    
    response = session.post('https://www.bstn.com/eu_de/customer/address/formPost/', headers=headers, data=data, allow_redirects=False)
    
    print(response.text)
    print(response.status_code)
