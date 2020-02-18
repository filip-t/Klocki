import pygame
from game import Game


class Klocki(Game):
    def __init__(self):
        Game.__init__(self, 'Klocki', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.is_game_running = False


def main():
    Klocki.run()


if __name__ == '__main__':
    main()