"""
Solutions to exam tasks for module 3.
Name:
Code:

The file contains:
   1) the class LinkedList with tasks A5, A6 and B2,
   2) the class BST with tasks A7, A8, 
   3) the function bst_sort to be analyzed in task B3
 

The main function runs a small test of the methods. Note that main will not
fully function until all tasks are solved.
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
        if f is None:
            return None
        elif f.data == x:
            return self._remove_all(x, f.succ)
        else:
            f.succ = self._remove_all(x, f.succ)
            return f

        """ Task A5:
            Remove all x from list starting with node f.
            Return the first node in the remaing list.
        """
        pass

    def insert(self, data, index=0):
        """ B2: Inserts a new node at a specified index """
        f = self.first
        if self.first is None and index == 0:
            self.first = self.Node(data, None)
        elif index == 0:
            self.first = self.Node(data, self.first)
        else:
            for i in range(index-1):
                if f is None:
                    raise ExamException(f'Index out of range: {index}')
                else:
                    f = f.succ

            if f is not None:
                f.succ = self.Node(data, f.succ)
        print(self)














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

    def __eq__(self, other):
        if bst_sort(self) == bst_sort(other):
            return True
        else:
            return False

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
        if r is None:
            return 0
        elif r.right is None and r.left is None:
            return 1
        else:
            return self._count_leaves(r.right) + self._count_leaves(r.left)
        """ A7:
            Count the leaves in the subtree with root r
        """
        pass


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
Om listan har längden k måste den gå igenom hela listan för att lägga till något sist,
 k + (k+1) + k(+2) +...+ (k+n) = approx (k*n)
 Theta(k*n) tidsomplexitet
 Om tom lista så blir k=n vilket ger Theta(n^2) 


    """

"""\n\nAnswer to task B3 - Complexity of bst_sort:
Average instick skalar som log2 n, men måste upprepas n gånger Theta(nlogn). 
Worst case skalar som n^2 om listan redan är sorterad men högst osannolikt om slumptal



    """
