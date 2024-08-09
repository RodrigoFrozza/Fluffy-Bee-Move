import pygame
from menu import Menu
from game import Game

class Main:
    def __init__(self, sizex, sizey, title) -> None:
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title  = pygame.display.set_caption(title)

        self.menu = Menu()
        self.game = Game()

        self.game_loop = True

    
    def new(self) -> None: #---------------------------------------------- NEW_GAME
        pass

    def events(self)-> None: #---------------------------------------------- EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_loop = False

            self.menu.events(event)

    def update(self)-> None: #---------------------------------------------- UPDATE
        while self.game_loop:
            self.draw()
            self.events()
            pygame.display.update()

    def draw(self)-> None: #---------------------------------------------- DRAW
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()


game = Main(360, 640, 'BeeHoney')
game.update()
