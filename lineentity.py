"""lineentity.py
Defines the LineEntity class, an abstraction of a line segment geometry that
can be drawn on a screen.
"""
import pygame

class LineEntity(pygame.sprite.Sprite):
    containers = None

    def __init__(self, a, b, velocity = pygame.Vector2(0,0), angular_speed = 0):
        """constructor
        a: Vector2 - one end of the line segment
        b: Vector3 - the other end of the line segment
        """
        super().__init__()
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        # the position of the entity is its center of mass (assume uniformity)
        self.pos = pygame.Vector2((a.x + b.x) / 2, (a.y + b.y) / 2)
        # redefine the end points relative to the center for ease of rotation
        self.a = a - self.pos
        self.b = b - self.pos

        self.velocity = velocity
        self.angular_speed = angular_speed
        # rotation is tracked from init, not based the angle of the line
        # this saves a few vector calculations when updating an entity
        # that is not on the screen (not applicable with the current play area)
        self.rotation = 0


    def update(self, state, dt):
        """update
        Override the utility hook of the pygame.sprite.Sprite class.
        """
        self.pos += (self.velocity * dt)
        self.rotation += (self.angular_speed * dt)
        if self.rotation > 360.0 or self.rotation < 0:
            self.rotation %= 360


    def draw(self, screen):
        """draw
        Note - we are overriding the draw function on the Sprite class in a way
        that does not respect the original implementation.
        """
        #TODO - set color based on entity?
        pygame.draw.line(screen,
            "white",
            self.a.rotate(self.rotation) + self.pos,
            self.b.rotate(self.rotation) + self.pos,
            2)
