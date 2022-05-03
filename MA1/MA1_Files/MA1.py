"""
Solutions to module 1
Student: Ture Hassler
Mail: ture.hassler@gmail.com
Reviewed by: Alicia Robertsson
Reviewed date: 30 Mars 2022
"""

import random
import time
from MA1_examples import fib


def power(x, n):  # Optional
    pass


def multiply(m, n):  # Compulsory
    """ Tar in två heltal m, n och returnerar m*n. Beräknat med rekursiv addition"""
    if n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


def divide(t, n):  # Optional
    pass


def harmonic(n):  # Compulsory
    """ Tar ett heltal n som input. Returnerar summan av de n första termerna i harmoniska serien """
    if n == 1:
        return n
    else:
        return 1 / n + harmonic(n - 1)


def digit_sum(x):  # Optional
    pass


def get_binary(x):  # Optional
    pass


def reverse(s):  # Optional
    pass

# Hittar största elementet i en lista rekursivt
def largest(a):  # Compulsory
    """
    Tar en lista a med jämförbara element (t.ex char, double), returnerar det största värdet i listan.
    Beräknat rekursivt
    """
    if len(a) <= 1:
        return a[0]
    else:
        b = largest(a[1:])
    if a[0] > b:
        return a[0]
    else:
        return b

# Räknar antalet förekomster av x, hanterar nestlade listor ifall x ej är en lista
# Basfall då längden av s=1. Extra if else hanterar fallet då x är en lista
def count(x, s):  # Compulsory
    """
    Tar en lista s och ett objekt x som input. Returnerar antalet förekomster av x i listan s.
    Inklusive förekomster i nestlade listor.
    """
    if len(s) == 0:
        return 0
    elif x == s[0]:
        return 1 + count(x, s[1:])
    elif type(s[0]) == list:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return count(x, s[1:])


# Slår ihop två listor rekursivt
def zippa(l1, l2):  # Compulsory
    """ Tar två listor l1, l2 som input. Returnerar en kombinerad lista med ordningen vartannat element """
    if len(l1) <= 1:
        return l1 + l2
    elif len(l2) <= 1:
        return [l1[0], l2[0]] + l1[1:]
    else:
        return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])

# Löser Towers of Hanoi rekursivt
def bricklek(f, t, h, n):  # Compulsory
    """ Löser Towers of Hanoi rekursivt. Flyttar tornet från plats f till t.
    Input tar namnet på de tre platserna, f, t, h och antalet brickor i tornet n.
    Returnerar en lista med instruktioner över de flyttar som krävs """
    if n == 0:
        return []
    else:
        return bricklek(f, h, t, n - 1) + [f + '->' + t] + bricklek(h, t, f, n-1)


def main():
    """ Demonstates my implementations """
    #print(multiply(5, 5))
    #print(harmonic(3))
    #print(largest([1, 3, 4, 6, 2, 4, 2, 3]))
    #print(count(4, [1, [4, 4], 3, 1, 4, 2, ['a', [[4, 4], 4, 4]]]))
    #print('')
    #print(zippa([1, 3, 5], [2, 4, 6, 8, 10]))
    print(bricklek('V', 'H', 'M', 7))
    # print('Bye!')

    # tstart = time.perf_counter()
    # fib(31)
    # tstop = time.perf_counter()
    # print(f"Measured time: {tstop - tstart} seconds")


if __name__ == "__main__":
    main()

####################################################    

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  Brickleken skalar exponentiellt som 2^n -1 
  Så för fallet med 50 brickor och 1s per förflyttning får vi 
  2^50 steg == ca 10^15s = ca 30 miljoner år?
  
  
  Exercise 17: Time for Fibonacci:
  A.
  Om den skalar som 1.618^n bör 5 till punkter leda till ca en faktor 11 hos tiden
  fib(32) = 1.3s
  fib(37) = 14.13s 
  fib(42) = 157s 
  Vilket ger en faktor 10.8 och 11.1, vilket om vi tar 5:e roten ur ger oss tillväxt 
  med ca 1.61832. Stämmer bra!
  Går även att beräkna konstanten c för t(n) = c * 1.618^n för min dator men bör ge samma resultat!
  
  B. 
  Jag utgår från att fib(31) = 0.93 == ca 1s
  Vilket ger tiden för fib(50) = fib(31) * 1.618^(50-31) = ca 9300s = 2.5h
  Tiden för fib(100) = fib(31) * 1.618^(100-31) = 2.5*10^14s = ca 8 miljoner år
  

  Exercise 20: Comparison sorting methods:
  Instickssortering skalar som n^2
  Mergesort skalar som n*log(n)
  En ökning från storleken n=10^3 till 10^6 eller 10^9 är en faktor 10^3 och 10^6 större
  Om det tar 1s för 10^3 får vi därmed tiden (10^3)^2 och 10^12 för instickssortering
  Vilket är ca 11 dagar eller 31 tusen år.
  För merge sort får vi en en ökning med 10^3 * log2(10^3) och 10^6*log2(10^6)
  Vilket ger ca 2h och ca 160 dagar
  

  Exercise 21: Comparison Theta(n) and Theta(n log n)
  För c * n*log(n) tar 1s för n=10 så får vi konstanten c = 0.043
  Sätter vi tiderna lika får vi att c*n*log(n) = n --> log(n) = 1/c
  --> n = e^1/c = e^23 --> n = ca 9.7 * 10^9
  A är snabbare för n > 10^10
  

"""
