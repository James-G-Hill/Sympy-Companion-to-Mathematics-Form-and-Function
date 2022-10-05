from .identity import Identity
from .reflection import (
    GroupReflection,
    Reflection
)
from .rotation import (
    GroupRotation,
    Rotation
)
from .translation import (
    GroupTranslation,
    Translation
)
from sympy import Point


class GroupSpecialEuclidean(GroupRotation, GroupTranslation):
    """ Group of all rototranslations. """

    def _repr_latex_(self):
        return "$E_0$"
    
    def get_example(self):
        """ Return an example. """
        r = GroupRotation.get_example(self)
        t = GroupTranslation.get_example(self)
        return ProperRigidMotion(r, t)


class GroupEuclidean(GroupSpecialEuclidean, GroupReflection):
    """ Group of all rigid motions. """

    def _repr_latex_(self):
        return "$E$"

    def get_example(self):
        """ Return an example. """
        prm = GroupSpecialEuclidean.get_example(self)
        l = GroupReflection.get_example(self)
        return RigidMotion(prm.r, prm.t, l)


class ProperRigidMotion(Rotation, Translation):
    """ A rigid motion. """

    def __init__(self, r: Rotation, t: Translation):
        if Rotation is None:
            self.r = Identity
        elif not isinstance(r, Rotation):
            raise ValueError("r is not a Rotation.")
        else:
            self.r = r
        
        if Translation is None:
            self.t = Identity
        elif not isinstance(t, Translation):
            raise ValueError("t is not a Translation")
        else:
            self.t = t

    def __repr__(self):
        return '\n'.join((
            "ProperRigidMotion(",
            "  " + str(self.r.__repr__()),
            "  " + str(self.t.__repr__()),
            ")"
        ))

    def __str__(self):
        return self.__repr__()

    def __add__(self, prm):
        if (isinstance(prm, int) and prm == 1):
            return ProperRigidMotion(self.r, self.t)
        else:
            new_r = self.r + prm.r
            new_t = self.t + prm.t
            return ProperRigidMotion(new_r, new_t)

    def act(self, plane):
        plane = self.r.act(plane)
        plane = self.t.act(plane)
        return plane

    def inverse(self):
        inv_ang = self.r.ang * -1
        in_p = Point(self.r.p.x + self.t.x, self.r.p.y + self.t.y)
        in_r = Rotation(inv_ang, in_p)
        in_t = self.t.inverse()
        return ProperRigidMotion(in_r, in_t)


class RigidMotion(ProperRigidMotion, Reflection):
    """ A proper rigid motion. """

    def __init__(self, r: Rotation, t: Translation, l: Reflection):
        super().__init__(r, t)
        self.l = l

    def __repr__(self):
        return '\n'.join((
            "RigidMotion(",
            "  " + str(self.r.__repr__()),
            "  " + str(self.t.__repr__()),
            "  " + str(self.l.__repr__()),
            ")"
        ))

    def __str__(self):
        return self.__repr__()

    def __add__(self, prm):
        if (isinstance(prm, int) and prm == 1):
            return RigidMotion(self.r, self.t, self.l)
        else:
            new_r = self.r + prm.r
            new_t = self.t + prm.t
            return ProperRigidMotion(new_r, new_t)

    def act(self, plane):
        plane = self.r.act(plane)
        plane = self.l.act(plane)
        plane = self.t.act(plane)
        return plane

    def inverse(self):
        inv_ang = self.r.ang * -1
        in_p = Point(self.r.p.x + self.t.x, self.r.p.y + self.t.y)
        in_r = Rotation(inv_ang, in_p)
        in_t = self.t.inverse()
        in_l = self.l.inverse()
        return RigidMotion(in_r, in_t, in_l)
