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
        

class MainUI_Syntax(wx.Frame):
    def __init__(self, *args, **kwargs):
         pass           

class App_Syntax(wx.App):
    def OnInit(self):
        """ Generate a splash screen while loading assets """
        self.img = wx.Image("images/splash.jpg")
        self.img = wx.BitmapFromImage(self.img)
        self.splashscreen = wx.SplashScreen(self.img, 
            wx.SPLASH_CENTRE_ON_SCREEN, 2000, None)
        return True

def main():
    app = App_Syntax()
    frame = wx.Frame(None, wx.ID_ANY, "Hello World")
    frame.Show(True)
    app.MainLoop()
    return 0

if __name__ == '__main__':
	main()

