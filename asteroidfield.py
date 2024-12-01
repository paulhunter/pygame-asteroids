import pygame
import random

from asteroid import Asteroid
from constants import ASTEROID_KINDS \
                    , ASTEROID_SPAWN_INTERVAL \
                    , ASTEROID_MIN_RADIUS \
                    , ASTEROID_MAX_RADIUS \
                    , SCREEN_HEIGHT \
                    , SCREEN_WIDTH

class AsteroidField(pygame.sprite.Sprite):
    containers = None

    # Spawn Zones - Orthogonal Travel Vector + Start Position Function
    edges = [
        [
            # Left side of the screen
            pygame.Vector2(1,0),
            lambda y: pygame.Vector2(
                -ASTEROID_MAX_RADIUS, 
                y * SCREEN_HEIGHT),
        ],
        [
            # Right side of the screen
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, 
                y * SCREEN_HEIGHT
            ),
        ],
        [
            # Top of the screen
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, 
                -ASTEROID_MAX_RADIUS),
        ],
        [
            # Bottom of the screen
            pygame.Vector2(0, -1), 
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, 
                SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]


    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.spawn_timer = 0.0
        self.spawn_count = 0


    def reset(self):
        self.spawn_timer = 0.0
        self.spawn_count = 0


    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
    

    def generateSpawn(self):
        edge = random.choice(self.edges)
        speed = random.randint(40,100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0,1))
        return (position, velocity)


    def update(self, dt):
        self.spawn_timer += dt
        
        if (self.spawn_timer > ASTEROID_SPAWN_INTERVAL):
            self.spawn_timer = 0

            # spawn a new asteroid out of view at a random edge
            position, velocity = self.generateSpawn()
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
            self.spawn_count += 1


