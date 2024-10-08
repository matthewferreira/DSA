import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from stacks.stack import Stack


def infix_to_postfix(expr: str):
    op_stack = Stack()
    operators = "*/+-()"
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    # print(input_str)
    output = []
    for token in expr:
        print(token)
        print(output)
        if token not in operators:
            output.append(token)
        else:
            if token == "(":
                op_stack.push(token)
            elif token == ")":
                while op_stack.peek() != "(":
                    output.append(op_stack.pop())
            else:
                while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]:
                    output.append(op_stack.pop())
                op_stack.push(token)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    result = ""
    for c in output:
        if c not in "()":
            result += c
    return result
