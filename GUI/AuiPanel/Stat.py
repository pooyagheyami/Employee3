# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python
# -*- codnig: utf-8 -*-
import wx
import wx.dataview
#import Database.wxmem as mem
import Database.wxsq as sq
#import Database.wxdb as db
#from khayyam import * 
from Config.Init import *
    
class MyPanel(wx.Panel):
    def __init__(self,parent,id,pos,siz,style,ndata=[]):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 142,396 ), style = wx.TAB_TRAVERSAL )

        self.parent = parent
        self.ndata=ndata
        
        self.SetLayoutDirection(1)
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_dataViewCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_MULTIPLE|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VARIABLE_LINE_HEIGHT|wx.dataview.DV_VERT_RULES )

        self.DVCol = []
        for cloum in self.ndata:
            self.DVCol.append(self.m_dataViewCtrl1.AppendTextColumn(cloum,0))

        #self.showitem()    


        bSizer2.Add( self.m_dataViewCtrl1, 4, wx.ALL|wx.EXPAND, 5 )
        


        self.SetSizer( bSizer2 )
        self.Layout()

    def showitem(self):
        now = NOW
        mylist = sq.wxsqltxt('employee.db',"""select attend.date , employ.name , employ.family , attend.enterit , attend.exitit , Groups.groupname , Shifts.Shiftname
                                        from attend  natural join employ,Shifts,Groups
                                        
                                        on Shifts.Shiftid = attend.shiftid
                                        and Groups.Groupid = attend.groupid
                                        and attend.date = '%s' """ %now)
        for item in mylist:
                    self.m_dataViewCtrl1.AppendItem(item[::-1])
                    #self.m_dataViewCtrl1.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED,self.oncheng)
        


    def refresh(self):
        self.m_dataViewCtrl1.DeleteAllItems()
        self.m_dataViewCtrl1.Refresh()

