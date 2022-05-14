# https://docs.python.org/3/library/unittest.html
"""
Unittests for the linked lists methods 

"""

import unittest

from linked_list import *

class Test(unittest.TestCase):


    def test_length(self):
        lst = LinkedList()
        self.assertEqual(lst.length(), 0)
        lst.insert(3)
        self.assertEqual(lst.length(), 1)
        lst.insert(2)
        self.assertEqual(lst.length(), 2)
    
    def test_mean(self):
        lst = LinkedList()
        for x in [3, 1, 2, 6]:
            lst.insert(x)
        self.assertEqual(lst.mean(), 3)
        
    def test_remove_last(self):
        lst = LinkedList()
        for x in [3, 1, 2, 6]:
            lst.insert(x)
    
        self.assertEqual(lst.remove_last(), 6)
        self.assertEqual(lst.remove_last(), 3)
        self.assertEqual(lst.remove_last(), 2)
        self.assertEqual(lst.remove_last(), 1)
        #self.assertEqual(lst.length(), 0)

        
    def test_remove(self):
        lst = LinkedList()
        for x in [3, 1, 2, 6, 1]:
            lst.insert(x)
        
        self.assertEqual(lst.remove(0), False)
        self.assertEqual(lst.remove(1), True)
        self.assertEqual(lst.remove(1), True)
        self.assertEqual(lst.remove(3), True)
        self.assertEqual(lst.remove(3), False)
        self.assertEqual(lst.remove(2), True)
        self.assertEqual(lst.remove(2), False)
        

    def test_count(self):
        lst = LinkedList()
        for x in [1, 1, 2, 6, 6]:
            lst.insert(x)
        self.assertEqual(lst.count(1), 2)
        self.assertEqual(lst.count(2), 1)
        self.assertEqual(lst.count(3), 0)
        self.assertEqual(lst.count(6), 2)
        self.assertEqual(lst.count(7), 0)

    def test_to_list(self):
        lst = LinkedList()
        self.assertEqual(lst.to_list(), [])
        lst.insert(1)
        self.assertEqual(lst.to_list(), [1])
        for x in [1, 2, 6]:
            lst.insert(x)
        self.assertEqual(lst.to_list(), [1, 1, 2, 6])
        
    def test_remove_all(self):
        lst = LinkedList()
        for x in [1, 1, 2, 6, 6, 8, 9, 9]:
            lst.insert(x)
        lst.remove_all(5)
        self.assertEqual(lst.to_list(), [1, 1, 2, 6, 6, 8, 9, 9])
        lst.remove_all(9)
        self.assertEqual(lst.to_list(), [1, 1, 2, 6, 6, 8])
        lst.remove_all(1)
        self.assertEqual(lst.to_list(), [2, 6, 6, 8])
        lst.remove_all(2)
        self.assertEqual(lst.to_list(), [6, 6, 8])
        lst.remove_all(8)
        self.assertEqual(lst.to_list(), [6, 6])
        lst.remove_all(6)
        self.assertEqual(lst.to_list(), [])

            
    def test___str__(self):
        lst = LinkedList()
        self.assertEqual(str(lst), '()')
        lst.insert(1)
        self.assertEqual(str(lst), '(1)')
        lst.insert(2)
        self.assertEqual(str(lst), '(1, 2)')
        
    def test_merge(self):
        lst1 = LinkedList()
        lst2 = LinkedList()
        for x in [1, 1, 3, 7, 9]:
            lst1.insert(x)
            lst2.insert(x+1)
        lst1.merge(lst2)
        self.assertEqual(lst1.to_list(), [1, 1, 2, 2, 3, 4, 7, 8, 9, 10])
    
    def test___getitem__(self):
        lst = LinkedList()
        for x in [1, 2, 6]:
            lst.insert(x)
        self.assertEqual(lst[0], 1)
        self.assertEqual(lst[1], 2)
        self.assertEqual(lst[2], 6)
        

if __name__ == "__main__":
    unittest.main()