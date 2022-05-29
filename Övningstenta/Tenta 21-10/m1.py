"""
m1.py
"""

import random
import time
import math

def length_longest(lst):
    """Returns the length of the longest (sub-)list in lst"""
    if not type(lst) == list:
        return 0
    else:
        m = len(lst)
        for l in lst:
            if type(l) == list:
                m = max(m, length_longest(l))
        return m



def bubbelsort(aList):
    for i in range(len(aList)-1):
        for j in range(len(aList)-1):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
                

def foo(n):
    result = 1
    for k in range(3):
        for i in range(n*n):
            result += k*n
    return result
    

def main():
    print(length_longest(1))                   # Should be 0
    print(length_longest([]))                  # Should be 0
    print(length_longest([1,2,3]))             # Should be 3
    print(length_longest([1,[2,3]]))           # Should be 2
    print(length_longest([1,[1,2,3,4],3]))     # Should be 4 

    aList=[3,2,5,1,7]
    bubbelsort(aList)
    print(aList)

    l = [random.random() for i in range(10)]
    start = time.perf_counter()
    bubbelsort(l)
    end = time.perf_counter()
    print(f'Len: {len(l)}, Time: {end-start}')

    start = time.perf_counter()
    bubbelsort(l)
    end = time.perf_counter()

    C = []
    for n in range(200, 700):
        if n % 10 == 0:
            start = time.perf_counter()
            foo(n)
            end = time.perf_counter()
            C.append((end-start)/(n*n))
    avg_C = sum(C)/len(C)
    print(avg_C)
    print('Estimated time foo(1000000) : ', avg_C * (1000000**2) / 3600, ' h')











if __name__ == "__main__":
    main()
    
"""
Solution to A2 (Time complexity for bubbelsort):
Att gå igenom alla element i en lista med längd n tar det t = C * n
För varje lista måste vi gå igenom en lista igen fast av längd n-1, vilket ger t = C * n * (n-1)
Att stoppa in värden i en python lista vid index n borde gå snabbt, Theta(1)
Alltså blir tidskomplexiteten Theta(n^2)









Solution to B1 (Time complexity for function foo):
Yttre for loopen beror ej på n, kör alltid 3 varv 
Inre for kommer köra n*n gånger
Vilket ger Theta(3*n*n) = Theta(n^2)
Vi kan uppskatta konstanten C
t = C * n^2
C = 3.9175912870344527e-07 
Vilket ger foo(1000000) 








"""
    