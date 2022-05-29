"""
Test of append (task A5)
"""

import unittest

from m3 import *

class Test(unittest.TestCase):
    
    def test_append(self):
        lst = LinkedList()
        self.assertEqual(str(lst), '()')
        lst.append(1)
        self.assertEqual(str(lst), '(1)')
        lst.append('x')
        self.assertEqual(str(lst), '(1, x)')
        lst.append(2)
        self.assertEqual(str(lst), '(1, x, 2)')
        lst.append([5,6,7])
        self.assertEqual(str(lst), '(1, x, 2, [5, 6, 7])')


        
 
        
        
if __name__ == "__main__":
    unittest.main()

    