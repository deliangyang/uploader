# -*-- coding:utf-8 -*--
import wx
from uploader.ui.frame import MainFrame
from uploader.ui.panel import ExamplePanel

app = wx.App(False)
frame = MainFrame(None, "HELLO WORLD")
nb = wx.Notebook(frame)
nb.AddPage(ExamplePanel(nb), "Absolute Positioning")
nb.AddPage(ExamplePanel(nb), "Page Two")
nb.AddPage(ExamplePanel(nb), "Page Three")
frame.Show()

app.MainLoop()
