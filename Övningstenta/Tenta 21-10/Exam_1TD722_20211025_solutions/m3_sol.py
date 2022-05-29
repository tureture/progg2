"""
Solutions to exam tasks for module 3.

"""
import random
import time

class ExamException(Exception):            
    def __init__(self, msg):
        self.msg = msg


class LinkedList:
    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ
    
    def __init__(self, param=None):                ### First implementation  A7
        self.first = None
        if param is None:
            return
        try:
            iter(param)
        except TypeError:
            self.first = self.Node(param)  
            return
        
        # Create the list from an iterable
        self.first = self.Node(None) # A dummy node
        temp = self.first
        for x in param:
            temp.succ = self.Node(x)
            temp = temp.succ
        self.first = self.first.succ # Remove thge dummy node
    
    def __init__(self, param=None):            ### Second implementation  A7
        self.first = None
        if param is None:
            return
        try:
            iter(param)
        except TypeError:
            self.first = self.Node(param)
            return
        
        # Create the list from an iterable
        for x in param:
            self.append(x)
    
    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ
    
    def __str__(self):
        if self.first is None:
            return '()'
        res = ''
        for x in self:
            res += str(x) + ', '
        return '(' + res[:-2] + ')'
    
    def __getitem__(self, index):
        ind = 0
        for x in self:
            if ind == index:
                return x
            ind += 1
        raise ExamException(f'Index out of range: {index}')
    
    def __setitem__(self, index, value):               ##### A6
                                                       # We use iterator to count down but we
                                                       # have to keep track of the node pointer
                                                       # "manually" since the iterator just gives
                                                       # the stored values
        current_node = self.first
        for x in self:
            if index==0:         
                current_node.data = value
                return
            current_node = current_node.succ
            index -= 1
        raise ExamException(f'Index out of range: {index}') 
    
    def append(self, x):
        self.first = self._append(self.first, x)
    
    def _append(self, f, x):                               ##### A5
        if f == None:
            return self.Node(x)
        else:
            f.succ = self._append(f.succ, x)
            return f                                       # Do not forget this! A common problem...

    
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

    def __str__(self):
        result = ''
        for x in self:
            result += str(x) + ', '
        if self.root:
            result = result[:-2]
        return '<' + result + '>'
        
    def ipl(self):
        return self._ipl(self.root, 1)

    def _ipl(self, r, level):
        if r is None:
            return 0
        else:
            return level + \
                self._ipl(r.left, level + 1) + \
                self._ipl(r.right, level + 1)
    
    def is_omorph(self, t):                             #### A8
        
        def iso(r1, r2):                                # The help function is written as can of cause
                                                        # of cause be placed outside also
            if r1 is None and r2 is None:
                return True
            elif r1 is None or r2 is None:
                return False
            else:
                return iso(r1.left, r2.left) and iso(r1.right, r2.right)
            
        return iso(self.root, t.root)
            
            
    def merge(self, bst):                               #### B3
        for x in bst:
            self.insert(x)

    def better_merge(self, bst):                        #### B3 Solution. Do a preorder instead
        self._better_merge(bst.root)                    ####    of the inorder traversal

    def _better_merge(self, r):                          
        if r:
            self.insert(r.key)
            self._better_merge(r.left)
            self._better_merge(r.right)
                                                
                                                        

def random_tree(n):
    t = BST()
    for x in range(n):
        t.insert(random.random())
    return t
        

def main():
    print('Using append')
    print('============')
    ll = LinkedList()
    for i in range(5):
        ll.append(i)
    print('After som appends    : ', ll)
    ll.append('x')
    print('After one more append: ', ll)
    
    print('\nUsing index operations:')
    print('=======================')
    ll = LinkedList([2, 5, 8])
    print(ll)
    print(f'll[2]: {ll[2]}')
    try:
        ll[0] = 9
        ll[2] = 11
        print(ll)
        ll[-1] = 17
    except ExamException as e:
        print(e)
        

    print('\nTrying is_omorph')
    print('================')
    t1 = BST([1,2,3])
    t2 = BST([2,1,3])
    t3 = BST([2,3,1])
    t4 = BST([7,8,9])
    
    print(f't1 and t2: {t1.is_omorph(t2)}')
    print(f't1 and t3: {t1.is_omorph(t3)}')
    print(f't2 and t3: {t2.is_omorph(t3)}')
    print(f't1 and t4: {t1.is_omorph(t4)}')
    
    print('\n\nTime measuring for merge')
    print('========================\n')
    
    #exit()                         # Remove this line when working with B3

    print('           Average node height')
    print('     n   t1     t2     t3     t4')
    m = 1000
    for n in (1000, 2000, 4000, 8000, 16000,
              32000, 64000, 128000, 256000):
        t1 = random_tree(m)
        t2 = random_tree(n)
        h1 = t1.ipl()/m
        h2 = t2.ipl()/n
        t1.better_merge(t2)
        h3 = t1.ipl()/(n+m)
        t4 = random_tree(n+m)
        h4 = t4.ipl()/(n+m)
        print(f'{n:6d} {h1:5.1f}, {h2:5.1f}, {h3:5.1f}, {h4:5.1f}')


if __name__ == '__main__':
    main()

"""
Answer to A6:
Using append in the __init__-file will cause each addition of element to start
from the beginning of the list and pass all already added elements.
The method will then have the complexity
c(0 + 1 + 2 + 3 + 4 + ... + n-1) which is Theta(n^2)

The first implementation kept track of the last added value so it does not
have to start from the beginning. The complexity will then be Theta(n)



Answer to B3:
The problem with the given merge is that the node from t2 will come sorted
which will cause a degenerated tree.
Changing to inorder traversal will avoid that problem.

The most common solution to this task was to create a list with the elements
and then use random.shuffle to scramble the list anthe insert them in the tree.
This solution is, of cause, also is ok.


"""