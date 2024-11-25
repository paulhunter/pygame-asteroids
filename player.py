'''
Player

Represents the player, visualized as a triangle

'''

import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS \
                    , PLAYER_TURN_SPEED \
                    , PLAYER_ACCELERATION \
                    , PLAYER_MAX_SPEED \
                    , PLAYER_SHOOT_SPEED \
                    , PLAYER_SHOOT_COOLDOWN \
                    , SHOT_RADIUS \
                    , SCREEN_WIDTH \
                    , SCREEN_HEIGHT
from collisions import circleLineSegmentCollision

class Player(CircleShape):
    containers = None


    def __init__(self, x, y):
        # degrees clockwise from north
        self.rotation = 0
        self.shotCooldown = 0
        self.score = 0
        super().__init__(x, y, PLAYER_RADIUS)
        self.__a = self.forward() * PLAYER_RADIUS
        self.__b = self.forward()


    def forward(self):
        # y-axis is negative going up, positive going down
        # forward is north vector rotated by current rotation
        return pygame.Vector2(0,-1).rotate(self.rotation)


    def triangle(self):
        forward = self.forward() * self.radius
        right = forward.rotate(140)
        left = forward.rotate(220)

        a = self.position + forward
        b = self.position + right # - (forward * self.radius) - pygame.Vector(-right.x
        c = self.position + left # - (forward * self.radius) + right
        return [a, b, c]


    def rotate(self, dt):
        self.rotation = (self.rotation + (PLAYER_TURN_SPEED * dt)) % 360


    def accel(self, dt):
        forward = self.forward()
        newVelocity = self.velocity + (forward * dt * PLAYER_ACCELERATION)
        if (newVelocity.length() > PLAYER_MAX_SPEED):
            newVelocity.scale_to_length(PLAYER_MAX_SPEED)
        self.velocity = newVelocity


    def shoot(self):
        shotPos = self.position + (self.forward() * PLAYER_RADIUS)
        s = Shot(shotPos.x, shotPos.y, SHOT_RADIUS, self)
        s.velocity = (self.forward() * PLAYER_SHOOT_SPEED) + self.velocity


    def collideAsteroid(self, asteroid):
        a,b,c = self.triangle()
        if circleLineSegmentCollision(asteroid.position, asteroid.radius, a, b):
            return True
        elif circleLineSegmentCollision(asteroid.position, asteroid.radius, b, c):
            return True
        elif circleLineSegmentCollision(asteroid.position, asteroid.radius, c, a):
            return True
        else:
            return False


    def scoreOnAsteroidKill(self, asteroid):
        self.score += int(120 / asteroid.radius)


# circleshape overrides

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        # Circlular Boundary
        # pygame.draw.circle(screen, "blue", self.position, self.radius, 2)


    def update(self, dt):
        keys = pygame.key.get_pressed()

        # MOVEMENT CONTROLS + MOVEMENT
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

        # SHOOTING CONTROLS + SHOOTING
        if self.shotCooldown > 0:
            self.shotCooldown -= dt
        elif keys[pygame.K_SPACE]:
            self.shotCooldown = PLAYER_SHOOT_COOLDOWN
            self.shoot()


