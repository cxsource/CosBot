"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] testtest.py                                       """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 12/05/2022 01:20:24                                     """
"""   Updated: 19/05/2022 00:28:34                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import random


# profile = "14"


# print("Submitted Your Size..")
# try:
#     url = "https://de.afew-store.com/products/air-jordan-1-mid-mystic-navy-mint-foam-white"

#     url_link = url.replace("https://de.afew-store.com", "https://raffles.afew-store.com") \
#         .replace("https://en.afew-store.com", "https://raffles.afew-store.com")

#     json_link = url_link + ".json"
    
#     r = requests.get(json_link)
#     variants = r.json()["product"]["variants"]

#     variant_wanted = "not found"

#     if profile == "random":
#         size_info = random.choice(variants)
#         variant_wanted = size_info["id"]
        
#     for size in variants:
#         if size["title"] == profile:
#             variant_wanted = size["id"]
#     if variant_wanted == "not found":
#         print("We couldn't find the size.. We will choose a random size for you!")
#         size_info = random.choice(variants)
#         variant_wanted = size_info["id"]
#         print(variant_wanted)
# except Exception as SizeError:
#     print("There's a problem to scrape the correct sizes..", "AFEW", "error")

# import requests

# cookies = {
#     'cf_chl_2': '20eab7de4e1807c',
#     'cf_chl_prog': 'x13',
#     'cf_clearance': 'nRpnWCL6foGI6UbrBSH50W7TH.QYX8blJWZuWlveA9I-1652528072-0-1-2d31fbe9.c2f5a42c.12614d33-150',
#     'nakedcph.state': 'en-DE-0-0',
#     'AntiCsrfToken': '073a5249a48f4db59cef5b29079a0f13',
#     'png.state': 'Ea8E4U4DmI64fbBBK0BTXg2HUno9n9DFxZSvW+8AY/liO6rneipGEvd5Vg5MvJGdcA8hnCbRDJzEJMYFFyzVJBnmru5vb1kaNaE9qiZklbJOLoWA8UC3JTSWa0ObHAB7qbWO1w==',
#     '__cf_bm': 'UAjohjeNqlUJaXcNHi4sRTd_y0aR061ceQ.B9MLSaak-1652528072-0-Acy+omoY2ZVz49zLYwTv/Vl6vwoOv36XhRGKDOqt6JwwuMFHsqHPNzmXx7NLko4xz8ZnTOUIzAdry98NQ5ln1eA=',
#     'CookieInformationConsent': '%7B%22website_uuid%22%3A%22f9bd9a9d-e73a-46db-96d4-b498c1ae8dd7%22%2C%22timestamp%22%3A%222022-05-14T11%3A35%3A14.566Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.nakedcph.com%2Fen%2Fsearch%2Fbysearchdefinition%2F1282%22%2C%22consent_website%22%3A%22nakedcph.com%22%2C%22consent_domain%22%3A%22www.nakedcph.com%22%2C%22user_uid%22%3A%2273ff2fa9-bc58-4c2f-ba0b-3d1ccb464b85%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F101.0.4951.64%20Safari%2F537.36%22%7D',
#     '_gcl_au': '1.1.472856037.1652528115',
#     '_gid': 'GA1.2.790757063.1652528115',
#     '_gat_gtag_UA_36099866_1': '1',
#     '_fbp': 'fb.1.1652528114840.22770050',
#     '_ga_JZ8QLBHSKW': 'GS1.1.1652528072.1.1.1652528122.0',
#     '_ga': 'GA1.2.1276833141.1652528074',
# }

