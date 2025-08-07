"""lineentity.py
Defines the LineEntity class, an abstraction of a line segment geometry that
can be drawn on a screen.
"""
import pygame

class LineEntity(EntityBase):
    containers = None

    def __init__(self, a, b, velocity = None, angular_speed = 0):
        """constructor
        a: Vector2 - one end of the line segment
        b: Vector3 - the other end of the line segment
        """
        # the position of the entity is its center of mass (assume uniformity)
        self.pos = pygame.Vector2((a.x + b.x) / 2, (a.y + b.y) / 2)
        # redefine the end points relative to the center for ease of rotation
        self.a = a - self.pos
        self.b = b - self.pos

        self.velocity = pygame.Vector2(velocity) if velocity is not None
            else pygame.Vector2(0,0)

        self.angular_speed = angular_speed if angular_speed != 0 else 0


    def update(self, state, dt):
        #TODO
        pass

    def draw(self, screen):
        #TODO
        pass

