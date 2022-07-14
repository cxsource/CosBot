#!/usr/bin/python3

import cffi
import platform
import sysconfig

# ------------------------------------------------------------------------------- #

extensionMap = {
    'Linux': 'so',
    'Darwin': 'dylib',
    'Windows': 'dll'
}

# ------------------------------------------------------------------------------- #

ffibuilder = cffi.FFI()

# ------------------------------------------------------------------------------- #

ffibuilder.embedding_api(
    """
    char *auth(char apiKey[], int discover);
    char *getBalance();
    char *bifrost(int sessionID, char libraryPath[]);
    char *wokou(int sessionID, char browser[]);

    char *createSession(char options[]);
    char *deleteSession(int sessionID);
    char *debug(int sessionID, int state);

    char *request(int sessionID, char payload[]);

    char *setProxy(int sessionID, char proxy[]);
    char *setHeaders(int sessionID, char headers[]);
    char *setKasada(int sessionID, char kasada[]);
    char *setKasadaHooks(int sessionID, char kasadaHooks[]);

    char *setCookie(int sessionID, char cookie[]);
    char *delCookie(int sessionID, char cookie[]);
    """
)

# ------------------------------------------------------------------------------- #

libraryPath = sysconfig.get_config_vars('LIBDIR')
if libraryPath and libraryPath[0]:
    ffibuilder.set_source("helheim_cffi", "", library_dirs=libraryPath)
else:
    ffibuilder.set_source("helheim_cffi", "")

# ------------------------------------------------------------------------------- #

with open('template.tpl', 'r') as code:
    ffibuilder.embedding_init_code(code.read())

# ------------------------------------------------------------------------------- #

ffibuilder.compile(
    target=f"../helheim_cffi.{extensionMap[platform.system()]}",
    verbose=True
)
