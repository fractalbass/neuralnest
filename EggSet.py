

class EggSet:

    eggs = []

    def __init__(self, basket):
        self.basket = basket
        self.eggs_were_broken = False
        self.eggs_were_caught = False

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

    def addEgg(self, eggx, eggy):
        egg = Egg(eggx, eggy, self.basket)
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

class Egg:

    def __init__(self, eggx, eggy, basket):
        self.eggx = eggx
        self.eggy = eggy
        self.basket = basket
        self.broken = False
        self.caught = False

    def update(self):
        if not self.broken:
            self.eggy = self.eggy + 1
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