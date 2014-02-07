#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2014 Kevin <kevin@Liora>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import wx
print wx.version()

class MainUI_Syntax(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainUI_Syntax, self).__init__(*args, **kwargs)
        self.Centre()
        self.__Generate_Menubar()
    def __Generate_Menubar(self):
        self.Menubar = wx.MenuBar()
        self.MenubarFile = wx.Menu()
        self.MenubarEdit = wx.Menu()
        self.MenubarHelp = wx.Menu()
		
        id_FILE_OPEN = wx.NewId()
        id_FILE_QUIT = wx.NewId()
        id_HELP_ABOUT = wx.NewId()
		
        self.MenubarFile.Append(id_FILE_OPEN, "&Open", "Open a file")
        self.MenubarFile.AppendSeparator()
        self.MenubarFile.Append(wx.ID_EXIT, "&Quit", "Quit the Program")
		
        self.MenubarHelp.Append(wx.ID_ABOUT, "About")
		
        self.Menubar.Append(self.MenubarFile, "File")
        self.Menubar.Append(self.MenubarEdit, "Edit")
        self.Menubar.Append(self.MenubarHelp, "Help")
		
        self.Bind(wx.EVT_MENU, self.OnQuit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)
        
        self.SetMenuBar(self.Menubar)
    def OnQuit(self, event):
        self.Close()
    def OnAbout(self, event):
        helpDialog = wx.MessageDialog(self, "An Open Source Language Learning Program", "Syntax", wx.OK)
        helpDialog.ShowModal()
        helpDialog.Destroy()
class App_Syntax(wx.App):
    loading = True
	
    def OnInit(self):
        """ Generate a splash screen while loading assets """
        self.img = wx.Image("images/splash.jpg")
        self.img = wx.BitmapFromImage(self.img)
        self.splashscreen = wx.SplashScreen(self.img, 
            wx.SPLASH_CENTRE_ON_SCREEN, 2000, None)
        self.UI = MainUI_Syntax(None, wx.ID_ANY, "Syntax")
        self.UI.Show(True)
        self.splashscreen.Destroy()
        return True

def main():
    app = App_Syntax()
    app.MainLoop()
    return 0

if __name__ == '__main__':
	main()

