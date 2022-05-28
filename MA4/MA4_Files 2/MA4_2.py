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

	nn = 47
	print('N: ', nn)
	start = pc()
	f = Person(nn)
	f.fib()
	end = pc()
	print('fibc: ', end - start)

	start = pc()
	fib_numba(nn)
	end = pc()
	print('fib_numba: ', end - start)

	x = range(30, 46)
	y_py = []
	y_numba = []
	y_c = []

'''
	for n in x:
		print('N: ', n)
		start = pc()
		fib_py(n)
		end = pc()
		y_py.append(end-start)
		print('fib_py: ', end-start)

		start = pc()
		fib_numba(n)
		end = pc()
		y_numba.append(end - start)
		print('fib_numba: ', end-start)

		start = pc()
		f = Person(n)
		f.fib()
		end = pc()
		y_c.append(end - start)
		print('fibc: ', end-start)

	plt.plot(x, y_py, label='Python')
	plt.plot(x, y_numba, label='Numba')
	plt.plot(x, y_c, label='C++')
	plt.savefig('plot_MA42.png')
'''


if __name__ == '__main__':
	main()
