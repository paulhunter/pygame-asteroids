import pygame

from constants import MODIFIER_RADIUS \
                    , SCREEN_WIDTH \
                    , SCREEN_HEIGHT
from circleshape import CircleShape

class WeaponModifier(CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, MODIFIER_RADIUS)

        self.shot_interval_modifier = 0.9

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)
        pygame.draw.circle(screen,
                            "yellow",
                            self.position - ((self.radius / 2) * pygame.Vector2(-1,0)),
                            2,
                            2)
        pygame.draw.circle(screen,
                            "yellow",
                            self.position,
                            2,
                            2)
        pygame.draw.circle(screen,
                            "yellow",
                            self.position - ((self.radius / 2) * pygame.Vector2(1,0)),
                            2,
                            2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        if self.out_of_bounds():
            self.kill()


