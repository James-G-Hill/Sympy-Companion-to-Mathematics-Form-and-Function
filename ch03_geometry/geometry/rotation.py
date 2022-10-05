from .identity import (
    GroupIdentity,
    Identity
)
from .plane import Plane
from random import uniform
from sympy import (
    Line,
    pi,
    Point
)


class GroupRotation(GroupIdentity):
    """ Rotation group. """

    def _repr_latex_(self):
        return "$R$"

    def get_point(self):
        return Point(uniform(-1, 1), uniform(-1, 1), evaluate = False)

    def get_example(self, p=None):
        if p is None:
            p = self.get_point()
        return Rotation(ang = uniform(0, (pi*2).evalf()), p = p)


class GroupRotationPoint(GroupRotation):
    """ Rotation group around point. """

    def __init__(self, p=Point(0, 0)):
        self.p = p

    def get_point(self):
        return self.p

    def get_rotation(self, ang):
        return Rotation(ang = ang, p = self.p)

    def is_isomorphic(self, group):
        return isinstance(group, GroupRotationPoint)

    def is_equal(self, group):
        x = self.is_isomorphic(group)
        y = self.contains(group.get_point())
        return x and y

    def contains(self, p: Point):
        return self.p.equals(p)


class Rotation(Identity):
    """ Rotates all objects on the plane. """

    def __init__(self, ang=0, p=Point(0, 0)):
        """
        x: The point to rotate around.
        ang: The angle to rotate.
        """
        self.ang = ang
        self.p = p
        self.is_Point = False

    def __repr__(self):
        return '\n'.join((
            "Rotation(",
            "  angle = " + str(self.ang),
            "  point = " + str(self.p),
            ")"
        ))

    def __str__(self):
        return self.__repr__()

    def __add__(self, r):
        if not(self.p.x == r.p.x and self.p.y == r.p.y):
            new_ang = self.ang + r.ang
            if new_ang == 0:
                new_p = Point(0, 0)
            else:
                l1 = Line(self.p, r.p.rotate(-self.ang/2, pt=self.p))
                l2 = Line(r.p, self.p.rotate(r.ang/2, pt=r.p))
                new_p = l1.intersection(l2)[0]
            return Rotation(self.ang + r.ang, new_p)
        elif (isinstance(r, int) and r == 1):
            return Rotation(self.ang, self.p)
        else:
            return Rotation(self.ang + r.ang, self.p)

    def __rotate__(self, plane: Plane):
        """
        plane: a list of objects on the plane.
        """
        new_plane = Plane()

        for o in plane:
            if o.is_Point:
                new_plane.append(o.rotate(self.ang, self.p))
            elif hasattr(o, 'points'):
                t = type(o)
                pnts = [p.rotate(self.ang, self.p) for p in o.points]
                new_plane.append(t(*pnts))
            else:
                t = type(o)
                pnts = [p.rotate(self.ang, self.p) for p in o.vertices]
                new_plane.append(t(*pnts))
        
        return new_plane

    def act(self, plane: Plane):
        return self.__rotate__(plane)

    def inverse(self):
        """ Return the inverse of the rotation. """
        return Rotation(self.ang * -1, self.p)
