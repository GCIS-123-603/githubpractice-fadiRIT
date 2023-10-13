
def countingdown(n):
    if n<0:
        return "Undefined"
    elif n==0:
        return 0

    else:
        print(n)
        return n + countingdown(n-1)

#print(countingdown(5))

def recur_factorial(n):
    if n == 1:
        return n
    if n == 0:
        return "Not valid."
    else:
        return n * recur_factorial(n-1)



print(recur_factorial(5))