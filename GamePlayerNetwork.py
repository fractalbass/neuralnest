import pandas as pd
from keras.models import Model
from keras.layers import Dense, Input
from keras.models import model_from_json
import matplotlib.pyplot as plt
import numpy as np


class GamePlayerNetwork:

    def __init__(self, screen_width, screen_height):
        self.update_learning_graph_count = 0

        inputs = Input(shape=(screen_width*screen_height,))
        x = Dense(10, activation='sigmoid')(inputs)
        predictions = Dense(1, activation='sigmoid')(x)
        model = Model(inputs=inputs, outputs=predictions)
        model.summary()
        model.compile(optimizer='rmsprop',
                      loss='mean_squared_error',
                      metrics=['accuracy'])
        self.model = model
        self.plot = None
        self.results = None

    def train(self, filename):
        df = pd.read_csv(filename)
        training_set = df.values[:, 0:400]
        target_set = df.values[:,401]
        self.results = self.model.fit(training_set, target_set, batch_size=100, epochs=5000, verbose=1)

    def save_model(self, filename):
        # serialize model to JSON
        model_json = self.model.to_json()
        json_name = "{0}.json".format(filename)
        h5_name = "{0}.h5".format(filename)
        with open(json_name, "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        self.model.save_weights(h5_name)
        print("Saved model to disk")

    def load_model(self,filename):
        # load json and create model
        json_file = open('{0}.json'.format(filename), 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_model_json)
        # load weights into new model
        self.model.load_weights("{0}.h5".format(filename))
        print("Loaded model from disk")

    def display_training_results(self):
        plt.plot(self.results.history['loss'])
        #plt.plot(self.results.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.show(block=True)

    def get_player_action(self, screen_array):

        o = self.model.predict(screen_array.reshape(1,400), batch_size=10, verbose=1)

        if o<0.5:
            return 'left'
        elif o>=0.5:
            return 'right'
        else:
            return None

