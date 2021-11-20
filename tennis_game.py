from tkinter import *
from tkinter import ttk

from tennis_court import TennisCourt
# https://tcl.tk/man/tcl8.6/TkCmd/contents.htm


def tennis_game():
    root = Tk()
    tennis_canvas = Canvas(root, width=400, height=1200, background='black')
    tennis_canvas.grid(column=0, row=0, sticky=(N,W,E,S))

    tennis_court = TennisCourt()

    tennis_court.draw(tennis_canvas)

    root.mainloop()

if __name__ == '__main__':
    tennis_game()