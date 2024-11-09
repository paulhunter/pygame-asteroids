'''
Player

Represents the player, visualized as a triangle

Note - the collision box will be a circle of PLAYER_RADIUS to simplify the math
'''

import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS \
                    , PLAYER_TURN_SPEED \
                    , PLAYER_ACCELERATION \
                    , PLAYER_MAX_SPEED \
                    , SCREEN_WIDTH \
                    , SCREEN_HEIGHT

class Player(CircleShape):
    containers = None


    def __init__(self, x, y):
        # degrees clockwise from north
        self.rotation = 0
        super().__init__(x, y, PLAYER_RADIUS)
        

    def forward(self):
        # y-axis is negative going up, positive going down
        # forward is north vector rotated by current rotation
        return pygame.Vector2(0,-1).rotate(self.rotation)


    def triangle(self):
        forward = self.forward()
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + (forward * self.radius)
        b = self.position - (forward * self.radius) - right
        c = self.position - (forward * self.radius) + right
        return [a, b, c]


    def rotate(self, dt):
        self.rotation = (self.rotation + (PLAYER_TURN_SPEED * dt)) % 360


    def accel(self, dt):
        forward = self.forward()
        newVelocity = self.velocity + (forward * dt * PLAYER_ACCELERATION)
        if (newVelocity.length() > PLAYER_MAX_SPEED):
            newVelocity.scale_to_length(PLAYER_MAX_SPEED)
        self.velocity = newVelocity


# circleshape overrides

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.accel(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.accel(-dt)

        newPos = self.position + (self.velocity * dt);
        # Bound the player to the screen
        # Wrap around if they have traveled too far
        if (newPos.x < 0):
            newPos.update(newPos.x + SCREEN_WIDTH, newPos.y)
        if (newPos.x > SCREEN_WIDTH):
            newPos.update(newPos.x - SCREEN_WIDTH, newPos.y)
        if (newPos.y < SCREEN_HEIGHT):
            newPos.update(newPos.x, newPos.y + SCREEN_HEIGHT)
        if (newPos.y > SCREEN_HEIGHT):
            newPos.update(newPos.x, newPos.y - SCREEN_HEIGHT)

        self.position = newPos;


