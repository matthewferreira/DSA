import pytest
from stacks.problems import balance_parens

def test_balance_parens():
    assert balance_parens.balanced_parenthesis("(()()()())") == True
    assert balance_parens.balanced_parenthesis("(()()(()") == False
    assert balance_parens.balanced_parenthesis("(()()()())") == True
