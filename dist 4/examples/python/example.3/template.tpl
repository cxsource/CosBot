import cloudscraper
import itertools
import json
import os
import sys

from collections import OrderedDict
from helheim_cffi import ffi

# ------------------------------------------------------------------------------- #

sys.path.append(os.getcwd())
import helheim

# ------------------------------------------------------------------------------- #
class AttributeDict(dict):
    __slots__ = ()
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

sessions = {
    0: AttributeDict(), # reserved
    'index': itertools.count(1)
}

# ------------------------------------------------------------------------------- #

def injection(session, response):
    if helheim.isChallenge(session, response):
        return helheim.solve(session, response)
    else:
        return response

# ------------------------------------------------------------------------------- #

def _getcookies(sessionID):
    cookies = []

    for cookie in sessions[sessionID].cookies:
        cookies.append({
            'name': cookie.name,
            'value': cookie.value,
            'domain': cookie.domain,
            'path': cookie.path,
            'expires': cookie.expires
        })

    return cookies

# ------------------------------------------------------------------------------- #

def responseWrapper(payload):
    sessionID = payload['sessionID']
    response = ffi.new(
        'char []',
         json.dumps(payload).encode()
    )

    sessions[sessionID].memory_stack = response # hackery to hold memory from gc

    return response

# ------------------------------------------------------------------------------- #

def getString(payload):
    return ffi.string(payload).decode()

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def auth(apiKey, discover):
    helheim.auth(getString(apiKey), discover=discover)

    return responseWrapper({
        'sessionID': 0,
        'response': 'authenticated'
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def getBalance():
    response = helheim.getBalance()
    if not response:
        responseWrapper({
                'sessionID': 0,
                'error': True,
                'errorMsg': 'Could not get Balance'
            })

    return responseWrapper({
        'sessionID': 0,
        'error': False,
        'response': response
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def bifrost(sessionID, libraryPath):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    helheim.bifrost(sessions[sessionID], getString(libraryPath))

    return responseWrapper({
        'sessionID': 0,
        'response': 'bifrost',
        'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def wokou(sessionID, browser):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    helheim.wokou(sessions[sessionID], getString(browser))

    return responseWrapper({
        'sessionID': sessionID,
        'response': 'wokou',
        'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def createSession(options):
    sessionID = next(sessions['index'])

    options = json.loads(
        getString(options)
    )

    if 'browser' not in options:
        options['browser'] = {
            'browser': 'chrome',
            'mobile': False,
            'platform': 'windows'
        }

    options['requestPostHook'] = injection

    sessions[sessionID] = cloudscraper.create_scraper(**options)

    helheim.wokou(sessions[sessionID])

    return responseWrapper({
        'sessionID': sessionID,
        'headers': sessions[sessionID].headers,
        'cookies': _getcookies(sessionID),
        'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def request(sessionID, payload):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    payload = json.loads(getString(payload))

    options = {
        'method': payload['method'],
        'url': payload['url']
    }

    options.update(payload['options'])

    try:
        response = sessions[sessionID].request(**options)
    except Exception as e:
        return responseWrapper({
            'sessionID': sessionID,
            'error': True,
            'errorMsg': str(e)
        })

    payload = {
        'sessionID': sessionID,
        'session': {
            'headers': dict(sessions[sessionID].headers),
            'cookies': _getcookies(sessionID)
        },
        'response': {
            'headers': dict(response.headers),
            'cookies': response.cookies.get_dict(),
            'status_code': response.status_code,
            'body': response.text
        },
        'error': False
    }

    if hasattr(sessions[sessionID], 'kasada'):
        payload['session']['kasada'] = sessions[sessionID].kasada

    if hasattr(sessions[sessionID], 'kasadaHooks'):
        payload['session']['kasadaHooks'] = sessions[sessionID].kasadaHooks

    return responseWrapper(payload)

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def deleteSession(sessionID):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    del sessions[sessionID]

    return responseWrapper({
       'sessionID': 0,
       'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def debug(sessionID, state):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    sessions[sessionID].debug = state

    return responseWrapper({
        'sessionID': sessionID,
        'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def setProxy(sessionID, proxy):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    sessions[sessionID].proxies = {
        'http': getString(proxy),
        'https': getString(proxy)
    }

    return responseWrapper({
        'sessionID': sessionID,
        'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def setHeaders(sessionID, headers):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    try:
        sessions[sessionID].headers = json.loads(
            getString(headers),
            object_pairs_hook=OrderedDict
        )
    except Exception as e:
        return responseWrapper({
            'error': True,
            'errorMsg': e
        })

    return responseWrapper({
        'sessionID': sessionID,
        'error': False
    })


# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def setKasadaHooks(sessionID, kasadaHooks):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    try:
        sessions[sessionID].kasadaHooks = json.loads(
            getString(kasadaHooks),
            object_pairs_hook=OrderedDict
        )
    except Exception as e:
        return responseWrapper({
            'error': True,
            'errorMsg': e
        })

    return responseWrapper({
        'sessionID': sessionID,
        'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def setKasada(sessionID, kasada):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    try:
        sessions[sessionID].kasada = json.loads(
            getString(kasada),
            object_pairs_hook=OrderedDict
        )
    except Exception as e:
        return responseWrapper({
            'error': True,
            'errorMsg': e
        })

    return responseWrapper({
        'sessionID': sessionID,
        'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def setCookie(sessionID, cookiePayload):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    cookie = json.loads(
        getString(cookiePayload)
    )

    sessions[sessionID].cookies.set(**cookie)

    return responseWrapper({
        'sessionID': sessionID,
        'cookies': _getcookies(sessionID),
        'error': False
    })

# ------------------------------------------------------------------------------- #

@ffi.def_extern()
def delCookie(sessionID, cookie):
    if sessionID not in sessions:
        return responseWrapper({
            'sessionID': 0,
            'error': True,
            'errorMsg': 'No Session By that ID'
        })

    cookie = getString(cookie)
    if cookie in sessions[sessionID].cookies:
        del sessions[sessionID].cookies[cookie]

    return responseWrapper({
        'sessionID': sessionID,
        'cookies': _getcookies(sessionID),
        'error': False
    })

# ------------------------------------------------------------------------------- #
