mainnumber = int(input("Enter the number you'd like to use for your sequence"))

def fibonacciCount(num1):

    for i in range(5):
        total = num1 + num1
        total2 = total + num1
    return total2

print(fibonacciCount(1))







'''
Fibonacci sequence example:
1+1=2
2+1=3
3+2=5
5+3=8
8+5=13
13+8=21

so basically, let's say the starting number and we want to find the nth term

total = num + num
total2 = total + num

'''

