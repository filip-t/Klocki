from pygame.rect import Rect


class GameObject:
    def __init__(self, x, y, w, h):
        self.bounds = Rect(x, y, w, h)
        self.border = Rect(x, y, w, h)
        self.moving = False
        self.speed = 30

    def draw(self, surface):
        pass

    def move(self, direction):
        self.moving = True

    def update(self):
        if not self.moving:
            return
