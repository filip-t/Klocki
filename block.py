import pygame, colors

from game_object import GameObject


class Block(GameObject):
    def __init__(self, block_type, board_x, board_y):
        self.board_x = board_x
        self.board_y = board_y
        self.x = 100 + board_x * 100
        self.y = 100 + board_y * 100
        if block_type == 0:
            self.w = 100
            self.h = 100
            self.color = colors.BURLYWOOD
        elif block_type == 1:
            self.w = 100
            self.h = 200
            self.color = colors.BURLYWOOD1
        elif block_type == 2:
            self.w = 200
            self.h = 100
            self.color = colors.BURLYWOOD2
        else:
            self.w = 200
            self.h = 200
            self.color = colors.CRIMSON
        GameObject.__init__(self, self.x, self.y, self.w, self.h)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)
        pygame.draw.rect(surface, colors.GRAY16, self.border, 3)
