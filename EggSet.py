from random import randint
from random import randrange

class EggSet:

    eggs = []

    observer = None
    basket = None
    wave_count = -1
    eggs_were_broken = False
    eggs_were_caught = False
    drop_threshold = None
    drop_height = None
    min_speed = None
    max_speed = None
    egg_radius = None
    total_dropped = 0
    total_broken = 0
    total_caught = 0
    egg_radius = 0

    def __init__(self, **kwargs):  #observer, basket, drop_threshold, drop_height, wave_count, min_speed, max_speed):
        for (k, v) in kwargs.items():
            setattr(self, k, v)
        
    def active_eggs(self):
        return len(self.eggs)

    def get_highest_egg(self):
        highest_egg = None
        if len(self.eggs)>0:
            highest_egg=self.eggs[0]

        for egg in self.eggs:
            if egg.eggy < highest_egg.eggy:
                highest_egg = egg
        return highest_egg

    def get_lowest_egg(self):
        lowestEgg = None
        if len(self.eggs) > 0:
            lowestEgg = self.eggs[0]

        for egg in self.eggs:
            if egg.eggy > lowestEgg.eggy:
                lowestEgg = egg
        return lowestEgg

    def add_egg(self, eggx):
        self.total_dropped = self.total_dropped + 1
        egg = Egg(eggx, self.drop_height, self.basket, self.min_speed, self.max_speed, self.egg_radius)
        self.eggs.append(egg)

    def update(self):
        for egg in self.eggs:
            egg.update()
            if egg.broken:
                if self.observer is not None:
                    self.observer.dropped()
                self.total_broken = self.total_broken + 1
                self.eggs.remove(egg)
                self.eggs_were_broken=True
            if egg.caught:
                if self.observer is not None:
                    self.observer.caught()
                self.eggs_were_caught=True
                self.total_caught  = self.total_caught + 1
                if egg in self.eggs:
                    self.eggs.remove(egg)

    def empty(self):
        return len(self.eggs)==0

    def remove_broken_eggs(self):
        for egg in self.eggs:
            if egg.broken:
                self.eggs.remove(egg)

    def launch_more_eggs(self):
        if self.wave_count == -1 and self.get_highest_egg() is not None and self.get_highest_egg().eggy > self.drop_threshold:
            self.add_egg(randint(0.1 * self.basket.windowWidth, 0.9 * self.basket.windowWidth))
        elif self.total_dropped < self.wave_count and self.active_eggs() < 3 and self.get_highest_egg().eggy > self.drop_threshold:
            self.add_egg(randint(0.1 * self.basket.windowWidth, 0.9 * self.basket.windowWidth))

    def wave_over(self):
        return self.total_dropped >= self.wave_count and len(self.eggs) == 0

class Egg:

    def __init__(self, eggx, eggy, basket, minSpeed, maxSpeed, egg_radius):
        self.egg_radius = egg_radius
        self.eggSpeed = minSpeed + (randint(0,10)/10.0 * (maxSpeed - minSpeed))
        self.eggx = eggx
        self.eggy = eggy
        self.basket = basket
        self.broken = False
        self.caught = False

    def get_egg_x(self):
        return self.eggx

    def update(self):
        if not self.broken:
            self.eggy = self.eggy + self.eggSpeed
            if self.eggy > self.basket.baskety:
                print("Egg Broken:  Egg at ({0},{1})  and basket at ({2},{3}) - ({4},{5})".format(self.eggx, self.eggy,
                                                                                                  self.basket.basketx,
                                                                                                  self.basket.baskety,
                                                                                                  self.basket.basketx + self.basket.cellWidth,
                                                                                                  self.basket.baskety))

                self.broken = True
            if self.basket.baskety - self.eggy < 1 and self.eggx > self.basket.basketx and self.eggx < self.basket.basketx + self.basket.cellWidth:
                print("Egg Caught:  Egg at ({0},{1})  and basket at ({2},{3}) - ({4},{5})".format(self.eggx, self.eggy, self.basket.basketx, self.basket.baskety,self.basket.basketx + self.basket.cellWidth, self.basket.baskety ))
                self.caught = True