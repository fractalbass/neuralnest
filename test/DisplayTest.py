#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  July 7, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import unittest
from Display import Display

class EggTest(unittest.TestCase):

    def display_black_test(self):
        d = Display(20,20,1)
        d.drawBox(0,0,20,20,Display.BLACK)
        m = d.getDisplayMatrix()
        self.assertTrue(m.shape == (20,20,3))
        for r in m:
            for c in r:
                self.assertTrue(c==Display.WHITE)
        
    def display_white_test(self):
        d = Display(20,20,1)
        d.draw_box(0,0,20,20,Display.WHITE)
        m = d.get_display_matrix()
        self.assertTrue(m.shape==(2,2,3))
        self.assertTrue(m.eachPixel() == Display.WHITE)

    def display_tupple_array_test(self):
        d = Display(20,20,1)
        d.drawCheckboard(0,0,20,20, Display.WHITE, Display.BLACK)
        a = d.get_display_tupple_array()
        for i in range(0,400)
            if i%2==0:
                self.assertTrue(a[i] == Display.WHITE)
            else:
                self.assertTrue(a[i] == Display.BLACK)

    def display_grayscale_array_test(self):
        d = Display(20,20,1)
        d.drawCheckboard(0,0,20,20, Display.WHITE, Display.BLACK)
        a = d.get_display_grayscale_array()
        for i in range(0,400):
            if i%2==0:
                self.assertTrue(a[i] == 255)
            else:
                self.assertTrue(a[i] == 0)

