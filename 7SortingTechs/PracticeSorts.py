tested_array = [4,6,3,2,5,9,2,5,4]

def insertSort(an_array):

    lengthArray = len(an_array)

    if lengthArray<=1:
        return lengthArray
    
    for i in range(1,lengthArray):
        key = an_array[i]
        j=i-1

        while j>=0 and key < an_array[j]:
            an_array[j+1] = an_array[j]
            j=j-1

        an_array[j+1] = key

    return an_array

#tested = insertSort(tested_array)
#print(tested)

def merge_sort(arr):
    if len(arr)<=1:
        return arr


    #split array into indexed subarays    
    left = arr[0::2]
    right = arr[1::2]

    print(left)
    print(right)



merge_sort(tested_array)