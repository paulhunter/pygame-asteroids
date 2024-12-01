'''
Running this Game
Navigate to the project directory and enable the python virtual environment

source venv/bin/activate

You should see your terminal prompt now prepended with "(venv)"

To exit the virtual environment, simply use the following command "deactivate"

Developer Resources
- Python Style Guide - https://peps.python.org/pep-0008/#imports

'''

# Python Libraries
import types

# PyGame Modules
import pygame
import pygame.font

# Local Modules
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from weaponmodifier import WeaponModifier
from button import Button

def click_start(state):
    state.in_menu = False

    for a in state.asteroids:
        a.kill()

    state.field.reset()
    state.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def click_quit(state):
    state.quit = True


def main():
    print("Starting asteroids")

    # Init the pygame engine and create our canvas
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.Font(None, 36)

    font_ocr_reg = pygame.font.Font("OCR-a.ttf", 36)
    font_ocr_title = pygame.font.Font("OCR-a.ttf", 120)

    title = font_ocr_title.render("ASTEROIDS", False, (230,230,230))


    font = font_ocr_reg

    # Load the background image, convert for performance.
    bg = pygame.image.load("bg_space.jpg").convert()

    # Game State Container
    state = types.SimpleNamespace()
    state.in_menu = True
    state.quit = False


    # all game objects that can be updated.
    state.updatable = pygame.sprite.Group()
    # all game objects that can be drawn.
    state.drawable = pygame.sprite.Group()
    # all asteroids
    state.asteroids = pygame.sprite.Group()
    # all player shots
    state.shots = pygame.sprite.Group()
    # all player modifiers
    state.modifiers = pygame.sprite.Group()

    # Time Delta
    dt = 0
    
    # Configure the applicable containers for the given sprite types
    # Note - As long as these are set, pygame.sprite.Sprite will automatically
    #       add them to these groups at the time of creation
    Player.containers = (state.updatable, state.drawable)
    Shot.containers = (state.updatable, state.drawable, state.shots)
    Asteroid.containers = (state.updatable, state.drawable, state.asteroids)
    AsteroidField.containers = (state.updatable)
    WeaponModifier.containers = (state.updatable, state.drawable, state.modifiers)

    # Create the player at the middle of the screen
    state.player = None

    # Create the asteroid field
    state.field = AsteroidField()

    # Main Menu Buttons
    # 130 Pixel Vertical Offsets
    start_button = Button(50, 50, 260, 80, "Start")
    start_button.onClick = lambda: click_start(state)

    how_to_button = Button(50, 180, 260, 80, "How To Play")

    quit_button = Button(50, 590, 260, 80, "Quit")
    quit_button.onClick = lambda: click_quit(state)


    # Modifier Spawn Paramters
    modifier_spawn_threshold = 20
    next_modifier_spawn = modifier_spawn_threshold


    # Game Loop
    while True:
        if (state.quit):
            return

        events = pygame.event.get()
        for event in events:
            # Window was closed
            if event.type == pygame.QUIT:
                return 

        state.updatable.update(dt)

        start_button.update(dt, events)
        how_to_button.update(dt, events)
        quit_button.update(dt, events)

        for a in state.asteroids:
            if state.player and state.player.collideCircle(a):
                print("GAME OVER")
                return
            
            for s in state.shots:
                if a.circle_collision(s):
                    s.player.scoreOnAsteroidKill(a)
                    if (s.player.score > next_modifier_spawn):
                        next_modifier_spawn += modifier_spawn_threshold
                        p,v = state.field.generateSpawn()
                        wmod = WeaponModifier(p.x, p.y)
                        wmod.velocity = v
                    a.split()
                    s.kill()

        for m in state.modifiers:
            if state.player and state.player.collideCircle(m):
                state.player.shot_interval_modifier *= m.shot_interval_modifier
                m.kill()

        # Refresh the canvas
        screen.blit(bg, (0,0))

        # drawable.draw(screen) - Can't be used as it expects images
        for d in state.drawable:
            d.draw(screen)

        if (state.in_menu == False):
            score_text = font.render(f"{state.player.score}", False, "yellow", "black")
            screen.blit(score_text, (10,10))

            asteroid_count_text = font.render(f"A:{len(state.asteroids)}, S:{len(state.shots)}", False, "yellow", "black")
            screen.blit(asteroid_count_text, (SCREEN_WIDTH - 10 - asteroid_count_text.get_width(), SCREEN_HEIGHT - 10 - asteroid_count_text.get_height()))

        if (state.in_menu) :
            start_button.draw(screen, font)
            how_to_button.draw(screen, font)
            quit_button.draw(screen, font)

            screen.blit(title, (SCREEN_WIDTH - title.get_width() - 150, 100))

        pygame.display.flip()

        # Stall til end of frame, and capture the delta-time in seconds
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
    pygame.quit()


