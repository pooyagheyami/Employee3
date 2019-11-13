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
from khayyam import *
from datetime import * 

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent , lbl ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 520,470 ), style = wx.TAB_TRAVERSAL )

		#self.SetLayoutDirection(2)
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_BACK,  ), wx.DefaultPosition, wx.DefaultSize, wx.BU_LEFT )
		bSizer2.Add( self.m_bpButton1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_datePicker1 = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer2.Add( self.m_datePicker1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD,  ), wx.DefaultPosition, wx.DefaultSize, wx.BU_RIGHT )
		bSizer2.Add( self.m_bpButton2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"تاریخ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		self.m_dataViewCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_MULTIPLE|wx.dataview.DV_ROW_LINES|wx.dataview.DV_VARIABLE_LINE_HEIGHT|wx.dataview.DV_VERT_RULES )

		self.DVCol = []
		for cloum in lbl:
                        self.DVCol.append(self.m_dataViewCtrl1.AppendTextColumn(cloum,0))

                '''        
		self.m_dataViewColumn1 = self.m_dataViewCtrl1.AppendTextColumn( u"توضیحات", 0 )
		self.m_dataViewColumn2 = self.m_dataViewCtrl1.AppendTextColumn( u"خروج صبح", 0 )
		self.m_dataViewColumn3 = self.m_dataViewCtrl1.AppendTextColumn( u"ورود صبح", 0 )
		self.m_dataViewColumn4 = self.m_dataViewCtrl1.AppendTextColumn( u"نام خانوادگی", 0 )
		self.m_dataViewColumn5 = self.m_dataViewCtrl1.AppendTextColumn( u"نام", 0 )
		self.m_dataViewColumn6 = self.m_dataViewCtrl1.AppendTextColumn( u"شماره عضویت", 0 )
                '''

		bSizer4.Add( self.m_dataViewCtrl1, 4, wx.ALL|wx.EXPAND, 5 )

		self.day = JalaliDatetime.now().strftime('%N/%P/%K')
		#print self.day

                mylist = sq.wxsqltxt('employee.db',"""select  employ.name , employ.family , attend.enterit , attend.exitit , Groups.groupname , Shifts.Shiftname
                                        from attend  natural join employ,Shifts,Groups
                                        
                                        on Shifts.Shiftid = attend.shiftid
                                        and Groups.Groupid = attend.groupid
                                        and attend.date = '%s'
                                        """ %self.day)

                

                for item in mylist:
                    self.m_dataViewCtrl1.AppendItem(item[::-1])
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"تائید", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"ارسال به فایل اکسل", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_checkBox1.Enable( False )

		bSizer3.Add( self.m_checkBox1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		# Connect Events
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.OnFor )
		self.m_bpButton2.Bind( wx.EVT_BUTTON, self.OnBck )
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnCanel )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnOkey )
		self.m_datePicker1.Bind( wx.EVT_DATE_CHANGED, self.Ondate )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnBck( self, event ):
		f5 = self.m_datePicker1.GetValue()
		
		self.m_datePicker1.SetValue(f5-wx.DateSpan(days=1))
		self.myday = self.m_datePicker1.GetValue()
		inout = self.showrecord(self.getjalali(self.myday))
                #print inout
                self.employfield(inout)

	
	def OnFor( self, event ):
		f5 = self.m_datePicker1.GetValue()
		
		self.m_datePicker1.SetValue(f5+wx.DateSpan(days=1))
		self.myday = self.m_datePicker1.GetValue()
		inout = self.showrecord(self.getjalali(self.myday))
                #print inout
                self.employfield(inout)

		
		
	
	def OnCanel( self, event ):
		q = self.GetParent()
                q.Close()
	
	def OnOkey( self, event ):
		q = self.GetParent()
                q.Close()
	def Ondate( self, event ):
                f5 = self.m_datePicker1.GetValue()               #.strftime('%Y-%M-%D')
                self.myday = JalaliDatetime( date(int(f5.FormatISODate()[:4]),
                                                  int(f5.FormatISODate()[5:7]),
                                                  int(f5.FormatISODate()[8:10]))).strftime('%N/%P/%K')
                
                #print self.myday
                inout = self.showrecord(self.myday)
                #print inout
                self.employfield(inout)
                #self.fild6.SetValue(inout[0][2])
                #self.fild7.SetValue(inout[0][3])
                #self.thisdate=JalaliDatetime()
		#event.Skip()
                
        def getjalali(self,f5):
                return JalaliDatetime( date(int(f5.FormatISODate()[:4]),
                                                  int(f5.FormatISODate()[5:7]),
                                                  int(f5.FormatISODate()[8:10]))).strftime('%N/%P/%K')
            

        def employfield(self,data):
                global MAP
                #print MAP
                self.m_dataViewCtrl1.DeleteAllItems()
                self.m_dataViewCtrl1.Refresh()
                

                #print fs
                for item in data:
                        self.m_dataViewCtrl1.AppendItem(item[::-1])
                        
               
                self.Refresh()
		self.Layout()

	def showrecord(self,myday):
            #print myday
            return sq.wxsqltxt('employee.db',"""select  employ.name , employ.family , attend.enterit , attend.exitit , Groups.groupname , Shifts.Shiftname
                                        from attend  natural join employ,Shifts,Groups
                                        
                                        on Shifts.Shiftid = attend.shiftid
                                        and Groups.Groupid = attend.groupid
                                        and attend.date = '%s'
                                        """ %myday )
        

