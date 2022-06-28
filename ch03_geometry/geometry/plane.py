from matplotlib import (
    cm,
    pyplot
)
from sympy import Line
from .translation import Translation


def plane_plot(*args, transArrows=False):
    """
    Plot all objects on the plane.

    *args: a list or lists of objects to plot.
    """
    pyplot.clf()
    groups = list(args)
    translations = [x for x in groups if isinstance(x, Translation)]
    groups = [x for x in groups if not isinstance(x, Translation)]
    groups = [[x] if not isinstance(x, list) else x for x in groups]

    colors = list(cm.tab10.colors)
    pyplot.axes()

    for group in groups:
        c = colors.pop()
        for o in group:
            if o.is_Point:
                pyplot.plot(o.x, o.y, 'o', color = c)
            elif isinstance(o, Line):
                pyplot.axline(
                    xy1=(float(o.p1.x), float(o.p1.y)),
                    xy2=(float(o.p2.x), float(o.p2.y)),
                    color='k',
                    linestyle='-.',
                    linewidth=.5,
                    zorder=3
                )
            elif hasattr(o, 'points'):
                xs = [l.x for l in o.points]
                ys = [l.y for l in o.points]
                pyplot.plot(xs, ys, color = c)
            else:
                xs = [l.x for l in o.vertices]
                xs.append(xs[0])
                ys = [l.y for l in o.vertices]
                ys.append(ys[0])
                pyplot.plot(xs, ys, color = c)

    pyplot.axis('square')

    if translations:
        ax = pyplot.gca()
        x0, x1 = ax.get_xlim()
        xCentre = x1 - ((x1 - x0) / 2)
        y0, y1 = ax.get_ylim()
        yCentre = y1 - ((y1 - y0) / 2)
        t = 0
        for trans in translations:
            t += 1
            pyplot.annotate(
                str(t),
                xy = (xCentre, yCentre),
                xytext = (xCentre + trans.x, yCentre + trans.y),
                arrowprops = dict(arrowstyle = "<-")
            )
            xCentre += trans.x
            yCentre += trans.y

    pyplot
