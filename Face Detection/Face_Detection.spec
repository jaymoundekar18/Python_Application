# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Face_Detection.py'],
    pathex=[],
    binaries=[],
    datas=[('Python\\Lib\\site-packages\\cv2', 'cv2'), ('Python\\Lib\\site-packages\\facenet_pytorch', 'facenet_pytorch'), ('Python\\Lib\\site-packages\\PIL', 'PIL')],
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
    [],
    exclude_binaries=True,
    name='Face_Detection',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Face_Detection',
)
