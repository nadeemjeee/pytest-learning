import pytest
from cal import Calculator

@pytest.fixture
def cal():
    return Calculator()

def test_add(cal):
    assert cal.add(2,3)== 5
