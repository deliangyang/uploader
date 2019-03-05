# -*-- coding:utf-8 -*--
import wx
from uploader.ui.frame import MainFrame

app = wx.App(False)
frame = MainFrame(None, "HELLO WORLD")

app.MainLoop()
