import pygame

class Basket:

    def __init__(self, display):
        self.surface_width = display.surface_width
        self.surface_height = display.surface_height
        self.cell_width = display.cell_width
        self.basket_x = int(self.surface_width / 2.0)
        self.basket_y = int(self.surface_height - 1)
        self.move_delta = int(display.cell_width/3)

    LEFT = 'left'
    RIGHT = 'right'

    def update(self, move):
        if move is not None:
            if move == self.LEFT:
                self.basket_x = self.basket_x - self.move_delta
                if self.basket_x < 0:
                    self.basket_x = 0
            if move == self.RIGHT:
                self.basket_x = self.basket_x + self.move_delta
                if self.basket_x > self.surface_width - self.cell_width:
                    self.basket_x = self.surface_width - self.cell_width
