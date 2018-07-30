import test
import nose
import collections
import numpy as np

from  RNNmodel import basic,rnn_net
import unittest

class TruthTest(unittest.TestCase):
    def setUp(self):
      self.basic=basic()
  
    def test_get_releation_layers(self):
      x = np.array([[0, 1, 1, 1, 1, 1],
                    [0, 0, 1, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0]], np.int32)
      y = {'a': {'Dense': [7]}, 'b': {'Dense': [5]}, 'c': {'LSTM': [4, False]}, 'd': {'GRU': [6, False]},
           'e': {'LSTM': [4, False]}, 'f': {'LSTM': [8, False]}}
  
      result=collections.OrderedDict([('b', ['a']), ('c', ['a', 'b']),('d', ['a', 'b', 'c']), ('e', ['a', 'b', 'c', 'd']), ('f', ['a', 'b', 'c', 'd', 'e'])])
      self.assertEqual(self.basic.get_releation_layers(x,y),result)


if __name__ == '__main__':
    unittest.main()

