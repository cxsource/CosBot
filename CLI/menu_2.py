"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] main_cli.py                                       """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 29/04/2022 14:01:25                                     """
"""   Updated: 12/07/2022 01:53:40                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import os
import ctypes
import questionary
from questionary import Style
from rich.console import Console
from license.auth import auth
from license.auth import getusername
from module.Afew.afewtest import afew_main1
from ultilities.DiscordRPC import updateRPC
from module.EmailScraper.email_scraper import *
from module.EmailConfirmer.email_confirmer import *
from module.Afew.afew import afew_main
from module.BSTN.bstn_accountgen import bstn_gen_main
from module.BSTN.bstn import bstn_main
from module.Naked.naked import naked_main
from module.Naked.naked_accountgen import naked_account_gen, naked_gen_main
from module.SVD.svd import svd_main
os.system("")



class colors:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'
    BEIGE  = '\33[36m'
    GREY    = '\33[90m'
    DARK_GREY = "\033[1;30m"
    BROWN = "\033[38;5;215m" #214
    CBLUE = "\033[38;5;81m" #117
    CGREY = "\033[1;38;5;246m"
    CGREEN = "\033[38;5;70m"

class colors1:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def getVersion():
	version = "0.0.1"
	return version
	
console = Console()

def setTitle(title):
	if (os.name == "nt"):
		ctypes.windll.kernel32.SetConsoleTitleW(title)
	else:
		print(f"\33]0;{title}\a", end='', flush=True)


def clearConsole():
	if (os.name == "nt"):
		os.system("cls")
	else:
		os.system("clear")


def printHeader():
	# ## big design 
	# banners_1 = [
	# 	"   _____                    _      _         ____          _    ",
	# 	"  / ____|                  | |    (_)       |  _ \        | |   ",
	# 	" | |      ___   ___  _ __  | |__   _ __  __ | |_) |  ___  | |_  ",
	# 	" | |     / _ \ / __|| '_ \ | '_ \ | |\ \/ / |  _ <  / _ \ | __| ",
	# 	" | |____| (_) |\__ \| |_) || | | || | >  <  | |_) || (_) || |_  ",
	# 	"  \_____|\___/ |___/| .__/ |_| |_||_|/_/\_\ |____/  \___/  \__| ",
	# 	"                    | |                                         ",
	# 	"                    |_|                                         "
	# ]

    # ## slat design
	# banners_2 = [
	# 	"   ______                     __     _          ____          __   ",
	# 	"  / ____/____   _____ ____   / /_   (_)_  __   / __ ) ____   / /_  ",
	# 	" / /    / __ \ / ___// __ \ / __ \ / /| |/_/  / __  |/ __ \ / __/  ",
	# 	"/ /___ / /_/ /(__  )/ /_/ // / / // /_>  <   / /_/ // /_/ // /_    ",
	# 	"\____/ \____//____// .___//_/ /_//_//_/|_|  /_____/ \____/ \__/    ",
	# 	"                  /_/                                              ", 
	# ]
	
	## standard design
	banners = [
		"       ____                    _      _         ____          _    ",
		"      / ___| ___   ___  _ __  | |__  (_)__  __ | __ )   ___  | |_  ",
		"     | |    / _ \ / __|| '_ \ | '_ \ | |\ \/ / |  _ \  / _ \ | __| ",
		"     | |___| (_) |\__ \| |_) || | | || | >  <  | |_) || (_) || |_  ",
		"      \____|\___/ |___/| .__/ |_| |_||_|/_/\_\ |____/  \___/  \__| ",
		"                       |_|                                         "
	]
	
	width = os.get_terminal_size().columns
	
	for line in banners:
		lineFormat = f"{colors.CYAN}{line}{colors.RESET}"
		print(lineFormat.center(width))

	print()
	print(f"{colors.GREY}    [ Version: Beta - {getVersion()} ]{colors.RESET}".center(width))
	# print(f"{colors.CYAN}      ———————————————————————————————————————————————\n{colors.RESET}".center(width))
	print(f"{colors.CYAN}      ------------------------------------------------\n{colors.RESET}".center(width))
    # print(f"{colors.CYAN}      ————————————————\n{colors.RESET}".center(width))

