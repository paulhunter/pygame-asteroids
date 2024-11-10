
import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = None


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        divert = random.uniform(20, 50)
        velocityA = self.velocity.rotate(divert) * 1.2
        velocityB = self.velocity.rotate(-divert) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS

        childA = Asteroid(self.position.x, self.position.y, radius)
        childA.velocity = velocityA

        childB = Asteroid(self.position.x, self.position.y, radius)
        childB.velocity = velocityB


# circleshape overrides

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        newPos = self.position + (self.velocity * dt)
        self.position = newPos


