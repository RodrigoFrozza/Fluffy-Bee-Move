import pygame
import pygame.image

class DefaultObject:
    def __init__(self, image, x, y) -> None:

        self.group      = pygame.sprite.Group()
        self.sprite     = pygame.sprite.Sprite(self.group)

        self.sprite.image      = pygame.image.load(image)
        self.sprite.rect       = self.sprite.image.get_rect()
        self.sprite.rect[0]    = x
        self.sprite.rect[1]    = y

        self.frame  = 1
        self.fps    = 0 

    def drawing(self, window):
        self.group.draw(window)

    def animation(self, image, fps, frame):
        self.fps += 1

        if self.fps > fps:

            self.frame += 1
            self.fps    = 0

            if self.frame > frame:
                self.frame = 1

        self.sprite.image = pygame.image.load('assets/' + str(image) + str(self.frame) + '.png')

class Bee(DefaultObject):
    def __init__(self, image, x, y) -> None:
        super().__init__(image, x, y)

        self.health = 5
        self.points = 0

    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 28

    def colision(self, group, name):
        obj_name = name
        colision = pygame.sprite.spritecollide(self.sprite, group, True)

        if obj_name == "Flower" and colision:
            self.points += 1
        elif obj_name == "Spider" and colision:
            self.health -= 1
