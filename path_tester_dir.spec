# -*- mode: python -*-

block_cipher = None


a = Analysis(['path_tester.py'],
             pathex=['C:\\Users\\gotharbg\\Documents\\Python Projects\\PyInstaller_Testing'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('test.json', 'test.json', 'DATA')]
a.datas += [(os.path.join('directory', 'test.json'), os.path.abspath(os.path.join('directory', 'test.json')), 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='path_tester',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='path_tester')
