from tkinter import *
from tkinter import ttk

from tennis_court import TennisCourt
# https://tcl.tk/man/tcl8.6/TkCmd/contents.htm

m = 100
a = 50
b = 250
c = 300
d = 300
r = 5

def tennis_game():
    root = Tk()
    tennis_canvas = Canvas(root, width=2*(m+c+d), height=2*(m+a+b), background='grey')
    tennis_canvas.grid(column=0, row=0, sticky=(N,W,E,S))

    tennis_court = TennisCourt()

    tennis_court.draw(tennis_canvas)
    # FIXME: get rid of this once the class methods TennisCourt.draw and canvas_resize work
    # rectangles = [(m, m, m+2*(c+d), m+2*(a+b)),
    #               (m, m+a, m+2*(c+d), m+a+2*b),
    #               (m+c, m+a, m+c+2*d, m+a+b),
    #               (m+c, m+a+b, m+c+2*d, m+a+2*b)]
    # for rectangle in rectangles:
    #     tennis_court.create_rectangle(*rectangle, fill='blue', outline='white')
    
    # tennis_court.create_line(m+c+d, m/2, m+c+d, m*3/2+2*(a+b), fill='white', width=3)

    # tennis_court.create_oval(2*m, m+2*a+b, 2*m+2*r, m+2*a+b+2*r, fill='yellow', outline='black')

    # p1 = tennis_court.create_rectangle(m*3/2, m+2*a+b, m*7/4, 2*m+2*a+b, fill='black', outline='black')
    
    # root.bind('<a>', lambda x: tennis_court.move(p1, -5, 0))
    # root.bind('<w>', lambda x: tennis_court.move(p1, 0, -5))
    # root.bind('<s>', lambda x: tennis_court.move(p1, 0, 5))
    # root.bind('<d>', lambda x: tennis_court.move(p1, 5, 0))



    root.mainloop()

if __name__ == '__main__':
    tennis_game()