from tdd import Calculator

def test_add():
    calc = Calculator()
    assert calc.add (3,4)==7

def test_substract():
    calc = Calculator()
    assert calc.substract(6,3)==3