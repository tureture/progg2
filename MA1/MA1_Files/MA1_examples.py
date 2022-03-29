"""
This file contains the code examples in module 1 and
the code from the video lesson with sorting experiments.
"""

import random   
import time     

def fac(n):
    """ Computes and returns n!""" 
    if n==0:
        return 1
    else:
        return n*fac(n-1)


def power(x,n):
    """ Computes and returns x**n recursively"""
    if n == 0:
        return 1
    elif n > 0:
        return x*power(x, n-1)
    else:
        return 1./power(x, -n)



def reverse_mid(x):
    """ Returns s reversed """
    if len(x) <= 1:
        return x
    else:
        mid = len(x)//2
        return reverse_mid(x[mid:]) + reverse_mid(x[:mid])
    


def exchange(a, coins):
    """ Count possible way to exchange a with the coins in coins"""
    if a == 0:
        return 1
    elif (a < 0) or (len(coins) == 0):
        return 0
    else:
        return exchange(a, coins[1:]) + exchange(a - coins[0], coins)


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def fib_memoization(n):
    memory = {0:0, 1:1}

    def _fib(n):
        if n not in memory:
             memory[n] = _fib(n-1) + _fib(n-2)
        return memory[n]

    return _fib(n) 



def insertion_sort(l):
    """ Iterative insertion sort """
    for j in range(1, len(l)):
        x = l[j]
        i = j-1
        while i >= 0 and x < l[i]:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = x
             

#####################################################################
#
#  The sorting methods from the video lesson about sorting experiments
#

#    Recursive insertion sort
    
def ins_sort_rec(lst):
    return _ins_sort_rec(lst, len(lst))

def _ins_sort_rec(lst, n):
    if n > 1:
        _ins_sort_rec(lst, n-1)
        x = lst[n-1]
        i = n - 2
        while i >= 0  and lst[i] > x:
            lst[i+1] = lst[i]
            i -= 1
        lst[i+1] = x
    return lst


########################### Iterative insertion sort
def ins_sort_iter(lst):
    for i in range(1, len(lst)):
        j = i-1
        while j >= 0 and lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            j -= 1
    return lst


############################ Merge sort
def merge_sort(lst):
    if len(lst) <= 1: return lst
    else:
        n = len(lst)//2
        l1 = lst[:n]
        l2 = lst[n:]
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
        return merge_iter(l1, l2)      # or merge(l1,l2)
    

def merge(l1, l2):
    """ Merges two lists recursively """
    if len(l1) == 0:return l2.copy()
    elif len(l2) == 0: return l1.copy()
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])
    
        
def merge_iter(l1, l2):
    """ Merges two lists iteratively """
    result = []
    i1 = 0
    i2 = 0
    while i1 < len(l1) and i2 <len(l2):
        if l1[i1] <= l2[i2]:
            result.append(l1[i1])
            i1 += 1
        else:
            result.append(l2[i2])
            i2 += 1
    result.extend(l1[i1:])
    result.extend(l2[i2:])
    return result
        

############################ Partition sort

def psort(lst):
    _psort(lst, 0, len(lst)-1)
    return lst
    
def _psort(lst, n, m):
    if m > n:
        ip = partition(lst, n, m)
        _psort(lst, n, ip-1)
        _psort(lst, ip+1, m)
        
def partition(lst, n, m):
    if m>n:
        p = lst[n]
        i = n
        j = m
        while j > i:
            while j>i and lst[j] > p:
                j -= 1
            lst[i] = lst[j]
            while i < j and lst[i] < p:
                i += 1
            lst[j] = lst[i]
            j -= 1
        lst[i] = p
        return i  


##################    
        
def compare_sorting_methods():
    sort_functions = [ins_sort_iter, merge_sort, psort, sorted]   # Note!

    for sort in sort_functions[1:]:               # Do not try insertion sort here
        print(f'\n ***{sort.__name__}***')
        for n in [100000, 200000, 400000, 800000]:
            lst = []
            for i in range(n):
                lst.append(random.random())
            tstart = time.perf_counter()
            lst = sort(lst)
            tstop = time.perf_counter()
            print(f" Time for {n}\t : {tstop - tstart:4.2f}")



def main():
    
    print(f"fac(100) = {fac(100)}\n")
    
    print(f"power(2, 5) = {power(2, 5)}")
    print(f"power(2,-1) = {power(2,-1)}\n")

    coins = (1, 5, 10, 50, 100)
    for a in [1, 4, 5, 9, 10, 100]:
        print(f"exchange({a}, {coins}) : {exchange(a, coins)}")
    print()

    for i in [0, 1, 2, 5, 10]:
        print(f"fib({i}) : {fib(i)}")
    print()
    
    for i in [0, 1, 2, 5, 10, 200]:
        print(f"fib_memoization({i}) : {fib_memoization(i)}")
    print()
   
   
    # Demonstrates how the time complexity can be verified by experiments
    print('\nSorting with non recursive insertion sort')
    for test_size in [1000, 2000, 4000, 8000]:   
        l =[random.random() for i in range(test_size)]
        tstart = time.perf_counter()
        insertion_sort(l)
        tstop = time.perf_counter()
        print(f"Time for sorting {test_size} values: {tstop-tstart:.2f} seconds")
        
    print('\n\nThe video lesson with sorting experiments')
    print('=========================================')
    compare_sorting_methods()
    print('Bye!')
        
if __name__ == "__main__":
    main()




