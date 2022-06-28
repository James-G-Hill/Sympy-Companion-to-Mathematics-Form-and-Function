from sympy import (
    Line,
    Point
)

class Reflection():
    """ Reflects objects on the plane across a line. """

    def __init__(self, l: Line):
        """ l: The line to reflect across. """
        self.l = l

    def __repr__(self):
        return 'Reflection(' + str(self.l) + ')'

    def __str__(self):
        return 'Reflection(' + str(self.l) + ')'

    def __point_reflect(self, p: Point):
        s = self.l.perpendicular_segment(p)
        if s.length == 0:
            return Point(s.x, s.y)
        else:
            new_x = s.p2.x + (s.p2.x - p.x)
            new_y = s.p2.y + (s.p2.y - p.y)
            return Point(new_x, new_y)

    def reflect(self, plane: list):
        """
        plane: a list of objects on the plane.
        """
        new_plane = list()

        for o in plane:
            if o.is_Point:
                new_plane.append(self.__point_reflect(o))
            elif hasattr(o, 'points'):
                t = type(o)
                pnts = [self.__point_reflect(p) for p in o.points]
                new_plane.append(t(*pnts))
            else:
                t = type(o)
                pnts = [self.__point_reflect(p) for p in o.vertices]
                new_plane.append(t(*pnts))
        
        return new_plane
