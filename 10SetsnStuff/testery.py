
list = [1,2,3,4,5,6]
list.reverse()

print(list)


my_names = ["Hey","Hello","There","Here"]    
my_names.reverse()
print(my_names)

mynums = [1,2,3,4,5]
for number in reversed(mynums):
    print(number,end="")

numbers = [34,12,89,5]
sortednum = sorted(numbers, reverse=True)
print(sortednum)



arrayed = [[1,2,3],[4,5,6],[7,8,9]]
print(arrayed[2][2])
#arrayed[2][2] = 200
#print(arrayed[2][2])

rows, cols = (3,3)
arr=[[0]*cols]*rows
print(arr)


for row in arrayed:
    for element in row:
        print(element,end=" ")


