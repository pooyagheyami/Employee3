#In the name of God
# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import input5


class tstframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent=parent

        

        lbl =  [u'شماره عضويت:',u'نام:',u'نام خانوادگي:',u'گروه:',u'شيفت:',u' تاريخ امروز:',u'ورود و خروج:']
        chk = u'در لیست حقوق ثبت شود'
        btn = u'ثبت ورود'

        
        
        panel = input5.MyPanel1(self,lbl,chk,btn)
        
    def closeit(self):
        
        self.Close(True)
        
        #return None
def size():
    return (565,255)


def main(panel=None):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    parent =  panel.GetParent()
    frame = tstframe(parent)
    frame.SetTitle(u'ورود اطلاعات')
    frame.SetSize(size())
    frame.Show()
    

    

if __name__ == '__main__':
    main()
    
    
