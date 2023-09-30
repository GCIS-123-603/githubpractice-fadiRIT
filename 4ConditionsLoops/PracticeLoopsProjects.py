#This is where I will practice my loops to become even better.
#There will be one main main function, and one main function for testing.
#There will be multiple functions for each program I work on.
'''

LIST OF PROJECTS FOR LOOP LOGIC:

- Countdown Timer : Done

- Multiplication Table: Write a program that generates multiplication tables for numbers from 1 to 10. Use nested loops to accomplish this, with one loop iterating through the numbers and another loop for the multiplication itself.

- Factorial Calculator: Build a program that calculates the factorial of a given number using a for loop. The factorial of a number is the product of all positive integers up to that number (e.g., 5! = 5 x 4 x 3 x 2 x 1).

Print Patterns: Create programs that print various patterns using loops. For example, you can print a right-angled triangle, a square, or a diamond pattern using nested loops.

List Sum and Average: Write a program that calculates the sum and average of a list of numbers. Use a for loop to iterate through the list and accumulate the sum.

Simple Fibonacci Sequence: Generate and print the Fibonacci sequence up to a specified number of terms. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers.

- Guess the Number (Limited Attempts): Modify the number guessing game by giving the player a limited number of attempts (e.g., 3 or 5) to guess the correct number. Use a loop to handle the attempts.

- Print Even and Odd Numbers: Write a program that prints all even or odd numbers within a specified range (e.g., 1 to 100). Use a for loop with conditional statements to check and print the numbers.

Print Prime Numbers: Create a program that prints all prime numbers within a specified range. Use nested loops and conditional statements to determine whether a number is prime.

Password Checker: Develop a program that asks the user to enter a password and checks its strength. You can define different criteria (e.g., length, use of special characters) and use loops to validate the password.

Simple Calendar: Build a basic text-based calendar that displays a given month's calendar, including days of the week and numbered days. Use loops to organize and print the calendar.

Basic Dice Rolling Simulator: Create a program that simulates rolling dice. Allow the user to specify the number of dice and the number of sides on each die. Use loops to generate random rolls and calculate the total.

'''
import random



'''
This small program makes a countdown timer, my main issues started by the following:

The overall logic of the program was simple, and I only had it counting from 0 to 5, rather than a countdown from 5 to 0, so i tried the reversed function and it actually worked!

That is a bit surprising overall, but it's good and works.
'''
def countdownTimer():
    input_time = int(input("Input the time for the countdown."))

    for i in reversed(range(input_time+1)):
        print(i)

'''
This program makes multiplcation table for a certain number, from 1 to 11, i can easily make it specify but its fine and everything worked.
'''
def multiplicationTable():
    inputted_number = int(input("Please enter the number you want the multiplication table for."))

    for i in range(1,11):
        multiplicated = inputted_number*i
        print(f"{inputted_number}x{i} = {multiplicated}")

'''
This program uses nested for loops to make tables from 1 to 10, I got this right from the first try which surprised me a bit, and I'm glad to be improving.
'''
def multiplyAllNumbers():
    first_number = 1

    for i in range(1,11):
        print(f"The table for {i}")

        for x in range(1,11):
            multiplied = first_number*x
            print(f"{i}*{x}={multiplied}")
        
        first_number = first_number+1

'''
this was a bit confusing, and still needs more revision but its mainly because i dont understand how factorials work, but thats fine. still done!
'''
def factorialCalculator():
    #5! = 5*4*3*2*1
    #5! = 120
    #5! = 5*5-1*5-2*5-3*5-4

    inputted_number = int(input("What number would you like the factorial of?"))

    factorial = 1
    for i in range(1,inputted_number+1):

        factorial*=i

        print(factorial)

'''
This was fairly easy to do, just needed to look up the .random library on google to check for syntax, other than that it was great.
'''
def guessTheNumber():
    print("Welcome to Guess The Number! You only get 3 attempts to guess a number between 1 and 10.")

    randomized_number = random.randrange(0,10)
    #print(randomized_number)

    for i in range(1,4):
        inputted_guess = int(input(f"Enter guess #{i}\n"))


        if inputted_guess is randomized_number:
            print("Correct Guess!")
            break
        else:
            print("Wrong!")


    print(f"The correct number was {randomized_number}!")

'''
Easy program, just took time to configure the overall, not much difficulty and was straight forward.
'''
def evenOrOdd():

    ranges_input = input("Enter the ranges like this: '1,100'\n")
    splut_range = ranges_input.split(",")


    for i in range(int(splut_range[0]),int(splut_range[1])+1): #1,100

        print(f"\n{i}")

        if i%2==0:
            print("Even.")
        else:
            print("Odd.")
    
    i+=1
