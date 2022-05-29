"""
Solutions to exam tasks for module 2
Name:
Code:
"""
from tokenize import TokenError
import math
import io
import tokenize

"""
Interface class to the tokenizer module.
"""


class TokenizeWrapper:
    def __init__(self, line):
        # Quick fix to handle input lines like "  ? "
        line = line.replace(' ', '')
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

    def has_next(self):
        return self.current[0] != 0 and self.current[0] != 4


variables = {}


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg


def assignment(wtok):
    result = expression(wtok)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Expected name after '=' ")
        wtok.next()
    return result


def expression(wtok):
    result = term(wtok)
    while wtok.get_current() in ('+', '-'):
        op = wtok.get_current()
        wtok.next()
        trm = term(wtok)
        if op == '+':
            result += trm
        else:
            result -= trm
    return result


def term(wtok):
    result = factor(wtok)
    while wtok.get_current() in ('*', '/', '%'): #<<<< Task A3
        op = wtok.get_current()
        wtok.next()
        fact = factor(wtok)
        if op == '*':
            result *= fact
        else:
            try:
                if op == '/':        # Task A3
                    result /= fact   # Task A3
                else:                # Task A3
                    result %= fact   # Task A3
            except ZeroDivisionError:
                raise EvaluationError(f'Division of {result} by zero')
    return result


def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok)
        if wtok.get_current() == ')':
            wtok.next()
        else:
            raise SyntaxError("Expected ')'")
    elif wtok.get_current() == '-':
        wtok.next()
        result = - factor(wtok)

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(f"Undefined variable: {wtok.get_current()}")
    else:
        raise SyntaxError("Expected '(', '-', number or name")
    return result


def main():
    print("Calculator version of 2021-08-26")
    input_buffer = []  # For input lines from file
    try:
        with open('init.txt', 'r') as f:
            input_buffer.extend(f.readlines())
    except FileNotFoundError:
        print('*** No init file: ')
    source = 'init'
    while True:
        try:
            line = ""
            while True:
                if len(input_buffer) == 0:
                    break
                templine = input_buffer.pop(0)
                print(f'{source}  :', templine, end='')
                if templine.strip() != '' and templine.strip()[0] != '#':
                    line = templine
                    break
            if line == '':
                line = input('Input : ')
                while line == '' or line.strip()[0] == '#':
                    line = input("Input : ")

            wtok = TokenizeWrapper(line)

            if wtok.get_current() == 'quit':
                break
            elif wtok.get_current() == 'clear':    #<<<<<<<<<<<< Task A4
                variables.clear()                  #<<<<<<<<<<<< Task A4
            else:
                result = assignment(wtok)
                if wtok.is_at_end():
                    print('Result: ', result)
                else:
                    raise SyntaxError('Unexpected token')

        except SyntaxError as se:
            print("*** Syntax: ", se.arg)
            print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")
        except TokenError:
            print('*** Syntax: Unbalanced parentheses')
        except EvaluationError as ee:
            print("\nEvaluationError: ", ee.arg)

    print('Bye!')


if __name__ == "__main__":
    main()
