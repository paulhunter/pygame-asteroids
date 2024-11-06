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

def main():
    print("Starting asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        # Clear the Screen
        screen.fill((0,0,0))


        # Refresh the display
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
    pygame.quit()