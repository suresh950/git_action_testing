from src.math_operation import add, sub

def test_add():
    assert add(2,3)==5
    assert add(4, 1)==5
def test_sub():
    assert sub(1,1) ==0
    assert sub(5,2) ==3
    assert sub(2,4) ==1
