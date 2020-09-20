import wx
# this is the main window class for wx python
class UserInput(wx.Frame):
    def __init__(self, parent, title):
        super(UserInput, self).__init__(parent, title=title)

        # define the panel and the sizer for elements
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)


# starting to define the GUI elements
        apiKey = wx.TextCtrl(panel)
        text = "please type your API key:"
        apiKey.SetLabelText(text)
        box.Add(apiKey)

        notificationTitle = wx.TextCtrl(panel)
        text = "notification title:"
        notificationTitle.SetLabel(text)
        box.Add(notificationTitle)

        topic = wx.TextCtrl(panel)
        text = "topic:"
        topic.SetLabelText(text)
        box.Add(topic)

        body = wx.TextCtrl(panel,)
        text = "body:"
        body.SetLabel(text)
        box.Add(body)

        sound = wx.TextCtrl(panel)
        text = "sound:"
        sound.SetLabel(text)




        panel.SetSizer(box)




        self.Show()
if __name__ == '__main__':
    app = wx.App()
    UserInput(None, title='fcmApp')
    app.MainLoop()