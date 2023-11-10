
def binarySearch(array,start,end,targetted):
    mid_point = (start+end)//2
    
    if start>end:
        return -1
    
    if array[mid_point]<targetted:
        #print(f"Array mid at {array[mid_point]}, target value is {targetted}")

        return binarySearch(array,mid_point+1,end,targetted)
    elif array[mid_point]>targetted:
        #print(f"Array mid is {array[mid_point]}, and the value is {targetted}")
        return binarySearch(array,start,mid_point-1,targetted)
    
    elif array[mid_point] == targetted:
        return mid_point

    
def main():
    arrD = [20,40,60,80,90,110]


    target = int(input("Enter the target number"))
    answer = binarySearch(arrD,0,(len(arrD))-1,target)
    print(answer)

main()