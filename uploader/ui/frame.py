# -*-- coding:utf-8 -*--
import wx


class MainFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 300))
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # self.CreateStatusBar()
        #
        # file_menu = wx.Menu()
        # about_menu = file_menu.Append(wx.ID_ABOUT, '&About', 'Information about this program')
        # self.Bind(wx.EVT_MENU, self.on_about, about_menu)
        # file_menu.AppendSeparator()
        # file_menu.Append(wx.ID_EXIT, 'E&xit', ' Terminate the program')
        #
        # menu_bar = wx.MenuBar()
        # menu_bar.Append(file_menu, '&File')
        # self.SetMenuBar(menu_bar)
        # self.Show(True)

    def on_about(self, event):
        dialog = wx.MessageDialog(self, 'A small editor in wxPython', 'About Sample Editor', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()
        print('hello world')