# headers = {
#     'authority': 'www.nakedcph.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'de-DE,de;q=0.9',
#     # Requests sorts cookies= alphabetically
#     # 'cookie': 'cf_chl_2=20eab7de4e1807c; cf_chl_prog=x13; cf_clearance=nRpnWCL6foGI6UbrBSH50W7TH.QYX8blJWZuWlveA9I-1652528072-0-1-2d31fbe9.c2f5a42c.12614d33-150; nakedcph.state=en-DE-0-0; AntiCsrfToken=073a5249a48f4db59cef5b29079a0f13; png.state=Ea8E4U4DmI64fbBBK0BTXg2HUno9n9DFxZSvW+8AY/liO6rneipGEvd5Vg5MvJGdcA8hnCbRDJzEJMYFFyzVJBnmru5vb1kaNaE9qiZklbJOLoWA8UC3JTSWa0ObHAB7qbWO1w==; __cf_bm=UAjohjeNqlUJaXcNHi4sRTd_y0aR061ceQ.B9MLSaak-1652528072-0-Acy+omoY2ZVz49zLYwTv/Vl6vwoOv36XhRGKDOqt6JwwuMFHsqHPNzmXx7NLko4xz8ZnTOUIzAdry98NQ5ln1eA=; CookieInformationConsent=%7B%22website_uuid%22%3A%22f9bd9a9d-e73a-46db-96d4-b498c1ae8dd7%22%2C%22timestamp%22%3A%222022-05-14T11%3A35%3A14.566Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fwww.nakedcph.com%2Fen%2Fsearch%2Fbysearchdefinition%2F1282%22%2C%22consent_website%22%3A%22nakedcph.com%22%2C%22consent_domain%22%3A%22www.nakedcph.com%22%2C%22user_uid%22%3A%2273ff2fa9-bc58-4c2f-ba0b-3d1ccb464b85%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F101.0.4951.64%20Safari%2F537.36%22%7D; _gcl_au=1.1.472856037.1652528115; _gid=GA1.2.790757063.1652528115; _gat_gtag_UA_36099866_1=1; _fbp=fb.1.1652528114840.22770050; _ga_JZ8QLBHSKW=GS1.1.1652528072.1.1.1652528122.0; _ga=GA1.2.1276833141.1652528074',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
# }

# response = requests.get('https://www.nakedcph.com/en/search/bysearchdefinition/1282', cookies=cookies, headers=headers)


# links ="https://raffle.bstn.com/verify/"
# link = "https://www.bstn.com/eu_de/customer/account/confirm/?back_url=&id=1427030&key=j6L7BPCtCnqYPndLkYxKAAn9mmQawTR0"
# token = links.replace('https://www.bstn.com/eu_de/customer/account/confirm/?back_url=&id=1427030&key=j6L7BPCtCnqYPndLkYxKAAn9mmQawTR0', '')
# print(token)


## getting the edit page

