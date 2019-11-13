#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import edit1


class tstframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent=parent

              
        
        panel = edit1.MyPanel1(self)
        
    def closeit(self):
        
        self.Close(True)
        
        #return None
def size():
    return (561,255)


def main(panel=None):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    parent =  panel.GetParent()
    frame = tstframe(parent)
    frame.SetTitle(u'ويرايش اطلاعات')
    frame.SetSize(size())
    frame.Show()
    

    

if __name__ == '__main__':
    main()
    
    
