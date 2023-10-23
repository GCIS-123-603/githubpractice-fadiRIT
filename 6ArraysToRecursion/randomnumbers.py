import random

#randrange(start,stop, step=1) it returns a random integer from the spceified range, and the maximum possbiel value stop is -1. randint(a,b) returns a random integer between a and b (inclusive)
#random() returns a random floating point between 0 and 1

def for_test():
    for _ in range(25):
        number = random.randint(0,100)
        print(number, end=" ")

def arrays_testing1():
    #initiliaze array
    randomlist = []

    for i in range(5):
        randomizednumber = random.randint(0,30)
        randomlist.append(randomizednumber)

    print(randomlist)

