const ObservableSlim = require('observable-slim');
const {CookieJar} = require('tough-cookie');
const ffi = require('ffi-napi');
const path = require('path');

/* ------------------------------------------------------------------------------- */

class Helheim {
    constructor(config) {
        this.helheim_cffi = 'helheim_cffi.so';
        this.python_path = config.python_path == 'undefined' ? '' : config.python_path; // only needed on windows, set the python dir ie 'c:\\python39\\'
        this.helheim = this.initHelheim();
        this.auth(
            config.key,
            typeof(config.discover) != "undefined" ? true : false
        );
    }

    /* ------------------------------------------------------------------------------- */

    initHelheim() {
        if (this.python_path && this.python_path.length) {
            process.env.Path = this.python_path + ';' + process.env.Path;
        }

        let __dirname = path.resolve();
        return ffi.Library(
            path.join(__dirname, this.helheim_cffi),
            {
                'auth': ['string', ['string', 'int']],
                'getBalance': ['string', []],

                'bifrost': ['string', ['int', 'string']],
                'wokou': ['string', ['int', 'string']],

                'createSession': ['string', ['string']],
                'deleteSession': ['string', ['int']],

                'debug': ['string', ['int', 'int']],

                'setCookie': ['string', ['int', 'string']],
                'delCookie': ['string', ['int', 'string']],

                'setProxy': ['string', ['int', 'string']],
                'setHeaders': ['string', ['int', 'string']],

                'setKasada': ['string', ['int', 'string']],
                'setKasadaHooks': ['string', ['int', 'string']],

                'request': ['string', ['int', 'string']]
            },
            ffi.DynamicLibrary(
                path.join(__dirname, this.helheim_cffi),
                ffi.DynamicLibrary.FLAGS.RTLD_NOW | ffi.DynamicLibrary.FLAGS.RTLD_GLOBAL
            )
        );
    }

    /* ------------------------------------------------------------------------------- */

    auth(apiKey, discover) {
        let response = this.helheim.auth(apiKey, discover);

        if (response == null) {
            throw `Error -> auth() -> NULL response detected`;
        }

        return JSON.parse(response);
    }

    /* ------------------------------------------------------------------------------- */

    getBalance() {
        let response = this.helheim.getBalance();

        if (response == null) {
            throw `Error -> getBalance() -> NULL response detected`;
        }

        response = JSON.parse(response);
        if (response.error) {
            throw response.errorMsg;
        }

        return response.response;
    }

    /* ------------------------------------------------------------------------------- */

    createSession(options={}) {
        return new Session(this.helheim, options);
    }

    /* ------------------------------------------------------------------------------- */

    bifrost(session, libraryPath) {
        this.helheim.bifrost(session.sessionID, libraryPath);
    }

    /* ------------------------------------------------------------------------------- */

    wokou(session, browser='chrome') {
        this.helheim.wokou(session.sessionID, browser);
    }

    /* ------------------------------------------------------------------------------- */

    deleteSession(session) {
        session.close();
        session = null;
    }
}

/* ------------------------------------------------------------------------------- */

