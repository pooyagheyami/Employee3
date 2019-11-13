#In the name of God

import sys
import codecs
import os
from  Config.Init import *
from khayyam import *
import Utility.user as user
import Database.wxsq as sq





def BaseCheck():
    now = JalaliDatetime.now().strftime('%N/%P/%K')
    menlist = sq.wxsqsel('menu.db','access','*')
    for U in menlist:
        print U[0]
        print U[1]
        print U[2]

    
    return 0

    

def Startpro():
    f = codecs.open(CONFIG_PATH+'file1.txt',mode='r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    txt = ''
    for t in range(len(lines)):
            txt = txt + '\n' + lines[t]
    #print txt
    return txt


def Checkdatatime(date,now):
    if date[0][0] == now:
        print 'yes'
        return 11
    else:
        print 'no'
        return 12
        
    
def Getprogini():
    f = codecs.open(CONFIG_PATH+'program.ini',mode='r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    parametr = []
    for t in range(len(lines)):
        #print lines[t][:3]
        if lines[t][:3]=='rps':
            parametr.append(lines[t][6:7])
        if lines[t][:3]=='sps':
            parametr.append(lines[t][6:7])
        if lines[t][:3]=='bps':
            parametr.append(lines[t][6:7])
        if lines[t][:3]=='tps':
            parametr.append(lines[t][6:7])    
        if lines[t][:3]=='BGF':
            parametr.append(lines[t][6::])

    #print parametr
    return parametr

            
        
        
    
