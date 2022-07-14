import os
import sys
from importlib.util import find_spec

installedPaths = find_spec('helheim').submodule_search_locations
version=f"{sys.version_info.major}.{sys.version_info.minor}"
execPrefix = next(
    filter(
        lambda k: os.path.isfile(k),
        [f"{sys.exec_prefix}/Python", f"{sys.exec_prefix}/Python3"]
    ),
    False
)

if execPrefix:
    print(
        "if you are getting the error `Reason: image not found` when importing helheim, " \
        "try issue the following command."
    )
    for path in installedPaths:
        print(
            "install_name_tool -change " \
            f"@rpath/Frameworks/Python.framework/Versions/{version}/Python " \
            f"{execPrefix} " \
            f"{path}/pytransform.cpython-{version.replace('.', '')}" \
            f"{'m' if version == '3.7' else ''}-darwin.so"
        )
else:
    print()
    print(r'[!!] Unable to determine your python install ¯\_(ツ)_/¯')