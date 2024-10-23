# this file contains a number of functions that carry 
# out the bulk of the work in the game. The game_functions 
# module also contains update_screen(), which redraws the 
# screen on each pass through the main loop.

import sys
import pygame


def check_events(ship):
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """Checks for key press events"""
    if event.key == pygame.K_RIGHT:
        # The ship moves to the right
        ship.moving_right = True

        # if the left arrow key is pressed
    elif event.key == pygame.K_LEFT:
        # The ship moves to the left
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Checks for key release events"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            # ship movement to the right stops
            ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            # ship movement to the left stops
            ship.moving_left = False


def update_screen(ai_settings, screen, ship, alien):
    """Updates images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()
