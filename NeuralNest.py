import random, pygame, sys
from pygame.locals import *
from pygame.key import *
from Basket import Basket
from Display import Display
from EggSet import EggSet
from User import User
from Wave import Wave
from random import randint

class NeuralNest:
    FPS = 30

    QUIT = 'quit'

    def run(self):
        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.runGame()

    def runGame(self):

        display = Display(640, 480, 60)

        basket = Basket(display.window_width, display.window_height, display.cell_width)

        user = User()

        waveSet = []

        waveSet.append(Wave('one', 240,1,2,5))
        waveSet.append(Wave('two', 240, 1, 2, 10))
        waveSet.append(Wave('three', 200, 1, 2, 15))
        waveSet.append(Wave('four', 180, 1, 3, 20))
        waveSet.append(Wave('five', 160, 1, 3, 25))

        for wave in waveSet:
            eggSet = EggSet(basket, wave.dropHeight, wave.waveCount, wave.minSpeed, wave.maxSpeed)
            eggSet.addEgg(320, 20, 1, 1)
            display.show_wave_start(wave)
            while not eggSet.wave_over():  # main game loop

                action = user.get_player_action()
                if action == 'quit':
                    return
                basket.update(action)
                eggSet.update()
                if eggSet.eggs_were_broken:
                    return
                else:
                    eggSet.launch_more_eggs()

                display.update(basket, eggSet)
            display.show_wave_over(eggSet)


neuralNest = NeuralNest()
neuralNest.run()