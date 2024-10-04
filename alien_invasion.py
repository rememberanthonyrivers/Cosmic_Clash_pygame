# an EVENT is an action the user performs while playing the game
# the FOR loop creates an event loop to listen for user input
import sys
import pygame

from settings import Settings

from ship import Ship 


def run_game():
    # initialize the game and creates the screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # create an instance of a ship
    ship = Ship(screen)

    # start the game loop
    while True:

        # watches for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraws the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme() 
        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()