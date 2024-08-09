from default_object import DefaultObject, Bee
import random


class Game:
    def __init__(self) -> None:
        self.bg        = DefaultObject('assets/bg.png', 0, 0)
        self.bg2       = DefaultObject('assets/bg.png', 0, -640)

        self.spider    = DefaultObject('assets/spider1.png' , random.randrange(0, 300), -50)
        self.flower    = DefaultObject('assets/florwer1.png', random.randrange(0, 300), -50)

        self.bee       = Bee('assets/bee1.png', 150, 600)   

        self.change_scene   = False

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)

        self.spider.drawing(window)
        self.flower.drawing(window)

        self.bee.drawing(window)

    def update(self):

        self.spider.animation('spider' , 8, 4)
        self.flower.animation('florwer', 6, 2)
        self.bee   .animation('bee'    , 2, 4)

        self.bee.colision(self.spider.group, 'Spider')
        self.bee.colision(self.flower.group, 'Flower')

        self.move_spider()
        self.move_flower()
        self.move_bg()
        self.game_over()

    def move_bg(self):
        self.bg.sprite.rect[1]  += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] > 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] > 0:
            self.bg2.sprite.rect[1] = -640
    
    def move_spider(self):
        self.spider.sprite.rect[1] += 10

        if self.spider.sprite.rect[1] > 700:
            self.spider.sprite.kill()
            self.spider = DefaultObject('assets/spider1.png',random.randrange(0, 300), -50)
    
    def move_flower(self):
        self.flower.sprite.rect[1] += 6

        if self.flower.sprite.rect[1] > 700:
            self.flower.sprite.kill()
            self.flower = DefaultObject('assets/florwer1.png', random.randrange(0, 300), -50)

    def game_over(self):
        if self.bee.health <= 0:
            self.change_scene = True