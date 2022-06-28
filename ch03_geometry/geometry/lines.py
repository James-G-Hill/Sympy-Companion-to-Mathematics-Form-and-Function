from sympy import (
    Line,
    Point
)


def line_side(l: Line, p: Point):
    """ Obtain the side of a line a point is on. """
    A, B = l.points
    z = ((B.x - A.x) * (p.y - A.y) - (B.y - A.y) * (p.x - A.x)).evalf()
    sign = 0
    if (z < 0):
        sign = -1
    elif (z > 0):
        sign = 1
    return sign
