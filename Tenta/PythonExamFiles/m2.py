""" Exam tasks for modul 2 for exam 2022-05-30

Exam code:                  Important to fill in this!!!!


"""

import tokenize
from tokenize import TokenError
import io
import math
import time
import random

"""
Interface class to the tokenizer module.
"""
class TokenizeWrapper:
    def __init__(self, line):
        self.line = line
        self.tokens = tokenize.generate_tokens(io.StringIO(line).readline)
        self.current = next(self.tokens)
        self.previous = 'START'

    def __str__(self):
        return self.current[0] + self.current[1]

    def get_current(self):
        if self.current[0] > 0:
            return self.current[1]
        else:
            return 'NO MORE TOKENS'

    def get_previous(self):
        return self.previous

    def next(self):
        if self.has_next():
            self.previous = self.current[1]
            self.current = next(self.tokens)
            return self.current
        else:
            return (0, 'EOS')

    def is_number(self):
        return self.current[0] == 2

    def is_name(self):
        return self.current[0] == 1
    
    def is_string(self):
        return self.current[0] == 3

    def is_newline(self):
        return self.current[0] == 4
    
    def is_comment(self):
        return self.current[0] == 55

    def is_at_end(self):
        return self.current[0] == 0 or self.current[0] == 4 or \
               self.current[1][0] == '#'
               #self.current[0] == 55   # This test doesn't work everywhere
                                        # try to check on '#' instead

    def has_next(self):
        return self.current[0] != 0 and self.current[0] != 4


###################################


def my_log(x):
    if x <= 0:
        raise EvaluationError(f'Illegal argument to log: {x}')
    return math.log(x)


functions_1 = {  # Functions with a single argument
    'sin': math.sin,
    'cos': math.cos,
    'exp': math.exp,
    'log': my_log,   
}
                                       

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    """ See syntax diagram for statement"""
    result = assignment(wtok, variables)
    if wtok.is_at_end() == False:
        raise SyntaxError('Expected end of line')
    return result


def assignment(wtok, variables):
    """ See syntax diagram for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Expected name after '=' ")
        wtok.next()
    return result


def expression(wtok, variables):
    result = term(wtok, variables)
    while wtok.get_current() in ('+', '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    result = factor(wtok, variables)
    while wtok.get_current() in ('*', '/'):  
        op = wtok.get_current()
        wtok.next()
        if op == '*':
            result = result * factor(wtok, variables)
        else:
            try:
                result = result / factor(wtok, variables)
            except ZeroDivisionError:
                raise EvaluationError("Division by zero")
    return result


def parse(wtok, c, aux=''):                          ## Just for convenience
    if wtok.get_current() != c:
        raise SyntaxError(f"Expected '{c}'" + aux)
    wtok.next()


def factor(wtok, variables):
    """ See syntax diagram for factor"""
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        parse(wtok, ')', '')                         ##
            
    elif wtok.get_current() in functions_1:
        func = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            result = functions_1[func](factor(wtok, variables))
        else:
            raise SyntaxError("Missing '(' after function name") 

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(
                f"Undefined variable: '{wtok.get_current()}'")

    elif wtok.is_number():
        result = float(wtok.get_current())                     
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)
        
    else:
        raise SyntaxError(
            "Expected number, word or '('")
    return result


def vars_print(variables):
    for name, value in sorted(variables.items()):
        print(f"   {name:<5} : {value}")
 
    
def main():
    """
    Handles:
       the iteration over input lines,
       the commands 'quit' and 'vars' and
       catches raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    
    init_file = 'm2_init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('\nFrom init file:', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)
        if wtok.get_current() == 'vars':
            vars_print(variables)
        elif wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print(result)
                           
            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"*** Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

                
if __name__ == "__main__":
    main()
