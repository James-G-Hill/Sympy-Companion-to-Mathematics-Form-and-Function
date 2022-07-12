from .reflection import GroupReflection
from .rotation import GroupRotation
from .translation import GroupTranslation
from random import choice


class GroupSpecialEuclidean:
    """ Group of all rototranslations. """

    def get_example():
        """ Return an example. """
        g = choice([GroupTranslation, GroupRotation])
        return g.get_example()


class GroupEuclidean:
    """ Group of all rigid motions. """

    def get_example():
        """ Return an example. """
        g = choice([GroupSpecialEuclidean, GroupReflection])
        return g.get_example()