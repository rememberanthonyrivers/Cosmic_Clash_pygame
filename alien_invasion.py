import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf

from ship import Ship


def run_game():
    # initialize the game and creates the screen object.
    pygame.init()
    ai_settings = Settings()
    # \/ The main display for the game \/
    screen: pygame.Surface = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)

    # creates a group to store the bullets in, and a group of aliens
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main game loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # the ships position will update after weve checked for key events and before we update the screen
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
