# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent , txt ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.TAB_TRAVERSAL )

		self.SetLayoutDirection(2)
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, txt, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE  )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 7, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"تائید", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Okey )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Okey( self, event ):
                
                import GUI.proman as pro
                a = pro.DoProgram(1001)
                #print dir(a)
                s = a.size() if 'size' in dir(a) else ()
                win1 = wx.Frame(self,-1)
                win1.SetSize(s)
                a.main(win1)
                
                                                
		#q = self.GetParent()
                #q.Close()
	
