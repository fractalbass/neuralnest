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

    def __init__(self, observer):
        self.user = User()
        self.basket = None
        self.eggSet = None
        self.observer = observer

    def run(self, total_eggs):
        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.total_eggs=total_eggs
        total_caught, total_broken = self.runGame()
        return total_caught, total_broken

    def runGame(self):

        displayWidth = 80
        displayHeight = 80
        basketWidth = 20
        dropThreshold = 40
        dropHeight = 10
        minSpeed = 1
        maxSpeed = 2

        display = Display(displayWidth, displayHeight, basketWidth)

        self.basket = Basket(display)

        self.eggSet = EggSet(self, self.basket, dropThreshold, dropHeight, -1, minSpeed, maxSpeed)
        self.eggSet.addEgg(displayWidth/2)
        display.show_wave_start(None)

        while self.eggSet.total_caught + self.eggSet.total_broken < self.total_eggs:  # main game loop
            for i in pygame.event.get():
                if i.type == self.QUIT:
                    return self.QUIT

            action = self.get_player_action()
            if action == 'quit':
                return
            self.basket.update(action)
            self.eggSet.update()

            if self.eggSet.totalDropped<self.total_eggs:
                self.eggSet.launch_more_eggs()
            display.update(self.basket, self.eggSet)

        return self.eggSet.total_caught, self.eggSet.total_broken

    def get_player_action(self):
        return self.user.get_player_action()

    def get_best_player_action(self):
        if self.eggSet is not None and self.eggSet.activeEggs()>0:
            eggx = self.eggSet.getLowestEgg().get_egg_x()
            if eggx < self.basket.basketx + (self.basket.cellWidth/2):
               return 0

            if eggx > self.basket.basketx + (self.basket.cellWidth / 2):
                return 1
        return 0.5

    def caught(self):
        print("Caught!!!!!!!")
        if self.observer is not None:
            self.observer.caught()

    def dropped(self):
        print("Dropped!!!!!!")
        if self.observer is not None:
            self.observer.dropped()

if __name__ == "__main__":
    neuralNest = NeuralNest(None)
    neuralNest.run(10)