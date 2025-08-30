
""" button.py
Defines a the Button class
"""
import pygame

class Button:
    """ Button
    A generalized UI element for button like interactions.
    """


    def __init__(self, x, y, width, height, text):
        self.position = pygame.Vector2(x,y)
        self.width = width
        self.height = height
        self.text = text
        self.on_click = None

        self.foreground_color = None
        self.background_color = None
        self.on_hover_color = None
        self.on_press_color = None

        # true when mouse is over the button's container
        self.__hover = False
        # true when left mouse button pressed down within the bounds of the button
        self.__mouse_down = False
        # rectangle defining the area of the button
        self.__rect = pygame.Rect(  self.position.x,
                                    self.position.y,
                                    self.width,
                                    self.height)

    def draw(self, screen, font):
        t = font.render(self.text, False, "white")

        pygame.draw.rect(screen,
            ((0,60,60) if not self.on_press_color
                else self.on_press_color) if self.__mouse_down
            else ((40,40,40) if not self.on_hover_color
                else self.on_hover_color) if self.__hover
            else ("black" if not self.background_color
                else self.background_color), self.__rect)

        pygame.draw.rect(screen,
            ("white" if not self.foreground_color else self.foreground_color),
            self.__rect, 2)

        # center the text vertically and horizontally
        t_offset = pygame.Vector2((self.width - t.get_width()) / 2,
                (self.height - t.get_height()) / 2)

        screen.blit(t, (self.position.x + t_offset.x,
                        self.position.y + t_offset.y))


    def update(self, dt, events):
        for ev in events:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if (callable(self.on_click)
                        and self.__rect.collidepoint(ev.pos)
                        and ev.button == 1):
                    self.__mouse_down = True

            if ev.type == pygame.MOUSEBUTTONUP:
                if (self.__mouse_down
                    and callable(self.on_click)
                    and self.__rect.collidepoint(ev.pos)
                    and ev.button == 1):
                    # on release of left button 
                    self.on_click()
                self.__mouse_down = False

            if ev.type == pygame.MOUSEMOTION:
                if (self.__hover
                    and not self.__rect.collidepoint(ev.pos)):
                    self.__hover = False
                elif (not self.__hover
                    and self.__rect.collidepoint(ev.pos)):
                    self.__hover = True
