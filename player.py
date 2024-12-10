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

        self.shot_interval_modifier = 1.0
        self.shield_level = 0
        self.hit_points = 1


    def forward(self):
        # y-axis is negative going up, positive going down
        # forward is north vector rotated by current rotation
        return pygame.Vector2(0,-1).rotate(self.rotation)


    def triangle(self):
        forward = self.forward() * self.radius
        right = forward.rotate(140)
        left = forward.rotate(220)

        a = self.position + forward
        b = self.position + right
        c = self.position + left
        return [a, b, c]


    def rotate(self, dt):
        self.rotation = (self.rotation + (PLAYER_TURN_SPEED * dt)) % 360


    def accel(self, dt, dir = None):
        direction = dir if dir != None else self.forward()
        newVelocity = self.velocity + (direction * dt * PLAYER_ACCELERATION)
        if (newVelocity.length() > PLAYER_MAX_SPEED):
            newVelocity.scale_to_length(PLAYER_MAX_SPEED)
        self.velocity = newVelocity


    def shoot(self):
        shotPos = self.position + (self.forward() * PLAYER_RADIUS)
        s = Shot(shotPos.x, shotPos.y, SHOT_RADIUS, self)
        s.velocity = (self.forward() * PLAYER_SHOOT_SPEED) + self.velocity


    def collideCircle(self, asteroid):
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
        self.score += int(60 / asteroid.radius)


    def hit(self):
        if self.shield_level > 0:
            self.shield_level -= 1
        else:
            self.hit_points -= 1


    def is_alive(self):
        return self.hit_points > 0


# circleshape overrides

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        if self.shield_level > 0:
            pygame.draw.circle(screen, "blue", self.position, self.radius + 2, 2)
        if self.shield_level > 1:
            pygame.draw.circle(screen, "blue", self.position, self.radius + 5, 2)
        if self.shield_level > 2:
            pygame.draw.circle(screen, "blue", self.position, self.radius + 8, 2)
        # Circlular Boundary
        # pygame.draw.circle(screen, "blue", self.position, self.radius, 2)


    def update(self, state, dt):
        keys = pygame.key.get_pressed()

        self.position += (self.velocity * dt);

        if not self.is_alive():
            return

        # MOVEMENT CONTROLS + MOVEMENT
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.accel(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.accel(-dt)

        if keys[pygame.K_q]:
            self.accel(dt, -self.velocity.normalize())

        # SHOOTING CONTROLS + SHOOTING
        if self.shotCooldown > 0:
            self.shotCooldown -= dt
        elif keys[pygame.K_SPACE]:
            self.shotCooldown = PLAYER_SHOOT_COOLDOWN * self.shot_interval_modifier
            self.shoot()


