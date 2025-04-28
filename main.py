import wx
from gui import AudioLangAnalyzerFrame

class AudioLangAnalyzerApp(wx.App):
    def OnInit(self):
        self.frame = AudioLangAnalyzerFrame(None, title="AudioLangAnalyzer")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = AudioLangAnalyzerApp()
    app.MainLoop()
