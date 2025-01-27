class Telefon:
    def __init__(self, nomi, ram, Narx, brand):
        self.nomi = nomi
        self.ram = ram
        self.narx = Narx
        self.brend = brand

    def Kiritish(self):
        return f"Nomi -->{self.nomi}, Ram --> {self.ram}, Narxi --> {self.narx}, Brendi --> {self.brend}"
    
    def ram_filter(self):
        return 2 < self.ram < 8
    
t = Telefon("Samsung Galaxy A10", 3, 150.00, "Samsung")
t2 = Telefon("iPhone 7", 2, 300.00, "Apple")
t3 = Telefon("Xiaomi Redmi Note 8", 4, 200.00, "Xiaomi")
t4 = Telefon("Huawei P30 Lite", 6, 250.00, "Huawei")

for i in [t, t2, t3, t4]:
    if i.ram_filter():
        print(i.Kiritish())
