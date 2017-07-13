import pygame
import datetime
import numpy as np

class Display:

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARKGREEN = (0, 155, 0)
    DARKGRAY = (40, 40, 40)
    BGCOLOR = BLACK
    BLACK = (0,0,0)
    text_surface_height = 20

    def __init__(self, window_width, window_height, surface_width, surface_height, cell_width):
        pygame.display.init()
        self.window_width = window_width
        self.cell_width = cell_width
        self.surface_width = surface_width
        self.surface_height = surface_height
        self.window_height = window_height
        self.text_surface = pygame.surface.Surface((window_width, self.text_surface_height), 0, 24)
        self.display_surface = pygame.surface.Surface((surface_width,surface_height))
        self.display_window = pygame.display.set_mode((window_width,window_height), 0, 24)
        pygame.display.set_caption('NeuralNest')
        self.display_surface.fill(self.BGCOLOR)
        pygame.display.update()

    def update(self, basket, egg_set):
        self.display_surface.fill(self.BGCOLOR)

        # Draw Basket
        if basket is not None:
            self.draw_box(basket.basketx, basket.baskety, basket.cellWidth, 1, self.DARKGREEN)

        # Draw EggSet
        if egg_set is not None:
            for egg in egg_set.eggs:
                self.draw_box(egg.eggx, egg.eggy, egg.egg_radius, egg.egg_radius, self.WHITE)

            # Display score
            self.display_text_top("{0}:{1}".format(egg_set.total_caught, egg_set.total_broken))

        self.update_display()
        return True

    def update_display(self):
        self.display_window.blit(pygame.transform.scale(self.display_surface, (self.window_width, self.window_height +
                                                                               self.text_surface_height)), (0, self.text_surface_height))
        self.display_window.blit(self.text_surface, (0, 0))
        pygame.display.update()

    def draw_circle(self, x, y, radius, color, width):
        pygame.draw.circle(self.display_surface, color, (int(x), int(y)), radius, width)

    def draw_box(self, x, y, width, height, color):
        basket_rect = pygame.Rect((x, y), (width, height))
        pygame.draw.rect(self.display_surface, color, basket_rect)

    def draw_checkerboard(self, x, y, width, height, c1, c2):
        for xi in range(x, x + width):
            for yi in range(y, y + height):
                c = c1
                if (xi + yi) % 2 == 0:
                    c = c2
                self.draw_box(xi, yi, 1, 1, c)

    def show_wave_start(self, wave):
        if wave is None:
            msg = "Ready?"
        else:
            msg = "{0}:{1}".format(wave.waveName, wave.waveCount)
        self.display_text_middle(msg)

    def show_wave_over(self, eggSet):
        msg = "Caught: {0}".format(eggSet.totalDropped)
        self.display_text_middle(msg)

    def text_objects(self, text, font):
        text_surface = font.render(text, False, self.RED)
        return text_surface, text_surface.get_rect()

    def display_text_top(self, msg):
        self.text_surface.fill(self.BGCOLOR)
        score_text = pygame.font.Font("/Library/Fonts/Courier New.ttf", 18)
        scoreSurf, scoreRect = self.text_objects(msg, score_text)
        self.text_surface.blit(scoreSurf, scoreRect)

    def display_text_middle(self, msg):
        self.text_surface.fill(self.BGCOLOR)
        score_text = pygame.font.Font("/Library/Fonts/Courier New.ttf", 18)
        text_surf, text_rect = self.text_objects(msg, score_text)
        text_rect.center = ((self.window_width / 2), 5)
        text_rect.top = 2
        self.text_surface.blit(text_surf, text_rect)
        self.update_display()
        self.wait_for_key()

    def wait_for_key(self):
        start = datetime.datetime.utcnow()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: run = False
                if e.type == pygame.KEYDOWN:
                    return
            if (datetime.datetime.utcnow() - start).total_seconds() > 3:
                return

    def get_surface_array(self):
        self.update_display()
        surface_array = pygame.surfarray.array3d(self.display_surface)
        return np.reshape(surface_array, (self.surface_width*self.surface_height, 3))

    def get_surface_matrix(self):
        self.update_display()
        surface_array = pygame.surfarray.array3d(self.display_surface)
        return surface_array

    def get_surface_grayscale_array(self):
        gray_scale_array = []
        surface_array = pygame.surfarray.array3d(self.display_surface)
        new_surface = np.reshape(surface_array, (self.surface_width * self.surface_height, 3))
        for x in new_surface:
            c = ((int(x[0])+int(x[1])+int(x[2]))/(255*3))
            gray_scale_array.append(c)
        return np.array(gray_scale_array, dtype=float)
