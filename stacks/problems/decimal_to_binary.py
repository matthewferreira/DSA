import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from stacks.stack import Stack


def decimal_to_binary(num: int):
    """The challenge then is to write an algorithm that will
    read a string of parentheses from left to right and
    decide whether the symbols are balanced."""
    stack = Stack()
    if num < 1:
        return 0

    while num > 0:
        stack.push(num % 2)
        num = num // 2

    bin_str = ""
    while not stack.is_empty():
        bin_str += str(stack.pop())

    return bin_str
