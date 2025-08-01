"""circleshape.py
Defines the CircleShape class
"""
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from collisions import circle_circle_collision

class CircleShape(pygame.sprite.Sprite):
    """CircleShape represents a circular sprite"""


    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius


    def circle_collision(self, c):
        """Check for a collision with another CircleShape"""
        return circle_circle_collision(self.position, self.radius, c.position, c.radius)


    def out_of_bounds(self):
        """Check if the circle has left the observable play area"""
        b = 2 * self.radius
        if (self.position.x - b > SCREEN_WIDTH
            or self.position.x + b < 0
            or self.position.y - b > SCREEN_HEIGHT
            or self.position.y + b < 0):
            return True

        # Otherwise, we are within bounds.
        return False


    def draw(self, screen):
        """Draw the sprite on screen"""
        # concrete-classes must override
        pass


    def update(self, state, dt):
        """Update the entity within the frame time delta"""
        # concrete-classes must override
        pass
