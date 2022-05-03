""" linked_list.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""

class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ      
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self):             # Optional
        pass
  
  
    def mean(self):               # Optional
        pass
    
    
    def remove_last(self):        # Optional
        pass
    
    
    def remove(self, x):          # Compulsory
        pass        
    
    
    def count(self, x):           # Optional
        pass
    
    
    def to_list(self):            # Compulsory
        pass
    
    
    def remove_all(self, x):      # Compulsory
        pass
    
    
    def __str__(self):            # Compulsary
        pass
    
    
    def merge(self, lst):         # Compulsory
        pass
    
    
    def __getitem__(self, ind):   # Compulsory
        pass


class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"
    

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    
    # Test code:

    


if __name__ == '__main__':
    main()
    


    

