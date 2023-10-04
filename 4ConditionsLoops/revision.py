'''
- Countdown Timer : Done

- Multiplication Table: Write a program that generates multiplication tables for numbers from 1 to 10. Use nested loops to accomplish this, with one loop iterating through the numbers and another loop for the multiplication itself.

- Factorial Calculator: Build a program that calculates the factorial of a given number using a for loop. The factorial of a number is the product of all positive integers up to that number (e.g., 5! = 5 x 4 x 3 x 2 x 1).

- Guess the Number (Limited Attempts): Modify the number guessing game by giving the player a limited number of attempts (e.g., 3 or 5) to guess the correct number. Use a loop to handle the attempts.

- Print Even and Odd Numbers: Write a program that prints all even or odd numbers within a specified range (e.g., 1 to 100). Use a for loop with conditional statements to check and print the numbers.

Password Checker: Develop a program that asks the user to enter a password and checks its strength. You can define different criteria (e.g., length, use of special characters) and use loops to validate the password.

'''


#Countdown & Countup Timer

def countdown():
    orig_time = 10

    for i in reversed(range(orig_time)):
        print(i)
    
    i=10
    while i>=0:
        print(i)
        i=i-1
    
def multiplication_table():
    selected_num = 5

    i = 0
    while i<=10:
        result = i*selected_num
        print(f"{selected_num} x {i} = {result}")
        i=i+1
    
def all_multiplication():

    multi_second = 0 # second
    multi_first = 0 #first
    i = 0 #increment

    while multi_second<=10:
        
        while multi_first<=10:
            result = multi_first*multi_second
            print(result)
            multi_first=multi_first+1
        
        multi_second=multi_second+1




    


def main():
    #countdown()
    #multiplication_table()
    all_multiplication()











main()