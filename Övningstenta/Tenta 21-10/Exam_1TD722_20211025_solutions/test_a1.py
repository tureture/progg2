"""
m1_test
"""

import unittest

from m1 import *

class Test(unittest.TestCase):
    
    def test_length_longest(self):
        lista = []
        self.assertEqual(length_longest(lista), 0)
        lista = [1,2,3]
        self.assertEqual(length_longest(lista), 3)
        lista = [1,[2,3],3]
        self.assertEqual(length_longest(lista), 3)
        lista = [1,2,[3,4,5,6]]
        self.assertEqual(length_longest(lista), 4)
        lista = [[1,2,3,4], [], 2, [1,2,3]]
        self.assertEqual(length_longest(lista), 4)
        lista = [[1,2,3,4], [], 2, [1,2,3,4,5]]
        self.assertEqual(length_longest(lista), 5)
        lista = [[[1,2]]]
        self.assertEqual(length_longest(lista), 2)
        lista = [[1,[1,2,3,4,5,6],3,4], [], 2, [1,2,3,4,5]]
        lista = [[[1,2,3]], [1]]
        self.assertEqual(length_longest(lista), 3)
        
if __name__ == "__main__":
    unittest.main()