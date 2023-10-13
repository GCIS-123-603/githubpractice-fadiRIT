import array as arr



array1 = arr.array('i', [10,20,30,40,50])

length = len(array1)

counter = 0
while counter<length:
    array1[counter] = counter * 2
    
    counter +=1

for i in range(0,len(array1)):
    print(array1[i], end=" ")
