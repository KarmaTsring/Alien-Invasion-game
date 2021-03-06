class Settings:
    """A Class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the games settings."""
        #Screen settings
        self.screen_width = 1440
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_speed = 1.5
        self.ship_vertical_speed = 1

        #bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3 #in pixel
        self.bullet_height = 13 #In pixel
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 17


