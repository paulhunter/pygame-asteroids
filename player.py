'''
player.py
Represents the player, visualized as a triangle, and its actions as an entity.
'''
import types
import pygame
from entitybase import EntityBase
from spritebase import SpriteBase
from shot import Shot
from constants import PLAYER_RADIUS \
                    , PLAYER_TURN_SPEED \
                    , PLAYER_ACCELERATION \
                    , PLAYER_MAX_SPEED \
                    , PLAYER_SHOOT_SPEED \
                    , PLAYER_SHOOT_COOLDOWN \
                    , SHOT_RADIUS
from collisions import circle_and_line_segment_collision

class Player(EntityBase, SpriteBase):
    """Player
    TODO: On death of player, generate LineEntity instances for each edge of
    the 'ship' triangle, and set their velocity and rotation appropriately.
    """
    containers = None

    def __init__(self, pos):
        # degrees clockwise from north
        self.rotation = 0
        self.shot_cooldown = 0
        self.score = 0
        self.radius = PLAYER_RADIUS
        self.__triangle = None
        # EntityBase Init
        super().__init__(pos)

        self.frame = 0 # animation frame
        self.thrusting = False # Is ship firing the main thruster?
        self.shot_interval_modifier = 1.0 # larger value, greater interval, slower rate of fire.
        self.shield_level = 0
        self.hit_points = 1 # Number of collisions the ship will sustain.


    def forward(self):
        # y-axis is negative going up, positive going down
        # forward is north vector rotated by current rotation
        return pygame.Vector2(0,-1).rotate(self.rotation)


    def triangle(self):
        if self.__triangle is None:
            self.__triangle = types.SimpleNamespace()
            self.__triangle.forward = self.forward() * self.radius
            self.__triangle.right = self.__triangle.forward.rotate(140)
            self.__triangle.left = self.__triangle.forward.rotate(220)

        a = self.position + self.__triangle.forward.rotate(self.rotation)
        b = self.position + self.__triangle.right.rotate(self.rotation)
        c = self.position + self.__triangle.left.rotate(self.rotation)
        return [a, b, c]


    def rotate(self, dt):
        self.rotation = (self.rotation + (PLAYER_TURN_SPEED * dt)) % 360


    def accel(self, dt, direction = None):
        direction = direction if direction is not None else self.forward()
        new_velocity = self.velocity + (direction * dt * PLAYER_ACCELERATION)
        if new_velocity.length() > PLAYER_MAX_SPEED:
            new_velocity.scale_to_length(PLAYER_MAX_SPEED)
        self.velocity = new_velocity


    def shoot(self):
        shot_pos = self.position + (self.forward() * PLAYER_RADIUS)
        s = Shot(shot_pos.x, shot_pos.y, SHOT_RADIUS, self)
        s.velocity = (self.forward() * PLAYER_SHOOT_SPEED) + self.velocity


    def collide_circle(self, asteroid):
        a,b,c = self.triangle()
        if circle_and_line_segment_collision(asteroid.position, asteroid.radius, a, b):
            return True
        if circle_and_line_segment_collision(asteroid.position, asteroid.radius, b, c):
            return True
        if circle_and_line_segment_collision(asteroid.position, asteroid.radius, c, a):
            return True

        return False


    def score_on_asteroid_kill(self, asteroid):
        self.score += int(60 / asteroid.radius)


    def hit(self):
        if self.shield_level > 0:
            self.shield_level -= 1
        else:
            self.hit_points -= 1


    def is_alive(self):
        return self.hit_points > 0

    def destory(self):
        # Destroy the ship into pieces.
        a, b, c = self.triangle();
        line_a = LineEntity(a, b)
        line_b = LineEntity(b, c)
        line_c = LineEntity(c, a)
        #TODO - Spin and set velocity with some amount of randomness.


# spritebase overrides
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        if self.shield_level > 0:
            pygame.draw.circle(screen, "blue", self.position, self.radius + 2, 2)
        if self.shield_level > 1:
            pygame.draw.circle(screen, "blue", self.position, self.radius + 5, 2)
        if self.shield_level > 2:
            pygame.draw.circle(screen, "blue", self.position, self.radius + 8, 2)

        if self.thrusting:
            a,b,c = self.triangle()
            m = b.lerp(c, 0.5)
            m += (m - a.lerp(m, 0.7))
            pygame.draw.circle(screen, "yellow", m, 10-self.frame, 3)


#entitybase overrides
    def update(self, state, dt):
        keys = pygame.key.get_pressed()

        # The player is bound to the play area within the game engine
        self.position += (self.velocity * dt)

        if not self.is_alive():
            return

        # MOVEMENT CONTROLS + MOVEMENT
        self.frame = (self.frame + 1) % 4
        self.thrusting = False
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.thrusting = True
            self.accel(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.accel(-dt)

        if keys[pygame.K_q]:
            self.accel(dt, -self.velocity.normalize())

        # SHOOTING CONTROLS + SHOOTING
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt
        elif keys[pygame.K_SPACE]:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN * self.shot_interval_modifier
            self.shoot()

# DRY Violation - Copy Pasta from circleshape
    def out_of_bounds(self, bounds):
        """Check if the circle has left the play area with a visual fudge factor"""
        b = PLAYER_RADIUS * 2
        if (self.position.x - b > bounds[1]
            or self.position.x + b < bounds[0]
            or self.position.y - b > bounds[3]
            or self.position.y + b < bounds[2]):
            print ("check failed")
            return True

        # Otherwise, we are within bounds.
        return False
