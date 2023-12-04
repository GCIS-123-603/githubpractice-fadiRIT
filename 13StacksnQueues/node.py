class Node:

    __slots__ = ['__value','__next']

    def __init__(self,value,next_node=None):
        self.__value = value
        self.__next = next_node

    def get_value(self):
        return self.__value
    def get_nextNode(self):
        return self.__next
    

    def set_nextNode(self,new_next):
        self.__next=new_next





