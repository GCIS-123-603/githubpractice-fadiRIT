'''
GCIS-123.603
    Prof. Mehtab Khurshid.

Group 6 : 
    Mohamad Dakwar
    Aamna Fathima Manyar
    Abdullah Alblooshi

This activity is mainly done to test the usage of classes and the proficiency with them. It includes a program that initiates two classes:
    Country : This class has the main information about the country, and it ensures that all variables are kept private. 
        That is why the calling for any attributes is different or of that sort. It also involves the actual calling of the attributes via accessors and mutators.

    HappinessMeter : This class contains the calculation function, which takes the average of all the attributes which are present in the country function. 
        Following that, it returns an average value.

    We are measuring countries on the various input:
        Environment
        Economy
        Culture
        Healthcare
        Education

        Following that, we take the rating itself, add them up, then divide by 5. Thus giving us the average.

    Meaning generally, we have the Country Class which contains the actual class information, while the HappinessMeter calculates the actual happiness to be displayed.

    This program supports dynamic user input as seen, and is able to successfully take a certain amount of countries and print the average happiness for them.


    Encapsulation and private fields have been implemented successfully in both classes.
    



'''

# ?

# Left Empty On Purpose !

# ? 

'''
!   !   !

-   -   -   CORE FUNCTIONS FOR FUNCTIONALITY OF THE PROGRAM BELOW   -   -   - 

!   !   !
'''
#The main country class, it is private and consists of certain attributes listed below. 
#This function employs the usage of accessors and getters.
class Country:
    
    #This is the __slots__ function used for defining certain attributes to be used.
    __slots__ = ["__name","__environment","__economy","__culture","__healthcare","__education"]

    #Constructor function, initialization.
    def __init__(self,name,environment,economy,culture,healthcare,education):
        self.__name = name
        self.__environment =environment
        self.__economy=economy
        self.__culture=culture
        self.__healthcare=healthcare
        self.__education=education

    #Accessors - Gets or allows you to use it.
    def get_name(self):
        return self.__name
    def get_environment(self):
        return self.__environment
    def get_economy(self):
        return self.__economy
    def get_culture(self):
        return self.__culture
    def get_healthcare(self):
        return self.__healthcare
    def get_education(self):
        return self.__education
    
    #Mutators - Literally sets the thing
    def set_name(self,name):
        self.__name=name
    def set_environment(self,environment):
        self.__environment=environment
    def set_economy(self,economy):
        self.__economy=economy
    def set_culture(self,culture):
        self.__culture=culture
    def set_healthcare(self,healthcare):
        self.__healthcare=healthcare
    def set_education(self,education):
        self.__education=education
#HappinessMeter class, it is also private and uses a list to keep track of countries.
class HappinessMeter:

    #This is the __slots__ function that only keeps the countries list.
    __slots__=["__countries"]

    #Constructor for initilization
    def __init__(self):
        self.__countries=[]
    
    #Getter
    def get_countries(self):
        return self.__countries
    
    #Mutator
    def set_countries(self,country):
        self.__countries.append(country)
    
    #This is the measure_happiness() function, that takes various attributes and loops a certain times, then it adds them and divides them to get the average.
    def measure_happiness(self):
        for country in self.__countries:
            average = (country.get_environment()+country.get_economy()+country.get_culture()+country.get_healthcare()+country.get_education())/5
            rounded_average = round(average,2)
            HappinessValues.append(rounded_average)
            

'''
!   !   !

-   -   -   CORE FUNCTIONS FOR FUNCTIONALITY OF THE PROGRAM ABOVE   -   -   -

!   !   !
'''

# ?

# Left Empty On Purpose !

# ? 

'''
| ̅ ̅ ̅   *       *   *       *       *   *       *       *   *       *     ̅ ̅ ̅ |
|                                                                           |
|           *   M A I N     F U N C T I O N     B E L O W   *               |
|                                                                           |
|___     *       *   *       *       *   *       *       *   *       *   ___|
'''

#Initilizing two lists that are used for looping and printing results.
#This list is holding country names
HappinessCountries = [] 

#This list holds country average happiness values
HappinessValues = []
def main():
    

    #How many countries do you want to calculate happiness for?
    country_number = int((input("Enter the number of countries: \t")))

    #Using for loop to repeat a certain amount of times
    for i in range(country_number):
        #Creating an instance of the happiness measure.
        MeterForHappiness = HappinessMeter()


        #Extracting all information needed for the input.
        country_named = input("Enter name of country: \t")

        #Appending the country name to a list, so it can print desired output.
        HappinessCountries.append(country_named)

        country_environment = int(input("Enter environment factor (0-100): \t"))
        country_economy = int(input("Enter economy factor (0-100): \t"))
        country_culture = int(input("Enter culture factor (0-100): \t"))
        country_healthcare = int(input("Enter healthcare factor (0-100): \t"))
        country_education = int(input("Enter education factor (0-100): \t"))

        #Create a country class, and provide it the given information, then carry out calculation.
        country_called = Country(country_named,country_environment,country_economy,country_culture,country_healthcare,country_education)
        MeterForHappiness.set_countries(country_called)
        #Proceed with calculation, and return result
        measured = MeterForHappiness.measure_happiness()

        #Print result.print(f"\n \tAverage Happiness for {country_named} .    .    .", measured)


    #print result from loop

    i=0
    for country_counter in range(len(HappinessCountries)):
        print("Average Happiness For ",HappinessCountries[i],":",HappinessValues[i])
        i=i+1

#Calling main function
main()
