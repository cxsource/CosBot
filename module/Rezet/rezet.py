"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] rezet.py                                          """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 27/05/2022 10:18:54                                     """
"""   Updated: 12/07/2022 02:49:45                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

# import requests

# headers = {
#     'Host': 'master-7rqtwti-2sungu3anaqlq.eu-4.platformsh.site',
#     'accept': '*/*',
#     'access-control-request-method': 'POST',
#     'access-control-request-headers': 'content-type',
#     'origin': 'https://rezetstore.dk',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://rezetstore.dk/',
#     'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
# }

# response = requests.options('https://master-7rqtwti-2sungu3anaqlq.eu-4.platformsh.site/api/da/wr/register', headers=headers)

import requests
import random
from threading import Thread
from ultilities.ThreadManager import *
from ultilities.DelayManager import *
from ultilities.createsession import getsession
from ultilities.CaptchaManager import *
from ultilities.logger import *
from ultilities.CSVManager import getCsvInfo
from ultilities.ProxyManager import *
from ultilities.DiscordRPC import updateRPC
from ultilities.WebhookManager import *
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed

def RezetEntry(profiles, proxy):

    session = getsession(proxy)

    headers = {
        'authority': 'master-7rqtwti-2sungu3anaqlq.eu-4.platformsh.site',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://rezetstore.dk',
        'referer': 'https://rezetstore.dk/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }

    json_data = {
        'captcha': 'P0_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiazVTbFhld0E5dFd5V05kbkdxNmVDYWNwU2tlOVljeVdQV3BCTEdZbVFTeW1qWk9DVmw0VDNIdFBHU3YyNlVaWjNHenpXMG5FNklLdU9jb1BRTnllRVBFVTdIVmNpUy83YnRJbHJtU1c3WTZPaTFFclM0b0xCU2xmR2NYblNsRU1uMlFIb1Q0ekdxR2EyeHJlUGY0RlNpcHNFd0JWa2hpbzEzWWZTNFd3VlF5SWRqS0tpUXhkZVpNQy9LSFk1Uk1raW9ycE9raHZjMFdJUlprU0VmTDB6S1YxNW5iU1d6RThOUmtBanRnbTVhSXN3SmZPOXRUTmtOU1lrNW14d1UwbFM0d3ZOWSt6SHhLVmdlRkhuNzJaRW9xS1lKWlBhZ2hLNmNYaWtTWm1jS1k1V2E2U1pkWmhocjZrVitidXYwRDBON0RnMHozZkt3Z1R0My9kN20wUWNtdVk2ZVo2YVUxamtzZEN1RmlhdkVmQ2pUV2Uxa1EyYXhCWXFvTVJRd1lycUtMbkFua0FDaWh6c2ZpdkJPdmVwRVkyR1FqdHgyU0hpTjNkZU10WXJiQy9nZTNna3ljZjZzK2paWGdnUkhrYjRNLzJaR0xvOU9MQ0tydGM4blAyTm8zR2Qyd2RkSlQ0MFhFZHZLdlBvaHRxc2VGckhpenJzNXN2eHZOdzIvMHk0N2NpOFd5YldSczJOZ1ZUQTQ0NUZUWkJMc3Iwc29oRWhmSzlkSlJIQWdaYkltMnE2dzBjc0s0Qk9vM3BWQi9rVmhlV2I3NjFLNVlXWDlPbnIxM013VW5seXBLbVRqS1RsU1VWK3BZWmVFZHRub1ZPcFpnTUhldDVXMTBOZTBNQnB2Z1Q4d0swSDZxQVFEeVNFSE9TMjdUQ0JTVTBueW9KTTVNSXozRlRTWTliTTdkazZxNVhBRFp0dFhuSXRFUjBVcnRyWkNSZ2J4L1JwZmZYamZPWm5nd3I4V2d5UmhBdzAvUXBlb2p0bjQyU0pGWm9VY1JRZGQ4OEtpai9PM1A5RVpQbzQxZDlpRS9vb0FvMVBwcHpMcjhuZ2hMeXVhcDBKaGx2NVdDOUMxZ2Frc3B2dGM4TFNjdGc4S2RXTS9ocE5MVW81dEMydEIzekRnblE5ZUJYRUxEUDVPOGN6NEVuRHBncE1iK3hlK05rdWY2cFpuR3hhaUdDNTFMdjhWUE9yYyt2T0JNeE1QY1BqalNxaytOYTBPNklGR1VGam9RN1FJSVl3T3BKcGVPNzE5Zk9JYm4vb2I3dmlDbjhJM0VwT3VLSjV6amVkM2ZwTlVZZTBjS0lvZTdnUzRPcTF5UTU1S3dwcmRKWWR0M0ZqaXlEak9mTmR4TW9sTnY5TmRRU21Ydkl6S1dodWpEZjRvbHN4ck1UVmliT1RoMXN2NHNpdHlKZEVhcmJPRU5ka3ZJWk01YzFLVm9xTmlXcmpFV0NEdi9lSms2dnpQZDQxRWRjNmRLZVZsN09HSVdZaTVUek9kd3hMTVNpREJXSHJEbTZ1RUEraVo1ZzAwcHJycHNSUm10Um56RDU2RnpjbGxMRW1mMTZtY00vNXpKb1NZT3hPOVcwWlE5UEZCMU5POW8ydnRId2NPeHNGTmtxdDhmckJpVzVObkVkYTFIQWVJdFhiYStRQW5XOG4wVndiWll4RHVxS0g1MENFNUxGN2ZkYytscWhIYTRWUzNIdGF6ZjM2NmE2MTNJd05jaG5EdmU5TTNsSFBrSnplOXlGUC9JYk5jS3IrVG5aWGNQc0dTbjNIVVVuMkVoUkNlVkFrTmZtcTZIUVlTZEJPd0l4SnY3OXY2clpQNVIwM013YkVxekgzcUVncGFrOUh3YUNhVXM4T2dnODBYY1l5SlFsNk9RblBkWDlmYlo4NUFweHF1NUpIUlV1cDZGdDhEb0dxTmFkazRxem9qZDBQNFJPaVI4ZTFxSXFnTGdJRzQyc25MaHVQVVRWclhuQjdnb2Q3ZXFuSGJJbHVKcFJCSFBtRWxDcVlTdU5Bc1ljYWVqVkNReU9QOEdHSkE1aFd0SDR5RTAwZE5tNlIyUEJ5UW9COVFicXBKMHRwNDlWT2U2RXVnLzhkU0NzUjYwY0tUaCtQQzB3eWhaOVlXVkZ6UjFhaTdNM2tsd3YvM3JodzFscVhXdEIvZU93YXFqMHhJOEdIUWYwUTlJaGVlWDlNWkhDbjlXQWs0U2x1eWlzeDI0K2NWaFZ0aTVFR05uWU5TL25jZnVOa29QVldmVkIyVHJ1amtVVG1UVVp6ZTluRTBISEpSTmNQS3A0OVIrRXRTdUc3bGlwUStNRWR6UVZXWTIxbzZrU0hOc0padEpwRjJ2Y2Y2bGhLb0lOL2tnaHAyaGJCZTU4bGFBZ3N1U3VjUEZZTmFKelA5bEN6MjNlUGltcTd4VU90TXdQTll3UGszZFJRaXRXakxxSFhVejZ5TWtQTk9XOCtGWkU2OVEvd2RFQit1eCt5czNGYmRWWG45QVM5RjRybVpyMExWUU1mK1FEbzFQdFArcWUrZ3ZjVldKOFExZXZZQ1MrY09PSlZVNTVhcDdwd2t3UjFYb3JzYVFoTDB6bnJpV1o2YVZNNTVhV29CTEZPS0hmZTBZTGZ2aHdLbXhEUmpsZHBtbHdPSCtMZSt0Z1h6ZmVVL2lVcXNqUWdkek1iWHQrczNxT1A0RHpFa2pXTEc4VFA1ZHYrQ01iNzVMNCtja0dsaGxJNE1IUG1WNmRHV05NRlVIUUttN0lMODc2ajdpbHMwMkplUVN6KzRySUZwSkI1MmdKTWFKWkErdmZOUlJkZi8zakNoalVESWdTRjFKWnBibE1ILy9zdlNleUJPNld4dFF3QVJKbjdpZU9jRWNuc0lHbVh1VEQrYVhDR2FMZC8rbG9kdWZMNkgyRElEVzJpNFZ1dmpGOE9OYW9QZlE3Z090eUJNbm9oQUlIUnVrSE8yNkJmcUI4bFRFTUl4M25rV2dJWTR5Um5LQlFSOTNQQThQcE40UGFJVEdTKy9WcEhiT01JVnJUcE5jbmVPbGxNSm1ENzNSRGZFN0p0Q3lkdDZNdTZtL3pWMkNKc1lNVmF0QkRueVM3T0dGRzVlZExFOFJRTm5TbE5jaXJ6MHpTUTFzR1VJMTE5aXZudndFdGNpYXp5akJTa2F1dmdvdzJ6Y242WHY2alByZytJVEsvZ1ZSUVd0L0JnSUdoalRQUXA1SzU1ZEZhbzRoS3hRNEo1dmJRaGI5Z0g4bjlEVTRrQll4Qm1WaHBqcHdQVUxuRUFnaFErRjY2S2x3NFJzSnhydng3QWFxQ0lHMVl2eVVQVzMwSldldXAwaWpYQWR5cDdKb1JqeUs2bXBOY1hnUi93VUhxYUg4bW8zbXQ2MklqdURUNEJKMTZRdGY2dUJXcHdDQW5ud3NyMEV2UHZMKy9wU2duWjU0Nk9KVXNWQ21zRUlLekY3K0pYZnN4azM4MmlwWkIyOEJYdzY5OVR1Z3dCSHJCLzZhWUlTemJLalhFbSswcHBiMWd2d2l4Q3Exem8vWHEzaVliTk5aQTVMSUVXWTRPdWREWXVMRUlWbXh3dEJTMjVSY2Q2TVVNZW0yNTl6RzdRb0lMcFZMMms3VVY5NTQ5YWFjTFlZdkhRNG9xQlNkV1owL1BHSkFaTXdXRlNPbkVhQS9BU3B3cEQ4TDFXclNWa1YrMVA2QzYwVnUzMVNjdW96aHlVeks2VTh2QjVQTzljTzh3V2ZTa0RuSSt1VkZuc285aTZVcEVHWTVJaHJyMDIvY21mMjIzdDRzR1NPakxOVU92TkM3QUlUblhNL05Ua0NlMFZEVTVORVdUbEY3K3JESUtEUk1rNElQUnQ1QkFWZElET0VQekwzUGxONWZzZ3FLQzhzRzZHc2swSXFCUEwyS1FSMmdkUkgwdHNibE92TnNkWXVsVWtpVUQ3SVpmTlVjeUxVeDBNUERqbnV6eXFVMlNzSEpWN1V0NUJnWExmd2trYXYrYzNPMlEvekRCc0k2bUZRWEE1cW1Jai9JZW12d0hlQWhUUDFqVUlMWWpNN2NMQVpoODRVMlFWNUlwaGwwbTA5dHduQWR6SjlTMFBJVFZDdDJyejdKN1ZGQzRobkpDbUZ6Y0dyMWxjSFM2eTBPQXd6WCswUU9GSk9IMVhIYm1hT0plaWM3YUREYWpidnR1Q3lQVFhHSnduc09hcFVOTVFsYXdMR3NXczc1dTI0ZStBbXNLUVJoS3VEVzFxMzNxRjNqR1NpZWV1SG5mRGg5ckxrMTZpTEVzbmFJbFNhSXpJeGtDZFJtaDlSZTZPYjVCWFdCUUVsVjFNWm4xSnlIeVAxL0N3YkRuaC91cWlFUmRhTEowRGFyRTlLbWRTMDZMc0E3UVAwUTR0NUxBZEcwWmRndkU3eXg3S29WMGFOL3hjS2Jvcy9KSzIzQUtBM1ZCak9GN2JhczZhY3ppNmd3REJqR3ZKYnhUalFBa2NEeEJzK1R2SEVrSGl1eXloY2E2bzZwWUJXOFhRNWRzWFl2Wk4vdGkyNU1yenl0M2lOdjE0c28ybXZ6U2ZaTjRSa1dmL0JaaTUrdHk0WWRNUHVPN2lXUzBEbytSakRENGZVOENnVElZZ1VmZ0tKYkZhYnhXVEZWYitxUEJTU21sQ0gyU21ZVG5ZRFd1STYvUk9nVGlQQUc5Mkp6dVFiLzFvNHVyaGl4Q2dnenNrVVN3R3dqUk9zM0x1Tm1HVnBmNEpidzRmUUhRc1ZaNVNobUVOM25zOVEra25PWU9LU1lUaVF4WXhjS29xR21YWUZRWWxITDBDeWFpNTNmWVUvRGEvekdXSnhBempadGZieDR4d0crLzhadDlwV2w1cm9sSnFZc0NNOFVNa3NOaEI3QW5rMVo3a01hWkRkTDdOM3dyeEhQUVRERUxrWlprTCsrWFMvVGZXZEJJb25LVlk5Wll3Yjd1cVNGa1JyeVQvQ1Q5WTQ1WXliRUdQVjJyeDNVR3crVTM2WCtXbkVpSVVDc0tvbFhzRzgwdmJNeHhYV0pHUXJQUTVZQVRkL0tCUmFheEFjN2JGZG9vMmhmZU9CTjg1VTN1S1lydEFERXFENVZtclNkN2lWODNQaHFndEd2a3dtRk00V05acis5aFZ5QjZ0eUdSS0I4ZmpKQkM0OUp3b0V3SlNUaGh2dHlxeldVT1JhNGRhMzdxOTBnY2FXb2hGNGo2cHdHWWhXa0JYN0pnN2I0dERacVNJdEZMWTVYR1NkeGlWaU95aUUxN3lSdEpId1hUSFJGUG5NamQyeVlaVkpFYXlLa1VSZVY2cHgxV042VExBQU9pY0x6cFB4YXliNzRIVFk0Mkh0enlrdGtldG52RnJDQ2pwWlBlM2ZSQWw2OERJeFdOYVkzemVnQkNHQUp0T2xXTlpTclJkcEk2MXhObWwybDBFc3BORm5lNFExRTNWWm95aEJoR0doQWNabHRhc2lNWDVMT3FzK2psdWNEZS9hK2M5QkdwUFdWZnBpSks4NktIMjNiZVB3bzhuYUZ2cHcyciIsImV4cCI6MTY1MzYzOTg3Mywic2hhcmRfaWQiOjgyMDc4NjA4NiwicGQiOjB9.SjrSJcVGOmMc1iSpKJehGdN9QnXwiI7H_fRppwPL8YY',
        'email': profiles['email'],
        'sdk': '2219026',
        'sku': '195481078478',
        'size': '42',
        'phone': profiles['phone'],
        'country': 'DK',
        'ip': '195.123.106.198',
    }

    response = session.post('https://master-7rqtwti-2sungu3anaqlq.eu-4.platformsh.site/api/da/wr/register', headers=headers, json=json_data)

    if response.status_code == 200:
        print("success")
    else:
        print(response.status_code)


def rezet_main():

    setTitle("Running Rezet")
    
    rows_list = getCsvInfo("Rezet")
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
            
            result = RezetEntry(row, chosen_proxy, tasknumber)
            # print(row)
            
            if result == 0:
                success_webhook("Rezet", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                logger("Webhook sent!", "Rezet", "success", tasknumber=tasknumber)
                successTasks +=1
                               
            else:
                if row in rows_list:
                    tasksFailed.append(row)
                    # print(tasksFailed)
                failed_webhook("Rezet", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                logger("Webhook Error sent!", "Rezet", "error", tasknumber=tasknumber)
                failedTasks +=1

            resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
            setTitle(f"Running Rezet - {resultTracker}")
                
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
                
                result = RezetEntry(newrow, chosen_proxy, tasknumber)
                # print(row)
                
                if result == 0:
                    success_webhook("Rezet", "None", "Product", newrow['email'], threads, maxDelay, chosen_proxy, newrow['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                    logger("Webhook sent!", "Rezet", "success", tasknumber=tasknumber)
                    successTasks +=1
                                
                else:
                    failed_webhook("Rezet", "None", "Product", newrow['email'], threads, maxDelay, chosen_proxy, newrow['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                    logger("Webhook Error sent!", "Rezet", "error", tasknumber=tasknumber)
                    failedTasks +=1

                resultTracker = f"Success: {successTasks} / Failed: {failedTasks}"
                setTitle(f"Running Rezet - {resultTracker}")
                    
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
                        RezetEntry, 
                        row, 
                        chosen_proxy, 
                        tasknumber
                        )
                    tasksResult.append(tasks)
                    index +=1

                for task in as_completed(tasksResult):

                    results = task.result()
                    
                    if results == 0:
                        success_webhook("Rezet", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                        logger("Webhook sent!", "Rezet", "success", tasknumber=tasknumber)
                        successTasks +=1
                    else:
                        failed_webhook("Rezet", "None", "Product", row['email'], threads, maxDelay, chosen_proxy, row['link'], "https://media.discordapp.net/attachments/812303141114478593/824408440172183572/Bildschirmfoto_2021-03-24_um_23.24.25.png")
                        logger("Webhook Error sent!", "Rezet", "error", tasknumber=tasknumber)
                        failedTasks +=1
                        
                    resultTracker = f"success: {successTasks} / failed: {failedTasks}"
                    setTitle(f"Running Rezet - {resultTracker}")
                    
    logger("Finished Tasks", "Rezet", "info", tasknumber="DONE")


    