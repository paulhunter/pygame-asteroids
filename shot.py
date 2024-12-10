
import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH \
                    , SCREEN_HEIGHT \
                    , SHOT_RADIUS

class Shot(CircleShape):
    containers = None


    def __init__(self, x, y, radius, player):
        self.player = player
        super().__init__(x, y, radius)
    

# CircleShape overrides

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)


    def update(self, state, dt):
        self.position += self.velocity * dt
        if self.out_of_bounds():
            self.kill()
        