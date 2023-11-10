import array as arr
import random as ran
import time

#Defined Array
array1 = arr.array('i', [10,20,30,40,50])

BrandArray = arr.array('i', [])
#6.1
def printing_array(an_array):
    length = len(an_array)
    for i in range(0,len(an_array)):
        print(an_array[i], end=" ")
def while_fill(an_array):

    length_array = len(an_array)
    counter = 0 

    while counter<length_array:
        an_array[counter] = counter
        
        counter=counter+1
def range_arrays(start,stop,step):
    
    
    for i in range(start,stop,step):
        BrandArray.append(i)
    
    
    #print(BrandArray)
def rollDice(Times,Sides):
    print("Welcome to Roll The Dice ! \n")

    for i in range(1,Times+1):
        randomgen = ran.randint(0,Sides)
        print(f"Attempt #{i} \nThe dice rolled {randomgen}!\n")
def random_array(size,min_value=0,max_valune=None):
    
    InitialArray = arr.array('i',[])

    for i in range(min_value,max_valune):

        number_random = ran.randint(min_value,max_valune)

        InitialArray.append(number_random)
def linearSearch(target,an_array):
    
    for i in range(0,len(an_array)):
        
        if an_array[i] == target:
            return f"Found {target} at index {i}\n"
        elif an_array[i] < 0 or an_array[i]>len(an_array):
            return "Error.\n"








def main():
    #pass
    #rollDice(10,6)
    '''
    begin = time.perf_counter()

    range_arrays(0,10000000,1)
    test = linearSearch(1000000,BrandArray)
    print(test)

    end = time.perf_counter()

    elapsed = end-begin
    print(elapsed)
    '''


    

main()