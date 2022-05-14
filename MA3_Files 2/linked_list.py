""" linked_list.py

Student: Ture Hassler
Mail: ture.hassler@gmail.com
Reviewed by: Kieran
Date reviewed: May 6th 2022
"""


class LinkedList:
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):  # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):  # Discussed in the section on operator overloading
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

    def length(self):  # Optional
        pass

    def mean(self):  # Optional
        pass

    def remove_last(self):  # Optional
        pass

    def remove(self, x):  # Compulsory
        if self.first is None or x < self.first.data:  # Finns ej i listan, gör ingenting
            return False
        elif self.first.data == x:
            if self.first.succ is None:
                self.first = None
            else:
                self.first = self.first.succ
            return True
        else:
            f = self.first

            while f.succ and x >= f.succ.data:
                if f.succ.data == x:
                    if f.succ.succ is not None:
                        f.succ = f.succ.succ
                    else:
                        f.succ = None
                    return True
                f = f.succ
        return False

    def count(self, x):  # Optional
        pass

    def to_list(self):  # Compulsory
        if self.first is None:  # Tom lista
            return []
        else:
            return self._to_list(self.first)

    def _to_list(self, node):  # Hjälpfunk till to_list
        if node.succ:
            return [node.data] + self._to_list(node.succ)
        else:
            return [node.data]

    def remove_all(self, x):  # Compulsory
        if self.first is None or x < self.first.data:  # Tom lista eller finns ej, gör ingenting
            return
        else:
            self._remove_all(x, self.first)
            return

    def _remove_all(self, x, node):
        if node.succ is None or x < node.data:
            self.remove(x)
            return
        else:
            self.remove(x)
            self._remove_all(x, node.succ)
            return

    def __str__(self):  # Compulsary
        s = "("
        f = self.first
        while f:
            s = s + str(f.data)
            f = f.succ
            if f:
                s = s + ', '
        s = s + ')'
        return s

    def merge(self, lst):  # Compulsory
        # Komplexitet n^2? Insert har n och vi upprepar det n gånger
        for element in lst:
            self.insert(element)
        return

    def __getitem__(self, ind):  # Compulsory
        i = 0
        for element in self:
            if i == ind:
                return element
            else:
                i = i + 1
        raise IndexError('Index out of bounds')


class Person:  # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self, other):  # self < other, använder pnr
        if self.pnr < other.pnr:
            return True
        else:
            return False

    def __le__(self, other):
        if self.pnr <= other.pnr:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.pnr == other.pnr and self.name == other.name:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.pnr > other.pnr:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.pnr >= other.pnr:
            return True
        else:
            return False

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True





def main():
    print('Listorna:')
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 9, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    lst2 = LinkedList()
    for x in [2, 3]:
        lst2.insert(x)
    lst2.print()

    lst3 = LinkedList()

    print('Testkod:')

    # Test code:

    # Testar remove
    '''
    print(lst.remove(1)) # Test första element
    print(lst.remove(2)) # Test mitten
    print(lst.remove(9)) # Test slutet
    lst.print()
    print(lst2.remove(2)) # Test enda elementet
    lst2.print()
    print(lst2.remove(2)) # Test tom lista
    lst2.print()
    '''

    # Testar to_list
    '''
    print(lst.to_list())
    print(lst2.to_list())
    print(lst3.to_list())
    '''

    # Testar remove_all
    '''
    lst2.print()
    lst2.remove(2)
    lst2.print()
    lst.print()
    lst.remove_all(2)
    lst.print()
    lst.remove_all(1)
    lst.print()
    lst.remove_all(9)
    lst.print()
    lst2.print()
    lst2.remove_all(2)
    lst2.print()
    '''
    # Test str
    # print(str(lst))

    # Test merge
    '''
    print(lst)
    print(lst2)
    lst.merge(lst2)
    print(lst)
    '''
    '''
    # Test index (getitem)
    print(lst[3])
'''
    # test Person
    lst7 = LinkedList()

    for x in [1, 3, 1, 2]:
        lst7.insert(Person('Ture', x))
    lst7.print()



if __name__ == '__main__':
    main()
