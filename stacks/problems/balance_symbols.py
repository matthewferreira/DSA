import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from stacks.stack import Stack


def balance_symbols(test_str: str):
    """The challenge then is to write an algorithm that will
    read a string of parentheses from left to right and
    decide whether the symbols are balanced."""
    stack = Stack()
    test_str = test_str.replace(" ", "")
    for symbol in test_str:
        if symbol in "({[":
            stack.push(symbol)
        else:
            if stack.is_empty():
                return False
            elif not matches(stack.pop(), symbol):
                return False
    if stack.is_empty():
        return True
    return False

def matches(left, right):
    lefts = "({["
    rights = ")}]"
    return lefts.index(left) == rights.index(right)
