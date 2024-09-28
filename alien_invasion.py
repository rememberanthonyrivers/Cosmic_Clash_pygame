# an EVENT is an action the user performs while playing the game
# the FOR loop creates an event loop to listen for user input
import sys
import pygame


def run_game():
    # initialize the game and creates the screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # lets set the background color
    bg_color = (230, 230, 230) 

    # start the game loop
    while True:
        # watches for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()