import random

def rolltheDice():

    playorNO = input("P to Play, Q to Quit.\n")


    if playorNO != "Q":

        while playorNO:

            print("Welcome to Roll The Dice!\n")
            side_amount = int(input("How many sides would you like your dice to have?\n"))
            roll_amount = int(input("How many times would you like to roll?\n"))

            for x in range(roll_amount):
                for i in range(1):
                    randomstuff = random.randint(1,side_amount)
                    print(f"Dice role #{x+1} : {randomstuff}")
                
            print('Done!')
            
            doneorno = input("Would you like to quit? Y, N\n")

            if doneorno == "Y":
                break
    



def main():
    #rolltheDice()


    print("outside")


main()