class Session {
    constructor(helheim, options={}) {
        this.helheim = helheim;
        this.session = {
            cookies: [],
            headers: {},
            helheim: {},
            kasada: {},
            kasadaHooks: {}
        };

        let proxyHandle = this; // hackery to use `this` in proxy...

        /* ------------------------------------------------------------------------------- */

        this.createSession(options);

        /* ------------------------------------------------------------------------------- */

        this.headers = ObservableSlim.create(
            this.session.headers,
            false,
            function(changes) {
                proxyHandle.helheim.setHeaders(
                    proxyHandle.sessionID,
                    JSON.stringify(proxyHandle.session.headers)
                );
            }
        );

        /* ------------------------------------------------------------------------------- */

        this.cookies = new Proxy(this.session.cookies, {
            set (target, property, value) {
                if (property !== 'length') {
                    let response = proxyHandle.handleResponse(
                        proxyHandle.helheim.setCookie(
                            proxyHandle.sessionID,
                            JSON.stringify(value)
                        )
                    );

                    proxyHandle.pushCookies(response.cookies);
                }

                return true;
            },

            deleteProperty (target, property) {
                let response = proxyHandle.handleResponse(
                    proxyHandle.helheim.delCookie(
                        proxyHandle.sessionID,
                        target[property].name
                    )
                );

                proxyHandle.pushCookies(response.cookies);

                return true;
            }
        });

        /* ------------------------------------------------------------------------------- */

        this.kasada = ObservableSlim.create(
            this.session.kasada,
            false,
            function(changes) {
                /*
                changes.forEach((n, i) => {
                    //JSON.stringify(n);
                    //console.log(JSON.stringify(n.target));
                });
                */
                proxyHandle.helheim.setKasada(
                    proxyHandle.sessionID,
                    JSON.stringify(proxyHandle.session.kasada)
                );
            }
        );

        /* ------------------------------------------------------------------------------- */

        this.kasadaHooks = ObservableSlim.create(
            this.session.kasadaHooks,
            false,
            function(changes) {
                proxyHandle.helheim.setKasadaHooks(
                    proxyHandle.sessionID,
                    JSON.stringify(proxyHandle.session.kasadaHooks)
                );
            }
        );
    }

    /* ------------------------------------------------------------------------------- */

    pushCookies(cookies) {
        this.session.cookies.length = 0;

        if (cookies.length) {
            for (let i = 0; i < cookies.length; i++) {
                this.session.cookies.push(cookies[i]); // we do this so we dont de-reference `target`
            }

            return true;
        }

        return false;
    }

    handleResponse(payload) {
        if (payload == null) {
            throw `Error -> NULL response detected`;
        }

        let response = JSON.parse(payload);

        if (response.error) {
            throw response.errorMsg;
        }

        return response;
    }

    /* ------------------------------------------------------------------------------- */

    createSession(options={}) {
        let session = this.handleResponse(
            this.helheim.createSession(
                JSON.stringify(options)
            )
        );

        this.sessionID = session.sessionID;
        this.session.headers = session.headers;

        this.pushCookies(session.cookies);

        return session;
    }

    /* ------------------------------------------------------------------------------- */

    close() {
        return this.handleResponse(
            this.helheim.deleteSession(this.sessionID)
        );
    }


    /* ------------------------------------------------------------------------------- */

    debug(state) {
        return this.handleResponse(
            this.helheim.debug(this.sessionID, state)
        );
    }

    /* ------------------------------------------------------------------------------- */

    // https://docs.python-requests.org/en/master/api/
    request(method, url, options={}) {
        try {
            let payload = this.handleResponse(
                this.helheim.request(
                    this.sessionID,
                    JSON.stringify({
                        method: method.toUpperCase(),
                        url: url,
                        options: options
                    })
                )
            );

            this.pushCookies(payload.session.cookies);

            Object.assign(this.session.headers, payload.session.headers);

            Object.assign(this.session.kasada, payload.session.kasada);
            Object.assign(this.session.kasadaHooks, payload.session.kasadaHooks);

            return {
                headers: payload.response.headers,
                cookies: payload.response.cookies,
                status_code: payload.response.status_code,
                body: payload.response.body
            };
        } catch(error) {
            throw error;
        }
    }

    /* ------------------------------------------------------------------------------- */

    get(url, options={}) {
        return this.request('GET', url, options);
    }

    /* ------------------------------------------------------------------------------- */

    post(url, options={}) {
        return this.request('POST', url, options);
    }

    /* ------------------------------------------------------------------------------- */

    proxy(proxy) {
        return this.handleResponse(
            this.helheim.setProxy(this.sessionID, proxy)
        );
    }

    /* ------------------------------------------------------------------------------- */

    // Give the user the ability to transform the cookies into a native cookieJar
    cookieJar() {
        cookieJar = new CookieJar();

        for (var cookie in this.session.cookies) {
            if (cookie) {
                cookieJar.setCookieSync(`${cookie.name}=${cookie.value}`, cookie.domain);
            }
        }

        return cookieJar;
    }
}

/* ------------------------------------------------------------------------------- */

module.exports = Helheim;
