from calculator import Calculator
def test_add():
    calc = Calculator()
    assert calc.add (3,4)==7

def test_substract():
    calc = Calculator()
    assert calc.substract (3,4)==-1

def test_multiply():
    calc = Calculator()
    assert calc.multiply (10,2)==20

def test_divide():
    calc = Calculator()
    assert calc.divide (10,2)==5

def test_module():
    calc = Calculator()
    assert calc.module (10,2)==0



