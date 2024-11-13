# this module manages the ships position , and a blitme() method
# to draw the ship to the screen on eash pass through the main while
# loop. The actual image (/images/ship.bpm) is stored within the
# images folder
import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position on the screen"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ships center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # update the ships center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Enforce boundaries to prevent the ship from going out of the screen.
        if self.rect.left < 0:
            self.center = self.rect.width / 2  # Reset to the edge if left out of bounds

        if self.rect.right > self.screen_rect.width:
            self.center = self.screen_rect.width - (
                self.rect.width / 2
            )  # Reset to right edge

        # Update rect object from self.center
        self.rect.centerx = int(self.center)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
