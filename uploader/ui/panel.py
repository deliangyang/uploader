# -*-- coding:utf-8 -*--
import wx

import wx


class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        import_excel = wx.BoxSizer(wx.HORIZONTAL)
        self.logger = wx.TextCtrl(self, size=(120, 30))
        self.btn_open_excel = wx.Button(self, label='导入Excel')
        import_excel.Add(self.logger, proportion=0, flag=wx.EXPAND, border=10, userData=None)
        import_excel.Add((10, 10), proportion=0, flag=wx.EXPAND, border=10, userData=None)
        import_excel.Add(self.btn_open_excel, proportion=0, flag=wx.EXPAND, border=10, userData=None)
        mainSizer.Add(import_excel, proportion=0, flag=wx.TOP, border=10, userData=None)
        self.SetSizer(mainSizer)


    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())

    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())

    def OnClick(self, event):
        self.logger.AppendText(" Click on object with Id %d\n" % event.GetId())

    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())

    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()

    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())
