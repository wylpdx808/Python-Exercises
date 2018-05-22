# -*- coding: utf-8 -*-
"""
################################
# CodeWar Basic Math Operators #
################################

Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), 
value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples:

    basic_op('+', 4, 7)         # Output: 11
    basic_op('-', 15, 18)       # Output: -3
    basic_op('*', 5, 5)         # Output: 25
    basic_op('/', 49, 7)        # Output: 7

"""

def basic_op(operator, value1, value2): 
    if operator == '+': 
        return value1 + value2
    elif operator == '-': 
        return value1 - value2 
    elif operator == '*':
        return value1 * value2
    elif operator == '/': 
        return value1/value2 
        
# another solution
def basic_oper(operator, value1, value2): 
    return eval("{}{}{}" .format(value1, operator, value2))
    
print basic_oper('+', 4, 5)