"""
Test of __setitem__ (task A7)
"""

import unittest

from m3 import *

class Test(unittest.TestCase):
        
    def test___setitem__(self):
        lst = LinkedList([1])
        lst[0] = 2
        self.assertEqual(str(lst), '(2)')
        lst = LinkedList([1, 2])
        lst[1] = 9
        self.assertEqual(lst[1], 9)
        lst = LinkedList([1, 2, 3])
        lst[0] = 4
        lst[1] = 5
        lst[2] = 6
        self.assertEqual('(4, 5, 6)', str(lst))
        with self.assertRaises(ExamException):
            lst[3] = 999
        with self.assertRaises(ExamException):
            lst[-1] = 999
            
        
        
if __name__ == "__main__":
    unittest.main()

    
