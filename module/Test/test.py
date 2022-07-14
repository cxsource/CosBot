# # import requests 
# # from bs4 import BeautifulSoup


# # res = requests.get("https://de.afew-store.com/products/nike-dunk-low-retro-white-black-white")
# # print(res.status_code)
# # soup = BeautifulSoup(res.text, 'html.parser')
# # product_name = soup.find_all('title')[0]
# # title = product_name.text
# # split_title = title.split('|')
# # name = split_title[0]
# # print(name)
# # # res = requests.get("https://de.afew-store.com/products/air-jordan-5-retro-se-regal-pink-ghost-copa")
# # # print(res.status_code)
# # # soup = BeautifulSoup(res.text, 'html.parser')
# # # product_name = soup.find_all('a', {'class': 'product-card'})
# # # for elt in product_name:
# # #     if "raffle" in str(elt).lower():
# # #         name = str(elt).split('<p class="card-title">')[1].split('</p>')[0]
# # #         print(name)


# # # soup = BeautifulSoup(r.text, 'html.parser')
# # # authenticity_token = soup.find("input", {"name": 'authenticity_token'})["value"]
# # # action = soup.find("form", {"class": 'edit_checkout'})["action"]
# # # soup.find_all('a', {'class': 'product-card'})

# # import helheim

# # helheim.auth("b7e34971-4093-4a76-898e-c7c3f3ba7cf3")
# # print(helheim.getBalance())

# # import questionary

# # questions = [
# #   {
# #     "type": "confirm",
# #     "name": "first",
# #     "message": "Would you like the next question?",
# #     "default": True,
# #   },
# #   {
# #     "type": "select",
# #     "name": "second",
# #     "message": "Select item",
# #     "choices": ["item1", "item2", "item3"],
# #   },
# # ]

# # questionary.prompt(questions)
# import csv
# from importlib.metadata import files
# from imap_tools import MailBox, A
# from bs4 import BeautifulSoup

# def afew_scraper():

    
#         email = "sneakercd9@gmail.com"
#         password = "Sneaker1998"
#         sender = "noreply@afew-store.com"
#         links_to_find = "https://www.paypal.com/cgi-bin"

#         if "gmail.com" in email:
#             imap_server = "imap.gmail.com"
#         elif "outlook" in email:
#             imap_server = "outlook.office365.com"
#         else:
#             print("We dont support others. Please open a ticket and ask for it!")

#         with MailBox(imap_server).login(email, password, 'INBOX') as mailbox:
#             list_links = []
#             for msg in mailbox.fetch(A(from_=sender, seen=False), mark_seen=False):
#                 body = msg.html ## wandelt die nachrichten es in html um 
#                 soup = BeautifulSoup(body, 'html.parser')
#                 urls = soup.find_all('a')
#                 for url in urls:
#                     links = url.attrs['href']
#                     # print(links)
#                     if links_to_find in links:
#                         # print(links)
#                         list_links.append(links)
                        
#                         print(list_links)
#                         # savetocsv(list_links)

# def savetocsv(links):
    
#     with open(f'afew_scraper.csv', 'w') as f: ##tools/link_scrapper/Afew/
#         writer = csv.writer(f)
#         headers = ['links']
#         writer.writerow(headers)
#         for link in links:
#             writer.writerow(link)


# afew_scraper()



#######################################################

# def paypal_confirmer():
    
#     ## open paypal login
#     driver = setup_paypal_login()
#     ## getting the confirmer csv
#     row_list = get_confirmer_info("Afew")
#     # row_list = []
#     # with open(f"tools/Confirmer/Confirmer/afew-link-2022-05-11.csv", "r") as file:
#     #     csv_reader = csv.DictReader(file)
#     #     for row in csv_reader:
#     #         row_list.append(row)
#             # print(row_list)
#     ## open the links 
    
#     for task in row_list:
#         links = task['links']
#         driver.get(links)
#         time.sleep(4)
#         submit_payment = driver.find_element_by_id("payment-submit-btn")
#         time.sleep(1)
#         submit_payment.click()
#         time.sleep(3)
#         print("Success")
        

# #  def get_confirmer_info(moduleName):
# #     rowList = []
# #     csv_name = choose_toolscsv(moduleName)
# #     with open(f'tools/Confirmer/{moduleName}/{csv_name}', 'r') as csvfile:
# #         reader = csv.DictReader(csvfile)
# #         for row in reader:
# #             rowList.append(row)
# #     return rowList



from datetime import date
from datetime import datetime
t = datetime.now().strftime("%H:%M:%S:%f")[:-10]
time = date.today()
print(time, t)


 # with ThreadPoolExecutor(max_workers=5) as executor:
    #     tasknumber = f"{counter}/{taskTotal}"
        
    #     updateRPC("Destroying Naked ...")

    #     chosen_proxy = random.choice(proxyList)
    #     # print(chosen_Proxy)
    #     proxyList.remove(chosen_proxy)

    #     for rows in rows_list:
        
    #         executor.submit(
    #             NakedEntry,
    #             rows,
    #             chosen_proxy,
    #             tasknumber
    #             )
        