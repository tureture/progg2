""" MA4_1.py

Student: Ture Hassler
Mail: ture.hassler@gmail.com
Reviewed by:
Date reviewed:
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import math
from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp
import concurrent.futures as future


def monte_carlo_pi(n):
    n_c = []
    n_k = []
    for i in range(n):
        point = (random.uniform(-1, 1), random.uniform(-1, 1))
        if sum([x ** 2 for x in point]) <= 1:
            n_c.append(point)
        else:
            n_k.append(point)

    pi = 4 * len(n_c) / n
    print('Nr points inside: ', len(n_c))
    print('Approx pi: ', pi)
    print('Exact pi: ', math.pi)

    x1, y1 = zip(*n_c)
    x2, y2 = zip(*n_k)
    plt.scatter(x2, y2, color='b')
    plt.scatter(x1, y1, color='r')
    plt.savefig('approx_pi_' + str(n) + '.png')
    return


def monte_carlo_n_sphere(n, d):
    # Använder map, lambda och listbyggare
    # Listbyggare skapar n stycken d-dimensionella punkter
    # Map itererar igenom listan med punkter och anropar lambdafunktion
    # Lambdafunktionen kollar om punkten är innanför enhetscirkeln
    n_inside = sum(list(map(lambda point: True if sum([x ** 2 for x in point]) <= 1 else False,
                            [[random.uniform(-1, 1) for dim in range(d)] for nr in range(n)])))
    volume = 2 ** d * n_inside / n
    exact = (math.pi ** (d / 2)) / math.gamma(d / 2 + 1)

    print('Exact: ', exact)
    print('Approx volume: ', volume)
    return n_inside


# Uppgift MA4 1.1
'''
N = 1000, Approx pi:  3.108
N = 10000, Approx pi:  3.1664
N = 100000, Approx pi:  3.1482
'''
# monte_carlo_pi(1000)

# Uppgift MA4 1.2
# monte_carlo_n_sphere(100000, 11)
'''
(100000, 2)
Exact:  3.141592653589793
Approx volume:  3.1466

(100000, 11)
Exact:  1.8841038793898994
Approx volume:  1.90464
'''


# Uppgift MA4 1.3
def paralell_n_sphere(n, d, nr_cores):
    with future.ProcessPoolExecutor(
            mp_context=mp.get_context('fork')) as ex:  # Problem med macOS? Behövde lägga till fork
        # Preprocessing
        nr_cores = 10
        d = 11
        nd_split = [(n // nr_cores, d) for _ in range(nr_cores)]
        results = ex.map(_parallell_n_sphere, nd_split)

        volume = 2 ** d * sum(results) / n
        exact = (math.pi ** (d / 2)) / math.gamma(d / 2 + 1)
        print('Multiprocessing')
        print('Approx vol: ', volume)
        print('Exact vol: ', exact)


def _parallell_n_sphere(inp):
    # Ger antalet punkter inuti
    n, d = inp
    return sum(list(map(lambda point: True if sum([x ** 2 for x in point]) <= 1 else False,
                        [[random.uniform(-1, 1) for dim in range(d)] for nr in range(n)])))


start = pc()
monte_carlo_n_sphere(10000, 11)
end = pc()
print(f"Process took {round(end - start, 2)} seconds")

start = pc()
paralell_n_sphere(10000, 11, 10)
end = pc()
print(f"Process took {round(end - start, 2)} seconds")

'''
(n, d) = (10000000, 11)
Normal
Exact:  1.8841038793898994
Approx volume:  1.8548736
Process took 185.2 seconds
Multiprocessing
Approx vol:  1.8765824
Exact vol:  1.8841038793898994
Process took 52.81 seconds
'''