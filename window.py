# this is the main window class for wx python
import wx
import wx.lib.scrolledpanel
from pyfcm import FCMNotification

def push_to_topic(key, topic, title, body, sound):
    push_service = FCMNotification(api_key=key)
    result = push_service.notify_topic_subscribers(topic_name=topic, message_body=body, message_title=title, sound=sound)
    return result

class UserInput(wx.Frame):
    def __init__(self, parent, title, style, size):
        super(UserInput, self).__init__(parent, title=title, style=style, size=size)

        screenSize = wx.DisplaySize()
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]

        def onSubmitClicked(event):
            if apiKey.Value == "":
                dialog = wx.MessageDialog(None, "Please make sure that your API key is correctly entered. You can find this in the Google Services json file, or from the FCM dashboard.", "Form Error",
                                          wx.OK | wx.ICON_INFORMATION)
                dialog.ShowModal()
                return
            result = push_to_topic(key=apiKey.Value, topic=topic.Value, title=notificationTitle.Value, body=body.Value, sound=sound.Value)
            dialog = wx.MessageDialog(None, "Push sent with the following result." + str(result), "Message result", wx.OK | wx.ICON_INFORMATION )
            dialog.ShowModal()

        def onResetClicked(event):
            topic.Value = ""
            notificationTitle.Value = ""
            body.Value = ""
            sound.Value = ""

        def OnImportClicked(event):
            with wx.FileDialog(self, "Import API Key", "*.fbk files (*.bfk)|*.fbk", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return

            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    apiKey.Value = file.read()
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)

        # define the panel and the sizer for elements
        panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(screenWidth/4, screenHeight/2) )
        panel.SetupScrolling()
        box = wx.BoxSizer(wx.VERTICAL)

        # starting to define the GUI elements
        hBox = wx.BoxSizer(wx.HORIZONTAL)
        apilabel = wx.StaticText(panel, size=(-1, 20))
        text = "API Key"
        apilabel.SetLabelText(text)
        hBox.Add(apilabel)
        importButton = wx.Button(panel, -1, "Import Key", size=(-1, 20))
        importButton.Bind(wx.EVT_BUTTON, OnImportClicked)
        hBox.Add(importButton)
        box.Add(hBox)
        apiKey = wx.TextCtrl(panel, size=(screenWidth/4, 25))
        apiToolTip = wx.ToolTip("FCM API Key")
        apiKey.SetToolTip(apiToolTip)
        # text = "please type your API key:"
        # apiKey(text)
        box.Add(apiKey)


        topicLabel = wx.StaticText(panel, size=(screenWidth/4, 20))
        topicLabel.SetLabelText("Notification Topic")
        box.Add(topicLabel)
        topic = wx.TextCtrl(panel, size=(screenWidth/4, 25))
        topicToolTip = wx.ToolTip("Notification Topic")
        topic.SetToolTip(topicToolTip)
        text = ""
        topic.SetLabelText(text)
        box.Add(topic)

        titleLabel = wx.StaticText(panel, size=(screenWidth/4, 20))
        text = "Notification title:"
        titleLabel.SetLabelText(text)
        box.Add(titleLabel)
        notificationTitle = wx.TextCtrl(panel, size=(screenWidth/4, 25))
        text = ""
        titleToolTip = wx.ToolTip("Notification Title")
        notificationTitle.SetLabel(text)
        notificationTitle.SetToolTip(titleToolTip)
        box.Add(notificationTitle)

        bodyLabel = wx.StaticText(panel, size=(screenWidth/4, 20))
        bodyLabel.SetLabelText("Notification body")
        box.Add(bodyLabel)
        body = wx.TextCtrl(panel, size=(screenWidth/4, 60), style=wx.TE_MULTILINE)
        bodyToolTip = wx.ToolTip("Notification body")
        body.SetToolTip(bodyToolTip)
        text = ""
        body.SetLabel(text)
        box.Add(body)

        soundLabel = wx.StaticText(panel, size=(screenWidth/4, 20))
        soundLabel.SetLabelText("Sound:")
        box.Add(soundLabel)
        sound = wx.TextCtrl(panel, size=(screenWidth/4, 25))
        soundToolTip = wx.ToolTip("Notification Sound")
        sound.SetToolTip(soundToolTip)
        text = ""
        sound.SetLabel(text)
        box.Add(sound)

        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox.AddStretchSpacer(prop=1)
        submit = wx.Button(panel, -1, "Submit Push")
        submit.Bind(wx.EVT_BUTTON, onSubmitClicked)
        hBox.Add(submit, 0, wx.CENTER)

        reset = wx.Button(panel, -1, "Reset")
        reset.Bind(wx.EVT_BUTTON, onResetClicked)
        hBox.Add(reset, 0, wx.CENTER)
        hBox.AddStretchSpacer(prop=1)

        box.Add(hBox, 0, wx.CENTER)

        panel.SetSizer(box)

        self.Show()

        panel.Fit()

if __name__ == '__main__':
    app = wx.App()
    screenSize = wx.DisplaySize()
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    UserInput(None, title='fcmApp', style=wx.DEFAULT_DIALOG_STYLE, size=(screenWidth/4, screenHeight/2))
    app.MainLoop()