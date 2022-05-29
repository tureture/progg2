"""
Test of is_omorph (task A8)
"""

import unittest

from m3 import *

class Test(unittest.TestCase):
        
    def test_is_omorph(self):          
        t1 = BST()
        t2 = BST()
        self.assertEqual(t1.is_omorph(t2), True)
        t1.insert(1)
        t1.insert(2)
        t2.insert(2)
        t2.insert(1)
        self.assertEqual(t1.is_omorph(t2), False)
        t1 = BST()
        t2 = BST()        
        for x in [2,1,3]:
            t1.insert(x)
            t2.insert(x)
        self.assertEqual(t1.is_omorph(t2), True)
        t1.insert(9)
        self.assertEqual(t1.is_omorph(t2), False)
        t2.insert(8)
        self.assertEqual(t1.is_omorph(t2), True)
        t1.insert(4)
        self.assertEqual(t1.is_omorph(t2), False)
        t2.insert(5)
        self.assertEqual(t1.is_omorph(t2), True)  
        
        
if __name__ == "__main__":
    unittest.main()

    