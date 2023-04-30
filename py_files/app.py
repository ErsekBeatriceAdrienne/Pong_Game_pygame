import pygame
import button
import pong_game
from pygame.locals import *


class App:

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        App.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Ball Games")

        App.running = True

    def run(self):
        start_button_image = pygame.image.load('../Images/Start_button_green_arrow.svg.png').convert_alpha()
        start_button = button.Button(200, 200, start_button_image, 11)

        while App.running:
            if start_button.draw(App.screen):
                App.screen = pygame.display.set_mode((pong_game.width, pong_game.height))
                pong_game.main(True)

            start_button.draw(App.screen)
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
            pygame.display.update()

        pygame.quit()


# main
if __name__ == '__main__':
    App().run()
