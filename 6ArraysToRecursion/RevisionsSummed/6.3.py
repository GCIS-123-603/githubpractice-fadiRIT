import array as arr



arrayedarray = arr.array('i',[2,4,6,8,10,12,25,62,92])

def countup(start,end):

    if start > end:
        print("0")
    elif start == end:
        print(end)
    else:
        print(start)
        return countup(start+1,end)

def binary_search(an_array,target,start,end): 
    midpoint = (start+end)//2 #index 4, which is 10.
    
    if start>end:
        return -1
    
    if an_array[midpoint]<target: #10 less than 12
        return binary_search(an_array,target,midpoint+1,end)
    elif an_array[midpoint]>target:
        return binary_search(an_array,target,start,midpoint-1)
    elif an_array[midpoint] == target:
        return midpoint
    


def main():
    #countup(0,10)
    h = binary_search(arrayedarray,92,0,len(arrayedarray)-1)
    print(h)


main()