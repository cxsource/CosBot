#!/usr/bin/python3

# ------------------------------------------------------------------------------- #

import cloudscraper
from collections import OrderedDict

# import'able helheim exceptions if you want to trap specific errors.
from helheim.exceptions import (
    HelheimException,
    HelheimSolveError,
    HelheimRuntimeError,
    HelheimSaaSError,
    HelheimSaaSBalance,
    HelheimVersion,
    HelheimAuthError,
    HelheimBifrost
)

# ------------------------------------------------------------------------------- #

import helheim

# ------------------------------------------------------------------------------- #

'''
    # To disable closet SaaS API edge point discovery use `discover=False`
    # This is will force to use default defined api host
    # kwargs for .auth()
    #    discover (boolean) (default: True)
    #    debug (boolean) (default: False)
    helheim.auth('place_your_apiKey_here', discover=False)
'''

helheim.auth('place_your_apiKey_here')

# ------------------------------------------------------------------------------- #

def injection(session, response):
    '''
    # use 'ignore' parameter to not trigger helheim....
    # (some sites put BFM into their overloaded pages etc)
    if helheim.isChallenge(
        response,
        ignore=[
            {
                'status_code': [403, 503], # list or int
                'text': ['text on page to match', ...] # list of strings.. or string of regex to match
            },
            {
                ...
            }
        ]
    ):
    '''
    if helheim.isChallenge(session, response):
        # solve(session, response, max_tries=5)
        return helheim.solve(session, response)
    else:
        return response

# ------------------------------------------------------------------------------- #

# Documentation for cloudscraper https://github.com/venomous/cloudscraper/

session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome', # we want a chrome user-agent
        'mobile': False, # pretend to be a desktop by disabling mobile user-agents
        'platform': 'windows' # pretend to be 'windows' or 'darwin' by only giving this type of OS for user-agents
    },
    requestPostHook=injection,
    # Add a hCaptcha provider if you need to solve hCaptcha
    # captcha={
    #     'provider': '...', # use 'vanaheim' for built in solver, dont need api key param
    #     'api_key': '....'
    # }
)

# ------------------------------------------------------------------------------- #

# using proper http/2 headers...
session.headers = OrderedDict([
    ('sec-ch-ua', '"Not A;Brand;v="99", "Chromium";v="90", "Google Chrome";v="90"'),
    ('sec-ch-ua-mobile', '?0'),
    ('upgrade-insecure-requests', '1'),
    ('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'),
    ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
    ('sec-fetch-site', 'none'),
    ('sec-fetch-mode', 'navigate'),
    ('sec-fetch-user', '?1'),
    ('sec-fetch-dest', 'document'),
    ('accept-encoding', 'gzip, deflate'),
])

# ------------------------------------------------------------------------------- #

# Manipulate / tune the session SSL Context
# session.bifrost_clientHello = browser # if this variable is not defined, the default is chrome

# chrome (default chrome98) -> chrome62, chrome70, chrome72, chrome83, chrome91, chrome98
# firefox (default firefox98) -> firefox55, firefox56, firefox63, firefox65, firefox89, firefox97
# safari (default safari14) -> safari14
# ie (default ie11) -> ie11 # currently broken...
# ios (default ios15.3.1) -> ios11.1, ios12.1, 14.8, 15.3.1
# veve (default veve_ios) -> veve_ios
# veve_ios (default veve15.3.1) -> veve_ios14, veve_ios14.8, veve15.3.1,
# veve_android (LineageOS 17.1)

session.bifrost_clientHello = 'chrome'

# Or use a ja3 string from https://ja3er.com/
# session.bifrost_ja3 = '771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-21,29-23-24,0'

helheim.bifrost(session, '/tmp/bifrost.so') # use your own path of where you are storing your bifrost uTLS shared library

# ------------------------------------------------------------------------------- #

# uncomment the following to disable verify on push... `server not authoritative for push with host`
# session.bifrost_disablePushVerify = True

# ------------------------------------------------------------------------------- #

# uncomment the following if you don't want to solve Cloudflare challenges
# session.disableCloudflare = True

# ------------------------------------------------------------------------------- #

# uncomment the following if you don't want to solve BFM (Bot Fight Mode)
# https://blog.cloudflare.com/cleaning-up-bad-bots/
# session.disableBFM = True

# ------------------------------------------------------------------------------- #

# uncomment the following if you don't want to solve Kasada
# session.disableKasada = True

# ------------------------------------------------------------------------------- #

# uncomment the following if you don't want to solve SNS ATC
# session.disableSNS = True

# ------------------------------------------------------------------------------- #

# uncomment the following if you don't want to solve slowAES
# session.disableSlowAES = True

# ------------------------------------------------------------------------------- #

# helheim is designed to NOT inherit the headers, proxies params on a request, it will only access the session.
# if you require to manually set the User-Agent or proxies, set them on the session not in the get().

# ie session.headers['User-Agent'] = '....'
# ie session.proxies = {'https': 'http://username:password@myproxy:8080'}

# ------------------------------------------------------------------------------- #

print(session.get('https://www.sneakersnstuff.com/en/product/42337/adidas-700').status_code)

