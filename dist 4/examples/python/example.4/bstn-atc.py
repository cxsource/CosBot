#!/usr/bin/python3

import re
import cloudscraper

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

session = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    },
    requestPostHook=injection
)

# ------------------------------------------------------------------------------- #

helheim.wokou(session)

# ------------------------------------------------------------------------------- #

baseURL = 'https://www.bstn.com'

# ------------------------------------------------------------------------------- #
# Get page that has the fingerprint challenge
session.get(baseURL)

# ------------------------------------------------------------------------------- #

# Load product page & parse kasada hooks...
response = session.get(f'{baseURL}/eu_it/p/reebok-reebok-x-kung-fu-panda-club-c-85-gz8633-0250255')

# ------------------------------------------------------------------------------- #
# Extract formKey from the product URL

if '"formKey":"' in response.text:
    session.cookies['form_key'] = re.search(
        r'''"formKey":"(?P<formkey>\w+)"''',
        response.text,
        re.S | re.M
    ).groupdict()['formkey']

# ------------------------------------------------------------------------------- #
# ATC

if hasattr(session, 'kasada'): # if epk was solved, helheim creates `kasada` attritbute.
    response = session.post(
        f"{baseURL}/eu_it/amasty_cart/cart/add/",
        data={
            'product': 60284,
            'selected_configurable_option': '',
            'related_product': '',
            'item': 60284,
            'alert_type': '',
            'form_key': session.cookies['form_key'], 
            'super_attribute[203]': 6348,
            'super_attribute[205]': 6372,
            'super_attribute[204]': 6318,
            'qty': 1,
            'product_page': 'true'
        },
        headers={
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': f'{baseURL}/eu_it/p/reebok-reebok-x-kung-fu-panda-club-c-85-gz8633-0250255'
        }
    )
    
    # ------------------------------------------------------------------------------- #
    
    response = session.get(f'{baseURL}/eu_it/checkout/')
    
    # ------------------------------------------------------------------------------- #
    
    cartID = re.search(
        r'''"quoteData":{"entity_id":"(\w+)",''',
        response.text,
        re.M | re.S
    ).group(1)
    
    print(f"cart id -> {cartID}")
    
    # ------------------------------------------------------------------------------- #
    
    response = session.post(
        f"{baseURL}/eu_it/rest/eu_it/V1/customers/isEmailAvailable",
        json={
            'customerEmail': 'blah123433@blah.com'
        },
        headers={
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }
    )
    
    # ------------------------------------------------------------------------------- #
    
    response = session.post(
        f"{baseURL}/eu_it/rest/eu_it/V1/guest-carts/{cartID}/estimate-shipping-methods",
        json={
            "address": {
                'street': [
                    'Guild Street',
                    '38',
                    'Floor 1'
                ],
                'city': 'London',
                'region': '',
                'country_id': 'GB',
                'postcode': None,
                'firstname': 'John',
                'lastname': 'Doe',
                'company': '',
                'telephone': '',
                'custom_attributes': [{
                    'attribute_code': 'gender',
                    'value': '1'
                }]
            }
        },
        headers={
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }
    )
    print(response.json())

# ------------------------------------------------------------------------------- #
# etc... etc...
