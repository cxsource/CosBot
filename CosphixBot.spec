# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['dist\\obf\\temp'],
    binaries=[('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\helheim\\pytransform_vax_000061.pyd', 'helheim')],
    datas=[('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\helheim', 'helheim'), ('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cloudscraper', 'cloudscraper'), ('C:\\Users\\Administrator\\AppData\\Local\\Programs\Python\\Python39\\Lib\\site-packages\\dateutil', 'dateutil')],
    hiddenimports=['helheim', 'cloudscraper', 'dateutil', 'pytransform_vax_001920'],
    hookspath=['dist\\obf\\temp'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CosphixBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='cosphixlogo.ico',
)
