
def countdown(start,number): #0

    if start==number:
        print(start)
    else:
        print(start)
        return countdown(start+1,number)

def main():
    countdown(1,50)

main()