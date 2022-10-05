from .identity import (
    GroupIdentity,
    Identity
)
from .plane import Plane
from random import uniform


class GroupTranslation(GroupIdentity):
    """ Translation group. """

    def _repr_latex_(self):
        return "$H$"

    def get_example(self):
        """ Return an example. """
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        return Translation(x, y)


class Translation(Identity):
    """ Translates all objects on the plane. """

    def __init__(self, x = 0, y = 0):
        """
        p: a Point describing the vector from Point(0, 0).
        """
        self.x = x
        self.y = y
        self.is_Point = False

    def __repr__(self):
        return '\n'.join((
            "Translation(",
            "  x = " + str(self.x),
            "  y = " + str(self.y),
            ")"
        ))

    def __str__(self):
        return self.__repr__()

    def __add__(self, t):
        if (isinstance(t, int) and t == 1):
            new_t = Translation(self.x, self.y)
        else:
            new_t = Translation(self.x + t.x, self.y + t.y)
        return new_t

    def __translate__(self, plane: Plane):
        """
        plane: a list of objects on the plane.
        """
        new_plane = Plane()

        for o in plane:
            if o.is_Point:
                new_plane.append(o.translate(x = self.x, y = self.y))
            elif hasattr(o, 'points'):
                t = type(o)
                pnts = [
                    p.translate(x = self.x, y = self.y)
                    for p in o.points
                ]
                new_plane.append(t(*pnts))
            else:
                t = type(o)
                pnts = [
                    p.translate(x = self.x, y = self.y)
                    for p in o.vertices
                ]
                new_plane.append(t(*pnts))
        
        return new_plane

    def act(self, plane: Plane):
        return self.__translate__(plane)

    def inverse(self):
        """ Return the inverse of the translation. """
        return Translation(self.x * -1, self.y * -1)
