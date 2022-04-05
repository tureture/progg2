"""
A very small calculator that only handles +, * and ( )

Note that it will give the correct priority to the operations.
Also note the usage of next! Missing call (or to many call)
to next is probbaly the most common problem students have with
the assignment.

You can use the program to see whats happens with incorrect
expressions.

"""

from MA2tokenizer import TokenizeWrapper

def expression(wtok):
    result = term(wtok)
    while wtok.get_current() == '+':
        wtok.next()
        result = result + term(wtok)
    return result

def term(wtok):
    result = factor(wtok)
    while wtok.get_current() == "*":  
        wtok.next()                   
        result *= factor(wtok)
    return result

def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()                  # bypass (
        result = expression(wtok)
        wtok.next()                  # bypass )
    else:                            # should be a number
        result = float(wtok.get_current())
        wtok.next()                  # bypass the number
    return result


def main():
    print("Very simple calculator")
    while True:
        line = input("Input : ")
        wtok = TokenizeWrapper(line)
        if wtok.get_current() == "quit":
            break
        else:
            print("Result: ", expression(wtok))
            
    print("Bye!")
  
if __name__ == '__main__':
    main()
