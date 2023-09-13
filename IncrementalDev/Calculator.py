


def addition(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a/b


def main():
    a = int(input("Enter the first number.\n"))
    b = int(input("Enter the second number.\n"))
    
    totaladd = addition(a,b)
    print("Total addition is",totaladd)

    totalsub = subtract(a,b)
    print("Total substraction is",totalsub)

    totalmult = multiply(a,b)
    print("Total multiplication is",totalmult)

    totaldiv = divide(a,b)
    print("Total division is",totaldiv)



main()