


'''
def swap(an_array,a,b):
    varT = an_array[0]

    an_array[0] = an_array[1]
    an_array[1] = varT

def shift(an_array):
    for i in range(1,len(an_array)):
        j=i

        while j>0 and an_array[j-1] > an_array[j]:
            an_array[j], an_array[j-1] = an_array[j-1],an_array[j]

            j=j-1
        
    return array

'''
array = [3,1,4,2]
def insertSort(an_array):
    n=len(an_array)

    if n<=1: #if length of array is less than or equal to 1, return array length
        return n
    
    for i in range(1,n): #from 1 to array length (splitting into sorted and unsorted)
        key = an_array[i] #value 1 on index 1
        j=i-1 #the element to the left of i, index 0 value 3


        while j>=0 and key < an_array[j]: #while the j element compared is greater than 0 (meaning not the first, and the key is less than final length)
            an_array[j+1]=an_array[j] #value to the right of j becomes j
            j=j-1   #decrement to end process

        an_array[j+1]=key #the value to the right of j becomes the new key for comparision, rinse and repeat
    return an_array



sorted_array = insertSort(array)
print(sorted_array)
