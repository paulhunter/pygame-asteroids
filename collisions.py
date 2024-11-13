
import pygame

DEBUG = False

def circleLineSegmentCollision(origin, radius, a, b):
    ''' Dev Notes:
        - Find the point on the segment closest to the origin
        - Compare the distance of that point to the origin to
          the max of the distance from either end of the segment
        - If the closest point is inside, and the segment end
          is outside, we have an intersection
        - Otherwise, no intersection

        Later:
        - Perhaps we care about the thickness of the render
    '''
    # TODO - Debug Check for Types?

    DEBUG = globals()['DBEUG']

    u = b - a
    v = origin - a

    # project the line to the origin, onto the segment,
    # and add the origin of the vector to give us the point on the line
    p = v.project(u) + a

    min_d2 = p.distance_squared_to(origin)
    max_d2 = max(a.distance_squared_to(origin), b.distance_squared_to(origin))
    r2 = radius * radius


    if DEBUG:
        print(f"Origin: {origin.x},{origin.y}")
        print(f"Radius: {radius}")
        print(f"A: {a.x},{a.y}")
        print(f"B: {b.x},{b.y}")
        print(f"U (o-a): {u.x},{u.y}")
        print(f"V (b-a): {v.x},{v.y}")
        print(f"P (u on v) + a: {p.x},{p.y}")


    if (min_d2 < r2 and max_d2 < r2):
        if DEBUG:
            print("Both Points Inside")
        return False
    elif (min_d2 > r2 and max_d2 > r2):
        if DEBUG:
            print(f"Both Points Outside")
        return False
    else:
        if DEBUG:
            print("Intersection")
        return True


def __main():
    globals()['DBEUG'] = True

    o = pygame.Vector2(3,3)
    a = pygame.Vector2(2,0)
    b = pygame.Vector2(4,0)

    u = b - a
    v = o - a

    p = v.project(u) + a


    print(f"project v p u = {p.x}, {p.y}")


    origin = pygame.Vector2(0,3)
    radius = 5
    a = pygame.Vector2(5,1)
    b = pygame.Vector2(0,0)
    print(f"{circleLineSegmentCollision(origin, radius, a, b)}")


    origin = pygame.Vector2(5,0)
    radius = 3
    a = pygame.Vector2(0,5)
    b = pygame.Vector2(5,6)

    p = (origin - a).project(b-a) + a
    print(f"{p.x}, {p.y}")
    print(f"{circleLineSegmentCollision(origin, radius, a, b)}")


    origin = pygame.Vector2(0,0)
    radius = 3
    a = pygame.Vector2(-2,0)
    b = pygame.Vector2(2,0)

    p = (origin - a).project(b-a) + a
    print(f"{p.x}, {p.y}")
    print(f"{circleLineSegmentCollision(origin, radius, a, b)}")


if __name__ == "__main__":
    __main()