import pygame

from constants import MODIFIER_RADIUS
from modifierbase import ModifierBase

class ShieldModifier(ModifierBase):
    def __init__(self, x, y, velocity = None):
        super().__init__(x, y, velocity)


    def apply_to_player(self, player):
        if (player.shield_level < 3):
            player.shield_level += 1
        else:
            player.score += 50


    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)
        pygame.draw.circle(screen, "blue", self.position, self.radius - 5, 2)


    def update(self, state, dt):
        super().update(state, dt)
