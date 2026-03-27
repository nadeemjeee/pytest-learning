import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize ("a,b, expected",[
    (0, 0, 0),
    (-5, 3, -2),
    (1000000, 2000000, 3000000)
])
def test_add(calc,a,b,expected):
    assert calc.add(a,b)==expected

@pytest.mark.parametrize ("a,b,expected", [
    (0, 0, 0),
    (3, 5, -2),
    (-5, -3, -2)
])
def test_substract(calc,a,b,expected):
    assert calc.substract(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[
    (0, 100, 0),        # zero
    (-2, 3, -6),        # negative
    (-2, -3, 6)        # double negative
])
def test_multiply(calc,a,b,expected):
    assert calc.multiply(a,b)== expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (-10, 2, -5),
    (10, -2, -5)
])
def test_divide(calc,a,b,expected):
    import pytest
    assert calc.divide(a,b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (8, 3, 2),
    (-8, 3, 1),
    (8, -3, -1),
    (-8, -3, -2)
])
def test_module(calc,a,b,expected):
    assert calc.module(a,b)== expected

