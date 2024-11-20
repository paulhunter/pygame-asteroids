import pygame
import math

# TODO - Unit Tests as a __main__ ?

def circleLineSegmentCollision(o, radius, a, b):
    ''' Dev Notes:
    High Level Algorithm
    - Find the point on the line segment nearest to the circle's origin
    - Find the point on the line segment farthest from the circle's origin
    - If the distance to the nearest point is less than the radius and the
      distance to the farthest point is larger than the radius, the line
      segment intersects the circle, otherwise it does not
    - Note: Line segment can be enclosed within the circle and not intersect

    The Math
    The point on the line segment that is closest to the circle, is the
    projection of the circle's origin onto the line, call it P

    To determine if P would land on the line segment, we can check if the dot
    product of the vectors drawn from the ends of the line to the origin and
    line segment itself, if both greater than zero, indicating the angle
    between the vectors is less than 90 degrees, the point P lands on the line.

    If this is not the case, P is not on the line, and cannot be the nearest
    point to the circle. If it is not the nearest point, one of the ends of
    the line segment will be the nearest point to the circle.

    When calculating distances, we will use their squares, to avoid costly
    square root calculations

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
        # The nearest and farthest points to the circle will be either end of
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


