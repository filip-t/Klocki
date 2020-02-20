import pygame
import colors
import config as c
from game_object import GameObject


class Block(GameObject):
    def __init__(self, block_type, board_x, board_y):
        self.hover = False
        self.selected = False
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
        if self.selected:
            if self.hover:
                border_color = c.block_border_selecthover_color
            else:
                border_color = c.block_border_selected_color
        else:
            if self.hover:
                border_color = c.block_border_hover_color
            else:
                border_color = c.block_border_idle_color
        pygame.draw.rect(surface, border_color, self.bounds, 3)

    def handle_mouse_event(self, event_type, pos):
        if event_type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif event_type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            self.hover = True
        else:
            self.hover = False

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.selected = True if not self.selected else False
