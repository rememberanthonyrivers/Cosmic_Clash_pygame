class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 4
        self.ship_limit = 3

        # Alien settings
        self.alien_speed_factor = 1

        # fleet drop speed controls how quickly the alien fleet drops down the screen
        self.fleet_drop_speed = 0.25

        # horizontal speed, fleet direction of 1 represents movement to the right; -1 means to the left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed_factor = 7
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 69, 0)  # Fiery orange/red color
        self.bullets_allowed = 3
