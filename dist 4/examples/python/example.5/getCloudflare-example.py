#!/usr/bin/python3

# ------------------------------------------------------------------------------- #

import argparse
import cloudscraper
import json

# ------------------------------------------------------------------------------- #

import helheim
helheim.auth('place_your_apiKey_here')

# ------------------------------------------------------------------------------- #

def injection(session, response):
    if helheim.isChallenge(session, response):
        return helheim.solve(session, response)
    else:
        return response

# ------------------------------------------------------------------------------- #

parser = argparse.ArgumentParser(description='Helheim Example.')

parser.add_argument('-u', '--url', action='store', type=str, help='URL with IUAM / hCaptcha', required=True)
parser.add_argument('-p', '--proxy', action='store', type=str, help='proxy to use.', required=False)
parser.add_argument('-a', '--agent', action='store', type=str, help='User-Agent to use.', required=False)
parser.add_argument('-c', '--captcha', action='store', type=str, help='captcha parmeters in json format.', required=False)
parser.add_argument('-d', '--debug', action='store_true', help='Enable Debug', required=False, default=False)
parser.add_argument('--no-bfm', action='store_true', help='disable Bot Fight Mode', required=False, default=False)
parser.add_argument('--platform', action='store', help='Which browser Platform to use.', required=False, default='windows')

args = parser.parse_args()

# ------------------------------------------------------------------------------- #

session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'mobile': False,
        'platform': args.platform
    },
    requestPostHook=injection,
    captcha={} if not args.captcha else json.loads(args.captcha.replace("'", '"')),
    debug=args.debug
)

helheim.wokou(session)

# ------------------------------------------------------------------------------- #

if args.no_bfm:
    session.disableBFM = True

# ------------------------------------------------------------------------------- #

if args.agent:
    session.headers['User-Agent'] = args.agent

# ------------------------------------------------------------------------------- #

if args.proxy:
    session.proxies = {
        'https': args.proxy,
        'https': args.proxy
    }

# ------------------------------------------------------------------------------- #

response = session.get(args.url)

print(f'Status Code -> {response.status_code}')
print(
    json.dumps(
        {
            'headers': session.headers,
            'cookies': session.cookies.get_dict()
        },
        indent=4
    )
)

