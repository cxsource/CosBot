"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] bstnfinaltest.py                                  """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 27/06/2022 18:49:51                                     """
"""   Updated: 05/07/2022 12:03:25                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import json
import requests
from bs4 import BeautifulSoup
from ultilities.createsession import *
from ultilities.ProxyManager import getProxies


def TestBSTN():

    proxyList = getProxies()
    chosen_proxy = random.choice(proxyList)
    
    session = CFsession3(chosen_proxy)


    r = session.get('https://raffle.bstn.com/de-DE/nike-dunk-high-retro-cargo-khaki-dd1399-107-0262810')

    json_data = {
        'operationName': 'loginAndRetrieveCustomerData',
        'variables': {
            'email': 'sneakercd3@gmail.com',
            'password': 'Password007!',
        },
        'query': 'mutation loginAndRetrieveCustomerData($email: String!, $password: String!) {\n  loginAndRetrieveCustomerData(email: $email, password: $password) {\n    firstname\n    lastname\n    email\n    instagram_name\n    registered_raffles\n    addresses {\n      id\n      firstname\n      lastname\n      street\n      city\n      region {\n        region_id\n        region_code\n        region\n        __typename\n      }\n      postcode\n      country_code\n      country_name\n      telephone\n      __typename\n    }\n    __typename\n  }\n}',
    }

    r = session.post('https://raffle.bstn.com/graphql', json=json_data)
    print(r.status_code)
    
            
    r = session.get('https://raffle.bstn.com/us_en/new-balance-new-balance-x-joe-freshgoods-u9060v1-d-u9060jf1-0277270')
    print(r.status_code)

    # soup = BeautifulSoup(r.text)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        raffle_details = json.loads(soup.find("script", {"id":"__NEXT_DATA__"}).text)
        # print(raffle_details)
        variants = raffle_details.get("props").get("pageProps").get("raffleProduct").get("variants")
         #.get("attributes")
        # print(variants)

        size = "41,5"

        for a in variants:
            print(a.get("attributes")[0].get("label"))
            if a.get("attributes")[0].get("label") == size: ## bekomme alle sizes
                # print(a.get("product").get("id"))
                product_id = a.get("product").get("id")
                print(product_id)

        # for attr in variants:
        #     attributes = (attr['attributes'][0])
        #     print(attributes)
            # product = prod['product']
            # print(product)
            # for p in variants:
            #     product = p['product']
            #     print(product)
            # for v in attributes:
            #     if v["label"] == size:
            #         product_id = json.loads(variants).get('product')
            #         print(product_id)


            
            # for p in variants:
            #     product = p['product']
            #     print(product)
            # for v in attributes:
            #     if v["label"] == size:
                    
            #         product_id = v["value_index"]
            #         print(product_id)
            #         break