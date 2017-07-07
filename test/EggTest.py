#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  July 7, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import unittest
from EggSet import Egg
from EggSet import EggSet
from Basket import Basket

class EggTest(unittest.TestCase):

    def test_break_an_egg(self):
        basket = Basket(640, 480, 40)
        egg = Egg(320, 10, basket)

        while not egg.broken:
            egg.update()

        self.assertTrue(egg.eggy>basket.baskety)

    def test_break_some_eggs(self):
        basket = Basket(640, 480, 40)
        eggSet = EggSet(basket)
        eggSet.addEgg(10,10)
        eggCount = 0
        self.assertTrue(not eggSet.empty())
        self.assertTrue(not eggSet.eggs_were_broken)

        while not eggSet.empty():
            eggSet.update()
            eggSet.remove_broken_eggs()
            if eggCount < 100:
                eggSet.addEgg(320,10)
                eggCount = eggCount + 1

        print("Egg count: {0}".format(eggCount))
        self.assertTrue(eggCount==100)
        self.assertTrue(len(eggSet.eggs)==0)
        self.assertTrue(eggSet.eggs_were_broken)
        self.assertTrue(not eggSet.eggs_were_caught)

    def test_catch_an_egg(self):
        basket = Basket(640,480,40)
        eggSet = EggSet(basket)
        eggSet.addEgg(330,10)
        self.assertTrue(not eggSet.empty())
        self.assertTrue(not eggSet.eggs_were_broken)
        self.assertTrue(not eggSet.eggs_were_caught)

        while not eggSet.empty():
            eggSet.update()

        self.assertTrue(len(eggSet.eggs)==0)
        self.assertTrue(not eggSet.eggs_were_broken)
        self.assertTrue(eggSet.eggs_were_caught)

    def test_get_highest_egg(self):
        basket = Basket(640,480,40)
        eggSet = EggSet(basket)
        eggSet.addEgg(330,10)
        eggSet.addEgg(330, 20)
        eggSet.addEgg(330, 30)

        self.assertTrue(eggSet.getHighestEgg().eggy == 10)



