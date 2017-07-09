from random import randint
from random import randrange

class EggSet:

    eggs = []

    def __init__(self, basket, dropHeight, waveCount, minSpeed, maxSpeed):
        self.basket = basket
        self.waveCount = waveCount
        self.eggs_were_broken = False
        self.eggs_were_caught = False
        self.dropHeight = 240
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.totalDropped = 0

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

    def addEgg(self, eggx, eggy, minSpeed, maxSpeed):
        self.totalDropped = self.totalDropped + 1
        egg = Egg(eggx, eggy, self.basket, minSpeed, maxSpeed)
        self.eggs.append(egg)

    def update(self):
        for egg in self.eggs:
            egg.update()
            if egg.broken:
                self.eggs_were_broken=True
            if egg.caught:
                self.eggs_were_caught=True
                self.eggs.remove(egg)

    def empty(self):
        return len(self.eggs)==0

    def remove_broken_eggs(self):
        for egg in self.eggs:
            if egg.broken:
                self.eggs.remove(egg)

    def launch_more_eggs(self):
        if self.totalDropped < self.waveCount and self.activeEggs() < 3 and self.getHighestEgg().eggy > self.dropHeight:
            self.addEgg(randint(200, 440), 20, self.minSpeed, self.maxSpeed)

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