""" bst.py

Student: Ture Hassler
Mail: ture.hassler@gmail.com
Reviewed by: Kieran
Date reviewed: May 6th 2022
"""
import random
import math

from linked_list import LinkedList


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):  # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):  # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    #
    #   Methods to be completed
    #

    def height(self):  # Compulsory
        if self.root is None:
            return 0
        else:
            return self._height(self.root)

    def _height(self, r):
        if r.left is None and r.right is None:
            return 1
        elif r.left is None:
            return 1 + self._height(r.right)
        elif r.right is None:
            return 1 + self._height(r.left)
        else:
            return 1 + max(self._height(r.left), self._height(r.right))

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):  # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)  # left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)  # right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:  # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                s = self._smallest(r.right)
                r.key = s.key
                self._remove(r.right, s.key)

                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def _smallest(self, r):  # Går bara åt vänster
        if r.left is not None:
            return self._smallest(r.left)
        else:
            return r

    def __str__(self):  # Compulsory
        s = ""
        for element in self:  # Itererar över objekten
            s = s + str(element) + ', '

        if len(s) != 0:  # Quickfix tar bort extra komma och blanksteg
            s = s[0:-2]

        return '<' + s + '>'

    def to_list(self):  # Compulsory
        lst = []
        for element in self:
            lst.append(element)
        return lst

    def to_LinkedList(self):  # Compulsory
        LL = LinkedList()
        for element in self:
            LL.insert(element)
        return LL

    def ipl(self):  # Compulsory
        if self.root:
            return self._ipl(self.root, 1)
        else:
            return 0

    def _ipl(self, r, h):
        if r.left is None and r.right is None:
            return h
        elif r.left is None:
            return h + self._ipl(r.right, h + 1)
        elif r.right is None:
            return h + self._ipl(r.left, h + 1)
        else:
            return h + self._ipl(r.left, h + 1) + self._ipl(r.right, h + 1)


def random_tree(n):  # Useful
    tree = BST()
    for i in range(n):
        tree.insert(random.random())
    return tree


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()
    '''
    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")
    '''
    # Testkod:
    # print('Testkod:')
    # print(t.height())
    '''
    t.print()
    t.remove(4)
    print()
    t.print()
    print()
    print(str(t))
    '''

    # Test uppgift 20
    k = []
    for i in range(1, 100):
        tree = random_tree(i)
        ipl = tree.ipl()
        height = tree.height()
        expected_ratio = 1.39 * math.log2(i) + O(1)
        r = ipl/i
        koeff = r - expected_ratio
        k.append(koeff)
        print(f'n:{i : >2}, R: {r: >18}, E: {expected_ratio : >18}, Koeff: {koeff :>5} Height: {height : >3}')
    print(sum(k) / len(k))








if __name__ == "__main__":
    main()

"""
What is the generator good for?
==============================
Bra för att enkelt iterera igenom alla element i objektet

1. computing size? Bra! 
2. computing height? Tror inte det?
3. contains? Bra!
4. insert? Nej
5. remove? Nej




Results for ipl of random trees
===============================
n är antalet noder, R är ration mellan ipl och n, E är 1.39 log2(n) utan konstant, Height är höjden.
Verkar stämma bra! Konstanten O(1) verkar vara omkring -1.8 för mig 
Höjden verkar också bero logaritmiskt av n

Urval av  resultat: 
n: 1, R:                1.0, E:                0.0 Height:   1
n: 2, R:                1.5, E:               1.39 Height:   2
n: 3, R:                2.0, E: 2.2030978760024067 Height:   3

n:97, R:  8.525773195876289, E:  8.173878850640108 Height:  16
n:98, R:  8.173469387755102, E:   8.19444668332014 Height:  15
n:99, R:  6.636363636363637, E:  8.214805701910656 Height:  11

n:498, R:  10.08433734939759, E: 12.454402685574632 Height:  18
n:499, R: 10.198396793587174, E:  12.45842544741879 Height:  20







"""
