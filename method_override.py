class A():
    def cetak(self):
        print("Ini dari Class A")

class B():
    def cetak(self):
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
objectC.cetak()
help(objectC)
'''
Help on C in module __main__ object:

class C(A, B)
 |  # Class C py karakteristik dari Class A dan B
 |
 |  Method resolution order:
 |      C
 |      A
 |      B
 |      builtins.object
 |
 |  Methods inherited from A:
 |
 |  cetak(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from A:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 '''

