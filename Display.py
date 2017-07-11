import pygame
import datetime
class Display:

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARKGREEN = (0, 155, 0)
    DARKGRAY = (40, 40, 40)
    BGCOLOR = BLACK
    BLACK = (0,0,0)

    def __init__(self, window_width, window_height, cell_width):
        self.window_width = window_width
        self.cell_width = cell_width
        self.window_height = window_height
        self.display_surface = pygame.surface.Surface((80,80))
        self.display_window = pygame.display.set_mode((800,800),0,24)
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
                self.draw_circle(egg.eggx, egg.eggy, 3, self.WHITE, 1)

            # Display score
            self.display_text_top("{0}:{1}".format(egg_set.total_caught, egg_set.total_broken))

        self.update_display()
        return True

    def update_display(self):
        self.display_window.blit(pygame.transform.scale(self.display_surface, (800, 800)), (0, 0))
        pygame.display.update()

    def draw_circle(self, x, y, radius, color, width):
        pygame.draw.circle(self.display_surface, color, (int(x), int(y)), radius, width)

    def draw_box(self, x, y, width, height, color):
        basket_rect = pygame.Rect((x, y), (width, height))
        pygame.draw.rect(self.display_surface, color, basket_rect)

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
        score_text = pygame.font.Font("/Library/Fonts/Courier New.ttf", 12)
        scoreSurf, scoreRect = self.text_objects(msg, score_text)
        self.display_surface.blit(scoreSurf, scoreRect)

    def display_text_middle(self, msg):
        self.display_surface.fill(self.BGCOLOR)
        self.score_text = pygame.font.Font("/Library/Fonts/Courier New.ttf", 18)
        text_surf, text_rect = self.text_objects(msg, self.score_text)
        text_rect.center = ((self.window_width / 2), (self.window_height / 2))
        self.display_surface.blit(text_surf, text_rect)
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
