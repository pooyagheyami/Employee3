#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import ramp1


class telframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent=parent

        #lbel = [u'شيفت',u'گروه',u'خروجي',u'ورودي',u'نام خانوادگي',u'نام',u'تاريخ']       
        self.panel = ramp1.MyPanel1(self)

        
    def closeit(self):
        self.Close(True)

        
def size():
    return (393,464)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    parent =  panel.GetParent()
    
    frame = telframe(parent )
    frame.SetTitle(u'آمار')
    frame.SetSize(size())
    frame.Show()
    

    

if __name__ == '__main__':
    #app = wx.App(False) 
    main()
    #app.MainLoop()
    
