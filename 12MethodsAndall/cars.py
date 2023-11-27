class Car:

    __slots__ = ['__VIN','__make','__model','__year','__mileage','__fuel']

    def __init__(self,VIN,make,model,year,mileage,fuel):
        self.__VIN=VIN
        self.__make=make
        self.__model=model
        self.__year=year
        self.__mileage=mileage
        self.__fuel=fuel



    #getters
    def get_VIN(self):
        return self.__VIN
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def get_miles(self):
        return self.__mileage
    def get_fuel(self):
        return self.__fuel

    #setters
    def set_VIN(self,vin):
        self.__VIN=vin
    def set_make(self,make):
        self.__make=make
    def set_model(self,model):
        self.__model=model
    def set_year(self,year):
        self.__year=year
    def set_miles(self,miles):
        self.__mileage=miles
    def set_fuel(self,fuel):
        self.__fuel=fuel

    #methods
    def filler_up(self,gallons):
        if gallons>15:
            return "Cannot fill more than 15."
        else:
            self.__fuel=self.__fuel+float(gallons)

    def drive(self,miles_driven):
        mpg_stuff = float(miles_driven/30)

        if mpg_stuff<self.__fuel:
            self.__mileage=self.__mileage+float(miles_driven)
            #subtract amount of fuel, 30 miles per gallon
            self.__fuel=self.__fuel - mpg_stuff
        else:
            return "Can't Drive!"







myCar = Car("AE-9102","Mercedes","G-Class","2008",10000,6)

a=myCar.drive(179)


print(myCar.get_fuel())
print(myCar.get_miles())


