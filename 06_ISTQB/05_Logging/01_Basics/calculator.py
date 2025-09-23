
import logging



def add(a, b):
    logging.info(f"Add function started with a:{a} and b:{b}")
    return a + b 


def subtract(a, b):
    logging.info(f"Sub function started with a:{a} and b:{b}")
    return a - b

def multiply(a, b):
    logging.info(f"Multiply function started with a:{a} and b:{b}")
    return a * b

def divide(a, b):
    logging.info(f"Div function started with a:{a} and b:{b}")
    if b == 0:
        raise ValueError("Cannot be divided by zero")
    return a / b