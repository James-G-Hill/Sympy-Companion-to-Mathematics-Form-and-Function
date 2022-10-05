class GroupIdentity:

    def _repr_latex_(self):
        return "$\{I\}$"

    def get_identity(self):
        i = Identity()
        return i
    
    def get_example(self):
        """ Return an example. """
        return Identity()

    @classmethod
    def overgroup_of(cls, grp):
        """ Checks 'grp' is a subgroup of this group. """
        return issubclass(cls, type(grp))


class Identity:
    """ The Identity isometry. """

    def __init__(self):
        self

    def __repr__(self):
        return 'Identity'

    def __str__(self):
        return 'Identity'

    def act(self, plane):
        return plane