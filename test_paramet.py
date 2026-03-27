import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize ("a,b, expected",[
    (2,3,5),
    (0,0,0),
    (-2,-2,-4)
])
def test_add(calc,a,b,expected):
    assert calc.add(a,b)==expected

@pytest.mark.parametrize ("a,b,expected", [
    (30,10,20),
    (-30,10,-40),
    (-20,-20,0)
])
def test_substract(calc,a,b,expected):
    assert calc.substract(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[
    (10,3,30),
    (-10,2,-20),
    (-2,-2,4)
])
def test_multiply(calc,a,b,expected):
    assert calc.multiply(a,b)== expected


@pytest.mark.parametrize("a,b,expected", [
    (9,3,3),
    (-30,3,-10),
])
def test_divide(calc,a,b,expected):
    import pytest
    assert calc.divide(a,b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (10,3,1),
    (8,4,0),
    (8,3,2)
])
def test_module(calc,a,b,expected):
    assert calc.module(a,b)== expected