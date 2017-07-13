import pandas as pd
import numpy as np


class TrainingData():

    dataFrame = None

    def append_training_data(self, i, t):
        assert isinstance(i, np.ndarray)
        s = np.append(i, t)
        if self.dataFrame is None:
            self.dataFrame = pd.DataFrame(data=[s])
        else:
            self.dataFrame = self.dataFrame.append(pd.DataFrame(data=[s]))

    def save_csv(self, filename):
        if self.dataFrame is not None:
            self.dataFrame.index = range(len(self.dataFrame))
            self.dataFrame.to_csv(filename, header=None)

    def load_csv(self, filename):
        if self.dataFrame is not None:
            self.dataFrame = pd.DataFrame()
        self.dataFrame = pd.read_csv(filename, header=None, index_col=0)
        self.dataFrame.columns = range(0, len(self.dataFrame.columns))
