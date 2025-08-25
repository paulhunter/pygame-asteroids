"""speedmodifier
Defines the SpeedModifier class
"""
import types

import pygame

from modifierbase import ModifierBase
from constants import PLAYER_ACCELERATION

class SpeedModifier(ModifierBase):
    """SpeedModifier
    Ship modifier which increase the acceleration of the ship
    """
    def __init__(self, x, y, velocity = None):
        super().__init__(x,y,velocity)

        w = self.radius * 0.2 # Width of Wedge
        h = self.radius * 0.6 # Height of Wedge
        f = w # Offset from Center
        self.__geometry = types.SimpleNamespace()
        self.__geometry.a = pygame.Vector2(0 - w - f, 0 - h)
        self.__geometry.b = pygame.Vector2(0 - f, 0)
        a = self.__geometry.a
        self.__geometry.c = pygame.Vector2(a.x, -a.y)
        self.__geometry.d = pygame.Vector2(0 + f, 0 - h)
        self.__geometry.e = pygame.Vector2(0 + w + f, 0)
        d = self.__geometry.d
        self.__geometry.f = pygame.Vector2(d.x, -d.y)

    # def update(self, state, dt): - No override.

    def apply_to_player(self, player):
        if player.acceleration < 5 * PLAYER_ACCELERATION:
            player.acceleration += PLAYER_ACCELERATION
        else:
            player.score += 50


    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

        g = self.__geometry
        p = self.position
        pygame.draw.line(screen, "green", p + g.a, p + g.b, 2)
        pygame.draw.line(screen, "green", p + g.b, p + g.c, 2)
        pygame.draw.line(screen, "green", p + g.d, p + g.e, 2)
        pygame.draw.line(screen, "green", p + g.e, p + g.f, 2)
