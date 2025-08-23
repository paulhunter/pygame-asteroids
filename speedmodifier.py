"""speedmodifier
Defines the SpeedModifier class
"""
import pygame

from modifierbase import ModifierBase
from constants import PLAYER_ACCELERATION

class SpeedModifier(ModifierBase):
    """SpeedModifier
    Ship modifier which increase the acceleration of the ship
    """
    # def __init__(self, x, y, velocity = None): - No override.
    # def update(self, state, dt): - No override.

    def apply_to_player(self, player):
        if player.acceleration < 5 * PLAYER_ACCELERATION:
            player.acceleration += PLAYER_ACCELERATION
        else:
            player.score += 50


    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)
        pygame.draw.line(screen, "green",
            self.position + (self.radius * 0.7 * pygame.Vector2(-1, -1)),
            self.position, 2)
        pygame.draw.line(screen, "green",
            self.position + (self.radius * 0.7 * pygame.Vector2(-1, 1)),
            self.position, 2)
