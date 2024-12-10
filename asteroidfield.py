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
            lambda y, r: pygame.Vector2(
                -r,
                y * SCREEN_HEIGHT),
        ],
        [
            # Right side of the screen
            pygame.Vector2(-1, 0),
            lambda y, r: pygame.Vector2(
                SCREEN_WIDTH + r,
                y * SCREEN_HEIGHT
            ),
        ],
        [
            # Top of the screen
            pygame.Vector2(0, 1),
            lambda x, r: pygame.Vector2(
                x * SCREEN_WIDTH, 
                -r),
        ],
        [
            # Bottom of the screen
            pygame.Vector2(0, -1), 
            lambda x, r: pygame.Vector2(
                x * SCREEN_WIDTH, 
                SCREEN_HEIGHT + r
            ),
        ],
    ]


    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.asteroid_spawn_timer = 0.0
        self.asteroid_spawn_count = 0


    def reset(self):
        self.asteroid_spawn_timer = 0.0
        self.asteroid_spawn_count = 0


    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
    

    def generateSpawn(self, radius):
        # radius - Size of the sprite to the spawned
        edge = random.choice(self.edges)
        speed = random.randint(40,100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0,1), radius + 10)
        return (position, velocity)


    def update(self, dt):
        self.asteroid_spawn_timer += dt
        
        if (self.asteroid_spawn_timer > ASTEROID_SPAWN_INTERVAL):
            self.asteroid_spawn_timer = 0

            # spawn a new asteroid out of view at a random edge
            kind = random.randint(1, ASTEROID_KINDS)
            radius = kind * ASTEROID_MIN_RADIUS
            position, velocity = self.generateSpawn(radius)
            self.spawn(radius, position, velocity)
            self.asteroid_spawn_count += 1


