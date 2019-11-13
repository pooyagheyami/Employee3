# -*- codnig: utf-8 -*-
# In the name of God
# Main Program Start
#!/usr/bin/env python


import wx
#import os
#import sys

import GUI.window as window
from  Config.Init import *
#import Utility.user as user

class mainApp(wx.App):

    def OnInit(self):
        #check directory and path in config file and program

        #check Databases of program

        #check Date,Time,propertis of file

        #Inter username and password of users
               

        #Check lock if nassesry
        #if not getregkey():
        #    wx.MessageBox(u'???? ?? ??? ????? ??? ??????? ????',u'???',wx.OK | wx.ICON_WARNING)
        #    wx.MessageBox(u'??? ??? ??? ?? 09115036878 ???? ?????',u'???',wx.OK | wx.ICON_WARNING)
        #    wx.Exit()

        #check hardware and connection
        SIZE = wx.DisplaySize()
        #print SIZE

        #do main windows of program 

        frame = window.MainWin()
        frame.SetSize(SIZE)
        frame.SetPosition((1,1))
        #frame.CenterOnScreen()
        
        frame.Show()


        
        return True
  



if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
