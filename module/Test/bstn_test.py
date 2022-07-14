"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] bstn.py                                           """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 19/05/2022 12:39:37                                     """
"""   Updated: 27/06/2022 18:49:30                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""
import json
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from ultilities.createsession import *
from ultilities.ProxyManager import getProxies

# def bstnEntry():

#     session = CFsession1()

#     session.headers = OrderedDict([
#         ('authority', 'raffle.bstn.com'),
#         ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
#         ('accept-language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7'),
#         ('cache-control', 'max-age=0'),
#         # Requests sorts cookies= alphabetically
#         # 'cookie': '_ga_9FC6HBPLQ6=GS1.1.1653349229.1.0.1653349229.0; _ga=GA1.1.586683679.1653349229; cf_clearance=7G.Q0t9IU1uNEKU4mxY.2JSYMg4pSzuE4p9mtdcXkKU-1653349230-0-150; __cf_bm=l.YGzvseYsvAY4_gcOvOwBbuQxF6vPY2om5QSbK59Ok-1653349230-0-Ac0UT3IPJYJwoCOPK+n0GJbD67sdBMduRGRO+PGsg8vv1Trl3ghrFv17De/4+jVv8SKYnuFpVdz4bCjA98MT62k=',
#         ('dnt', '1'),
#         ('referer', 'https://raffle.bstn.com/?__cf_chl_tk=m8RDzeLlSkWZVTCIDlrDt7fVCYGDn_GkBpkNv5V9gMs-1653349228-0-gaNycGzNB_0'),
#         ('sec-ch-ua', '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"'),
#         ('sec-ch-ua-mobile', '?0'),
#         ('sec-ch-ua-platform', '"macOS"'),
#         ('sec-fetch-dest', 'document'),
#         ('sec-fetch-mode', 'navigate'),
#         ('sec-fetch-site', 'same-origin'),
#         ('upgrade-insecure-requests', '1'),
#         ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'),
#     ])

#     print("Get Raffle Main Page")

#     response = session.get('https://raffle.bstn.com/')
    
#     print(response.status_code)

#     print("Get Raffle Shoe")

#     response = session.get('https://raffle.bstn.com/de-DE/nike-nike-x-travis-scott-air-trainer-1-grey-haze-dr7515-001-0263098')

#     # print(response.text)
#     print(response.status_code)


#     r = session.get('https://raffle.bstn.com/de-DE/nike-nike-x-travis-scott-air-trainer-1-grey-haze-dr7515-001-0263098')

#     with open("page_response.html", "w") as f:
#         f.write(r.text)
    
#     if r.status_code == 200:
#         text = json.loads(r.text)
        
        
        # text = r.text
        #print(text)
        # with open("text_response.html", "w") as f:
        #     f.write(text)
        # variants = json.loads(text).get("variants")
        # print(variants)
        # for i in variants:
        #     if "37" in i.get("attributes")[0].get("label"):
        #         product_id=i.get("product").get("id")
        #         print(product_id)
        # data = text.split('type="application/json">')[1].split('</script>')[0]
        # data = json.loads(text)
        # print(data)
        # with open("data_response.html", "w") as f:
        #     f.write(data)
        # sizes = data['product']['sizes']
        # print(sizes)
        # product_id = data['product'].get(profile["size"]) ## to fix

def TestBSTN():

    proxyList = getProxies()
    chosen_proxy = random.choice(proxyList)
    
    session = CFsession3(chosen_proxy)
    # session = CFsession1()
            
    r = session.get('https://raffle.bstn.com/de-DE/nike-dunk-high-retro-cargo-khaki-dd1399-107-0262810')

    if r.status_code == 200:
        text = r.text
        variants = json.loads(text).get('variants')
        print(variants)

        
    #     text = r.text
    #     with open("bstn_size_response.html", "w") as f:
    #         f.write(r.text)
    #     # data = text.split('type="application/json">')[1].split('</script>')[0]
    #     # data = json.loads(data)
    #     data = json.loads(text) 
    #     print(data)
    # #     sizes = data['product']['sizes']
    # #     print(sizes)
    # #     product_id = data['product'].get('41') ## to fix
    # #     print(product_id)
    # # else:
    # #     print("something went wrong")