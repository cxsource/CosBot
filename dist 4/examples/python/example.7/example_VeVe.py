#!/usr/bin/python3

# ------------------------------------------------------------------------------- #

import cloudscraper
import json

from collections import OrderedDict

# ------------------------------------------------------------------------------- #

import helheim
helheim.auth('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# ------------------------------------------------------------------------------- #

def injection(session, response):
    if helheim.isChallenge(session, response):
        response = helheim.solve(session, response, 3)
    return response

# ------------------------------------------------------------------------------- #

session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'mobile': False,
        'platform': 'windows'
    },
    requestPostHook=injection,
    debug=True
)

# ------------------------------------------------------------------------------- #

helheim.wokou(session)

# ------------------------------------------------------------------------------- #

session.headers = OrderedDict([
    ('client-version', '1.0.588'),
    ('cache-control', 'no-cache,no-store'),
    ('client-name', 'veve-app-ios'),
    ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'),
    ('client-model', 'iphone 7 plus'),
    ('pragma', 'no-cache'),
    ('client-brand', 'apple'),
    ('x-kpsdk-v', 'i-1.6.0'),
    ('accept-language', 'en-us'),
    ('expires', '0'),
    ('client-manufacturer', 'apple'),
    ('client-installer', 'appstore'),
    ('accept', 'application/json, text/plain, */*'),
    ('content-type', 'application/json;charset=utf-8'),
    ('accept-encoding', 'gzip, deflate, br'),
    ('client-id', '0110f916-bcaa-4a0c-x43a-xxxxxxx')
])

# ------------------------------------------------------------------------------- #

# manually define kasada end point prehooks since VeVe doesnt act like normal kasada
session.kasadaHooks = {
    'mobile.api.prod.veve.me': {
        'POST': [
            '/graphql',
            '/api/auth/*'
        ]
    }
}

# ------------------------------------------------------------------------------- #

# manually call VeVe's Kasada EPK challenge
session.get('https://mobile.api.prod.veve.me/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp')

# ------------------------------------------------------------------------------- #

response = session.post(
    'https://mobile.api.prod.veve.me/graphql',
    data=json.dumps(
        {
            'operationName': 'AppMetaInfo',
            'variables': {},
            'query': '''query AppMetaInfo { minimumMobileAppVersion featureFlagList { name enabled __typename }}'''
        },
        separators=(',', ':')
    ),
    headers={
        'Content-Type': 'application/json',
        'client-operation': 'AppMetaInfo'
    }
)

# ------------------------------------------------------------------------------- #

session.post(
    'https://mobile.api.prod.veve.me/graphql',
    data=json.dumps(
        {
            'operationName': 'LoginBackground',
            'variables': {},
            'query': '''query LoginBackground { loginBackground { id fullResolutionUrl  __typename }}'''
        },
        separators=(',', ':')
    ),
    headers={
        'Content-Type': 'application/json',
        'client-operation': 'LoginBackground'
    }
)

# ------------------------------------------------------------------------------- #

session.post(
    'https://mobile.api.prod.veve.me/api/auth/totp/send',
    data=json.dumps(
        {'email': 'blah@blah.com'},
        separators=(',', ':')
    )
)

# ------------------------------------------------------------------------------- #

response = session.post(
    'https://mobile.api.prod.veve.me/api/auth/login',
    data=json.dumps(
        {
            'email': 'blah@blah.com',
            'password': 'mypassword',
            'totp': totp_code_from_email
        },
        separators=(',', ':')
    ),
    headers={
        'Content-Type': 'application/json'
    }
)


