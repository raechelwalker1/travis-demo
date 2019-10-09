import unittest
from travis_demo import task
import numpy as np


class TestTask(unittest.TestCase):
    
    def test_task_vectors(self):
        a = np.array([1, 2, 3, 4])
        b = np.array([5, 6, 7, 8])
        exp = np.array([7, 9, 11, 13])
        obs = task.sum_plus_one(a, b)
        self.assertTrue(np.allclose(exp, obs))

    def test_task_scalars(self):
        a = 1
        b = 2
        exp = 4
        obs = task.sum_plus_one(a, b)
        self.assertAlmostEqual(exp, obs)

