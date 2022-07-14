/* ------------------------------------------------------------------------------- */

const Helheim = require("./helheim");

/* ------------------------------------------------------------------------------- */

const helheim = new Helheim({
    key: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    discover: false
});

/* ------------------------------------------------------------------------------- */

let session = helheim.createSession({
    browser: {
        browser: 'chrome',
        mobile: false,
        platform: 'windows'
    },
    captcha: {provider: 'vanaheim'},
});

helheim.wokou(session);

/* ------------------------------------------------------------------------------- */

Object.assign(
    session.headers,
    {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'x-kpsdk-v': 'i-1.4.0',
        'client-brand': 'apple',
        'accept': '*/*',
        'client-id': '0010x916-xxxx-4xxc-b43a-xxxxxxx',
        'client-name': 'veve-app-ios',
        'client-manufacturer': 'apple',
        'client-model': 'iphone 7 plus',
        'client-version': '1.0.539'
    }
);

//session.proxy('http://xxx.x.xx.xx:8080');

/* ------------------------------------------------------------------------------- */

session.kasadaHooks['mobile.api.prod.veve.me'] = {
    POST: [
        '/graphql',
        '/api/auth/*',
    ]
};

/* ------------------------------------------------------------------------------- */

try {
    session.get('https://mobile.api.prod.veve.me/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp');

    //session.debug(true);

    let response = session.post(
        'https://mobile.api.prod.veve.me/graphql',
        {
            json: {
                'operationName': 'AppMetaInfo',
                'variables': {},
                'query': `query AppMetaInfo {minimumMobileAppVersion featureFlagList {name enabled __typename}}`
            },
            headers: {'client-operation': 'AppMetaInfo'},
        }
    );

    response = session.post(
        'https://mobile.api.prod.veve.me/graphql',
        {
            json: {
                'operationName': 'LoginBackground',
                'variables': {},
                'query': `query LoginBackground { loginBackground { id fullResolutionUrl  __typename }}`
            },
            headers: {'client-operation': 'LoginBackground'},
        }
    );
} catch (error) {
    console.log(error);
}

/* ------------------------------------------------------------------------------- */

helheim.deleteSession(session); // free any memory bound in python library for this session

/* ------------------------------------------------------------------------------- */
