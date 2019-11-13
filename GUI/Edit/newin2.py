# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Config.Init import *
import Database.wxsq as sq
import srchlist as sr

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent , lbl , btn1 , btn2 ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 579,272 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		VS1 = wx.BoxSizer( wx.VERTICAL )
		
		HSA1 = wx.BoxSizer( wx.HORIZONTAL )
		
		VS2 = wx.BoxSizer( wx.VERTICAL )
		
		HSC3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, lbl[0], wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.lbl3.Wrap( -1 )
		HSC3.Add( self.lbl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		HSC3.Add( self.fild3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.sbtn1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSC3.Add( self.sbtn1, 0, wx.ALL, 5 )
		
		self.filePic1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"فایل عکس کارمند", u"*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN )
		HSC3.Add( self.filePic1, 0, wx.ALL, 5 )
		
		
		VS2.Add( HSC3, 1, wx.EXPAND, 5 )
		
		HSC1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, lbl[1], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
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
		
		self.lbl4 = wx.StaticText( self, wx.ID_ANY, lbl[3], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl4.Wrap( -1 )
		HSC2.Add( self.lbl4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		List1Choices = self.grouplist()
		self.List1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,-1 ), List1Choices, 0 )
		self.List1.SetSelection( 0 )
		HSC2.Add( self.List1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.sbtn2 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSC2.Add( self.sbtn2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl5 = wx.StaticText( self, wx.ID_ANY, lbl[4], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl5.Wrap( -1 )
		HSC2.Add( self.lbl5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		List2Choices = self.shiftlist()
		self.List2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,-1 ), List2Choices, 0 )
		self.List2.SetSelection( 0 )
		HSC2.Add( self.List2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.sbtn3 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HSC2.Add( self.sbtn3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS2.Add( HSC2, 1, wx.EXPAND, 5 )
		
		
		HSA1.Add( VS2, 1, wx.EXPAND, 5 )
		
		HSB = wx.BoxSizer( wx.HORIZONTAL )
		
		
		HSB.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		#self.man = wx.Image("..\\employee\\Icons\\man.jpg" , wx.BITMAP_TYPE_JPEG)
		
		self.picmploy = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSB.Add( self.picmploy, 0, wx.EXPAND|wx.SHAPED, 5 )
		
		
		HSA1.Add( HSB, 1, wx.EXPAND, 5 )
		
		
		VS1.Add( HSA1, 1, wx.EXPAND, 5 )
		
		HSA2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl6 = wx.StaticText( self, wx.ID_ANY, lbl[5], wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_RIGHT )
		self.lbl6.Wrap( -1 )
		HSA2.Add( self.lbl6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA2.Add( self.fild4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl7 = wx.StaticText( self, wx.ID_ANY, lbl[6], wx.DefaultPosition, wx.Size( 60,-1 ), wx.ALIGN_RIGHT )
		self.lbl7.Wrap( -1 )
		HSA2.Add( self.lbl7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl8 = wx.StaticText( self, wx.ID_ANY, lbl[7], wx.DefaultPosition, wx.Size( 10,-1 ), wx.ALIGN_RIGHT )
		self.lbl8.Wrap( -1 )
		HSA2.Add( self.lbl8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA2.Add( self.fild5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl9 = wx.StaticText( self, wx.ID_ANY, lbl[8], wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.lbl9.Wrap( -1 )
		HSA2.Add( self.lbl9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA2.Add( self.fild6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS1.Add( HSA2, 1, wx.EXPAND, 5 )
		
		HSA3 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		HSA3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, btn1, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA3.Add( self.btn3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
				
		self.btn1 = wx.Button( self, wx.ID_ANY, btn2, wx.DefaultPosition, wx.DefaultSize, 0 )
		HSA3.Add( self.btn1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS1.Add( HSA3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( VS1 )
		self.Layout()
		
		# Connect Events
		self.sbtn1.Bind( wx.EVT_BUTTON, self.search )
		self.filePic1.Bind( wx.EVT_FILEPICKER_CHANGED, self.picfile )
		self.sbtn2.Bind( wx.EVT_BUTTON, self.Ongroup )
		self.sbtn3.Bind( wx.EVT_BUTTON, self.Onshift )
		self.btn1.Bind( wx.EVT_BUTTON, self.entry )
		self.btn3.Bind( wx.EVT_BUTTON, self.cancel)
	
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
		#print fs
		filds = self.showrecord(fs[0])
		
                #print filds
                self.employfield(filds[0])
		#gr.Layout()
		srch.Destroy()
	def showrecord(self,code):
                return sq.wxsqltxt('employee.db',"""select empfile.employid,employ.name,employ.family,empfile.groupid,
                                                    empfile.workid,empfile.picpath,empfile.empdate,empfile.tsktimein,empfile.tsktimeout
                                                    from empfile,employ
                                                    where employ.employid = %s
                                                    and empfile.employid = employ.employid
                                                  """ %code)
	def picfile( self, event ):
				
		self.Img = wx.Image(unicode(event.GetPath()), wx.BITMAP_TYPE_JPEG)
		self.bitpath = event.GetPath()
		#print self.bitpath
		#self.MaxImageSize = 300
		#print MAP
		self.picmploy.SetBitmap(wx.BitmapFromImage(self.Img))
		self.picmploy.SetSize((20,20))
		self.Refresh()
		self.Layout()
	
	def Ongroup( self, event ):
		gr = wx.Dialog(self)
		pnlgr = MyPanel3(gr)
		gr.SetSize(( 325,180 ))
		gr.ShowModal()
		self.Refresh()
		self.Layout()
	
	def Onshift( self, event ):
		sh = wx.Dialog(self)
		pnlsh = MyPanel2(sh)
		sh.SetSize(( 390,160 ))
		sh.ShowModal()
		self.Refresh()
		self.Layout()
	
	def entry( self, event ):
                f1=self.fild1.GetValue()
                f2=self.fild2.GetValue()
                f3=self.fild3.GetValue()
                f4=self.fild4.GetValue()
                f5=self.fild5.GetValue()
                f6=self.fild6.GetValue()
                #print f1,f2,f3,f4,f5,f6
                f7=self.List1.GetSelection()
                f8=self.List2.GetSelection()
                print str(f7)+' Group ',str(f8)+' Shift '
                #pic = self.picmploy.GetName()
                #pic2 = self.picmploy.GetBitmap()
                
                global MAP
                #print MAP
                #print self.bitpath.split(MAP)[1]
                
                sq.wxsqins('employee.db',' employ ',' employid , name , family ,specfid ',[f3,unicode(f1),unicode(f2),1001])
                sq.wxsqins('employee.db',' empfile',' employid , groupid , workid , empdate , tsktimein , tsktimeout , picpath'
                           ,[f3,f7,f8,f4,f5,f6,str(self.bitpath.split(MAP)[1])])
		q = self.GetParent()
                q.Close()

        

        def cancel( self, event ):
                q = self.GetParent()
                q.Close()

        def shiftlist(self):
                result = []
                slist = sq.wxsqsel('employee.db','Shifts','*')
                #print slist
                for item in slist:
                        result.append(item[1])
                return result
        def grouplist(self):
                result = []
                glist = sq.wxsqsel('employee.db','Groups','*')
                #print glist
                for item in glist:
                        result.append(item[1])
                return result
                
        def employfield(self,fs):
                global MAP
                print fs[5]
                print str(fs[3])+' Group',str(fs[4])+' Shift'
                self.fild1.SetValue(fs[1])
                self.fild2.SetValue(fs[2])
                self.fild3.SetValue(str(fs[0]))
                self.fild4.SetValue(fs[6])
                self.fild5.SetValue(fs[7])
                self.fild6.SetValue(fs[8])
                #self.List1.SetValue(fs[3])
                #self.List2.SetValue(fs[4])
                self.List1.SetSelection(int(fs[3]))
                self.List2.SetSelection(int(fs[4]))
                self.filePic1.SetPath(unicode(fs[5]))
                self.Img = wx.Image(unicode(MAP+fs[5]), wx.BITMAP_TYPE_JPEG)
                self.picmploy.SetBitmap(wx.BitmapFromImage(self.Img))
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
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 389,158 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		VS21 = wx.BoxSizer( wx.VERTICAL )
		
		HS21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"نام شیفت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		HS21.Add( self.lbl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS21.Add( self.fild1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btns = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HS21.Add( self.btns, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS21.Add( HS21, 1, wx.ALIGN_CENTER, 5 )
		
		HS22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"از ساعت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )
		HS22.Add( self.lbl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS22.Add( self.fild2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"تا ساعت", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )
		HS22.Add( self.lbl3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS22.Add( self.fild3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS21.Add( HS22, 1, wx.ALIGN_CENTER, 5 )
		
		HS23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS23.Add( self.btn3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"حذف شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS23.Add( self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"اضافه شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS23.Add( self.btn1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS21.Add( HS23, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( VS21 )
		self.Layout()
		
		# Connect Events
		self.btns.Bind( wx.EVT_BUTTON, self.srshift )
		self.btn3.Bind( wx.EVT_BUTTON, self.canelit )
		self.btn2.Bind( wx.EVT_BUTTON, self.delshift )
		self.btn1.Bind( wx.EVT_BUTTON, self.Addshift )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def srshift( self, event ):
                data = sq.wxsqsel('employee.db','Shifts','totime ,fromtime ,Shiftname')
                fild_title=[u'نام شيفت',u'از ساعت',u'تا ساعت']
		srch = wx.Dialog(self)
		pnlsr = sr.MyPanel1(srch,data,fild_title)
		srch.SetSize(( 359,384 ))
		srch.ShowModal()
		fs = pnlsr.retdata()
		#print fs
		self.fild3.SetValue(fs[0])
                self.fild2.SetValue(fs[1])
                self.fild1.SetValue(fs[2])
		self.Refresh()
		self.Layout() 
		srch.Destroy()
		
	def canelit( self, event ):
		q = self.GetParent()
                q.Close()
	def delshift( self, event ):
		q = self.GetParent()
                q.Close()
	def Addshift( self, event ):
                f1 = self.fild1.GetValue()
                f2 = self.fild2.GetValue()
                f3 = self.fild3.GetValue()

                #print type(f1),type(f2),type(f3)

                inlist = sq.wxsqins('employee.db','Shifts','shiftid,shiftname,fromtime,totime',(u'null',f1,f2,f3))
		
		self.Refresh()
		self.Layout()
	        q = self.GetParent()
                q.Close()

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

class MyPanel3 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 320,176 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		VS31 = wx.BoxSizer( wx.VERTICAL )
		
		HS31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"کد گروه", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		HS31.Add( self.lbl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS31.Add( self.fild1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btns = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		HS31.Add( self.btns, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS31.Add( HS31, 1, wx.ALIGN_CENTER, 5 )
		
		HS32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"نام گروه کاری", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )
		HS32.Add( self.lbl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.fild2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		HS32.Add( self.fild2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS31.Add( HS32, 1, wx.ALIGN_CENTER, 5 )
		
		HS33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS33.Add( self.btn3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"حذف شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS33.Add( self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"اضافه شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		HS33.Add( self.btn1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		VS31.Add( HS33, 1, wx.ALIGN_CENTER, 5 )
		
		
		self.SetSizer( VS31 )
		self.Layout()
		
		# Connect Events
		self.btns.Bind( wx.EVT_BUTTON, self.srgroup )
		self.btn3.Bind( wx.EVT_BUTTON, self.cancelit )
		self.btn2.Bind( wx.EVT_BUTTON, self.delgroup )
		self.btn1.Bind( wx.EVT_BUTTON, self.Addgroup )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def srgroup( self, event ):
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
		
	def cancelit( self, event ):
		q = self.GetParent()
                q.Close()

	def delgroup( self, event ):
		q = self.GetParent()
                q.Close()
		
	def Addgroup( self, event ):
                f1 = self.fild1.GetValue()
                f2 = self.fild2.GetValue()
               

                #print type(f1),type(f2)

                inlist = sq.wxsqins('employee.db','Groups','groupname,Groupid',(f2,f1))

                self.Refresh()
		self.Layout()
		q = self.GetParent()
                q.Close()
	
