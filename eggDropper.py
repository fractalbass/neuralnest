import random, pygame, sys
from pygame.locals import *
from pygame.key import *


class EggDropper:
    FPS = 15
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    CELLWIDTH = 60
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARKGREEN = (0, 155, 0)
    DARKGRAY = (40, 40, 40)
    BGCOLOR = BLACK
    LEFT = 'left'
    RIGHT = 'right'
    move_delta = 0.5
    DISPLAYSURF = None
    basketx = 240
    baskety = 400
    QUIT = 'quit'

    def run(self):
        global FPSCLOCK, DISPLAYSURF, BASICFONT
        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((640, 480), 0, 24)
        pygame.display.set_caption('Egg Drop')
        self.showStartScreen()
        running=True
        self.runGame()
        self.showGameOverScreen()

    def showStartScreen(self):
        print("Start screen.")

    def runGame(self):

        while True:  # main game loop
            #Note: We will replace this with our neural net.
            move = self.get_player_action()

            if move==self.QUIT: return
            self.update_basket(move)
            self.egg_interaction()
            self.bird_interaction()

    def showGameOverScreen(self):
        print("Game over.")

    def bird_interaction(self):
        return

    def egg_interaction(self):
        return

    def get_player_action(self):
        for i in pygame.event.get():
            if i.type == QUIT:
                return
            key = pygame.key.get_pressed()
            for i in range(0, len(key)):
                if key[i] == 1:
                    print("Key: {0}".format(key[i]))
                    if key[pygame.K_LEFT] != 0:
                        return self.LEFT
                    if key[pygame.K_RIGHT] != 0:
                        return self.RIGHT
                    if key[pygame.K_q] != 0:
                        return self.QUIT

    def update_basket(self, move):
        if move!=None:
            if move==self.LEFT:
                self.basketx = self.basketx - (self.move_delta * self.CELLWIDTH)
                if self.basketx < 0:
                    self.basketx = 0
            if move==self.RIGHT:
                self.basketx = self.basketx + (self.move_delta * self.CELLWIDTH)
                if self.basketx > self.WINDOWWIDTH - self.CELLWIDTH:
                    self.basketx = self.WINDOWWIDTH - self.CELLWIDTH

        self.DISPLAYSURF.fill(self.BGCOLOR)
        basketRect = pygame.Rect(self.basketx, self.baskety, self.CELLWIDTH, 6)
        print("Drawing basket...{0}".format(basketRect))
        pygame.draw.rect(self.DISPLAYSURF, self.DARKGREEN, basketRect)
        pygame.display.update()
        return True

eggDropper = EggDropper()
eggDropper.run()