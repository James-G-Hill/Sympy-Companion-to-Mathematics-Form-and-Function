from .identity import (
    GroupIdentity,
    Identity
)
from .plane import Plane
from random import uniform
from sympy import (
    Line,
    Point
)


class GroupReflection(GroupIdentity):
    """ Reflection group. """

    def _repr_latex_(self):
        return "$L$"

    def get_example(self):
        """ Return an example. """
        p1 = Point(uniform(-1, 1), uniform(-1, 1), evaluate = False)
        p2 = Point(uniform(-1, 1), uniform(-1, 1), evaluate = False)
        l = Line(p1, p2)
        return Reflection(l)


class Reflection(Identity):
    """ Reflects objects on the plane across a line. """

    def __init__(self, l):
        """ l: The line to reflect across. """
        self.l = l

    def __repr__(self):
        return '\n'.join((
            "Reflection(",
            "  line = " + str(self.l),
            ")"
        ))

    def __str__(self):
        return self.__repr__()

    def __add__(self, r):
        return Identity()

    def __point_reflect(self, p: Point):
        s = self.l.perpendicular_segment(p)
        if s.length == 0:
            return Point(s.x, s.y)
        else:
            new_x = s.p2.x + (s.p2.x - p.x)
            new_y = s.p2.y + (s.p2.y - p.y)
            return Point(new_x, new_y)

    def act(self, plane: Plane, inverse=False):
        """
        plane: a list of objects on the plane.
        """
        if inverse:
            return plane
        else:
            new_plane = Plane()

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

    def inverse(self):
        """ Return the inverse of the reflection. """
        return self.l