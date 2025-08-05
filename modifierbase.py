'''
Abstract representing any object capable of modifying a player objects attributes.
'''
import pygame

from constants import MODIFIER_RADIUS
from circleshape import CircleShape

class ModifierBase(CircleShape):
    containers = None

    def __init__(self, x, y, velocity = None):
        super().__init__(x, y, MODIFIER_RADIUS)
        if velocity is not None:
            self.velocity = velocity


    def apply_to_player(self, player):
        '''abstract - apply modifier effect to player
            implemented by the concrete class'''
        pass


# CircleShape Overrides
    def draw(self, screen):
        # pass to concrete class.
        pass


    def update(self, state, dt):
        self.position += self.velocity * dt
        if self.out_of_bounds(state.field.get_play_area()):
            self.kill()
