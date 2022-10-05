class Plane():
    """ Implementation of a Plane. """

    def __init__(self, *args):
        self.entities = list(args)
        self.entities.sort(key=repr)

    def __repr__(self):
        return ' '.join(([x.__str__() for x in self.entities]))

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.entities)

    def __getitem__(self, item):
        return self.entities[item]

    def append(self, i):
        self.entities.append(i)
        self.entities.sort(key=repr)
