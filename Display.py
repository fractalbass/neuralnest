import pygame


class Display:


    CELLWIDTH = 60
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARKGREEN = (0, 155, 0)
    DARKGRAY = (40, 40, 40)
    BGCOLOR = BLACK
    DISPLAYSURF = None

    def __init__(self, window_width, window_height, cell_width):
        self.window_width = window_width
        self.cell_width = cell_width
        self.window_height = window_height
        self.DISPLAYSURF = pygame.display.set_mode((window_width, window_height), 0, 24)
        pygame.display.set_caption('NeuralNest')

    def update(self, basket, eggSet, eggDropper):
        self.DISPLAYSURF.fill(self.BGCOLOR)

        #Draw Basket
        basketRect = pygame.Rect(basket.basketx, basket.baskety, self.CELLWIDTH, 6)
        pygame.draw.rect(self.DISPLAYSURF, self.DARKGREEN, basketRect)

        #Draw EggSet
        for egg in eggSet.eggs:
            pygame.draw.circle(self.DISPLAYSURF, self.WHITE, (egg.eggx, egg.eggy), 3, 1)

        pygame.display.update()
        return True