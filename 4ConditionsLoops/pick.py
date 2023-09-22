

def check_guess(guess,answer):
        

    if guess is answer:
        return 0 #that means its correct
    elif guess > answer:
        return abs(answer-guess)
    elif guess < answer:
        return abs(answer-guess)


    


print(check_guess(5,6))

def test_check_guess_too_high():
    assert check_guess(3,7) == 7-3

def test_check_guess_correct():

    if check_guess(5,5) is 0:
        print("Working")
    else:
        print("Error!")