"""entitybase.py
Defines a EntityBase abstract which represents any game logic entity that exists
within the game space.
"""
import pygame

class EntityBase:

    def __init__(self, pos):
        self.position = pygame.Vector2(pos.x,pos.y)
        self.rotation = 0 # Positive is clockwise rotation in degrees.

        self.velocity = pygame.Vector2(0,0)
        self.rotation_speed = 0 # Positive is clockwise rotation in degrees/sec.

    def update(self, state, dt):
        """update
        Update the entity over the time space of the frame dt, using the current
        provided game state. 
        """
        self.position += self.velocity * dt
        self.rotation = (self.rotation + (self.rotation_speed * dt)) % 360
