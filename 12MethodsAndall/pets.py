class Pet:
    

    __slots__ = ['__species','__name','__weight','__fur_color','__age']
    
    def __init__(self,species,name,weight,fur_color,age=0):
        self.__species=species
        self.__name=name
        self.__weight=weight
        self.__fur_color=fur_color
        self.__age=age

    def display_info(self):
        print(self.__species,self.__name,self.__weight,self.__fur_color,self.__age)
    
    def get_species(self):
        return self.__species
    def get_name(self):
        return self.__name
    def get_weight(self):
        return self.__weight
    def get_furcolor(self):
        return self.__fur_color
    def get_age(self):
        return self.__age

    def set_species(self,species):
        self.__species=species
    def set_name(self,new_name):
        self.__name=new_name
    def set_weight(self,weight):
        self.__weight=weight
    def set_furcolor(self,furcolor):
        self.__fur_color=furcolor
    def set_age(self,age):
        self.__age=age
    
    
    


    
    def feed(self,calories):
        pounds = calories/3000
        
        self.__weight=self.__weight + float(pounds)

    def walk(self,miles):
        pounds_lost = (miles * 100) / 3000

        self.__weight=self.__weight - float(pounds_lost)

    #used properly to debug purposes
    def __repr__(self):
        return str(self.__species + self.__name + self.__weight + self.__fur_color + self.__age) 
    
    #str more comfortbale and common to use
    def __str__(self):
        return self.__species,self.__name,self.__weight,self.__fur_color,self.__age
    
    def __eq__(self,other):
        if self.__age==other.__age:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.__age!=other.__age:
            return True
        else:
            return False
    
    def __gt__(self,other):
        #greater than
        if self.__age>other.__age:
            return True
        else:
            return False
        


