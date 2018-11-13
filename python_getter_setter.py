#/usr/bin/env python3

# Object : Attribute and Method
class Hero(object):
    def __init__(self,inputName, inputArmor, inputHealth):
        self.__name = inputName
        self.__armor = inputArmor
        self.__health = inputHealth

    # Treat as variable
    @property
    def info(self):
        return "Name : {}, Armor : {}, Health :{}".format(self.__name, self.__armor, self.__health) 

    @property
    def health(self):
        pass
    # define setter, getter and deleter ==> use the function name above and use .notation 
    @health.getter
    def health(self):
        return self.__health
    
    @health.setter
    def health(self,x):
        self.__health = x

    @health.deleter
    def health(self):
        self.__health = None

   
Zelda = Hero("Zelda", "Shield", 100)
print(Zelda.__dict__)
print(Zelda.info)
print(Zelda.__dict__)
print(Zelda.health)
Zelda.health =120
print(Zelda.health)
print(Zelda.__dict__)
del Zelda.health
print(Zelda.__dict__)







