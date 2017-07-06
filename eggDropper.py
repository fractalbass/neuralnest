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
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    move_delta = 0.5
    DISPLAYSURF = None


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
        # Set a random start point.
        basketx = 240
        baskety = 400

        while True:  # main game loop
            for i in pygame.event.get():
                if i.type==QUIT:
                    return

                key = pygame.key.get_pressed()
                for i in range(0,len(key)):
                    if key[i]==1:
                        print("Key: {0}".format(key[i]))
                        if key[pygame.K_LEFT] != 0:
                            basketx = basketx - (self.move_delta*self.CELLWIDTH)
                            if basketx<0:
                                basketx=0
                        if key[pygame.K_RIGHT] != 0:
                            basketx = basketx +  (self.move_delta*self.CELLWIDTH)
                            if basketx > self.WINDOWWIDTH - self.CELLWIDTH:
                                basketx = self.WINDOWWIDTH - self.CELLWIDTH
                        if key[pygame.K_q] != 0:
                            return

                        print("Filling screen...")
                        self.DISPLAYSURF.fill(self.BGCOLOR)
                        basketRect = pygame.Rect(basketx, baskety, self.CELLWIDTH, 6)
                        print("Drawing basket...{0}".format(basketRect))
                        pygame.draw.rect(self.DISPLAYSURF, self.DARKGREEN, basketRect)
                        pygame.display.update()

    def showGameOverScreen(self):
        print("Game over.")




eggDropper = EggDropper()
eggDropper.run()