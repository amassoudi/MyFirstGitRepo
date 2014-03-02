'''
Created on 2 mars 2014

@author: Massoudi-A
'''

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          id=-1,
                          title='Transport management IHM',
                          pos=(100,100),
                          size=(400,300),
                          style=wx.DEFAULT_FRAME_STYLE,
                          name='MainFrame')
        
class MainApp(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)
    
    def OnInit(self):
        print 'MainApp.OnInit...'
        self.mainFrame = MainFrame() 
        self.mainFrame.Show()
        self.SetTopWindow(self.mainFrame)
        return True
    
    def OnExit(self):
        print 'MainApp.OnExit...'
        

if __name__ == '__main__':
    mainApp = MainApp()
    mainApp.MainLoop()