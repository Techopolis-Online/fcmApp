# this is the main window class for wx python
import wx
from pyfcm import FCMNotification

def push_to_topic(key, topic, title, body, sound):
    push_service = FCMNotification(api_key=key)
    result = push_service.notify_topic_subscribers(topic_name=topic, message_body=body, message_title=title, sound=sound)
    return result

class UserInput(wx.Frame):
    def __init__(self, parent, title):
        super(UserInput, self).__init__(parent, title=title)

        def onSubmitClicked(event):
            print(body.Value)
            result = push_to_topic(key=apiKey.Value, topic=topic.Value, title=notificationTitle.Value, body=body.Value, sound=sound.Value)
            dialog = wx.MessageDialog(None, "Push sent with the following result." + str(result), "Message result", wx.OK | wx.ICON_INFORMATION )
            dialog.ShowModal()

        # define the panel and the sizer for elements
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)


# starting to define the GUI elements
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        apilabel = wx.StaticText(panel)
        text = "API Key"
        apilabel.SetLabelText(text)
        box.Add(apilabel)
        apiKey = wx.TextCtrl(panel)
        apiToolTip = wx.ToolTip("FCM API Key")
        apiKey.SetToolTip(apiToolTip)
        # text = "please type your API key:"
        # apiKey(text)
        box.Add(apiKey)

        topicLabel = wx.StaticText(panel)
        topicLabel.SetLabelText("Notification Topic")
        box.Add(topicLabel)
        topic = wx.TextCtrl(panel)
        topicToolTip = wx.ToolTip("Notification Topic")
        topic.SetToolTip(topicToolTip)
        text = ""
        topic.SetLabelText(text)
        box.Add(topic)

        titleLabel = wx.StaticText(panel)
        text = "Notification title:"
        titleLabel.SetLabelText(text)
        box.Add(titleLabel)
        notificationTitle = wx.TextCtrl(panel)
        text = ""
        titleToolTip = wx.ToolTip("Notification Title")
        notificationTitle.SetLabel(text)
        notificationTitle.SetToolTip(titleToolTip)
        box.Add(notificationTitle)

        bodyLabel = wx.StaticText(panel)
        bodyLabel.SetLabelText("Notification body")
        box.Add(bodyLabel)
        body = wx.TextCtrl(panel,)
        bodyToolTip = wx.ToolTip("Notification body")
        body.SetToolTip(bodyToolTip)
        text = ""
        body.SetLabel(text)
        box.Add(body)

        soundLabel = wx.StaticText(panel)
        soundLabel.SetLabelText("Sound:")
        box.Add(soundLabel)
        sound = wx.TextCtrl(panel)
        soundToolTip = wx.ToolTip("Notification Sound")
        sound.SetToolTip(soundToolTip)
        text = ""
        sound.SetLabel(text)
        box.Add(sound)

        submit = wx.Button(panel, -1, "Submit Push")
        submit.Bind(wx.EVT_BUTTON, onSubmitClicked)
        box.Add(submit)

        panel.SetSizer(box)



        self.Show()


if __name__ == '__main__':
    app = wx.App()
    UserInput(None, title='fcmApp')
    app.MainLoop()