#!/usr/bin/env python3.9

from person import Person
from numba import njit
import matplotlib.pyplot as plt
from time import perf_counter as pc

def main():

	def fib_py(n):
		if n <= 1:
			return n
		else:
			return fib_py(n - 1) + fib_py(n - 2)

	@njit
	def fib_numba(n):
		if n <= 1:
			return n
		else:
			return fib_numba(n - 1) + fib_numba(n - 2)


	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.fibc(5))

	n = 10
	start = pc()
	fib_py(n)
	end = pc()
	print(f"Process took {round(end - start, 2)} seconds")

	start = pc()
	fib_numba(n)
	end = pc()
	print(f"Process took {round(end - start, 2)} seconds")


if __name__ == '__main__':
	main()
