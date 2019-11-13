# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import Database.wxsq as sq

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 587,287 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer5.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_Item = []
		self.m_choice2 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.m_Item, 0 )
		self.m_choice2.SetSelection( 0 )
		
		bSizer5.Add( self.m_choice2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"ایتمها", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer5.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button2 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer5.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_Bar = []
		self.data = sq.wxsqsel('Menu.db','menubar','*')
                for i in range(len(self.data)):
                        self.m_Bar.append(self.data[i][1])
                print self.data        
                        
		self.m_choice1 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.m_Bar, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer5.Add( self.m_choice1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"منوبار اصلی", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer5.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"نام برنامه", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer7.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_dirPicker1 = wx.DirPickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer7.Add( self.m_dirPicker1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"نام دایرکتوری", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer7.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		m_choice4Choices = []
		self.m_choice4 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		self.m_choice4.Enable( False )
		
		bSizer8.Add( self.m_choice4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"برای کاربر", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.Enable( False )
		
		bSizer8.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice3Choices = []
		self.m_choice3 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		self.m_choice3.Enable( False )
		
		bSizer8.Add( self.m_choice3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"مد نمایش", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.Enable( False )
		
		bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"تذکر: بعد از اعمال تغییرات لازم است نرم افزار بسته و مجدد راه اندازی شود تا تغییرات اعمال شده مورد استفاده واقع گردد ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer10.Add( self.m_staticText7, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"تعریف ظاهر برنامه", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button7 = wx.Button( self.m_panel2, wx.ID_ANY, u"جدول جدید", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"جدول کاری", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer11.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel2, wx.ID_ANY, u"شیفت جدید", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"شیفت کاری", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer11.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.m_panel2, wx.ID_ANY, u"گروه جدید", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"گروه کاری", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer11.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel2.SetLayoutDirection(1)
		self.m_checkBox1 = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"نمایش پنجره ساعت و تقویم در برنامه", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_checkBox1.SetValue(True) 
		bSizer12.Add( self.m_checkBox1, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"نمایش وضعیت عملکرد جاری در پائین برنامه", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_checkBox2.SetValue(True) 
		bSizer12.Add( self.m_checkBox2, 0, wx.ALIGN_CENTER|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_checkBox3 = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"نمایش ورود اطلاعات در بخش راست برنامه", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_checkBox3.SetValue(True) 
		bSizer12.Add( self.m_checkBox3, 0, wx.ALIGN_CENTER|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer12.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer13.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"تذکر: بعد از اعمال تغییرات لازم است نرم افزار بسته و مجدد راه اندازی شود تا تغییرات اعمال شده مورد استفاده واقع گردد ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer13.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"تعریف پارامترهای داخلی", False )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"تعریف حسابهای اصلی و متقابل", True )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"اعمال شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()

		

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnItem )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnmBar )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.OnBar )
		self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnDir )
		self.m_button7.Bind( wx.EVT_BUTTON, self.NWork )
		self.m_button6.Bind( wx.EVT_BUTTON, self.NShif )
		self.m_button5.Bind( wx.EVT_BUTTON, self.NGroup )
		self.m_button3.Bind( wx.EVT_BUTTON, self.Oncancel )
		self.m_button4.Bind( wx.EVT_BUTTON, self.Onapply )
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def OnItem( self, event ):
		event.Skip()
	
	def OnmBar( self, event ):
		event.Skip()

	def OnBar( self, event ):
                #print event.GetEventObject().GetSelection()
                #print event.GetEventObject().GetString()
                #print event.GetEventObject().GetStringSelection()
                s = event.GetEventObject().GetStringSelection()
                for ibar in self.data:
                        if unicode(s) in ibar:
                                bar = ibar[0]
                                
                self.m_Item = []
                self.m_Item = self.Litem(bar)
                #print self.m_Item
                self.m_choice2.SetItems(self.m_Item)
                self.Refresh()
		self.Layout()
		
        def Litem( self , bar ):
                data = sq.wxsqltxt('Menu.db',"""select distinct mitem.itemname
                                                from mitem
                                                where mitem.mbarid=%s
                                                """%bar)
                result = []
		
                for i in range(len(data)):
                        if data[i][0] != None:
                                result.append(data[i][0])

                return result
                
	
	def OnDir( self, event ):
		event.Skip()
	
	def NWork( self, event ):
		event.Skip()
	
	def NShif( self, event ):
		event.Skip()
	
	def NGroup( self, event ):
		event.Skip()
	
	def Oncancel( self, event ):
		q = self.GetParent()
                q.Close()
	
	def Onapply( self, event ):
		q = self.GetParent()
                q.Close()
	
	

