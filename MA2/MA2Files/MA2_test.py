"""
This is a unit test för the calculator assignment.
In order to use the test BEFORE all requirements are implemented
you can comment out lines for unimplemneted features.
Remember to uncomment them before the final presentation!

"""


import unittest

from MA2 import *

class Test(unittest.TestCase):
    
    def test_statement(self):
        print('\nTest basic arithemtic')
        variables = {"ans": 0.0, "E": math.e, "PI": math.pi}

        tests = {'1+2':3, '2-1':1, '2+1-2':1, '2-2+1':1,'2*3':6, '4/2':2,
                 '8*2/2':8, '8/2*2':8, '(2+1)*2':6, '2*(2+1)':6, '(2+1)*(2+2)': 12,
                 '6/(2*3)': 1, '-(-2-3)':5, '1+2-2=x':1, '2*x+4':6, '2=x=y':2,
                 'x*y':4,'(1=x)+(2=y)=z':3}

        for line, answer in tests.items():
            print(f'{line:30s} expects {answer}', end='\t\t')
            wtok = TokenizeWrapper(line)
            result = statement(wtok, variables)
            print(f'got {result}')
            self.assertEqual(result, answer)
     

    def test_functions(self):
        print('\nTest functions')
        variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
        tests = {'sin(PI)+1': 1,
                 'sin(PI/2)+4': 5,
                 'cos(PI)': -1,
                 'log(E)': 1,
                 'exp(7-2*3=x)': math.e,
                 'exp(log(3))': 3,
                 '(sin(2)=x)*x + (cos(2)=y)*y': 1,
                 'fib(4)' : 3,
                 'fib(10)' : 55,
                 'fib(60)' : 1548008755920,
                 'fac(3)'  : 6,
                 'fac(20)' : 2432902008176640000,
                 'sum(1)' : 1,
                 'sum(1,2,3)' : 6,
                 'min(2,1,3)' : 1,
                 'min(3,2,1)' : 1,
                 'max(sin(PI/2), 2+3, log(1)+1)' :5,
                 'max(sin(PI/2), 5, log(2-1)+7)' : 7
                 }
        for line, answer in tests.items():
            print(f'{line:30s} expects {answer}', end='\t\t')
            wtok = TokenizeWrapper(line)
            result = statement(wtok, variables)
            print(f'got {result}')
            self.assertAlmostEqual(result, answer)
        

    def test_exceptions(self):
        print('\nTest exceptions')
        variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
        
        tests = ['1+*2', 'sin 2', '((1)++)', '1=2', '+1', 'mean(1,2 3)', '1=x+2']
        
        for line in tests:
            print(f'{line:30s} expects SyntaxError', end = ' \t \t ')
            wtok = TokenizeWrapper(line)
            with self.assertRaises(SyntaxError):
                result = statement(wtok, variables)
            print('Got it')        
        
        line = '((1)'
        print(f'{line:30s} expects TokenError', end = ' \t \t ')
        wtok = TokenizeWrapper(line)
        with self.assertRaises(TokenError):
            result = statement(wtok, variables)
        print('Got it')

        tests = ['xxx', 'a+b', '1/(2*3-6)', 'log(-1)', 'fib(-1)', 'fac(1.5)', '1/sin(1-1)']
        for line in tests:
            print(f'{line:30s} expects EvaluationError', end=' \t \t ')
            wtok = TokenizeWrapper(line)
            with self.assertRaises(EvaluationError):
                result = statement(wtok, variables)
            print('Got it')
        
        
if __name__ == "__main__":
    unittest.main()
    