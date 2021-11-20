from geometry import Array

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
    width = (csw + s2s) * 2  # total tennis court width
    length = (csl + b2b) * 2  # total tennis court length

    # Tennis Court dimensions in inches, then converted to meters
    cml = 4 * m_per_in  # center mark length
    ncsw = 2 * m_per_in  # net central strap width
    npw = 6 * m_per_in  # net post width
    lw = 3 * m_per_in  # line width 2 to 4 inches

    def __init__(self):
        pass
        # TODO: define court zones where ball is allowed to bounce
                    