#     headers = {
#         'authority': 'www.bstn.com',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-language': 'de-DE,de;q=0.9',
#         # Requests sorts cookies= alphabetically
#         # 'cookie': 'gender=men; _ALGOLIA=anonymous-f76e196e-712d-478c-8d12-a3f03a53bb34; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; form_key=33wIDfH8eJgtWZSy; cjConsent=MHxZfDB8Tnww; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; scarab.visitor=%227622DAE98BE4DEC8%22; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1652777861%2C%22type%22%3A%22category%22%2C%22version%22%3A%227ff7db62-4f82-4346-af4a-421f8a8bf045%22%7D; _gcl_au=1.1.1388763952.1652777861; __gtm_referrer=https%3A%2F%2Fraffle.bstn.com%2F; _gid=GA1.2.229697031.1652777861; _fbp=fb.1.1652777861469.1569413978; cebs=1; _tt_enable_cookie=1; _ttp=49965965-3fdc-40a4-a7af-708e1144a199; aa-search=aa-Y3VzdG9tZXItc25lYWtlcmNkOUBnbWFpbC5jb20tMTQyNzAzMA; __cf_bm=8LHzlOTNyV.sznAk2YZ41Lu42wFLjUDZBDs7b94Crlk-1652828685-0-AYjZOO4gnuTO51UYhndO6dMPeog/l7Gv08Rtmo2ir0g4K4G65syLhQWKo7Fyh3B6rUuRl/Vl4x2VIXI/sn4Eazo=; cf_clearance=gerssf0jzSBpu.bxQoS3uRdSpEAZZpw8B6R.PjKWOoA-1652828842-0-150; _ga_9FC6HBPLQ6=GS1.1.1652827557.2.1.1652828843.0; mage-cache-sessid=true; PHPSESSID=d4sa850vrdue4g0hltv90fj43l; private_content_version=d8aba6fb990c61a1b3a4ba5f3de516a1; form_key=33wIDfH8eJgtWZSy; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; _ga_3480EPZ6W5=GS1.1.1652827549.2.1.1652828925.59; _ga=GA1.1.872180635.1652777857; _ga_NCXNW87L01=GS1.1.1652827549.2.1.1652828925.0; _uetsid=68c057d0d5bf11ec8a99b9c8313837a2; _uetvid=68c037e0d5bf11ec9da13350e14564fa; cto_bundle=ESqexV9xNFV5OWdSbTVGN0N6a2ZjeUhGWSUyQnVLd3I1V2FrYXFtWmdsdCUyRmpMQ0lkUEROaExXNEg1empFUDdLUnd4T2VaSVdYR0Y1TWVEWHFKYmxRWTRYMEE2TTl2Q3ZVWXVxYzRKVFVVdllqdTczTGdqRFNrbmtrNXhjelNuZ2p3eDhuMXlENVc2czJ1dFY0eFRTTkVQT1JjemhLMlh2MWxGV2h6NXdSNzIxZFJjMlhnJTNE; section_data_ids=%7B%22emrssection%22%3A1652828926%2C%22cart%22%3A1652828924%2C%22customer%22%3A1652828924%2C%22wishlist%22%3A1652828924%2C%22rafflesection%22%3A1652828927%2C%22compare-products%22%3A1652828924%2C%22last-ordered-items%22%3A1652828924%2C%22directory-data%22%3A1652828924%2C%22instant-purchase%22%3A1652828924%2C%22captcha%22%3A1652828924%2C%22sociallogin%22%3A1652828924%2C%22recently_viewed_product%22%3A1652828924%2C%22recently_compared_product%22%3A1652828924%2C%22product_data_storage%22%3A1652828924%2C%22paypal-billing-agreement%22%3A1652828924%2C%22messages%22%3A1652828924%7D; ABTasty=uid=myzdmqd01k04pzg7&fst=1652777861444&pst=1652777861444&cst=1652827548476&ns=2&pvt=26&pvis=25&th=822959.0.24.23.2.1.1652777861534.1652828927394.1; ABTastySession=mrasn=&sen=46&lp=https%253A%252F%252Fwww.bstn.com%252Feu_de%252Fmen%252Fupcoming.html; _ce.s=v~80738519b3dd3ed5ebf0a583398cfdc4152a0f58~vpv~0~v11.rlc~1652827549279~ir~1~gtrk.la~l3arqm69',
#         'referer': 'https://www.bstn.com/eu_de/customer/account/index/',
#         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"macOS"',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
#     }

#     response = session.get('https://www.bstn.com/eu_de/customer/address/edit/', headers=headers)

# ## add adress infos 

