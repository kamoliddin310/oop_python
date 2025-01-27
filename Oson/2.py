class Employee:
    def __init__(self, ism, familiya, maosh):
        self.name = ism
        self.last_name = familiya
        self.maosh = maosh

    def yillik_daromad(self):
        return 12 * self.maosh
    
Xodim = Employee("Layli", "Layliyeva", 200)

print(Xodim.yillik_daromad())