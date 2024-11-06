import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position on the screen"""
        # Initialize the sprite class using super()
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and get its rect.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien at the top left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right."""
        # tracks the aliens position on the x plane 
        self.x += self.ai_settings.alien_speed_factor
        # We then use the value of self.x to update the position of the alien’s rect
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
