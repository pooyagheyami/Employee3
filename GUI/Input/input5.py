# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.lib.masked as masked
from khayyam import *
import datetime
import time
import Database.wxsq2 as sq
#import srchlist as sr
import Utility.src as src
from Config.Init import *
import Database.sendgets as sg
###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent, lbl = [] , chk = '' , btn = '' ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 561,255 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		self.sndget = sg.GetData(u'',u'')
		VS1 = wx.BoxSizer( wx.VERTICAL )
		
		HSA1 = wx.BoxSizer( wx.HORIZONTAL )
		
		VS2 = wx.BoxSizer( wx.VERTICAL )
		
		HSC3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, lbl[0], wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.lbl3.Wrap( -1 )
		HSC3.Add( self.lbl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		HSC3.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )
		
		self.sbtn = wx.Button( self, wx.ID_ANY, u":::", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSC3.Add( self.sbtn, 0, wx.ALL, 5 )
		
		
		VS2.Add( HSC3, 1, wx.EXPAND, 5 )
		
		HSC1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY,lbl[1], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl1.Wrap( -1 )
		HSC1.Add( self.lbl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSC1.Add( self.fild1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl2 = wx.StaticText( self, wx.ID_ANY, lbl[2], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl2.Wrap( -1 )
		HSC1.Add( self.lbl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSC1.Add( self.fild2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS2.Add( HSC1, 1, wx.EXPAND, 5 )
		
		HSC2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, lbl[3], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl3.Wrap( -1 )
		HSC2.Add( self.lbl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSC2.Add( self.fild3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl4 = wx.StaticText( self, wx.ID_ANY, lbl[4], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl4.Wrap( -1 )
		HSC2.Add( self.lbl4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSC2.Add( self.fild4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS2.Add( HSC2, 1, wx.EXPAND, 5 )
		
		
		HSA1.Add( VS2, 1, wx.EXPAND, 5 )
		
		HSB = wx.BoxSizer( wx.HORIZONTAL )
		
		
		HSB.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.picture = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		HSB.Add( self.picture, 0, wx.EXPAND|wx.SHAPED, 5 )
		
		
		HSA1.Add( HSB, 1, wx.EXPAND, 5 )
		
		
		VS1.Add( HSA1, 1, wx.EXPAND, 5 )
		
		HSA3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl5 = wx.StaticText( self, wx.ID_ANY, lbl[5], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl5.Wrap( -1 )
		HSA3.Add( self.lbl5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		#print TODAY
		self.fild5 = wx.TextCtrl( self, wx.ID_ANY, unicode(NOW), wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA3.Add( self.fild5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.timer=wx.Timer(self)
                self.timer.Start(1000)
                self.Bind(wx.EVT_TIMER, self.OnTimer)
		
		self.lbl6 = wx.StaticText( self, wx.ID_ANY, lbl[6], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl6.Wrap( -1 )
		HSA3.Add( self.lbl6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		if btn == u'ثبت ورود':
                        self.intim = unicode(JalaliDatetime.now().strftime('%h:%r'))
                        self.outtim = ''
                elif btn ==  u'ثبت خروج':
                        self.intim = ''
                        self.outtim = unicode(JalaliDatetime.now().strftime('%h:%r'))
                        
		self.fild6 = wx.TextCtrl( self, wx.ID_ANY, self.intim, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA3.Add( self.fild6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild7 = wx.TextCtrl( self, wx.ID_ANY, self.outtim, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA3.Add( self.fild7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS1.Add( HSA3, 1, wx.EXPAND, 5 )
		
		HSA4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chklst = wx.CheckBox( self, wx.ID_ANY,chk , wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chklst.Enable( False )
		self.chklst.SetToolTipString( u"این بخش بوسیله شما خریداری نشده است" )
		
		HSA4.Add( self.chklst, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		HSA4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn = wx.Button( self, wx.ID_ANY, btn, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA4.Add( self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS1.Add( HSA4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( VS1 )
		self.Layout()
		
		# Connect Events
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.srcbtn )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT, self.dotxt )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT_ENTER, self.dotxtetr )
		self.sbtn.Bind( wx.EVT_BUTTON, self.search )
		self.btn.Bind( wx.EVT_BUTTON, self.entry )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def srcbtn( self, event ):
                data = sq.wxsqsel('employee.db','employ','employid ,family , name')
                fild_title = [u'نام',u'نام خانوادگي',u'کد پرسنل']
                siz = (190,380)
                '''
                gr = wx.Dialog(self)
		dlg = sr.MyPanel1(gr,data,fild_title)
		gr.SetSize((190,380))
		gr.ShowModal()
		fs = dlg.retdata()
		'''
                gr = src.srch(self,siz,data,fild_title)
                gr.ShowModal()
                fs = gr.backdata()
		#filds = self.showrecord(fs[0])
                filds = self.sndget.showrecord(fs[0])

		#print filds

		self.shiftid = filds[0][2]
		self.groupid = filds[0][3]

		#print filds[0]
		self.employfield(filds[0])
		
		#gr.Destroy()
	                                   
	def dotxt( self, event ):
		event.Skip()
	
	def dotxtetr( self, event ):
		event.Skip()
	
	def search( self, event ):
		dlg = MyPanel3(None)
		dlg.ShowModal()
		s = dlg.showadad()
		print s
		print dlg.GetReturnCode()
		self.m_searchCtrl1.SetValue(unicode(s))
		self.m_searchCtrl1.SetLabel(unicode(s))
		
		#print dlg.GetParentForModalDialog()
		filds = self.sndget.showrecord(s)

		#print filds[0]
		self.employfield(filds[0])
		self.Refresh()
		self.Layout()
		dlg.Destroy()

	def shent(self, event):
                print event
	
	def entry( self, event ):
		f0 = self.m_searchCtrl1.GetValue()
		f1 = self.fild1.GetValue()
		f2 = self.fild2.GetValue()
		f3 = self.fild3.GetValue()
		f4 = self.fild4.GetValue()
		f5 = self.fild5.GetValue()
		f6 = self.fild6.GetValue()
		f7 = self.fild7.GetValue()

		fs = self.sndget.gropshft(f0)
		
		tst = self.sndget.ateencod(f0)
		#print tst
		#print tst[0]
				
		if tst != [] and tst[0][0] == fs[0][0] and tst[0][1] != u' ' :
                                sq.wxsqlup('employee.db',' attend ' , " exitit = ? where attend.employid = %s and attend.date = "%f0+"'"+unicode(NOW)+"'",[f7])
                else:
                        sq.wxsqins('employee.db','attend','employid , date ,enterit , exitit , shiftid , groupid',
                                   [f0,unicode(f5),unicode(f6),unicode(f7),fs[0][2],fs[0][1]])
                #print tst[0]
                
		self.Refresh()
		self.Layout()
		q = self.GetParent()
                q.Close()

	def OnTimer(self, evt):
                #t = time.localtime(time.time())
                #st = time.strftime("%I:%M:%S", t)
                
                        
                st = unicode(JalaliDatetime.now().strftime('%h:%r'))
                if self.intim == '':
                        self.fild7.SetValue(st)
                elif self.outtim == '':
                        self.fild6.SetValue(st)
		
	def employfield(self,fs):
                global MAP
                #print MAP
                self.m_searchCtrl1.SetValue(str(fs[0]))
                self.fild1.SetValue(fs[1])
                self.fild2.SetValue(fs[2])
                self.fild3.SetValue(fs[3])
                self.fild4.SetValue(fs[4])
                self.Img = wx.Image(unicode(MAP+fs[5]), wx.BITMAP_TYPE_JPEG)
                self.picture.SetBitmap(wx.BitmapFromImage(self.Img))
                self.picture.SetSize((20,20))
                #self.List1.SetSelection(fs[2])
                #self.List2.SetSelection
                #self.picmploy
                self.Refresh()
		self.Layout()



# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

#import wx
#import wx.xrc

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 154,190 ), style = wx.TAB_TRAVERSAL )

		lbl = [u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'ثبت',u'0',u'پاک']
		gSizer1 = wx.GridSizer( 4, 3, 0, 0 )

		self.btn = []
		self.adad = ''

		for i in range(12):
                    self.btn.append( wx.Button( self, wx.ID_ANY, lbl[i], wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT ))
                    gSizer1.Add( self.btn[i], 0, wx.ALL|wx.EXPAND, 5 )
                    self.btn[i].Bind( wx.EVT_BUTTON, self.Onenter )
					
		
		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	def Onenter( self, event ):
                #print event.GetEventObject().GetLabel()
                #self.adad = self.adad + event.GetEventObject().GetLabel()
                if event.GetEventObject().GetLabel() == u'ثبت' :
                        #print self.adad
                        self.Close()
                elif  event.GetEventObject().GetLabel() == u'پاک' :
                        self.adad = ''
                        self.Close()
                else:
                        self.adad = self.adad + event.GetEventObject().GetLabel()
                     
                self.SetReturnCode(int(self.adad))
                
                        

	def showadad(self):
                return self.adad
	


