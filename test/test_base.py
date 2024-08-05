import sys
sys.path.append('..')

from ..src.app.calculator.base import add

def test_number():
    assert add(5, 8) == 4

 