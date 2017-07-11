import pandas as pd
from keras.models import Model
from keras.layers import Dense, Input
import matplotlib.pyplot as plt
import numpy as np

class GamePlayerNetwork:



    def __init__(self):
        self.update_learning_graph_count = 0

        inputs = Input(shape=(6400,))
        x = Dense(6400, activation='sigmoid')(inputs)
        x = Dense(10, activation='sigmoid')(x)
        predictions = Dense(1, activation='sigmoid')(x)
        model = Model(inputs=inputs, outputs=predictions)
        model.summary()
        model.compile(optimizer='rmsprop',
                      loss='mean_squared_error',
                      metrics=['accuracy'])
        self.model = model
        self.plot = None

    def train(self, screen_array, desired_action):
        if desired_action == 0:
            o = 0
        elif desired_action == 1:
            o = 1
        else:
            o = 0.5


        ta = [screen_array]
        results = self.model.fit(np.array(ta), np.array([o]),0,0)
        self.update_learning_graph_count = self.update_learning_graph_count + 1
        if self.update_learning_graph_count > 10:
             self.update_learning_graph_count = 0
             results_df = pd.DataFrame(results.history)
             print("Results history: {0}".format(results_df))
    def get_player_action(self, screen_array):
        ta = [screen_array]

        o = self.model.predict(np.array(ta),1)

        if o<0.33:
            return 'left'
        elif o>0.66:
            return 'right'
        else:
            return None

