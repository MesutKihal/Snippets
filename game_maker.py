import pygame
import sys

class App(object):
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.title)
        self.fps = 60
        self.clock = pygame.time.Clock()

    def mainloop(self):
        WHITE = (255, 255, 255)
        while True:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(WHITE)
            pygame.display.update()


if __name__ == '__main__':
    my_game = App(480, 800, "Game")
    my_game.mainloop()
