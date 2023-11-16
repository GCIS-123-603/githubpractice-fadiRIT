

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

    def sound(self):
        print(self.name,"says meow!")


my_cat = Cat(name="buddy",age=3)

print("My cat name is", my_cat.name)

my_cat.sound()