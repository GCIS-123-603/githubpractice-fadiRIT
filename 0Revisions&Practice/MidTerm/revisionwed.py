def draw_star():
    for i in range(1, 6):  # Adjust the range to change the size of the star.
        spaces = " " * (5 - i)  # Calculate the number of spaces before the stars.
        stars = "#" * (2 * i - 1)  # Calculate the number of stars in each row.
        print(spaces + stars)

def PrimeNumCheck():
    flag=0
    num=3
    m=int(num/2)

    if (num==0 or num==1):
        print(num,"is not a prime number!")
    else:
        i=2
        while(i<=m):
            if(num%i==0):
                print(num,"is not prime num")
                flag=1
                break
            i+=1
        if(flag==0):
            print(num,"is a prime number.")

def secondcheck():

    inputtednum = int(input("Which number do you want to check? \n"))

    determine = 0

    if inputtednum==0 or inputtednum==1:
        print("It's not a prime number!")
    elif (inputtednum%2==0):
        print("Not prime number!")
    else:
        print("Prime!")

    #NOT ACCURATE

string="hey123i12dojt"
def checkdigits():
    for i in string:
        if i.isdigit() == True:
            print(i,"is a digit")
        else:
            print(i,"is not digit",end="\nqq    ")


def whiletesting():
    numberCOMP = 0
    
    while numberCOMP<=5:
        if numberCOMP<5:
            print(f"{numberCOMP} is less than 5")
        elif numberCOMP==5:
            print("It is now 5!")
        
        numberCOMP=numberCOMP+1
