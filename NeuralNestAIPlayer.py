from NeuralNest import NeuralNest
from random import randint
import pygame
import pygame.surfarray
import numpy as np
import pandas
from TrainingData import TrainingData
from GamePlayerNetwork import GamePlayerNetwork


class NeuralNestAIPlayer:

    LEARNING = 'learning'
    PLAYING = 'playing'

    def __init__(self):
        self.nnest = None
        self.surface_array = None
        self.network = None
        self.mode = 'training'
        self.training_data = TrainingData()

    def get_neural_nest(self):
        return self.nnest

    def gather_data(self, FPS):
        self.nnest = NeuralNest(observer=self,
                                window_width=800,
                                window_height=800,
                                surface_width=20,
                                surface_height=20,
                                drop_height=0,
                                drop_threshold=17,
                                basket_width=5,
                                min_speed=1,
                                max_speed=2,
                                egg_radius=1)
        self.nnest.FPS = FPS
        pygame.display.update = self.function_combine(pygame.display.update, self.on_screen_update)

        print("Loading game")
        caught, dropped = self.nnest.run(300)
        self.training_data.save_csv("one_thousand_run.csv")

        print("Game complete: caught={0}  dropped={1}".format(caught, dropped))

    # function that we can give two functions to and will return us a new function that calls both
    def function_combine(self, screen_update_func, our_intercepting_func):
        def wrap(*args, **kwargs):
            screen_update_func(*args,
                               **kwargs)  # call the screen update func we intercepted so the screen buffer is updated
            our_intercepting_func()  # call our own function to get the screen buffer

        return wrap

    def on_screen_update(self):
        if self.mode == self.LEARNING:
            surface_array = self.nnest.display.get_surface_grayscale_array()
            assert(len(surface_array) > 0)
            best_action = self.nnest.get_best_player_action()
            self.training_data.append_training_data(surface_array, best_action)

    # The game will call us when it is time for a move
    def get_ai_action(self):
        if self.mode == self.PLAYING:
            surface_array = self.nnest.display.get_surface_grayscale_array()
            result = self.network.get_player_action(surface_array)
        return result

    def caught(self):
        return

    def dropped(self):
        return

    def learn(self):
        network = GamePlayerNetwork(20, 20)
        network.train("synthetic_training_data.txt")
        network.save_model("trained_model")
        network.display_training_results()
        network.plot_model()

    def play(self):
        self.network = GamePlayerNetwork(20, 20)
        self.network.load_model("trained_model")

        self.nnest = NeuralNest(observer=self,
                                window_width=800,
                                window_height=800,
                                surface_width=20,
                                surface_height=20,
                                drop_height=0,
                                drop_threshold=17,
                                basket_width=5,
                                min_speed=1,
                                max_speed=2,
                                egg_radius=1)
        self.nnest.FPS = 20

        self.nnest.get_player_action = self.get_ai_action

        pygame.display.update = self.function_combine(pygame.display.update, self.on_screen_update)

        print("Loading game")
        caught, dropped = self.nnest.run(100)
        print("Game complete: caught={0}  dropped={1}".format(caught, dropped))


if __name__ == "__main__":
    ai_player = NeuralNestAIPlayer()
    ai_player.mode = NeuralNestAIPlayer.LEARNING
    # ai_player.gather_data(60)
    # ai_player.learn()
    ai_player.mode = 'playing'
    ai_player.play()
