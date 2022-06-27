import wx
 
class Window(wx.Frame):
    def __init__(self, title):
        super().__init__(parent = None, title = title)
        self.panel = wx.Panel(self)
 
        self.Show()
         
app = wx.App()
window = Window("Coloring utility")
app.MainLoop()