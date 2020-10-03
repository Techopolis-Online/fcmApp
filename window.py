import wx
# this is the main window class for wx python
class UserInput(wx.Frame):
    def __init__(self, parent, title):
        super(UserInput, self).__init__(parent, title=title)

        # define the panel and the sizer for elements
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        # Add objects to left or right boxes. Labels on the left and text boxes on the right. This may change in the future ad labels and boxes are not always aligned.
        leftBox = wx.BoxSizer(wx.VERTICAL)
        rightBox = wx.BoxSizer(wx.VERTICAL)

# starting to define the GUI elements
        apiLabel = wx.StaticText(panel)
        text = "API Key:"
        apiLabel.SetLabel(text)
        leftBox.Add(apiLabel)
        apiKey = wx.TextCtrl(panel)
        text = ""
        apiKey.SetLabelText(text)
        rightBox.Add(apiKey)

        titleLabel = wx.StaticText(panel)
        text = "Notification Title:"
        titleLabel.SetLabel(text)
        leftBox.Add(titleLabel)
        notificationTitle = wx.TextCtrl(panel)
        text = "notification title:"
        notificationTitle.SetLabel(text)
        rightBox.Add(notificationTitle)

        topicLabel = wx.StaticText(panel)
        text = "Notification Topic:"
        topicLabel.SetLabel(text)
        leftBox.Add(topicLabel)
        topic = wx.TextCtrl(panel)
        text = ""
        topic.SetLabelText(text)
        rightBox.Add(topic)

        bodyLabel = wx.StaticText(panel)
        text = "Notification Body"
        bodyLabel.SetLabel(text)
        leftBox.Add(bodyLabel)
        body = wx.TextCtrl(panel,)
        text = ""
        body.SetLabel(text)
        rightBox.Add(body)

        soundLabel = wx.StaticText(panel)
        text = "Sound:"
        soundLabel.SetLabel(text)
        leftBox.Add(soundLabel)
        sound = wx.TextCtrl(panel)
        text = ""
        sound.SetLabel(text)
        rightBox.Add(sound)

        box.Add(leftBox)
        box.Add(rightBox)

        panel.SetSizer(box)




        self.Show()
if __name__ == '__main__':
    app = wx.App()
    UserInput(None, title='fcmApp')
    app.MainLoop()