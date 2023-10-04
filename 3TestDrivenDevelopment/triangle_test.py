
#1/2 * base * height

def triangle_area(b,h):
    base = abs(b)
    height = abs(h)
    return (1/2)*base*height

def test_triangle_area_0_0():
    assert triangle_area(0,0) == 0

def test_triangle_area_3_4():
    assert triangle_area(3,4) == 6

def test_triangle_area_base_negative():
    assert triangle_area(-3,4) == 6
#abs(num)