# -*- mode: python ; coding: utf-8 -*-
from kivy.deps import sdl2,glew
import time
import json
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

block_cipher = None


a = Analysis(['C:\\Users\\Merve\\Desktop\\app\\pythonkivy\\Main.py'],
             pathex=['C:\\Users\\Merve\\Desktop\\todolist'],
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
          a.scripts,
          [],
          exclude_binaries=True,
          name='todolist',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,Tree('C:\\Users\\Merve\\Desktop\\app\\pythonkivy'),
               a.binaries,
               a.zipfiles,
               a.datas,
	       *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='todolist')
