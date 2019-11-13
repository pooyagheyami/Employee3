#In the name of God
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import newin2


class tstframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent=parent

        lbl = [u"شماره عضویت",u"نام:",u"نام خانوادگی",u"گروه کاری",u"شیفت کاری"
               ,u"تاریخ استخدام",u"ساعت کاری",u"از",u"تا"]
        btn1 = u"انصراف"
        btn2 = u"حذف ثبت"


              
        
        panel = newin2.MyPanel1(self,lbl,btn1,btn2)
        
    def closeit(self):
        
        self.Close(True)
        
        #return None
def size():
    return (580,280)


def main(panel=None):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    parent =  panel.GetParent()
    frame = tstframe(parent)
    frame.SetTitle(u'ويرايش اطلاعات')
    frame.SetSize(size())
    frame.Show()
    

    

if __name__ == '__main__':
    main()
    
    
