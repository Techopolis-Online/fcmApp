import wx

class Window(wx.Frame):
    def __init__(self, parent, title):
        super(Window, self).__init__(parent, title=title)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Window(None, title='fcmApp')
    app.MainLoop()