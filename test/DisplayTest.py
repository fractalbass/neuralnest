#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  July 7, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import unittest
from Display import Display
from Basket import Basket
import pygame
import numpy as np


class DisplayTest(unittest.TestCase):

    def test_display_black(self):
        d = Display(800, 800, 20, 20, 1)
        d.draw_box(0,0,20,20,Display.BLACK)
        d.update_display()
        pygame.event.get()
        m = d.get_surface_matrix()
        self.assertTrue(m.shape == (20, 20, 3))
        for r in m:
            for c in r:
                self.assertTrue(np.all(c == 0))

    def test_display_white(self):
        d = Display(800, 800, 20, 20, 1)
        d.draw_box(0, 0, 20, 20, Display.WHITE)
        d.update_display()
        pygame.event.get()
        m = d.get_surface_matrix()
        self.assertTrue(m.shape == (20, 20, 3))
        for r in m:
            for c in r:
                self.assertTrue(np.all(c == 255))

    def test_display_tupple_array(self):
        d = Display(210, 200, 3, 3, 1)
        d.draw_checkerboard(0, 0, 3, 3, Display.WHITE, Display.BLACK)
        d.update_display()
        pygame.event.get()
        a = d.get_surface_array()
        print("A = ".format(a))
        self.assertTrue(a.shape == (9, 3))
        for i in range(0, 9):
                print("a[{0}]={1}".format(i, a[i]))
                if i % 2 == 0:
                    self.assertTrue(np.all(a[i] == 0))
                else:
                    self.assertTrue(np.all(a[i] == 255))

    def test_display_grayscale_array(self):
        pygame.init()
        d = Display(300, 300, 3, 3, 1)
        d.draw_checkerboard(0, 0, 3, 3, Display.WHITE, Display.BLACK)
        d.update_display()
        pygame.event.get()
        a = d.get_surface_grayscale_array()
        print("A =".format(a))
        self.assertTrue(a.size == 9)
        for i in range(0, 9):
            print(a[i])
            if (i % 2) == 0:
                self.assertTrue(a[i] == 0)
            else:
                self.assertTrue(a[i] == 1)

    def test_display_grayscale_2(self):
        pygame.init()
        d = Display(200, 200, 20, 20, 3)
        b = Basket(d)
        b.basket_x = 15
        b.cell_width = 5
        pygame.event.get()
        d.update(b, None)
        pygame.event.get()
        a = d.get_surface_grayscale_array()
        self.assertTrue(a[399] == 1)
        self.assertTrue(a[398] == 1)
        self.assertTrue(a[397] == 1)
        self.assertTrue(a[396] == 1)
        self.assertTrue(a[395] == 1)
