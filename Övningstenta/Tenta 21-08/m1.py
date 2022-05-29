"""
Solutions to exam tasks for modul 1
Name:
Code:
"""

import random
import time
import math


def count_all(lst, d):
    """ A1: Count all occurencies of d recursively """
    if len(lst) == 0:
        return 0
    elif lst[0] == d:
        return 1 + count_all(lst[1:], d)
    elif type(lst[0]) == list:
        return count_all(lst[0], d) + count_all(lst[1:], d)
    else:
        return count_all(lst[1:], d)


def c(n):
    if n <= 2:
        return 1
    else:
        return c(n-1) - c(n-3)


def c_mem(n):
    """ A2:
        Compute c(n) recursively as above but use
        memorization to keep the runtime down.
    """
    mem = {0:1, 1:1, 2:1}
    def _c_mem(n):
        if n not in mem:
            mem[n] = _c_mem(n-1) + _c_mem(n-3)
        return mem[n]
    return _c_mem(n)


def main():
    print('Test count_all')
    print(count_all([], 1))
    print(count_all([1, 2, 1, 3, [[1], [1, 2, 3]]], 1))
    print(count_all([1, 2, 3, 4], 4))

    print('\nTest of c')
    print('c(3):', c(3))
    print('c(4):', c(4))
    print('c(5):', c(5))
    print('c(9):', c(9))

    print('\nTest of c_mem')
    print('c_mem(3):', c_mem(3))
    print('c_mem(4):', c_mem(4))
    print('c_mem(5):', c_mem(5))
    print('c_mem(9):', c_mem(9))

    print('c_mem(100):', c_mem(100))

    print('\nCode for task B1')
    # Skalar exponentiellt, programmet körs 2^(n-2)? gånger. t = C * 2^n
    # C beror på dator osv. Kan uppskattas
    t = []
    C = []
    for n in range(10, 30):
        start = time.perf_counter()
        c(n)
        end = time.perf_counter()
        C.append( (end-start) / (2**(n-3)))
        print(end-start)
    print(C)
    print(sum(C) / len(C))






if __name__ == "__main__":
    main()
    print('Over and out')


"""
Answer to task B1:




"""
