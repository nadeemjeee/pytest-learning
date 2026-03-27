from calculator2 import add, substract, multiply, divide, module


def test_add():
    
    assert add (3,4)==7

def test_substract():
    
    assert substract (3,4)==-1

def test_multiply():
   
    assert multiply (10,2)==20

def test_divide():
   
    assert divide (10,2)==5

def test_module():
   
    assert module (10,2)==0



