'''
Running this Game
Navigate to the project directory and enable the python virtual environment

source venv/bin/activate

You should see your terminal prompt now prepended with "(venv)"

To exit the virtual environment, simply use the following command "deactivate"

Developer Resources
- Python Style Guide - https://peps.python.org/pep-0008/#imports

Things to further enhance the project:
[ ] Add a Main Menu
[ ] Add Ambience/Background Asteroids to Main Menu
[x] Add a scoring system
[ ] Multiple Lives and respawning
[ ] Add an explosion effect for the asteroids
[x] Add acceleration to the player
[x] Make the player wrap around the screen
[ ] Clear Asteroids that have traveled off screen
[ ] Increase asteroid spawn rate with time
[x] Add a background image
[ ] Spawn Modifiers on Score Thesholds
    - Grant half the modifier if shot
    - Grant full value if 'collected' with ship
    [ ] Create different weapon types
    [ ] Add a shield power-up
    [ ] Add a speed power-up (acceleration)
[ ] Make the asteroids lumpy instead of round
    > Pin the points to a circle, and use a circle bounding box to optimize
    collision checks before iterating line segments
[x] Make the ship have a triangular hitbox
    [x] Create a line segment + circle intersect check
    [ ] Optimize check with a bounding circle check first
        [x] Constrain ship dimensions to a circle
[ ] Add bombs that can be dropped
[ ] Add Hyperspace Jump
    - Original ROM - if Random(0,62) >= Num_Asteroids + 44 - Fail
'''

import pygame
import pygame.font

from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from button import Button

def main():
    print("Starting asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Init the pygame engine and create our canvas
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.Font(None, 36)

    # Load the background image, convert for performance.
    bg = pygame.image.load("bg_space.jpg").convert()

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

    # POC Button Tester
    button = Button(50, 50, 400, 100, "Test!")

    # Game Loop
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                print("QUIT SIGNAL");
                return 

        updatable.update(dt)

        button.update(dt, events)

        for a in asteroids:
            if player.collideAsteroid(a):
                print("GAME OVER")
                return
            
            for s in shots:
                if a.circle_collision(s):
                    s.player.scoreOnAsteroidKill(a)
                    a.split()
                    s.kill()

        # Refresh the canvas
        # screen.fill((0,0,0))
        screen.blit(bg, (0,0))

        # drawable.draw(screen) - Can't be used as it expects images
        for d in drawable:
            d.draw(screen)

        score_text = font.render(f"{player.score}", False, "yellow", "black")
        screen.blit(score_text, (10,10))

        asteroid_count_text = font.render(f"{len(asteroids)}", False, "yellow", "black")
        screen.blit(asteroid_count_text, (SCREEN_WIDTH - 10 - asteroid_count_text.get_width(), SCREEN_HEIGHT - 10 - asteroid_count_text.get_height()))

        # WIP Button - uncomment for testing
        # button.draw(screen, font)

        pygame.display.flip()

        # Stall til end of frame, and capture the delta-time in seconds
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
    pygame.quit()


