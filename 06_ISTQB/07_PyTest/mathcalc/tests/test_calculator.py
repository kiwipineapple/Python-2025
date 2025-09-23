import pytest 
from mathcalc.calculator import add, subtract, multiply, divide 




@pytest.mark.parametrize("a,b,expected", [
    (2,3,5),
    (-1,1,0),
    (0,0,0),
    (-10,-20,-30)
])
def test_add(a, b, expected):
    assert add(a,b) == expected




def test_divide_by_zero():
    with pytest.raises(ValueError, match ="Division by zero is not allowed."):
        divide(5 , 0)


# Exercise:  After Code type-down, Write other test cases for subrract, multiply and divide