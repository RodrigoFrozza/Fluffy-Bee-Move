from default_object import DefaultObject



class Game:
    def __init__(self) -> None:
        self.bg             = DefaultObject('assets/bg.png', 0, 0)
        self.bg2            = DefaultObject('assets/bg.png', 0, -640)
        self.change_scene   = False

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)

    def update(self):
        self.bg.sprite.rect[1]  += 1
        self.bg2.sprite.rect[1] += 1

        if self.bg.sprite.rect[1] > 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] > 0:
            self.bg2.sprite.rect[1] = -640