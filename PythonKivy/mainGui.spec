# -*- mode: python ; coding: utf-8 -*-
# 导入需要的模块
from kivy_deps import sdl2, glew
# 根据项目情况添加gstreamer（打包视频应用）
# from kivy_deps import sdl2, glew, gstreamer

block_cipher = None


a = Analysis(['GuiKivy.py'],
             pathex=['F:\\05.Python\\PythonKivy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='MainGui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,Tree('F:\\05.Python\\PythonKivy'),  # 这里填写 spec文件存放的路径，不包含文件名
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               # 根据项目情况添加gstreamer（打包视频应用）
               # *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='MainGui')  # 文件夹名