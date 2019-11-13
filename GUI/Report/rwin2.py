# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import Database.wxsq as sq

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent,lbl ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 768,293 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_dataViewCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_MULTIPLE|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VARIABLE_LINE_HEIGHT|wx.dataview.DV_VERT_RULES )

                self.DVCol = []
		for cloum in lbl:
                        self.DVCol.append(self.m_dataViewCtrl1.AppendTextColumn(cloum,0))

		'''
		self.m_dataViewColumn1 = self.m_dataViewCtrl1.AppendTextColumn( u"توضیحات", 0 )
		self.m_dataViewColumn2 = self.m_dataViewCtrl1.AppendTextColumn( u"خروج عصر", 0 )
		self.m_dataViewColumn3 = self.m_dataViewCtrl1.AppendTextColumn( u"ورود عصر", 0 )
		self.m_dataViewColumn4 = self.m_dataViewCtrl1.AppendTextColumn( u"خروج صبح", 0 )
		self.m_dataViewColumn5 = self.m_dataViewCtrl1.AppendTextColumn( u"ورود صبح", 0 )
		self.m_dataViewColumn6 = self.m_dataViewCtrl1.AppendDateColumn( u"تاریخ", 0 )
		self.m_dataViewColumn7 = self.m_dataViewCtrl1.AppendTextColumn( u"نام خانوادگی", 0 )
		self.m_dataViewColumn8 = self.m_dataViewCtrl1.AppendTextColumn( u"نام", 0 )
		self.m_dataViewColumn9 = self.m_dataViewCtrl1.AppendTextColumn( u"شماره عضویت", 0 )
		'''
		bSizer4.Add( self.m_dataViewCtrl1, 4, wx.ALL|wx.EXPAND, 5 )

		#mylist = sq.wxsqsel('employee.db','attend ,employ ','*','')
		mylist = sq.wxsqltxt('employee.db',"""select attend.date , employ.name , employ.family , attend.enterit , attend.exitit , Groups.groupname , Shifts.Shiftname
                                        from attend,employ,Shifts,Groups
                                        where employ.employid = attend.employid
                                        and Shifts.Shiftid = attend.shiftid
                                        and Groups.Groupid = attend.groupid """)
		
		#print mylist
		for item in mylist:
                    self.m_dataViewCtrl1.AppendItem(item[::-1])
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
	
	def __del__( self ):
		pass
	

