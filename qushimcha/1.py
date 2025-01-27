class Kitob:
    def __init__(self, nom, muallif, narx):
        self.nom = nom
        self.muallif = muallif
        self.narx = narx

    def printBook(self):
        print(f"Kitob nomi: {self.nom}, Muallif: {self.muallif}, Narxi: {self.narx} so'm")

class Kutubxona:
    def __init__(self, nomi):
        self.nomi = nomi
        self.kitoblar = []

    def addBook(self, kitob):
        self.kitoblar.append(kitob)

    def barchaKitoblarniChopEt(self):
        print(f"{self.nomi} kutubxonasidagi kitoblar:")
        for kitob in self.kitoblar:
            kitob.printBook ()

kitob1 = Kitob("O'tgan kunlar", "Abdulla Qodiriy", 50000)
kitob2 = Kitob("Ikki eshik orasi", "O`tkir Hoshimov", 45000)

kutubxona = Kutubxona("Markaziy kutubxona")
kutubxona.addBook(kitob1)
kutubxona.addBook(kitob2)

kutubxona.barchaKitoblarniChopEt()