"""
Solutions to exam tasks for module 3.

Lines added for the solutions ar marked with # Task followed by task number

"""
import random
import time


class LinkedList:
    class Node:
        def __init__(self, key, succ=None):
            self.key = key
            self.succ = succ
            self.count = 1  # Task A5

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.key, current.count  # Task A6
            current = current.succ

    def __str__(self):
        if self.first is None:
            return '<>'
        res = ''
        for x in self:
            res += str(x) + ', '
        return '<' + res[:-2] + '>'

    def insert(self, key):
        if self.first == None or key < self.first.key:
            self.first = self.Node(key, self.first)
        else:
            node = self.first
            while node.key != key and node.succ and key >= node.succ.key:  # Task A6
                node = node.succ

            if node.key == key:  # Task A6
                node.count += 1  # Task A6
            else:  # Task A6
                node.succ = self.Node(key, node.succ)


def build_list(n):
    llist = LinkedList()
    for x in range(n):
        llist.insert(x)
    return llist


""" # Task A5
Since the list is kept sorted each insertion will go into the en of the list 
so the number of tries will be 1 + 2 + 3 + ... + n = n*(n+2)/2 which is Theta(n^2).
Measuring on n n= 2000, 4000, 8000 shows clearly that doubled n takes 4 time as ling time.
t(10000) takes 6 seconds on my computer. To go to from 10^4 to 10^6 multiplies n by 100
an the time will thus increase with a fator of 100^2. The estimated time will then
be 6*10^4 seconds ≈ 17 hours
"""


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, param=None):
        self.root = None
        if param:
            for x in param:
                self.insert(x)

    def __iter__(self):
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(key, self.root)

    def _insert(self, key, r):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(key, r.left)
        elif key > r.key:
            r.right = self._insert(key, r.right)
        else:
            pass  # Already there
        return r

    def __str__(self):
        result = ''
        for x in self:
            result += f'{x}, '
        if self.root:
            result = result[:-2]
        return '<' + result + '>'

    def count_nodes_on_level(self, level):
        return self._count_nodes_on_level(self.root, level)

    def _count_nodes_on_level(self, r, level):  # Task A7
        if r == None:
            return 0
        elif level == 0:
            return 1
        else:
            return self._count_nodes_on_level(r.left, level-1) + \
                self._count_nodes_on_level(r.right, level-1)

    def __getitem__(self, index):  # Task A8
        ind = 0
        for x in self:
            if ind == index:
                return x
            ind += 1
        raise IndexError(f'Tree index out of range: {index}')


class LevelOrderIterator:  # Task B3
    def __init__(self, bt):
        self.queue = [bt.root]

    def __iter__(self):
        return self

    def __next__(self):
        if self.queue != []:
            out = self.queue.pop(0)
            if out.left:
                self.queue.append(out.left)
            if out.right:
                self.queue.append(out.right)
            return out.key
        else:
            raise StopIteration


def main():
    print('A5: Time complexity for build list')
    for n in (2000, 4000, 8000, 10000):
        tstart = time.perf_counter()
        build_list(n)
        tstop = time.perf_counter()
        print(f'{n:6} {tstop-tstart:7.2f}')

    print('\nA6: Counting frequences')
    lst = LinkedList()
    for x in (3, 1, 2, 5, 4, 3, 3, 4, 1, 5):
        print(x, end=' ')
        lst.insert(x)
    print('\n',  lst)

    bst = BST()
    for x in (5, 3, 2, 4, 8, 10, 6, 1, 7, 9):
        bst.insert(x)

    print('\nA7: Count nodes on level')
    for i in range(5):
        print(f'level {i}:  {bst.count_nodes_on_level(i)}')
    print()

    print('\nA8: The index operator')
    for i in range(0, 6, 2):
        print(f'bst[{i}] = {bst[i]}')
    try:
        bst[10]
    except IndexError as ie:
        print(ie)
    try:
        bst[-1]
    except IndexError as ie:
        print(ie)

    print('\nB3: LevelOrderIterator')
    bst = BST()
    print('Insertion order: ', end=' ')
    for x in [5, 3, 2, 4, 8, 10, 6, 1, 7, 9]:
        print(x, end=' ')
        bst.insert(x)
    print('\nSymmetric order: ', end=' ')
    for x in bst:
        print(x, end=' ')
    print('\nLevel order    : ', end=' ')
    loi = LevelOrderIterator(bst)
    for x in loi:
        print(x, end=' ')
    print('\n\nDone')


if __name__ == '__main__':
    main()
