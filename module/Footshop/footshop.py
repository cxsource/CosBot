"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] footshop.py                                       """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 25/05/2022 23:25:10                                     """
"""   Updated: 31/05/2022 00:18:41                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import json
import time
import random
import requests
from ultilities.createsession import getsession
from ultilities.CaptchaManager import Hcaptchasolver
from ultilities.adyen_tools import encrypt
from ultilities.adyen_tools import bin_lookup
from ultilities.adyen_tools import gen_risk_data
from ultilities.adyen_3ds_handler import handle_3ds



sitekey = "55c7c6e2-6898-49ff-9f97-10e6970a3cdb"
session = requests.session()


def FootshopEntry():
    
    ###-------------------------------------
    ###      Getting the raffle page        |
    ###-------------------------------------

    headers = {
        'Host': 'releases.footshop.com',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_vsid=1203a5b2-24c2-4e40-acbe-b611515b83c3; _gcl_au=1.1.1296509918.1652515468; _fbp=fb.1.1652515467904.1676578708; _ga=GA1.2.993097310.1652515468; _gid=GA1.2.820386360.1653643165',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response = session.get('https://releases.footshop.com/adidas-yeezy-foam-runner-lzWuBIEBKNDGyVGQXOX7', headers=headers)
    
    print(response.status_code)

    ###-------------------------------------
    ###    Another Step to get the page     |
    ###-------------------------------------

    headers = {
        'Host': 'releases.footshop.com',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_vsid=1203a5b2-24c2-4e40-acbe-b611515b83c3; _gcl_au=1.1.1296509918.1652515468; _fbp=fb.1.1652515467904.1676578708; _ga=GA1.2.993097310.1652515468; _gid=GA1.2.820386360.1653643165',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'accept': 'application/json, text/plain, */*',
        'cache-control': 'no-cache',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://releases.footshop.com/register/lzWuBIEBKNDGyVGQXOX7/Unisex/dc156ce2-dd98-11ec-9f4c-cee84d9682c5',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response = session.get('https://releases.footshop.com/api/raffles/lzWuBIEBKNDGyVGQXOX7', headers=headers)

    ###-------------------------------------------------
    ###    Enter email/phone to checking dublicity      |
    ###-------------------------------------------------


    headers = {
        'Host': 'releases.footshop.com',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_vsid=1203a5b2-24c2-4e40-acbe-b611515b83c3; _gcl_au=1.1.1296509918.1652515468; _fbp=fb.1.1652515467904.1676578708; _ga=GA1.2.993097310.1652515468; _gid=GA1.2.820386360.1653643165',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'accept': 'application/json, text/plain, */*',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'origin': 'https://releases.footshop.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://releases.footshop.com/register/lzWuBIEBKNDGyVGQXOX7/Unisex/dc156ce2-dd98-11ec-9f4c-cee84d9682c5',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    json_data = {
        'email': 'charafdissou1@gmail.com',
        'phone': '017664157817',
        'id': None,
    }

    response = session.post('https://releases.footshop.com/api/registrations/check-duplicity/lzWuBIEBKNDGyVGQXOX7', headers=headers, json=json_data)

    
    ###----------------------------------
    ###  Submitting raffle information   |
    ###----------------------------------

    headers = {
        'authority': 'releases.footshop.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_vsid=1203a5b2-24c2-4e40-acbe-b611515b83c3; _gcl_au=1.1.1296509918.1652515468; _fbp=fb.1.1652515467904.1676578708; _ga=GA1.2.993097310.1652515468; _gid=GA1.2.820386360.1653643165',
        'origin': 'https://releases.footshop.com',
        'referer': 'https://releases.footshop.com/register/lzWuBIEBKNDGyVGQXOX7/Unisex/dc156ce2-dd98-11ec-9f4c-cee84d9682c5',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }

    json_data = {
        'id': None,
        'sizerunId': 'dc156ce2-dd98-11ec-9f4c-cee84d9682c5',
        'account': 'New Customer',
        'email': 'charafdissou7@gmail.com',
        'phone': '01765625737',
        'gender': 'Mr',
        'firstName': 'Charaf',
        'lastName': 'Dissou',
        'instagramUsername': 'charafdissou',
        'birthday': f"{random.randint(1989, 2000)}-0{random.randint(1, 9)}-{random.randint(1, 28)}",
        'deliveryAddress': {
            'country': 'DE',
            'state': '',
            'county': '',
            'city': 'Hamburg',
            'street': 'Sportplatzring',
            'houseNumber': '15',
            'additional': '',
            'postalCode': '22527',
        },
        'consents': [
            'privacy-policy-101',
        ],
        'verification': {
            'token': Hcaptchasolver(sitekey, f"https://releases.footshop.com/register/lzWuBIEBKNDGyVGQXOX7/Unisex/dc156a1c-dd98-11ec-8fc7-cee84d9682c5") ## da müssen noch die daten geändert werden im link
        },
    }

    response = session.post('https://releases.footshop.com/api/registrations/create/lzWuBIEBKNDGyVGQXOX7', headers=headers, json=json_data)
    
    
    ###----------------------------------
    ###      Payment Part                |
    ###----------------------------------

    adyen_encryptor = encrypt.Encryptor("10001|A05EE5BCE99CA6C29B937BF6A5F0392A586C53EEEF3E4F848ACB086D35F54E38B99BAF63C297689D09E533E6B3F2606608492B618D9219F47C7B7D97A56EFC9E5F118AB5257BD57DFB09A7A22DCA4C9BD17BDD22871A903FAA840F7897A2036E02CB3956C6CAE6B712C3E0A83BCD42A9B4E4008D177935901C853E6A4F8705DF3F6D3A3C350C5A488B5C931C96C021959BF9317E642D96724744238A4F8EB8F5304BC05789C5942490FB7DD851C740A1310058304ADE2265B014196F871FD3DDADF0E4C4C698EE217A16BC6CC9308D23E21A9C98764F0F37874F29FD6EEA7FAA3DADB18DD8D7C48E6E91E126BA378129AFC2FD5C606AF03110183D24080BD603")

    while True:
        try:
            headers = {
                'authority': 'releases.footshop.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'no-cache',
                'content-type': 'application/json;charset=UTF-8',
                # Requests sorts cookies= alphabetically
                # 'cookie': '_vsid=1203a5b2-24c2-4e40-acbe-b611515b83c3; _gcl_au=1.1.1296509918.1652515468; _fbp=fb.1.1652515467904.1676578708; _ga=GA1.2.993097310.1652515468; _gid=GA1.2.820386360.1653643165',
                'origin': 'https://releases.footshop.com',
                'referer': 'https://releases.footshop.com/register/lzWuBIEBKNDGyVGQXOX7/Unisex/dc156a1c-dd98-11ec-8fc7-cee84d9682c5',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
            }

            cc_data = {
                'riskData': gen_risk_data.gen_risk_data(),
                
                'paymentMethod': {
                    'type': 'scheme',
                    'holderName': 'C.Dissou',
                    'encryptedCardNumber': adyen_encryptor.encrypt_card_data(number='5167603150366622'), # 'adyenjs_0_1_25$ghOQRhUDTm1VsrE3ROU9e8GwQMeiRiTqHDju6grYWkQcwbdDysorA/wodv035R+6fmVW+hg4Z04xI1DOx9EOjIo0lAZQGidbcdDWoh43tL9oR/1i+gCgg24cgHahIMNzINnj5fGso/WpjxK+qfrUHwREIYiqMK2LBd6nDax6MHUyppzW8eKhOgzcY1YIloGsn20Mi1CD0fwfpJLkqSe2cly1dt8UBI8UqkSdtqwkLNTuGbag229Jvo72HRH/3oWTG6Lmc3pZhOBmFV4hYayrr2lUMj3TEKwAokhoHkInVye+uaLrwTpdvESuqQEeCO5ZraEIF/qGvoeE+S6wd/fpfw==$lD/jYAfgAIACUoCit8pJWzdq+oI7UEwS6cSA+sufdP6itmdFaBQBxtbxwKQv84Upj+mZ5ucpl5QqcBuFy3tOIM/pH2sEcsGJBVqxwpuFoLqhVUUyi3m3YRuI247Rhx+IwYmyYbZH16AiG6Q6yZAQ6bFB13C2QzHPTbEEg7mMvA4IYVm7Sh/PkSV1NqYijGoCCaAHzSZempLUx7iNX01Xwc12RxLCG9Rl/vmAqXe2PjYcjEpG8bg+OEfCk8yVCFz+lKv0nxhDA015vwRx55mxYsIMi/hT91RLeS9FUaIOooCe8CwG2k7ZrCJHONmYqIIE4rzBiUUdnPCJ1ZcZdVz0xax2xPAsTZZJT+jueHKOFW1ZT18KbgKQ5luxIFoUNKERW6OINJq9qfvCbVdaJ4ZlUxiDgYUWlDqxAXqFqBNJMLJbRnG6bcSPgkBiwmBCeemVg87+vuEzUe7p/XHkg3plmTvG2Ozj49bFG5tJC1Z215TJHzNKnWYkrTyv5qpf8lurmEt5rGKjB1T62WlLfX+Leh4PCcXNPoJr53tdmXqb9fuLnqU4R/ykHQ6jQzCMb7AyAcs9EnLUZ5fktrcJGmV8Rz+vjh9QnDSCzwjUYgqBu3bs6y5L9S1Cj3DTG4Vj8baT7oMTdYsf0ab6BXVHYg7hCT4macovqnphtf2CCadxvRAvpaMaabzuBEnVjl+vwJGS8yrYn4we5jwI94F5Yl6/PrunCtdOjxe6Bxl4JfadoOy83i0TFYt+XUGV3SkkRICIZN9oAsVH5e40XPvhiQhzPABsEr49fCXL9awiDj4yVvZbF2TRe5rniKdDhbEvNEysD77VtkVedxZ9fMv5bc1DsgInr3SK0fAsGaOfZMVH0/XkteaEVzIlCyAN21fXw1gtaN9+rpzSnCj3NzZNk5W8fpJs7xQoRenXn8tHwl8c+Mts9Miob4Opg1gLOR0CEP81rXQhd9FZLxmaS7fxXpstcQcEWahpLzuBrJH/+RXJ16tDTxhKj4c/no102ZSSSXC528VGx2FsqFadPqRteK24DOPVOst+9IAOuS3uXqryDzu8ZcCKYJ/hbyg0j/Tqk5VPTuZQRTgAyU3uwbOvTMlMhRSc',
                    'encryptedExpiryMonth': adyen_encryptor.encrypt_card_data(expiry_month='10'), # adyenjs_0_1_25$nKRHuDs3cEcJwItRzrfgFaHcqMa104yK4sLApeZ7+S0b3XzNro8zA4C8euEGq9d1nFcjLBTiBLykEb2EsV98iEOku/EIigaKjt734pVbXniYTr4LaMOuvsqaYvR/rGZIkxyHc/TwlSC5eVNHzL6IKKrJcmkslM42dMgPpxfl6FLMlZglnbSQIgucGJ6x+9bJ7W2uKV1eVwJn8Do/afndJwJVJ+wqKqxyFup8eUdhEwYkbMVs/9AZ0vSjB8JPl5j1WWoJHRVQrVcluKLJXShmKMizuEyd7qKDj9b4h62wlaMYAXw9aGEW5K6Cl3lj1uVhr+btfsIQSQTtF2Aa/H78QQ==$ODipSlmBYnrDnv0lu1cF40Cnq12608KiSVjRwzvsj7bsFHBL4Qt2ghkI6hrVjyNYrn9bH8O+QnlA3tPKppdEyvGw2N0NVFf48KQXTvJRl0h5/BL7b3e+DNpIYRSSB9MlER+uS1PY2o6i52w+PRMihopwwgPzwGVIDYKJ5GJMsdwhpww18AqZYUqlRUUTzwJnLycduG7xSKbw1DNiwSGgjIpymhVWeFrP7Go4pnPxG+JZnOMho/611ml2FJLqjgzs2gID4VTwUYFNoIBOHxECgeZ0ZAfT3d3xn9SRKiik6gbsN+demmFEGCw9MsaPsoiXPC09MIW0wD74ywxrP32SYO3j3FhTGtFetTDXnZ+VCHuo/MhQ7b2/yOXGUHsTZQhzovh/lUulrYRrMOdB+Sg963k/HOMw56b6M1GXBsdRk8lpW/FgWZOuiQrmLgdlnMxEQpn1YALd1SR0Yri8fuyfPw==',
                    'encryptedExpiryYear': adyen_encryptor.encrypt_card_data(expiry_year='2025'), # adyenjs_0_1_25$V4+OMFzAh/f+4ujw3WaQuQVA+36KmzbQ5LJhahpv/GqTBPi5bSDqxWoPrz5VXKxXSrED3jt7qPzHN9lsckxfg1v1AySdGB2Ug3C78DY+QJRPkeSTfeoJ+IaCqe0j3cmrPTJkItzHPMt88o+epV0mA8CqKiat7yDuh42ogwJW/ebbJolxrPjBSV4fODljFImIYM3F7/8vj9cA5IJq1Q5TTnUvVgU92V6xYA41StJ1Eb4+j+Zd7KhEnbg7wp5O/ZNySwYXU4HCBkvyaZIa6bYIOjPLy7HndmCUxaL0H8XMrSMSj1XO35PbXPxMvmD7M/t4NAZ/S4f/597HLY5EX7BamQ==$6N5jHP96ZB9SLCohaaRF2N1L4BOE2uMMOs9VK4aBCGCjZE6wkUCQNnC0/OEDm1plMHJc5FtiUHRFVjKND34yG4Xy8reMTCVWYPY3RlpcUGdJFYIMbkmByNhWc2WX1dqJJ7VRu2euN8ELc7MDh3PdHXUjit7P41NeyAvSqmuxCNUXxiqtdch786YqGmpqEwVs2Vn1b1R+loM490K43Lvl5l+/9onCBeE4ESMtZ17XutKEXr7Pid/Qu7U3aIGNwEYxE51eeN61G47oEWOFzPtb/sa+0MAIIIaX//ou58HSO2NiYuCqVPMa8U0cOiPhRz1VeAg2gZndIzwTm5m55sMN+IRZi0u1oAOarw9fDDcHRIHAG6J1qkkbmHeAB4YRkOrJoxftLK4bgvOa1bxvPIAMpdrihltQjRPSoP6Fm5b6dv8RUiKgQM4r5cPjtrKkkoowAnVjrgjaMXYCUZOKbExuthM=',
                    'encryptedSecurityCode': adyen_encryptor.encrypt_card_data(cvc='102'), # adyenjs_0_1_25$b6ucoTofCuyHu/cpvGHzUl4tKs0obgnJjWkzb6JdeNpH3IPmi5fAxhKZF1OmEHBPWjpBnSOmXdyv2GtGA6/JDCNyBSV+JfuYTmuE2XbLWuEh7q2X/b1Vl599r55n/kBRikSjBCf6/yHvGrrefa1H3jqT43dvYva1GuNclyimn5m1kzSwB39iKSdTeZ4TrW/s9+J/0qTleZ0x4BMFrSLWtWpUKONnMY6FKM/DiLXaKBf9G9VytT7a7hBdi+fqfO50YFkrOm5MQhwhA6X/oLwVljrCDggjO31JhmGQdz4DplF/3b8S8vAEQgZ6o3FrkZP1cH8KQBHCp2x3A5hdZBOpdQ==$M+OTdVqrLAktD23J9atfF8JI7neT7b8XhaU+vNNLgDr5hjSysJ7chiw6h+q9mIRmLKsvJQzenYggRy8+Go350h+bWEq2d06kFVgQu99e+QV+D/NXPf/wIkMma6EjAPkE8cjITWNDk2vgFAYdURFEZf17GkD93BexV9IZMi7qiKdCPwjKm5M/dWdXQpDfmqBaA7G20AKcnypx4bma+H85h/m1ze793Z4dGICrZltegB/dRT79pY3prYqf39Lt8HcxBYbGXBWO4jwp2K/7UNdakpPuftuNSNnLgdJuqNe+zrPgOclJQIrafFvenCCSWFMorGGGSd6cxNNbmoleWZ7dkV7AL/QaB8/l0s6op6UeMRQjZDjyj733Y77Htmt9z328+a0tUwdSRHNs/BVbOKF11KP81C5U06dGVAOVygKG0MXycKAr4JdugAW9xkIH6q3gSFQYgaGNPB9rUr4JaQ+Ohaz63IwlGNf8PT6oaoYqMC/3q5dyfLhsUhXQScFO6S6Q7h+eJHR7GoBgQRHYwzzwN8tWfNyzu7ZpHgnSUButvDwfFeImIy0OrEksDyYQGbttHpagPA3rlEuB52xI+b16alfeb03CgBu3M59VDryPUCH1MtPnCXJqnlvhd1681YFxP3K/bGslAdZj6/X26b0N15IN0ytTejvQNHNIDoUdgr+PBOgwxF02xDMr914idGoO8VlAanaLlW2M101LTU3/dj6FH8Gr7EBlpa7HfcyvqQss/6t5TP2d5tQzFYcaDVtnKSPbIWHb2i77vIGye7+agLrqYN+hwhnOPHiZXUU7E0QAiWA=',
                    # 'brand': bin_lookup.get_card_brand(session, adyen_encryptor.encrypt_card_data(bin_value=adyen_encryptor.encrypt_card_data(number='5167603150366622')[:6]), json_response['details']['paymentMethods']['paymentMethods'][0]['brands'], json_response['details']['clientKey']) # 'mc',
                },
                
                'browserInfo': {
                    'acceptHeader': '*/*',
                    'colorDepth': 30,
                    'language': 'de-DE',
                    'javaEnabled': False,
                    'screenHeight': 900,
                    'screenWidth': 1440,
                    'userAgent': session.headers['user-agent'],
                    'timeZoneOffset': -120,
                },
                'origin': 'https://releases.footshop.com',
                'clientStateDataIndicator': True,
            }
        except Exception as e:
            print(f'Error encrypting card details: {e}')
            time.sleep(10)
            continue

        json_response = response.json()

        # registration_id = json_response.get('registration')['id']

        try:
            registration_id = json_response.get("id", False)
            if not registration_id:
                registration_id = json_response.get(
                    "registration").get("id")

            response = session.post(f"https://releases.footshop.com/api/payment/make/{registration_id}", json=cc_data)
        except Exception as e:
            print(f"Error completing the registration: {e}")
            time.sleep(10)
            continue

        if response.status_code not in (400, 403, 404, 500, 502):
                try:
                    card_response = response.json()
                except Exception:
                    print(
                        f'Error submitting card, status code: {response.status_code}')
                    time.sleep(10)
                    continue

                errors = card_response.get("errors", None)

                if errors is None:
                    card_response.get("errors", None)

                if errors is not None:
                    print(f'Error submitting card: {errors}')
                    time.sleep(10)
                    return False

                if card_response['registration']['noWin']:
                    print(f'Entry was filtred out...')
                    return False

                else:
                    if threeDS(response.json()):
                        return True
                    else:
                        return False

def threeDS(json):
    try:
        payment_action = json['paymentDetail']['action']

        json_response = json

        # registration_id = json_response.get('registration')['id']

        try:
            registration_id = json_response.get("id", False)
            if not registration_id:
                registration_id = json_response.get(
                    "registration").get("id")
        except Exception as e:
            print(f"Error happendend while getting registration_id: {e}")

        def redirect_hook(driver):
            threeds_confirmed = False
            for i in range(300):
                if driver.current_url.startswith("https://releases.footshop.com/registration/finish"):
                    threeds_confirmed = True

                    time.sleep(1)
                    break
                else:
                    time.sleep(1)

            return threeds_confirmed

        threeds_result = handle_3ds(payment_action, session, "live_Y44FYNDGDNFBNKSYXDDP4H2LBQKOU4N3",
                                    f"https://releases.footshop.com/api/payment/make/{registration_id}", redirect_hook)

        if threeds_result is not None:
            if not threeds_result.json()['registration']['authorized']:
                print(f"Entry unauthorized with 3DS")
                return False

    except Exception as exc:
        print(f"Couldn't confirm 3DS: {exc}")
        return False

    return True

            

        # response = session.post('https://releases.footshop.com/api/payment/make/NTy2BYEBKNDGyVGQTp2M', cookies=cookies, headers=headers, json=json_data)









##############################################################################################################################################################################################################################################################################

    ###----------------------------------
    ###  3Ds Result                      |
    ###----------------------------------


cookies = {
    '_vsid': '1203a5b2-24c2-4e40-acbe-b611515b83c3',
    '_gcl_au': '1.1.1296509918.1652515468',
    '_fbp': 'fb.1.1652515467904.1676578708',
    '_ga': 'GA1.2.993097310.1652515468',
    '_gid': 'GA1.2.820386360.1653643165',
}

headers = {
    'authority': 'releases.footshop.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_vsid=1203a5b2-24c2-4e40-acbe-b611515b83c3; _gcl_au=1.1.1296509918.1652515468; _fbp=fb.1.1652515467904.1676578708; _ga=GA1.2.993097310.1652515468; _gid=GA1.2.820386360.1653643165',
    'origin': 'https://releases.footshop.com',
    'referer': 'https://releases.footshop.com/register/lzWuBIEBKNDGyVGQXOX7/Unisex/dc156a1c-dd98-11ec-8fc7-cee84d9682c5',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}

json_data = {
    'details': {
        'threeDSResult': 'eyJ0cmFuc1N0YXR1cyI6IlkiLCJhdXRob3Jpc2F0aW9uVG9rZW4iOiJBYjAyYjRjMCFCUUFCQWdDRTgraUJrdUhSZE5zVjE2amlxT0V6OVd3MjdQc283ajVUdVR6aUFJNVRxQ2s1TGRreEovbSs4OVVreFdtS1VOOFhNMXFneTVYVFhUTHBjNVBDSm1ZVzBEa3ovOFJYOVlVL1JmSm0zRXBBYUcvbmQrejNZUGxmWUttbGV0Z1lpb2RPM1pFU3BuTUY3RGw5NzBQdFgrbmVjSUM0V2ZHa3pneklKMTVtaTliZE5BQXRTUnV5OE1ta213a2R4ZjdWYmJJT044WHhxbUxjMThwZDZ6ekdZOUhhV0hnUFJ6bXA0cXhWU1V5ZXhtNUprQUx6SnJ2bDFiWi91VzdwYS9HUUxQT0IxRldiRXBTMStpMDJlZ3BaTFFhQVJoRXkvb3ZrcHA4ZjFrd1gvSi9RWXhCMUhqdlBpbWw0L2tIUy9OYTlNK0Y2R1Z0N3NLZ25Kb1crOEQ0d2k2aWFjWW1pSytaNksxR1A3ZS9pdjVseCtPMElNbWh5ajlaRVFTSDhWVm9TWjkybTdiWW8rL3haMnlJUW91aE1nRjRBWDdpSkloQnFWSEQrR210MWxlcWpuaGxabTVVWkhUV0tZd0ZsRU1TTUczR013R2x2ZWhPYUZBS3YzRWlWRjlCa3ZzVmdoVlExbExsZThDN0JWVGZHbkFRTEl3bkNDTStPdzhadmFFcGlKN2VJWTg0dXdrcllIaDRYQm1BK1cvUFZZQk11dlFSRWZhb05rZzgvcTlNTEFvL3pTWm5tRHlGc1lKRkd5aHAzNTcrc2tzY2pMbWZDbHpVVXZaRkVDY0hYTEo2c2w1SUlKbnJyRUVLOFhXS0RyTVZmWGFScGpLYm9XeDFucUJUVERSL2dqbHVqR2Zmc2F1b21VTlVXTldPY1JkU2xLRlB6a2QyRVR6c0dSVy90VEJEZXhlOXVsOEIrN0xKQ0VoWURCeVIzQUVwN0ltdGxlU0k2SWtORE1rUTFRMEZFTUVWRE5qRkRSREUwUVVKQ1JrUXlNVGhCTVRGQk5URTRRVUZGTkVNeU5USTVNRVpGT1RsQ04wTXpNRUpCTmtNeU9USkRORVpGUVVZaWZjV05UZ3kzRkhPNURHdEtoeHFVVzRNMkJ3SHZUSENlZFZmdFNxRHVZVk83ZExSQ3JUOElPMUp6YjBGem1EK204RGljZ2t5bGVJUmhHZW8vMFZQb29rbndFVUNBb3FDV2FQUmwzVDZVbnovbmpvR1E3TXNVTi9TSHFqSGdjcnJmbXlrQ1dseTZtOC9Vc2FBMHBTYzl5T2pzcUFsRnVpc05GZU9aYWQ2NlVaWWl6eUZ4ZjFqNlFCak05bmZlb3BEeFg1bnY5T2ZwNTJIdFdYS2ovYkcyMi9BVS9wbnZuNEdhYlNtQ3dvdVExSXk2ei9XeUdFdkZtdFZKUUpmbStOay9mSEVwenQ3K2w3VThLK1VDR0xsK0Y3MTFVMDg1WGhWMm04bUVXcmtGcG5MODU1dkhjakJNUVJSNldQSkRSSzZ4VWJ6L0FWSVlSWnFubUhZSnVmancydlpjYXIxczNkcFY3SjI3aWNmbk0xSGRFMCttQXJldnE5UldHc2xrZzdscUZ1VFRTdmVjT1lzZVhOeVlISVdLejVtVVVsR3hmdGtuM0t3eDZFUGcxK1lGOURDL0dIMGVMQllxOW96WTE4RWFzb09sZGdvWlMyYmc3b0tDV2dmMzhBZnhzRDh2bHo2djZuTmY0Wk96dDJackpzQ3QwVWt3cTBTblVqcDBtdUgxSGZzTnBGQTd6QkJ6REcvWTJUVTV2TEd6bXBZUStFbVE1RnM0S0MzVS90eXd2dFBCWndxWjZlbURabS90SjBFT3B6Ny9JWW9ua0gxNERyWXNJenpwWjJFN2gvMTAwdjk5NXo4d2RobkprN2VNL3IwZ2RJWmMyK05Eb0xXaUtPSlVnZ1lWdCtTVjZjRmZVOFR2RFE2L0JaWEZrcERTNW16TG04a1JuZWFhQ3NIVUdSRTBsOEdhV2xSNWVjMVJXOWYwck52S013NEVBUGh2SDAxeUNTSUhRZTN6NFBsemxhOW1NbmEySWVtc3JYdlI5dXpFZ3pQS3ZNWWUvYTh2NmhjTE92dG9vRTEyOFRPaWlySy9vTEdUOHczY2dVdXhtSVZIV05GOTRyaTZzN3BlLzA0ajhvOXNZMmlNemh4VUlXRlcwaXgyRG9yL0pReHhRN1NXamMrVXRtREpzNHpsOHcxQ0NDSkRYWXM1WjJ0ZVFuaWx4VlFuTFpmTGRsZjdDYTgrVDVnbmV5L2JPdHZwTHNuNlVqaUpRZG1WVG9na0ZkRmFsNG1xTXBEcmFUUldXS3RZcXhEdG1SemZsTnFaWkpNdzUrQ3VLVmRvSUpyaDVmSy8rSXBpeExtalNlZ2loMThVNTBqWFhGTWFtNmpoVUhoUWxnYWNyb0hjODVKRXA5YVVYQkN4bjBseE51VDJ0dHp1Z1FwTVpYZm40WUNiYTIyLzFWUHczOG9idVBEdmJoRU1BRTZOckZ4T3c1aVpFN0xFNE5sMTNTeTZ0MzRyOFlhWEtPYmp3aXJUWWtQSUtvTWEzWndOS0gybS94TlZsYkZkbEZNYlBIcXBGRnJhd2h3Vng3N1dGTnJuRzZOZnh3VzUvRGlGclJMSlNpZC9JYXZIMittNnVWV0NwaXRlTUlQYk93WHJwaHQ1enhmdjRKREdhODhLY0VWRTY1WXozR1ZhQkFtMlpSMnUra2puOXI5ZU4rMjlkYmlYWGc4NzFRWHFJaXlJY0hXNXp1LzByQm9SclpJbS82ajBZYVI2OHdOSjkvUFRSUlpaOXNhVk5BN2hiSUVNS2Zja3c4SWtiVUpFQ0QrL0ZSTDZtdGNDcEhOMWxYSkdJL3VXVlN5RW5vbklIQ3NhenU0RDUyMUdlaXJhdTVTTVRla3oxSEdLR05kTTNsZnAwZHdDS2YyczNNd2dpa1pVT0VZdk9HZ3E1VjZsSGVEMVpoNHlBMlNDdHJkNXRuM295V3BvU0c2YjNvZU0rS2NXUUxKSTBwblBzNWgxY2dIMEVTZVF2aXJSME5HY3dSSXFXdzlubEhvRWdNMWhSSTBBTkxnOHVFUDEzaWNoZDJUNUZ0WE5nVjBvMUx5YnROR05LZ0pIOTh3S2VHNjBGUm5KSXBjY3VoN3o2dUh6VG15RWMzVkZUUnEwKzF6WWRXRWxET0puR0NyR2VtdXY4Q3RDL3JnUHJVYzdxd0ZSeDczUHgxVUtCeXdvY05ud0ZSN1dONFNORVhjU01Ba1c1VUtmMDBhWCt1WmV2T3BuYWJURW5mSHMxaEdadnlMZEZyTSt6dlFCR1VxcUZRQnVyblo0VTFxTHdCR3VWTnZMNXlPR2NLQWgzNnlrRUtQVldvVllHMytaYVV6cy9vZWpEbjNJRFBDcEdmc29HeEgxT1FwdllPMFBQV2hDakVHTjFtcXducXNRblZBVEloYXByeFBxZ0hORVFjTFZFL0N5bzJEaC9GSzhwRGhVVnVFVHdrcXFDdk50cmVPdUxkbUJjY2tLeU9pdjBLVjRNczNIcWFrc0F0elpYbnd1TXFOdFRhUTBHWW1naXZDQmhzSGhwOUFIUjZ6NVVOS0Q4WG9QblB3enlJanhDVjJJSkpid29sUWgxVTVRa0FZaHc4VXJCczlUY0hMejltdkxjR3pUMURoc0RBaXJTQ0lNRmNhZHRCQkpON3YvMEU0NU9qNWp6SHp3ZFhkUGQrYUN1eHN1WXU0RWQySDMxS1lpNDVKTCtPOG9jaktmTWRxOFZESmdJN25XbU83K3F2UFo3RGMxazVuVXY1RGo5bk5iNjUrZWlKd0dRUjFtRTViSVdldWhabUpRb0xuS2lHL2djWkp3SUJtT2FQSEU2djhIZndRd1Z5MzNaak1TZ0J5MExkK0YwYm9Pa0RuTEl3d2JMMUp6c1hYNTEycjFMdHNSVEd4dkluNnBPRzdIOFB3RGU0MDVpRXdLeDBIdGdCOFNzcllWaG5MSUVHZEwyOW5oTTllU3lDVU9yTnQvUzZQUXE4YnpQWkZ1a3hzS0hLZS8yNXY4WjI4SXBJb1pSZ0RBUngyZG5sS3dGWWtWQ0ZnSnFBdHZxTStYNHF0bmpvQWUyUnEvVTNsZnZMT1U0ejk0QUJXWEJuUmRXTlB3U3pzenRWWE01b1dBZ2ExWnQ3ZVdhUVRYVGdWajVUZ2dWeDN4blkzbDduakprLytzOFhJcTNXU2o4djNuekcvWFhyTXFkL2N1ZUgxZmNhd3R5U2tlNDV3SE4xc2N2bWdiaVFXaGJZYWxQSTNnRTZYVEpKTHNrRXRTT1JoRzJjZE1MNjlDTExCVHNWZXN2Y05NUmF6elFJL0Z4ZGFNUUZhWEkxYWRnN1BORXBOZytWdG9oUmFTV3NoQ1BpRE8zT0Z1Q0ZMV3NuRHRKUEpyYXA4MDJhdDd2VEh2a2drUEI0b2YzRDgwcXg3NC9ncWk3WGFNOTdKOFhnVDM0TDJ3TVBTUWZEamx5MGlyclZLN2hPbm9iVmVNd2MwZmY0aXQzYzl1ZUdrVWdmMmp6VHdCSWZiTW5SaGppQVpKS1FIQjBWL1JDY1BYdDlua3JpR211THpPZVhZT3Y1OTFnYVkra2M5MUc5U1pZUVlUTEVBTUN3a0tsOXdocjJDSGQ0OGVRekFhVUFnNXVOMUpCdnVLTXBmWjNzWjJUWDQyaVFBSGVUVUdZUEhBSE96ZEMyWUVWYzk3SGJpR0hYcVVOSEJrV1BOQUpZTlhkZGxhSVRpREMwSHhlSTlZNDJ1eE1pQThxTld3aGpGUUJKeVppTjcyMm5ZcGRiWWFibXptVmpnS2tMZWo5blU5bTZzNkZpZG5WRzNWT3hONVJJUlE1WGZFdVk5c052SWhYeWxIaXlYd0xQb3ZVWDgzTXRRMzVUMExCdkZPWWdWb0dYZzFLbElEb0xsa3RQOTBlL1poamNUdExqcWtaK3RpOXpST0lNc1Vva1lOMjVyRGgvZzB4Q2xRS3o5cDc2OFVTM1E2Vk1LNG4zaTkya2YxR0NxbW1FaVBQajcvcllPeEd2K2FPLzhEYk11SVdIbXljYXFEZlg1Zkl0T3ZwQWJ5TXZXemRNSjhDMTBpTk1adStUVlFERXhvM0VWQmlmR24vSWVOOEluZ2d3RFg3aTVPY2xYeFMrb3lOd2VvNFJTVGUwa3FoM3RaamZoakc2Q2tkTzZlYjVMd21BNFl0ZEswSTVjSW9Wazl2b21jNDJrSHVwZkVOUEcySHpkQUJFTmVwNTF3clBYTkV3RStRamhFVzYwNjZHdGpoRVdqK0t5aWo4LzFrNVZnWkFFbmNsNTY3b2FRQzUrMmg2V1BVNEl2UW1aMnlTdVgvYUU2MStiV1FYdWltcFMvais4cUQvQUI3VDkxSzBuelFjQ05UWWxGUm41QmRkQ1NzYzV0SDNLdlFtRCtzZWh4MW02d1RnN09UK3JMU0xPdmRQS1AwUnFsS0VDOVl3NmNGUlNMenQvZHYyVHhKWFJKVWV6SjVnN2N4ZFBEZUx6OGpwVmJTM3ZlUXVNdjZGOUxpSzIrUGZYR2FhU0RrYUR4UERXZkRRZVQ3ZTc0dWdjYnYyM1pjWkliRG04VDZuSWpJVUhRYXQxK2JVZTlxLy9zaDNicWVZMUxWSVhzZG8vY3VuTysyb2k0RXdLaTBIL0ErbTYvb3c5RnZMVXJXdTRsOExTbmFCRTk5TjdobzArZ0VOMzRpK1NTZnhudzc3dU8ybGdDMWlXczJoMXFSK05ncUs4Qi9aSWlMTDdzaGk5M2xrZWo2QTVFcE5uY2ZxbGNkQXJMeWVSWEUvODBJMEVzeXRYeEkvYVZXbERIdjhxUWxaaVhPVUJSQmd2RWxqcEsvWkY2Sy9jV0lKK3cvZWVaNUhhYzRnZUtwWnVDeFBxL3dLZ0pJRTRBdXg2amVmRDA0VFFGdVBJbDFYY283Wm11NUtEeUp6SnJxb2RqQlUxOWpKVW8xTnVWVFY4SFpFRC9DMUpzS0l0ZUJrelVDRjNkU1RCR1hlb016MnlGS2ZqWmg3emdrZDB5WXZRYmlVL3pEVkE5M3h2QXJTS2lnb29pN0pYU0YwMzA5NTlrSEhiSzloYVN6c1RQTGZNZFZzb2pxNkl1TStVeDN4aEpld3BxdkxrT0tPczcwaVZSU2pNa0dRZWV1QjRMSW50NVdaNk9ndEY5QUFjczlaWlMzOXkvZnd1YnJUWXlwMVQ1Q3ZFdU1uejhla1NNM3ZQNlpNSFJSbkZxellOWVFCUzNOQVpjbVlRZkhIbHlIVGpyMW5JSzhWOUFUNVNxaFNrU0huTmpNcFNFRVRkS0IyalBVVWFVaVY5NlNUaExaa0FNMHFSR010YVIrV0IwSHpZdTZhdlZNWngrM3U3cmxXaUVTK0ZUdEI4V2xneGgwMXBma09rck4rM2hJUjJRZk9mWWFxR0tDdi80WWswZ3NHc1FZSHowNmpVRWQwYnFLQ25rRnhyNk9WaDRSc1lXYU9uS1R4WjV1anV6cExVN1hIYUo1VzVnU0JtL0YzUEptS0dTV3hzalYyazV1bVgxeGFGNnZIK21zdzRWRTZhekFqeWpuN0ltcm0vWGgvalArS1M0VlFCWGJYd25sK202R0N3WVZXbzg1enpkT3ROUjRpNnQ1b1FjSmllYVVuTjVUMTlGSHlCMVk0bWY3ZGo1ZmI2ZG13bVovN3owaFpLcUN6cjdBWHVDK2lHY29rU2FqSmIxbGlDT3JTZlJ4TERHODZ3Sy9wbGJDcTMzWTVjVUVSRHdGYXVWdW1ia0hoWnVVQmdOTVN0ckFtbm1rcTNQd3JKTlNLNHpjOVNHVHZqRUJnV2RYeTlGR3NhbkN5NlFpM25wd29tN3JwMER1RTFIZlhEa0NJMkw5L3l5VkZWN3dHcnJSZmxTclBDdm9VTXJUSk9vcmhzNUkrMEI5YU9kZnJKcUthTHV3SUJ4aE5UaUtGV3NtRzU4dzlyZ2pqRUVOY0o4NU1sb2cwVVdKWlN6aVN4cUlqWmlPOEVqL2svUHFKTk5WSW9TMGZRamF2VmF5cDltbmtSclhPa0x3V2Q1N2lSSzI1RlJEWEFUQU9qZ20wYkVVVDRreDQ1cDdCbWFSK1ZuVVlKVEhTZk9VcitBeDEyazl2Z0IwRVgwTFloL1dUTHc1Rit4dGFPbmRyd1ZSVm5JVUpJcWxlWmlGSm5YZ0l3M002ZVJ4SHF3WmprMmRUKzhNNGZ6dmNHcGVYRDFncnNlV2VpWS93eHoyU0tjMFhCclYxWUsxWWk3aHNuczVKRDNmQUVvb0NNK0d4UDllWDdsN1ZJRGhXaW42NmNLSzUzSnJ0cnZkR1V2azZQQ3hXQWVVWERZL2dxYmJ1aEJuamY1Um15anRBNzIzbmIwMCt6R0piM3FvUXNvQXFjZ29vVFNiRFd1dkFoazJiSEZ0dWtaY3RsWmJ1VVNud09EMFc1elg0dDF3bXFZZ1c3V1JxbjVoNVh6ZFdpZHRXTy8zT3ZVa0tjbnN3TW0zNTJobGxtcnUzTUt6YTNUNWtxd3gyUUs2bzlnQ1o2SlA1YTF5c2NHTFc2RXVHNnVvNFI5UUpEa1pqRUtaVzhyT3hKZ0RIVXBpVHoyWXRrNGx3K05SbEo0UnVleWpTN2M1M0tOREFjbUxKalJwdFN5T1luZVI2TVFxcmo1MXl1d3N1aFl3UTduQVp2dldYQitzaWNmV3dkQnJNeVc3Y29QSE40WGxMNU10Zm95VGFkM0U0bGZ3ZENPcXg5aEFtTUFhSG4vL2U3TGRFb2xLRlF0Z282OWlZeEVSR29pNktmVmhNQkt6TDlYK1VVZUkzb3JUZXJIOFhacllQM0ZnZDJPZUdVUlRVUGlkZG1XaWFDcjRFRUdDVzJqRDVvaXFaemZRUXA4NHVhU2QwK2E5Z1gxdnNOdE8zR3JLWlorU05uQlY0VUFVR0luY2V0dC9JSG9kZk10bGJtc0NEbFpRMnVMbmRoVFRoS295YTZWRlVWaHFDMzd5SE1kOFFsQkFtbFA0bEFnYXFrNkRaUi9vOHRvWWZHcDlIWkRSQWtURGpuUmhZSDFtMWxpZVZDb2p6YTQ4dk5xUEVCcHNwTjh5OXNnK2lxRGUzMDlZZ3ZOaVFZRHNNMzQyc2tjdmoxdlNIcXpaNjluRC8rK1FibVdlUlRkQnFacGxDMXFtaitTRjBidHhLMzhqaTFYSGwrU1hiTnUwN3JvNXNNSXFqOWpoZ1loSFhGWURxNkJPS1hpdTJwQ2NuSk83R0VUeXRuNnJleWJWN1dRUThORjBGWmlBZVhBVW04OC9yaDQxZHZkRUpiZWRsMWJCL0VyVVlDdE94T2REWXorYjRIdnBOVUZtYXlYTjA5NVpobHJPUkZTM0gramYrQUpTUDdPcHNuK0EydnhIRGthd1ZCVUFqTmgzNzRoenVPaFJzV0lFbEJCOXQ0MURkOGNVcjNoRHZ2YlUrTklYTDJCT3JBVlAxQXhLMmk1YnBIUTR4SHMyTlcxRERmR0hEY1JxUTdXK3M2a283Q0JnZWNYVXVHWjVWZHkifQ==',
    },
}

response = session.post('https://releases.footshop.com/api/payment/make/NTy2BYEBKNDGyVGQTp2M', cookies=cookies, headers=headers, json=json_data)
















    ###----------------------------------
    ###  Finishing Entry                 |
    ###----------------------------------



headers = {
    'authority': 'releases.footshop.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_vsid=1203a5b2-24c2-4e40-acbe-b611515b83c3; _gcl_au=1.1.1296509918.1652515468; _fbp=fb.1.1652515467904.1676578708; _ga=GA1.2.993097310.1652515468; _gid=GA1.2.820386360.1653643165',
    'referer': 'https://releases.footshop.com/register/lzWuBIEBKNDGyVGQXOX7/Unisex/dc156a1c-dd98-11ec-8fc7-cee84d9682c5',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}

response = session.get('https://releases.footshop.com/registration/finish/NTy2BYEBKNDGyVGQTp2M/guest/1653681600', cookies=cookies, headers=headers)

    