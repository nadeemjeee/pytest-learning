from tdd import Calculator

def test_add():
    calc = Calculator()
    assert calc.add (3,4)==7