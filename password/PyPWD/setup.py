"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
from glob import glob

APP_NAME = "PyPWD"
APP = ['pypwd.py']
DATA_FILES = [('libs', glob('libs/*.py')),'app.icns']
OPTIONS = {
	'iconfile':'app.icns',
	'argv_emulation': True,
	 'plist': {
	        'CFBundleName': APP_NAME,
	        'CFBundleDisplayName': APP_NAME,
	        'CFBundleGetInfoString': "PyPWD Manager",
	        'CFBundleIdentifier': "com.metagaranet.osx.pypwd",
	        'CFBundleVersion': "1.0.8",
	        'CFBundleShortVersionString': "1.0.8", 
	        'NSHumanReadableCopyright': u"Copyright © 2005-2019 Garanet. All Rights Reserved"
	    },	
    'compressed': True,
	'packages': ['numpy','pandas','pyAesCrypt','cryptography','PyQt5-sip','PyQt5']
}

setup(
	name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)