from sympy import Point


class Rotation():
    """ Rotates all objects on the plane. """

    def __init__(self, ang: float, p=Point(0, 0)):
        """
        x: The point to rotate around.
        ang: The angle to rotate.
        """
        self.p = p
        self.ang = ang

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

    def rotate(self, plane: list, reverse=False):
        """
        plane: a list of objects on the plane.
        reverse: rotate the opposite direction.
        """
        new_plane = list()

        ang = self.ang
        if reverse:
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
