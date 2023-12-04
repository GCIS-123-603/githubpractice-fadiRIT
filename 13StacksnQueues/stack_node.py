class Node:
    
    __slots__ = ['__value','__next']
    
    def __init__(self,value=None,next=None):
        self.__value=value
        self.__next=next



class Stack:
    __slots__=["__size","__top"]

    def __init__(self):
        self.__size = 0
        self.__top = None


    def get_size(self,size):
        self.__size = size


    def is_empty(self):
        if self.__size == 0:
            return True
        
        #we can do :
        #return self.__size == 0


    def push(self,value):
        new_node = Node(value)

        new_node.__next=self.__top
        self.__top=new_node

        self.__size += 1 #extension operator

    def pop(self):
        deleted = self.__top.__value
        self.__top=self.__top.__next
        self.__size -= 1

        return deleted


if __name__ == "__main__":
    stack = Stack()

    print(stack.is_empty())
    #print(stack.get_size())


    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.get_size())

    deleted = stack.pop()
    print(deleted)

