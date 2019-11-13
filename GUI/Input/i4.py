#In the name of God

# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import newin4


class tstframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent=parent

        lbl = [u"کد پرسنل",u"مسیر عکس",u"نام:",u"نام خانوادگی",u"گروه کاری"
               ,u"جدول کاری",u"ip فعالیت",u"مشخصات پرسنلی",u"مشخصات استخدامی"]
        btn1 = u"انصراف"
        btn2 = u"ثبت نام"
        
        panel = newin4.MyPanel1(self,lbl,btn1,btn2)
        
    def closeit(self):
        
        self.Close(True)
        
        #return None
def size():
    return (580,280)


def main(panel=None):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)

    parent =  panel.GetParent()
    
    frame = tstframe(parent)
    frame.SetTitle(u'اعضاء جديد')
    frame.SetSize(size())
    frame.Show()
    

    

if __name__ == '__main__':
    main()
    
    
