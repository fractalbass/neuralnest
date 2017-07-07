import pygame

class Basket:

    def __init__(self, WindowWidth, WindowHeight, CellWidth):
        self.windowWidth = WindowWidth
        self.windowHeight = WindowHeight
        self.cellWidth = CellWidth
        self.basketx = int(self.windowWidth / 2.0)
        self.baskety = int(self.windowHeight * 0.9)
        self.move_delta = 30

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
