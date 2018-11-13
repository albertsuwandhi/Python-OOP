class A():
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(A):
   def show(self):
        print("Show from C")

class D(B,C):
   def show(self):
        print("Show from D")

objectA = A()
objectB = B()
objectC = C()
objectD = D()
objectA.show()
objectB.show()
objectC.show()
objectD.show()
help(objectD)
'''
class D(B, C)
 |  Method resolution order:
 |      D
 |      B
 |      C
 |      A
 |      builtins.object
 '''
