class Bookshop:
    def __init__(self, xaridor_ismi, xaridor_yoshi, kitob_nomi, kitob_narxi):
        self.xaridor_ismi = xaridor_ismi
        self.xaridor_yoshi = xaridor_yoshi
        self.kitob_nomi = kitob_nomi
        self.kitob_narxi = kitob_narxi

    def get_price(self):
        return f"Xaridor yoshi --> {self.xaridor_yoshi}\nXaridor ismi --> {self.xaridor_ismi}\nKitob nomi --> {self.kitob_narxi}\nChegirma --> {self.kitob_narxi*(100 - self.xaridor_yoshi)// 100}"

a = Bookshop("Anna", 21, "Salomnat", 10000)

print(a.get_price())

# self.kitob_narxi*(100 - self.xaridor_yoshi)// 100