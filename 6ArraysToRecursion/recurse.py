
mYArray = [68,10,20,34,52,72,100]

def print_odd(an_array):
    for i in range(0,len(an_array)):
        if mYArray[i]%2==0:
            print(mYArray[i],end=" ")

def recSearch(theArray,index,target):
    if index == -1:
        return -1
    if theArray[index] == target:
        return index
    
    return recSearch(theArray,index-1,target)

def factorial(num):
    if num == 1:
        return num
    elif num<0:
        return "Does not exist"
    else:
        return num * factorial(num-1)

def countdown(num):
    if num==0:
        return 0
    else:
        print(num)
        return 
        
        num + countdown(num-1)








def main():
    ind = len(mYArray)-1
    x=68
    #hey = recSearch(mYArray,ind,x)
    #print(hey)

    #var = factorial(6)
    #print(var)

    var = countdown(10)
    print(var)



main()

