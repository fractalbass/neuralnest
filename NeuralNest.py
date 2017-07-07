import random, pygame, sys
from pygame.locals import *
from pygame.key import *
from Basket import Basket
from Display import Display
from EggSet import EggSet
from EggDropper import EggDropper
from User import User
from random import randint

class NeuralNest:
    FPS = 30

    QUIT = 'quit'

    def run(self):
        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.runGame()

    def runGame(self):

        display = Display(640, 480, 40)
        basket = Basket(display.window_width, display.window_height, display.cell_width)
        eggSet = EggSet(basket)
        eggDropper = EggDropper()
        user = User()
        running = True
        eggSet.addEgg(320,20)

        while running:  # main game loop

            action = user.get_player_action()
            if action == 'quit':
                return

            basket.update(action)

            eggSet.update()

            if eggSet.eggs_were_broken:
                return

            if eggSet.activeEggs() < 10 and eggSet.getHighestEgg().eggy > 220:
                eggSet.addEgg(randint(20,620), 20)
            #eggDropper.update(eggSet)
            display.update(basket, eggSet, eggDropper)

neuralNest = NeuralNest()
neuralNest.run()