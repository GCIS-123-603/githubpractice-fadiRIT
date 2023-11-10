arrayed = [10,3,5,6,1,4,8,7]


def merge_sort(arr):
    if len(arr)<=1:
        return arr


    #split array into indexed subarays    
    left = arr[0::2]
    right = arr[1::2]

    #recusrively sort them
    left = merge_sort(left)
    right = merge_sort(right)

    #merge them
    return merge(left,right)

def merge(Le,Ri):
    merged = []
    i = j = 0

    #compare each element in the sub array
    while i<len(Le) and j<len(Ri):

        if Le[i] < Ri[j]:
            merged.append(Le[i])
            i=i+1
        else:
            merged.append(Ri[j])
            j=j+1


    while i<len(Le):
        merged.append(Le[i])
        i=i+1
    while j<len(Ri):
        merged.append(Ri[j])
        j=j+1

    return merged

sortedarray = merge_sort(arrayed)

print(sortedarray)
