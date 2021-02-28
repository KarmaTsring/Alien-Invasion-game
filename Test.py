import pygame


class BlueSky:

    def __init__(self):
        pygame.init()

    def run(self):

            self.screen = pygame.display.set_mode((800, 500))
            self.bg_color = (0,0,255)

            while True:
                pygame.display.flip()
                self.screen.fill(self.bg_color)
blue = BlueSky()
blue.run()
