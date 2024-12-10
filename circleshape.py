import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class CircleShape(pygame.sprite.Sprite):


    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius


    def circle_collision(self, c):
        d = self.position.distance_to(c.position)
        d2 = self.radius + c.radius
        return (d2 > d)

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

        