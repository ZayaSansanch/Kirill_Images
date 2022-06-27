import wx

def __init__(self, parent, title):
     self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

app = wx.App()
wnd = wx.Frame(None, wx.ID_ANY, "Coloring utility")
wnd.Show(True)
app.MainLoop()