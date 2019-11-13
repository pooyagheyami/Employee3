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
import wx.grid
from Config.Init import *
import Database.wxsq as sq
import Utility.srchlist as sr
import Database.sendgets as sg
from Utility.lanip import *


###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent , lbl , btn1 , btn2 ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 563,228 ), style = wx.TAB_TRAVERSAL )


                self.SetLayoutDirection(2)    
		self.sndget = sg.GetData(u'',u'')
		
		VS1 = wx.BoxSizer( wx.VERTICAL )
		
		HSA1 = wx.BoxSizer( wx.HORIZONTAL )
		
		VS2 = wx.BoxSizer( wx.VERTICAL )
		
		HSC3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, lbl[0], wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.lbl3.Wrap( -1 )
		HSC3.Add( self.lbl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		HSC3.Add( self.fild3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.sbtn1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSC3.Add( self.sbtn1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl35 = wx.StaticText( self, wx.ID_ANY, lbl[1], wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_RIGHT )
		self.lbl35.Wrap( -1 )
		HSC3.Add( self.lbl35, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.filePic1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"فایل عکس کارمند", u"*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		HSC3.Add( self.filePic1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS2.Add( HSC3, 1, wx.EXPAND, 5 )
		
		HSC1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, lbl[2], wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.lbl1.Wrap( -1 )
		HSC1.Add( self.lbl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSC1.Add( self.fild1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl2 = wx.StaticText( self, wx.ID_ANY, lbl[3], wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT )
		self.lbl2.Wrap( -1 )
		HSC1.Add( self.lbl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSC1.Add( self.fild2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS2.Add( HSC1, 1, wx.EXPAND, 5 )
		
		HSC2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl4 = wx.StaticText( self, wx.ID_ANY, lbl[4], wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.lbl4.Wrap( -1 )
		HSC2.Add( self.lbl4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		List1Choices = self.grouplist()
		self.List1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), List1Choices, 0 )
		self.List1.SetSelection( 0 )
		HSC2.Add( self.List1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.sbtn2 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSC2.Add( self.sbtn2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl5 = wx.StaticText( self, wx.ID_ANY, lbl[5], wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
		self.lbl5.Wrap( -1 )
		HSC2.Add( self.lbl5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		List2Choices = []
		self.List2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), List2Choices, 0 )
		self.List2.SetSelection( 0 )
		HSC2.Add( self.List2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS2.Add( HSC2, 1, wx.EXPAND, 5 )
		
		
		HSA1.Add( VS2, 1, wx.EXPAND, 5 )
		
		HSB = wx.BoxSizer( wx.HORIZONTAL )
		
		
		HSB.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.picmploy = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 20,20 ), wx.DOUBLE_BORDER )
		HSB.Add( self.picmploy, 0, wx.SHAPED|wx.EXPAND, 5 )
		
		
		HSA1.Add( HSB, 1, wx.EXPAND, 5 )
		
		
		VS1.Add( HSA1, 1, wx.EXPAND, 5 )
		
		HSA2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl6 = wx.StaticText( self, wx.ID_ANY, lbl[6], wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.lbl6.Wrap( -1 )
		HSA2.Add( self.lbl6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		HSA2.Add( self.fild4, 0, wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.sbtn3 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSA2.Add( self.sbtn3, 0, wx.ALL, 5 )
		
		self.lbl7 = wx.StaticText( self, wx.ID_ANY, lbl[7], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl7.Wrap( -1 )
		HSA2.Add( self.lbl7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.sbtn4 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSA2.Add( self.sbtn4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl8 = wx.StaticText( self, wx.ID_ANY, lbl[8], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl8.Wrap( -1 )
		HSA2.Add( self.lbl8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.sbtn5 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSA2.Add( self.sbtn5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS1.Add( HSA2, 0, wx.EXPAND, 5 )
		
		HSA3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"ثبت در لیست حقوق", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_checkBox1.Enable( False )
		HSA3.Add( self.m_checkBox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		HSA3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, btn1, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA3.Add( self.btn3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, btn2, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA3.Add( self.btn1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS1.Add( HSA3, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( VS1 )
		self.Layout()
		
		# Connect Events
		self.sbtn1.Bind( wx.EVT_BUTTON, self.search )
		self.filePic1.Bind( wx.EVT_FILEPICKER_CHANGED, self.picfile )
		self.sbtn2.Bind( wx.EVT_BUTTON, self.Ongroup )
		self.sbtn3.Bind( wx.EVT_BUTTON, self.iplist )
		self.sbtn4.Bind( wx.EVT_BUTTON, self.finger )
		self.sbtn5.Bind( wx.EVT_BUTTON, self.othersp )
		self.btn3.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn1.Bind( wx.EVT_BUTTON, self.entry )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def search( self, event ):
		data = sq.wxsqsel('employee.db','employ','employid ,family , name')
                fild_title = [u'نام',u'نام خانوادگي',u'کد پرسنل']
		srch = wx.Dialog(self)
		pnlsr = sr.MyPanel1(srch,data,fild_title)
		srch.SetSize(( 259,384 ))
		srch.ShowModal()
		fs = pnlsr.retdata()

		filds = self.sndget.showrecord(fs[0])

		self.employfield(filds[0])

		srch.Destroy()
	
	def picfile( self, event ):
		self.Img = wx.Image(unicode(event.GetPath()), wx.BITMAP_TYPE_JPEG)
		self.bitpath = event.GetPath()
		#self.MaxImageSize = 300
		self.picmploy.SetBitmap(wx.BitmapFromImage(self.Img))
		self.picmploy.SetSize((20,20))
		self.Refresh()
		self.Layout()
	
	def Ongroup( self, event ):
		gr = wx.Dialog(self)
		pnlgr = MyPanel2(gr)
		gr.SetSize(( 325,180 ))
		gr.ShowModal()
		self.Refresh()
		self.Layout()
		
	def iplist( self, event ):
		ip = wx.Dialog(self)
		pnlip = MyPanel3(ip)
		ip.SetSize(( 225,270 ))
		ip.ShowModal()
		ips = pnlip.retdata()
		print ips
		self.fild4.SetValue(ips[0])
		self.Refresh()
		self.Layout()
		
	def finger( self, event ):
		dg = wx.Dialog(self)
		txt1 = [u"کد پرسنل",u"<کد>",u"<نام>",u"<نام خانوادگی>",u"مشخصات فردی/پرسنلی "]
		pnlgr = MyPanel4(dg,txt1)
		dg.SetSize(( 307,300 ))
		dg.ShowModal()
		self.Refresh()
		self.Layout()
	
	def othersp( self, event ):
		dg = wx.Dialog(self)
		txt2 = [u"کد پرسنل",u"<کد>",u"<نام>",u"<نام خانوادگی>",u"مشخصات استخدامي/کاري"]
		pnlgr = MyPanel4(dg,txt2)
		dg.SetSize(( 307,300 ))
		dg.ShowModal()
		self.Refresh()
		self.Layout()
		
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	def entry( self, event ):
		q = self.GetParent()
                q.Close()
	def grouplist(self):
                result = []
                glist = self.sndget.groplist()
                for item in glist:
                        result.append(item[1])
                return result
        def employfield(self,fs):
                global MAP
                #print MAP
                #print str(fs[3])+' Group',str(fs[4])+' Shift'
                self.fild1.SetValue(fs[1])
                self.fild2.SetValue(fs[2])
                self.fild3.SetValue(str(fs[0]))
                #self.fild4.SetValue(fs[6])
                #self.fild5.SetValue(fs[7])
                #self.fild6.SetValue(fs[8])
                #self.List1.SetValue(fs[3])
                #self.List2.SetValue(fs[4])
                #self.List1.SetSelection(fs[3])
                #self.List2.SetSelection(fs[4])
                self.filePic1.SetPath(unicode(fs[5]))
                self.Img = wx.Image(unicode(MAP+fs[5]), wx.BITMAP_TYPE_JPEG)
                
                self.picmploy.SetBitmap(wx.BitmapFromImage(self.Img))
                #self.picmploy
                self.Refresh()
		self.Layout()
		

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 280,165 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		VS21 = wx.BoxSizer( wx.VERTICAL )
		
		Hs21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text21 = wx.StaticText( self, wx.ID_ANY, u"کد گروه کاری", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		self.Text21.Wrap( -1 )
		Hs21.Add( self.Text21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs21.Add( self.fld21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnsrch = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		Hs21.Add( self.btnsrch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS21.Add( Hs21, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Hs22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text22 = wx.StaticText( self, wx.ID_ANY, u"نام گروه کاری", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		self.Text22.Wrap( -1 )
		Hs22.Add( self.Text22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs22.Add( self.fld22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS21.Add( Hs22, 1, wx.EXPAND, 5 )
		
		Hs23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs23.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"اصلاح", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs23.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"انتخاب", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs23.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS21.Add( Hs23, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( VS21 )
		self.Layout()
		
		# Connect Events
		self.btnsrch.Bind( wx.EVT_BUTTON, self.srchit )
		self.btn1.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn2.Bind( wx.EVT_BUTTON, self.editit )
		self.btn3.Bind( wx.EVT_BUTTON, self.slctit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def srchit( self, event ):
		data = sq.wxsqsel('employee.db','Groups','groupname,Groupid  ')
                fild_title=[u'کد گروه',u'نام گروه']
		srch = wx.Dialog(self)
		pnlsr = sr.MyPanel1(srch,data,fild_title)
		srch.SetSize(( 259,384 ))
		srch.ShowModal()
		fs = pnlsr.retdata()
		
                self.fild2.SetValue(fs[0])
                self.fild1.SetValue(fs[1])
                
		self.Refresh()
		self.Layout() 
		srch.Destroy()
	
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	
	def editit( self, event ):
		q = self.GetParent()
                q.Close()
	
	def slctit( self, event ):
		q = self.GetParent()
                q.Close()
	

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 225,270 ), style = wx.TAB_TRAVERSAL )

		#self.SetLayoutDirection(2)
		count = 0
		t = testlan(u'192.168.1.1',u'192.168.1.20',80)
		VS31 = wx.BoxSizer( wx.VERTICAL )
		
		Hs31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text31 = wx.StaticText( self, wx.ID_ANY, u"انتخاب لیست کامپوترهای فعال", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text31.Wrap( -1 )
		Hs31.Add( self.Text31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS31.Add( Hs31, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		Hs32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.DVLC1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Col1 = self.DVLC1.AppendTextColumn( u"Name" )
		self.Col2 = self.DVLC1.AppendTextColumn( u"ip" )
		self.Col3 = self.DVLC1.AppendTextColumn( u"mac" )
		Hs32.Add( self.DVLC1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		#MessageBox(u'چند لحظه صبر کنيد تا شبکه بررسي شود',u'waiting',OK | ICON_WARNING)
		#MessageBox(u'چند لحظه صبر کنيد تا شبکه بررسي شود',u'waiting')
		#self.OnButton()
		
		dlg = wx.ProgressDialog(u"در حال بررسي",u"بررسي آي پي هاي موجود در شبکه",maximum= 95,style=0|wx.PD_CAN_ABORT
                                  |wx.PD_ESTIMATED_TIME|wx.PD_REMAINING_TIME)
		count += 10
		dlg.Update(count)

		wx.MilliSleep(250)
		count = 36
		dlg.Update(count)
		wx.Yield()
		count = 54
		dlg.Update(count)


		p = t.run(u'192.168.1.1',u'192.168.1.20')
		count = 95
		dlg.Update(count)
		#print p

		dlg.Destroy()

		for itemvalues in p:
                        self.DVLC1.AppendItem(itemvalues)
                        
		
		VS31.Add( Hs32, 1, wx.EXPAND, 5 )
		
		Hs33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs33.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انتخاب", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs33.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		VS31.Add( Hs33, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( VS31 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.onselect1, id = wx.ID_ANY )
		
		self.btn1.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn2.Bind( wx.EVT_BUTTON, self.selct )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	
	def selct( self, event ):
		event.Skip()

	def onselect1( self, event ):
		
		a= self.DVLC1.GetSelectedRow()
		#print a
		#print self.dVLCtrl1.GetTextValue(a,0)
		#print self.dVLCtrl1.GetTextValue(a,1)
		self.retdata()
		q = self.GetParent()
                q.Close()	
	def retdata(self):
                r = self.DVLC1.GetSelectedRow()
                data = []
                #print self.Col1
                #print self.Col2
                #print self.Col3
                
                data.append( unicode(self.DVLC1.GetValue(r,1)) )
                return data
        

###########################################################################
## Class MyPanel4
###########################################################################

class MyPanel4 ( wx.Panel ):
	
	def __init__( self, parent , txt ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 307,300 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		Vs41 = wx.BoxSizer( wx.VERTICAL )
		
		Hs41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text41 = wx.StaticText( self, wx.ID_ANY, txt[0], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text41.Wrap( -1 )
		Hs41.Add( self.Text41, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Text42 = wx.StaticText( self, wx.ID_ANY, txt[1], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text42.Wrap( -1 )
		Hs41.Add( self.Text42, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Text43 = wx.StaticText( self, wx.ID_ANY, txt[2], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text43.Wrap( -1 )
		Hs41.Add( self.Text43, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Text44 = wx.StaticText( self, wx.ID_ANY, txt[3], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text44.Wrap( -1 )
		Hs41.Add( self.Text44, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vs41.Add( Hs41, 1, wx.EXPAND, 5 )
		
		Hs42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Text45 = wx.StaticText( self, wx.ID_ANY, txt[4], wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text45.Wrap( -1 )
		Hs42.Add( self.Text45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vs41.Add( Hs42, 1, wx.EXPAND, 5 )
		
		Hs43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 5, 2 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.SetColSize( 0, 95 )
		self.m_grid1.SetColSize( 1, 171 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"عنوان" )
		self.m_grid1.SetColLabelValue( 1, u"مشخصه" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 19 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		Hs43.Add( self.m_grid1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vs41.Add( Hs43, 1, wx.EXPAND, 5 )
		
		Hs44 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"عنوان جدید", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs44.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs44.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"ثبت شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hs44.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		Vs41.Add( Hs44, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( Vs41 )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.newtit )
		self.btn2.Bind( wx.EVT_BUTTON, self.cancl )
		self.btn3.Bind( wx.EVT_BUTTON, self.savit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def newtit( self, event ):
		pass
	
	def cancl( self, event ):
		q = self.GetParent()
                q.Close()
	
	def savit( self, event ):
		q = self.GetParent()
                q.Close()
	

