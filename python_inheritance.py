#/usr/bin/env python3

# Object : Attribute and Method
class Hero(object):
    def __init__(self,inputName, inputHealth):
        self.__name = inputName
        self.__health = inputHealth
'''
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
'''

class Superhero1(Hero):
    pass

class Superhero2(Hero):
    pass

   
Zelda = Hero("Zelda", 100)
print(Zelda.__dict__)
Luigi = Superhero1("Luigi", 80)
print(Luigi.__dict__)
Mario = Superhero1("Mario",90)
print(Mario.__dict__)







