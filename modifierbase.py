import pygame

from constants import MODIFIER_RADIUS
from circleshape import CircleShape

class ModifierBase(CircleShape):
    containers = None

    def __init__(self, x, y, velocity = None):
        super().__init__(x, y, MODIFIER_RADIUS)
        if velocity != None:
            self.velocity = velocity


    def apply_to_player(self, player):
        # pass to implementer
        pass


# CircleShape Overrides
    def draw(self, screen):
        # pass to implementer
        pass


    def update(self, state, dt):
        self.position += self.velocity * dt
        if self.out_of_bounds():
            self.kill()

