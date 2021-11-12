from tkinter import *
from tkinter import ttk

m = 100
a = 50
b = 250
c = 300
d = 300

def tennis_game():
    root = Tk()
    tennis_court = Canvas(root, width=2*(m+c+d), height=2*(m+a+b), background='grey')
    tennis_court.grid(column=0, row=0, sticky=(N,W,E,S))
    rectangles = [(m, m, m+2*(c+d), m+2*(a+b)),
                  (m, m+a, m+2*(c+d), m+a+2*b),
                  (m+c, m+a, m+c+2*d, m+a+b),
                  (m+c, m+a+b, m+c+2*d, m+a+2*b)]
    for rectangle in rectangles:
        tennis_court.create_rectangle(*rectangle, fill='blue', outline='white')
    root.mainloop()

if __name__ == '__main__':
    tennis_game()