import  pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add (3,4)==7

def test_substract(calc):
    assert calc.substract (3,4)==-1

def test_multiply(calc):
    assert calc.multiply (10,2)==20

def test_divide(calc):
    assert calc.divide (10,2)==5

def test_module(calc):
    assert calc.module (10,2)==0
