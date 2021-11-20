from tkinter import *
from tkinter import ttk
# https://tcl.tk/man/tcl8.6/TkCmd/contents.htm

from tennis_court import TennisCourt
from geometry import Point


class TennisGame():
    """This is the Tkinter representaiton of the Tennis Game"""

    draw_styles = {
        'margin_rectangle': ('create_polygon', {'fill': 'grey', 'outline': 'white'}),
        'outer_rectangle': ('create_polygon', {'fill': 'blue', 'outline': 'white', 'width': 3}),
        'court_line': ('create_line', {'fill': 'white', 'width': 3}),
        'net': ('create_line', {'fill': 'white', 'width': 3})
    }

    def __init__(self, width:float=1200, height:float=600) -> None:
        self.scale = 1
        self.is_landscape = True
        self.hm = 0  # horizontal margin
        self.vm = 0  # vertical margin

        self.root = Tk()
        
        self.canvas = Canvas(self.root, width=width, height=height, 
                             background='black')
        self.canvas.grid(column=0, row=0, sticky=(N,W,E,S))
        
        self.window_width = width
        self.window_height = height
        
        self.court = TennisCourt()

        self.draw()

        self.root.bind('<Configure>', self.resize_window)

        self.root.mainloop()

    def resize_window(self, event) -> None:
        width, height = event.width, event.height
        is_root = event.widget == self.root
        width_updated = self.window_width != width
        height_updated = self.window_height != height

        if is_root and (width_updated or height_updated):
            self.window_width = width
            self.window_height = height
            self.canvas.config(width=width-4, height=height-4)
            
            self.resize_court()
 
    def draw(self):
        c = self.court
        elements = [
            ('margin_rectangle', (Point(c.csl+c.b2b, c.csw+c.s2s),
                                  Point(-c.csl-c.b2b, c.csw+c.s2s),
                                  Point(-c.csl-c.b2b, -c.csw-c.s2s),
                                  Point(c.csl+c.b2b, -c.csw-c.s2s))),
            ('outer_rectangle', (Point(c.csl, c.csw),
                                 Point(-c.csl, c.csw),
                                 Point(-c.csl, -c.csw),
                                 Point(c.csl, -c.csw))),
            # single sidelines
            ('court_line', (Point(c.csl, c.scsw),
                            Point(-c.csl, c.scsw))),
            ('court_line', (Point(c.csl, -c.scsw),
                            Point(-c.csl, -c.scsw))),
            # service lines
            ('court_line', (Point(c.sbl, c.scsw),
                            Point(c.sbl, -c.scsw))),
            ('court_line', (Point(-c.sbl, c.scsw),
                            Point(-c.sbl, -c.scsw))),
            # center service line
            ('court_line', (Point(c.sbl, 0),
                            Point(-c.sbl, 0))),
            # center marks
            ('court_line', (Point(c.csl, 0),
                            Point(c.csl - c.cml, 0))),
            ('court_line', (Point(-c.csl, 0),
                            Point(-c.csl + c.cml, 0))),
            # net
            ('net', (Point(0, c.csw + c.npd),
                            Point(0, -c.csw - c.npd)))]
        
        self.elements = {}

        for element_type, points in elements:
            canvas_method, kwargs = self.draw_styles[element_type]
            coords = [p.xy for p in points]
            i = getattr(self.canvas, canvas_method)(*coords, **kwargs)
            self.elements[i] = points
        
        self.resize_court()
    
    def resize_court(self):
        """handles the re-drawing of the court when the canvas size changes"""
        canvas_attrs = self.canvas.config()
        canvas_width = float(canvas_attrs['width'][4])  # px
        canvas_height = float(canvas_attrs['height'][4])  # px
        self.is_landscape = canvas_width > canvas_height
        canvas_max = max([canvas_width, canvas_height])
        canvas_min = min([canvas_width, canvas_height])
        scale1 = canvas_max / self.court.length       
        scale2 = canvas_min / self.court.width
        
        self.scale = min([scale1, scale2])

        court = self.court

        length_margin = (canvas_max - court.length) / 2
        width_margin = (canvas_min - court.width) / 2
        
        if self.is_landscape:
            self.hm, self.vm = length_margin, width_margin
            self.left_ref = self.hm + court.b2b + court.csl
            self.top_ref = self.vm + court.s2s + court.csw
        else:
            self.hm, self.vm = width_margin, length_margin
            self.left_ref = self.hm + court.s2s + court.csw
            self.top_ref = self.vm + court.b2b + court.csl

        for i, element in self.elements.items():
            new_coords = [c for p in element for c in self.xy_to_lefttop(p.xy)]
            self.canvas.coords(i, *new_coords)
    
    def xy_to_lefttop(self, xy):
            x, y = [coord * self.scale for coord in xy]
            delta_left, delta_top = (x, -y) if self.is_landscape else (-y, -x)
            return (self.left_ref + delta_left, self.top_ref + delta_top)
if __name__ == '__main__':
    tennis_game = TennisGame()