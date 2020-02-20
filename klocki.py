import pygame
from game import Game
from block import Block
from board import Board
import config as c


class Klocki(Game):
    def __init__(self):
        Game.__init__(self,
                      'Klocki',
                      c.screen_width,
                      c.screen_height,
                      c.background_image,
                      c.frame_rate)
        self.is_game_running = False
        self.blocks = None
        self.board = Board()
        self.objects.append(self.board)
        self.create_blocks()

    def create_blocks(self):
        blocks = [Block(1, 0, 0),
                  Block(3, 1, 0),
                  Block(1, 3, 0),
                  Block(1, 0, 2),
                  Block(2, 1, 2),
                  Block(0, 1, 3),
                  Block(0, 2, 3),
                  Block(1, 3, 2),
                  Block(0, 0, 4),
                  Block(0, 3, 4)]
        self.blocks = blocks
        for block in blocks:
            self.objects.append(block)
            self.mouse_handlers.append(block.handle_mouse_event)

    def update(self):
        super().update()


def main():
    Klocki().run()


if __name__ == '__main__':
    main()
