import turtle
import array as arr
import math

array1 = arr.array("i",[1,2,3,4,5,6])



def print_oddEv_array(an_array):

    for i in range(0,len(an_array)):
        if an_array[i]%2==0:
            print(f"Found even number ({an_array[i]}) at index : {i}\n")
        else:
            print(f"\tODD ! Number {an_array[i]} found at index : {i}\n")
def print_odd_recursion(an_array, index=0):
    if index >= len(an_array):
        print("Done")
    elif an_array[index] % 2 != 0:
        print(f"Found odd number at index {index}: {an_array[index]}")
    else:
        print(f"Found even number at index {index}: {an_array[index]}")
    
    if index < len(an_array) - 1:
        print_odd_recursion(an_array, index + 1)

def countdownRedux(number):
    if number<0:
        return 0
    else:
        print(number)
        return number + countdownRedux(number-1)
def factorial(num):

    if num==0:
        return 1
    elif num==1:
        return 1
    else:

        return num * factorial(num-1)

def blowup(number):
    if number<0:
        print(0)
    else:
        return number + blowup(number-1)


def circles(radius,depth):
    
    if depth == 0:
        return 0
    elif depth == 1:
        turtle.circle(radius)
        circumference = ((math.pi)*(radius**2))
        return circumference    
    else:
        turtle.circle(radius)
        arc_circumference = (math.pi * radius * 2) 
        return arc_circumference + circles(radius/2,depth-1)





def main():
    #print_oddEv_array(array1)
    #print_odd_recursion(array1)

    #varred = countdownRedux(10)
    #print(varred)

    #factored = factorial(5)
    #print(factored)

    #blowup(100000)

    heythere = circles(100,5)
    print(f"Circumference is {heythere}")






    
main()