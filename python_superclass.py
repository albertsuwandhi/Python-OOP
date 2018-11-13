#/usr/bin/env python3

# Object : Attribute and Method
class Hero(object):
    def __init__(self,inputName, inputHealth):
        self.__name = inputName
        self.__health = inputHealth

class Superhero1(Hero):
    def __init__(self,name):
        # Superclass of Superhero1 is Hero
        super().__init__(name,90)

class Superhero2(Hero):
     def __init__(self,name):
        Hero.__init__(self,name,80)

   
Zelda = Hero("Zelda", 100)
print(Zelda.__dict__)
Luigi = Superhero1("Luigi")
print(Luigi.__dict__)
Mario = Superhero2("Mario")
print(Mario.__dict__)







