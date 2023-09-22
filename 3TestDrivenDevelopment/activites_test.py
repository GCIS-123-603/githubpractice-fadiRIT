#testing
def test_square_area_8():
    total = square_area(8)
    assert total == 64

def test_square_area_6():
    total = square_area(6)
    assert total == 36

def test_square_area_neg():
    total = square_area(-2)
    if total<0:
        assert total == None



def square_area(n):
    if n<0:
        print("x")

    return n**2





