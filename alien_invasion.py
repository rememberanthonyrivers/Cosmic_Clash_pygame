# alien_invasion.py is the only file you need to run 
# when you want to play Alien Invasion. The other 
# files—settings.py, game_functions.py, ship.py— contain 
# code that is imported, directly or indirectly, into this 
# file.

import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # initialize the game and creates the screen object.
    pygame.init()
    ai_settings = Settings()
    # \/ The main display for the game \/
    screen: pygame.Surface = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # create an instance of a ship
    ship = Ship(ai_settings, screen)

    # create an instance of an alien
    alien = Alien(screen)

    # start the main game loop
    while True:
        gf.check_events(ship)
        # the ships position will update after weve checked for key events and before we update the screen
        ship.update()
        # redraws the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, alien)
        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()