from tkinter import *
from tkinter import ttk

from tennis_court import TennisCourt
# https://tcl.tk/man/tcl8.6/TkCmd/contents.htm


class TennisGame():
    def __init__(self, width=1200, height=600) -> None:
        self.root = Tk()
        
        self.canvas = Canvas(self.root, width=width, height=height, background='black')
        self.canvas.grid(column=0, row=0, sticky=(N,W,E,S))
        
        self.window_width = width
        self.window_height = height
        
        self.court = TennisCourt()

        self.court.draw(self.canvas)

        self.root.bind('<Configure>', self.resize)

        self.root.mainloop()

    def resize(self, event):
        width, height = event.width, event.height
        is_root = event.widget == self.root
        width_updated = self.window_width != width
        height_updated = self.window_height != height

        if is_root and (width_updated or height_updated):
            self.window_width = width
            self.window_height = height
            self.canvas.config(width=width-4, height=height-4)
            
            self.court.resize_canvas(self.canvas)

if __name__ == '__main__':
    tennis_game = TennisGame()