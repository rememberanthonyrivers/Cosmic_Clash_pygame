import sys
import pygame


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # checks if a key is pressed
        elif event.type == pygame.KEYDOWN:
            # if the key is the right arrow key
            if event.key == pygame.K_RIGHT:
                # The ship moves continuously to the right 
                ship.moving_right = True

        # checks if a key is released
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # The ship stops moving to the right
                ship.moving_right = False

def update_screen(ai_settings, screen, ship, alien):
    """Updates images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()
