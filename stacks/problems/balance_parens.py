import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from stacks.stack import Stack


def balanced_parenthesis(test_str: str):
    """The challenge then is to write an algorithm that will
    read a string of parentheses from left to right and
    decide whether the symbols are balanced."""
    stack = Stack()
    for paren in test_str:
        if paren == "(":
            stack.push(paren)
        elif paren == ")":
            stack.pop()
    if stack.is_empty():
        return True
    return False