def menu():

    width = os.get_terminal_size().columns

    print(f"{colors.BROWN}Which site should we destroy this time?\n                             ")
	
    print(f"{colors.GREY} 0. Tools                           ")
    print(f"{colors.CBLUE} 1. Afew                                             11. SVD {colors.CGREY}(TESTING){colors.RESET}")
    print(f"{colors.CBLUE} 2. Backdoor {colors.CGREY}(IN DEVELOPMENT)")
    print(f"{colors.CBLUE} 3. BSTN")
    print(f"{colors.CBLUE} 4. Googleform {colors.CGREY}(IN DEVELOPMENT){colors.RESET}")
    print(f"{colors.CBLUE} 5. Flatspot {colors.CGREY}(IN DEVELOPMENT){colors.RESET}")
    print(f"{colors.CBLUE} 6. Footshop {colors.CGREY}(IN DEVELOPMENT){colors.RESET}")
    print(f"{colors.CBLUE} 7. Mesh {colors.CGREY}(IN DEVELOPMENT){colors.RESET}")
    print(f"{colors.CBLUE} 8. Naked")
    print(f"{colors.CBLUE} 9. Rezet {colors.CGREY}(IN DEVELOPMENT){colors.RESET}")
    print(f"{colors.CBLUE}10. Woodwood")
    print(f"{colors.RED}X. EXIT\n{colors.RESET}")
    
    # print("Enter Selection: ")
    option = int(input("Enter Selection: "))
    return option
    

def CLI():

	printHeader()
	auth(getVersion())
	clearConsole()
	
	updateRPC("Starting the beast ...")
	
	printHeader()

	width = os.get_terminal_size().columns
	
	print(f"Welcome back {getusername()}, Ready to destroy ? \n".center(width))
	
	user_choice = menu()

	#################################################################################################################

	if user_choice == 0:
		clearConsole()
		printHeader()
		mode = questionary.select(
        "Which module do you want to start?",
        choices=[
			"Email Scraper",
			"Email Confirmer"
			]
    	).ask()
		
		if mode == "Email Scraper":
			scraper = questionary.select(
				"Which site do you want to scrape?",
				choices=[
					"Afew - Scraper",
					"BSTN - Scraper"
					
				]
			).ask()

			if scraper == "Afew - Scraper":
				afew_scraper()
				endTask = questionary.confirm(
					"Do you want to go back to the menu?"
				).ask()
				if endTask == True: 
					CLI()
			elif scraper == "BSTN - Scraper":
				bstn_scraper()
				endTask = questionary.confirm(
					"Do you want to go back to the menu?"
				).ask()
				if endTask == True: 
					CLI()
					
		if mode == "Email Confirmer":
			confirmer = questionary.select(
				"Which site do you want to scrape?",
				choices=[
					"Afew - Confirmer",
					"BSTN - Confirmer"
					
				]
			).ask()

			if confirmer == "Afew - Confirmer":
				paypal_confirmer()
				endTask = questionary.confirm(
					"Do you want to go back to the menu?"
				).ask()
				if endTask == True: 
					CLI()
					
			elif confirmer == "BSTN - Confirmer":
				bstn_confirmer()
				endTask = questionary.confirm(
					"Do you want to go back to the menu?"
				).ask()
				if endTask == True: 
					CLI()
			
	#################################################################################################################
		
	if user_choice == 1:
		clearConsole()
		printHeader()
		afew_main1()
		# afew_main()
		endTask = questionary.confirm(
			"Do you want to go back to the menu?"
		).ask()
		if endTask == True: 
			CLI()

	#################################################################################################################

	if user_choice == 3:
		clearConsole()
		printHeader()
		mode = questionary.select(
        "Which module do you want to start?",
        choices=[
			"BSTN - Account Generator",
			"BSTN - Entry"
			]
    	).ask()

		if mode == "BSTN - Account Generator":
			bstn_gen_main()
			endTask = questionary.confirm(
			"Do you want to go back to the menu?"
			).ask()
			if endTask == True: 
				CLI()

		if mode == "BSTN - Entry":
			bstn_main()
			endTask = questionary.confirm(
			"Do you want to go back to the menu?"
			).ask()
			if endTask == True: 
				CLI()
			

	#################################################################################################################

	if user_choice == 8:
		clearConsole()
		printHeader()
		mode = questionary.select(
        "Which module do you want to start?",
        choices=[
			"Naked - Account Generator",
			"Naked - Entry"
			]
    	).ask()

		if mode == "Naked - Entry":
			naked_main()
			endTask = questionary.confirm(
			"Do you want to go back to the menu?"
			).ask()
			if endTask == True: 
				CLI()
		
		elif mode == "Naked - Account Generator":
			naked_gen_main()
			endTask = questionary.confirm(
			"Do you want to go back to the menu?"
			).ask()
			if endTask == True: 
				CLI()

	#################################################################################################################

	if user_choice == 11:
		clearConsole()
		printHeader()
		mode = questionary.select(
        "Which module do you want to start?",
        choices=[
			"SVD - Account Generator",
			"SVD - Info Updater",
			"SVD - Entry"
			]
    	).ask()
		
		if mode == "SVD - Entry":
			svd_main()
			endTask = questionary.confirm(
			"Do you want to go back to the menu?"
			).ask()
			if endTask == True: 
				CLI()

