import sys
import pygame


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    # \/ checks for key press events \/
    if event.key == pygame.K_RIGHT:
        # The ship moves to the right
        ship.moving_right = True

        # if the left arrow key is pressed
    elif event.key == pygame.K_LEFT:
        # The ship moves to the left
        ship.moving_left = True


def check_keyup_events(event, ship):
    # \/ checks for key releases events \/
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
