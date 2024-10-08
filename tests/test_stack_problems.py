import pytest
from stacks.problems import (
    balance_parens,
    balance_symbols,
    decimal_to_binary,
    decimal_to_base,
    expressions,
)


def test_balance_parens():
    assert balance_parens.balanced_parenthesis("(()()()())") == True
    assert balance_parens.balanced_parenthesis("(()()(()") == False
    assert balance_parens.balanced_parenthesis("(()()()())") == True


def test_balance_symbols():
    assert balance_symbols.balance_symbols("{ { ( [ ] [ ] ) } ( ) }") == True
    assert balance_symbols.balance_symbols("[ [ { { ( ( ) ) } } ] ]") == True
    assert balance_symbols.balance_symbols("[ ] [ ] [ ] ( ) { }") == True
    assert balance_symbols.balance_symbols("( [ ) ]") == False
    assert balance_symbols.balance_symbols("( ( ( ) ] ) )") == False
    assert balance_symbols.balance_symbols("[ { ( ) ]") == False


def test_decimal_to_binary():
    assert decimal_to_binary.decimal_to_binary(4) == "100"
    assert decimal_to_binary.decimal_to_binary(44) == "101100"
    assert decimal_to_binary.decimal_to_binary(456) == "111001000"
    assert decimal_to_binary.decimal_to_binary(256) == "100000000"


def test_base_to_binary():
    assert decimal_to_base.decimal_to_base(16, 56) == "38"
    assert decimal_to_base.decimal_to_base(16, 7666) == "1DF2"
    assert decimal_to_base.decimal_to_base(16, 4999) == "1387"
    assert decimal_to_base.decimal_to_base(8, 7666) == "16762"
    assert decimal_to_base.decimal_to_base(8, 8765) == "21075"
    assert decimal_to_base.decimal_to_base(8, 256) == "400"
    assert decimal_to_base.decimal_to_base(2, 456) == "111001000"
    assert decimal_to_base.decimal_to_base(2, 256) == "100000000"
    assert decimal_to_base.decimal_to_base(2, 44) == "101100"


def test_infix_to_postfix():
    assert expressions.infix_to_postfix("A*B+C*D") == "AB*CD*+"
    assert expressions.infix_to_postfix("A+B*C+D") == "ABC*+D+"
    assert expressions.infix_to_postfix("(A+B)*(C+D)") == "AB+CD+*"
    assert expressions.infix_to_postfix("A*B+C*D") == "AB*CD*+"
    assert expressions.infix_to_postfix("A+B+C+D") == "AB+C+D+"
