def func_caller(a_func,x):
    print(a_func.__name__)
    result = a_func(x)
    print(result)

def square_it(y):
    return y*y

def double_it(z):
    return z * 2

func_caller(square_it,5)