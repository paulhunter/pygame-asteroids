""" slider.py
Defines the Slider class
"""
import pygame



class Slider:
    """ Slider
    A GUI Slider Control
    """

    def __init__(self, pos, size):
        self.pos = pygame.Vector2(pos)
        self.size = pygame.Vector2(size)

        self.on_change = None
        self.range = None
        self.value = None

    def set_range(self, range):
        pass

    def set_value(self, value):
        pass

    def draw(self, screen):
        pass

    def update(self, dt, events):
        pass



