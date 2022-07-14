#!/usr/bin/python3
import cloudscraper
import time
import uuid

from collections import OrderedDict
from datetime import datetime
from rest import REST

# ------------------------------------------------------------------------------- #

restAPI = REST()
restAPI.auth('xxxxxxxxxxxxxxxxxxxxxxxxxx') # dont spam auth, store your REST API framework globally or you will be banned

# ------------------------------------------------------------------------------- #

session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'mobile': False,
        'platform': 'windows'
    }
)

session.headers = OrderedDict([
    ('Connection', 'keep-alive'),
    ('Content-Length', None),
    ('Pragma', 'no-cache'),
    ('Cache-Control', 'no-cache,no-store'),
    ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'),
    ('Accept', 'application/json, text/plain, */*'),
    ('Accept-Encoding', 'gzip, deflate'),
    ('Accept-Language', 'en-us'),
    ('client-name', 'veve-app-ios'),
    ('client-model', 'iphone 7 plus'),
    ('client-version', '1.0.555'),
    ('client-brand', 'apple'),
    ('expires', '0'),
    ('client-installer', 'appstore'),
    ('client-manufacturer', 'apple'),
    ('client-id', '0110f916-bcaa-4a0c-b43a-xxxxxxxxx'),
    ('x-kpsdk-v', '1.6.0'),
])

# ------------------------------------------------------------------------------- #

domain = 'mobile.api.prod.veve.me'
baseURL = f'https://{domain}/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3'

# ------------------------------------------------------------------------------- #

response = session.get(f'{baseURL}/ips.js?x-kpsdk-v=1.6.0')

challengeAnswer = restAPI.solveCT(
    session.headers['User-Agent'],
    domain,
    response.text
)

response = session.post(
    f'{baseURL}/tl',
    data=challengeAnswer,
    headers={
        'Accept': '*/*',
        'x-kpsdk-ct': response.headers['x-kpsdk-ct'],
        'Content-Type': 'application/octet-stream',
        'Referer':f'{baseURL}/fp'
    }
)

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
        'x-kpsdk-ct': response.headers['x-kpsdk-ct'],
        'x-kpsdk-cd': restAPI.solveCD(domain),
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
        'x-kpsdk-ct': response.headers['x-kpsdk-ct'],
        'x-kpsdk-cd': restAPI.solveCD(domain),
        'client-operation': 'LoginBackground'
    }
)

# ------------------------------------------------------------------------------- #

session.post(
    'https://mobile.api.prod.veve.me/api/auth/totp/send',
    data=json.dumps(
        {'email': 'blah@blah.com'},
        separators=(',', ':')
    ),
    headers={
        'x-kpsdk-ct': response.headers['x-kpsdk-ct'],
        'x-kpsdk-cd': restAPI.solveCD(domain)
    }
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
        'Content-Type': 'application/json',
        'x-kpsdk-ct': response.headers['x-kpsdk-ct'],
        'x-kpsdk-cd': restAPI.solveCD(domain)
    }
)
