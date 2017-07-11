import NeuralNest
from random import randint
import pygame
import pygame.surfarray
import numpy as np
from GamePlayerNetwork import GamePlayerNetwork


class NeuralNestAIPlayer:

    def __init__(self):
        self.nnest = None
        self.surface_array = None
        self.network = GamePlayerNetwork()
        self.mode = 'training'

    def get_neural_nest(self):
        return self.nnest

    def play(self):
        self.nnest = NeuralNest.NeuralNest(self)

        #  Set  up the AI Player
        self.nnest.get_player_action = self.get_ai_action
        #  Setup grabbing the screen for training purposes.
        # set our on_screen_update function to always get called whenever the screen updated

        pygame.display.update = self.function_combine(pygame.display.update, self.on_screen_update)
        # FYI the screen can also be modified via flip, so this might be needed for some games
        pygame.display.flip = self.function_combine(pygame.display.flip, self.on_screen_update)

        print("Loading game")
        caught, dropped = self.nnest.run(1000)
        print("Game complete: caught={0}  dropped={1}".format(caught, dropped))

    # function that we can give two functions to and will return us a new function that calls both
    def function_combine(self, screen_update_func, our_intercepting_func):
        def wrap(*args, **kwargs):
            screen_update_func(*args,
                               **kwargs)  # call the screen update func we intercepted so the screen buffer is updated
            our_intercepting_func()  # call our own function to get the screen buffer

        return wrap

    def on_screen_update(self):
        if self.mode=='training':
            self.surface_array = pygame.surfarray.array2d(pygame.transform.scale(pygame.display.get_surface(),(80,80))).ravel()
            newArray = []
            for x in self.surface_array:
                newArray.append(int(x))

            self.network.train(newArray, self.nnest.get_best_player_action())

    # The game will call us when it is time for a move
    def get_ai_action(self):
            result = self.network.get_player_action(self.surface_array)
            return result

    def caught(self):
        print("Caught in agent.")


    def dropped(self):
        print("Dropped in agent.")

if __name__ == "__main__":
    ai_player = NeuralNestAIPlayer()
    ai_player.play()

