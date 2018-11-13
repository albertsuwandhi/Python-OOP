class Fruit():
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self):
        return "Class Fruit - REPR"

    def __str__(self):
        return "Class Fruit - STR Magic Method"

    def __add__(self,objek):
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self):
        return "Objek memilik nama dan jumlah"



Apel = Fruit("Apel", 10)
Mangga = Fruit("Mangga", 30)
print(str(Apel))
print(Apel.__dict__)
print(repr(Mangga))
print(Apel + Mangga)


