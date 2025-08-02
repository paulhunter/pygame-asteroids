import pygame
import math

# TODO - Unit Tests as a __main__ ?

def circle_circle_collision(o1, radius1, o2, radius2):
        d = o1.distance_squared_to(o2)
        d2 = (radius1 * radius1) + (radius2 * radius2)
        return (d2 > d)


def circle_and_line_segment_collision(o, radius, a, b):
    ''' Dev Notes:
        https://github.com/paulhunter/pygame-asteroids/blob/main/README.md#circle-and-a-line-segment
    TODO - Perhaps we care about the thickness of the render in our collision
    '''

    # Vectors from one end the line to the origin and the line itself
    u = b - a
    v = o - a
    # Vectors from the other end of the line to the origin and the line itself
    w = a - b
    x = o - b

    min_d2 = math.inf
    max_d2 = 0
    r2 = radius * radius

    if (u.dot(v) > 0 and w.dot(x) > 0):
        # The projection of the origin onto the line segment will be the nearest
        # point to the circle
        p = v.project(u) + a
        min_d2 = o.distance_squared_to(p)
        max_d2 = max(o.distance_squared_to(a), o.distance_squared_to(b))
    else:
        # The nearest and farthest points to the circle will be at either end of
        # the line segment.
        d1 = o.distance_squared_to(a)
        d2 = o.distance_squared_to(b)
        min_d2 = min(d1, d2)
        max_d2 = max(d1, d2)

    if (min_d2 < r2 and max_d2 < r2):
        return False
    elif (min_d2 > r2 and max_d2 > r2):
        return False
    else:
        return True
