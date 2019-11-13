#In the name of God
# -*- coding: cp1256 -*-
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import srchlist as sr


class srch(wx.Dialog):
    def __init__(self,parent,siz,data,fild_title):
        wx.Dialog.__init__(self,parent)
        self.parent = parent

        self.pnl = sr.MyPanel1(self,data,fild_title)
        self.SetSize(siz)

    def backdata(self):
        return self.pnl.retdata()

        

            
