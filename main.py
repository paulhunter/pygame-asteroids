'''

Running this Game
Navigate to the project directory and enable the python virtual environment

source venv/bin/activate

You should see your terminal prompt now prepended with "(venv)"

To exit the virtual environment, simply use the following command "deactivate"


Developer Resources
- Python Style Guide - https://peps.python.org/pep-0008/#imports



'''

import pygame

from constants import *

from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Init the pygame engine and create our canvas
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Time Delta
    dt = 0

    # all game objects that can be updated.
    updatable = pygame.sprite.Group()
    # all game objects that can be drawn.
    drawable = pygame.sprite.Group()
    # all asteroids
    asteroids = pygame.sprite.Group()
    # all player shots
    shots = pygame.sprite.Group()
    
    # Configure the applicable containers for the given sprite types
    # Note - As long as these are set, pygame.sprite.Sprite will automatically
    #       add them to these groups at the time of creation
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # Create the player at the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create the asteroid field
    field = AsteroidField()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT SIGNAL");
                return 

        updatable.update(dt)

        for a in asteroids:
            if a.circle_collision(player):
                print("GAME OVER")
                return
            
            for s in shots:
                if a.circle_collision(s):
                    a.split()
                    s.kill()


        # Refresh the canvas
        screen.fill((0,0,0))
        # drawable.draw(screen) - Can't be used as it expects images
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        # Stall til end of frame, and capture the delta-time in seconds
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
    pygame.quit()

