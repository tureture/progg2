"""
Interface class to the tokenizer module.

Versions:
2021-03-27: Checking for comments (#) in is_at_end altered since 55 didn't work everywhere
2021-03-01: Comments (#) added
2020-09-05:
"""
import io
import tokenize


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


def main():
    line = 'hello! 123.4 (1e10 ++) - "LAST" #hej hopp'
    w = TokenizeWrapper(line)
    try:
        while w.has_next():
            print(w.get_current(), end='\t')
            if w.is_name():
                print('NAME')
            elif w.is_number():
                print('NUMBER')
            elif w.is_string():
                print('STRING')
            elif w.is_comment():
                print('COMMENT')
            else:
                print()
            w.next()
    except tokenize.TokenError:  # For handling unbalanced parentheses
        print('*** Unbalanced parentheses')
    print('Bye')


if __name__ == '__main__':
    main()
