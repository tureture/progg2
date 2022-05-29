"""
Solutions to exam tasks for modul 1 for exam 2021-10-25
"""

import random
import time
import math

#                             Task A1

def length_longest(lst):
    # Variant 1: Iteratively in the 'width' direction
    if type(lst) != list:
        return 0
    result = len(lst)
    for x in lst:
        result = max(result, length_longest(x))
    return result

def length_longest(lst):
    # Variant 2: Recursively in both directions
    if type(lst) != list or lst==[]:
        return 0
    else:
        return max(len(lst), length_longest(lst[0]), length_longest(lst[1:]))

def bubbelsort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
"""

"""
                
def random_list(n):
    res = []
    for i in range(n):
        res.append(random.random())
    return res


def foo(n):
    result = 1
    for k in range(3):
        for i in range(n*n):
            result += k*n
    return result
    

def main():
    print('Testing length_longest')
    print(length_longest(1), '\t Should be 0')
    l1 = [1,2,[[1,2,3,[1,2,3,4,5,6,7,8],5,6],2,3,4,5,6,7,8]]
    print(length_longest(l1), '\t Should be 8')
    l1 = [1,2,[[1,2,3,[1,2,3,4,5,6,7],5,6],2,3]]
    print(length_longest(l1), '\t Should be 7')

  

    print('\nTiming of bubbelsort')
    measured = []
    for n in [1000, 2000, 4000, 8000]:
        rl = random_list(n)
        # rl = [x for x in range(n)]  # Try this if you want to see that it is Theta(n^2) even in best case
        tstart = time.perf_counter()
        bubbelsort(rl)
        print(n,  end =' \t')
        dt= time.perf_counter()-tstart
        measured.append(dt)
        print(f"{dt:5.1f}")
    print('\nTime growth when doubling input' )  
    for i in range(1,len(measured)):
        print(f'{measured[i]/measured[i-1]:5.1f}')  

    print('\nTiming of foo')
    measured = []
    for n in [1000, 2000, 4000, 8000]:
        tstart = time.perf_counter()
        print(n, end ='\t')
        foo(n)
        dt= time.perf_counter()-tstart
        measured.append(dt)
        print(f" {dt:5.1f}")
    print('\nTime growth when doubling input' )  
    for i in range(1,len(measured)):
        print(f'{measured[i]/measured[i-1]:5.1f}')  

    print('\nEstimation of time for foo(1000000)')
    n = 10000
    tstart = time.perf_counter()
    foo(n)
    dt= time.perf_counter()-tstart
    print(f"Time for {n}: {dt:5.1f}")
 
if __name__ == "__main__":
    main()
    
"""
Solution to A2 (Time complexity for bubbelsort):
Complexity Theta(n^2).
For each of the n rounds in the outer loop the inner loop will also goes n rounds.

It is practically demonstrated in the testrun where n is doubled thus expecting the time
to be multiplied by 4 each step.

Note that you want to see a n^2 behaviour you should at least have three measurements where
you, at lerast, double n. Changing n with a factor 10 is also convenient in which case the
time should increase with a factor 10^2 = 100.

Several students claimed that the code the time was Theta(n) if the list was already sorted
but that is not true. Even if the code doesn't do any swaps, n^2 comparisons will be done.
Bubbelsort CAN be implemented to have a Theta(n) complexity but that was not in the given
implementation. 







Solution to B1 (Time complexity for function foo):

Complexity Theta(n^2)
To compute foo(1000000) can be estimated to time for foo(10000) multiplied
by 100^2 which is 20*10000 seconds 55 hours.






"""
    