import pytest
from calculator import Calculator

@pytest.fixture (scope="module")
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2,3)==5

def test_1(calc):
    print("Running test_1")
    assert calc.add(1, 2) == 3

def test_2(calc):
    print("Running test_2")
    assert calc.add(2, 3) == 5

def test_3(calc):
    print("Running test_3")
    assert calc.add(3, 4) == 7