#     headers = {
#         'authority': 'www.bstn.com',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-language': 'de-DE,de;q=0.9',
#         'cache-control': 'max-age=0',
#         'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryZGgCDCADwGp5791a',
#         # Requests sorts cookies= alphabetically
#         # 'cookie': 'gender=men; _ALGOLIA=anonymous-f76e196e-712d-478c-8d12-a3f03a53bb34; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; form_key=33wIDfH8eJgtWZSy; cjConsent=MHxZfDB8Tnww; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; scarab.visitor=%227622DAE98BE4DEC8%22; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1652777861%2C%22type%22%3A%22category%22%2C%22version%22%3A%227ff7db62-4f82-4346-af4a-421f8a8bf045%22%7D; _gcl_au=1.1.1388763952.1652777861; __gtm_referrer=https%3A%2F%2Fraffle.bstn.com%2F; _gid=GA1.2.229697031.1652777861; _fbp=fb.1.1652777861469.1569413978; cebs=1; _tt_enable_cookie=1; _ttp=49965965-3fdc-40a4-a7af-708e1144a199; aa-search=aa-Y3VzdG9tZXItc25lYWtlcmNkOUBnbWFpbC5jb20tMTQyNzAzMA; __cf_bm=8LHzlOTNyV.sznAk2YZ41Lu42wFLjUDZBDs7b94Crlk-1652828685-0-AYjZOO4gnuTO51UYhndO6dMPeog/l7Gv08Rtmo2ir0g4K4G65syLhQWKo7Fyh3B6rUuRl/Vl4x2VIXI/sn4Eazo=; cf_clearance=gerssf0jzSBpu.bxQoS3uRdSpEAZZpw8B6R.PjKWOoA-1652828842-0-150; _ga_9FC6HBPLQ6=GS1.1.1652827557.2.1.1652828843.0; mage-cache-sessid=true; PHPSESSID=d4sa850vrdue4g0hltv90fj43l; private_content_version=d8aba6fb990c61a1b3a4ba5f3de516a1; form_key=33wIDfH8eJgtWZSy; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; cto_bundle=ESqexV9xNFV5OWdSbTVGN0N6a2ZjeUhGWSUyQnVLd3I1V2FrYXFtWmdsdCUyRmpMQ0lkUEROaExXNEg1empFUDdLUnd4T2VaSVdYR0Y1TWVEWHFKYmxRWTRYMEE2TTl2Q3ZVWXVxYzRKVFVVdllqdTczTGdqRFNrbmtrNXhjelNuZ2p3eDhuMXlENVc2czJ1dFY0eFRTTkVQT1JjemhLMlh2MWxGV2h6NXdSNzIxZFJjMlhnJTNE; _ce.s=v~80738519b3dd3ed5ebf0a583398cfdc4152a0f58~vpv~0~v11.rlc~1652827549279~ir~1~gtrk.la~l3arqm69; _ga_3480EPZ6W5=GS1.1.1652827549.2.1.1652829132.60; _ga_NCXNW87L01=GS1.1.1652827549.2.1.1652829132.0; _ga=GA1.1.872180635.1652777857; _uetsid=68c057d0d5bf11ec8a99b9c8313837a2; _uetvid=68c037e0d5bf11ec9da13350e14564fa; ABTasty=uid=myzdmqd01k04pzg7&fst=1652777861444&pst=1652777861444&cst=1652827548476&ns=2&pvt=27&pvis=26&th=822959.0.25.24.2.1.1652777861534.1652829132846.1; ABTastySession=mrasn=&sen=48&lp=https%253A%252F%252Fwww.bstn.com%252Feu_de%252Fmen%252Fupcoming.html; section_data_ids=%7B%22emrssection%22%3A1652829132%2C%22cart%22%3A1652828924%2C%22customer%22%3A1652828924%2C%22wishlist%22%3A1652828924%2C%22rafflesection%22%3A1652829133%2C%22compare-products%22%3A1652828924%2C%22last-ordered-items%22%3A1652828924%2C%22directory-data%22%3A1652828924%2C%22instant-purchase%22%3A1652828924%2C%22captcha%22%3A1652828924%2C%22sociallogin%22%3A1652828924%2C%22recently_viewed_product%22%3A1652828924%2C%22recently_compared_product%22%3A1652828924%2C%22product_data_storage%22%3A1652828924%2C%22paypal-billing-agreement%22%3A1652828924%2C%22messages%22%3A1652828924%7D',
#         'origin': 'https://www.bstn.com',
#         'referer': 'https://www.bstn.com/eu_de/customer/address/edit/',
#         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"macOS"',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
#     }

    # data = {
    #     'form_key': form_key, # 33wIDfH8eJgtWZSy
    #     'success_url': '',
    #     'error_url': "",
    #     'firstname': 'Max',
    #     'lastname': 'Moritz',
    #     'street[0]': 'Eichwischen',
    #     'street[1]': '17',
    #     'street[2]': '',
    #     'country_id': 'DE',
    #     'postcode': '22143',
    #     'city': 'Hamburg',
    #     'telephone': '017612345678'
    # }

#     # data = '------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="form_key"\r\n\r\n33wIDfH8eJgtWZSy\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="success_url"\r\n\r\n\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="error_url"\r\n\r\n\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="firstname"\r\n\r\nMax\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="lastname"\r\n\r\nMoritz\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="street[0]"\r\n\r\nEichwischen\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="street[1]"\r\n\r\n17\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="street[2]"\r\n\r\n\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="country_id"\r\n\r\nDE\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="postcode"\r\n\r\n22143\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="city"\r\n\r\nHamburg\r\n------WebKitFormBoundaryZGgCDCADwGp5791a\r\nContent-Disposition: form-data; name="telephone"\r\n\r\n017612345678\r\n------WebKitFormBoundaryZGgCDCADwGp5791a--\r\n'

#     response = session.post('https://www.bstn.com/eu_de/customer/address/formPost/', headers=headers, data=data)
#     print(response.text)
#     print(response.status_code)
