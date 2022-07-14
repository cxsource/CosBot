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
    ("client-bootloader", "g998bxxs3auj7"),
    ("client-host", "21djfo06"),
    ("client-manufacturer", "samsung"),
    ("client-brand", "samsung"),
    ("Client-model", "sm-g998b"),
    ("client-id", "080d788a38ff7eee"),
    ("client-adb-enabled", "false"),
    ("client-hook", "false"),
    ("client-version", "1.0.555"),
    ("client-name", "veve-app-android"),
    ("user-agent", "Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36"),
    ("x-kpsdk-v", "a-1.3.0"),
    ("client-installer", "com.android.vending"),
    ("client-carrier", "smarty"),
    ("client-fingerprint", "samsung/p3sxeea/p3s:11/rp1a.200720.012/g998bxxs3auj7:user/release-keys"),
    ("client-hardware", "exynos2100"),
    ("client-product", "p3sxeea"),
    ("client-tags", "release-keys"),
    ("client-development-settings", "false"),
    ("client-user-id", "d9102b11-76b1-462e-a112-3a698ae95343"),
    ("Content-Type", "application/json"),
    ("Accept-Encoding", "gzip, deflate")
])

# ------------------------------------------------------------------------------- #

domain = 'mobile.api.prod.veve.me'
baseURL = f'https://{domain}/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3'

# ------------------------------------------------------------------------------- #

response = session.get(f'{baseURL}/ips.js?x-kpsdk-v=a-1.3.0')

challengeAnswer = restAPI.solveCT(
    session.headers['user-agent'],
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

