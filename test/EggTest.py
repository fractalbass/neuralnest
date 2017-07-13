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
        display = Display(800,800,80,80,20)
        basket = Basket(display)
        egg = Egg(40, 10, basket, 1, 2, 1)

        while not egg.broken:
            egg.update()

        self.assertTrue(egg.eggy>basket.baskety)

    def test_break_some_eggs(self):
        display = Display(800,800,80,80,20)
        basket = Basket(display)
        # observer, basket, drop_threshold, drop_height, wave_count, min_speed, max_speed):
        eggSet = EggSet(observer=None, basket=basket, drop_threshold=20,drop_height=3,wave_count=-1,min_speed=1,max_speed=2)
        eggSet.add_egg(10)
        eggCount = 0
        self.assertTrue(not eggSet.empty())
        self.assertTrue(not eggSet.eggs_were_broken)

        while not eggSet.empty():
            eggSet.update()
            eggSet.remove_broken_eggs()
            if eggCount < 100:
                eggSet.add_egg(10)
                eggCount = eggCount + 1

        print("Egg count: {0}".format(eggCount))
        self.assertTrue(eggCount==100)
        self.assertTrue(len(eggSet.eggs)==0)
        self.assertTrue(eggSet.eggs_were_broken)
        self.assertTrue(not eggSet.eggs_were_caught)

    def test_catch_an_egg(self):
        display = Display(800,800,80,80,20)
        basket = Basket(display)
        eggSet = EggSet(observer=None, basket=basket, drop_threshold=20,drop_height=3,wave_count=-1,min_speed=1,max_speed=2)
        eggSet.add_egg(45)
        self.assertTrue(not eggSet.empty())
        self.assertTrue(not eggSet.eggs_were_broken)
        self.assertTrue(not eggSet.eggs_were_caught)

        while not eggSet.empty():
            eggSet.update()

        self.assertTrue(len(eggSet.eggs)==0)
        self.assertTrue(not eggSet.eggs_were_broken)
        self.assertTrue(eggSet.eggs_were_caught)

    def test_get_highest_egg(self):
        display = Display(800,800,80,80,20)
        basket = Basket(display)
        eggSet = EggSet(observer=None, basket=basket, drop_threshold=60,drop_height=10,wave_count=-1,min_speed=1,max_speed=2)

        eggSet.add_egg(10)
        for x in range(0,10):
            eggSet.update()

        eggSet.add_egg(20)
        for x in range(0, 10):
            eggSet.update()

        eggSet.add_egg(30)

        self.assertTrue(eggSet.get_highest_egg().eggy == 10)



