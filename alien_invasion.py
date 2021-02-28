import sys

import pygame

from settings import Settings
from ship import Ship
from bullets import Bullet
from enemy import Enemy_Plane


class AlienInvasion:
    """OVerall vlas to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #Enemy plane
        self.enemy_planes = pygame.sprite.Group()

        self.create_fleet()



        #Set background color:
        self.bg_color = (30, 20, 220)

    def create_fleet(self):
        """Create the fleet of enemy planes"""
        #make enemy plane

        plane = Enemy_Plane(self)

        plane_width, plane_height = plane.rect.size
        available_space_x = self.settings.screen_width - (2 * plane_width)
        number_plane_x = available_space_x // (2 * plane_width)

        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * plane_height) - ship_height)

        number_rows = available_space_y // (2 * plane_height)


        #Create the first row of planes:
        for row_number in range(number_rows):
            for number_plane in range(number_plane_x):
                self.create_enemy_plane(number_plane, row_number)

    def create_enemy_plane(self, number_plane, row_number):
        """Create an enemy plane and place it in the row"""
        plane = Enemy_Plane(self)
        plane_width, plane_height = plane.rect.size
        plane.x = plane_width + 2 * plane_width * number_plane
        plane.rect.x = plane.x
        plane.y = plane_height + 2 * plane_height * row_number
        plane.rect.y = plane.y
        self.enemy_planes.add(plane)




        self.enemy_planes.add(plane)



    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_screen()


    def update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #Update bullet positions
        self.bullets.update()

        #Get rid of bullets that have disappeared.

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        #Check for any bullets that have hit enemy planes

        #IF so, get rid of the bullet and the plane

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemy_planes, True, True)

        



    def check_events(self):
        """Respond to key pressess and mouse movement""" \
            # Watch for keyword and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)



    def check_keydown_events(self, event):
        """Key pressed section"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()



    def check_keyup_events(self, event):
        """Key release section"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

        # display enemy plane
        self.enemy_planes.draw(self.screen)

    def update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemy_planes.draw(self.screen)

        



        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game
    game = AlienInvasion()
    game.run_game()