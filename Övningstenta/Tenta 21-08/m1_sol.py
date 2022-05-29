"""
Solutions to exam tasks for module 1 2021-08-26
Name:
Code:
"""

import random
import time
import math


def count_all(lst, d):
    """ A1: Count all occurencies of d recursively """
    result = 0
    for x in lst:
        if x == d:
            result += 1
        elif type(x) == list:
            result += count_all(x, d)
        else:
            pass
    return result
        
        
        


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
    memory = {0:1, 1:1, 2:1}
    
    def c(n):
        if not n in memory:
            memory[n] = c(n-1) - c(n-3)
        return memory[n]
    
    return c(n)


def main():
    print('Test count_all')
    print(count_all([], 1),
          '\tShould be 0')
    print(count_all([1, 2, 1, 3, [[1], [1, 2, 3]]], 1),
          '\tShould be 4')
    print(count_all([[1, 2], [[1, 2], [[1, 2], 1, 2]]], [1, 2]),
          '\tShould be 3')
    
    
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

    measured = []
    for n in [44,45,46,47,48,49,50]:
        tstart = time.perf_counter()
        print(c(n), end =' \t')
        dt= time.perf_counter()-tstart
        measured.append(dt)
        print(f"{n} \t {dt}")
        
    for i in range(1,len(measured)):
        print(measured[i]/measured[i-1])
    



if __name__ == "__main__":
    main()
    print('Over and out')


"""
Answer to task B1:
My output:
245     44   2.616603916
524     45   3.668804042
595     46   5.346963958000001245    
524     45   3.668804042
595     46   5.346963958000001
350     47   7.842969500000001
-174    48   11.328292458
-769    49   16.479312500000002
-1119   50   24.495762291
1.4021243412371323
1.4574133414564092
1.466807998259561
1.4443881820527287
1.4547040130803095
1.4864553537048342
350     47   7.842969500000001
-174    48   11.328292458
-769    49   16.479312500000002
-1119   50   24.495762291
1.4021243412371323
1.4574133414564092
1.466807998259561
1.4443881820527287
1.4547040130803095
1.4864553537048342

c(100) will take 24*1.45**50 ≈ 90 years


"""
