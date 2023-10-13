def power(base, exponent):
    

    if exponent == 0:
        return 1
    elif exponent<0:
        return "This is not allowed."
    else:
        return base * power(base, exponent - 1)



def counting_recursion(n):
    if n<=0:
        print("0")
    else:
        print(n)
        counting_recursion(n-1)

#print("RECURSION COMPLETE, LOOP BEGIN.")

def loop_example(n):


    while n>=0:
        print(n)
        n=n-1

def factorial(num):
    if num == 1:
        print ("1")
    elif num == 0:
        print("0")
    
    else:
        
        new=num #5  
        while new>=1:
            new-1
    

        factorialed = num*(num-1)
        
        return factorial(4)
        


def add(num,stop):
    if num <= 0:
        return "Invalid."
    elif num == stop:
        return num
    else:
        return num + add(num+1,stop)

print(add(1,12))

