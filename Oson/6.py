from pprint import pprint
class Avtomobil:
    def __init__(self, markasi: str, modeli: str, yili: int, narxi: float,) -> None:
        self.marka = markasi
        self.model = modeli
        self.yili = yili
        self.narxi = narxi
        
    def get_info(self):
        self.marka = input("avtomobil markasi --> ")
        self.model = input("avtomobil modeli --> ")
        self.yili = int(input("avtomobil yili --> "))
        self.narxi = float(input("avtomobil narxi --> "))

    def malumot(self):
        return f"Avtomobil markasi: ({self.marka}) Modeli: ({self.model}) Narxi: ({self.narxi}) Yili: ({self.yili})"

A = [ 
    Avtomobil("Chevrolet", "Cobalt", 2015, 9000),
    Avtomobil("Toyota", "Corolla", 2008, 7000),
    Avtomobil("BMW", "X5", 2019, 50000),
    Avtomobil("Hyundai", "Accent", 2011, 12000),
    Avtomobil("Ford", "Focus", 2005, 5000)
]

pprint(list(map (lambda i: i.malumot(),\
        filter(lambda i: i.yili >= 2010, A ))))