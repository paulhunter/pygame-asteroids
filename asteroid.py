"""asteroid.py - Defines the Asteroid class and its logic"""
import random
import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    """Asteroid - Sprite component"""
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
            if total + o > 360:
                break
            v = v.rotate(o)
            self.__points.append(v)
            total += o


    def split(self):
        """Destroy this instance, and if its large enough, generate two new
            Asteroids with a position and velocity derived from the original"""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        divert = random.uniform(20, 50)
        velocity_a = self.velocity.rotate(divert) * 1.2
        velocity_b = self.velocity.rotate(-divert) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS

        child_a = Asteroid(self.position.x, self.position.y, radius)
        child_a.velocity = velocity_a

        child_b = Asteroid(self.position.x, self.position.y, radius)
        child_b.velocity = velocity_b


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
        if self.out_of_bounds(state.field.get_play_area()):
            self.kill()
