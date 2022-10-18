""" Exam tasks for modul 3 for exam 2022-05-30

Exam code:                  Important to fill in this!!!!!


"""
import random
import time


class LinkedList:
    class Node:
        def __init__(self, key, succ=None):
            self.key = key
            self.succ = succ
    
    def __init__(self):                
        self.first = None
    
    
    def __iter__(self):
        current = self.first
        while current:
            yield current.key
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
            while node.succ and key > node.succ.key:
                node = node.succ
            node.succ = self.Node(key, node.succ)
    

def build_list(n):       ### A5: Complexity? Write your answer in
                         ###     the designated area in main
    llist = LinkedList()
    for x in range(n):
        llist.insert(x)
    return llist

           
    
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
            pass ### Already there
        return r

    def __str__(self):
        result = ''
        for x in self:
            result += f'{x}, '
        if self.root:
            result = result[:-2]
        return '<' + result + '>'


    def count_nodes_on_level(self, level):
        pass
           
 
class LevelOrderIterator:
    pass
       

def main():
    print('A5: Time complexity for build list >')

    ### Write your code for empirical investigation of the complexity here:
    

    ###
    '''
        Answer to the question about complexity:
        
        
        
        Estimated time for build_list(1000000):
        Use reasonable time units!
    '''
    
    print('\nA6: Counting frequences >')            
    lst = LinkedList()
    for x in (3,1,2,5,4,3,3,4):
        lst.insert(x)
    print(lst)
   

    bst = BST()
    for x in (5, 3, 2, 4, 8, 10, 6, 1, 7, 9):
        bst.insert(x)

    print('\nA7: Count nodes on level >')
    for i in range(5):
        print(f'level {i}:  {bst.count_nodes_on_level(i)}')
    print()
    
    try:
        print('\nA8: The index operator >')   
        for i in range(0, 6, 2):
            print(f'bst[{i}] = {bst[i]}' )
        try:
            bst[10]
        except IndexError as ie:
            print(ie)
    except:
        print('\n\n*** The index operator not fully implemented yet')
    
    try:
        print('\nB3: LevelOrderIterator >') 
        bst = BST()
        print('Insertion order: ', end=' ')
        for x in [5, 3, 2, 4, 8, 10, 6, 1, 7, 9 ]:
            print(x, end =' ')
            bst.insert(x)
        print('\nSymmetric order: ', end=' ')
        for x in bst:
            print(x, end=' ')
        print('\nLevel order    : ', end = ' ')
        loi = LevelOrderIterator(bst)
        for x in loi:
            print(x, end= ' ')
        print()
    except:
        print('\n\n*** The LevelOrderIterator is not fully implmented yet')


if __name__ == '__main__':
    main()


