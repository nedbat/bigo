from __future__ import division

import math

def lrange(upper, steps):
    """From 0 to upper in `steps` steps, on a log scale."""
    upexp = math.log(upper)
    fstep = upexp / steps
    delta = math.e ** fstep
    for i in range(steps + 1):
        yield math.e ** (fstep * i) - delta


def distance(pt1, pt2):
    return math.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

def angle(pt1, pt2):
    return math.atan2(pt2[1] - pt1[1], pt2[0] - pt1[0])


def beziers(points):
    """Produce a list of beziers that pass smoothly through points."""
    # https://gielberkers.com/drawing-a-smooth-bezier-line-through-several-points/
    points = list(points)

    # Calculate the distances and angles between neighboring points for each point.
    dist = [0]
    ang = [0]
    for i in range(1, len(points) - 1):
        dist.append(distance(points[i - 1], points[i + 1]))
        ang.append(angle(points[i - 1], points[i + 1]))
    dist.append(0)
    ang.append(0)

    FRAC = .2
    for i in range(len(points) - 1):
        d = distance(points[i], points[i+1])
        p1 = (
            points[i][0] + FRAC * d * math.cos(ang[i]),
            points[i][1] + FRAC * d * math.sin(ang[i])
        )
        p2 = (
            points[i + 1][0] - FRAC * d * math.cos(ang[i + 1]),
            points[i + 1][1] - FRAC * d * math.sin(ang[i + 1])
        )
        p3 = points[i + 1]
        yield p1, p2, p3

def beziers(points):
    # From https://www.particleincell.com/2012/bezier-splines/
    px1, px2 = compute_control_points([p[0] for p in points])
    py1, py2 = compute_control_points([p[1] for p in points])

    for i in range(len(points) - 1):
        yield (
            (px1[i], py1[i]),
            (px2[i], py2[i]),
            points[i + 1]
        )

def compute_control_points(k):
    n = len(k) - 1
    a = [0]
    b = [2]
    c = [1]
    r = [k[0] + 2 * k[1]]

    for i in range(1, n - 1):
        a.append(1)
        b.append(4)
        c.append(1)
        r.append(4 * k[i] + 2 * k[i + 1])

    a.append(2)
    b.append(7)
    c.append(0)
    r.append(8 * k[n - 1] + k[n])

    for i in range(1, n):
        m = a[i] / b[i - 1]
        b[i] -= m * c[i - 1]
        r[i] -= m * r[i - 1]

    p1 = [None] * n
    p1[n - 1] = r[n - 1] / b[n - 1]
    for i in range(n - 2, -1, -1):
        p1[i] = (r[i] - c[i] * p1[i+1]) / b[i]

    p2 = [None] * n
    for i in range(n - 1):
        p2[i] = 2 * k[i + 1] - p1[i + 1]
    p2[n - 1] = (k[n] + p1[n - 1]) / 2

    return p1, p2
