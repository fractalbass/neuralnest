from random import randint
from random import randrange

class EggSet:

    eggs = []

    def __init__(self, observer, basket, drop_threshold, drop_height, wave_count, min_speed, max_speed):
        self.observer = observer
        self.basket = basket
        self.waveCount = wave_count
        self.eggs_were_broken = False
        self.eggs_were_caught = False
        self.dropThreshold = drop_threshold
        self.dropHeight = drop_height
        self.minSpeed = min_speed
        self.maxSpeed = max_speed
        self.totalDropped = 0
        self.total_broken = 0
        self.total_caught = 0

    def activeEggs(self):
        return len(self.eggs)

    def getHighestEgg(self):
        highestEgg = None
        if len(self.eggs)>0:
            highestEgg=self.eggs[0]

        for egg in self.eggs:
            if egg.eggy < highestEgg.eggy:
                highestEgg = egg
        return highestEgg

    def getLowestEgg(self):
        lowestEgg = None
        if len(self.eggs) > 0:
            lowestEgg = self.eggs[0]

        for egg in self.eggs:
            if egg.eggy > lowestEgg.eggy:
                lowestEgg = egg
        return lowestEgg

    def addEgg(self, eggx):
        self.totalDropped = self.totalDropped + 1
        egg = Egg(eggx, self.dropHeight, self.basket, self.minSpeed, self.maxSpeed)
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
        if self.waveCount == -1 and self.getHighestEgg().eggy > self.dropThreshold:
            self.addEgg(randint(0.1 * self.basket.windowWidth, 0.9 * self.basket.windowWidth))
        elif self.totalDropped < self.waveCount and self.activeEggs() < 3 and self.getHighestEgg().eggy > self.dropThreshold:
            self.addEgg(randint(0.1 * self.basket.windowWidth, 0.9 * self.basket.windowWidth))

    def wave_over(self):
        return self.totalDropped >= self.waveCount and len(self.eggs) == 0

class Egg:

    def __init__(self, eggx, eggy, basket, minSpeed, maxSpeed):
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
            if self.basket.baskety - self.eggy < 6 and self.eggx > self.basket.basketx and self.eggx < self.basket.basketx + self.basket.cellWidth:
                print("Egg Caught:  Egg at ({0},{1})  and basket at ({2},{3}) - ({4},{5})".format(self.eggx, self.eggy, self.basket.basketx, self.basket.baskety,self.basket.basketx + self.basket.cellWidth, self.basket.baskety ))
                self.caught = True