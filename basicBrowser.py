#!/usr/bin/python
"""GTK Webkit Browser - second iteration.
"""
import sys
import time
from gi.repository import Gtk
from gi.repository import WebKit


class Browser:
    def __init__(self, url):
        """ browser class """
        self.url = url
        self.webview = WebKit.WebView()
        scrolled_win = Gtk.ScrolledWindow()
        scrolled_win.add(self.webview)

        self.window = Gtk.Window()
        self.window.set_size_request(800, 600)
        self.window.add(scrolled_win)
        # destroy signal - to terminate the program neatly
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.connect("show", self.window_show)
        self.window.show_all()

    def window_show(self, win):
        """ 'Show' Signal, after window's 'Map', 'Realize' signal
        when the window is visible.
        """
        self.webview.open(url)

if __name__ == '__main__':
    url = sys.argv[1]
    win = Browser(url)
    Gtk.main()
