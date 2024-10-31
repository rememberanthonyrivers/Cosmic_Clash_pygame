# this file contains a number of functions that carry
# out the bulk of the work in the game. The game_functions
# module also contains update_screen(), which redraws the
# screen on each pass through the main loop.

import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Checks for key press events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        print("\nRight Key was pressed\n")
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        print("\nLeft Key was pressed\n")
    elif event.key ==pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            # print("\nSpace Key was pressed\n")
            bullets.add(new_bullet)
        


def check_keyup_events(event, ship):
    """Checks for key release events"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def update_screen(ai_settings, screen, ship, alien, bullets):
    """Updates images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    # make the most recently drawn screen visible
    pygame.display.flip()
