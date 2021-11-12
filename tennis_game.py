from tkinter import *
from tkinter import ttk

def tennis_game():
    root = Tk()
    content = ttk.Frame(root)
    frame = ttk.Frame(content, borderwidth=3)
    canvas = Canvas(frame, width=400, height=800, background='grey')
    tennis_court = Canvas(canvas, width=300, height=700, left=50, top=50, background='blue')
    root.mainloop()

if __name__ == '__main__':
    tennis_game()