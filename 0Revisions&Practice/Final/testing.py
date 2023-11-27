'''
Q.1
1.	(10 points) Write a function to calculate the factorial of a given number and return the result. 
1-	Use recursive calls
2-	Raise ValueError if the given number is less than 0.


#factorial function that takes number as parameter
def factorial(number):

    #begin of try statement
    try:
        #base case
        if number==1 or number==0:
            return 1
        
        #checking if number less than 0
        elif number<0:
            raise ValueError("Number Less Than 0!")

        #active factorial taking via recursion
        else:
            return number * factorial(number-1) 
    
    #excepting the value as a var to print our custom cmd
    except ValueError as ve:
        return f"\nError {ve}"

#calling
a = factorial("Hey")
print(a)
'''

'''
Q2

def binary_search(array, low, high, target):
    if high >= low:     # Check base case
        mid = (high+low)//2  # find the middle index

    # If element is present at the middle itself
        if array[mid] == target:           
            return mid
                # If element is smaller than mid, then it can only be present in the left subarray
        elif array[mid] > target:
            return binary_search(array,low,mid+1,target)
        #Else the element can only be present in the right subarray
        else:
            return binary_search(array,mid-1,high,target)
    else:
        # Element is not present in the array
        return -1

arrayed = [i for i in range(1,200)]
a=binary_search(arrayed,0,len(arrayed),23)
print(a)
'''
'''
def reverse(str):

    whatever=""
    for letter in str[::-1]:
        whatever += letter
    
    return whatever

def my_way_reverse(string):

    empty=""
    for letter in reversed(string):
        empty = empty+letter
    return empty


print(reverse("Hello"))
'''


'''
a)	(6 points) Create a class called “BankAccount” for managing bank accounts. 
When a new account is created, it will set a name and balance of a client. 
The name is mandatory, but if no balance is given, the balance should be initialized to 100 as default.

b)	(6 points) Make slots (name, balance) private.


c)	(8 points) In the main, create 2 clients, one with 110, the other with no balance. 
Print their balances. To reach slots, add other necessary methods in BankAccount class.

d)	(4 points) In the BankAccount class, add 2 methods: deposit and withdraw. 
The deposit method allows adding a given amount to the client’s account, 
whereas withdraw deducts a given amount from the available balance.

e)	(4 points) Deposit 50 to the first client and withdraw 20 from the second client. 
Print final balances for each client.

f)	(4 points) Use special method __gt__ to compare 2 clients’ balances and 
return true if the first client’s balance is greater than the second one. 
Then compare and print the result in the main.

g)	(3 points) Use special methods to print all details of a client. Then print client1 information.


'''

class BankAccount:

    __slots__ = ["__name","__balance"]
    
    def __init__(self,name,balance=100):
        self.__name=name
        self.__balance=balance


    def deposit(self,amount):
        self.__balance=self.__balance+amount
    def withdraw(self,amount):
        self.__balance=self.__balance-amount

    def get_name(self):
        return self.__name
    
    def get_balance(self):
        return self.__balance
    
    def set_name(self,name):
        self.__name = name
    
    def set_balance(self,balance):
        self.__balance = balance

    def __gt__(self,person):
        if self.__balance>person.get_balance():
            return True
        else:
            return False
    
    def __str__(self):
        return "name is"+self.__name+"Balance:"+str(self.__balance)



client1 = BankAccount("Mohamad")
client2 = BankAccount("Malak")

client1.deposit(50)
client2.withdraw(20)


#printing balances
print(client1)
print(client2)

print("Comparing results between both client1 and client2",client1>client2)