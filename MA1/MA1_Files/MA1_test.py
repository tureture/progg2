# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(9, 0), 0)

    def test_harmonic(self):
        self.assertAlmostEqual(harmonic(1), 1.)
        self.assertAlmostEqual(harmonic(2), 1.5)
        self.assertAlmostEqual(harmonic(3), 1.5 + 1/3)
        self.assertAlmostEqual(harmonic(4), 1.5 + 1/3 + 1/4)

    def test_largest(self):
        lst = [5, 3, 7, 11, 4]
        self.assertEqual(largest(lst), 11)
        self.assertEqual(lst, [5, 3, 7, 11, 4])
        self.assertEqual(largest(lst[0:1]), 5)
        self.assertEqual(largest(lst[0:2]), 5)
        self.assertEqual(largest(lst[0:3]), 7)
        self.assertEqual(lst, [5, 3, 7, 11, 4])

    def test_count(self):
        l = [1, 'a', 3, 7, 1, [1, 4]]
        self.assertEqual(count('a', l), 1)
        self.assertEqual(count(1, l), 3)
        self.assertEqual(count(4, l), 1)
        self.assertEqual(count([1, 4], l), 1)
        self.assertEqual(count('x', l), 0)
        self.assertEqual(l, [1, 'a', 3, 7, 1, [1, 4]])

    def test_zippa(self):
        l1 = [1, 3, 5, 7, 9]
        l2 = [2, 4, 6]
        l3 = zippa(l1, l2)
        l4 = l3
        self.assertEqual(l3, [1, 2, 3, 4, 5, 6, 7, 9])
        self.assertEqual(l1, [1, 3, 5, 7, 9])
        self.assertEqual(l2, [2, 4, 6])
        l1.append(42)
        l2.append(43)
        l3.append(44)
        self.assertEqual(l1, [1, 3, 5, 7, 9, 42])
        self.assertEqual(l2, [2, 4, 6, 43])
        self.assertEqual(l3, [1, 2, 3, 4, 5, 6, 7, 9, 44])

    def test_bricklek(self):
        res = bricklek('f', 't', 'h', 2)
        self.assertEqual(res, ['f->h', 'f->t', 'h->t'])
        res = bricklek('f', 't', 'h', 3)
        self.assertEqual(res, ['f->t', 'f->h', 't->h',
                               'f->t', 'h->f', 'h->t', 'f->t'])


#  Tests of some of the optional exercises. Add more if you like!

#    def test_power(self):
#        self.assertEqual(power(2,5), 32, "2^5 = 32")
#        self.assertEqual(power(2, 0), 1, "2^0 = 1")
#        self.assertEqual(power(10, -1), 0.1, "10^-1 = 0.1")

#    def test_divide(self):
#        self.assertEqual(divide(2, 5), 0)
#        self.assertEqual(divide(5, 2), 2)
#        self.assertEqual(divide(16, 5), 3)
#        self.assertEqual(divide(0, 1), 0)

if __name__ == "__main__":
    unittest.main()
