"""shot.py
Defines the Shot class
"""

import pygame
from circleshape import CircleShape
from constants import SHOT_COLOR

class Shot(CircleShape):
    """Shot
    A projectile most often fired from a ship.
    """
    containers = None


    def __init__(self, x, y, radius, player):
        self.player = player
        super().__init__(x, y, radius)


# CircleShape overrides
    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius, 2)


    def update(self, state, dt):
        self.position += self.velocity * dt
        if self.out_of_bounds(state.field.get_play_area()):
            self.kill()
        