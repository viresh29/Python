import logging

"""
DEBUG: Detalied information, typically of interest only when diagnosing problems.

INFO: confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or indicative of some problem in the near future 
        (e.g. 'disk space low'). The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able to perform 
       some function.

CRITICAL: A serious error, indicating that the progeam itself may be unable to continue running. 

"""

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

x = 10
y = 5

add_result = add(x,y)
print('Add: {} + {} = {}'.format(x,y,add_result))

sub_result = subtract(x,y)
print('Sub: {} - {} = {}'.format(x,y,sub_result))

mul_result = multiply(x,y)
print('Mul: {} * {} = {}'.format(x,y,mul_result))

div_result = add(x,y)
print('Div: {} / {} = {}'.format(x,y,div_result))
