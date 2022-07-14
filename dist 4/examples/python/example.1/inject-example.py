#!/usr/bin/python3

# ------------------------------------------------------------------------------- #

import cloudscraper

# import'able helheim exceptions if you want to trap specific errors.
from helheim.exceptions import (
    HelheimException,
    HelheimSolveError,
    HelheimRuntimeError,
    HelheimSaaSError,
    HelheimSaaSBalance,
    HelheimVersion,
    HelheimAuthError
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

# "Attempt" to Manipulate / tune the session SSL Context ... may not work on mac
# helheim.wokou(session, browser)
# browser parameter (tries to mimic browser ssl context): 'chrome' (default), 'firefox or 'safari'

helheim.wokou(session)

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
# ie session.proxies = {'https': 'http://myproxy:8080'}

# ------------------------------------------------------------------------------- #

print(session.get('https://www.sneakersnstuff.com/en/product/42337/adidas-700').status_code)

