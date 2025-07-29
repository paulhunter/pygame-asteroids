"""spritebase.py
Defines a SpriteBase abstract class which represents any visual graphic that can
be drawn on a screen. 
"""

import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class SpriteBase(pygame.sprite.Sprite):
    containers = None
    """SpriteBase represents a visual graphic that can be drawn on a screen"""

    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


    def draw(self, screen):
        """Draw the graphic on the provided screen."""
        pass
