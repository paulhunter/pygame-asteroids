import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from collisions import circleCircleCollision

class CircleShape(pygame.sprite.Sprite):


    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius


    # self - CircleShape
    # c - CircleShape
    def circle_collision(self, c):
        return circleCircleCollision(self.position, self.radius, c.position, c.radius)


    def out_of_bounds(self):
        b = 2 * self.radius
        if (self.position.x - b > SCREEN_WIDTH
            or self.position.x + b < 0
            or self.position.y - b > SCREEN_HEIGHT
            or self.position.y + b < 0):
            return True
        else:
            return False

    def draw(self, screen):
        # sub-classes must override
        pass


    def update(self, state, dt):
        # sub-classes must override
        pass

        