"""
Solutions to exam tasks for modul 1 for exam 2022-05-30
"""

import random
import time
import math

#######       A1: is_sorted


def is_sorted(lst):
    if len(lst) <= 1:
        return True
    elif lst[0] > lst[1]:
        return False
    else:
        return is_sorted(lst[1:])


#######      A2: depth
def depth(lst, d=0):
    if type(lst) != list:
        return d
    else:
        result = d+1
        for e in lst:
            result = max(result, depth(e, d+1))
        return result


# B1: recursive largest without list copying
# This is a common way to recusively find the largest element in a list
# However, the a list-slicing copies the list so each this call will make
# a new list with n-1 elements.
'''
def largest(lst):
    if len(lst)==1:
        return lst[0]
    elif lst[0] > lst[-1]:
        return largest(lst[:-1])
    else:
        return largest(lst[1:])
'''

# A) What will the complexity of this function be?. Answer Theta(n^2)
# B) Solve this problem recursively without making the copies of the list which
#    giving much less complexity. Which?
# Answer: Theta(n).
#
# Code:


def largest(a):
    def _largest(a, n):
        if n == 1:
            return a[0]
        else:
            mx = _largest(a, n-1)
            return mx if mx > a[n-1] else a[n-1]
    return _largest(a, len(a))
    pass


"""
Complexity or this function:
    
        Complexity for the original function:
    
    """


def main():
    print('A1: is_sorted')
    args = ([], [1], [1, 2], [1, 3, 2], [2, 3, 5, 4], ['a', 'ab', 'c'])
    for a in args:
        print(f'{str(a):28} {is_sorted(a)}')

    print('\nA2: depth')
    print(f'Argument                     Depth')
    lists = (1, [], [[]], [1, 2, 3],
             [[1], 2, [[3]]],
             [[1, (1, [2])], [[[[2]]]], 3],
             ['[[', [']']])
    for lst in lists:
        print(f'{str(lst):30} {depth(lst)}')

    print('\nB1: largest')
    lists = ([1, 2, 3, 4], [1, 2, 5, 3], [1, 6, 2, 3], [7, 1, 2, 3])
    for lst in lists:
        print(f'In {lst} is {largest(lst)} largest')


if __name__ == "__main__":
    main()
