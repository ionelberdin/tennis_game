from tkinter.constants import W
from geometry import Point

m_per_ft = 0.3048
m_per_in = 0.0254


class TennisCourt:
    # Tennis Court dimensions in feet, then converted to meters
    daw = 4.5 * m_per_ft  # doubles alley width
    csw = 36 / 2 * m_per_ft  # court semi width
    scsw = csw - daw  # singles court semi width
    csl = 78 / 2 * m_per_ft  # court semi length
    sbl = 21 * m_per_ft  # service box length
    npd = 3 * m_per_ft  # net post distance (to sideline)
    nph = 3.5 * m_per_ft  # net post height
    nch = 3 * m_per_ft  # net central height
    b2b = 21 * m_per_ft  # baseline to backstop distance
    s2s = 12 * m_per_ft  # sideline to sidestop distance
    court_width = (csw + s2s) * 2  # total tennis court width
    court_length = (csl + b2b) * 2  # total tennis court length

    # Tennis Court dimensions in inches, then converted to meters
    cml = 4 * m_per_in  # center mark length
    ncsw = 2 * m_per_in  # net central strap width
    npw = 6 * m_per_in  # net post width
    lw = 3 * m_per_in  # line width 2 to 4 inches

    draw_styles = {
        'margin_rectangle': ('create_polygon', {'fill': 'grey', 'outline': 'white'}),
        'outer_rectangle': ('create_polygon', {'fill': 'blue', 'outline': 'white', 'width': 3}),
        'court_line': ('create_line', {'fill': 'white', 'width': 3}),
        'net': ('create_line', {'fill': 'white', 'width': 3})
    }

    def __init__(self):
        self.scale = 1
        self.is_landscape = True
        self.hm = 0  # horizontal margin
        self.vm = 0  # vertical margin
                    
    def draw(self, canvas):
        elements = [
            ('margin_rectangle', (Point(self.csl+self.b2b, self.csw+self.s2s),
                                  Point(-self.csl-self.b2b, self.csw+self.s2s),
                                  Point(-self.csl-self.b2b, -self.csw-self.s2s),
                                  Point(self.csl+self.b2b, -self.csw-self.s2s))),
            ('outer_rectangle', (Point(self.csl, self.csw),
                                 Point(-self.csl, self.csw),
                                 Point(-self.csl, -self.csw),
                                 Point(self.csl, -self.csw))),
            # single sidelines
            ('court_line', (Point(self.csl, self.scsw),
                            Point(-self.csl, self.scsw))),
            ('court_line', (Point(self.csl, -self.scsw),
                            Point(-self.csl, -self.scsw))),
            # service lines
            ('court_line', (Point(self.sbl, self.scsw),
                            Point(self.sbl, -self.scsw))),
            ('court_line', (Point(-self.sbl, self.scsw),
                            Point(-self.sbl, -self.scsw))),
            # center service line
            ('court_line', (Point(self.sbl, 0),
                            Point(-self.sbl, 0))),
            # center marks
            ('court_line', (Point(self.csl, 0),
                            Point(self.csl - self.cml, 0))),
            ('court_line', (Point(-self.csl, 0),
                            Point(-self.csl + self.cml, 0))),
            # net
            ('net', (Point(0, self.csw + self.npd),
                            Point(0, -self.csw - self.npd)))]
        
        self.elements = {}

        for element_type, points in elements:
            canvas_method, kwargs = self.draw_styles[element_type]
            coords = [p.xy for p in points]
            i = getattr(canvas, canvas_method)(*coords, **kwargs)
            self.elements[i] = points
        
        self.resize_canvas(canvas)
    
    def resize_canvas(self, canvas):
        """handles the re-drawing of the court when the canvas size changes"""
        canvas_attrs = canvas.config()
        canvas_width = float(canvas_attrs['width'][4])  # px
        canvas_height = float(canvas_attrs['height'][4])  # px
        self.is_landscape = canvas_width > canvas_height
        canvas_max = max([canvas_width, canvas_height])
        canvas_min = min([canvas_width, canvas_height])
        scale1 = canvas_max / self.court_length       
        scale2 = canvas_min / self.court_width
        
        self.scale = min([scale1, scale2])

        
        length_margin = (canvas_max - self.court_length) / 2
        width_margin = (canvas_min - self.court_width) / 2
        
        if self.is_landscape:
            self.hm, self.vm = length_margin, width_margin
            self.left_ref = self.hm + self.b2b + self.csl
            self.top_ref = self.vm + self.s2s + self.csw
        else:
            self.hm, self.vm = width_margin, length_margin
            self.left_ref = self.hm + self.s2s + self.csw
            self.top_ref = self.vm + self.b2b + self.csl

        for i, element in self.elements.items():
            canvas.coords(i, *[c for p in element for c in self.xy_to_lefttop(p.xy)])
    
    def xy_to_lefttop(self, xy):
            x, y = [coord * self.scale for coord in xy]
            delta_left, delta_top = (x, -y) if self.is_landscape else (-y, -x)
            return (self.left_ref + delta_left, self.top_ref + delta_top)



