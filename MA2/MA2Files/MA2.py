"""
Solutions to module 2 - A calculator
Student: Ture Hassler
Mail: ture.hassler@gmail.com
Reviewed by: Lina Sundqvist
Reviewed date: 25/4 2022
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if not wtok.is_at_end():
        raise SyntaxError('Expected EOL')
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)

    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Expected variable name")
        wtok.next()

    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        else:
            wtok.next()
            denominator = factor(wtok, variables)
            if denominator == 0:
                raise EvaluationError('Division by 0')
            else:
                result = result / denominator
    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    function_1 = {"sin": math.sin, "cos": math.cos, "fib": fib, "exp": math.exp, "log": log, "fac": fac}
    function_n = {"sum": sum, "max": max, "min": min, "mean": mean, 'std': std}

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in function_1:
        wtok.next()
        if wtok.get_current() == '(':
            result = function_1[wtok.get_previous()](factor(wtok, variables))
            # Resten av felhanteringen sköts av anropet till factor
        else:
            raise SyntaxError('Expected (')

    elif wtok.get_current() in function_n:
        wtok.next()
        result = function_n[wtok.get_previous()](arglist(wtok, variables))

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
        else:
            raise EvaluationError(f'No variable named {wtok.get_current()}')
        wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -1 * factor(wtok, variables)

    else:
        raise SyntaxError(
            "Expected number or '('")
    return result


def arglist(wtok, variables):
    args = []

    if wtok.get_current() == '(':
        wtok.next()
        args.append(assignment(wtok, variables))
    else:
        raise SyntaxError("Expected (")

    while wtok.get_current() == ',':
        wtok.next()
        args.append(assignment(wtok, variables))

    if wtok.get_current() != ')':
        raise SyntaxError("Expected closing )")
    else:
        wtok.next()
        return args


def fib(n):
    """
    Beräknar n'te talet i Fibonacciserien
    :param n: Heltal n
    :return: n'te fiboanccitalet
    """
    if not n.is_integer() or n < 0:
        raise EvaluationError(f'Fib only accepts positive integer values, at fib({n}) ')

    prev1 = 1
    prev2 = 0

    for i in range(int(n)):
        num = prev1 + prev2
        prev2 = prev1
        prev1 = num
    return prev2  # Returnerar prev2 för råkade räkna ut n+1:te talet


def mean(a):
    '''
    Calculates the mean of list a
    :param a: List of numbers
    :return: Mean of elements in a
    '''
    if len(a) == 0:
        raise EvaluationError("Mean of empty string")
    else:
        return sum(a) / len(a)


def fac(n):
    '''
    Factorial of n with error handling
    :param n:
    :return: Factorial of n
    '''
    if n.is_integer():
        return math.factorial(int(n))
    else:
        raise EvaluationError('Fac only accepts integer values')


def log(n):
    if n > 0:
        return math.log(n)
    else:
        raise EvaluationError('Log only accepts positive values')

def std(a):
    m = mean(a)
    sum = 0
    for elemnt in a:
        sum += (elemnt - m)**2
    sum = sum / len(a)
    return sum**0.5



def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}

    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print('Variables:')
            for key in variables:
                print(f'{key : <8} = {variables[key]}')

        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')


if __name__ == "__main__":
    main()
