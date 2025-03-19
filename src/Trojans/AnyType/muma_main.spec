# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['muma_main.py'],
    pathex=[],
    binaries=[],
    datas=[('files/屏幕截图 2025-02-28 104805.png', 'files'), ('files/屏幕截图 2025-02-28 104805.png', 'files'), ('files/client.exe', 'files'), ('conf.txt', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='muma_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['files\\屏幕截图 2025-02-28 104805.png'],
)
