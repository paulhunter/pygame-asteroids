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
        self.__rect = pygame.Rect(  self.pos.x,
                                    self.pos.y,
                                    self.size.x,
                                    self.size.y)

        self.on_change = None
        self.range = None
        self.value = None

    def set_range(self, range):
        # TOOD - Guards?
        self.range = tuple(range[:2])

    def set_value(self, value):
        self.value = value

    def draw(self, screen):
        # Draw the bar of the slider. 
        pygame.draw.rect(screen,
            "grey", self.__rect)
        

    def update(self, dt, events):
        pass



