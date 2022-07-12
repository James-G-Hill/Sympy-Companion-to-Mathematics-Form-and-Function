from random import uniform
from sympy import (
    pi,
    Point
)


class GroupRotation:
    """ Rotation group. """

    def get_example():
        """ Return an example. """
        p = Point(uniform(-1, 1), uniform(-1, 1), evaluate = False)
        r = Rotation(ang = uniform(0, pi*2), p = p)
        return r


class Rotation:
    """ Rotates all objects on the plane. """

    def __init__(self, ang: float, p=Point(0, 0)):
        """
        x: The point to rotate around.
        ang: The angle to rotate.
        """
        self.p = p
        self.ang = ang
        self.is_Point = False

    def __repr__(self):
        return 'Rotation(' + str(self.p) + ', ' + str(self.ang) + ')'

    def __str__(self):
        return 'Rotation(' + str(self.p) + ', ' + str(self.ang) + ')'

    def __add__(self, T2):
        if not(self.p.x == T2.p.x and self.p.y == T2.p.y):
            raise ValueError('Rotations are not around same point')
        else:
            new_ang = self.ang + T2.ang
            return Rotation(new_ang, self.p)

    def act(self, plane: list, inverse=False):
        """
        plane: a list of objects on the plane.
        inverse: rotate the opposite direction.
        """
        new_plane = list()

        ang = self.ang
        if inverse:
            ang = ang * -1

        for o in plane:
            if o.is_Point:
                new_plane.append(o.rotate(ang, self.p))
            elif hasattr(o, 'points'):
                t = type(o)
                pnts = [p.rotate(ang, self.p) for p in o.points]
                new_plane.append(t(*pnts))
            else:
                t = type(o)
                pnts = [p.rotate(ang, self.p) for p in o.vertices]
                new_plane.append(t(*pnts))
        
        return new_plane
