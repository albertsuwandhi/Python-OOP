class A():
    def cetak_A(self):
        print("Ini dari Class A")

class B():
    def cetak_B(self):
        print("Ini dari Class B")

# Class C py karakteristik dari Class A dan B
class C(A,B):
    pass

class Team():
    def setTeam(self, team):
        self.team = team
    
    def getTeam(self):
        return self.team

class Type():
    def setType(self, type):
        self.type = type
    
    def getType(self):
        return self.type


class Hero(Team, Type):
    def __init__(self, name, heatlh):
        self.name = name
        self.health = heatlh

objectC = C()
objectC.cetak_A()
objectC.cetak_B()

Zelda = Hero("Zelda",100)
Zelda.setTeam("Nintendo")
Zelda.setType("Attacker")
print(Zelda.getTeam())
print(Zelda.getType())
print(Zelda.__dict__)
