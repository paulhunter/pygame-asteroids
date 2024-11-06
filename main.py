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

def main():
    print("Starting asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    # Time Delta
    dt = 0

    # Create the player at the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    rocks = []

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT SIGNAL");
                return 

        # Clear the Screen
        screen.fill((0,0,0))

        # Draw the Player on Screen
        player.draw(screen)
        player.update(dt)

        # Refresh the display
        pygame.display.flip()

        # Stall, and capture the delta-time in seconds
        dt = clock.tick(60) / 1000
        
        # Debug - Log the Frame Rate and Delta
        # print(f"{round(clock.get_fps(),1)}")
        # print(f"{round(dt,3)}")


if __name__ == "__main__":
    main()
    pygame.quit()

