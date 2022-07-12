class RigidMotion:
    """ A rigid motion. """

    def __init__(self, rm):
        """
        rm: A rigid motion.
        """
        self.rm = rm

    def __repr__(self):
        return 'RigidMotion(' + str(self.rm.__repr__()) + ')'

    def __str__(self):
        return 'RigidMotion(' + str(self.rm.__str__()) + ')'

    def __add__(self, rm2):
        if type(self.rm) == type(rm2):
            return RigidMotion(self.rm.__add__(rm2))
        else:
            return RigidMotion(self.rm)

    def act(self, plane, inverse=False):
        new_rm = self.rm.act(plane, inverse)
        return new_rm