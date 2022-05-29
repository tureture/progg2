"""
File: m2.py
"""

from tokenize import TokenError
import tokenize
import io


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
        # The return value is mainly intended for debugging purposes
        if self.has_next():
            self.previous = self.current[1]
            self.current = next(self.tokens)
            #print('next', self.current[0], self.current[1])
            return self.current
        else:
            return (0, 'EOS')

    def is_number(self):
        return self.current[0] == 2

    def is_name(self):
        return self.current[0] == 1

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


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class SyntaxError(Exception):
    def __init__(self, arg, wtok):
        self.arg = arg
        self.wtok = wtok
        super().__init__(self.arg)


variables = {"ans": 0.0}


def assignment(wtok):
    result = expression(wtok)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
                variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Expected name after '=' ", wtok)
        wtok.next()
    return result


def expression(wtok):
    result = term(wtok)
    while wtok.get_current() in ('+', '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok)
        else:
            wtok.next()
            result = result - term(wtok)
    return result


def term(wtok):
    result = factor(wtok)
    while wtok.get_current() in ('*', '/'):
        op = wtok.get_current()
        wtok.next()
        if op == '*':
            result = result * factor(wtok)
        else:
            try:
                if op == '/':
                    result = result / factor(wtok)
            except ZeroDivisionError:
                raise EvaluationError("Division by zero")
    return result


def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'", wtok)
        else:
            wtok.next()

    elif wtok.get_current() == '|':
        wtok.next()
        result = assignment(wtok)
        if result < 0:
            result = -1 * result
        if wtok.get_current() != '|':
            raise SyntaxError("Expected '|'", wtok)
        else:
            wtok.next()

 
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
        result = -factor(wtok)

    else:
        raise SyntaxError(
            "Expected number, word or '('", wtok)

    if wtok.get_current() == '**':
        wtok.next()
        exponent = factor(wtok)
        if (result == 0 and exponent <= 0) or (result < 0 and not exponent % 1 == 0) :
            raise EvaluationError(f'Illegal operation {result}**{exponent}')
        else:
            result = result ** exponent

    
    return result



def vars_print():
    for name, value in sorted(variables.items()):
        print(f"   {name:<5} : {value}")


def file_name(wtok):
    file = 'test.txt'
    if wtok.is_name():
        file = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '.':
            file += '.'
            wtok.next()
            if wtok.is_name():
                file += wtok.get_current()
    return file


def lines_from_file(wtok):
    wtok.next()
    file = file_name(wtok)
    try:
        with open(file, 'r') as f:
            return(f.readlines())
    except FileNotFoundError:
        print('*** No such file: ', file)
        return []

def statement(input_buffer):
    line = ''
    while True:
        if len(input_buffer) == 0:
            break
        line = input_buffer.pop(0).strip()
        print(f"File  :{line}")
        if len(line) != 0 and line[0] != '#':
            break
        
    if line == '':
        line = input('\nInput : ')
        while line == '':
            line = input("Input : ")
    wtok = TokenizeWrapper(line)
    if wtok.get_current() == 'vars':
        vars_print()
    elif wtok.get_current() == 'quit':
        print('Bye')
        exit()
    elif wtok.get_current() == 'file':
        input_buffer.extend(lines_from_file(wtok))
    else:
        result = assignment(wtok)
        if wtok.is_at_end() == False:
            raise SyntaxError('Expected end of line or an operator', wtok)
        variables['ans'] = result
        print('Result:', result)
   

def main():
    print("Numerical calculator")
    input_buffer = []             # For input lines from file
    while True:
        exception = True
        try:
            var_copy = variables.copy()
            statement(input_buffer)
            exception = False
        except EvaluationError as e:
            print("*** Evaluation error: ", e)

        except SyntaxError as se:
            print("*** Syntax error: ", se)
            print(
                f"Error occurred at '{se.wtok.get_current()}' just after '{se.wtok.get_previous()}'")

        except TokenError as te:
            print('*** Error!')
            print('*** Unbalanced parentheses')

        if exception:
            variables.clear()
            for key in var_copy:
                variables[key] = var_copy[key]


if __name__ == "__main__":
    main()
