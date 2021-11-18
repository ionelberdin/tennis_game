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
    bm = 21 * m_per_ft  # backstop margin
    lm = 12 * m_per_ft  # lateral margin
    tw = (csw + lm) * 2  # total width
    tl = (csl + bm) * 2  # total length

    # Tennis Court dimensions in inches, then converted to meters
    cml = 4 * m_per_in  # center mark length
    ncsw = 2 * m_per_in  # net central strap width
    npw = 6 * m_per_in  # net post width
    lw = 3 * m_per_in  # line width 2 to 4 inches

    draw_styles = {
        'outer_rectangle': ('create_rectangle', {'background': 'blue', 'outline': 'white'}),
        'court_line': ('create_line', {'fill': 'white', 'width': 3}),
        'net': ('create_line', {'fill': 'white', 'width': 3})
    }

    def __init__(self):
        pass
                    
    def draw(self, canvas):
        elements = [
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
        canvas_width = canvas_attrs['width'][3]
        canvas_height = canvas_attrs['height'][3]
        is_landscape = canvas_width > canvas_height
        canvas_max = max([canvas_width, canvas_height])
        canvas_min = min([canvas_width, canvas_height])
        canvas_ratio = canvas_max / canvas_min       
        court_ratio = self.tw / self.tl
        
        if canvas_ratio > court_ratio:
            scale = canvas_min / self.tw
        else:
            scale = canvas_max / self.tl
        
        # TODO: calculate horrizontal or vertical padding
        # TODO: transform points into canvas coords
        # TODO: re-postion elements
        



