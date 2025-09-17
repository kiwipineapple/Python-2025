def add(a, b):
    _validate_numbers(a, b)
    return a + b


def subtract(a, b):
    _validate_numbers(a, b)
    return a - b


def multiply(a, b):
    _validate_numbers(a, b)
    return a * b


def divide(a, b):
    _validate_numbers(a, b)
    if b == 0:
        raise ValueError('Cannot be divided by zero.')
    return a / b


def _validate_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('Inputs must be numbers')
