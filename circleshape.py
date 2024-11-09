
import pygame

class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius


    def cricle_collision(self, c): 
        d = self.position.distance_to(c.position)
        d2 = self.radius + c.radius
        return (d2 > d)


    def draw(self, screen):
        # sub-classes must override
        pass


    def update(self, dt):
        # sub-classes must override
        pass

        