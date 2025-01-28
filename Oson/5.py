from pprint import pprint

class Dukon:
    def __init__(self, Dukon_nomi: str, manzil, Mahsulot, Ish_vaqti):
        self.dukon_nomi = Dukon_nomi
        self.manzil = manzil
        self.mahsulot = Mahsulot
        self.ish_vaqti = Ish_vaqti

    def get_info(self):
        return f"{self.dukon_nomi} ({self.manzil} - {self.mahsulot}, ish vaqti: {self.ish_vaqti})"

dokon1 = Dukon("Do'kon A", "Toshkent, Chilonzor", "Kiyim-kechak", "09:00 - 20:00")
dokon2 = Dukon("Do'kon B", "Samarqand, Registon", "Elektronika", "08:00 - 18:00")
dokon3 = Dukon("Do'kon C", "Andijon, Bobur", "Qurilish materiallari", "07:00 - 21:00")
dokon4 = Dukon("Do'kon D", "Buxoro, Nodir Devonbegi", "Elektronika", "10:00 - 19:00")
dokon5 = Dukon("Do'kon E", "Namangan, Davlatobod", "Kanzelyariya buyumlari", "08:30 - 17:30")
dokon6 = Dukon("Do'kon F", "Buxoro, Nodir Devonbegi", "Elektronika", "10:00 - 19:00")

d = [dokon1, dokon2, dokon3, dokon4, dokon5, dokon6]
pprint(list(map(lambda i: i.get_info(), \
                filter(lambda i: i.mahsulot == "Elektronika", d))))

