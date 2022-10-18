""" Exam tasks for modul 1 for exam 2022-05-30

Exam code:                  Important to fill in this!!!!


"""

import random
import time
import math

#######       A1: is_sorted

def is_sorted(lst):
    pass





#######      A2: depth
def depth(lst, d=0):
    pass




#######      B1: recursive largest without list copying
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

Complexity for the function above:   ??????
'''

def largest(a):
    pass

'''
Complexity for this function:    ??????
'''


def main():
    print('A1: is_sorted')
    args = ([], [1], [1, 2], [1, 3, 2], [2, 3, 5, 4], ['a', 'ab', 'c'])
    for a in args:
        print(f'{str(a):28} {is_sorted(a)}')

    print('\nA2: depth')
    print(f'Argument                     Depth')
    lists = (1, [], [[]], [1, 2, 3],
             [[1], 2, [[3]]],
             [[1, (1, [2])],[[[[2]]]],3],
             ['[[', [']']])
    for lst in lists:
        print(f'{str(lst):30} {depth(lst)}')

    print('\nB1: largest')
    lists = ([1,2,3,4], [1,2,5,3], [1,6,2,3], [7,1,2,3])
    for lst in lists:
        print(f'In {lst} is {largest(lst)} largest')
 
if __name__ == "__main__":
    main()


    