def string_newline():
    phrase = input("Enter your string!\n")
    phraLength = len(phrase) #length of normal phrase
    phraLen = 0 #init for 0 for increment
    
    phraLen = -1

    for i in range(phraLength):
        phraLen+=1
        print(phrase[phraLen])
    
    print(phrase)

        
    for i in range(phraLength):

        print(phrase[phraLen])
        phraLen-=1




def differentMethod():
    greeting = "Hello World"

    for char in reversed(greeting):
        print(char)

string_newline()