import pytest 

class Calculator:
    def add(self, a, b):
        return a + b

# Fixture provides a reusable calculator object
@pytest.fixture
def calc():
    return Calculator()


# Fixture gives Testing Data 
@pytest.fixture(params=[(1,2,3), (0,0,0), (-1,-2,-3)])
def add_case(request):
    return request.param


def test_add(calc, add_case):
    a, b, expected = add_case  # Ref of the Fixture function
    assert calc.add(a, b) == expected

 

 