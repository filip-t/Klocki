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
        elif block_type == 1:
            self.w = 100
            self.h = 200
        elif block_type == 2:
            self.w = 200
            self.h = 100
        else:
            self.w = 200
            self.h = 200
        GameObject.__init__(self, self.x, self.y, self.w, self.h)