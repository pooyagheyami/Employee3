#In the name of God

import sys
import os
import random
import codecs
import string
#import _winreg
from khayyam import *

NOW = JalaliDatetime.now().strftime('%N/%P/%K')
MAP = os.getcwd()
DRIVE = os.getcwd()[0:1]+u':\\'

if MAP.find(u'\\') > 0:
    SLASH = u'\\'
else:
    SLASH = u'/'
    

def opj(path):
    """Convert paths to the platform-specific separator"""
    st = SLASH+path
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    #print(st)
    return st



DATABASE_PATH = os.path.join(MAP,opj(u'Database')+SLASH)

GUI_PATH      = os.path.join(MAP,opj(u'GUI')+SLASH)
RES_PATH      = os.path.join(MAP,opj(u'Res')+SLASH)

ICONS_PATH    = os.path.join(RES_PATH,opj(u'Icons')+SLASH)
PICS_PATH     = os.path.join(RES_PATH,opj(u'Pics')+SLASH)
SPALSH_PATH   = os.path.join(RES_PATH,opj(u'Splash')+SLASH)

UTILITY_PATH  = os.path.join(MAP,opj(u'Utility')+SLASH)
CONFIG_PATH   = os.path.join(MAP,opj(u'Config')+SLASH)
LOGS_PATH     = os.path.join(MAP,opj(u'Logs')+SLASH)

TEMPS_PATH    = os.path.join(MAP,opj(u'Temps')+SLASH)
GUI_HELP      = os.path.join(GUI_PATH,opj(u'Help')+SLASH)
MY_PIC_PATH   = os.path.join(DRIVE,opj(u'Picture')+SLASH)

'''
def thistxt(filename):
    f = codecs.open(LOGS_PATH+filename,mode='r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    txt = ''
    for t in range(len(lines)):
            txt = txt + '\n' + lines[t]
    #print txt
    return txt
    
F = codecs.open(CONFIG_PATH+u"Config.txt",mode='r',encoding='utf-8')
lines = F.readlines()
F.close()

FONT_SIZE = int(lines[0])
FONT_TYPE = lines[1]
SCANDIR = lines[2].split('\r\n')[0]
SCNFILE = lines[3].split('\r\n')[0]
T = True
F = False
SIZE = (1024,768)
StringLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\x81\x83\x8a\x8c\x8d\x8e\x8f\x90\x98\x9a\x9c\x9f\xaa\xb5\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf8\xf9\xfa\xfb\xfc\xff'

def getregkey():
    access = _winreg.KEY_READ | _winreg.KEY_ENUMERATE_SUB_KEYS | _winreg.KEY_QUERY_VALUE
    keypath = "SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum"

    try:
        hkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,keypath,0,access)
    except (Exception , e):
        print(e)
        return ''

    i = _winreg.QueryValueEx(hkey,'Count')[0]
    for l in range(int(i)):
        srialit =  _winreg.QueryValueEx(hkey,str(l))[0].split('\\')[-1]
        #print srialit[1:-2]
    
    try:
        f = codecs.open(MAP+SLASH+'licence.txt',mode='r',encoding='utf-8')
        lines = f.readlines()
        f.close()
    except (Exception , e):
        print(e)
        return ''
            
    global MYLOCK
    #print lines[0][2:-2],srialit[1:-2]
    if srialit[1:-2] == lines[0][2:-2]:
        MYLOCK = True
    else:
        MYLOCK = False

    return MYLOCK    
'''
 




