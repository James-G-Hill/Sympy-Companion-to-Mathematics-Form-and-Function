class Translation:
    """ Translates all objects on the plane. """

    def __init__(self, x: float, y: float):
        """
        x_val: value to move.
        y_val: value to move.
        """
        self.x = x
        self.y = y
        self.is_Point = False

    def __repr__(self):
        return 'Translation(' + str(self.x) + ', ' + str(self.y) + ')'

    def __str__(self):
        return 'Translation(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, T2):
        x_new = self.x + T2.x
        y_new = self.y + T2.y
        return Translation(x_new, y_new)

    def translate(self, plane: list, inverse=False):
        """
        plane: a list of objects on the plane.
        inverse: do the inverse of the transformation.
        """
        new_plane = list()

        x_val = self.x
        y_val = self.y

        if inverse:
            x_val *= -1
            y_val *= -1

        for o in plane:
            if o.is_Point:
                new_plane.append(o.translate(x = x_val, y = y_val))
            elif hasattr(o, 'points'):
                t = type(o)
                pnts = [
                    p.translate(x = x_val, y = y_val)
                    for p in o.points
                ]
                new_plane.append(t(*pnts))
            else:
                t = type(o)
                pnts = [
                    p.translate(x = x_val, y = y_val)
                    for p in o.vertices
                ]
                new_plane.append(t(*pnts))
        
        return new_plane
