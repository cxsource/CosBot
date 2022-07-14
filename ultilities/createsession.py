"""********************************************************************"""
"""                                                                    """
"""   [charafdissou] createsession.py                                  """
"""                                                                    """
"""   Author: Charaf <sourcetimenotify@gmail.com>                      """
"""                                                                    """
"""   Created: 17/04/2022 12:49:34                                     """
"""   Updated: 13/07/2022 15:10:55                                     """
"""                                                                    """
"""   Source Empire CSD UG (c) 2022                                    """
"""                                                                    """
"""********************************************************************"""

import requests
import helheim
import cloudscraper
import platform
import random
import json
from ultilities.logger import logger
from ultilities.ProxyManager import getProxies


def getsession(usedproxy):

    if usedproxy is None:
        session = requests.Session()
    else:
        session = requests.session()
        proxyParts = usedproxy.split(":")
        session.proxies.update(
            {
                "http": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
                "https": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
            }
        )
        return session

        #pro.nextproxies.io: username
        #7000: port
        #user-NXT_9330ti2A-country-de-session-KH8mabuj: 
        #j1yAQ3sfZP: pass




helheim.auth('b7e34971-4093-4a76-898e-c7c3f3ba7cf3')

def injection(session, response):
    if helheim.isChallenge(session, response):
        return helheim.solve(session, response)
    else:
        return response

def CFsession(usedproxy):

    with open("config.json", "r") as file:
        data = json.load(file)

    key = data["CaptchaServices"]["2Captcha"]
        
    session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome', # we want a chrome user-agent
        'mobile': False, # pretend to be a desktop by disabling mobile user-agents
        'platform': 'windows' # pretend to be 'windows' or 'darwin' by only giving this type of OS for user-agents
    },
    requestPostHook=injection,
    # Add a hCaptcha provider if you need to solve hCaptcha
    captcha={
        'provider': '2captcha', # use 'vanaheim' for built in solver, dont need api key param
        'api_key': key
    }
)

    try:
        session.bifrost_clientHello = 'chrome'
        if platform.system().lower() == "windows":
            helheim.wokou(session, random.choice(["chrome", "firefox"]))
            helheim.bifrost(session, '/bifrost.dll')
        elif (platform.system().lower() == "linux"):
            helheim.wokou(session, random.choice(["chrome", "firefox"]))
            helheim.bifrost(session, '/bifrost.so')
        else:
            helheim.bifrost(session, './bifrost.dylib')
    except Exception as e:
        logger(("Error while initiating session using bifrost : {}".format(str(e))), "Bitfrost", "error", tasknumber="Attention Needed!")

    proxyParts = usedproxy.split(":")
    session.proxies.update(
            {
                "http": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
                "https": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
            }
        )

    # proxy = getProxies()
    # session.proxies.update([proxy])

    # print(session.get('https://www.nakedcph.com/en/search/bysearchdefinition/1282').status_code)

    return (session)



def CFsession1():

    with open("config.json", "r") as file:
        data = json.load(file)

    key = data["CaptchaServices"]["2Captcha"]
        
    session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome', # we want a chrome user-agent
        'mobile': False, # pretend to be a desktop by disabling mobile user-agents
        'platform': 'windows' # pretend to be 'windows' or 'darwin' by only giving this type of OS for user-agents
    },
    requestPostHook=injection,
    # Add a hCaptcha provider if you need to solve hCaptcha
    captcha={
        'provider': '2captcha', # use 'vanaheim' for built in solver, dont need api key param
        'api_key': key
    }
)

    try:
        session.bifrost_clientHello = 'chrome'
        if platform.system().lower() == "windows":
            helheim.wokou(session, random.choice(["chrome", "firefox"]))
            helheim.bifrost(session, '/bifrost.dll')
        elif (platform.system().lower() == "linux"):
            helheim.wokou(session, random.choice(["chrome", "firefox"]))
            helheim.bifrost(session, '/bifrost.so')
        else:
            helheim.bifrost(session, './bifrost.dylib')
    except Exception as e:
        logger(("Error while initiating session using bifrost : {}".format(str(e))), "Bitfrost", "error", tasknumber="Attention Needed!")

    # proxyParts = usedproxy.split(":")
    # session.proxies.update(
    #         {
    #             "http": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
    #             "https": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
    #         }
    #     )

    # proxy = getProxies()
    # session.proxies.update([proxy])

    # print(session.get('https://www.nakedcph.com/en/search/bysearchdefinition/1282').status_code)

    return (session)


def CFsession3(usedproxy):

    with open("config.json", "r") as file:
        data = json.load(file)

    key = data["CaptchaServices"]["2Captcha"]
        
    session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome', # we want a chrome user-agent
        'mobile': False, # pretend to be a desktop by disabling mobile user-agents
        'platform': 'windows' # pretend to be 'windows' or 'darwin' by only giving this type of OS for user-agents
    },
    requestPostHook=injection,
    # Add a hCaptcha provider if you need to solve hCaptcha
    captcha={
        'provider': 'vanaheim', # use 'vanaheim' for built in solver, dont need api key param
    }
)

    try:
        session.bifrost_clientHello = 'chrome'
        if platform.system().lower() == "windows":
            helheim.wokou(session, random.choice(["chrome", "firefox"]))
            helheim.bifrost(session, './bifrost.dll')
        elif (platform.system().lower() == "linux"):
            helheim.wokou(session, random.choice(["chrome", "firefox"]))
            helheim.bifrost(session, './bifrost.so')
        else:
            helheim.bifrost(session, './bifrost.dylib')
    except Exception as e:
        logger(("Error while initiating session using bifrost : {}".format(str(e))), "Bitfrost", "error", tasknumber="Attention Needed!")

    proxyParts = usedproxy.split(":")
    # session.headers['user-agent'] = "SVD/2002252234 CFNetwork/1220.1 Darwin/20.3.0"
    session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    session.proxies.update(
            {
                "http": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
                "https": f"http://{proxyParts[2]}:{proxyParts[3]}@{proxyParts[0]}:{proxyParts[1]}",
            }
        )

    # proxy = getProxies()
    # session.proxies.update([proxy])

    # print(session.get('https://www.nakedcph.com/en/search/bysearchdefinition/1282').status_code)

    return (session)