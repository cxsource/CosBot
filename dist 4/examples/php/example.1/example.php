<?php

$ffi = FFI::cdef(
    "char *getURL(const char *url);",
    "./helheim_cffi.so"
);

$response = json_decode(
    FFI::string($ffi->getURL('https://www.genx.co.nz/iuam/')),
    true
);

var_dump($response);
