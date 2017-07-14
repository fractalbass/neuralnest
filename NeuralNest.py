import pygame
from Basket import Basket
from Display import Display
from EggSet import EggSet
from User import User

class NeuralNest:
    FPS = 30

    QUIT = 'quit'

    observer = None
    window_width = None
    window_height = None
    surface_widht = None
    surface_height = None
    basket_width = None
    drop_threshold = None
    drop_height = None
    wave_count = -1
    min_speed = None
    max_speed = None

    #def __init__(self, observer, window_width, window_height, surface_width, surface_height, basket_width):
    def __init__(self,
                 **kwargs):  # observer, basket, drop_threshold, drop_height, wave_count, min_speed, max_speed):
        for (k, v) in kwargs.items():
            setattr(self, k, v)

        self.display = Display(self.window_width, self.window_height, self.surface_width, self.surface_height, self.basket_width)
        self.user = User()
        self.basket = None
        self.eggSet = None

    def run(self, total_eggs):
        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.total_eggs=total_eggs
        total_caught, total_broken = self.runGame()
        return total_caught, total_broken

    def runGame(self):

        self.basket = Basket(self.display)
        self.eggSet = EggSet(observer=self, basket=self.basket, drop_threshold=self.drop_threshold,
                             drop_height=self.drop_height, wave_count=self.wave_count, min_speed=self.min_speed,
                             max_speed=self.max_speed, egg_radius=self.egg_radius)
        self.eggSet.add_egg(self.surface_width / 2)
        self.display.show_wave_start(None)
        clock = pygame.time.Clock()
        while self.eggSet.total_caught + self.eggSet.total_broken < self.total_eggs:  # main game loop

            clock.tick(self.FPS)

            for i in pygame.event.get():
                if i.type == self.QUIT:
                    return self.QUIT

            action = self.get_player_action()
            if action == 'quit':
                return
            self.basket.update(action)
            self.eggSet.update()

            if self.eggSet.total_dropped < self.total_eggs:
                self.eggSet.launch_more_eggs()

            self.display.update(self.basket, self.eggSet)

        caught = self.eggSet.total_caught
        broken = self.eggSet.total_broken
        total = caught+broken
        print("Game over.  Caught:{0}   Dropped:{1}  Success Rate={2}%".format(caught, broken, int(caught/total * 100)))
        return caught, broken

    def get_player_action(self):
        return self.user.get_player_action()

    def get_best_player_action(self):
        if self.eggSet is not None and self.eggSet.active_eggs() > 0:
            eggx = self.eggSet.get_lowest_egg().get_egg_x()
            if eggx < self.basket.basket_x:
                return [1]

            if eggx > self.basket.basket_x + self.basket.cell_width:
                return [-1]
        return [0]

    def caught(self):
        if self.observer is not None:
            self.observer.caught()

    def dropped(self):
        if self.observer is not None:
            self.observer.dropped()

if __name__ == "__main__":
    neuralNest = NeuralNest(observer=None,
                            window_width=800,
                            window_height=800,
                            surface_width=20,
                            surface_height=20,
                            drop_height=0,
                            drop_threshold=17,
                            basket_width=5,
                            min_speed=0.1,
                            max_speed=0.8,
                            egg_radius=1)
    neuralNest.run(10)