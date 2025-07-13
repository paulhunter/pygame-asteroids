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
from modifierbase import ModifierBase
from shieldmodifier import ShieldModifier
from button import Button

def click_start(state):
    state.sounds.interface_beep.play()
    state.in_menu = None

    for a in state.asteroids:
        a.kill()

    for s in state.shots:
        s.kill()

    for m in state.modifiers:
        m.kill()

    state.field.reset()
    # Create the player at the center of the screen.
    state.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def click_main_menu(state):
    state.in_menu = "MAIN"
    state.player.kill()

def click_how_to(state):
    state.in_menu = "HOW-TO"

def click_quit(state):
    state.quit = True


def main():
    # Init the pygame engine and create our canvas
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    pygame.mixer.init()

    pygame.font.init()
    font = pygame.font.Font(None, 36)

    font_ocr_reg = pygame.font.Font("OCR-a.ttf", 36)
    font_ocr_lg = pygame.font.Font("OCR-a.ttf", 72)
    font_ocr_title = pygame.font.Font("OCR-a.ttf", 120)

    title = font_ocr_title.render("ASTEROIDS", False, (230,230,230))
    game_over = font_ocr_lg.render("GAME OVER", False, (230,230,230))

    font = font_ocr_reg

    # Load the background image, convert for performance.
    bg = pygame.image.load("bg_space.jpg").convert()

    # Game State Container
    state = types.SimpleNamespace()
    state.in_menu = "MAIN"
    state.quit = False
    state.sounds = types.SimpleNamespace()
    state.sounds.interface_beep = pygame.mixer.Sound('./sounds/interface-beep.wav')

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
    ModifierBase.containers = (state.updatable, state.drawable, state.modifiers)

    # Create the player at a later time.
    state.player = None;

    # Create the asteroid field
    state.field = AsteroidField()

    # Main Menu Buttons
    # 130 Pixel Vertical Offsets
    start_button = Button(50, 50, 260, 80, "Start")
    start_button.onClick = lambda: click_start(state)

    how_to_button = Button(50, 180, 260, 80, "How To Play")
    how_to_button.onClick = lambda: click_how_to(state)

    main_menu_button = Button(50, 460, 260, 80, "Main Menu")
    main_menu_button.onClick = lambda: click_main_menu(state)

    quit_button = Button(50, 590, 260, 80, "Quit")
    quit_button.onClick = lambda: click_quit(state)

    # Spawn Modifier Parameters
    modifier_spawn_threshold = 20
    next_modifier_spawn = modifier_spawn_threshold

    # How To Menu Assets
    sub_canvas = pygame.Surface((200,400))
    how_to_weaponModifier = ShieldModifier(100,200,pygame.Vector2(0,0))
    how_to_weaponModifier.draw(sub_canvas);

    # Game Loop
    while True:
        if state.quit:
            return

        events = pygame.event.get()
        for event in events:
            # Window was closed
            if event.type == pygame.QUIT:
                return 

        state.updatable.update(state, dt)

        start_button.update(dt, events)
        how_to_button.update(dt, events)
        main_menu_button.update(dt, events)
        quit_button.update(dt, events)


        for a in state.asteroids:
            if state.player and state.player.collideCircle(a):
                state.player.hit()
                if not state.player.is_alive():
                    state.in_menu = "END"
                else:
                    a.kill()

            
            for s in state.shots:
                if a.circle_collision(s):
                    s.player.scoreOnAsteroidKill(a)
                    a.split()
                    s.kill()

        for m in state.modifiers:
            if state.player and state.player.collideCircle(m):
                m.apply_to_player(state.player)
                m.kill()

        # Wipe the frame, and 'blit' the background image onto it - then draw
        # the scene.
        screen.blit(bg, (0,0))

        # drawable.draw(screen) - Can't be used as it expects images
        for d in state.drawable:
            d.draw(screen)

        if state.in_menu == None:
            # Game 
            score_text = font.render(f"{state.player.score}", False, "yellow", "black")
            screen.blit(score_text, (10,10))

            # Render and display asteroid and shot count.
            asteroid_count_text = font.render(f"A:{len(state.asteroids)}, S:{len(state.shots)}", False, "yellow", "black")
            screen.blit(asteroid_count_text,
                (
                SCREEN_WIDTH - 10 - asteroid_count_text.get_width(),
                SCREEN_HEIGHT - 10 - asteroid_count_text.get_height())
                )

        # On the title screen.
        if state.in_menu == "MAIN":
            start_button.draw(screen, font)
            how_to_button.draw(screen, font)
            quit_button.draw(screen, font)

            screen.blit(title, (SCREEN_WIDTH - title.get_width() - 150, 100))

        # Game over screen
        if state.in_menu == "END":
            main_menu_button.draw(screen, font)
            quit_button.draw(screen, font)

            screen.blit(game_over,
                        (int((SCREEN_WIDTH - game_over.get_width())/2), 100))

        # in the How-to menu off the main menu.
        if state.in_menu == "HOW-TO":
            main_menu_button.draw(screen, font)
            screen.blit(sub_canvas, (100,100));

        # Frame day complete, push the frame to the display.
        pygame.display.flip()

        # Stall til end of frame, and capture the delta-time in seconds
        dt = clock.tick(60) / 1000

    # Shutdown signal given..

    # Cleanup
    pygame.quit()


if __name__ == "__main__":
    main()


