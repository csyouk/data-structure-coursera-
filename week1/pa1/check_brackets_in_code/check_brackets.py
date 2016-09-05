# python3

import sys

opening_brackets_stack = []

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def inspect(text):
    for index, next in enumerate(text):
        if next in ('(', '[', '{'):
            opening_brackets_stack.append(Bracket(next, index+1))

        if next in (')', ']', '}'):
            if len(opening_brackets_stack):
                bracket = opening_brackets_stack.pop()
            else:
                print(index+1)
                return
            # print("bracket: ", bracket.bracket_type, next, bracket.position)
            if not bracket.match(next):
                print(index+1)
                return

    if(not len(opening_brackets_stack)):
        print("Success")
        return

    if(len(opening_brackets_stack)):
        print(opening_brackets_stack.pop().position)
        return



if __name__ == "__main__":
    text = sys.stdin.read()
    # text = "{}"*50000
    inspect(text)
