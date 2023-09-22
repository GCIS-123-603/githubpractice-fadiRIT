#do pytest ./TestingPyTest.py in the powershell in the directory.

def add(x,y):
    return x+y

def test():
    result = add(2,3)
    assert result == 5


def square_area(x):
    return x**2

def test_square_area_8():
    area = square_area(8)
    assert area == 64