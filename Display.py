import pygame
import time
class Display:

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARKGREEN = (0, 155, 0)
    DARKGRAY = (40, 40, 40)
    BGCOLOR = BLACK

    def __init__(self, window_width, window_height, cell_width):
        self.window_width = window_width
        self.cell_width = cell_width
        self.window_height = window_height
        self.DISPLAYSURF = pygame.display.set_mode((window_width, window_height),0,24)
        pygame.display.set_caption('NeuralNest')
        self.DISPLAYSURF.fill(self.BGCOLOR)
        pygame.display.update()

    def update(self, basket, eggSet):
        self.DISPLAYSURF.fill(self.BGCOLOR)

        #Draw Basket
        basketRect = pygame.Rect(basket.basketx, basket.baskety, basket.cellWidth, 6)
        pygame.draw.rect(self.DISPLAYSURF, self.DARKGREEN, basketRect)

        #Draw EggSet
        for egg in eggSet.eggs:
            pygame.draw.circle(self.DISPLAYSURF, self.WHITE, (egg.eggx, int(egg.eggy)), 3, 1)

        pygame.display.update()
        return True

    def show_wave_start(self, wave):
        msg = "Wave: {0}  Eggs: {1}".format(wave.waveName, wave.waveCount)
        self.displayText(msg)

    def show_wave_over(self, eggSet):
        msg = "Number of Eggs Caught: {0}".format(eggSet.totalDropped)
        self.displayText(msg)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.RED)
        return textSurface, textSurface.get_rect()

    def displayText(self, msg):
        self.DISPLAYSURF.fill(self.BGCOLOR)
        self.largeText = pygame.font.Font(None, 25)
        self.TextSurf, self.TextRect = self.text_objects(msg, self.largeText)
        self.TextRect.center = ((self.window_width / 2), (self.window_height / 2))
        self.DISPLAYSURF.blit(self.TextSurf, self.TextRect)
        pygame.display.update()
        self.wait_for_key()

    def wait_for_key(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: run = False
                if e.type == pygame.KEYDOWN:
                    return