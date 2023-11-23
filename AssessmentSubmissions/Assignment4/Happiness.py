class Country:
    
    __slots__ = ("Country_Name","Environment","Economy","Culture","Healthcare","Education")


    def __init__(self):
        self.Country_Name = input("Enter Country Name\n")
        self.Environment = int(input("How good is the Enviroment?\n"))
        self.Economy = int(input("How good is the Economy?\n"))
        self.Culture = int(input("How good is the culture?"))
        self.Healthcare = int(input("How good is the healthcare?"))
        self.Education = int(input("How good is the education?"))

        countries_list.append

class HappinessMeter:

    def measure_happiness(selfCountry):
        print("Calculations Calculating . . .")
        country_named = Country()
        added = country_named.Environment + country_named.Economy + country_named.Culture + country_named.Healthcare
        
        return added/2


countries_list = [{},{}]
def main():
    #amount_of_countries = int(input("Enter Number of Countries. . .\n"))



    #country_picked = Country()
    happiness_measurer = HappinessMeter()
    
    measured = happiness_measurer.measure_happiness()
    print(measured)


main()





        
    
        

