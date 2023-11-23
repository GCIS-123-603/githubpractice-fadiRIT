class Country:
    
    __slots__ = ("Country_Name","Environment","Economy","Culture","Healthcare","Education")


    def __init__(self):
        self.Country_Name = input("Enter Country Name\n")
        self.Environment = int(input("How good is the Enviroment?\n"))
        self.Economy = int(input("How good is the Economy?\n"))
        self.Culture = int(input("How good is the culture?"))
        self.Healthcare = int(input("How good is the healthcare?"))
        self.Education = int(input("How good is the education?"))

        Country_Names.append(self.Country_Name)




class HappinessMeter:

    def measure_happiness(selfCountry):
        print("Calculations Calculating . . .")
        country_named = Country()
        added = country_named.Environment + country_named.Economy + country_named.Culture + country_named.Healthcare
        
        return added/2


Country_Names = []

def main():

    how_times = int(input("How many countries?"))

    for i in range(how_times):
        instance_country = HappinessMeter()
        
        instance_country.measure_happiness()
    
    print(Country_Names)

main()