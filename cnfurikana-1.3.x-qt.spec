# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Qt5UI.py'],
             pathex=['D:\\Github\\cnfurikana'],
             binaries=[],
             datas=[( 'conv\\table.json', 'conv' ),
             ( 'conv\\settings.ini', 'conv' ),
             ( 'conv\\settings-cn.ini', 'conv' ),
             ( 'conv\\settings-jp.ini', 'conv' ),],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='cnfurikana-1.3.0qt',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='CNfurikana-1.3.1-qt')
