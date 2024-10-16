import sys
import pygame


# keys = pygame.key.get_pressed()

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # checks if a key is pressed, if both keys are pressed our ship stops moving
        elif event.type == pygame.KEYDOWN:
            # if the key is the right arrow key
            if event.key == pygame.K_RIGHT:
                # The ship moves continuously to the right
                ship.moving_right = True
                print("Right arrow pressed: moving_right =", ship.moving_right)
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                print("Left arrow pressed: moving_left =", ship.moving_left)

        # checks if a key is released
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # The ship stops moving to the right
                ship.moving_right = False
                print("Right arrow released: moving_right =", ship.moving_right)
                # the below line is not hitting, theflag is not being called 
            elif event.type == pygame.K_LEFT:
                ship.moving_left = False
                print("Left arrow released: moving_left =", ship.moving_left)


def update_screen(ai_settings, screen, ship, alien):
    """Updates images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()