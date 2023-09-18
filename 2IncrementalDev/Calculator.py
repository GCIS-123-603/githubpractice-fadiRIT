pie = 3.14159


def addition(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a/b

def circu(rad):
    return 2 * pie * rad

def areaof(rad):
    return pie * rad ** 2

def calc():
    a = int(input("Enter the first number.\n"))
    b = int(input("Enter the second number.\n"))
    number_rad = int(input("Enter a radius!\n"))
    
    totaladd = addition(a,b)
    print("Total addition is",totaladd)

    totalsub = subtract(a,b)
    print("Total substraction is",totalsub)

    totalmult = multiply(a,b)
    print("Total multiplication is",totalmult)

    totaldiv = divide(a,b)
    print("Total division is",totaldiv)

    #moving to circle functions

    print("\nThe circumference is",circu(number_rad))
    print("The area is",(areaof(number_rad)))

calc()



    