from geometry import Line, Point

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

    def __init__(self):
        self.boundary = Line(Point(self.csl, self.csw),
                             Point(-self.csl, self.csw),
                             Point(-self.csl, -self.csw),
                             Point(self.csl, -self.csw))
        self.lines = [
            # single sidelines
            Line(Point(self.csl, self.scsw),
                 Point(-self.csl, self.scsw)),
            Line(Point(self.csl, -self.scsw),
                 Point(-self.csl, -self.scsw)),
            # service lines
            Line(Point(self.sbl, self.scsw),
                 Point(self.sbl, -self.scsw)),
            Line(Point(-self.sbl, self.scsw),
                 Point(-self.sbl, -self.scsw)),
            # center service line
            Line(Point(self.sbl, 0),
                 Point(-self.sbl, 0)),
            # center marks
            Line(Point(self.csl, 0),
                 Point(self.csl - self.cml, 0)),
            Line(Point(-self.csl, 0),
                 Point(-self.csl + self.cml, 0)),
            # net
            Line(Point(0, self.csw + self.npd),
                 Point(0, -self.csw - self.npd))
        ]
    
    def draw(self, canvas):
        # TODO: the idea is that this method handles the drawing of the court
        print(canvas.width, canvas.height)
        #canvas.create_rectangle()


