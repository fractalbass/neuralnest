import pygame


class User:

    LEFT = 'left'
    RIGHT = 'right'
    QUIT = 'quit'
    last_move = ''

    def __init__(self):
        print("Initializing user.")

    def get_player_action(self):
        self.last_move = ''
        for i in pygame.event.get():
            if i.type == self.QUIT:
                return self.QUIT
            key = pygame.key.get_pressed()
            for i in range(0, len(key)):
                if key[i] == 1:
                    if key[pygame.K_LEFT] != 0:
                        self.last_move=self.LEFT
                    if key[pygame.K_RIGHT] != 0:
                        self.last_move=self.RIGHT
                    if key[pygame.K_DOWN] != 0:
                        self.last_move = ""
                    if key[pygame.K_q] != 0:
                        self.last_move=self.QUIT
        return self.last_move