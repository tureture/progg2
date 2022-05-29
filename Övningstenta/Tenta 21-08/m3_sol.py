"""
Solutions to exam tasks for module 3.
Name:
Code:

The file contains:
   1) the class LinkedList with tasks A5, A6 and B2,
   2) the class BST with tasks A7, A8, 
   3) the function bst_sort to be analyzed in task B3
 

The main function runs a small test of the methods. Note that main will not
fully function until all tasks are solved
"""
import random
import time
import math


class ExamException(Exception):
    def __init__(self, arg):
        self.arg = arg


class LinkedList:
    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def add_last(self, x):
        """ Adds x at the end of the list """
        if self.first == None:
            self.first = self.Node(x)
        else:
            f = self.first
            while f.succ:
                f = f.succ
            f.succ = self.Node(x)

    def remove_all(self, x):
        """ Removes all ocurrencies of x in the list """
        self.first = self._remove_all(x, self.first)

    def _remove_all(self, x, f):
        """ Task A5:
            Remove all x from list starting with node f.
            Return the first node in the remaing list.
        """
        if f == None:
            return None
        elif x == f.data:
            return self._remove_all(x, f.succ)
        else:
            f.succ = self._remove_all(x, f.succ)
            return f
    
    def insert(self, data, index=0): # An easy way to otry different insertions
        self.insert_2(data, index) 

    def insert_1(self, data, index=0):
        """ Task B2:
            Inserts a new node at a specified index.
            An iterative solution
        """
        if index < 0:
            raise ExamException(f'Index out of range: {index}')
        if index == 0:
            self.first = self.Node(data, self.first)
        else:
            n = self.first
            ind = index
            while n and ind > 1:
                n = n.succ
                ind -= 1
            if not n:
                raise ExamException(f'Index out range: {index}')
            else:
                n.succ = self.Node(data, n.succ)
        
             
    def insert_2(self, data, index=0):
        """ Task B2:
            Inserts a new node at a specified index
            A recursive solution
        """

        saved_index = index
        
        def insert(data, index, f):
            if f is None and index != 0:
                raise ExamException(f'Index out of range: {saved_index}')
            elif index == 0:
                return self.Node(data, f)
            else:
                f.succ = insert(data, index-1, f.succ)
                return f
        
        self.first = insert(data, index, self.first)        

####################################


class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.data
            if self.right:
                yield from self.right

        def __str__(self):
            return str(self.data)

    def __init__(self, init=None):
        self.root = None
        if init:
            for x in init:
                self.add(x)

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        result = ''
        for x in self:
            result += str(x) + ' '
        return '<' + result + '>'

    def add(self, x):
        """ Adds a new node to the tree"""
        def _add(x, r):
            if r == None:
                return self.Node(x)
            elif x < r.data:
                r.left = _add(x, r.left)
            elif x > r.data:
                r.right = _add(x, r.right)
            return r
        self.root = _add(x, self.root)

    def count_leaves(self):
        """ Returns the number of leaves """
        return self._count_leaves(self.root)

    def _count_leaves(self, r):
        """ A7:
            Count the leaves in the subtree with root r
        """
        if not r:
            return 0
        else:
            if r.left or r.right:
                return self._count_leaves(r.left) + self._count_leaves(r.right)
            else:
                return 1

    def __eq__(self, t):
        """ A8: Overloading =="""
        return str(self) == str(t)


def bst_sort(aList):
    """ Returns a sorted list"""
    bst = BST()
    for x in aList:
        bst.add(x)
    result = []
    for x in bst:
        result.append(x)
    return result


def main():
    print('\nTest run of m3.py')

    print('\nTest of A5 (remove_all)')
    lst = LinkedList()
    for x in (3, 1, 2, 3, 4, 3, 4, 7, 3):
        lst.add_last(x)
    print(lst)

    lst.remove_all(3)
    print(lst, ' \t Should be (1, 2, 4, 4, 7)')

    print('\nTest of B2 (insertion at an index)')
    lst = LinkedList()
    lst.insert(3)          # <3>
    lst.insert(5, 1)       # <3, 5>
    lst.insert(5)          # <5, 3, 5>
    lst.insert(4, 1)       # <5, 4, 3, 5>
    print(lst, ' \t Should be (5, 4, 3, 5)')
    try:
        lst.insert(1, 99)      # LinkedListError: Index out range: 99
    except ExamException as e:
        print(e)

    try:
        empty_list = LinkedList()
        empty_list.insert(1, 1)      # LinkedListError: Index out range: 1
    except ExamException as e:
        print(e)

    print('\nTest of A7: Number of leaves')
    bst = BST([5, 2, 1, 3, 6, 4])
    print('Number of leaves:', bst.count_leaves(), ' \t Should be 3')

    print("\nTest of A8: == for BST")
    print(BST() == BST(), ' \t Should be True')
    print(BST([1, 2, 3]) == BST([1, 2, 3]), ' \t Should be True')
    print(BST([2, 1, 3]) == BST([1, 2, 3]), ' \t Should be True')
    print(BST([0, 1, 3]) == BST([1, 2, 3]), ' \t Should be False')
    print(BST([1, 2, 3]) == BST([1, 2]), ' \t Should be False')

    print('\nDemonstration of bst_sort')
    print(bst_sort([5, 2, 4, 8, 1, 9, 3]))


if __name__ == '__main__':
    main()

"""\n\nAnswer to task A6 - Complexity of repeated add_last:

In a list with m elements, the add_last requires Theta(m) time - we have to start from
the beginning and iterate over the m elements in the list.
Theta(m) means that the time is approximately c*m.

The code starts with an empty list and the list grows for each add_last. The time for
code is then c*(0 + 1 + 2 + ... + n-1) = c*(n-1)*n which is Theta(n^2)




    """

"""\n\nAnswer to task B3 - Complexity of bst_sort:

We can assume that traversing the Python list of length n takes O(n) time. 
The height of a random tree with n keys is, according to the theory, O(log n).
Building a tree a from the beginning empty tree with n nodes is then O(n*log(n))
Traversing a binary tree with the given iterator takes O(n) time.
This sums up to O(n log(n)).



    """
