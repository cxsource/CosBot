@echo off

set "{{=setlocal enableDelayedExpansion&for %%a in (" & set "}}="::end::" ) do if "%%~a" neq "::end::" (set command=!command! %%a) else (call !command! & endlocal)"

%{{%
    c:\python37\scripts\pyarmor pack
    -x " --advanced 2 --bootstrap 2 --enable-suffix --exclude helheim"
    -e "
        --add-data 'c:/python37/lib/site-packages/helheim^;helheim'
        --add-binary 'c:/python37/lib/site-packages/helheim/pytransform_vax_000061.pyd^;helheim'
        --add-data 'c:/python37/lib/site-packages/cloudscraper^;cloudscraper'
        -c
        --onefile
        --hidden-import dateutil.parser
        --hidden-import helheim
        --hidden-import cloudscraper
        --hidden-import cryptography
        --hidden-import polling2
        --hidden-import PIL
        --hidden-import PIL.Image
    "
    --name test
    getCloudflare-example.py
%}}%
