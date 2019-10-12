import unittest
from travis_demo import raechel_task
import numpy as np

class TestTask(unittest.TestCase):
    def test_task_vectors(self):
        a = np.array([1, 2])
        b = np.array([5, 6])
        output=np.array([5,7])
        obs = raechel_task.sum_minus_one(a, b)
        self.assertTrue(np.allclose(obs,output))
        
