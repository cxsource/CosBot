"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] footshop test.py                                  """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 31/05/2022 11:38:05                                     """
"""   Updated: 31/05/2022 17:13:03                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import random
import time
import json 
import re
# from ultilities.createsession import getsession
from ultilities.ProxyManager import getProxies



# proxyList = getProxies()

# proxy = random.choice(proxyList)
# # print(proxy)

# def getsession(usedproxy):

#     if usedproxy is None:
#         session = requests.Session()
#     else:
#         session = requests.session()
#         proxyParts = usedproxy.split(":")
#         session.proxies.update(
#             {
#                 "http": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
#                 "https": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
#             }
#         )
#         return session

# session1 = getsession(proxy)
# session = requests

def global_sizes(url):

    try:
        r = requests.get(url, headers={
                         'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"})
    except Exception as e:
        print(f'Error loading rafflepage: {e}')
        time.sleep(5)

    initial_state = json.loads(re.search(
        "<script>window\\.__INITIAL_STATE__ = ({.+})</script>", r.text).group(1))
    raffle_id = initial_state['raffleDetail']['raffle']['id']

    print(raffle_id)

    sizes = {}
    for size_set in initial_state['raffleDetail']['raffle']['sizeSets']: ## hier bekomme ich die sizeSets wie Men, Women, Unisex, Kids
        for size in initial_state['raffleDetail']['raffle']['sizeSets'][size_set]['sizes']: ## list of sizes 

            size_info = size['eur']
            print(size_info)

            
            
    #         size["size_set"] = size_set
    #         try:
    #             size['us'] = int(size['us'])
    #         except ValueError:
    #             size['us'] = float(size['us'])

    #         sizes[size['us']] = size

    # return sizes, raffle_id

global_sizes("https://releases.footshop.com/vans-vault-x-imran-potato-knu-skool-vr3-lx-LaGjFYEBKNDGyVGQNe30")


# headers = {
#     'Host': 'releases.footshop.com',
#     # Requests sorts cookies= alphabetically
#     # 'Cookie': '_vsid=f07f9a34-a00f-48b0-b9e3-05e73c57dd6b; _ga=GA1.2.608142770.1635767974; _gcl_au=1.1.499987282.1652518233; _gid=GA1.2.1121585781.1653925523',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
#     'accept': 'application/json, text/plain, */*',
#     'cache-control': 'no-cache',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
#     'sec-ch-ua-platform': '"macOS"',
#     'dnt': '1',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://releases.footshop.com/register/aqKrFYEBKNDGyVGQEh6v/Unisex/4c39cede-e030-11ec-b783-cee84d9682c5',
#     'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
# }

# response = requests.get('https://releases.footshop.com/api/raffles/aqKrFYEBKNDGyVGQEh6v', headers=headers)

# # headers = {
# #         'Host': 'releases.footshop.com',
# #         # Requests sorts cookies= alphabetically
# #         'Cookie': '_vsid=1203a5b2-24c2-4e40-acbe-b611515b83c3; _gcl_au=1.1.1296509918.1652515468; _fbp=fb.1.1652515467904.1676578708; _ga=GA1.2.993097310.1652515468; _gid=GA1.2.820386360.1653643165',
# #         'cache-control': 'max-age=0',
# #         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
# #         'sec-ch-ua-mobile': '?0',
# #         'sec-ch-ua-platform': '"macOS"',
# #         'upgrade-insecure-requests': '1',
# #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
# #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# #         'sec-fetch-site': 'none',
# #         'sec-fetch-mode': 'navigate',
# #         'sec-fetch-user': '?1',
# #         'sec-fetch-dest': 'document',
# #         'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
# #     }

# # r = session.get('https://releases.footshop.com/vans-vault-x-imran-potato-sk8-hi-vr3-lx-aqKrFYEBKNDGyVGQEh6v', headers=headers)
# # print(r.status_code)