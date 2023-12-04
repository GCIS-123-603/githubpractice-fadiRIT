
from pets import Pet
from pets import __str__


def main():
    
    my_pet=Pet(species='cat',name='buddy',weight=10,fur_color='red',age=4)
    second_pet = Pet(species='dog',name='buddied',weight=16,fur_color='red',age=5)

    print(my_pet.__eq__(second_pet))
    print(my_pet.__ne__(second_pet))

    print(my_pet.__gt__(second_pet))




if __name__ == "__main__":
    main()