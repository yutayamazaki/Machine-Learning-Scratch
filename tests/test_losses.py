import unittest

import numpy as np

from mlscratch.models import losses


class TestBinaryCrossEntropy(unittest.TestCase):

    def setUp(self):
        self.y_true = np.array([0, 1, 0.5])
        self.y_pred = np.array([0, 1, 0.5])

    def test_return(self):
        bce = losses.binary_cross_entropy(self.y_true, self.y_pred)
        self.assertIsInstance(bce, np.float64)


class TestMeanSquaredError(unittest.TestCase):

    def setUp(self):
        self.y_true = np.array([0, 1])
        self.y_pred = np.array([0.3, 0.4])

    def test_return(self):
        mse = losses.mean_squared_error(self.y_true, self.y_pred)
        self.assertIsInstance(mse, np.float64)
