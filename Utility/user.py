#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import security1 as sc
import Database.wxsq as sq

class dial():
    def __init__(self):

        self.dlg = sc.Secret(None)
        self.s = self.dlg.ShowModal()
        #print self.s
        self.dlg.Destroy()

    def getback(self):
        usepas= self.dlg.back()
        
        if usepas[0] == u'' or usepas[1] == u'':
            return 'No'
        else:
            test=userchk( usepas[0],usepas[1])
        if self.s==5100:
            if test == 'passed':
                return 'OK'
            if test == 'wrong':
                return 'No'
        else:
            return 'No'

def Checkpass():
    dlg = sc.Secret(None)
    dlg.CenterOnScreen()
    dlg.SetTitle(u'ورود کاربر')
    #dlg.SetSize((225,160))
    a=dial()
    s=a.getback()
    print s
    return s


def userchk(user,pasw):
    sc=sq.wxsqsnd('menu.db','security','password','username',user)
    print sc[0][0]
    #chkpass = scsql+"'"+user+"'")
    #print chkpass
    if sc[0][0] == pasw:
        return 'passed'
    else:
        return 'wrong'
    





