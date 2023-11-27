
from pets import Pet
from pets import __str__


def main():
    
    my_pet=Pet(species='cat',name='buddy',weight=10,fur_color='red',age='4')

    print(__str__(my_pet))




if __name__ == "__main__":
    main()