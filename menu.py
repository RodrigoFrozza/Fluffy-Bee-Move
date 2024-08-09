import pygame
from default_object import DefaultObject

class Menu:
    def __init__(self) -> None:
        self.bg = DefaultObject('assets/start.png', 0, 0)
        
        self.change_scene = False

    def draw(self, window):
        self.bg.group.draw(window)

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True
                