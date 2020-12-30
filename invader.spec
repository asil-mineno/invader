# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['invader.py'],
             pathex=['C:\\work_suzuki\\invader_game-master'],
             binaries=[],
             datas=[],
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
          Tree('resources',prefix='resources'), #<-
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='invader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='crab.ico')
