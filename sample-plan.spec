# -*- mode: python -*-

block_cipher = None


a = Analysis(['sample-plan.py'],
             pathex=['C:\\Users\\100355\\app-dev\\python\\sample-plan'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='sample-plan',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='mag-glass.ico')
