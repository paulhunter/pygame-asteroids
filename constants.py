"""constants.py
Defines parameters and their default values.
"""

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_SPAWN_INTERVAL = 0.8 # seconds
ASTEROID_KINDS = 3 # Stages/Sizes of Asteroids
ASTEROID_MIN_RADIUS = 20 # pixels
ASTEROID_MAX_RADIUS = ASTEROID_KINDS * ASTEROID_MIN_RADIUS # pixels
ASTEROID_DIVERT_MIN = 0 # Degrees of diversion for child asteroids
ASTEROID_DIVERT_MAX = 60 # Degrees
ASTEROID_CHILD_VELOCITY_FACTOR = 1.2 # Multiplicative Factor of child velocity

PLAYER_RADIUS = 25 # pixels
PLAYER_TURN_SPEED = 300 # degrees per second
PLAYER_MAX_SPEED = 600 # pixels per second
PLAYER_ACCELERATION = 500 # pixels per second per second
PLAYER_SHOOT_SPEED = 500 # pixels per second
PLAYER_SHOOT_COOLDOWN = 0.3 # seconds

SHOT_RADIUS = 3 # pixels
SHOT_COLOR = "yellow" # Well-known or RGB Color

MODIFIER_RADIUS = 20 # pixels
MODIFIER_SPAWN_INTERVAL = 20 # points
MODIFIER_SPAWN_THRESHOLD_FACTOR = 2.1 # Multiplicative Factor for Modifer Spawn
