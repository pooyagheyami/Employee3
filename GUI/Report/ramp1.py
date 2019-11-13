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
from khayyam import *
import Database.wxsq as sq
import srchlist as sr
from Config.Init import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 393,464 ), style = wx.TAB_TRAVERSAL )
		
                self.SetLayoutDirection(2)
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"کد پرسنل", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer2.Add( self.m_searchCtrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u":::", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer2.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"نام", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"نام خانوادگی ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer4.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.SetLayoutDirection(1)
		
		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		'''
		self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn( u"تاریخ" )
		self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"ورود" )
		self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"خروج" )
		self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn( u"توضیحات" )
		'''
		
		self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendTextColumn( u"توضیحات" )
		self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"خروج" )
		self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"ورود" )
		self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn( u"تاریخ" )
		self.m_dataViewListColumn5 = self.m_dataViewListCtrl1.AppendTextColumn( u"روزهفته" )
		bSizer3.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 5, wx.EXPAND, 5 )

		self.SetLayoutDirection(2)
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1OK.SetLabel(u'تائيد')
		
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		self.m_sdbSizer1Cancel.SetLabel(u'انصراف')
		
		m_sdbSizer1.Realize();
		
		bSizer1.Add( m_sdbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.onsrch )
		self.m_button1.Bind( wx.EVT_BUTTON, self.onpad )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.OnOkey )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onsrch( self, event ):
		data = sq.wxsqsel('employee.db','employ','employid ,family , name')
                fild_title = [u'نام',u'نام خانوادگي',u'کد پرسنل']

                gr = wx.Dialog(self)
		dlg = sr.MyPanel1(gr,data,fild_title)
		gr.SetSize((190,380))
		gr.ShowModal()
		self.fs = dlg.retdata()
		
		self.filds = self.showrecord(self.fs[0])

		for  f in range(len(self.filds)):
                        d=self.filds[f][0].split('/')
                        dayname = JalaliDate(int(d[0]),int(d[1]),int(d[2])).strftime('%A')
                        self.filds[f] = (dayname,)+self.filds[f]
                        
		
		self.employfield(self.filds)
		
		gr.Destroy()
	def showrecord(self,code):
                return sq.wxsqltxt('employee.db',"""select distinct attend.date,attend.enterit,attend.exitit,empfile.tsktimeout
                                                    from attend,empfile
                                                    where attend.employid = empfile.employid
                                                    and attend.employid = %s
                                                    
                                                  """ %code)
	
	def onpad( self, event ):
		event.Skip()

	def employfield(self,data):
                global MAP
                #print MAP
                self.m_dataViewListCtrl1.DeleteAllItems()
                self.m_dataViewListCtrl1.Refresh()
                self.m_searchCtrl1.SetValue(self.fs[0])
                self.m_textCtrl1.SetValue(self.fs[2])
                self.m_textCtrl2.SetValue(self.fs[1])

                #print fs
                for item in data:
                        self.m_dataViewListCtrl1.AppendItem(item[::-1])
                        
               
                self.Refresh()
		self.Layout()

	def OnCancel( self, event ):
		q = self.GetParent()
                q.Close()
	
	def OnOkey( self, event ):
		q = self.GetParent()
                q.Close()	
	

