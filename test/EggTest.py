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
from Display import Display

class EggTest(unittest.TestCase):

    def test_break_an_egg(self):
        display = Display(80,80,20)
        basket = Basket(display)
        egg = Egg(40, 10, basket, 1, 2)

        while not egg.broken:
            egg.update()

        self.assertTrue(egg.eggy>basket.baskety)

    def test_break_some_eggs(self):
        display = Display(80,80,20)
        basket = Basket(display)
        eggSet = EggSet(None, basket,20,10,1,1,2)
        eggSet.addEgg(10)
        eggCount = 0
        self.assertTrue(not eggSet.empty())
        self.assertTrue(not eggSet.eggs_were_broken)

        while not eggSet.empty():
            eggSet.update()
            eggSet.remove_broken_eggs()
            if eggCount < 100:
                eggSet.addEgg(10)
                eggCount = eggCount + 1

        print("Egg count: {0}".format(eggCount))
        self.assertTrue(eggCount==100)
        self.assertTrue(len(eggSet.eggs)==0)
        self.assertTrue(eggSet.eggs_were_broken)
        self.assertTrue(not eggSet.eggs_were_caught)

    def test_catch_an_egg(self):
        display = Display(80,80,20)
        basket = Basket(display)
        eggSet = EggSet(None, basket, 20, 10, 1, 1, 2)
        eggSet.addEgg(45)
        self.assertTrue(not eggSet.empty())
        self.assertTrue(not eggSet.eggs_were_broken)
        self.assertTrue(not eggSet.eggs_were_caught)

        while not eggSet.empty():
            eggSet.update()

        self.assertTrue(len(eggSet.eggs)==0)
        self.assertTrue(not eggSet.eggs_were_broken)
        self.assertTrue(eggSet.eggs_were_caught)

    def test_get_highest_egg(self):
        display = Display(80,80,20)
        basket = Basket(display)
        eggSet = EggSet(None, basket,20,10,1,1,2)

        eggSet.addEgg(10)
        for x in range(0,10):
            eggSet.update()

        eggSet.addEgg(20)
        for x in range(0, 10):
            eggSet.update()

        eggSet.addEgg(30)

        self.assertTrue(eggSet.getHighestEgg().eggy == 10)



