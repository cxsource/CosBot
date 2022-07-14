/* ------------------------------------------------------------------------------- */

const Helheim = require("./helheim");

/* ------------------------------------------------------------------------------- */

const helheim = new Helheim({
    key: 'xxxxxxxxxxx',
    discover: false
});

/* ------------------------------------------------------------------------------- */

let session = helheim.createSession({
    browser: {
        browser: 'chrome',
        mobile: false,
        platform: 'windows'
    },
    captcha: {provider: 'vanaheim'}
});

session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36';

helheim.wokou(session);

// helheim.bifrost(session, './bifrost.so'); // use bifrost for JA3

// session.debug(true); // turn debugging on / off

session.cookies.push({name: 'test', value: 'test'}); // add cookie to the session
// console.log(session.cookies);

delete session.cookies[session.cookies.findIndex(x => x.name === 'test')]; // delete the cookie with the name 'test'

// session.proxy('https://user:password@host:port) // set proxy

try {
    
    let response = session.get("https://www.genx.co.nz/iuam/");
    
    /*
        let response = session.get(
            'https://www.genx.co.nz/iuam/',
            {
                headers: {'Accept-Encoding': 'gzip, deflate'},
                params: {myparam: 'myvalue'}
            }
        );
    */
    
    if (response.body.includes(`you got here`)) {
        console.log(response.body);
    }
    
    console.log();
    console.log(`Status Code -> ${response.status_code}`);
    console.log(
        JSON.stringify(
            {
                headers: session.headers,
                cookies: session.cookies
            },
            null,
            4
        )
    );
} catch (error) {
    console.log(error);
}

/* ------------------------------------------------------------------------------- */

helheim.deleteSession(session); // free any memory bound in python library for this session

/* ------------------------------------------------------------------------------- */
