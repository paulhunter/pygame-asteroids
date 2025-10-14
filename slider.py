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

        i = self.size.y / 3 
        self.__bar = pygame.Rect(   self.pos.x + i,
                                    self.pos.y + i, 
                                    self.size.x - 2*i,
                                    self.size.y - 2*i)         
                                   

        # Mouse over the control
        self.__hover = False
        # Mouse Down on the control. 
        self.__mouse_down = False
        # Mouse Down occured over the knob - its 'held'
        self.__knob_held = False
        # Mouse Over the knob
        self.__knob_hover = False
        

        self.on_change = None
        self.range = pygame.Vector2(0,100)
        self.value = 0


    def set_range(self, range):
        # TOOD - Guards?
        self.range = tuple(range[:2])

    def set_value(self, value):
        self.value = value

    def on_knob(self, point):
        return self.__bar.collidepoint(point)

    def axis_to_value(self, x):
        # Returns a value based on the mouse position relative to the axis
        v = min(self.__bar.x + self.__bar.width, max(self.__bar.x, x))
        v = (v - self.__bar.x) / (self.__bar.width)
        z = self.range[0] + (v*(self.range[1] - self.range[0]))
        return z
    
    def value_to_axis(self, value = None):
        # Returns the axial position of the value provided, or the current value
        value = value if value is not None else self.value
        r = (value - self.range[0]) / (self.range[1] - self.range[0])
        x = (self.__bar.x) + (r * self.__bar.width)
        return x


    def draw(self, screen):
        # Draw a debug bounding box.
        pygame.draw.rect(screen,
            "pink", self.__rect, 1)

        # Draw the bar of the slider. 
        pygame.draw.rect(screen, 
            "grey", self.__bar)

        
        # Draw the 'knob' of the slider based on the current value. 
        x = (self.value - self.range[0]) / (self.range[1] - self.range[0]) 
        o = pygame.Vector2( (x * self.__bar.width) + self.__bar.x, 
                            (self.__bar.height / 2) + self.__bar.y)
        pygame.draw.circle(screen,
            ("yellow" if not self.__knob_hover else "orange"),
            o, self.size.y / 3, 2)

        # Colors dependent on the action
        

    def update(self, dt, events):
        for ev in events:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if (self.__rect.collidepoint(ev.pos)):
                    self.set_value(self.value + 20)
                else:
                    print (self.axis_to_value(ev.pos[0]))

            if ev.type == pygame.MOUSEMOTION:
                if (self.__knob_hover
                    and not self.on_knob(ev.pos)):
                    self.__knob_hover = False
                elif (not self.__knob_hover
                    and self.on_knob(ev.pos)):
                    self.__knob_hover = True



