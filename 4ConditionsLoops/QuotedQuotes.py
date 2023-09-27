

def printables():

    print("She said \"I don't like brocolli\"")
    print("A\tB\tC\tD\tE")
    print("This /is\\ /a\\ /test\\")
    print("This is a string with newlines in the middle")

    print("She\t said \"I \\ \ndon't \t like \\ \nbroccoli.\"")

def string_newline():
    phrase = input("Enter your string!\n")
    phraleng = len(phrase) #length of normal phrase
    phraLen = 0 #init for 0 for increment
    

    print(phrase)
    for i in range(phraleng):

        print(f"{phrase[phraLen]}")
        phraLen = phraLen + 1


    print(phrase)
    for i in range(phraleng):
        phraleng = phraleng - 1

        print(f"{phrase[phraleng]}")

def pixelart():
    size = 5
    row = 0

    while row < size:
        col = 0
        while col < size:
            if row == col:
                print('*', end='')
            else:
                print(' ', end='')
            col += 1
        print()
    row += 1



def breakFunction():
    for i in range(1,11):
        if i ==5:
            continue
        print(i)

def main():
    printables()

main()