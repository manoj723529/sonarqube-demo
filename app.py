def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(n):
    return n % 2 == 0

def multiply(a, b):
    result = a * b

if __name__ == "__main__":
    print(add(5, 3))
    print(subtract(10, 4))
    print(divide(20, 4))
    print(is_even(6))
