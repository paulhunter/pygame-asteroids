import pygame

from modifierbase import ModifierBase

class WeaponModifier(ModifierBase):
    def __init__(self, x, y, velocity = None):
        super().__init__(x, y, velocity)

        self.shot_interval_modifier = 0.9

    def apply_to_player(self, player):
        player.shot_interval_modifier *= self.shot_interval_modifier


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


    def update(self, state, dt):
        super().update(state, dt)


