import pygame, colors

from game_object import GameObject


class Board(GameObject):
    def __init__(self):
        self.x = 92
        self.y = 92
        self.w = 416
        self.h = 516
        GameObject.__init__(self, self.x, self.y, self.w, self.h)

    def draw(self, surface):
        pygame.draw.rect(surface, colors.BLACK, self.bounds, 10)
        pygame.draw.line(surface, colors.RED1, (200, 608), (400, 608), 10)
