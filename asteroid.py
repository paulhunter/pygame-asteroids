import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS \
                        , SCREEN_HEIGHT \
                        , SCREEN_WIDTH

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        # generate the points of the asteroid around the circle of given radius
        self.__points = []
        total = 0
        v = pygame.Vector2(radius, 0).rotate(random.randrange(20,60,1))
        self.__points.append(v)
        while True:
            o = random.randrange(20,110,10)
            if (total + o > 360):
                break
            v = v.rotate(o)
            self.__points.append(v)
            total += o
        
    
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
        # cast the shape points over the current position to create the 
        # polygon to visualize on screen
        ps = []
        for p in self.__points:
            ps.append(self.position + p)
        pygame.draw.polygon(screen, "white", ps, 2)


    def update(self, state, dt):
        self.position += (self.velocity * dt)
        if self.out_of_bounds():
            self.kill()


