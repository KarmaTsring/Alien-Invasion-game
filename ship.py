import pygame
from settings import Settings

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load the ship image and get its rect
        self.image = pygame.image.load('Game_plane.bmp')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


        #MOvement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """"Update the ship's position based on the movement of flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        #change if you want
        if self.moving_up and self.rect.top > self.screen_rect.top:

            self.y -= self.settings.ship_vertical_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: #(Also can insert "700" which is y coordinate)
            self.y += self.settings.ship_vertical_speed

            #Assign as if statment, becoz when right and left key held pressed
            #together the right key is given upperhand, hence the object moves to right
            #when both left and right key pressed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)



