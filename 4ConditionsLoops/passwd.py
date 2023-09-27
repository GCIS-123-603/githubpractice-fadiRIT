


def loopbreak():
    password = ""

    while True:
        password = input("Enter your passoword\n")
        if password=="pass":
            print("Accepted!")
            break
            
        else:
            print("Rejected")
    
def main():
    loopbreak()

main()