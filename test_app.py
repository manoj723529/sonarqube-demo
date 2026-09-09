from app import add, subtract, divide, is_even, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide():
    assert divide(10, 2) == 5

def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False

def test_multiply():
    assert multiply(3, 4) == 12
