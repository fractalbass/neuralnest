import pygame

class Basket:

    def __init__(self, display):
        self.windowWidth = display.window_width
        self.windowHeight = display.window_height
        self.cellWidth = display.cell_width
        self.basketx = int(self.windowWidth / 2.0)
        self.baskety = int(self.windowHeight * 0.9)
        self.move_delta = int(display.cell_width/3)

    LEFT = 'left'
    RIGHT = 'right'

    def update(self, move):
        if move is not None:
            if move == self.LEFT:
                self.basketx = self.basketx - self.move_delta
                if self.basketx < 0:
                    self.basketx = 0
            if move == self.RIGHT:
                self.basketx = self.basketx + self.move_delta
                if self.basketx > self.windowWidth - self.cellWidth:
                    self.basketx = self.windowWidth - self.cellWidth
