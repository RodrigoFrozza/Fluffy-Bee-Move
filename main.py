import pygame
from menu import Menu
from game import Game

class Main:
    def __init__(self, sizex, sizey, title) -> None:
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title  = pygame.display.set_caption(title)

        self.start_screen = Menu()
        self.game = Game()

        self.fps = pygame.time.Clock()

        self.game_loop = True

    
    def new(self) -> None: #---------------------------------------------- NEW_GAME
        pass

    def events(self)-> None: #---------------------------------------------- EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_loop = False
            if not self.start_screen.change_scene:
                self.start_screen.events(event)
            elif not self.game.change_scene:
                self.game.bee.move_bee(event)   
            

    def update(self)-> None:    #---------------------------------------- UPDATE
        while self.game_loop:   #---------------------------------------------- MAIN GAME LOOP
            self.fps.tick(30)   #-------------------------------------------------------------- GAME FPS
            self.draw()
            self.events()
            pygame.display.update()

    def draw(self)-> None: #---------------------------------------------- DRAW
        self.window.fill([0,0,0])
        if not self.start_screen.change_scene:
            self.start_screen.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()


game = Main(360, 640, 'Fluffy Bee Move')
game.update()
