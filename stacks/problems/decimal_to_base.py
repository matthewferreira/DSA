import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from stacks.stack import Stack


def decimal_to_base(base: int, num: int):
    stack = Stack()
    digits = "0123456789ABCDEF"
    while num > 0:
        stack.push(num % base)
        num = num // base

    bin_str = ""
    while not stack.is_empty():
        bin_str += digits[stack.pop()]

    return bin_str
