#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
from term1 import *

'''
class telframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent=parent

        self.panel = term1.MyPanel1(self)

        
    def closeit(self):
        self.Close(True)

        
def size():
    return (393,464)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    parent =  panel.GetParent()
    
    frame = telframe(parent )
    frame.SetTitle(u'اتصال')
    frame.SetSize(size())
    frame.Show()
    

'''

def size():
    return (393,464)


def main(panel=None):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    parent =  panel.GetParent()
    myapp = wx.GetApp()
    wx.InitAllImageHandlers()

    frame_terminal = TerminalFrame(parent, -1, "دريافت اطلاعات از پورت دستگاه")
    myapp.SetTopWindow(frame_terminal)
    frame_terminal.Show(True)
    return 1

if __name__ == '__main__':
    #app = wx.App(False) 
    main()
    #app.MainLoop()
    
