# https://docs.python.org/3/library/unittest.html
"""
Unittests for the binary search tree methods

"""

import unittest

from bst import *
from linked_list import *

class Test(unittest.TestCase):
    
    def test_height(self):
        bst = BST()
        self.assertEqual(bst.height(), 0)
        bst.insert(5)
        self.assertEqual(bst.height(), 1)
        bst.insert(2)        
        self.assertEqual(bst.height(), 2)
        bst.insert(1)
        self.assertEqual(bst.height(), 3)
        bst.insert(7)
        self.assertEqual(bst.height(), 3)
        bst.insert(8)
        self.assertEqual(bst.height(), 3)
        bst.insert(9)
        self.assertEqual(bst.height(), 4)        



    def test_remove(self):
        bst = BST()
        for x in [10, 5, 3, 8, 1, 4, 6, 9, 2, 7]:
            bst.insert(x)
        bst.remove(2)
        self.assertEqual(str(bst), '<1, 3, 4, 5, 6, 7, 8, 9, 10>')
        bst.remove(1)
        self.assertEqual(str(bst), '<3, 4, 5, 6, 7, 8, 9, 10>')
        bst.remove(4)
        self.assertEqual(str(bst), '<3, 5, 6, 7, 8, 9, 10>')
        bst.remove(6)
        self.assertEqual(str(bst), '<3, 5, 7, 8, 9, 10>')
        bst.remove(2)
        self.assertEqual(str(bst), '<3, 5, 7, 8, 9, 10>')
        bst.remove(5)
        self.assertEqual(str(bst), '<3, 7, 8, 9, 10>')
        bst.remove(3)
        self.assertEqual(str(bst), '<7, 8, 9, 10>')   
        bst.remove(7)
        self.assertEqual(str(bst), '<8, 9, 10>')
        bst.remove(8)
        self.assertEqual(str(bst), '<9, 10>')
        bst.remove(9)
        self.assertEqual(str(bst), '<10>') 
        bst.remove(10)
        self.assertEqual(str(bst), '<>')


 
    def test___str__(self):
        bst = BST()
        self.assertEqual(str(bst), '<>')
        bst.insert(3)
        self.assertEqual(str(bst), '<3>')
        bst.insert(2)
        self.assertEqual(str(bst), '<2, 3>')

    def test_to_list(self):
        bst = BST()
        self.assertEqual(bst.to_list(), [])
        bst.insert(3)
        self.assertEqual(bst.to_list(), [3])
        bst.insert(2)
        self.assertEqual(bst.to_list(), [2, 3])
        

    def test_to_LinkedList(self):
        bst = BST()
        lst = LinkedList()
        for x in [5, 3, 8, 1, 4, 6, 9, 2, 7]:
            bst.insert(x)
            lst.insert(x)             
        self.assertEqual(str(bst.to_LinkedList()), str(lst))

        
    def test_ipl(self):
        bst = BST()
        self.assertEqual(bst.ipl(), 0)
        bst.insert(5)
        self.assertEqual(bst.ipl(), 1)
        bst.insert(8)
        self.assertEqual(bst.ipl(), 3)
        bst.insert(9)
        self.assertEqual(bst.ipl(), 6)
        bst.insert(3)
        self.assertEqual(bst.ipl(), 8)
        bst.insert(1)
        self.assertEqual(bst.ipl(), 11)

        

if __name__ == "__main__":
    unittest.main()