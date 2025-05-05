def add1(x, y):
    return x + y

def sub1(x, y):
    return x - y

def mul1(x, y):
    return x * y

def div1(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def mod1(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "Error: Modulo by zero is not allowed."

def pow1(x, y):
    return x ** y