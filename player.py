'''
Player

Represents the player, visualized as a triangle

Note - the collision box will be a circle of PLAYER_RADIUS to simplify the math
'''

import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED

class Player(CircleShape):

    def __init__(self, x, y):
        # degrees clockwise from north
        self.rotation = 0
        super().__init__(x, y, PLAYER_RADIUS)
        

    def triangle(self):
        # y-axis is negative going up, positive going down
        # forward is north vector rotated by current rotation
        forward = pygame.Vector2(0,-1).rotate(self.rotation)
        # 
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + (forward * self.radius)
        b = self.position - (forward * self.radius) - right
        c = self.position - (forward * self.radius) + right
        return [a, b, c]


    def rotate(self, dt):
        self.rotation = (self.rotation + (PLAYER_TURN_SPEED * dt)) % 360

# circleshape overrides

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)


