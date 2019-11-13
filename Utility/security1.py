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
## Class MyDialog1
###########################################################################

class Secret ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 271,151 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetLayoutDirection(2)
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"نام کاربر", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txt1.Wrap( -1 )
		bSizer2.Add( self.txt1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.user = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.user, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"کلمه عبور", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txt2.Wrap( -1 )
		bSizer3.Add( self.txt2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.passw = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer3.Add( self.passw, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		choice = wx.StdDialogButtonSizer()
		self.choiceOK = wx.Button( self, wx.ID_OK )
		choice.AddButton( self.choiceOK )
		self.choiceOK.SetLabel(u"تائيد")
		
		self.choiceCancel = wx.Button( self, wx.ID_CANCEL )
		choice.AddButton( self.choiceCancel )
		self.choiceCancel.SetLabel(u"انصراف")
		choice.Realize();
		
		bSizer1.Add( choice, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def back( self ):
                v=[]
                v.append(self.user.GetValue())
                v.append(self.passw.GetValue())
                #print v
                return v
		#pass
	

