#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  July 7, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

import unittest
import numpy as np
from TrainingData import TrainingData


class TrainingDataTest(unittest.TestCase):

    def test_append_training_data(self):

        td = TrainingData()

        i = np.array([1, 2, 3, 4, 5])
        o = 6

        td.append_training_data(i, o)
        print("Cols: {0}".format(len(td.dataFrame.columns)))
        self.assertTrue(td.dataFrame.shape == (1, 6))

    def test_append_training_data_multiple_rows(self):

        td = TrainingData()

        i = np.array([1, 2, 3, 4, 5])
        o = 6

        td.append_training_data(i, o)
        td.append_training_data(i, o)
        td.append_training_data(i, o)
        td.append_training_data(i, o)
        td.append_training_data(i, o)

        print("Cols: {0}".format(len(td.dataFrame.columns)))
        self.assertTrue(td.dataFrame.shape == (5, 6))

    def test_save_and_load_training_data(self):
        td = TrainingData()
        i = np.array([1, 2, 3, 4, 5])

        td.append_training_data(i, 1)
        td.append_training_data(i, 2)
        td.append_training_data(i, 3)
        td.append_training_data(i, 4)
        td.append_training_data(i, 5)

        td.save_csv("test_file.csv")

        td2 = TrainingData()
        td2.load_csv("test_file.csv")

        self.assertTrue(td.dataFrame.equals(td2.dataFrame))
