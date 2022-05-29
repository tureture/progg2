
from numba import njit
from time import perf_counter as pc

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n - 1) + fib_numba(n - 2)


start = pc()
fib_numba(47)
end = pc()
print('fib_numba: ', end - start)

