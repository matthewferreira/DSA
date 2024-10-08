import pytest
from stacks.problems import balance_parens, balance_symbols

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
    
