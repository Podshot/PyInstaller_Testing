# -*- mode: python -*-

import sys

is_osx = sys.platform == 'darwin'

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

if not is_osx:
    a.scripts += a.binaries + a.zipfiles + a.datas + a.zipped_data

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
#          a.binaries,
#          a.zipfiles,
#          a.datas,
          name='path_tester',
          exclude_binaries=is_osx,
          debug=True,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True )

if is_osx:
    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   strip=None,
                   upx=True,
                   name='path_tester')

    bundle = BUNDLE(coll,
                    name='path_tester.app',
                    bundle_identifier='io.github.podshot.path_tester')


