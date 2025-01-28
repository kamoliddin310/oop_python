from pprint import pprint

class Student:
    def __init__(self, talaba_ismi: str, kursi: int, avg: float, stepindeya: float) -> None:
        self.name = talaba_ismi
        self.kurs = kursi
        self.avg = avg
        self.stipendiya = stepindeya
    
    def get_avg(self):
        if self.stipendiya > 1000000:
            return sum(self.avg) / len(self.avg) if len(self.avg) > 0 else 0
        return 0
    
    def is_passing(self) -> bool:
        return self.get_avg() > 80
    
a = Student("Aziz", 2, [80, 90, 75], 1200000)
b = Student("Ali", 2, [30, 40, 20], 700000)
c = Student("Sherbek", 1, [90, 85, 95], 1300000)
d = Student("Asror", 1, [20, 10, 30], 600000)
f = Student("Abror", 3, [20, 10, 30], 555000)
            
g = [            
    {"name": a.name, "average": a.get_avg(), "passing": a.is_passing()},
    {"name": b.name, "average": b.get_avg(), "passing": b.is_passing()},
    {"name": c.name, "average": c.get_avg(), "passing": c.is_passing()},
    {"name": d.name, "average": d.get_avg(), "passing": d.is_passing()},
    {"name": f.name, "average": f.get_avg(), "passing": f.is_passing()},
]
pprint(g)